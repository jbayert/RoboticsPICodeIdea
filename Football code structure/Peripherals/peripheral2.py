class Peripheral(object):#basic header to store variables

    
    def setup(self):
        #setup variables go here
        print("Peripheral 2 Setup")
    def loop(self):
        #loop variables go here
        print("Peripheral 2 Loop")


#footer needed at each component
peripheral = Peripheral()