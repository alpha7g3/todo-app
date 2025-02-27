
password= input("enter password:")
pas= {}

if len(password) >= 8:
    pas["length"] = True
else:
    pas["length"] = False



digit = False
for i in password:
   if i.isdigit() :
       digit = True

pas["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

pas["upper"] = upper

print(pas)

if all(pas.values()):
    print("strong password")
else:
    print("weak password")