'''
Consider an intelligent traffic signal. The signal has two states: red and green. The vehicle density in front of the signal is denoted by the variable v. 
If the vehicle density crosses a threshold T in either direction, the state of the signal changes. 
For example, if the signal is currently red, and the vehicle density becomes greater than or equal to the threshold, it is time to turn the signal green. 
This is denoted by the arrow from red to green at the bottom of the image.
Assume that the signal senses the vehicle density every 30 seconds and updates its state appropriately.
'''

class Signal:
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = T

    def sense(self, v):
        self.v = v

    def update(self):
        if self.v >= self.T:
            if self.state == 'red':
                self.state = 'green'
        else:
            if self.state == 'green':
                self.state = 'red'
