
from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd


class TitanicService:

    model = TitanicModel() # model과 같은 구조의 인스턴스

    def process(self):  #self : 자기 자신, 클래스 내부에 메소드 등록  this : @property
        print(f'프로세스 시작')
        this = self.model
        feature = ['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']

        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')

        self.df_info(this)
    
        this.id = this.test['PassengerId'] # 문제

        this = self.name_nominal(this)

        ##this = self.drop_feature(this,'Name','SibSp','Parch','Ticket','Cabin')
    
        self.df_info(this)

        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.create_train(this)

    
    @staticmethod
    def df_info(this):
        # for i in[this.train, this.test]:
        #print(f'{this.info()}') 
        [i.info() for i in [this.train, this.test]]
       
    
    @staticmethod
    def create_train(this) -> str: # 훈련 세트
        return this.train.drop('Survived', axis=1) # 0 : 행, 1 : 열 => 그러므로 해당라인에는 열을 주었음.

    
    @staticmethod
    def name_nominal(this) -> object:
        this.train['Name'] = this.train['Name'].str.extract('([A-Za-z]+)\.')
        this.test['Name'] = this.test['Name'].str.extract('([A-Za-z]+)\.')
        return this
    
    @staticmethod
    def extract_title_from_name(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i['Name'].str.extract('([A-Za-z]+)\.')
        return this
    
    @staticmethod
    def create_label(this) -> str: 
        return this.train['Survived']
    
    @staticmethod
    def pclass_ordinal(this) -> object:
        return this
    
    
    @staticmethod
    def sex_nominal(this) -> object:
        return this
    
    @staticmethod
    def embarked_nominal(this) -> object:
        return this
    
    @staticmethod
    def age_ratio(this) -> object:
        return this
    
    @staticmethod
    def fare_ratio(this) -> object:
        return this
    
   
    
    


    
        

