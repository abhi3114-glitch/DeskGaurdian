import cv2
import mediapipe as mp
import numpy as np

class FaceDetector:
    def __init__(self, min_detection_confidence=0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(
            min_detection_confidence=min_detection_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def process_frame(self, frame):
        """
        Process the frame to detect faces.
        Returns the frame with drawn annotations and the detection results.
        """
        # Convert BGR to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(img_rgb)
        return results

    def get_face_width_ratio(self, results, frame_width):
        """
        Get the ratio of the face width to the frame width.
        Returns the maximum ratio found (closest face).
        """
        max_ratio = 0.0
        
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                # bboxC.width is already relative to the image width
                if bboxC.width > max_ratio:
                    max_ratio = bboxC.width
                    
        return max_ratio

    def draw_faces(self, frame, results):
        """
        Draw bounding boxes on the frame.
        """
        if results.detections:
            for detection in results.detections:
                self.mp_draw.draw_detection(frame, detection)
        return frame
