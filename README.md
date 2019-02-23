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

[+] Get HTML data from URL .. 
[+] Checking from all tags html
[+] Indentification html Response .. 
[+] Unescape html indentified   aaaaaaa"checkxss true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa> true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa< true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa( true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa) true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa! true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa% true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa@ true
 [-->] Posible Parameter in URL  keywords  
 
[+] Unescape html indentified   aaaaaaa'checkxss true
 [-->] Posible Parameter in URL  keywords  
 
[+] Checking Xss Payload ... 
[+] Unescape html indentified   aaaaaaa<script>alert("xss found") true
 [-->] Posible Xss Parameter in URL Found  https://web.id/browse?keywords=aaaaaaa<script>alert("xss found");</script> 
 
[+] Unescape html indentified   aaaaaaa"><script>alert("xss found") true
 [-->] Posible Xss Parameter in URL Found  https://web.id/browse?keywords=aaaaaaa"><script>alert("xss found");</script> 
 
[+] Unescape html indentified   aaaaaaa<script>alert('xss found') true
 [-->] Posible Xss Parameter in URL Found  https://web.id/browse?keywords=aaaaaaa<script>alert('xss found');</script> 
 
[+] Unescape html indentified   aaaaaaa'><script>alert('xss found') true
 [-->] Posible Xss Parameter in URL Found  https://web.id/browse?keywords=aaaaaaa'><script>alert('xss found');</script> 
 
[+] Total request  14
[-] Request Success  14
[-] Error Request  0
[!] Process end with time 0:00:08.765309
```


### Sensitif Data Detection

```sh
$ python apps.py  -u 'https://web.com' -m info
[INFO] Checking information form server ...

 [+] Web Server Found  nginx/1.14.1 
 [Advice] Hardening your servers  
 [+] Backend Technology Found  PHP/5.6.38 
 [Advice] Hardening your servers  

[INFO] Checking Critical URL .. 

 [WARNING] Critical link found  https://web.id/.env 
 [WARNING] Critical link found  https://web.id/.git/config 
 [WARNING] Critical link found  https://web.id/phpmyadmin 
 [WARNING] Critical link found  https://web.id/artisan 
 [WARNING] Critical link found  https://web.id/.htaccess 
 [WARNING] Critical link found  https://web.id/robot.txt 
 [WARNING] Critical link found  https://web.id/db.sq 

[INFO] Scanning Port Server  https://web.id  ..

[-->] Scanning IP :  xx.xx.xx.xx
 [WARNING] FTP connection is open, Posible to brute force, Version  Pure-FTPd 
 [WARNING]  230 Anonymous user logged in 
drwxr-xr-x    2 0          0                   6 Dec 23  2015 .
drwxr-xr-x    2 0          0                   6 Dec 23  2015 ..
ls command execute  226-Options: -a -l 
226 2 matches total

```

&copy; [Rahmat Wahyu Hadi](https://github.com/wahyuhadi/) - 2019-02-20
