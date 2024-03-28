def get_integer(prompt):
    money = int(input(prompt))
    return money

def exchange(money):
    c500 = money // 500
    s = money % 500
    c100 = s // 100
    d = s % 100
    c50 = d // 50
    r = d % 50
    c10 = r // 10
    print('500원 동전의 개수:', c500)
    print('100원의 동전의 개수:', c100)
    print('50원의 동전의 개수:', c50)
    print('10원의 동전의 개수:', c10)

money = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)
