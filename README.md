# Automatic Security Testing

Fitur 
  - Xss Attack Detection
  - Sensitif Information
  
### Installation
Install python 3.x.x

```sh
$ git clone https://github.com/wahyuhadi/AutoSecurity-Check.git
```

# How To Use
```sh
$ python apps.py -h
```
### Xss Detection

```sh
$ python apps.py  -u 'https://web.com/browse?keywords=aaaaaaa' -m xss -t all
```

### Sensitif Data Detection

```sh
$ python apps.py  -u 'https://web.com' -m info
```

&copy; [Rahmat Wahyu Hadi](https://github.com/wahyuhadi/) - 2019-02-20
