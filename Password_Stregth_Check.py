"""
Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 
●       Implement a Python function called check_password_strength that takes a password string as input.
●       The function should check the password against the following criteria:
○       Minimum length: The password should be at least 8 characters long.
○       Contains both uppercase and lowercase letters.
○       Contains at least one digit (0-9).
○       Contains at least one special character (e.g., !, @, #, $, %).
●       The function should return a boolean value indicating whether the password meets the criteria.
●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
●       Provide appropriate feedback to the user based on the strength of the password.  
"""

def check_password_strengt(pwd):
    specialCharacter = "!@#$%"
    
    length = len(pwd)
    has_upper_case = any(char.isupper() for char in pwd)
    has_lower_case = any(char.islower() for char in pwd)
    has_digit = False
    has_special_character = False

    #check if pwd has digits
    for char in pwd:
        if char.isdigit():
            has_digit = True


    #Check if pwd has special characters
    for char in specialCharacter:
        if char in pwd:
            has_special_character = True  

    #to check the length of the password
    if length < 8 or not has_upper_case or not has_lower_case or not has_digit or not has_special_character:
        return False
    else:
        return True

def main():
    pwd = input("Enter your password : ")
    if check_password_strengt(pwd):
        print("Great!, you have entered valid password")
    else:
        print("""
The password you entered should have the following : 
   1. has minimum 8 characters 
   2. has at least one upper case 
   3. has at least one lower case 
   4. has at least one digit 
   5. has these special character "! @ # $ %"
              """)
        
if __name__ == "__main__":
    main()