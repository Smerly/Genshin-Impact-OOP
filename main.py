# from random import choice
# from Acquaint import Acquaint
# import choice
import random
from random import choice


class Account:
    def __init__(self, name, wish, characters=[], attempts=0, primogem=1600, ):
        self.name = name
        self.wish = wish
        self.attempts = attempts
        self.primogem = primogem
        # characters remained public because it needs to be called to be printed
        self.characters = list()

    # This takes in the parameter "wish" in order to see which type of wish is chosen. Whichever is chosen, attempts is then sent to the method chosen.
    def choosewish(self, wish, attempts, primogem):
        if self.wish == 'Acquaint':
            return self.Acquaint(self.attempts, self.primogem)
        elif self.wish == 'Intertwined':
            return self.Intertwined(self.attempts, self.primogem)

    # This takes away 160 primogems from the user and runs the Intertwined wish

    def Intertwined(self, attempts, primogem):
        for attempt in range(attempts):
            self.primogem -= 160
            obj = IntertwinedPull(self.attempts)
            data = obj.Intertwinedchances(self.attempts)
            # return self.Intertwinedpull(1)

    # This takes away 160 primogems from the user and runs the Acquaint wish
    def Acquaint(self, attempts, primogem):
        for attempt in range(attempts):
            self.primogem -= 160
            obj2 = AcquaintPull(self.attempts)
            data2 = obj.Acquaintchances(self.attempts)
            # return self.AcquaintPull(1)


class Characterlist:
    def __init__(self, name, characters):
        super(name, characters)

    def checkcharacters(self, characters):
        print(f'{self.name}')
        print('The characters you currently own are')
        print(f'{self.characters}')

    def removecharacters(self, character, characters):
        self.characters.remove(character)


class AcquaintPull(Account):

    def __init__(self, attempts):
        super(attempts)

    # This takes in attempts and uses the corresponding method from what is called for above. It will keep attempting and will print out what the result of each wish is
    def Acquaintchances(self, attempts):
        for attempt in range(self.attempts):
            chance = random.randrange(0, 10000, 3)
            if chance >= 0 and chance <= 50:
                five = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona', 'Qiqi', 'Amos\' Bow', 'Lost Prayer to the Sacred Winds',
                        'Wolf\'s Gravestone', 'Skyward Blade', 'Skyward Harp', 'Skyward Atlas', 'Skyward Spine', 'Skyward Pride', 'Aquila Favonia']
                random_five = choice(five)
                print(
                    f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five}**.')
                return self.characters.append(random_five)
            if chance >= 51 and chance <= 510:
                four = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                        'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
                random_four = choice(four)
                print(f'Nice! You got a 4 star *{random_four}*.')
                return self.characters.append(random_four)
            else:
                three = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                         'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                random_three = choice(three)
                print(
                    f'Oof... You got a 3 star {random_three}. Better Luck next time!')
                return self.characters.append(random_three)


class IntertwinedPull(Account):
    def __init__(self, attempts):
        super(attempts)

    def Intertwinedchances(self, attempts):
        for attempt in range(self.attempts):
            self.chance = random.randrange(0, 10000, 3)
            if self.chance >= 0 and self.chance <= 50:
                five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
                         'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
                random_five2 = choice(five2)
                print(
                    f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five2}**.')
                return self.characters.append(random_five2)
            if self.chance >= 51 and self.chance <= 510:
                four2 = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                         'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
                random_four2 = choice(four2)
                print(f'Nice! You got a 4 star *{random_four2}*.')
                return self.characters.append(random_four2)
            else:
                three2 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                          'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                random_three2 = choice(three2)
                print(
                    f'Oof... You got a 3 star {random_three2}. Better Luck next time!')
                return self.characters.append(random_three2)


if __name__ == "__main__":
    account_one = Account(name="acc1", wish='Acquaint')
    accounttwo = Account(name="acc2", wish='Intertwined')
    account_one.Intertwined(attempts=10, primogem=1600)


#   Questions:

# 1. How do I pass the values to a subclass's method

# 2. For choice(), I got the error "Too many positional arguments for method callpylint(too-many-function-args)" How can I fix this?
