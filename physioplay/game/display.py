import cv2
from config import FONT_SCALE, FONT_THICKNESS, TEXT_COLOR


class DisplayManager:
    def __init__(self):
        self.window_name = "PhysioPlay Game"
        cv2.namedWindow(self.window_name, cv2.WINDOW_FREERATIO)

    def update_display(self, frame, game_state):
        """Update the game display with current state."""
        self._draw_game_info(frame, game_state)
        cv2.imshow(self.window_name, frame)
        return cv2.waitKey(1) & 0xFF

    def _draw_game_info(self, frame, state):
        """Draw game information on the frame."""
        info_list = [
            ("Player: " + state["player_name"], 30, TEXT_COLOR["player"]),
            ("Exercise: " + state["current_exercise"], 60, TEXT_COLOR["exercise"]),
            (f"Score: {state['score']}", 90, TEXT_COLOR["score"]),
            (f"Time Left: {int(state['remaining_time'])}s", 120, TEXT_COLOR["time"]),
            (f"Skips Left: {state['skips_remaining']}", 150, TEXT_COLOR["skips"]),
        ]

        for text, y_pos, color in info_list:
            cv2.putText(
                frame,
                text,
                (50, y_pos),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                color,
                FONT_THICKNESS,
            )

        if state["show_skip_message"]:
            cv2.putText(
                frame,
                "Exercise Skipped! +0.5 points",
                (50, 180),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                TEXT_COLOR["skip_message"],
                FONT_THICKNESS,
            )

    def cleanup(self):
        """Clean up display resources."""
        cv2.destroyAllWindows()
