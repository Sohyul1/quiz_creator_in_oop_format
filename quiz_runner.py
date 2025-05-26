# Import random, Fore, style, init from colorama
import random
from colorama import Fore, Style, init

# import QuizReader from quiz_reader and Question from questions
from quiz_reader_oop_format import QuizReader
from question import Question

# Initialize autoreset of colors 
init(autoreset=True)

# Initialize QuizRunner class
class QuizRunner:
    def __init__(self, reader):
        self.reader = reader
        self.score = 0

# Methhod for asking the questions
    def ask_question(self, question):
            print(Style.BRIGHT + Fore.CYAN + "\n" + question.text + "\n")
            
            for letter in ['A', 'B', 'C', 'D']:
               print(Style.BRIGHT + Fore.MAGENTA + f"{letter}. {question.options[letter]}")
           
            while True:
                answer = input(Style.BRIGHT + Fore.CYAN + "\nEnter your answer [A/B/C/D]: ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break

            if question.is_correct(answer):
                print(Style.BRIGHT + Fore.GREEN + "Correct!")
                self.score += 1
            else:
                print(Style.BRIGHT + Fore.RED + f"Incorrect. The correct answer was {question.correct_answer}.")

    # Method for running the quiz
    def run_quiz(self):
        while True:
            self.score = 0  
            questions = self.reader.get_questions()  
            random.shuffle(questions)  

            # Ask each question one by one
            for question in questions:
                self.ask_question(question)
        

