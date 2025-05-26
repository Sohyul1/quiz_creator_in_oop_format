# Initialize a question with its text, answer options, and correct answer
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

# Check if the user's answer matches the correct one (case and space insensitive).
    def is_correct(self, user_answer):
        return user_answer.lower().strip() == self.correct_answer.lower().strip()

# Format the question, choices, and answer for saving to a text file.
    def format_for_file(self):
        lines = [f"Question: {self.text}"]
        for letter in ['A', 'B', 'C', 'D']:
            lines.append(f"{letter}. {self.option[letter]}")
        lines.append(f"Answer: {self.correct_answer}\n")
        return "\n".join(lines)