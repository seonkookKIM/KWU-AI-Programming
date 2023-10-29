import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def dataframe(df):
    print("원본 데이터 프레임:")
    print(df)

def sort_dataframe(df):
    valid_columns = [col for col in df.columns if col not in ['선수명', '팀명']]
    valid_columns_str = ', '.join(valid_columns)
    print(f"기록 종류 : {valid_columns_str}")
    sort_column = input("정렬할 기록 종류를 입력 : ")
    if sort_column not in valid_columns_str:
        print("존재하지 않는 기록입니다.")
        return
    df = df.sort_values(by=sort_column, ascending=False)
    selected_columns = [sort_column, '선수명']
    sorted_plyer_df = df[selected_columns]
    print("내림차순으로 정렬된 데이터 프레임:")
    print(sorted_plyer_df)
    sorted_plyer_df.to_csv(f'sorted_data_{sort_column}.csv', index=False, encoding='utf-8-sig')
    print(f"[sorted_data_{sort_column}.csv] 파일로 저장 완료!")

def team_data(df):
    grouped_by_team = df.groupby('팀명')
    team_data_list = []
    for team_name, team_data in grouped_by_team:
        print(f"\n{team_name} 팀:")
        print(team_data)
        team_data_list.append(team_data)
    all_teams_data = pd.concat(team_data_list)
    print(all_teams_data)
    all_teams_data.to_csv('team_group.csv', index=True, encoding='utf-8-sig')
    print("[team_group.csv] 파일로 저장 완료!")

def player_value_data(df):
    player_names = df['선수명'].unique()
    player_names_str = ', '.join(player_names)
    print(f"선수명 목록: {player_names_str}")
    player_name = input("선수명 입력 : ")

    valid_columns = [col for col in df.columns if col not in ['선수명', '팀명']]
    valid_columns_str = ', '.join(valid_columns)
    print(f"기록 종류 : {valid_columns_str}")
    column_name = input("기록 입력 : ")

    player_data = df[df['선수명'] == player_name]
    if not player_data.empty:
        if column_name in player_data.columns:
            print(f"{player_name}의 {column_name} 값:")
            print(player_data[column_name].values[0])
        else:
            print(f"{column_name} 기록을 찾을 수 없습니다.")
    else:
        print(f"{player_name}를 찾을 수 없습니다.")

def teamHR_pie_chart(df):
    team_hr = df.groupby('팀명')['HR'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(team_hr, labels=team_hr.index, autopct='%1.1f%%')
    plt.title('팀별 HR (홈런) 비율')
    plt.show()

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# CSV 파일의 경로
csv_file_path = './hw2.csv'

# CSV 파일을 데이터 프레임으로 읽어오기
df = pd.read_csv(csv_file_path)

while True:
    print("\n=====원하는 기능을 선택하세요=====")
    print("1. 원본 데이터 프레임 출력")
    print("2. 특정 기록 기준 내림차순 정렬 및 출력")
    print("3. 팀별 데이터 출력 및 저장")
    print("4. 특정 선수의 특정 기록 데이터 출력")
    print("5. 팀별 HR (홈런) 비율 Pie Chart 표시")
    print("6. 종료")
    
    choice = input("입력 (1/2/3/4/5/6) : ")
    
    if choice == '1':
        dataframe(df)
    elif choice == '2':
        sort_dataframe(df)
    elif choice == '3':
        team_data(df)
    elif choice == '4':
        player_value_data(df)
    elif choice == '5':
        teamHR_pie_chart(df)
    elif choice == '6':
        break
    else:
        print("올바른 선택이 아닙니다. 다시 선택하세요.")