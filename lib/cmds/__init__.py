from time import time
from . import misc
from . import Cgc
import _thread

PREFIX="!"
CGC={"فوق","يسار","يمين","تحت","a","run"}
cmds={"hi":misc.hello,"cgc":misc.cgccomd}
def process(bot,user,message):
    if message in CGC:
        print(message)
        _thread.start_new_thread( Cgc.controlGameCmd, (message,) )
    else:
        cmd=message.split(" ")[0][len(PREFIX):]
        
        args=message.split(" ")[1:]
        
        perform(bot,user,cmd,*args)

def perform(bot,user,cmd,*args):
    
    for name,func in cmds.items():
        if cmd==name:
            func(bot,user,*args)
            return
    if cmd=="help":
        misc.help(bot,PREFIX,cmds)
    else:
        bot.send_message(f"{user['name']},\"{cmd}\"isn't registerd command.")

