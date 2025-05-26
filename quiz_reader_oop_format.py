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
                choices = {
                    'A': lines[line_count + 1].replace("A.", "").strip(),
                    'B': lines[line_count + 2].replace("B.", "").strip(),
                    'C': lines[line_count  + 3].replace("C.", "").strip(),
                    'D': lines[line_count + 4].replace("D.", "").strip()
                }

                correct_answer = lines[line_count + 5].replace("Answer:", "").strip()
                questions_and_choices.append(Question(question_text, choices, correct_answer))
            line_count += 6
            
        return questions_and_choices