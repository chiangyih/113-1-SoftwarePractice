#使用usb webcam拍照，並將照片存檔
import cv2
cap = cv2.VideoCapture(0) # 0代表第一個webcam
pic_no=0 #設定照片初始編號為0

#按下鍵盤c鍵, 將frame存檔,按下鍵盤q鍵, 退出
while cap.isOpened(): # 當webcam開啟時
    ret, frame = cap.read() # ret是一個布林值，代表是否成功讀取frame, frame用來存放抓取的影像
    if ret==False: # 如果沒有成功讀取frame, 則持續等待
        continue
    frame_flip = cv2.flip(frame, 1) # 將frame左右翻轉; 1代表左右翻轉, 0代表上下翻轉, -1代表上下左右翻轉
    cv2.imshow('Video', frame_flip) # 顯示frame_flip, 'Video'是視窗的名稱
    
    key=cv2.waitKey(1) # cv2.waitKey(1)代表等待1毫秒,將按下的鍵盤的ASCII碼存入key
    
    if key==ord('c'): # 按c鍵存檔
        cv2.imwrite('pic'+str(pic_no)+'.jpg',frame_flip) # 將frame_flip存檔為pic0.jpg, pic1.jpg, pic2.jpg, ...
        pic_no+=1 # 照片編號加1
    elif key==ord('q'): # 按q鍵退出
        break
    
        

