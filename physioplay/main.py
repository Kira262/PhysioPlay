import cv2
from utils.camera import Camera
from utils.pose_detection import PoseDetector
from utils.scoreboard import ScoreboardManager
from game.exercise_manager import ExerciseManager
from game.display import DisplayManager
from game.game_logic import GameState


def main():
    # Initialize components
    camera = Camera()
    if not camera.initialize():
        print("Could not initialize camera. Please check your camera connection.")
        return

    pose_detector = PoseDetector()
    exercise_manager = ExerciseManager()
    display_manager = DisplayManager()
    scoreboard = ScoreboardManager()

    # Get player name and initialize game state
    player_name = input("Enter your name: ")
    game_state = GameState(player_name)

    try:
        # Main game loop
        while not game_state.game_over:
            # Get frame from camera
            frame = camera.read_frame()
            if frame is None:
                print("Failed to grab frame - camera may have been disconnected")
                break

            # Process frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose_detector.detect_pose(frame_rgb)

            # Draw pose landmarks
            frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
            pose_detector.draw_landmarks(frame_bgr, results)

            # Update game state
            game_state.update()
            current_exercise = exercise_manager.get_current_exercise()
            state_dict = game_state.get_state_dict()
            state_dict["current_exercise"] = current_exercise

            # Check for exercise completion or skip
            if pose_detector.check_exercise(results, current_exercise):
                game_state.handle_exercise_complete()
                exercise_manager.get_new_exercise()

            # Update display and check for user input
            key = display_manager.update_display(frame_bgr, state_dict)

            if key == ord("s"):
                if game_state.handle_skip():
                    exercise_manager.get_new_exercise()
            elif key == ord("q"):
                break

    except Exception as e:
        print(f"An error occurred during the game: {e}")

    finally:
        # Cleanup
        camera.release()
        pose_detector.cleanup()
        display_manager.cleanup()

        # Save score and display scoreboard
        try:
            scoreboard.save_score(player_name, game_state.score)
            scoreboard.display_scoreboard()
        except Exception as e:
            print(f"Error saving score: {e}")
            print(f"Final score: {game_state.score}")


if __name__ == "__main__":
    main()
