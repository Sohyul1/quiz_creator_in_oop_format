# Import the question from the "question" file
from question import Question

# Initialize quiz creator
class QuestionCreator:
    def __init__(self, filename= "questions.txt"):
        self.filename = filename

# Make a method for inputting the quetions, choices and right answer
    def create_question(self):
        text = input("\nEnter any question you want: \n")
        choices = {
            'A': input("Letter 'A' value: \n"),  
            'B': input("Letter 'B' value: \n"),  
            'C': input("Letter 'C' value: \n"),    
            'D': input("Letter 'D' value: \n")
        }

# Method for saving as a text file 
