#/usr/local/bin/python3
#直接调用
import threading
import time

def sayhi(num):
	print('running on number:%s'%num)
	time.sleep(3)
if __name__ == '__main__':
	# t1=threading.Thread(target=sayhi,args=(1,))
	# t2=threading.Thread(target=sayhi,args=(2,))
	# t1.start()   #启动线程
	# t2.start()   #又启动一个
    t_list=[]
    for i in range(10):
        t=threading.Thread(target=sayhi,args=[i,])
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()
    print('main')