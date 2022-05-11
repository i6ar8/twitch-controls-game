def help (bot,prefix,cmds):
    bot.send_message("Registered commands:"+", ".join([f"{prefix}{cmd}" for cmd in sorted(cmds.keys())]))

def hello (bot,user,*args):
    bot.send_message(f"hey {user['name']}!")

def cgccomd (bot,user,*args):
    bot.send_message("for walk UP send up, for walk Down send down, for walk left send left,for walk right send right.")
    