from example.utils import myRandom


class LeapYear:

    def __init__(self) -> None:

        print(f'utils.py myRandom() 를 이용하여 윤년계산기 객체를 생성합니다')
        print ('(ex) 2020년은 윤년입니다. 단 컴프리헨션을 사용합니다')

    def is_leap_year(self, year: int) -> bool:  # 윤년 계산기 if / swich 문 사용
        if year % 4 ==0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:   
            return True
        
    def is_leap_year_comprehension(self, year: int) -> bool:  # 윤년 계산기 컴프리헨션 사용
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def is_leap_year(self):
        y = myRandom(2000, 2024)
        s = '윤년' if (y % 4 == 0 and y % 100 !=0) or (y % 400 == 0) else '평년'
        # Python style = > String s = if () : "윤년" else : "평년"
        # Java stlye = > String s = () ? "윤년" : "평년"

        '''
        ()  ?   " " : " " ;   자바 삼항연산자

        ' ' if ( ) else ' '   파이썬 문법
        '''

        '''
        True if () else False
        y % 4 == 0 and y % 100 !=0
        s1 = '윤년' if (y % 4 == 0 and y % 100 != 0) else '평년'
        s2 = '윤년' if (y%400 ==0) else '평년'

        s3 = '윤년' if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) else '평년'
        '''
        
      