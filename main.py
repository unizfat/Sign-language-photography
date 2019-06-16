import numpy as np
import cv2
import datetime
import os

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
    while (True):
        diff = (datetime.datetime.now() - start_time).seconds
        while diff % pause < pause - 1:
            cv2.putText(frame1, str((pause - 1 - diff) % pause), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 20, 220), 3)
            cv2.imshow("color", frame1)
            diff = (datetime.datetime.now() - start_time).seconds
            ret1, frame1 = cap.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return
        cv2.imwrite(os.path.join(path, str(i) + ".jpg"), frame1)
        start_time = datetime.datetime.now()
        i += 1

if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    capture(cap, 'like', 5)

    cap.release()
    cv2.destroyAllWindows()