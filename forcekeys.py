#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pynput.keyboard import Key, Listener, Controller
import pyperclip


class MainCLS(object):


    def __init__(self):

        print('Waiting for key ...')

        self.keyboard = Controller()
        with Listener(on_press=self.onPress) as listener:
            listener.join()


    def onPress(self, key):
        
        if(str(key) == 'Key.f4'):
            print('Simulating keys ... ', end='')
            self.keyboard.type(pyperclip.paste())
            print('OK')


if __name__ == '__main__':

    try:
        mainCLS = MainCLS()

    except KeyboardInterrupt as e:
        # Ctrl+C, it's ok.
        pass

    except Exception as e:
        # Unhandled exception
        raise e
