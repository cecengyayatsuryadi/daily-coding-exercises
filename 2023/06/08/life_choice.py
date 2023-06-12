class LifeManager:
    """
    A class that manages life.
    """

    @staticmethod
    def run(difficulty):
        """
        Runs life with the given difficulty.
        """
        if difficulty == "hard":
            print("Running life in hard mode...")
        elif difficulty == "easy":
            print("Running life in easy mode...")
        else:
            print("Invalid difficulty level.")

    @staticmethod
    def hard():
        """
        Runs life in hard mode.
        """
        LifeManager.run("hard")

    @staticmethod
    def easy():
        """
        Runs life in easy mode.
        """
        LifeManager.run("easy")


difficulty = input("Enter difficulty level (easy/hard): ")

try:
    LifeManager.run(difficulty)
except Exception as e:
    # Print error message and suggest to try again
    print("Error occurred while running life:", e)
    print("It's okay, you can try again.")
else:
    if difficulty == "hard":
        print("You're a brave soul!")
    elif difficulty == "easy":
        print("You're taking it easy, huh?")
    else:
        print("How about trying again with a valid difficulty level?")
