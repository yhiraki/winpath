#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from enum import Enum, auto


class PathType(Enum):
    POSIX = auto()
    WINDOWS = auto()
    ANY = auto()
    NONE = auto()


def detect(path):
    for i, c in enumerate(path):
        if i == 1 and c == ':':
            return PathType.WINDOWS
        if c == '\\':
            return PathType.WINDOWS
        if c == '/':
            return PathType.POSIX
    return PathType.ANY


def to_windows(path):
    return path.replace('/', '\\')


def to_posix(path):
    return path.replace('\\', '/')


def convert(path, method):
    return method(path)


def convert_static(path, to_type, mappings):
    for mapping in mappings:
        for a, b in mapping, reversed(mapping):
            if (path.startswith(a['prefix']) and b['type'] == to_type):
                return path.replace(a['prefix'], b['prefix'])
    return path


CONFIG_NAME = '.winpathrc.json'
CONFIG_PATHS = [
    f'{__file__}/../config/{CONFIG_NAME}',
    f'./{CONFIG_NAME}',
    f'~/{CONFIG_NAME}',
]


def load_config(config_path):
    return json.load(config_path)


methods = {
    PathType.WINDOWS: to_windows,
    PathType.POSIX: to_posix,
    PathType.ANY: lambda x: x
}

to_defaults = {
    PathType.WINDOWS: PathType.POSIX,
    PathType.POSIX: PathType.WINDOWS,
    PathType.ANY: PathType.ANY
}


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-t', '--to-path', dest='t', metavar='dest',
                        choices=[i.name.lower() for i in PathType])
    parser.add_argument('path')
    args = parser.parse_args()

    mappings = []
    for path in CONFIG_PATHS:
        p = Path(path).expanduser().resolve()
        if p.exists():
            with p.open('r', encoding='utf-8') as f:
                config = load_config(f)
                if not config.get('inherit'):
                    mappings = []
                for m in config['mappings']:
                    ml = []
                    for i in m:
                        ml.append(dict(
                            type=PathType[i['type'].upper()],
                            prefix=i['prefix'],
                        ))
                    mappings.append(ml)

    to_path = None
    if args.t:
        to_path = PathType[args.t.upper()]
    else:
        to_path = to_defaults[detect(args.path)]

    method = methods[to_path]

    ret = convert_static(args.path, to_path, mappings)
    ret = convert(ret, method)

    sys.stdout.write(str(Path(ret).expanduser()))


if __name__ == '__main__':
    main()
