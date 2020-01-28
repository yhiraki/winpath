# winpath

Convert Windows and POSIX path each other.

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

- `~/.winpathrc.json`

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

## Examples

### Mount and open file on MacOS

```json
{
  "mappings": [
    [
      {
        "type": "windows",
        "prefix": "\\192.168.0.11"
      },
      {
        "type": "posix",
        "prefix": "smb://192.168.0.11"
      }
    ]
  ]
}
```

```console
$ open $(winpath '\\192.168.0.11\share\sample.pptx')
```
