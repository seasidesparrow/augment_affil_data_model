import json
import os
from glob import glob
from jsonschema import validate
from referencing import Registry, Resource


schema_path = os.path.abspath('./affil_schema')

class LoadResolverException(Exception):
    pass


class LoadSchemaException(Exception):
    pass


class ValidationTool(object):

    def __init__(self):
        try:
            schema_loc = os.path.join(schema_path,'AugmentedAffil.json')
            with open(schema_loc,'r') as fs:
                self.schema = json.load(fs)
            self.registry = Registry()
        except Exception as err:
            raise LoadSchemaException('problem loading schema: %s' % err)

    def test(self, data):
        try:
            validate(instance=data,
                     schema=self.schema,
                     registry=self.registry)
        except Exception as err:
            return ('Validation failed:\n\tError: %s' % (err))
        else:
            return ('Validation passed')


def main():

    test_dir = os.path.abspath('./test_data')
    test_files = glob(test_dir+'/*.json')
    try:
        validator = ValidationTool()
    except Exception as err:
        print('Cannot validate, problem loading schema: %s' % err)
    else:
        for f in test_files:
            print('\n\n\n\n\nTesting file %s' % f)
            with open(f, 'r') as fj:
                print(validator.test(json.load(fj)))

if __name__ == '__main__':
    main()
