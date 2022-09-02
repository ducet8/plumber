import datetime
import hashlib
import importlib
import os


def execute(section, module):
    mod = f'{section}_modules.{module}'
    source = importlib.import_module(mod)
    source.source_def()


def generate_sku(pipe):
    _hash = hashlib.new('sha256')
    _hash.update(pipe['name'].encode())
    _hash.update(pipe['content'].__str__().encode())
    _hash.update(str(datetime.datetime.now()).encode())
    return _hash.hexdigest()


def main(trigger, action):
    if validate_module('trigger', trigger) and validate_module('action', action):
        execute('trigger', trigger)
        execute('action', action)


def process_new_pipe(pipe):
    # TODO: Add endpoint
    # TODO: Create key and rename configuration using it
    # TODO: Move configuration from staging to pipes
    # TODO: Should each pipe be a file or all in one json?
    sku = generate_sku(pipe)


def startup_check():
    for config in os.listdir('./staging'):
        if verify_is_yaml(config) or verify_is_json(config):
            # TODO: Validate syntax
            # TODO: Convert to standard - json?
            process_new_pipe(config)


def validate_module(section, module):
    if f'{module}.py' in os.listdir(f'{os.getcwd()}/{section}_modules'):
        return True
    else:
        return False


def verify_is_json(filename):
    if filename.lower().endswith('.json'):
        return True
    else:
        return False


def verify_is_yaml(filename):
    if filename.lower().endswith('.yml') or filename.lower().endswith('.yaml'):
        return True
    else:
        return False


if __name__ == '__main__':
    # main('trigger2', 'action1')
    startup_check()