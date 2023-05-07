import platform
def main():
    message()

def message():
    print(f'This is python version {platform.python_version()}')

if __name__ == '__main__': main()