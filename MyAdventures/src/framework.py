import sys
from agents.Exception_bot import ExceptionBot
from agents.Insult_bot import InsultBot
from agents.TNT_bot import TNTBot
from agents.Info_bot import InfoBot

def main ():

    if len( sys.argv ) == 1 :
        return

    agent_type = sys.argv[1]

    if agent_type.lower()   == 'insultbot':
        bot = InsultBot()
    elif agent_type.lower() == 'tntbot':
        bot = TNTBot()
    elif agent_type.lower() == 'infobot':
        bot = InfoBot()
    else:
        bot = ExceptionBot() # Mensaje de error

    if bot.connected():
        bot.run()

if __name__ == "__main__":
    main()
