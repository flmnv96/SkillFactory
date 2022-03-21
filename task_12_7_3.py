per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму "))
deposit = list(per_cent.values())
new_dep = [int(i * money/100) for i in deposit]
print("meney = ", int(money))        # money = 100000
print("deposit = ", new_dep)         # deposit = [5600, 5900, 4280, 4000]
# Максимальная сумма, которую вы можете заработать — deposit[i]
print("Максимальная суммa которую вы можете заработать - ", max(new_dep))