from pynput.keyboard import Key,Controller
import time
keyboard=Controller()
MST=0.17

def controlGameCmd(cmd):
    
    if cmd=="فوق":
        print(cmd) 
        keyboard.press(Key.up)
        time.sleep(MST)
        keyboard.release(Key.up)
    elif cmd=="يسار":
        print(cmd)
        keyboard.press(Key.left)
        time.sleep(MST)
        keyboard.release(Key.left)
    
    elif cmd=="يمين":
        print(cmd)
        keyboard.press(Key.right)
        time.sleep(MST)
        keyboard.release(Key.right)
    
    elif cmd=="تحت":
        print(cmd)
        keyboard.press(Key.down)
        time.sleep(MST)
        keyboard.release(Key.down)
    elif cmd=="a":
        keyboard.press('a')
        time.sleep(0.1)
        keyboard.release('a')
    elif cmd=="run":
        keyboard.press('b')
        time.sleep(15)
        keyboard.release('b')
    else:
        pass


    

    
