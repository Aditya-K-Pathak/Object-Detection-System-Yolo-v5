import detect
import os
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


def start_webcam():
    detect.run(weights=ROOT / 'yolov5s.pt',  # model.pt path(s)
               source='1',  # file/dir/URL/glob, 0 for webcam
            #    source = "../Video_1.avi",
               data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
               imgsz=(640, 640),  # inference size (height, width)
               conf_thres=0.63,  # confidence threshold
               iou_thres=0.45,  # NMS IOU threshold
               max_det=1000,  # maximum detections per image
               device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
               view_img=True,  # show results
               save_txt=False,  # save results to *.txt
               save_conf=False,  # save confidences in --save-txt labels
               save_crop=False,  # save cropped prediction boxes
               nosave=False,  # do not save images/videos
               classes=None,  # filter by class: --class 0, or --class 0 2 3
               agnostic_nms=False,  # class-agnostic NMS
               augment=False,  # augmented inference
               visualize=False,  # visualize features
               update=False,  # update all models
               project=ROOT / 'runs/detect',  # save results to project/name
               name='exp',  # save results to project/name
               exist_ok=False,  # existing project/name ok, do not increment
               line_thickness=3,  # bounding box thickness (pixels)
               hide_labels=False,  # hide labels
               hide_conf=True,  # hide confidences
               half=False,  # use FP16 half-precision inference
               dnn=False,  # use OpenCV DNN for ONNX inference
               )

def start_scan(path):
    detect.run(weights=ROOT / 'yolov5s.pt',  # model.pt path(s)
               source=path,  # file/dir/URL/glob, 0 for webcam
               data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
               imgsz=(640, 640),  # inference size (height, width)
               conf_thres=0.4,  # confidence threshold
               iou_thres=0.45,  # NMS IOU threshold
               max_det=1000,  # maximum detections per image
               device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
               view_img=True,  # show results
               save_txt=False,  # save results to *.txt
               save_conf=False,  # save confidences in --save-txt labels
               save_crop=False,  # save cropped prediction boxes
               nosave=False,  # do not save images/videos
               classes=None,  # filter by class: --class 0, or --class 0 2 3
               agnostic_nms=False,  # class-agnostic NMS
               augment=False,  # augmented inference
               visualize=False,  # visualize features
               update=False,  # update all models
               project=ROOT / 'runs/detect',  # save results to project/name
               name='exp',  # save results to project/name
               exist_ok=False,  # existing project/name ok, do not increment
               line_thickness=3,  # bounding box thickness (pixels)
               hide_labels=False,  # hide labels
               hide_conf=False,  # hide confidences
               half=False,  # use FP16 half-precision inference
               dnn=False,  # use OpenCV DNN for ONNX inference
               )
# start_webcam()