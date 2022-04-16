money_from_papa =20
money_daily_to_weekly = 10*7
money_expensed =50
money_in_hand = 0
week=0

while money_in_hand < 500:
    money_in_hand = money_in_hand+money_from_papa+money_daily_to_weekly-money_expensed
    week = week+1
    print("Money on week: %d is = %d" % (week, money_in_hand))
money_in_hand=0
for cweek in range(1,14):
    money_in_hand = money_in_hand+money_from_papa+money_daily_to_weekly-money_expensed
    print("Money on week: %d is = %d" % (cweek, money_in_hand))