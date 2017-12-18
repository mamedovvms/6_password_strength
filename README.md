# Password Strength Calculator


The program checks the reliability of the password.
Outputs a number from 1 to 10, where 1 is very weak, 10 is very reliable


#Functions

def get_password_strength(password) - function returns a number as an indicator of the reliability of the password.
The passphrase is passed as a parameter in the form of a string

The function checks several parameters occurrence of letters of the lower and upper registers,
numbers, special symbols. Checking the length of the password and checking for matches with a
phone number or with an email address


You can import the function
from password_strength import get_password_strength

#Example

1.Password: 123
  Security 1

2.Password: Qx23asdfHK2$ale
  Security 10


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
