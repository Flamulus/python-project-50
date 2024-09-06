import json
import yaml


def parse_json(path):
    return json.load(open(path))


def parse_yaml(path):
    return yaml.safe_load(open(path))


PARSERS = {
    'json': parse_json,
    'yml': parse_yaml,
    'yaml': parse_yaml,
}


def parse_files(*paths):
    files = []
    for path in paths:
        extension = path.split('.')[-1]
        if extension in PARSERS:
            files.append(
                PARSERS[extension](path)
            )
        else:
            files.append({})
    return files
