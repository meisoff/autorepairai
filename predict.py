# import cv2
# from ultralytics import YOLO
# img_pth = "4.jpg"
# model = YOLO("best.pt")
# results = model(source=img_pth)
# res_plotted = results[0].plot()
# cv2.imshow("result", res_plotted)
# cv2.waitKey(0)
import base64

# from my_fastapi_app.detect import detect_car

# import cv2
# from ultralytics import YOLO
# img_pth = "./car_type/nocar.jpg"
# model = YOLO("./car_type/best_2.pt")
# model.export(format="onnx", imgsz=[640,640], opset=12)
# results = model(source=img_pth)
# res_plotted = results[0].plot()
# cv2.imshow("result", res_plotted)
# cv2.waitKey(0)


# result = detect_car(base64.b64encode("./car_type/nocar.jpg"))
# print(result["status"], result["prediction"])