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
            hand_type=results.multi_handedness[i].classification[0].label # 取得手部的側邊, label表示左手或右手, 左手為Left, 右手為Right
            hand_joint_coordinate=results.multi_hand_landmarks[i] # 取得手部的關節座標
            mpDraw.draw_landmarks(frame_flip,hand_joint_coordinate,mpHands.HAND_CONNECTIONS) # 畫出手部關節連線, HAND_CONNECTIONS是手部關節連線的索引值, 這裡使用mpHands.HAND_CONNECTIONS取得索引值
            finger_tip_coordinate=[] # 建立空串列, 用來存放手指尖的座標
            
            for coordinate_id,joint in enumerate(hand_joint_coordinate.landmark): # 逐一取出手部的關節座標,hand_joint_coordinate.landmark是手部的關節座標;coordinate_id是索引值(關節編號),joint是元素值
                # enumerate()可以取得索引值和元素值,因此enumerate(hand_joint_coordinate.landmark)可以取得索引值(關節編號)和手部的關節座標
                x=int(joint.x*w) # 取得關節座標的x座標, 乘以寬度w, 並轉換為畫面上的座標, 存入x, 這裡使用int()將座標轉換為整數
                y=int(joint.y*h) # 取得關節座標的y座標, 乘以高度h, 並轉換為畫面上的座標, 存入y, 這裡使用int()將座標轉換為整數
                finger_tip_coordinate.append((x,y)) # 將座標(x,y)存入finger_tip_coordinate串列 
                cv2.circle(frame_flip,(x,y),5,(255,0,0),cv2.FILLED) # 畫出手部關節座標的圓圈, 圓心座標為(x,y), 半徑為5, 顏色為(255,0,0), 填滿圓圈
                cv2.putText(frame_flip,str(coordinate_id),(x,y),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2) # 在手部關節座標的位置(x,y)放置文字(關節編號), 字型為HERSHEY_PLAIN, 大小為1, 顏色為(255,255,255), 粗細為2
                
                if coordinate_id==0: # 如果手部關節座標的編號為0(手腕位置)
                    cv2.putText(frame_flip,hand_type,(finger_tip_coordinate[0][0],finger_tip_coordinate[0][1]+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2) # finger_tip_coordinate[0][0]位置在手腕的x座標, finger_tip_coordinate[0][1]位置在手腕的y座標
    
    end_time=time.time() # 計時結束
    fps=round(1/(end_time-start_time),2) # 計算FPS, 1除以(end_time-start_time), 並四捨五入到小數點後兩位
    cv2.putText(frame_flip,f"FPS:{fps}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) # 在畫面左上角放置FPS文字, 顯示FPS的值;f為格式化字串, {fps}表示要顯示的值, (10,30)為文字的位置, cv2.FONT_HERSHEY_SIMPLEX為字型, 大小為1, 顏色為(255,255,255), 粗細為2
    cv2.imshow("finger_detection",frame_flip) # 顯示畫面
    
    key=cv2.waitKey(1) # 等待1毫秒, 並取得鍵盤輸入值
    if key==ord('q'): # 如果按下q鍵
        break # 跳出迴圈
cap.release() # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有視窗