import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f() # do the stuff defined in the passed function (in this case (big_sum())
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper

@elapsed_time # decorator takes big_sum() and wrappe it with elapsed_time() function
def big_sum():
    num_list = []
    for num in (range(0, 1000000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum() # so here we call only big_sum(), but as output we get also elapsed time which is not mentioned within the big_sum() body at all -> it's defined in the wrapper elapsed_time() function

if __name__ == '__main__': main()