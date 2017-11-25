# crypt_passwd

Is a simple wrapper around the [passlib](https://passlib.readthedocs.io/en/stable/index.html) library. 
It prompt you for a password and display the encrypted version.

## Get started

```bash
$ crypt_passwd 
Enter password: 
Retype new password: 
$6$rounds=656000$62S97YpG1zdqvU04$DqdMO9dcfyQfCBk7ne4pkQMn3/8BDx6k.bC1c2owWDF/D8TCMMe9nya5jsGGLZMGeyTaTr5r2TkrnZJQjBsbc0
```  
The password is never display in clear.

The available algorithms are: 'bcrypt', 'sha256', 'sha512' (default), 'argon2', 
 'pbkdf2_sha256', 'pbkdf2_sha512'

If you do not provide a password *crypt_passwd* will generate one for you.
In this case you can control either the strength or the length of the password.
 
```bash
$ crypt_passwd  --strength secure --algo sha256
Enter password (return => will generated a password for you.) : 
ER?cC!lTk2
$5$rounds=535000$FmJaZVQtmZID4IVU$QFfdVDxvRLNuCDXCDuE9SSpI8masx8txAQZmhrW2Vj4
```
Of course, in this case, the password is displayed in clear on the console.

## Installation

*crypt_passwd* requires python >= 3.3

### pip method

```bash
python3 -m pip install git+git://github.com/freeh4cker/crypt_passwd.git#egg=crypt_passwd
```
