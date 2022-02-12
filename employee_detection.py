import cv2
from employee_faces import EmployeesFacesList

# we are getting the live feed from the door cameras
capture = cv2.VideoCapture(0)

# first lets encode the employee faces
emp = EmployeesFacesList()
emp.load_encoding_images("photos/")

# Now if we need to continuous feed
while True:
    ret, frame = capture.read()
    # Detect Faces
    face_locations, face_names = emp.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, x2), (x2, y2), (0, 0, 200), 2)
        s = ''.join(x for x in name if x.isdigit())
        print(int(s))


    cv2.imshow("Frame", frame)

    # This will stop the camera feed
    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
