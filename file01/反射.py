import sys
class Websever(object):
    def __init__(self,host,port):
        self.host=host
        self.port=port
    def start(self):
        print('Server is starting')
    def stop(self):
        print('Stop is starting')
    def restart(self):
        self.start()
        self.stop()
def test_run(self,name):
    print('running....',name,self.host)
if __name__=="__main__":
    server=Websever('localhost',3000)
    server2=Websever('localhost',4000)
    if hasattr(server,sys.argv[1]):
        func=getattr(server,sys.argv[1]) #获取server.start 的内存地址
        func()