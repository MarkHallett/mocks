# alib.py

class Alib(object):
    def __init__(self):
        print 'In Alib.__init__'
        self.a_connected = False #eg database
        self.b_connected = False #eg url
        self.c_connected = False #eg file
        self.a = self.b = self.c = None
        self.rtn = None

    def _connect_to_source_a(self):
        #connect to source_a, eg databse
        print 'connecting to source a'
        self.a_connected = True


    def _get_a(self):
        if self.a_connected == True:
            # get value from source
            return 4
        else:
            self._connect_to_source_a()
            return self._get_a()


    def _connect_to_source_b(self):
        #connect to source_a, eg url
        self.b_connected = True


    def _get_b(self):
        if self.b_connected == True:
            # get value from source
            return 5
        else:
            self._connect_to_source_b()
            return self._get_b()

    def _connect_to_source_c(self):
        #connect to source_c, eg file
        self.c_connected = True


    def _get_c(self):
        if self.c_connected == True:
            # get value from source
            return 6
        else:
            self._connect_to_source_b()
            return self._get_b()



    def collect_values(self):
        self.a = self._get_a()
        self.b = self._get_b()
        self.c = self._get_c()

    def combine(self):
        self.rtn = self.a + self.b + self.c

    def get_value(self):
        # eg do common formatting etc
        return self.rtn


class Connection(object):                                                        
    def execute(self):                                                           
        return "Connection to server made"
    def execute2(self):                                                           
        return "Connection to server made2"