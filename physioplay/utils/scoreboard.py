import os
import cv2
import numpy as np
from config import SCOREBOARD_FILE, MAX_HIGH_SCORES


class ScoreboardManager:
    def __init__(self):
        self.file_path = SCOREBOARD_FILE
        self.high_scores = []
        self._load_scores()

    def _load_scores(self):
        """Load existing scores from file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    for line in file:
                        parts = line.strip().split(":")
                        if len(parts) == 2:
                            self.high_scores.append((parts[0], int(parts[1])))
        except Exception as e:
            print(f"Error loading scores: {e}")
            self.high_scores = []

    def save_score(self, player_name, score):
        """Save a new score and maintain top scores."""
        try:
            # Add new score
            self.high_scores.append((player_name, score))

            # Sort scores in descending order
            self.high_scores.sort(key=lambda x: x[1], reverse=True)

            # Keep only top scores
            self.high_scores = self.high_scores[:MAX_HIGH_SCORES]

            # Save to file
            with open(self.file_path, "w") as file:
                for name, points in self.high_scores:
                    file.write(f"{name}:{points}\n")

            return True
        except Exception as e:
            print(f"Error saving score: {e}")
            return False

    def display_scoreboard(self):
        """Display the scoreboard in a window."""
        try:
            # Create a black background
            scoreboard = np.zeros((400, 500, 3), dtype=np.uint8)

            # Draw title
            cv2.putText(
                scoreboard,
                "🏆 High Scores 🏆",
                (120, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),  # Yellow color
                2,
            )

            # Draw scores
            for i, (player, score) in enumerate(self.high_scores):
                # Position each score entry
                y_position = 100 + i * 50

                # Create the score text
                score_text = f"{i+1}. {player}"
                score_value = f"{score} pts"

                # Draw player name (white)
                cv2.putText(
                    scoreboard,
                    score_text,
                    (50, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),  # White color
                    2,
                )

                # Draw score (green)
                cv2.putText(
                    scoreboard,
                    score_value,
                    (300, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),  # Green color
                    2,
                )

            # Show empty state if no scores
            if not self.high_scores:
                cv2.putText(
                    scoreboard,
                    "No scores yet!",
                    (150, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2,
                )

            # Display the scoreboard
            cv2.imshow("PhysioPlay High Scores", scoreboard)
            cv2.waitKey(5000)  # Display for 5 seconds
            cv2.destroyWindow("PhysioPlay High Scores")

        except Exception as e:
            print(f"Error displaying scoreboard: {e}")

    def get_high_scores(self):
        """Return the list of high scores."""
        return self.high_scores.copy()

    def clear_scores(self):
        """Clear all scores (useful for testing)."""
        try:
            self.high_scores = []
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
            return True
        except Exception as e:
            print(f"Error clearing scores: {e}")
            return False
