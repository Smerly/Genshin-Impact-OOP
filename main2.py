# from random import choice
# from Acquaint import Acquaint
# import choice
import random
from random import choice

# Account takes in wish, but doesn't do anything yet

# When you call .choosewish('Intertwined/Acquaint', 10), it will choose whichever you picked berween Intertwined and Acquaint and pull the amount of the second parameter entered.


class Account:

    shared_attempts_intertwined = 0
    shared_attempts_acquaint = 0
    shared_characters = []

    def __init__(self, name, attempts=0, characters=[], primogem=1600):
        self.name = name
        self.attempts = attempts
        self.primogem = primogem
        self.characters = list()

    # This takes away 160 primogems from the user and runs the Intertwined wish
    def Intertwined(self, attempts):
        for attempt in range(attempts):
            self.primogem -= 160
            Account.shared_attempts_intertwined = attempts
            account_one_pull = IntertwinedPull()
            account_one_pull.Intertwinedchances()

    # This takes away 160 primogems from the user and runs the Acquaint wish
    def Acquaint(self, attempts):
        for attempt in range(attempts):
            self.primogem -= 160
            Account.shared_attempts_acquaint = attempts
            account_one_pull = AcquaintPull()
            account_one_pull.Acquaintchances()

    def checkcharacters(self):
        print(f'{self.name}')
        print('The characters you currently own are')
        print(f'{self.characters}')

    def removecharacters(self, character):
        self.characters.remove(character)


# class Characterlist(Account):
#     def __init__(self, name, characters):
#         super(name, characters)

#     def checkcharacters(self, characters):
#         print(f'{self.name}')
#         print('The characters you currently own are')
#         print(f'{self.characters}')

#     def removecharacters(self, character):
#         self.characters.remove(character)


class AcquaintPull(Account):

    def __init__(self):
        self.characters = list()
        # super().__init__(attempts)
        # self.attempts = attempts

    # This takes in attempts and uses the corresponding method from what is called for above. It will keep attempting and will print out what the result of each wish is
    def Acquaintchances(self):
        for attempt in range(Account.shared_attempts_acquaint):
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
    def __init__(self):
        self.characters = list()
        # super(attempts).__init__()
        # self.attempts = attempts

    def Intertwinedchances(self):
        for attempt in range(Account.shared_attempts_intertwined):
            chance = random.randrange(0, 10000, 3)
            if chance >= 0 and chance <= 50:
                five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
                         'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
                random_five2 = choice(five2)
                print(
                    f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five2}**.')
                return self.characters.append(random_five2)
            if chance >= 51 and chance <= 510:
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
    account_one = Account('Naniderawr')
    account_one.Intertwined(5)

    # account_one_pull = IntertwinedPull()
    # account_one_pull.Intertwinedchances()

    # account_one.checkcharacters()
    # account_one.Intertwined(3)
    # print(account_one.characters)


# if __name__ == "__main__":
#     account_one = Account('something')
#     account_one.Intertwined(2)


#        ------class Account---------
#        |                          |
# class AcquaintPull    class IntertwinedPull
