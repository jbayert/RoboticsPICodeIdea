class Drive(object):#basic header to store variables

    
    def setup(self,motor_type):
        #setup variables go here

        #pass the variable through as save it for the loop. Otherwise it is reset when the loop ends
        self.motor_type = motor_type

        print("Omni Setup, motor type: ", self.motor_type)
    def loop(self):
        #loop variables go here
        print("Omni Loop, motor type: ", self.motor_type)
        

#footer needed at each component
drive = Drive()