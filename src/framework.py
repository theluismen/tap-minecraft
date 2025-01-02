import sys

from bots.PPT_bot       import PPTBot
from bots.TNT_bot       import TNTBot
from bots.Info_bot      import InfoBot
from bots.Insult_bot    import InsultBot
from bots.Exception_bot import ExceptionBot

def main ():

    if len(sys.argv) == 1:
        return

    bot_type = sys.argv[1]

    if bot_type.lower()   == 'insultbot':
        bot = InsultBot()
    elif bot_type.lower() == 'tntbot':
        bot = TNTBot()
    elif bot_type.lower() == 'infobot':
        bot = InfoBot()
    elif bot_type.lower() == 'pptbot':
        if len(sys.argv) == 3:
            choice   = sys.argv[2]
        bot = PPTBot(choice)
    else:
        bot = ExceptionBot() # Mensaje de error AL SERVIDOR

    if bot.connected():
        bot.run()
        print( bot.test_msg() )

if __name__ == "__main__":
    main()
