# Initialize a question with its text, answer options, and correct answer
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.option = options
        self.correct_answer = correct_answer
# Check if the user's answer matches the correct one (case and space insensitive).
    def is_correct(self, user_answer):
        return user_answer.lower().strip() == self.correct_answer.lower().strip()
