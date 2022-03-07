# https://medium.com/analytics-vidhya/how-to-make-face-recognition-with-tensorflow-2-and-data-scraping-fac960445e56

from pathlib import Path
from glob import glob
from mtcnn import MTCNN
from PIL import Image
import numpy as np
import pandas as pd
import cv2


def get_detected_face(filename, required_size=(48, 48)):
    """
    This function uses OpenCV to detect and crop faces from images
    Then it resizes the image to a specified height and width and
    converts the image to a numpy array.
    """
    img = cv2.imread(filename)
    detector = MTCNN()
    results = detector.detect_faces(img)
    if len(results) > 0:
        x, y, width, height = results[0]['box']
        face = img[y:y + height, x:x + width]
        if face.ndim == 3:
            image = Image.fromarray(face)
            image = image.resize(required_size)
            face_array = np.asarray(image)
            return str(face.tolist()) #, face_array.tolist()) 
        else:
            print(f"Dimensions doesn't match for: {filename}\nface.ndim = {face.ndim}") 
            return np.nan
    else:
        print(f"Faces not detected in: {filename}")
        return np.nan
    

def insert_as_nparray(df, image, path_base):
    """
    This function receives an image folder glob path and extract
    the face of each image, then it inserts it as np_array in a df
    
    It doesn't return anything
    """
    image_path = f"{image.split('/')[-2]}/{image.split('/')[-1]}"
    df["face_nparray"].iloc[int(df[df["full_path"] == image_path].index[0])] = get_detected_face(f"{path_base}{image_path}", required_size=(40, 40))

    

def save_array():
    df = pd.read_csv('wiki.csv')
    df["face_nparray"] = np.nan
    path_base = '../images/'
    csv_path = Path('./face_nparray.csv')
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    image_count = glob(f"{path_base}/**/*.jpg")

    for count, image in enumerate(image_count):
        try:
            print(f"{count}/{len(image_count)}")    
            insert_as_nparray(df, image, path_base)
        except ValueError as error:
            print(error)
            print(f"Image: {image}")
            continue
    print("Done")
    
    df.to_csv(csv_path)

    
if __name__ == '__main__':
    save_array()
