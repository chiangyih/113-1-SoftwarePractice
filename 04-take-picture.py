#使用usb webcam拍照，並將照片存檔
import cv2
cap = cv2.VideoCapture(0) # 0代表第一個webcam

#按下鍵盤c鍵, 將frame存檔,按下鍵盤q鍵, 退出
while True:
    ret, frame = cap.read() # ret是一個布林值，代表是否成功讀取frame, frame用來存放抓取的影像
    cv2.imshow('Video', frame) # 顯示frame, 'Video'是視窗的名稱; frame是要顯示的影像
    
    key=cv2.waitKey(1) # cv2.waitKey(1)代表等待1毫秒,將按下的鍵盤的ASCII碼存入key
    
    if key == ord('c'): # 按c鍵存檔; cv2.waitKey(1)代表等待1毫秒, 0xFF是一個16進位的數字
        cv2.imwrite('webcam.jpg', frame) # 將frame存檔為webcam.jpg
    elif key == ord('q'):
        break
