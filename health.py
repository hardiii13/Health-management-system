import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercises and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("hardik-ex.txt","a") as f:
                f.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here\n")
            with open("hardik-food.txt","a") as f:
                f.write(str([str(gettime())])+ ":"+value+"\n")
            print("successfully written")
    elif(k==2):
        c=int(input("ENter 1 for exercises and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("guy2-ex.txt","a") as f:
                f.write(str([str(gettime())]) + ":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value=input("type here\n")
            with open("guy2-food.txt","a") as f:
                f.write(str([str(gettime())]) + ":"+value+"\n")
            print("successfull writtten")
    elif(k==3):
        c=int(input("ENter 1 for exercises and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("guy3-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("guy3-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ":" + value + "\n")
            print("successfull writtten")
    else:
        print("please enter valid input((1.Hardik,2.guy2,3.guy3)")
def retrieve(k):
    if(k==1):
        c=int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("hardik-ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif(c==2):
            with open("hardik-food.txt") as f:
                for i in f:
                    print(i,end=" ")
    elif(k==2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("guy2-ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif (c == 2):
            with open("guy2-food.txt") as f:
                for i in f:
                    print(i, end=" ")
    elif(k==3):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("guy3-ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif (c == 2):
            with open("guy3-food.txt") as f:
                for i in f:
                    print(i, end=" ")
    else:
        print("please enter valid input((1.Hardik,2.guy2,3.guy3)")

print("Health Management system ")
a=int(input("Press 1 to lock the values and 2 for retrieve"))
if a==1:
    b=int(input("press 1 for hardik 2 for guy2 and 3 for guy3"))
    take(b)
else:
    b=int(input("press 1 for hardik 2 for guy2 and 3 for guy3"))
    retrieve(b)
