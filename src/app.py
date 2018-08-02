# app.py

import classB

def run():
    myb = classB.B()
    x = myb.dowork()
    print 'x = ', x


if __name__ == '__main__':
    run()