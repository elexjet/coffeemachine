class CoffeeMachine:
    def __init__(self, water_stack, milk_stack, beans_stack, cups_stack, money_stack):
        self.water_stack = water_stack
        self.milk_stack = milk_stack
        self.beans_stack = beans_stack
        self.cups_stack = cups_stack
        self.money_stack = money_stack

    def buy(self, coffee_type):
        if self.coffee_type == "1":
            if self.water_stack >= 250:
                self.water_stack = self.water_stack - 250
                self.beans_stack = self.beans_stack - 16
                self.cups_stack = self.cups_stack - 1
                self.money_stack = self.money_stack + 4
                print("I have enough resources, making you a coffee!")
                print()
                self.main()
            else:
                print("Sorry, not enough water!")
                print()
                self.main()
        elif self.coffee_type == "2":
            if self.water_stack >= 350:
                self.water_stack = self.water_stack - 350
                self.milk_stack =  self.milk_stack - 75
                self.beans_stack = self.beans_stack - 20
                self.cups_stack = self.cups_stack - 1
                self.money_stack = self.money_stack + 7
                print("I have enough resources, making you a coffee!")
                print()
                self.main()
            else:
                print("Sorry, not enough water!")
                print()
                self.main()
        elif self.coffee_type == "3":
            if self.water_stack >= 200:
                self.water_stack = self.water_stack - 200
                self.milk_stack =  self.milk_stack - 100
                self.beans_stack = self.beans_stack - 12
                self.cups_stack = self.cups_stack - 1
                self.money_stack = self.money_stack + 6
                print("I have enough resources, making you a coffee!")
                print()
                self.main()
            else:
                print("Sorry, not enough water!")
                print()
                self.main()
        elif self.coffee_type == "back":
            self.main()


    def fill(self, water, milk, beans, cup):
        self.water_stack += water
        self.milk_stack += milk
        self.beans_stack += beans
        self.cups_stack += cup
        self.main()


    def take(self):
        self.money_stack -= self.money_stack
        self.main()

    def printer(self, water_stack, milk_stack, beans_stack, cups_stack, money_stack):
        print(f'''The coffee machine has:
    {self.water_stack} of water
    {self.milk_stack} of milk
    {self.beans_stack} of coffee beans
    {self.cups_stack} of disposable cups
    ${self.money_stack} of money
        ''')
        self.main()

    def main(self):
        print("Write action (buy, fill, take, remaining, exit): ")
        action = str(input())
        if action == "buy":
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            self.coffee_type = input()
            self.buy(self.coffee_type)
        elif action == "fill":
            self.water = int(input("Write how many ml of water you want to add: "))
            self.milk = int(input("Write how many ml of milk you want to add: "))
            self.beans = int(input("Write how many grams of coffee beans you want to add: "))
            self.cup = int(input("Write how many disposable coffee cups you want to add: "))
            self.fill(self.water, self.milk, self.beans, self.cup)
        elif action == "take":
            print(f"I gave you ${self.money_stack}")
            print()
            self.take()
        elif action == "remaining":
            self.printer(self.water_stack, self.milk_stack, self.beans_stack, self.cups_stack, self.money_stack)
        elif action == "exit":
            exit

if __name__ == "__main__":
    coffee = CoffeeMachine(400, 540, 120, 9, 550)
    coffee.main()      # execute the main function
