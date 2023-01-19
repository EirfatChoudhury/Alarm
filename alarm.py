from cv2 import barcode, imread, haveImageReader, VideoCapture, imshow, waitKey, imwrite

if not haveImageReader("test.jpg") == True:
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
            temp_rval, test_image = cam.retrieve()
            imwrite("test.jpg", test_image)
        elif key == 27:
            break
    cam.release()

else:
    image1 = imread("barcode_test.jpg")
    image2 = imread("barcode_test2.png")
    image1_bc = barcode.BarcodeDetector().detect(image1)[1][0]
    image2_bc = barcode.BarcodeDetector().detect(image2)[1][0]

    for item1 in image1_bc:
        for item2 in image2_bc:
            if item1[0] == item2[0]:
                print(True)
            else:
                print(False)