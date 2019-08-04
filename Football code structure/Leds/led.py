class Led(object):#basic header to store variables
    def setup(self):
        #setup variables go here

        #set LED's color
        self.color = "blue"

        print("LEDs Setup, color:",self.color)

    def loop(self):
        #loop variables go here


        print("LEDs Loop",self.color)
        
        self.color = "green"#update color

#footer needed at each component
led = Led()