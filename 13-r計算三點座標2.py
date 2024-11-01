import math
"""
此程式計算三個點 (a, b, c) 之間的角度。
變數:
a -- 點 a 的座標，格式為 [x, y]
b -- 點 b 的座標，格式為 [x, y]
c -- 點 c 的座標，格式為 [x, y]
計算:
1. 使用 math.atan2 計算點 a 和點 c 之間的角度 e。
2. 使用 math.atan2 計算點 b 和點 c 之間的角度 f。
3. 計算角度 e 和角度 f 之間的差值 ang，並將其轉換為度數。
輸出:
1. 角度 e 的度數表示。
2. 角度 f 的度數表示。
3. 角度差值 ang 的度數表示。
"""

a=[0,0]
b=[1,0]
c=[1,1.732]

e=math.atan2(a[1]-c[1], a[0]-c[0]) 
f=math.atan2(b[1]-c[1], c[0]-c[0]) 

ang = math.degrees( e-f )

print("e=",math.degrees(e))
print("f=",math.degrees(f))
print(ang) # 90.0