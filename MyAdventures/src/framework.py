import sys
from agents.Exception_bot import ExceptionBot
from agents.Insult_bot import InsultBot
from agents.TNT_bot import TNTBot

def main ():

    if len( sys.argv ) == 1 :
        return

    agent_type = sys.argv[1]

    if agent_type.lower() == 'insultbot':
        bot = InsultBot()
    elif agent_type.lower() == 'tntbot':
        bot = TNTBot()
    else:
        bot = ExceptionBot(); # Mensaje de error
    bot.run()

if __name__ == "__main__":
    main()
