# # imported Libraries=============================
# import cv2
# import numpy as np
# import time

# # User-defined Library===========================
# import speech


# # Function Definition============================
# def start_webcam():
#     yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
#     classes = []

#     # Reads Object name from coco.names==============
#     with open("coco.names", "r") as file:
#         classes = [line.strip() for line in file.readlines()]
#     layer_names = yolo.getLayerNames()
#     output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

#     colorRed = (0, 0, 255)
#     colorGreen = (0, 255, 0)

#     # Starts VideoCapture============================
#     cap = cv2.VideoCapture(0)
#     # cap = cv2.VideoCapture(0)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     starting_time = time.time()
#     frame_id = 0

#     obj_name = ""
#     while True:
#         # #Loading WebCam Video======================
#         _, img = cap.read()
#         frame_id += 1
#         height, width, channels = img.shape

#         # # Detecting objects========================
#         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

#         yolo.setInput(blob)
#         outputs = yolo.forward(output_layers)

#         class_ids = []
#         confidences = []
#         boxes = []
#         for output in outputs:
#             for detection in output:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 # Checks probability of object
#                 if confidence > 0.5:
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)  # width of border
#                     h = int(detection[3] * height)  # height of border

#                     x = int(center_x - w / 2)  # x-coordinate
#                     y = int(center_y - h / 2)  # y-coordinate

#                     boxes.append([x, y, w, h])  # Appends coordinate, width and height to boxes list
#                     confidences.append(float(confidence))  # Appends possibility % to confidence list
#                     class_ids.append(class_id)  # Appends names to class_ids list
#                     # obj_name += class_id + ", "

#         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#         for i in range(len(boxes)):
#             if i in indexes:
#                 x, y, w, h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 obj_name += label + ", "
#                 cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Creates and place a border
#                 cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 3, colorRed, 3)  # Creates and place name

#         # Runs the Webcam
#         cv2.imshow("Live Object Detection", img)

#         # if object found==================================
#         if obj_name != "":
#             # Speaks object name===========================
#             speech.speak(f"{obj_name} detected")
#             # time.sleep(len(obj_name.split(", ")) + 2)
#             # Empties object name==========================
#             obj_name = ""
#         else:
#             speech.speak("No known object found")

#         # Closes operation if 'q' button is pressed========
#         if cv2.waitKey(1) == ord("q"):
#             break











# imported Libraries=============================
import cv2
import numpy as np
import time
from tkinter import messagebox as tmsg

# User-defined Library===========================
import speech


# Function Definition============================
def start_webcam():
    yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []

    # Reads Object name from coco.names==============
    with open("coco.names", "r") as file:
        classes = [line.strip() for line in file.readlines()]
    layer_names = yolo.getLayerNames()
    output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

    colorRed = (0, 0, 255)
    colorGreen = (0, 255, 0)

    # Starts VideoCapture============================
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    starting_time = time.time()
    frame_id = 0

    obj_name = ""
    while True:
        # #Loading WebCam Video======================
        _, img = cap.read()
        frame_id += 1
        height, width, channels = img.shape

        # # Detecting objects========================
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        yolo.setInput(blob)
        outputs = yolo.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        objects = []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # Checks probability of object
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)  # width of border
                    h = int(detection[3] * height)  # height of border

                    x = int(center_x - w / 2)  # x-coordinate
                    y = int(center_y - h / 2)  # y-coordinate

                    boxes.append([x, y, w, h])  # Appends coordinate, width and height to boxes list
                    confidences.append(float(confidence))  # Appends possibility % to confidence list
                    class_ids.append(class_id)  # Appends names to class_ids list
                    # obj_name += class_id + ", "

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                objects.append(label)
                obj_name += label + ", "
                cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Creates and place a border
                cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 3, colorRed, 3)  # Creates and place name

        # Runs the Webcam
        cv2.imshow("Live Object Detection", img)

        # # if object found==================================
        text = ""
        objects.sort()
        # print(objects)
        for i in set(objects):
            # print(objects)
            text += f"{objects.count(i)} " + i + ", "
            for j in range (objects.count(i)):
                objects.remove(i)


        # try:
        #     speech.speak(f"{text} detected")  # Speaks the names of detected Objects
        # except:
        #     tmsg.showerror("No Internet", "No Internet access")
        # # Closes operation if 'q' button is pressed========
        if cv2.waitKey(1) == ord("q"):
            break