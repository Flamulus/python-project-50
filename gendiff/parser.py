import json
import yaml


PARSERS = {
    'json': json.load,
    'yml': yaml.load,
    'yaml': yaml.load,
}


def parse_files(*paths):
    files = []
    for path in paths:
        extension = path.split('.')[-1]
        if extension in PARSERS:
            files.append(
                PARSERS[extension](open(path))
            )
        else:
            files.append({})
    return files
