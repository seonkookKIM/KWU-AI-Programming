

print("[hw2.csv] 데이터를 읽는 중...")

def read():
        list = []
        header_list = []
        with open('hw2.csv', 'r', encoding='UTF-8') as f:
            header_list = f.readline().replace('\n','').split(',')
            lines = f.readlines() #한   줄씩
            for line in lines:
                list.append(line.split(',')) # ,를 기준으로 잘라서 LIST에 저장
            return list, header_list
                
