import cv2 as cv
from cv2 import aruco
import numpy as np

calib_data_path =  "C:\\Users\\sayed\\Desktop\\InterIIT\\Camera Caliberation\\calib_data\\MultiMatrix.npz"
calib_data = np.load(calib_data_path)
print(calib_data.files)

cam_mat = calib_data["camMatrix"]
dist_coef = calib_data["distCoef"]
r_vector = calib_data["rVector"]
t_vector = calib_data["tVector"]

marker_size = 5.7 #in cm

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture(0)
prevx=0.0
prevy=0.0
prevz=0.0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners, marker_size, cam_mat, dist_coef)
        total_markers = range(0, marker_IDs.size)

        for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
            cv.polylines(
                frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()

            # Draw the pose of marker
            poit = cv.drawFrameAxes(frame, cam_mat, dist_coef, rVec[i], tVec[i], 3,2)
            z=prevz*0.95+round(tVec[i][0][2], 2)*0.05
            prevz=z
            z=round(z,2)
            cv.putText(
                frame,
                f"id: {ids[0]} Dist : {z}",
                top_right,
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (200, 100, 255),
                2,
                cv.LINE_AA,
            )
            # print(round(tVec[i][0][2], 2))

            cv.putText(
                frame,
                f"x : {round(tVec[i][0][0], 1)}, y : {round(tVec[i][0][1], 1)}",
                bottom_right,
                cv.FONT_HERSHEY_PLAIN,
                1.0,
                (200, 0, 0),
                2,
                cv.LINE_AA,
            )

            # print(ids, "  ", corners)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()

