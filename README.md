# winpath

## Usage

```console
$ winpath '\path\to\windows\dir'
/path/to/windows/dir
```

## Installation

```console
$ pip install git+https://github.com/yhiraki/winpath
```

## Configuration

```json
{
  "mappings": [
    [
      {
        "type": "windows",
        "prefix": "C:"
      },
      {
        "type": "posix",
        "prefix": "/mnt/c"
      }
    ]
  ]
}
```

```console
$ winpath 'C:\to\windows\dir'
/mnt/c/to/windows/dir
```
