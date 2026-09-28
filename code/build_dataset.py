"""Assemble the per-paper dataset from OpenReview pulls + the conference site CSVs.

Outputs data/dataset/papers.csv (one row per submission) and data/dataset/replies.jsonl (one row per reply).
"""
import json, glob, os, re, csv, collections
import pandas as pd

def val(c, k):
    v = (c or {}).get(k)
    return v.get('value') if isinstance(v, dict) else v

def load_forums():
    forums = {}
    for f in sorted(glob.glob('data/openreview/forums/chunk_*.json')) + sorted(glob.glob('data/openreview/forums2/*.json')):
        d = json.load(open(f))
        for fid, notes in d['forums'].items():
            if isinstance(notes, list): forums[fid] = notes      # later (throttled) pulls overwrite earlier ones
    return forums

def main():
    subs = json.load(open('data/openreview/submissions_by_venueid.json'))
    forums = load_forums()
    rows, replies = [], []
    for group, notes in subs.items():
        for n in notes:
            c = n['content']
            r = {'forum_id': n['id'], 'number': n['number'], 'group': group.split('/')[-1], 'title': val(c, 'title'),
                 'pdf': val(c, 'pdf'), 'authors': '; '.join(val(c, 'authors') or []) if val(c, 'authors') else None,
                 'keywords': '; '.join(val(c, 'keywords') or []), 'license': n.get('license'), 'cdate': n.get('cdate'),
                 'has_supp': bool(val(c, 'supplementary_material'))}
            rep = forums.get(n['id'])
            r['replies_pulled'] = rep is not None
            ai_scores, human_scores, corr_score = {}, [], None
            rw_comment, corr_comment, decision = None, None, None
            if rep:
                for x in rep:
                    if x['id'] == n['id']: continue
                    inv = (x.get('invitations') or ['?'])[0].split('/-/')[-1]
                    sig = (x.get('signatures') or ['?'])[-1].split('/')[-1]
                    xc = {k: val(x['content'], k) for k in x['content']}
                    replies.append({'forum_id': n['id'], 'number': n['number'], 'reply_id': x['id'], 'invitation': inv, 'signature': sig,
                                    'cdate': x.get('cdate'), 'content': xc})
                    if inv == 'Official_Review' and sig.startswith('Reviewer_AIRev') and sig[-1].isdigit():
                        ai_scores[sig[-1]] = xc.get('overall')
                    elif inv == 'Official_Review' and sig == 'Reviewer_AIRevCorrectness':
                        corr_score = xc.get('overall')
                    elif inv == 'Official_Review' and sig.startswith('Reviewer_'):
                        human_scores.append(xc.get('overall'))
                    elif sig == 'Reviewer_AIRevRelatedWork':
                        rw_comment = xc.get('comment')
                    elif sig == 'Reviewer_AIRevCorrectness':
                        corr_comment = xc.get('comment')
                    elif inv == 'Decision':
                        decision = xc.get('decision')
            r.update({'airev1': ai_scores.get('1'), 'airev2': ai_scores.get('2'), 'airev3': ai_scores.get('3'),
                      'human_score': human_scores[0] if human_scores else None, 'n_human_reviews': len(human_scores),
                      'correctness_score': corr_score, 'decision': decision,
                      'related_work_check': rw_comment is not None, 'rw_flagged_examples': None, 'correctness_check': corr_comment is not None})
            if rw_comment:
                ex = re.findall(r'^\s*[-*]\s+(.+)$', rw_comment, flags=re.M)
                r['rw_flagged_examples'] = json.dumps(ex)
                r['rw_n_examples'] = len(ex)
                r['rw_says_all_verified'] = bool(re.search(r'no hallucinated references detected|all (of the )?references (were|could be|are) verified', rw_comment, re.I))
            rows.append(r)
    os.makedirs('data/dataset', exist_ok=True)
    df = pd.DataFrame(rows)
    # merge the conference-site metadata (autonomy, topics, site scores) by forum id
    site = pd.read_csv('data/a4s_site/papers_with_ids.csv').drop_duplicates('paper_id')
    site['forum_id'] = site.link.str.extract(r'id=([A-Za-z0-9_-]+)')
    site = site.rename(columns={'AIRev1_score': 'site_airev1', 'AIRev2_score': 'site_airev2', 'AIRev3_score': 'site_airev3', 'Human_score': 'site_human', 'status': 'site_status'})
    df = df.merge(site[['forum_id', 'paper_id', 'site_airev1', 'site_airev2', 'site_airev3', 'site_human', 'site_status', 'hypothesis_development', 'experimental_design', 'data_analysis', 'writing', 'primary_topic', 'secondary_topic']], on='forum_id', how='left')
    df.to_csv('data/dataset/papers.csv', index=False)
    with open('data/dataset/replies.jsonl', 'w') as f:
        for r in replies: f.write(json.dumps(r) + '\n')
    print('papers', len(df), '| replies pulled for', int(df.replies_pulled.sum()), '| replies', len(replies))
    print('groups:', df.group.value_counts().to_dict())
    print('site merge: paper_id present for', int(df.paper_id.notna().sum()))
    pulled = df[df.replies_pulled]
    print('related-work check present:', int(pulled.related_work_check.sum()), 'of', len(pulled), '| with flagged examples:', int((pulled.rw_n_examples.fillna(0) > 0).sum()))
    # sanity: OpenReview scores vs site scores
    both = pulled.dropna(subset=['airev1', 'site_airev1'])
    if len(both): print('airev1 agreement with site csv:', float((both.airev1.astype(float) == both.site_airev1.astype(float)).mean()))
    print(pulled[['number', 'group', 'airev1', 'airev2', 'airev3', 'human_score', 'correctness_score', 'decision', 'rw_n_examples']].head(8).to_string())

if __name__ == '__main__':
    main()
