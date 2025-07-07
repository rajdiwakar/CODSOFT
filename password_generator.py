import string
import random

try:
    pass_generator =  int(input("Enter the password length : "))
    
    if pass_generator < 4 :
        print(" Password lenght should be at least 4 characters.")

    else:
        
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

            
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        print("Your password is :")
        print("".join(random.sample(s,pass_generator)))
        
except ValueError:
     print("Invalid input. Please enter a number.")        
    
