
from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd


class TitanicService:

    model = TitanicModel() # model과 같은 구조의 인스턴스

    def process(self):  #self : 자기 자신, 클래스내부에 메소드 등록  this : @property
        print(f'프로세스 시작')
        this = self.model

        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')

        self.df_info(this)
        # print(f'트레인 컬럼 : {this.train.columns}')
        # print(f'테스트 컬럼 : {this.test.columns}')

        this.id = this.test['PassengerId'] # 문제
        this = self.drop_feature(this,'Name','SibSp','Parch','Ticket','Cabin')


        self.df_info(this)
        # print(f'트레인 컬럼 : {this.train.columns}')
        # print(f'테스트 컬럼 : {this.test.columns}')



        this = self.create_train(this)


    @staticmethod
    def drop_feature(this, *feature) -> object: # * -> List 

        #1) List for문   inplace=True 없음
        # for i in feature: 
        #     this.train = this.train.drop([i], axis=1) # 하나씩 지우는 코드
        #     this.test = this.test.drop([i], axis=1)


        #2) Map for문  inplace=True  있음
        # for i in [this.train, this.test]: # 한번에  지우는 코드
        #    for j in feature:
        #        i.drop(j, axis=1, inplace=True)

        #3) 자바처럼 담아서 주지 않아도 되는 구조 (담거나 return을 안해도 된다.)
        # inplace=True 있음  this가 전역 this임 그 자체

        [i.drop(j, axis=1, inplace=True) for j in feature for i in[this.train, this.test]]      

        return this #  로컬 전역this에 담김 
    
    @staticmethod
    def df_info(this):
        # for i in[this.train, this.test]:
        #print(f'{this.info()}') 
        [i.info() for i in [this.train, this.test]]
       
  

    def new_model(self, playload) -> object:
        this = self.model
        this.context = './app/api/titanic/data/'
        this.fname = playload
        return pd.read_csv(this.context + this.fname)
    
    @staticmethod
    def create_train(this) -> str: # 훈련 세트
        return this.train.drop('Survived', axis=1) # 0 : 행, 1 : 열 => 그러므로 해당라인에는 열을 주었음.

    @staticmethod
    def create_label(this) -> str: # 답
        return this.train['Survived']
    
    


    
        

