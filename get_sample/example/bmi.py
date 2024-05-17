from example.utils import Member


class BMI():
    def __init__(self) -> None:
        '''utils.py / Members(), myRandom() 를 이용하여 BMI 지수를 구하는 계산기를 작성합니다.'''

    def getBMI(self, height: float, weight: float) -> float:
        this = Member()
        this.name= '홍길동'
        this.height = 170.8
        this.weight = 80.5
        res = this.weight / (this.height/100)**2
        if res < 18.5:
            return '저체중'
        elif 18.5 <= res < 23:
            return '정상'
        elif 23 <= res < 25:
            return '과체중'
        elif 25 <= res < 30:
            return '비만'
        