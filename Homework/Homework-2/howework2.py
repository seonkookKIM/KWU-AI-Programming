import tkinter as tk
from first_option import *
from second_option import *
from listread import *
from third_option import *

list , header = read()
while True:
    print("===========================================")
    print("옵션 1 : 기록 종류에 따른 값 내림차순 정렬")
    print("옵션 2 : 팀별로 그룹지어 출력 및 저장 ")
    print("옵션 3 : 선수명과 기록 종류에 따른 값 출력")
    print("종료 : end")
    print("===========================================")
    a = input("옵션 선택 : ")
    if a == '1':
        record()    
        
    elif a == '2':
        sort()
        
    elif a == '3':
        value()

    elif a == 'end':
        print("프로그램을 종료합니다.")
        break
    else:
        print("\n\n잘못된 옵션 입력")