import pynput
import time
from pynput.mouse import Button, Controller

def main():

    mouse = Controller()

    for x in range(50):
    #clicks at 10.00 CPS (clicks per second)
        time.sleep(0.01)
        mouse.press(Button.left)
        mouse.release(Button.left)

    print('the autoclicker has run successfully!')


if __name__ == '__main__':
    main()
