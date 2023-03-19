
# from rules import my_rules
from rules import StarClass_RuleSet
from rules import B_classStar
from rules import O_classStars
from rules import A_classStar
from rules import K_classStars
from rules import F_class_Star

from production import forward_chain
from production import backward_chain

class Choice:
    def __init__(self):
        self.var = "?x"
        self.questions = {
            'O-class': O_classStars().questions(),
            'K-class': K_classStars().questions(),
            'F-class': F_class_Star().questions(),
            'A-class': A_classStar().questions(),
            'B-class': B_classStar().questions(),
        }
        self.conclusions = [
            O_classStars.conclusion,
            K_classStars.conclusion,
            F_class_Star.conclusion,
            A_classStar.conclusion,
            B_classStar.conclusion,
        ]
        self.choice = ""

    def choice_input(self, name):
        print(f"Pick from the list of facts about {name} (ex: 1, 2, 10).\nYour choices are:")
        for index, fact in enumerate(self.concat_lists()):
            print(f"\t{index + 1} : {fact}")
        self.choice = input("\nChoose: ")
        to_chain = []
        for index in self.choice.split(" "):
            try:
                fact_index = int(index) - 1
                fact = self.concat_lists()[fact_index]
                to_chain.append(fact.replace(self.var, name))
            except (ValueError, IndexError):
                continue
        chained_data = forward_chain(StarClass_RuleSet, to_chain)
        return self.hints(chained_data, name)

    def concat_lists(self):
        return list(set(self.questions['A-class'] +
                        self.questions['B-class'] +
                        self.questions['F-class'] +
                        self.questions['K-class'] +
                        self.questions['O-class']))

    def hints(self, chained_data, name):
        hint_list = []
        for conclusion in self.conclusions:
            dec_conclusion = conclusion.replace(self.var, name)
            if dec_conclusion in chained_data:
                hint_list.append(dec_conclusion)
        if not hint_list:
            return f"{name} not known as a star class. Go on? (y/n)"
        return f"Does the star belong to the {hint_list}? Go on? (y/n)"

if __name__ == '__main__':
    print("Welcome to Expert System!")
    choice = Choice()
    while True:
        exit_input = input("If you want to exit the system write y: ")
        if exit_input == "y":
            print("The system will shut down soon...")
            break
        input_name = input("Please write your name: ")
        hint = choice.choice_input(input_name)
        print(hint)
        confirm_hint = input("Write 'yes' or 'no': ")
        while confirm_hint not in ('yes', 'no'):
            confirm_hint = input(f"The system does not understand '{confirm_hint}'. Write 'yes' or 'no': ")
        if confirm_hint == "yes":
            print("I am here to help you!")
        else:
            print("We are sorry we were not able to help.")

    
     

    