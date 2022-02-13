import cv2
from mysql import connector
import pywhatkit as wkt
import datetime
now_time  = datetime.datetime.now()
import main_file
from employee_faces import EmployeesFacesList

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='##Ajay2000@##',
                        database='monitoring_database')

cur = con.cursor()

con2 = connector.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='##Ajay2000@##',
                         database='existing_database')
cur2 = con2.cursor()


def push_in_monitor(User_Id, User_Name, Contact, email, office_no, Access):
    query = "insert into monitoring_record(userId,Dname,contact,email,officeNo,Access)" \
            " values({},'{}','{}','{}',{},'{}')".format(User_Id,
                                                        User_Name,
                                                        Contact,
                                                        email,
                                                        office_no,
                                                        Access)
    print(query)
    cur2 = con.cursor()
    cur2.execute(query)
    con.commit()
    print("Done Inserting in Monitoring Table")


get_id = 10000
flag = True

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

        ## This will give the userId of the employee who is in the live feed
        s = ''.join(x for x in name if x.isdigit())
        get_id = s
        print(int(s))

    cv2.imshow("Frame", frame)

    if flag:
        main_file.helper.Pull_Data(get_id)
        emp_id = main_file.one
        emp_name = main_file.two
        emp_contact = main_file.three
        emp_email = main_file.four
        emp_office = main_file.five


        query1 = "select userId from directors"
        cur2.execute(query1)
        ids = cur2.fetchall()
        for i in ids:
            if i[0] == emp_id:
                push_in_monitor(emp_id, emp_name, emp_contact, emp_email, emp_office, 'Y')
                print("Access Granted")
                continue

        query3 = f"select roomNo from access_table where userId = {emp_id}"
        cur2.execute(query3)
        idss = cur2.fetchall()
        for i[0] in idss:
            print("Accessible Room: ",i)


        query2 = "select userId from employee"
        cur2.execute(query2)
        ids1 = cur2.fetchall()
        for i in ids:
            if i[0] == emp_id:
                push_in_monitor(emp_id, emp_name, emp_contact, emp_email, emp_office, 'N')
                wkt.sendwhatmsg(f"+91{emp_contact}", f"Greetings,{emp_name}"
                                                     f"Your office number {emp_office}"
                                                     f"your are trying to go into room"
                                                     f"which is not accessible to you"
                                                     f"please return to your work",
                                                     now_time.hour,
                                                     now_time.minute+1)

        flag = False


    # # This will stop the camera feed
    key = cv2.waitKey(1)
    if key == 27:
        break

# capture.release()
# cv2.destroyAllWindows()

print(get_id)
