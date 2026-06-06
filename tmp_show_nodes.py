import json
from pathlib import Path
ids={
'"'T-Qi-hlambda-degree4-conjecture-open'"':'Qi hlambda degree4',
'"'T-Bessel-I-sqrt-log-concavity-nu-ge-0'"':'Bessel sqrt log-concavity',
'"'T-Bessel-I-Riccati-log-concavity-inequality'"':'Bessel Riccati log-concavity inequality',
'"'T-Bessel-I-ratio-quadratic-bound'"':'Bessel ratio quadratic bound',
'"'T-Bessel-I-split-regime-log-concavity-certificate'"':'Bessel split-regime certificate'
}

nodes={n['id']:n for n in json.loads(Path('.pudim/theory/theory.graph.json').read_text(encoding='utf-8-sig'))['nodes']}
for nid in ids:
 n=nodes[nid]
 print('\n##',nid)
 print('statement:',n['statement'])
 print('normalized:',n['normalized_statement'])
 print('tags:',','.join(n.get('tags',[])))
 print('refs:',n.get('truth_basis',{}).get('artifact_refs'))
