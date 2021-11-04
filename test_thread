import threading
import time, random


def t1():
    for i in range(5):
        print('a')
        time.sleep(random.random())
        
        
        

def t2():
    for i in range(5):
        print('b')
        time.sleep(random.random())
        
        
        
def main():
    threading.Thread(target=t1).start()
    threading.Thread(target=t2).start()
    print('main loop fin')
    
    

main()
