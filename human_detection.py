import cv2
import mediapipe as mp
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cap = cv2.VideoCapture(0)
while True :
    x,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        print("Human Detected")
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,i_amnot_here = img.shape
            cx,cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img,(cx,cy),5,(2,150,30),cv2.FILLED)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

    if cv2.getWindowProperty("Image",cv2.WND_PROP_VISIBLE)<1:
        break

cv2.destroyAllWindows()