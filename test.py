import cv2
import pytesseract
from PIL import ImageTk,Image

def main():
    # Use the attached camera to capture images
    # 0 stands for the first one
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(Image.fromarray(img1))
        cv2.imshow('frame', img1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return None
        print("Extracted Text: ", text)
        cv2.destroyAllWindows()
    cap.release()