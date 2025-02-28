
points=int(input("how much points? "))
if 1<=points<=200 :
    if 1<=points<=50:
        print("Congratulations! You won a wooden rabbit!")
    elif 51<=points<=150:
        print("Oh dear, no prize this time.")
    elif 151<=points<=180:
        print("Congratulations! You won a wafer-thin mint!")
    elif 181<=points<=200:
        print("Congratulations! You won a penguin!")   
else:
    print("the points must be btween 1:200 !")    
