import time
from config import GAME_DURATION, INITIAL_SKIPS, SKIP_PENALTY, SKIP_MESSAGE_DURATION


class GameState:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.skips_remaining = INITIAL_SKIPS
        self.start_time = time.time()
        self.skip_message_time = 0
        self.game_over = False

    def update(self):
        """Update game state."""
        elapsed_time = time.time() - self.start_time
        self.remaining_time = max(0, GAME_DURATION - elapsed_time)
        self.show_skip_message = (
            time.time() - self.skip_message_time < SKIP_MESSAGE_DURATION
        )

        if self.remaining_time <= 0:
            self.game_over = True

    def handle_exercise_complete(self):
        """Handle completed exercise."""
        self.score += 1

    def handle_skip(self):
        """Handle exercise skip."""
        if self.skips_remaining > 0:
            self.score += SKIP_PENALTY
            self.skips_remaining -= 1
            self.skip_message_time = time.time()
            return True
        return False

    def get_state_dict(self):
        """Get current game state as dictionary."""
        return {
            "player_name": self.player_name,
            "score": self.score,
            "remaining_time": self.remaining_time,
            "skips_remaining": self.skips_remaining,
            "show_skip_message": self.show_skip_message,
        }
