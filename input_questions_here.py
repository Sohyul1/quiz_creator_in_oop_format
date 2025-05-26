# Import the QuestionCreator class from quiz_creator_in_oop.py file
from quiz_creator_in_oop import QuestionCreator

# Check if this script is being run directly (and not imported into another script)
if __name__ == "__main__":
    # Create an instance of the QuestionCreator class, passing the file name "oop_questions.txt"
    creator = QuestionCreator("oop_questions.txt")
    # Run the method 
    creator.run()
