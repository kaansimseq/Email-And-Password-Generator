import random 
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
letter_list = lower + upper + num

poor = lower + upper
average = lower + upper + num
advance = lower + upper + num + symbols

print("\t********** E-mail & Password Generator **********\t")

choose1 = int(input("\nPlease select the mail extension:\n1)@hotmail.com\n2)@gmail.com\n"))

while True:
    chars = int(input("Please enter how much chars you want before e-mail, between 4 and 20 max:\n"))
    if(chars < 4 or chars > 20):
        print("Please enter between 4 and 20 chars max!!!")
    else:
        break    

email_format = ["@hotmail.com","@gmail.com"]
letter_list_to_str = "".join(letter_list)
e_mail1 = "".join(random.choices(letter_list_to_str, k=chars)) + email_format[0]
e_mail2 = "".join(random.choices(letter_list_to_str, k=chars)) + email_format[1]

if choose1 == 1:
    print("E-Mail =",e_mail1)
elif choose1 == 2:
    print("E-Mail =",e_mail2)    

choose = int(input("Please select the strength of the password:\n1)Poor\n2)Average\n3)Advance\n"))
lenght = int(input("Please enter the lenght of password:\n"))

if choose == 1: 
    temp = random.sample(poor, lenght)
    password = "".join(temp)

elif choose == 2: 
    temp = random.sample(average, lenght)
    password = "".join(temp)

elif choose == 3:
    temp = random.sample(advance, lenght)
    password = "".join(temp)

print("Password =",password)