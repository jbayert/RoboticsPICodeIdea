#import each peripheral but keep them named seperate
from Peripherals.peripheral1 import peripheral as p1
from Peripherals.peripheral2 import peripheral as p2

class Peripheral(object):#basic header to store variables

    
    def setup(self):
        #setup both peripherals
        p1.setup()
        p2.setup()
    def loop(self):
        #loop variables go here
        p1.loop()
        p2.loop()


#footer needed at each component
peripheral = Peripheral()