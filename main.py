# Write Your Code In This File


# 1 Define an animal class, it should have the attributes name,breed and diet. Diet should be a list. Name and breed should be passed through the constructor.
class Animal:
    def __init__(self, name, breed, diet):
        self.name = name
        self.breed = breed
        self.diet = []

    def eat(self, food):
        self.diet.append(food)

# 2 Give the animal class an eat method that accepts a paremeter of food. This method to add the provided food to the diet list.

# 3 Define a dog class, it should accept name,breed and color as attributes. It should inherit from the animal class. Make sure to pass the dog class name and breed to the animal class! Color should only belong to the dog class.


class Dog(Animal):
    def __init__(self, name, breed, diet, color):
        super().__init__(name, breed, diet)
        self.color = color

    def bark(self):
        print('{name} barked!'.format(name=self.name))

    def what_color(self):
        print('Dog name is {name} and is {color} colored.'.format(
            name=self.name, color=self.color))


my_dog = Dog('Fido', 'Golden', 'reg', 'yellow')
# my_dog.bark()
# my_dog.what_color()

# 4 The dog class should have a 2 methods, bark and what_color. The bark method should print the name of the dog that barked, example: Fido barked! The what_color method to should tell me the name of the dog followed by what color they are.

# 5 Create a cat class.It should inherit from the animal as well. Cat should accept name,breed and has_claws as attributes. Pass the name and breed to the animal class, has_claws should be a boolean and unique to the cat class.


class Cat(Animal):
    def __init__(self, name, breed, diet, has_claws):
        super().__init__(name, breed, diet)
        self.has_claws = has_claws

    def check_has_claws(self):
        print('Has claws: {has_claws}'.format(has_claws=self.has_claws))

    def meow(self):
        print('Name is {name} and has it meowed?'.format(name=self.name))


my_cat = Cat('Kitty', 'Calico', 'Tuna', True)
# my_cat.check_has_claws()
# my_cat.meow()

# 6 Give the cat class two methods: check_has_claws and meow. check_has_claws should check if the cat has claws and print a message stating whether it does or not. The meow method should print the name of the cat and if it meowed or not.

# 7 Create a new instance of the dog class and test your methods.

my_other_dog = Dog('Chance', 'Lab', 'reg', 'Chocolate')
# my_other_dog.bark()
# my_other_dog.what_color()

# 8 Make your instance of the dog class eat some food and print what food's it has eaten.

my_dog.eat('kibble')
# print(my_dog.diet)

# 9 Create a new instance of the cat class and test your methods.
my_other_cat = Cat('Catten', 'Maine Coon', 'Tuna', False)
# my_other_cat.check_has_claws()
# my_other_cat.meow()

# 10 Make your instance of the cat class eat some food and print out what food it has eaten.

my_other_cat.eat('Salmon')
print(my_other_cat.diet)
