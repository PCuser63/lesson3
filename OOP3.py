class Human:
    default_name = "Jack"
    default_age = 44
    default_money = 10000
    deault_home = True
    def __init__(self,name,age,money,home):
        self.name = name
        self.age = age
        self.__money = money
        self.__home = home
    def info(self):
        print(f" Имя: {self.name} \n Возраст: {self.age} \n Капитал: {self.__money} \n Дом: {self.__home}")
    def default_info():
        print(f" Имя: {Human.default_name} \n Возраст: {Human.default_age} \n Капитал: {Human.default_money} \n Дом: {Human.deault_home}")
    def make_deal(self,home,price):
        self.__money -= price
        self.__home = home
        print(f"Остаток средств: {self.__money}")
    def earn_money(self,add_money):
        self.__money += add_money
    def buy_house(self,home,discount):
        final_price = home.price - discount
        if self.__money < final_price:
            print("Денег недостаточно для покупки дома")
        else:
            self.make_deal(home,final_price)

class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price
    def final_price(self,discount):
        print("Конечная цена, учитывая скидку: ",self.price - discount)

class SmallHouse(House):
    area = 40
    def __init__(self,price):
        self.price = price
        self.area = SmallHouse.area

    


default = Human.default_info()
jack = Human("Jack",45,100,False)
jack.info()
h = SmallHouse(400)
jack.buy_house(h,1)
jack.earn_money(100000)
jack.buy_house(h,1)
