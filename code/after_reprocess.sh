#!/bin/bash
# Steps after the parallel reprocessing shards finish: remap decisions, second pass, arXiv re-pass, queue status.
set -e
cd "$(dirname "$0")/.."
. .venv/bin/activate
REPORT=${1:-/Users/admin/.claude/jobs/5f500ff7/tmp/parse_v4_report.json}
STEMS=$(python3 -c "import json; r=json.load(open('$REPORT')); print(' '.join(x['stem'] for x in r if x['new'] is not None and x['new']!=x['old']))")
python3 code/carry_over_verdicts.py $STEMS
python3 code/remap_decisions.py $STEMS
sleep 16
SKIP_GBOOKS=1 SKIP_DBLP=1 ONCE=1 SHARD=p2 python3 code/second_pass.py 2>&1 | tail -n 40
ONCE=1 python3 code/arxiv_repass.py 2>&1 | tail -n 40
python3 code/adjudicate.py status | head -3
