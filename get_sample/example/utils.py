import random

def myRandom(start, end): return random.randint(start, end-1) 

def my100(): return myRandom(1,100)  #자바기준 Math.random() 과 같다.

def memberlist() -> []: # type: ignore
    return ['홍정명', '노홍주', '전종현', '정경준', '양정오',
           "권혜민", "서성민", "조현국", "김한슬", "김진영",
           '심민혜', '권솔이', '김지혜', '하진희', '최은아',
           '최민서', '한성수', '김윤섭', '김승현',
           "강 민", "최건일", "유재혁", "김아름", "장원종"]