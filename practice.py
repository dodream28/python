"""
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[] 2번째 손님 ( 소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[] 50번째 손님 ( 소요시간 : 16분)

총 탑승 승객 : 2 분

"""
from random import *

time = range(5, 51)
Pick = []

for i in range(1, 51):
    timeset = sample(time, 1)
    mit = timeset[0]
    if 5 <= mit <16 :
        Pick.append("pickup")
        print("[0] {}번째 손님 (소요시간 : {}분)".format(i, mit))

    else :
        print("[] {}번째 손님 (소요시간 : {}분)".format(i, mit))

    if i == 50 :
        print("총 탑승 승객 : {}명".format(len(Pick)))
# print("총 탑승 승객 : {}분".format())
