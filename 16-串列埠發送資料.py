# 安裝pyserial套件
# pip install pyserial

import serial
import time
import sys

#初始化序列通訊埠
port="COM4" #依照狀況修改COM4
baudrate=9600 #鮑率9600

seri = serial.Serial(port, baudrate)  # 初始化序列通訊埠

try:
    while True:
        # 終端機輸入資料
        data = input("請輸入資料：")
        # 送出資料至序列通訊埠
        seri.write(data.encode())
        print("資料已送出：", data)

except (KeyboardInterrupt, serial.SerialException):
    print("找不到序列通訊埠或通訊埠被佔用！")

finally:
    seri.close()
    print("序列通訊埠已關閉")
    

