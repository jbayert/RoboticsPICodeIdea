#First import defualt parameters
from BackgroundCode.ValpoRobot import *

#Pick a drive train by uncommenting it
from DriveTrains.basic_drive_train import drive
#from DriveTrains.omni_drive_train import drive

#Pick a peripheral  by uncommenting it
#peripheral = Empty()
#from Peripherals.peripheral1 import peripheral
#from Peripherals.peripheral2 import peripheral
from Peripherals.peripheral1and2 import peripheral

from Leds.led import led

from time import sleep

class main(Robot):
    def setup(self):
        #set up variables needed change these next few lines to update settings.
        self.motor_type = "Bag"#set the motor type
        self.a = 1

        #run setups from components
        drive.setup(self.motor_type)
        peripheral.setup()
        led.setup()


        print("")#print blank line

    def loop(self):
        print("Main Loop: ", self.a)
        self.a +=1

        #run loop on the components
        drive.loop()
        peripheral.loop()
        led.loop()

        print("")#print blank line

        #slow down loop
        sleep(2)

main().run()#loops the code with some magic
