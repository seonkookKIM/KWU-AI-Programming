from listread import *
list , header = read()

def record():
    while True:
        print(header[2:14], end='')
        a = input("\n기록 종류 선택 : ")
        if a in header:
            choice = header.index(a)
            break
        else:
            print("잘못된 기록을 선택하셨습니다.")
            continue
    sort_list = []
    data = []
    new = []
    for i in range(30):
        sort_list.append(list[i][choice])
    data.append(sorted(sort_list, reverse=True, key=float))
    
    with open('first.csv','w+') as f:
        f.writelines(str(data))
    print(data)
    print("[first.csv] 파일로 저장 완료")
