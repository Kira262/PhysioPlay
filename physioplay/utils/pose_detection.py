import numpy as np
import mediapipe as mp


class PoseDetector:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_pose(self, image_rgb):
        """Process image and detect pose landmarks."""
        return self.holistic.process(image_rgb)

    def draw_landmarks(self, image, results):
        """Draw pose landmarks on the image."""
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS
            )

    def check_exercise(self, results, exercise):
        """Check if current pose matches the required exercise."""
        if not results.pose_landmarks:
            return False

        landmarks = results.pose_landmarks.landmark

        # Get required landmarks
        left_wrist = landmarks[self.mp_holistic.PoseLandmark.LEFT_WRIST]
        right_wrist = landmarks[self.mp_holistic.PoseLandmark.RIGHT_WRIST]
        left_shoulder = landmarks[self.mp_holistic.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[self.mp_holistic.PoseLandmark.RIGHT_SHOULDER]
        left_elbow = landmarks[self.mp_holistic.PoseLandmark.LEFT_ELBOW]
        right_elbow = landmarks[self.mp_holistic.PoseLandmark.RIGHT_ELBOW]
        left_hip = landmarks[self.mp_holistic.PoseLandmark.LEFT_HIP]
        right_hip = landmarks[self.mp_holistic.PoseLandmark.RIGHT_HIP]
        left_knee = landmarks[self.mp_holistic.PoseLandmark.LEFT_KNEE]
        right_knee = landmarks[self.mp_holistic.PoseLandmark.RIGHT_KNEE]
        left_ankle = landmarks[self.mp_holistic.PoseLandmark.LEFT_ANKLE]
        right_ankle = landmarks[self.mp_holistic.PoseLandmark.RIGHT_ANKLE]

        shoulder_width = abs(left_shoulder.x - right_shoulder.x)

        # Check specific exercises
        if exercise == "Raise your hands!":
            return (
                left_wrist.y < left_shoulder.y - 0.05
                and right_wrist.y < right_shoulder.y - 0.05
            )

        if exercise == "Do a squat!":
            return left_hip.y > left_knee.y and right_hip.y > right_knee.y

        # Add other exercise checks here...

        return False

    def cleanup(self):
        """Clean up resources."""
        self.holistic.close()
