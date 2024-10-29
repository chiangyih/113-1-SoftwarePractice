#使用usb webcam,並且將webcam影像顯示在視窗中
import cv2
cap = cv2.VideoCapture(0) # 0代表第一個webcam
while True:
    ret, frame = cap.read() # ret是一個布林值，代表是否成功讀取frame, frame用來存放抓取的影像
    cv2.imshow('Video', frame) # 顯示frame, 'Video'是視窗的名稱; frame是要顯示的影像
    if cv2.waitKey(1) & 0xFF == ord('q'): # 按q鍵退出; cv2.waitKey(1)代表等待1毫秒, 0xFF是一個16進位的數字
        break
