class Peripheral(object):#basic header to store variables

    
    def setup(self):
        #setup variables go here
        print("Peripheral 1 Setup")

        #create a variable
        self.motor_pos = 0
    def loop(self):
        #loop variables go here
        print("Peripheral 1 Loop, motor position:",self.motor_pos)

        self.motor_pos +=1#change position


#footer needed at each component
peripheral = Peripheral()