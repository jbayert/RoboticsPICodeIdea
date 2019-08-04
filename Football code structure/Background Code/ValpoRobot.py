#do not edit this program
#This creates the basic structure that creates the enviroment

from time import sleep

class Robot(object):
    #This is the standard setup function to be overriden
    def setup(self):
        pass
    def loop(self):
        pass
    def on_error(self):
        pass
    def run_once(self,should_setup = True):
        if should_setup: self.setup()
        self.loop()
    def run(self):
        #after the program dies the program waits x seconds and then runs again
        time_to_sleep_on_error = 2
            
        while True:
            try:
                self.setup()
            except KeyboardInterrupt as err:
                #rasie error if control c is passes
                raise
            except Exception as err:
                print(err)
                continue

                
            while True:
                try:
                    self.loop()
                except KeyboardInterrupt as err:
                    #rasie error if control c is passes
                    raise
                except Exception as err:
                    print(err)
                    break

            try:
                self.on_error()
            except KeyboardInterrupt as err:
                #rasie error if control c is passes
                raise
            except Exception as err:
                print(err)
                continue            
            
            sleep(2)

#used to create a Template or leave peripheral blank
class Empty():
    def setup(self):
        pass
    def loop(self):
        pass
