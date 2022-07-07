# num1=int(input("enter number 1"))
# num2=int(input("number 2"))
# try:
#
#     res=num1/num2
#     print(f"result{res}")
# except Exception as e:
#
#     num2=int(input("enter number 2"))
#
#     # try:
#     #     print(num1/num2)
#     # except Exception as e:
#     #     print(e)
#
# finally:
#
#     print("hello world")
#


# age=int(input("enter num1"))
#
# if(age<18):
#     raise Exception("not eligible")
# else:
#     print("eligible")

phone_number=(input("enter your phone number"))

if len(phone_number)!=10:
    raise Exception("enter your correct phone number")
else:
    print("aprooved")