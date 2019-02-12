from threading import Thread
from time import sleep

def func_1():
    pass
    def func_2(fi):
        sleep(10)
        print(fi)
        return fi
    f = [1,2,3]
    first = 0
    t = Thread(target=func_2,args=(first))
    t.run()
    list = [1,2,3,4,5]
    list_2 = []
    l_1 = [i for i in list if i%2]
    print(l_1)

func_1()