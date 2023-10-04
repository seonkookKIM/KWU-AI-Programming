from listread import *

list, header = read()

def value():
    player_list = []
    print("[선수 명단] : [", end='')
    for i in range(30):
        print(list[i][0], end=' ')
        player_list.append(list[i][0])

    print("]\n[기록 종류] : ",header[2:15], end='')
    print("\n입력 예시 ex) [손아섭 AVG]")
    player ,recoder = input("\n[선수명과 기록 종류 입력] : ").split()

    c = header.index(recoder)
    temp = player_list.index(player)
    print(player,"선수의",recoder,"값 =>",list[temp][c])
