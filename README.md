# OOCR

### Installation

```shell
$ docker  docker build -t oocr:1.0 .
```

### Using

```shell
$ docker run -d --name oocr -p 5010:80 oocr:1.0
```

### API

- `/identify/file`
   - file: binary image

- `/identify/url`
  - url: image url
  - response：result、headers、cookies