import cv2

def preprocessing(img):
    # 1) obtain binary image - grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img