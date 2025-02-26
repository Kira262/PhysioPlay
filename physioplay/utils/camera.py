import cv2
import time
from config import MAX_CAMERA_INDEX, CAMERA_READ_TIMEOUT


class Camera:
    def __init__(self):
        self.cap = None
        self.camera_index = None

    def initialize(self):
        """Initialize camera by trying different indices."""
        for idx in range(MAX_CAMERA_INDEX):
            try:
                cap = cv2.VideoCapture(idx)
                if cap is None or not cap.isOpened():
                    continue

                # Try to read a frame
                start_time = time.time()
                while time.time() - start_time < CAMERA_READ_TIMEOUT:
                    ret, frame = cap.read()
                    if ret and frame is not None:
                        self.cap = cap
                        self.camera_index = idx
                        return True

                cap.release()
            except Exception as e:
                print(f"Error with camera {idx}: {e}")
                continue

        return False

    def read_frame(self):
        """Read and process a frame from the camera."""
        if self.cap is None:
            return None

        ret, frame = self.cap.read()
        if not ret or frame is None:
            return None

        return cv2.flip(frame, 1)

    def release(self):
        """Release the camera resources."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
