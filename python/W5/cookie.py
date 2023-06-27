#user_input = input("Please insert a string value:")
#print(f"The inserted string has been: {user_input}")

# we want program which is going to ask for the input "cookie", until we will give the program the "cookie" it will bother us

cookie = " "
while(cookie != "cookie"):
    cookie = input("Hey you! Give me the cookie! Now!\n")
    if(cookie == "secret"):
        break
    #if(cookie == "continue"):
    #    print("nice try...")
    #    continue #last statement - nothing we can skip
else:
    print("Thank you for the cookie bro")

for question in range(15):
    input(f"\n Question # {question}\n")