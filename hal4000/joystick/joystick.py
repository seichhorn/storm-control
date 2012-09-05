#!/usr/bin/python
#
# Joystick monitoring class.
#
# Hazen 09/12
#

from PyQt4 import QtCore

# Debugging
import halLib.hdebug as hdebug

#
# Joystick monitoring class.
#
class JoystickObject(QtCore.QObject):
    toggle_film = QtCore.pyqtSignal()
    motion = QtCore.pyqtSignal(float, float, float, float)

    @hdebug.debug
    def __init__(self, joystick, parent = None):
        QtCore.QObject.__init__(self, parent)
        self.jstick = joystick
        self.jstick.start(self.joystickHandler)

    @hdebug.debug
    def close(self):
        self.jstick.shutDown()

    def joystickHandler(self, data):
        event_data = self.jstick.translate(data)
        if (event_data[0] == "Button"):
            if (event_data[1] == 6):
                self.toggle_film.emit()
        if (event_data[0] == "Joystick"):
            self.motion.emit(*event_data[1:])

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
