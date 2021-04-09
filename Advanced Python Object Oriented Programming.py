# OOP
# 1.
class BigObject:  # creating your class
    pass


obj1 = BigObject()  # instantiate
obj2 = BigObject()  # instantiate
obj3 = BigObject()  # instantiate
print(type(obj1))


# 2.  gaming company
class PlayerCharacter:  # make it singular
    membership = True  # class object attribute (to play the game u must be a member)

    # Init/ constructor function, whatever is after self(i.e, name is a parameter). it can take default characters
    def __init__(self, name='anonymous', age=0):  # default parameters
        if self.membership:  # if PlayerCharacter.membership- membership is an attribute of PlayerCharacter
            # if age > 18:
            self.name = name  # self is used to refer to the class you create
            self.age = age  # class attributes

    def run(self):  # method
        print(f'my name is {self.name}')
        # return 'done'


player1 = PlayerCharacter('Cindy', 44)  # object
player2 = PlayerCharacter('Tom', 21)  # object
player2.attack = 50

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print(player1.run())  # when a  function doesnt return anything, we get none
# print(player1.attack) this returns an error cos player1 has no attribute attack
print(player2.attack)
# help(player1)  # this gives the entire blueprint of the object
# help(list)  # shows the blueprint
# print(player1.membership)
# print(player2.membership)
print(player1.run())
print(player2.run())


# 3.cat exercise
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('Cat1', 22)
Cat2 = Cat('Cat2', 12)
Cat3 = Cat('Cat3', 2)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


x = oldest_cat(Cat1.age, Cat2.age, Cat3.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {x} years old')


# 4. class method
class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    @classmethod
    def add_things(cls, num1, num2):  # cls stands for class
        # return num1 + num2
        return cls('Teddy', num1 + num2)  # cls can be used to instantiate, teddy rep name and the sum the age

    @staticmethod
    def add_things2(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter()
# print(player1.name)
# print(player1.add_things(2, 3))
player3 = PlayerCharacter.add_things(6, 3)  # method on the actual class(class method) to create another player
print(player3.age)


# 5 summary of oop
class NameOfClass:  # classical oop-i.e use of classes, uses camelcase)
    class_attribute = 'value'

    def __init__(self, param1, param2):  # to instantiate objects
        self.param1 = param1
        self.param2 = param2

    def method(self):  # instance method
        # code
        pass

    @classmethod
    def cls_method(cls, param1, param2):  # class method
        # code
        pass

    @staticmethod  # static method
    def stc_method(param1, param2):
        # code
        pass
    # all of this is to create our data type that models the real world


# 6 inheritance example
class User(object):  # class User: everything in python is from the base object
    def sign_in(self):
        print('logged in')

    def attack(self):  # polymorphism doing wizard1.attack() overrides this cos the method is in the wizard class
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Arthur', 500)
wizard1.sign_in()

# polymorphism
wizard1.attack()
archer1.attack()


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
# isinstance a builtin function to check for inheritance (instance, class)
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True


# 7. calling a method from a subclass of the parent class
class Gamer(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wiz(Gamer):
    def __init__(self, name, power, email):
        super().__init__(email)  # this is a better alt than the code below, it doesnt take self
        # Gamer.__init__(self, email)  # here
        self.name = name
        self.power = power


wiz1 = Wiz("Merlin", 60, "merlin@gmail.com")
print(wiz1.email)


# 8. exercise pets everywhere
class Pets(object):
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class Susan(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 2), Sally('Sally', 3), Susan('Susan', 12)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
