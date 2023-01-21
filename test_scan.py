from pyzbar import pyzbar
import cv2
import os
import sys
import csv

def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    decoded_type = []
    decoded_data = []
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()
        decoded_type.append(obj.type)
        decoded_data.append(obj.data)

    return image, decoded_type, decoded_data


if __name__ == "__main__":
    if not os.path.exists("Output.txt"):
        cam = cv2.VideoCapture(0)
        first_type_list = []
        first_data_list = []
        while not first_type_list:
            # read the frame from the camera
            retval, frame = cam.read()
            # decode detected barcodes & get the image
            # that is drawn
            frame, first_type_list, first_data_list = decode(frame)
            # show the image in the window
            cv2.imshow("Picture", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        first_type = first_type_list[0]
        first_data = first_data_list[0]
        first_csv_list = [first_type, first_data]

        with open("Output.txt", "w") as text_file:
            header = ["type", "data"]
            writer = csv.writer(text_file)
            writer.writerow(header)
            writer.writerow(first_csv_list)


        # Next save string in file and compare w/ other scans
    
    cam = cv2.VideoCapture(0)
    first_type_list = []
    first_data_list = []
    second_type_list = []
    second_data_list = []
    with open("Output.txt", "r") as text_file:
        header = next(text_file)
        reader = csv.reader(text_file)
        for row in reader:
            if row:
                first_type_list.append(row[0])
                first_data_list.append(row[1])
    n = 0
    while n == 0:
        try:
            print(second_data_list)
            print(first_data_list)
            if second_data_list != first_data_list and second_type_list != first_type_list:
                second_type_list = []
                second_data_list = []
                raise TypeError("Not same type/data")
            n = 1
        except TypeError:
            print("Activating cam")
            while not second_type_list:
                # read the frame from the camera
                retval, frame = cam.read()
                # decode detected barcodes & get the image
                # that is drawn
                frame, second_type_list, second_data_list = decode(frame)
                # show the image in the window
                cv2.imshow("Picture", frame)
                if cv2.waitKey(1) == ord("q"):
                    break
            second_data_list[0] = str(second_data_list[0])
        
    print("SUCCESS")