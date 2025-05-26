# Import the QuizReader class from the quiz_reader....
from quiz_reader_oop_format import QuizReader

# Import the QuizRunner class from quiz_runner  
from quiz_runner import QuizRunner

# Check if this script is being run directly (not imported as a module).
if __name__ == "__main__":
    reader = QuizReader("oop_questions.txt")

# Create an object hat is responsible for running the quiz logic
    runner = QuizRunner(reader)

# Run the quiz
    runner.run_quiz()
