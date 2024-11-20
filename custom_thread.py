from threading import Thread
class CustomThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={},Verbose=None):
        #Initializing the thread class
        Thread.__init__(self,group,target,name,args,kwargs)
        self._return = None

    #Using function over writing, overwriting a Thred.run function
    def run(self):
        if self._target is not None:
            self._return=self._target(*self._args,**self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return
    