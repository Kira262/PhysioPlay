import os

# Suppress warnings and logging
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["PYTHONWARNINGS"] = "ignore"

# Game settings
GAME_DURATION = 180  # seconds
INITIAL_SKIPS = 5
SKIP_PENALTY = 0.5
SKIP_MESSAGE_DURATION = 2

# Camera settings
MAX_CAMERA_INDEX = 3
CAMERA_READ_TIMEOUT = 5

# Exercise list
EXERCISES = [
    "Raise your hands!",
    "Do a squat!",
    "Touch your toes!",
    "Left arm forward!",
    "Right arm forward!",
    "Clap your hands!",
    "Make a T with your arms straight!",
    "Bend your left elbow!",
    "Bend your right elbow!",
    "Raise your left leg!",
    "Raise your right leg!",
]

# Display settings
FONT_SCALE = 0.7
FONT_THICKNESS = 2
TEXT_COLOR = {
    "player": (255, 255, 255),
    "exercise": (0, 255, 0),
    "score": (0, 0, 255),
    "time": (255, 165, 0),
    "skips": (255, 192, 203),
    "skip_message": (0, 255, 255),
}

# Scoreboard settings
SCOREBOARD_FILE = "scoreboard.txt"
MAX_HIGH_SCORES = 5
