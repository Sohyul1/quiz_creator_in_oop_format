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
        # Loop until the user enters a valid correct answer (A, B, C, or D)
        while True:
            correct_answer = input("Letter of the right answer [A/B/C/D]: \n").strip().upper()
            if correct_answer in choices:
                break  
            else:
                print("Invalid input. Please enter A, B, C, or D.\n")
        return Question(text, choices, correct_answer)

# Method for saving as a text file 
    def save_question(self, question):  
        with open(self.filename, "a") as file:
            file.write(question.format_for_file())