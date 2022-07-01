# Inbuilt Libraries ============================ 
import cv2
import numpy as np
import os
import time
from tkinter import messagebox as tmsg
import speech


#  Method for main ============================
def start_scan(file_path):
    # print(file_path)
    yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    objects = []

    with open("coco.names", "r") as file:
        classes = [line.strip() for line in file.readlines()]
    layer_names = yolo.getLayerNames()
    output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

    colorRed = (0, 0, 255)
    colorGreen = (0, 255, 0)

    # #Loading Images ============================
    name = file_path
    img = cv2.imread(name)
    height, width, channels = img.shape

    # # Detecting objects ============================
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    yolo.setInput(blob)
    outputs = yolo.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # Checks probability of object
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)  # Width of box
                h = int(detection[3] * height)  # Height of box

                x = int(center_x - w / 2)  # X - Coordinate
                y = int(center_y - h / 2)  # Y - Coordinate

                boxes.append([x, y, w, h])  # Appends coordinates, length and width to boxes list
                confidences.append(float(confidence))  # Appends possibility % to confidence list
                class_ids.append(class_id)  # Appends name to class_ids list

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            # if label not in objects:
            objects.append(label)
            cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Generates and place a border
            cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 5, colorRed, 2)  # Generates and place name

    # cv2.imshow("Image", img)
    cv2.imwrite("output.jpg", img)  # Creates a new image file with frames and names
    tmsg.showinfo("Successful", "Your output image file is generated.\nKindly delete it after use")  # popup message

    text = ""
    objects.sort()
    # print(objects)
    for i in set(objects):
        # print(objects)
        text += f"{objects.count(i)} " + i + ", "
        for j in range (objects.count(i)):
            objects.remove(i)


    try:
        speech.speak(f"{text} detected")  # Speaks the names of detected Objects
    except:
        tmsg.showerror("No Internet", "No Internet access")
    # time.sleep(1)  # Waits for 1 second to keep things in sync
    os.system("output.jpg")  # Display the image in default image viewing application

    # cv2.waitKey(0)
    cv2.destroyAllWindows()  # Destroys all window on completions
