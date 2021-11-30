import math
import random
import sys

def l(g, m):
    return round(g - math.log(m, 2.5))
def g1brighterg2(g1, g2):
    return pow(2.5, abs(g2 - g1))
def gradefn(g, brighter):
    return l(g, brighter)
def grade10pc(g, p):
    return l(g, pow(p/10, 2))
def gradebb(b):
    return round(math.log(b, 2.5))
def pcbytd(td):
    return round(1/td, 1)

#flags = set(arg[0] == "-" for arg in sys.argv)
qs = []
aws = []
i = 0

def m():
    print(qs[-1])
    t = input()
    if(t.upper() == "EXIT"):
        print(qs)
        print(aws)
        exit()
    if(t == str(aws[-1])):
        print("정답")
    else:
        print(aws[-1])

while True:
    g1 = random.randint(-3, 6)
    g2 = 0
    b = random.choice([2.5, 6, 16, 40, 100])
    d = random.choice([25, 100, 40])
    td = round(random.uniform(0,2), 1)
    if(g1 > -3):
        g2 = random.randint(-3, g1)
    else:
        g2 = random.randint(g1, 6)
    qs.append("연주시차가 {}라면 거리는 몇 pc인가?".format(td))
    aws.append(pcbytd(td))
    m()
    qs.append("밝기 차이가 {}배 나면, 몇 등급 차이를 만드는가?".format(b))
    aws.append(gradebb(b))
    m()
    qs.append("{}등급 별은 {}등급 별과 밝기 차이가 몇배인가?".format(g1, g2))
    aws.append(round(g1brighterg2(g1, g2)))
    m()
    qs.append("{}등급 별이 {}배 밝아지면 몇 등급인가?".format(g1, b))
    aws.append(gradefn(g1, b))
    m()
    qs.append("{}pc거리의 {}등급 별의 절대 등급은 얼마인가?".format(d, g2))
    aws.append(grade10pc(g2, d))
    m()


    
# 밝기 2.5 1등급차
# 6 2등급차
# 16 3등급차
# 40 4등급차
# 100 5등급차