import json
import os

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from settings import BASE_DIR


def validate_data(filename):
    with open(os.path.join(BASE_DIR, 'schema.json'), "r") as f:
        sc = json.loads(f.read())

    with open(os.path.join(BASE_DIR, filename), "r") as f:
        op = json.loads(f.read())

    try:
        validate(op, sc)
    except ValidationError as e:
        return "Not valid: {}".format(e)
    else:
        return "Valid"
