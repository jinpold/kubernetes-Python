from dataclasses import dataclass
import os
import numpy as np
import pandas as pd # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.naive_bayes import GaussianNB # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.svm import SVC # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore
from app.api.titanic.model.titanic_model import TitanicModel

class TitanicService:

    model = TitanicModel() # model과 같은 구조의 인스턴스

    def preprocess(self):  #self : 자기 자신, 클래스 내부에 메소드 등록  this : @property
        print(f'전처리 시작')
        self.model.preprocess('app/api/context/data/train.csv', 'app/api/context/data/test.csv')
        return self.model
       

    def modeling(self, model_name:str):
        print(f'모델링 시작:')
        self.model
       
    def learning(self):  # 케이스마다 정확도가 다르기 때문에 이를 반영하여 모델을 생성해야 한다.
        print(f'학습 시작')
        print(f'결정트리를 활용한 검증 정확도: ')
        print(f'랜덤포레스트를 활용한 검증 정확도: ')
        print(f'나이브베이즈를 활용한 검증 정확도: ')
        print(f'KNN를 활용한 검증 정확도: ')
        print(f'SVM를 활용한 검증 정확도: ')
        self.model
       
    
    def postprocessing(self):
        print(f'후처리 시작')
        self.model
       

    def submit(self):
        print(f'제출 시작')
        self.model
    
    


    
        

