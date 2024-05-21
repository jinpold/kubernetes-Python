import os
import sys
from dotenv import load_dotenv
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example.crime_util import Editor, Reader
from example.crime_model import CrimeModel
from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from nltk.tokenize import word_tokenize; 
from nltk import FreqDist
import googlemaps
import re
import nltk
import pandas as pd
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
from icecream import ic
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


'''
문제정의 !
서울시의 범죄현황과 CCTV현황을 분석해서
정해진 예산안에서 구별로 다음해에 배분하는 기준을 마련하시오.
예산금액을 입력하면, 구당 할당되는 CCTV 카운터를 자동으로
알려주는 AI 프로그램을 작성하시오.
'''


class CrimeService:
    def __init__(self):
        self.data = CrimeModel()
        self.data.dname = 'C:\\Users\\jinpo\\kubernetes-python\\chat-server\\get_sample\\example\\data\\'
        self.data.sname = 'C:\\Users\\jinpo\\kubernetes-python\\chat-server\\get_sample\\example\\save\\'
        self.data.crime = 'crime_in_seoul.csv'
        self.data.cctv = 'cctv_in_seoul.csv'
        self.crime_rate_columns = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['강간', '강도', '살인', '절도', '폭력']
        self.arrest_columns = ['강간검거', '강도검거', '살인검거', '절도검거', '폭력검거']

    def crime_dataframe(self) -> pd.DataFrame:
        this = self.data
        #index_col = 0 을 해야 기존 index 값이 유지된다.
        #0은 컬럼명중에서 첫번째를 의미한다 (배열구조)
        #pd.read_csv(f'경로/파일명/csv', index_col=0 = '인덱스로 지정할 column명') Index 지정
        return pd.read_csv(f'{self.data.dname}{this.crime}', encoding='UTF-8', thousands=',')
    
    def cctv_dataframe(self) -> object:
        this = self.data
        # pd.read_csv(f'경로/파일명/csv') Index를 지정하지 않음.

        return pd.read_csv(f'{self.data.dname}{this.cctv}', encoding='UTF-8', thousands=',')
           
    
    def save_model(self, fname, dframe: pd.DataFrame) -> pd.DataFrame:
        this = self.data
        '''
        풀옵션은 다음과 같다.
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',    NaN=빈값
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
        '''
        return dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')
    

    def save_police_position(self) -> None:
        station_names = []
        crime = self.crime_dataframe()
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1]) + '경찰서')
        station_addreess = []
        station_lats = []
        station_lngs = []
        reader = Reader()
        gmaps = reader.gmaps(os.environ["api_key"])
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            print(t)
            station_addreess.append(t[0].get("formatted_address"))
            t_loc = t[0].get("geometry")
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
        
        gu_names = []
        for name in station_addreess:
            tmp = name.split()
            gu_name = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        
        crime['구별'] = gu_names
        # 구 와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        crime.to_csv(f'{self.data.sname}police_position.csv')
    
    def save_cctv_population(self) -> None:
        reader = Reader()
        population = reader.excel('C:\\Users\\jinpo\\kubernetes-python\\chat-server\\get_sample\\example\\data\\pop_in_seoul', 2, 'B, D, G, J, N')
        cctv = self.cctv_dataframe()
        cctv.rename(columns={cctv.columns[0] : '구별'}, inplace=True) # inplace=True 원본을 수정하겠다.
        population.rename(columns={population.columns[0] : '구별',
                                   population.columns[1] : '인구수',
                                   population.columns[2] : '한국인',
                                   population.columns[3] : '외국인',
                                   population.columns[4] : '고령자'}, inplace=True)
        
        ic(population.head(2))
        ic(cctv.head(2))
        #population에서 Nan값이 있는지 확인 후 제거하세요
        population.drop([26], axis=0, inplace=True) #26번째 행을 제거, axis=0은 행을 의미, axis=1은 열을 의미
        population['외국인비율'] = population['외국인'].astype(int) / population['인구수'].astype(int) * 100 #외국인비율을 구하는 공식
        population['고령자비율'] = population['고령자'].astype(int) / population['인구수'].astype(int) * 100 #고령자비율을 구하는 공식
        cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], axis=1, inplace=True) #열을 제거
        cctv_per_populations = pd.merge(cctv, population, on='구별') # on='구별'을 기준으로 병합
        cor1 = np.corrcoef(cctv_per_populations['고령자비율'], cctv_per_populations['소계']) # 상관계수를 구하는 함수
        cor2 = np.corrcoef(cctv_per_populations['외국인비율'], cctv_per_populations['소계'])
        ic(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """
        cctv_per_populations.to_csv(f'{self.data.sname}cctv_population.csv')
        
    def save_crime_arrest_normalization(self)-> None:
        crime = self.crime_dataframe()
        cctv = self.cctv_dataframe()

        
        
        

        
        
if __name__ == '__main__':
    service = CrimeService()
    crime_df = service.crime_dataframe()
    cctv_df = service.cctv_dataframe()
    #service.save_police_position()
    #service.save_cctv_population()
    service.save_crime_arrest_normalization()
    # ic(crime_df)
    # ic(cctv_df)
   
    
    