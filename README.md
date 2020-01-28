# winpath

## Usage

```
$ winpath '\path\to\windows\dir'
/path/to/windows/dir
```

## Configuration

```
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

```
$ winpath 'C:\to\windows\dir'
/mnt/c/to/windows/dir
```
