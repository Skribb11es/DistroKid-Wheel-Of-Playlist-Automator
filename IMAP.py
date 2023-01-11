#Credit for a large portion of this code goes to https://github.com/thomaswieland, I really didn't see a reason to redo what was already well made. However all the code within the dosync function is all original (along with some other minor changes)

import imaplib2, time, email
from threading import *
 
# This is the threading object that does all the waiting on 
# the event
class Idler(object):
    def __init__(self, conn, callbackFunc, callbackArgs):
        self.thread = Thread(target=self.idle)
        self.M = conn
        self.event = Event()
        self.callFunc = callbackFunc
        self.args = callbackArgs
        callbackFunc(callbackArgs[0], callbackArgs[1])
 
    def start(self):
        self.thread.start()
 
    def stop(self):
        # This is a neat trick to make thread end. Took me a 
        # while to figure that one out!
        self.event.set()
 
    def join(self):
        self.thread.join()
 
    def idle(self):
        # Starting an unending loop here
        while True:
            # This is part of the trick to make the loop stop 
            # when the stop() command is given
            if self.event.isSet():
                return
            self.needsync = False
            # A callback method that gets called when a new 
            # email arrives. Very basic, but that's good.
            def callback(args):
                if not self.event.isSet():
                    self.needsync = True
                    self.event.set()
            # Do the actual idle call. This returns immediately, 
            # since it's asynchronous.
            self.M.idle(callback=callback)
            # This waits until the event is set. The event is 
            # set by the callback, when the server 'answers' 
            # the idle call and the callback function gets 
            # called.
            self.event.wait()
            # Because the function sets the needsync variable,
            # this helps escape the loop without doing 
            # anything if the stop() is called. Kinda neat 
            # solution.
            if self.needsync:
                self.event.clear()
                self.dosync()
 
    # The method that gets called when a new email arrives. 
    # Replace it with something better.
    def dosync(self):
        status, info = self.M.uid('search', None, 'ALL')
        if status == "OK":
            status, info = self.M.uid('fetch', info[0].split()[-1], '(RFC822)')
            if status == "OK":
                object = email.message_from_bytes(info[0][1])
                if object['From'] == f"DistroKid <mailbot@distrokid.com>":
                    self.callFunc(self.args[0], self.args[1])