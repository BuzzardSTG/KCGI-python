print("hoj")

def myFunc():
    #statement1
    #statement2
    print("this is the stement that belongs into the  myAction()")

def myAnotherFunction():
    pass

def myFunctionWhichTakesAFewArguments(name, surname, age):
    if(surname == "Wick"):
        print(f"Hi {surname}, {name}, I have heard that you are {age} y.o.")
    elif(surname == "Parker"):
        print(f"Hi Parker, Daily is waiting for pictures \n BRING THEM NOWWW!!!!!")
print("ok")

myFunctionWhichTakesAFewArguments("John","Parker", 35)
def myFunctionWhichTakesNArguments(parameters=()): #default value (empty
    if len(parameters) ==0:
        print("No given argument")
    elif len(parameters)>0:
        print("item")
