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
        
        questions_and_choices = []
        line_count = 0
        while line_count < len(lines):
            if lines[line_count].startswith("Question:"):
                question_text = lines[line_count].strip()
                choice_a = lines[line_count + 1].strip()
                choice_b = lines[line_count + 2].strip()
                choice_c = lines[line_count + 3].strip()
                choice_d = lines[line_count + 4].strip()
                correct_answer = lines[line_count + 5].strip(".").replace("Answer:", "").strip()
                questions_and_choices.append((question_text, [choice_a, choice_b, choice_c, choice_d], correct_answer))
            line_count += 6
            
        return questions_and_choices