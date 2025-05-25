# Import the Question class from question file
from question import Question

# Initialize the quiz reader
class QuizReader:
    def __init__(self, filename="oop_questions.txt"):
        self.filename = filename

# Make a reader method 
    def get_questions(self):
            with open(self.filename, "r") as file:
                lines = file.readlines()
