import cv2 # 匯入cv2模組
import mediapipe as mp
import time

cv2.namedWindow("finger_detection", cv2.WINDOW_NORMAL) # 設定視窗名稱,大小可自由調整
mpHands = mp.solutions.hands # 建立手部偵測物件
mpDraw = mp.solutions.drawing_utils # 建立畫圖物件

hands=mpHands.Hands(   # 建立手部偵測物件, 可以設定參數, 例如最多偵測幾隻手, 最小信心值, 最小追蹤信心值等
    static_image_mode=False, # 是否為靜態圖片, 預設為False, 表示為影片, True表示為圖片    
    model_complexity=1, # 模型複雜度, 0, 1, 2, 3, 4, 預設為1 (使用raspberry pi此行須設定)
    max_num_hands=2, # 最多偵測幾隻手, 預設為2
    min_detection_confidence=0.5, # 最小信心值, 預設為0.5
    min_tracking_confidence=0.5 # 最小追蹤信心值, 預設為0.5
)
cap=cv2.VideoCapture(0) # 開啟攝影機

while  cap.isOpened(): # 當攝影機有開啟時
    start_time=time.time() # 計時開始
    ret, frame=cap.read() # 讀取影像
    h,w,c=frame.shape # 取得影像大小, 高, 寬, 通道, 通道表示彩色影像, 灰階影像為1, 彩色影像為3
    frame_flip=cv2.flip(frame,1) # 翻轉影像, 1表示水平翻轉, 0表示垂直翻轉, -1表示水平垂直翻轉
    imgRGB=cv2.cvtColor(frame_flip,cv2.COLOR_BGR2RGB) # 將BGR影像轉換為RGB影像, 因為mediapipe只能處理RGB影像,轉換後存入imgRGB
    results=hands.process(imgRGB) # 使用手部偵測物件處理imgRGB影像, 並將結果存入results
    
    if results.multi_hand_landmarks: # 如果有偵測到手部
        for i in range(len(results.multi_handedness)): # 逐一取出每一隻手; multi_handedness是手部的資訊, 包含手部的側邊, 可以用來判斷手部是左手還是右手, 以及手部的信心值; 這裡使用len()取得手部的數量
            for coordinate_id,joint in enumerate(results.multi_hand_landmarks[i].landmark): # 逐一取出手部的關節座標,results.multi_hand_landmarks是手部的關節座標;coordinate_id是索引值(關節編號),joint是元素值
                x=int(joint.x*w) # 取得關節座標的x座標, 乘以寬度w, 並轉換為畫面上的座標, 存入x, 這裡使用int()將座標轉換為整數
                y=int(joint.y*h) # 取得關節座標的y座標, 乘以高度h, 並轉換為畫面上的座標, 存入y, 這裡使用int()將座標轉換為整數
                h,w,c=frame_flip.shape # 取得影像大小, 高, 寬, 通道, 通道表示彩色影像, 灰階影像為1, 彩色影像為3
                cv2.circle(frame_flip,(x,y),5,(255,0,0),cv2.FILLED) # 畫出手部關節座標的圓圈, 圓心座標為(x,y), 半徑為5, 顏色炫為(255,0,0), 填滿圓圈
            mpDraw.draw_landmarks(frame_flip,results.multi_hand_landmarks[i],mpHands.HAND_CONNECTIONS) # 畫出手部關節點連線, HAND_CONNECTIONS是手部關節連線的索引值, 這裡使用mpHands.HAND_CONNECTIONS取得索引值
            #使用串列，存放5個手指的初始值，初始值=0
            finger=[0,0,0,0,0] # 0表示手指未彎曲, 1表示手指彎曲,依序為拇指、食指、中指、無名指、小指
            #判斷拇指是否彎曲
            if results.multi_hand_landmarks[i].landmark[4].x<results.multi_hand_landmarks[i].landmark[3].x: # 如果食指指尖的x座標小於食指第二個關節的x座標
                finger[0]=1
            #判斷食指是否彎曲(右手)
            if results.multi_hand_landmarks[i].landmark[8].y<results.multi_hand_landmarks[i].landmark[6].y: # 如果食指指尖的y座標小於食指第二個關節的y座標
                finger[1]=1
            #判斷中指是否彎曲(右手)
            if results.multi_hand_landmarks[i].landmark[12].y<results.multi_hand_landmarks[i].landmark[10].y: # 如果中指指尖的y座標小於中指第二個關節的y座標
                finger[2]=1
            #判斷無名指是否彎曲(右手)
            if results.multi_hand_landmarks[i].landmark[16].y<results.multi_hand_landmarks[i].landmark[14].y: # 如果無名指指尖的y座標小於無名指第二個關節的y座標
                finger[3]=1
            #判斷小指是否彎曲(右手)
            if results.multi_hand_landmarks[i].landmark[20].y<results.multi_hand_landmarks[i].landmark[18].y: # 如果小指指尖的y座標小於小指第二個關節的y座標
                finger[4]=1
            #在終端機顯示手指彎曲狀態
            # print(finger)
            #使用finger[]串列，判斷手指彎曲狀態，並在終端機顯示哪根手指彎曲，當finger[0]=1時，表示拇指彎曲,finger[1]=1時，表示食指彎曲，以此類推
            finger_names = ["拇指", "食指", "中指", "無名指", "小指"]
            for idx, bent in enumerate(finger):
                if bent == 0:
                    print(f"{finger_names[idx]}彎曲")
    cv2.imshow("finger_detection",frame_flip) # 顯示畫面
    key=cv2.waitKey(1) # 等待1毫秒, 並取得鍵盤輸入值
    if key==ord('q'): # 如果按下q鍵
        break # 跳出迴圈
cap.release() # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有視窗