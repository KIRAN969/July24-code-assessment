import time,threading,logging
logging.basicConfig(filename='Execution.log',level=logging.INFO)
try:
    
    def findodd(mylist):
        for i in mylist:
            time.sleep(2)
            if i%2!=0:
                print("odd=> ",i)
    def findeven(mylist):
        for i in mylist:
            time.sleep(2)
            if i%2==0:
                print("even=> ",i)
    if(__name__=='__main__'):

        list1=[12,2,15,6,9,8]
        t1=threading.Thread(target=findodd,args=(list1,))
        t2=threading.Thread(target=findeven,args=(list1,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("*****")
        logging.info("even and odd numbers are printed")
except Exception:
    logging.error("something went wrong")
finally:
    print("completed")
