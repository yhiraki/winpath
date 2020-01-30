# winpath

Convert Windows and POSIX path each other.

## Usage

```console
$ winpath '\path\to\windows\dir'
/path/to/windows/dir
```

```console
$ winpath '\\192.168.0.10\share'
smb://192.168.0.10/share
```

## Installation

```console
$ pip install git+https://github.com/yhiraki/winpath
```

## Configuration

If you add custom mappings, create `~/.winpathrc.json`.

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

### Mount Samba file and open file on MacOS

```console
$ open $(winpath '\\192.168.0.11\share\sample.pptx')
```
