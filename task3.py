def result(money, procent, years):
    i = 0
    m = money
    while i < years:
        drop = (money/100) * procent
        m = m + drop
        i += 1
    print(m)

mone = float(input("начальная сумма " ))
perc = float(input("ставка "))
year = int(input("количество лет "))
result(mone, perc, year)