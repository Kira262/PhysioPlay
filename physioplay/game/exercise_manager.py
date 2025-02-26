import random
from config import EXERCISES


class ExerciseManager:
    def __init__(self):
        self.current_exercise = None
        self.exercises = EXERCISES.copy()

    def get_new_exercise(self):
        """Get a new random exercise different from the current one."""
        available_exercises = [
            ex for ex in self.exercises if ex != self.current_exercise
        ]
        self.current_exercise = random.choice(available_exercises)
        return self.current_exercise

    def get_current_exercise(self):
        """Get the current exercise."""
        if self.current_exercise is None:
            self.current_exercise = random.choice(self.exercises)
        return self.current_exercise
