
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
from app.api.context.data_sets import DataSets
import pandas as pd
from app.api.context.models import Models
from icecream import ic
import numpy as np

@dataclass
class TitanicModel(object):

    model = Models() # model과 같은 구조의 인스턴스
    dataset = DataSets()

    def preprocess(self, train_fname, test_fname) -> DataSets:
        that = self.model
        this = self.dataset

        #데이터셋은 Train과 Test, Validation 3종류로 나누어져 있다.
        this.train = that.new_dataframe_no_index(train_fname)
        this.test = that.new_dataframe_no_index(test_fname)
        
        
        feature = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        
       
        this.id = this.test['PassengerId'] 
        this.label = this.train['Survived']

        self.extract_title_from_name(this)

        # this.train = self.drop_feature_in_train(this, 'Survived')
        # this.train = self.drop_feature_in_train(this,'SibSp','Parch','Cabin','Ticket')
        # this.test = self.drop_feature_in_test(this,'SibSp','Parch','Cabin','Ticket')
        

        title_mapping = self.remove_duplicate_title(this)

        
        this = self.title_nominal(this, title_mapping)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.embarked_nominal(this)
        this = self.sex_nominal(this)

      

        this = self.drop_feature(this, 'PassengerId', 'Name', 'Age', 'Fare', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Sex')

        # this = self.drop_feature(this,'SibSp','Parch','Cabin','Ticket')
        # this = self.drop_feature(this, 'Name')
        # this = self.drop_feature(this,'Sex')
        # this = self.drop_feature(this,'Age')
        # this = self.drop_feature(this,'Fare')
        this.train = this.train.drop(['Survived'], axis=1)

        this.train.fillna(0, inplace=True)
        this.test.fillna(0, inplace=True)

        
        
        self.df_info(this)

        # self.ds.info(this)
        # k_fold = self.create_k_fold()
        # accuracy = self.get_accuracy(this, k_fold)
        # ic(accuracy)

        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        print(accuracy)

 
        return this
    

    def df_info(self, this:DataSets) -> None:
        print('='*50)
        print(f'1. Train 의 type 은 {type(this.train)} 이다.')
        print(f'2. Train 의 column 은 {this.train.columns} 이다.')
        print(f'3. Train 의 상위 1개의 데이터는 {this.train.head()} 이다.')
        print(f'4. Train 의 null 의 갯수는 {this.train.isnull().sum()} 이다.')
        print(f'4-1. {this.train.isin({0, 1, 2, 3, 4, 5, 6, 7, 8}).sum() == this.train.count()}')
        print(f'5. Test 의 type 은 {type(this.test)} 이다.')
        print(f'6. Test 의 column 은 {this.test.columns} 이다.')
        print(f'7. Test 의 상위 1개의 데이터는 {this.test.head()} 이다.')
        print(f'8. Test 의 null 의 갯수는 {this.test.isnull().sum()} 이다.')
        print('='*50)

    # @staticmethod
    # def drop_feature_in_train(this, *feature) -> object: # * -> List 

    #     [i.drop(j, axis=1, inplace=True) for j in feature for i in[this.train]]      


    #     return this #  로컬 전역this에 담김
    # @staticmethod
    # def drop_feature_in_test(this, *feature) -> object: # * -> List 

    #     [i.drop(j, axis=1, inplace=True) for j in feature for i in[this.test]]      

    #     return this #  로컬 전역this에 담김
   
             

    @staticmethod
    def drop_feature(this:DataSets, *feature:str) -> DataSets: # * -> List 

        # 1) List for문   inplace=True 없음
        # for i in feature: 
        #     this.train = this.train.drop([i], axis=1) # 하나씩 지우는 코드
        #     this.test = this.test.drop([i], axis=1)


        # 2) Map for문  inplace=True  있음
        # for i in [this.train, this.test]: # 한번에  지우는 코드
        #    for j in feature:
        #        i.drop(j, axis=1, inplace=True)

        # 3) 자바처럼 담아서 주지 않아도 되는 구조 (담거나 return을 안해도 된다.)
        # inplace=True 있음  this가 전역 this임 그 자체

        [i.drop([*feature], axis=1, inplace=True) for i in [this.train, this.test]]      

        return this #  로컬 전역this에 담김

    @staticmethod
    def extract_title_from_name(this:DataSets) -> pd.DataFrame:
        for i in [this.train, this.test]:
            i['Title'] = i['Name'].str.extract('([A-Za-z]+)\.', expand=False)
        return this 
    
    @staticmethod
    def remove_duplicate_title(this:DataSets) -> pd.DataFrame:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
            a = list(set(a))
            print(a)
            '''
            ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
             'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
            Royal : ['Countess', 'Lady', 'Sir']
            Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
            Mr : ['Mlle']
            Ms : ['Miss']
            Master
            Mrs
            '''
            title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Royal": 5, "Rare": 6}

            return title_mapping
        
    @staticmethod
    def title_nominal(this:DataSets, title_mapping:map) -> pd.DataFrame:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this
    
    
    @staticmethod
    def sex_nominal(this:DataSets) -> pd.DataFrame:
        gender_mapping = {'male':0, 'female':1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def embarked_nominal(this:DataSets) -> pd.DataFrame:
        gender_mapping = {'S':1, 'C':2, 'Q':3}
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].fillna('S')
            these['Embarked'] = these['Embarked'].map(gender_mapping)
        return this
                
    
    @staticmethod
    def age_ratio(this:DataSets) -> pd.DataFrame:
        train = this.train
        test = this.test
        age_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult':6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5) # 왜 NaN 값에 -0.5 를 할당할까요 ?
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이것을 이해해보세요
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']

        for these in train, test:
            # pass #pd.cut()을 사용하시오. 다른 곳은 고치지 말고 다음 두줄만 수정하시오
            these['Age'] = pd.cut(these['Age'], bins, labels=labels) # cut() 사용 # ordinal로 변환
            these['AgeGroup'] = these['Age'].map(age_mapping) # map() 사용 # nominal로 변환

        return this
    
    @staticmethod
    def fare_ratio(this:DataSets) -> pd.DataFrame:
        fare_mapping = {'Unknown':0, 'Low':1, 'Middle':2, 'High':3}
        labels = ['Unknown','Low','Middle','High']
        this.train['Fare'] = this.train['Fare'].fillna(-0.5)
        this.test['Fare'] = this.test['Fare'].fillna(-0.5)
        bins=[-1, 8, 15, 31, np.inf]
        for these in [this.train, this.test]:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=labels)
            these['FareBand'] = these['FareBand'].map(fare_mapping)
        return this
    
   
    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)
    
    @staticmethod
    def learning(self, train_fname, test_fname) -> object:
        this = self.preprocess(train_fname, test_fname)
        print(f'학습 시작')
        k_fold = self.create_k_fold()
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        return this

    @staticmethod
    def get_accuracy(this, k_fold) -> object:
        score = cross_val_score(RandomForestClassifier(), this.train, this.label, cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2) # 소수점 2자리까지 반올림