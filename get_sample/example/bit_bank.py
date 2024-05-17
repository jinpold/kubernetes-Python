import datetime
import random
today = datetime.datetime.now()


class Account:

    
    def __init__(self, name: str, account_number, money) -> None:
        '''
        [요구사항(RFP)]
        은행이름은 비트은행이다.
        입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
        계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
        예를들면 123-12-123456 이다.
        금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
        '''

# if __name__ == "__main__":      
#     bank_name = "비트은행"
#     name = "홍길동"
#     account_number = f'{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(100000, 999999)}'
#     money = random.randint(100, 999)
#     print(f'은행명 : {bank_name}, name : {name}, 계좌번호 : {account_number}, 금액 : {money} 만원')

    # def generate_account_number(self):
    #     return f'{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(100000, 999999)}'


        self.BANK_NAME = '비트은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def __str__(self):
        return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")}' \
               f'은행 : {self.BANK_NAME}, ' \
               f'입금자: {self.name},' \
               f'계좌번호: {self.account_number},' \
               f'금액: {self.money} 만원'
    # __str__의 목적은 문자열화를 하여 서로 다른 객체 간의 정보를 전달하는 데 사용한다.
    
    # def __repr__(self):
    #     return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")} ' \
    #            f'은행 : {self.BANK_NAME}, ' \
    #            f'입금자: {self.name},' \
    #            f'계좌번호: {self.account_number},' \
    #            f'금액: {self.money} 만원' 
    # __repr__의 목적은 객체를 문자열화하여 객체 자체를 표현하는 데 사용한다.

    @staticmethod
    def creat_account_number(these: list):
            name = input('이름')
            money = input('입금액')
            account_number = f'{myRandom(1000, 10000)}-{myRandom(10, 100)}-{myRandom(100000, 1000000)}'
            money = money
            this = Account(name, account_number, money)
            print(f'__str__ 출력')
            print(f'{this} ... 개설되었습니다.')
            print(f'__repr__ 출력')
            print(f'{this}... 개설되었습니다.')
            these.append(this)
            return these
    
    @staticmethod
    def show_account_list(these: list):
        for account in these:
            print(account)
        # [print(i) for i in these]

    def deposit(self, amount: int):
        self.money += amount
        print(f'{amount}만원 입금되었습니다. 현재 잔액: {self.money} 만원')
    
    def withdraw(self, amount: int):
        if self.money >= amount:
            self.money -= amount
            print(f'{amount}만원 출금되었습니다. 현재 잔액: {self.money} 만원')
        else:
            print('잔액이 부족합니다.')

    @staticmethod
    def find_account(these, account_number):
        for account in these:
            if account.account_number == account_number:
                return account
        print('계좌를 찾을 수 없습니다.')
        return None

    @staticmethod
    def del_account(these, account_number):
        account = Account.find_account(these, account_number)
        if account:
            these.remove(account)
            print(f'계좌 {account_number}가 삭제되었습니다.')
        


import random        


def myRandom(start, end): 
    return random.randint(start, end-1)

if __name__ == "__main__":
    these = []
    while True :
        menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지 6.계좌조회')
        if menu == '0':
            break
        if menu == '1':
            these = Account.creat_account_number(these)
        elif menu == '2':
            Account.show_account_list(these)
        elif menu == '3':
            account_number = input('입금할 계좌번호: ')
            deposit_amount = int(input('입금액: '))
            account = Account.find_account(these, account_number)
            if account:
                account.deposit(deposit_amount)
        elif menu == '4':
            account_number = input('출금할 계좌번호: ')
            withdraw_amount = int(input('출금액: '))
            account = Account.find_account(these, account_number)
            if account:
                account.withdraw(withdraw_amount)

        elif menu == '5':
            account_number = input('탈퇴할 계좌번호: ')
            Account.del_account(these, account_number)
        elif menu == '6':
            account_number = input('검색할 계좌번호: ')
            account = Account.find_account(these, account_number)
            if account:
                print(account)
        else:
            print('Wrong Number.. Try Again')
            continue