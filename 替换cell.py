import os
import json

from sympy import false

rootpath = 'abupy_lecture'
for fn in os.listdir(rootpath):
    fpath = os.path.join(rootpath, fn)
    if os.path.isfile(fpath) and fn.endswith(".ipynb"):
        print(fpath)

        with open(fpath, 'r', encoding='utf-8') as f1:
            d = json.loads(f1.read())

        d['cells'] = d['cells'][1:-1]

        with open(fpath, 'w', encoding='utf-8') as f2:
            f2.write(json.dumps(d, indent=1, ensure_ascii=0))
