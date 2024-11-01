# a向量 dot b向量=x1*x2+y1*y2
# a向量 dot b向量=|a向量|*|b向量|*cos(θ) ，θ是a向量和b向量的夾角
# x1*x2+y1*y2=|a向量|*|b向量|*cos(θ)
# |a向量|=math.sqrt(x1**2+y1**2) ；計算a向量的長度
# |b向量|=math.sqrt(x2**2+y2**2) ；計算b向量的長度
# cos(θ)=(x1*x2+y1*y2)/(|a向量|*|b向量|)
import math
a=[1,1]
b=[2,1]
c=[2,2]

#計算b角度
# 利用ba向量和bc向量的夾角


# 計算a、b夾角
def angle(a,b):
    ab_length=math.sqrt(((b[1]-a[1])**2+(b[0]-a[0])**2)) #計算ab向量的長度
    bc_length=math.sqrt(((b[1]-c[1])**2+(b[0]-c[0])**2)) #計算bc向量的長度


# # 計算b、c夾角
# def angle(b,c):
#     return math.degrees(math.acos(b[0]*c[0]+b[1]*c[1]/(math.sqrt(b[0]**2+b[1]**2)*math.sqrt(c[0]**2+c[1]**2))))
                        
# # 計算a、c夾角
# def angle(a,c):
#     return math.degrees(math.acos(a[0]*c[0]+a[1]*c[1]/(math.sqrt(a[0]**2+a[1]**2)*math.sqrt(c[0]**2+c[1]**2))))

print(angle(a,b)) # 90.0
# print(angle(b,c)) # 60.0
# print(angle(a,c)) # 30.0