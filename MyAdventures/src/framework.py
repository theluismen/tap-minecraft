import sys
from agents.Exception_bot import ExceptionBot
from agents.Insult_bot import InsultBot
from agents.TNT_bot import TNTBot
from agents.Info_bot import InfoBot
from agents.PPT_bot import PPTBot
def main ():

    if len(sys.argv) == 1 or len(sys.argv) ==2:
        return

    agent_type = sys.argv[1]
    choice = sys.argv[2]

    if agent_type.lower()   == 'insultbot':
        bot = InsultBot()
    elif agent_type.lower() == 'tntbot':
        bot = TNTBot()
    elif agent_type.lower() == 'infobot':
        bot = InfoBot()
    elif agent_type.lower() == 'pptbot':
        bot = PPTBot(choice)
    else:
        bot = ExceptionBot() # Mensaje de error AL SERVIDOR

    if bot.connected():
        bot.run()
        print(bot.test_msg())

if __name__ == "__main__":
    main()
