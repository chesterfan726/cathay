import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
# 1. 之後存款1000元, 確認帳戶總金額為1100元
# 2. 接續提款500元, 確認帳戶總金額為600元
# 3. 之後提款700元, 會出現 RuntimeError
#
##########################################################################################
# 建立account
    account = Customer('Test User', '100-1100')
    print('帳戶名稱:', account.name)
    print('帳戶帳號:', account.account)
# 初始金額100
    account.balance = Decimal(INIT_MONEY)
    #print(INIT_MONEY)
    print('餘額:', account.balance)
# 存入1000
    account.deposit(1000)
    print('餘額:', account.balance)
# 提出500
    account.withdraw(500)
    print('餘額:', account.balance)
# 利息10%
    interest = Decimal(CustomerDataProcess.add_interest(account,0.1))
    print('餘額:', round(interest,1))
# 提出700
    account.withdraw(700)
