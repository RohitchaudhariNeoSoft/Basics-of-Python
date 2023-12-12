from time import sleep
from threading import *
class hello(Thread):
    def run(self):           ## Inbuilt function of Thread
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):               ## Inbuilt function of Thread
        for i in range(5):
            print("Hii")
            sleep(1)


t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)   ## To stop collision of threading
t2.start()

t1.join()       ## beacause of this "bye" will print at the end
t2.join()
print("bye")   ## Printing by Main Thread
