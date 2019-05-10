class Cat:

    def __init__(self, name, preffered_food, meal_time):
        self.name = name
        self.preffered_food = preffered_food
        self.meal_time = meal_time



    def __str__(self):
       return "the cat is happy"

    def eats_at(self):
        if self.meal_time < 12:
            return " {} am".format(self.meal_time)
        elif self.meal_time < 24:
            self.meal_time = self.meal_time - 12
            return " {} pm".format(self.meal_time)


    def meow(self):
        return "my name is {} and I eat {} at {}".format(self.name, self.preffered_food, self.eats_at())

cat1 = Cat("Bob", "chocolate", 14)
print(cat1.meow())
cat2 = Cat("Marla", "Candy", 9)
print(cat2.meow())
