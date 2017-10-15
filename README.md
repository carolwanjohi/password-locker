# Password Locker
## This is a Python application that allows a user to generate and store passwords for various accounts., 13/20/2017

## By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
This is a Python application that allows a user to generate and store passwords for various accounts. The application runs on the terminal and the user navigates through the app by using short codes. <br/>
The short codes are:
* cu - create Password Locker account
* du - display the names of the current Password Locker users
* lg - log into Pasword Locker account
* cc - storing an existing log in credential
* dc - display credentials for the logged in user
* cg - storing a credential with a generated password
* ex - exit for Password Locker account and also exit the terminal app

## User Stories
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Create an account | User Name : John <br/> Password : doe | An account is created |
| Display account names | N/A | Display a list of user names for Password Locker accounts |
| Log into an account | User Name : John <br/> Password : doe | Log into the users account |
| Store existing log in credential | Account : Githib <br/> Password : doe1 | Create and save the user's credentials | 
| Display a specific users credentials | N/A | List of the user's credentials | 
| Generate a password for a new credential | Account : Password Locker | Generate a password for the user. <br/> Create and save the user's credential with the generated password | 
| Log out | N/A | Log out of Password Locker account |

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* Clone [this repository](https://github.com/carolwanjohi/password-locker.git) and run the `run.py` file.

## Known Bugs

No known bugs

## Technologies Used
- Python3.6

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**

