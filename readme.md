# random-password

Generate random strings with python's random module.

## Help

```
usage: main.py [-h] [-a] [-A] [-d] [-l LENGTH] [-n NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  -a, --ascii-lowercase
                        abcdef... (default: False)
  -A, --ascii-uppercase
                        ABCDEF... (default: False)
  -d, --digits          12345... (default: False)
  -l LENGTH, --length LENGTH
                        length of a generated string (default: 4)
  -n NUMBER, --number NUMBER
                        generate specified number of strings (default: 5)

```

## Examples

```bash
$ python main.py
8709
0555
0421
0074
2744

$ python main.py -aAd -l 20 -n 3
JrSn3YoNSk1QKY9e3KIV
ZDpDtXVUXjdKHVwOVf28
tcqWixMeGCfc7p8dG9a1
```
