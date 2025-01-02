import random
from .base_agent import BaseAgent

class PPTBot(BaseAgent):
    def __init__(self, choice=None):
        super().__init__()
        self.options = ["piedra", "papel", "tijera"]
        self.bot_choice = None
        self.human_choice = choice

    def test_msg(self):
        self.mc.postToChat("PPTBot: Done")

    def run(self):

        if self.human_choice in ["piedra", "papel", "tijera"]:
            self.print_message()
            self.bot_choice = self.get_bot_choice()
            self.print_choices()
            result = self.determine_winner()
            self.print_result(result)
            self.mc.postToChat("¡Gracias por jugar! Hasta la proxima.")
        else:
            self.mc.postToChat("Error en la elecion de jugada, elige: piedra | papel | tijera  ")


    def get_bot_choice(self):
        return random.choice(self.options)

    def print_choices(self):
        self.mc.postToChat(f"Tu elegiste: {self.human_choice}")
        self.mc.postToChat(f"El bot eligió: {self.bot_choice}")

    def determine_winner(self):
        if self.human_choice == self.bot_choice:
            return "empate"
        elif (self.human_choice == "piedra" and self.bot_choice == "tijera") or \
             (self.human_choice == "papel" and self.bot_choice == "piedra") or \
             (self.human_choice == "tijera" and self.bot_choice == "papel"):
            return "humano"
        else:
            return "bot"

    def print_result(self, result):
        if result == "empate":
            self.mc.postToChat("¡Es un empate!")
        elif result == "humano":
            self.mc.postToChat("¡Ganaste!")
        else:
            self.mc.postToChat("El bot gana.")
