# Password Strength Calculator


The program checks the reliability of the password.
Outputs a number from 1 to 10, where 1 is very weak, 10 is very reliable


#Functions

```bash
def get_password_strength(password)
``` 
- function returns a number as an indicator of the reliability of the password.
The passphrase is passed as a parameter in the form of a string

The function checks several parameters occurrence of letters of the lower and upper registers,
numbers, special symbols. Checking the length of the password and checking for matches with a
phone number or with an email address


You can import the function
from password_strength import get_password_strength

#Example
The script requires an installed Python interpreter version 3.5 for its work.

Run on Linux:
```bash
$ python password_strength.py
  Please enter your password: # when you enter the password will not be displayed
  
  #123
  Password complexity 4 out of 10
  
  #Ghjnbdjufp2!
  Password complexity 10 out of 10   
```

Running on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
