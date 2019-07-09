import numpy as np
import cv2
import datetime
import os
from time import sleep


def capture(cap, label, pause):
    start_time = datetime.datetime.now()
    i = 0
    path = label
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        add_file_name_exists = 0
        while (os.path.exists(path + str(add_file_name_exists))):
            add_file_name_exists += 1
        path += str(add_file_name_exists)
        os.makedirs(path)
    ret1, frame1 = cap.read()
    j=0
    while (True):
        diff = (datetime.datetime.now() - start_time).seconds
        #while diff % pause < pause - 1:
        cv2.putText(frame1, str(j), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 20, 220),
                        3)
        sleep(0.1)
        cv2.imshow("color", frame1)
        #diff = (datetime.datetime.now() - start_time).seconds
        ret1, frame1 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return
        cv2.imwrite(os.path.join(path, str(i) + ".jpg"), frame1)
        start_time = datetime.datetime.now()
        i += 1
        j += 1
        if(j % 20 == 0):
            print(j)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    capture(cap, 'y', 3)

    cap.release()
    cv2.destroyAllWindows()
