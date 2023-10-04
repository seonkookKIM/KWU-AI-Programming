from listread import *

team_list = ['NC','LG','키움','SSG','삼성','두산','KIA','롯데','한화','KT']
list , header = read()

def sort():
    data = []
    team_player = []

    for i in range(len(team_list)): # 구현 사항 2번 팀별로 그룹짓는 부분
        player = []
        for j in range(30):
            if team_list[i] == list[j][1]:
                player.append(list[j])
        team_player.append(player)
            
    for i in range(len(team_list)):     # 팀별로 그룹지어서 출력
        print(team_player[i], sep='\n')
    
    for i in range(len(team_list)):
        data.append(team_player[i])
        data.append('\n')
    
    for i in range(len(data)):
        data[i] = str(data[i])
    
    with open('second.csv','w+') as f:
        f.write(' '.join(data))
    print("[second.csv] 파일로 저장 완료")
        