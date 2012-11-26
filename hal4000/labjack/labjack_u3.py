#!/usr/bin/python
#
# Labjack U3 Interface.
# Everything happens on the FIO4 pin.
#
# Hazen 5/12
#

import u3
import time

class PWM():
    def __init__(self):
        self.device = u3.U3()
        self.device.writeRegister(6004,0) # set FIO4 state to low.
        self.device.configTimerClock(TimerClockBase = 5, TimerClockDivisor = 1)

    def shutDown(self):
        self.device.close()

    def startPWM(self, duty_cycle):
        temp = 65535 - 256*duty_cycle
        self.device.configIO(NumberOfTimersEnabled = 1)
        self.device.getFeedback(u3.Timer0Config(TimerMode = 1, Value = 65535))
        self.device.getFeedback(u3.Timer0(Value = temp, UpdateReset = True))

    def stopPWM(self):
        self.device.getFeedback(u3.Timer0(Value = 65535, UpdateReset = True))
        self.device.configIO(NumberOfTimersEnabled = 0)

#
# Testing
#

if __name__ == "__main__":
    dev = PWM()
    for i in range(10):
        dev.startPWM(i)
        time.sleep(2)
    dev.stopPWM()
    dev.shutDown()


#
# The MIT License
#
# Copyright (c) 2012 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

