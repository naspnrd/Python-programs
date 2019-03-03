name =input("enter your name:")
age = int(input("How old are you, {0} ".format(name)))
if age >= 18 and age < 31 :
    print("You are welcome for holidays, {0}".format(name))
else:
    print("sorry, you are under age")
    
