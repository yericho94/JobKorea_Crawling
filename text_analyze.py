import numpy as np 
import pandas as pd 
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib import pyplot as plt
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


df=pd.read_excel('sample1.xlsx',header=0)
#df[['합격자 토익','합격자 수상횟수','지원자 수']] = df[['합격자 토익','합격자 수상횟수','지원자 수']].apply(pd.to_numeric, errors='coerce') 
df['회사 직원 수']=(pd.to_numeric(df['회사 직원 수'].replace(',',''), errors='coerce'))
df['평균 연봉']=(pd.to_numeric(df['평균 연봉'].replace(',',''), errors='coerce'))

if df['회사 설립년도'].any()=="년차)":
	df['회사 설립 년도']=df['회사 직원 수']
	df['회사 직원 수']=''

df['회사 설립년도']=(pd.to_numeric(df['회사 설립년도'].replace(',',''), errors='coerce'))

print(df.info())
print(df.head())

df.to_excel("sample5.xlsx")
