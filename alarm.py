from cv2 import barcode, imread, haveImageReader, VideoCapture, imshow, waitKey, imwrite
import sys
import os
from pyzbar.pyzbar import decode

"""if not haveImageReader("test.jpg") == True:
    cam = VideoCapture(0)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    while rval:
        imshow("preview", frame)
        rval, frame = cam.read()
        key = waitKey(20)
        if key%256 == 32:
            try:
                temp_rval, test_image = cam.retrieve()
                temp_bc = barcode.BarcodeDetector().detect(test_image)
                if temp_bc[0] != True:
                    raise TypeError("No bar`code")
            except TypeError:
                print("Part 1 Continued")
                continue
            imwrite("test.jpg", test_image)
            break
        elif key == 27:
            break
    cam.release()


image1 = imread("test.jpg")

cam = VideoCapture(0)
if cam.isOpened():
    rval, frame = cam.read()
else:
    rval = False
while rval:
    imshow("preview", frame)
    rval, frame = cam.read()
    key = waitKey(20)
    if key%256 == 32:
        try:
            temp_rval, image2 = cam.retrieve()
            temp_bc = barcode.BarcodeDetector().detect(image2)
            if temp_bc[0] != True:
                raise TypeError("No bar`code")
        except TypeError:
            print("Part 2 Continued")
            continue
        imwrite("test2.jpg", image2)
        break
    elif key == 27:
        break
cam.release()"""

image1 = imread("barcode_test.jpg")
image2 = imread("barcode_test2.png")
result = decode(image1)
for i in result:
    print(i.data.decode("utf-8"))
"""n = 0 
while n < 4:
    try:
        if image1_bc[n][0] == image2_bc[n][0] and image1_bc[n][1] == image2_bc[n][1]:
            n += 1
            print("True")
        else:
            raise TypeError("Not the same barcode")
    except TypeError:
        print("Part 3 Continued")
        os.remove("test2.jpg")
        sys.exit(0)
os.remove("test2.jpg")
print("SUCCESS")"""