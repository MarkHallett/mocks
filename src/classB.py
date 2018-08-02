# classB.py

#import alib
from alib import Alib

class B(object):
    def __init__(self):
            print 'In B.__init__'
            self.a = Alib()


    def dowork(self):
        self.a.collect_values()
        self.a.combine()
        x = self.a.get_value()
        return x
