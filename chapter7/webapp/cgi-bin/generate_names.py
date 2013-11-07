import json
from athletemodel import get_names_from_store
import yate
import cgitb

cgitb.enable()

names = get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))