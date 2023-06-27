import sys # has lot of constants in it

def main():
    try:
        x = int('foo')
        #x = 5 % 0
        #print(x)
        #x = 5 / 3
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Do not divide or modulo by zero')
    except:
        # default except as we do not know what kind of error expect
        print(f'Unknown error: {sys.exc_info()[1]}')
    else:
        # this will only be executed if i don't have an error
        print('good job!')
        print(x)

if __name__ == '__main__': main()