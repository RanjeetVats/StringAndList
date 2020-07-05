#check key is valid or not

 user_key=input("Enter key to be verifyied")
if user_key in d.keys():
    print("key is present")
    print("value:",d[user_key])
else:
    print("key is not valid")
