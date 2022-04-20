class Philanthrop:

    def __init__(self, first_name, last_name, money):
        self.first_name = first_name
        self.last_name = last_name
        self. money = money

    def philanthrop_info(self):
        return f'Клиент "{self.first_name} {self.last_name}". Баланс: {self.money} руб.'


money_1 = Philanthrop('Иван', "Петров", 50)
print(money_1.philanthrop_info())
