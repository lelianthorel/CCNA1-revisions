from controllers.configuration import *
from rich.console import Console
console = Console()

class PRINTJson:
    def __init__(self, data):
        self.data = data
    
    def GET_question(self):
        return self.data["question"]
    
    def GET_choices(self):
        return self.data["choices"]
    
    def GET_answers(self):
        return self.data["answers"]
    
    def ass_for_a_question(self):
        question = self.GET_question()
        choices = self.GET_choices()
        answers = self.GET_answers()
        
        console.print(f"{question}", style="italic blue")
        for choice in choices:
            print(f"{choices.index(choice)} : {choice}")
            
        return answers