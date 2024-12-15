def What_focal_length(cl):
    if cl == "0":
       focal_langth_class_all = focal_langth_class4
       know_height_all = know_height4
    if cl == "1":
        focal_langth_class_all = focal_langth_class1
        know_height_all = know_height1
    if cl == "2":
       focal_langth_class_all = focal_langth_class2
       know_height_all = know_height2
    if cl == "3":
       focal_langth_class_all = focal_langth_class3
       know_height_all = know_height3
    if cl == "4":
      focal_langth_class_all = focal_langth_class0
      know_height_all = know_height0
    if cl == "5":
       focal_langth_class_all = focal_langth_class5
       know_height_all = know_height5
    if cl == "6":
       focal_langth_class_all = focal_langth_class6
       know_height_all = know_height6
    if cl == "7":
       focal_langth_class_all = focal_langth_class7
       know_height_all = know_height7
        
    return focal_langth_class_all, know_height_all


def frame_Capture(cl):
    import cv2
    import keyboard
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("לא ניתן לפתוח את המצלמה")
        exit()
    
    # לולאה לקריאת פריימים מהמצלמה
    while True:
        # קרא את הפריימים מהמצלמה
        ret, frame = cap.read()
    
        # בדוק אם הקריאה מוצלחת
        if not ret:
            print("לא ניתן לקרוא פריימים מהמצלמה")
            break

        #שליחה לפונקצייה detect שבדף Detection
        height = Detect(frame, cl)

        focal_langth_class_all, know_height_all = What_focal_length(cl)

        if height:
            distance= distans_finder(focal_langth_class_all, know_height_all, height ) 
            if distance:
                distance = int(round(distance))
                distance_str = str(distance)
                print(distance_str)
                engine.say(f"the dis is {distance_str} centimeters.")
                engine.runAndWait()
        
    
        # בדוק אם מקש 'q' נלחץ כדי לצאת מהלולאה
        if keyboard.is_pressed('q'):
            print("יציאה מהלולאה, מקש 'q' נלחץ")
            engine.say("If you want to find another object - say its name, if you want to close the listening now say close.")
            engine.runAndWait()
            break

    # שחרר את חיבור המצלמה וסגור את כל החלונות
    cap.release()


