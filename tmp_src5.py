import json
from pathlib import Path
nodes={n['id']:n for n in json.loads(Path('.pudim/theory/theory.graph.json').read_text(encoding='utf-8-sig'))['nodes']}
for nid,n in nodes.items():
    if not nid.startswith('T-not-') or n.get('status')!='true':
        continue
    target='T-'+nid[6:] if nid.startswith('T-not-') else None
    tgt=nodes.get(target)
    if not tgt or tgt.get('status')!='open':
        continue
    if any('source' in t for t in tgt.get('tags',[])):
        print(f"{target}\t{','.join(tgt.get('tags',[]))}\t{nid}")
