import json 
import os
from rewrite_json import rewrite

dirname = os.path.dirname(__file__)

path = os.path.join(dirname, "history/silicon_valley_ex.json")

with open(path) as f:
   data = json.load(f)

rewrite(1, data, "1", "2", "updated interaction 1", "updated interaction 2")

rewrite(2, data, "1", "2", "updated interaction next", "updated interaction next next")

print(json.dumps(data, indent=1))