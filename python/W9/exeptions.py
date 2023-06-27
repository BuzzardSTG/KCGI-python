try:
    #here we try to realize implemented code
    #print(x)
    print("This is not problematic statement")
except NameError:
    #here we say what should be happening if an error occurs
    #print(x) #NameError: name (x) is not defined
    print('Something wrong with the name(s).')
except ValueError:
    print("Something wrong with value(s).")
except:
    print("Something went wrong with opening file.")
else:
    #this will be only happening if there will be no error