print("welocome to our shop")
size=input("enter the size  s small m for midiam l for larg: ").lower()
piprony=input("do you want a piprony y for yes n for no: ").lower()
cheese =input("do you want extra cheese  y for yes n for no:  ").lower()

pill=0

if size=="s":
    pill+=15
    if piprony=="y":
        pill+=2
elif  size=="m"  :
    if piprony=="y":
        pill+=3    
    pill+=20
elif  size=="l": 
    if piprony=="y":
        pill+=3    
    pill+=25
if cheese == "y" :
    pill+=1    

print(f"your pill is {pill}$")