import pandas as pd
df = pd.read_excel('score.xlsx',index_col='지원번호')
df

# df = pd.read_excel('20122022_출생.xlsx',skiprows=2,nrows=3, usecols='B:M',index_col=0)
# df.index.name = '제목'
# df.index

# 문자열 함수
# slice : 문자열 자르기
# df_str['idx'].str.slice(1,3)
# # df_str['idx'].map(lambda x:x[1:3])  #map(함수) , lambda : 익명함수

# # split : 문자열 분리
# a_list = ['데이터,분석가','영희,철수,바둑이','국어,영어,수학,과학,사회']
# data = {"d_split":a_list}
# df_str = pd.DataFrame(data)
# s_data = df_str['d_split'].str.split(',') #배열로 분리되어 리턴
# s_data

# replace:문자열 처리, strip:공백제거


# 조건 &, |
filt  = df['키']>188  #조건식 loc
filt
df.loc[filt]

# 2개 row데이터 출력
df.loc[['1번','5번']]
# 1번학생의 키 값만 출력
df.loc['1번','키']
df.loc['1번',['이름','키']] # 1번 학생의 이름,키 출력
df.loc[['1번','5번'],['이름','키']]
df.loc['1번':'5번','국어':'사회']

# rows데이터 가져오기
df[0:3]
df[5:]
# df[[0,1,3]] #error
df.iloc[[0,1,3]]   # rows데이터 부분적으로 가져오기
df.head()
df.tail(2)

# 컬럼별 호출
df['키']
df['이름']
df[['키','이름']][1:4]
df[df.columns[[1,3,4]]][1:4]
# 컬럼만 가져오기
df.columns
df.columns[0:3]
df.columns[[1,4,6]]

df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()
df['국어'].sum()
df['키'].describe()
df['키'].info()
df['grade'].unique() # 중복제거

df['SW특기'].count() # Nan데이터는 개수에 들어가지 않음.
df['키'].nlargest(4) # 키 큰순으로 3개 가져옴.
df['키'].nsmallest(3) # 키 작은순으로 3개 가져옴

df.describe() # 컬럼별 대략적인 정보, 최소값,최대값,평균 등 확인
df.head()     # 상단 5개 출력
df.tail()     # 하단 5개 출력
df.info()     # 컬럼별 타입,크기 정보
df.values     # rows데이터 배열로 출력
df.index      # index정보
df.columns    # 컬럼 정보
df.shape      # 데이터 크기 