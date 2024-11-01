# 餘弦定理
# 已知三角型三頂點座標
# 先計算三邊長
# 再利用餘弦定理計算三角形三個角度
# 三點a、b、c，對應三邊長為A、B、C
# 假設 a(0,0) b(1,0) c(1,1.732)
import math

a = [0, 0]
b = [1, 0]
c = [1, 1.732]

#計算A邊長
A = math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2)
#計算B邊長
B = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
#計算C邊長
C = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# print("A邊長:", A)  
# print("B邊長:", B)
# print("C邊長:", C)

# 依據餘弦定理計算三角形三個角度 ；cosA=(b^2+c^2-a^2)/(2*b*c)

a=math.degrees(math.acos((B**2+C**2-A**2)/(2*B*C))) #math.degrees()將弧度轉換為角度；
b=math.degrees(math.acos((A**2+C**2-B**2)/(2*A*C)))
c=math.degrees(math.acos((A**2+B**2-C**2)/(2*A*B)))

print("角度a:", a)
print("角度b:", b)
print("角度c:", c)

