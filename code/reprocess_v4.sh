#!/bin/bash
# Reprocess the papers whose parse changed under parser v4: back up old parses, re-parse + re-verify, remap decisions,
# rerun the second pass and the arXiv re-pass for those files, and print the new adjudication queue size.
set -e
cd "$(dirname "$0")/.."
. .venv/bin/activate
REPORT=${1:-/Users/admin/.claude/jobs/5f500ff7/tmp/parse_v4_report.json}
STEMS=$(python3 -c "import json,sys; r=json.load(open('$REPORT')); print(' '.join(x['stem'] for x in r if x['new'] is not None and x['new']!=x['old']))")
echo "stems to reprocess: $(echo $STEMS | wc -w | tr -d ' ')"
mkdir -p data/refs_v3
for s in $STEMS; do [ -e data/refs_v3/$s.verified.json ] || cp data/refs/$s.verified.json data/refs_v3/$s.verified.json; done
SKIP_DBLP=1 python3 code/reprocess.py $STEMS 2>&1 | tail -n 80
python3 code/remap_decisions.py $STEMS
sleep 16
SKIP_GBOOKS=1 SKIP_DBLP=1 ONCE=1 python3 code/second_pass.py 2>&1 | tail -n 5
ONCE=1 python3 code/arxiv_repass.py 2>&1 | tail -n 5
python3 code/adjudicate.py status | head -3
