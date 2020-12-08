# from random import choice
# from Acquaint import Acquaint
# import choice
import random
from random import choice

# Account takes in wish, but doesn't do anything yet

# When you call .choosewish('Intertwined/Acquaint', 10), it will choose whichever you picked berween Intertwined and Acquaint and pull the amount of the second parameter entered.


class Account:

    shared_attempts = 0

    def __init__(self, name, attempts=0, characters=[], primogem=1600):
        self.name = name
        self.attempts = attempts
        self.primogem = primogem
        # characters remained public because it needs to be called to be printed
        self.characters = list()

    # This takes away 160 primogems from the user and runs the Intertwined wish

    def Intertwined(self, attempts):
        for attempt in range(attempts):
            self.primogem -= 160
            print('Intertwined')
            Account.shared_attempts = attempts

        # return self.Intertwinedchances(attempts)

    # This takes away 160 primogems from the user and runs the Acquaint wish

    def Acquaint(self, attempts):
        for attempt in range(attempts):
            self.primogem -= 160
        return self.Acquaint(attempts)

        # obj2 = AcquaintPull(self.attempts)
        # data2 = obj.Acquaintchances(self.attempts)
        # return self.AcquaintPull(1)

    # This takes in the parameter "wish" in order to see which type of wish is chosen. Whichever is chosen, attempts is then sent to the method chosen.
    # def choosewish(self, wish, attempts, primogem=1600):
    #     if self.wish == 'Acquaint':
    #         return self.Acquaint(self.attempts, self.primogem)
    #     elif self.wish == 'Intertwined':
    #         return self.Intertwined(self.attempts, self.primogem)


class Characterlist(Account):
    def __init__(self, name, characters):
        super(name, characters)

    def checkcharacters(self, characters):
        print(f'{self.name}')
        print('The characters you currently own are')
        print(f'{self.characters}')

    def removecharacters(self, character, characters):
        self.characters.remove(character)


class AcquaintPull(Account):

    def __init__(self):
        self.characters = list()
        # super().__init__(attempts)
        # self.attempts = attempts

    # This takes in attempts and uses the corresponding method from what is called for above. It will keep attempting and will print out what the result of each wish is
    def Acquaintchances(self):
        for attempt in range(Account.shared_attempts):
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
        for attempt in range(Account.shared_attempts):
            chance = random.randrange(0, 10000, 3)
            if chance >= 0 and chance <= 50:
                five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
                         'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
                random_five2 = choice(five2)
                print(
                    f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five2}**.')
                self.characters.append(random_five2)
            if chance >= 51 and chance <= 510:
                four2 = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                         'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
                random_four2 = choice(four2)
                print(f'Nice! You got a 4 star *{random_four2}*.')
                self.characters.append(random_four2)
            else:
                three2 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                          'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                random_three2 = choice(three2)
                print(
                    f'Oof... You got a 3 star {random_three2}. Better Luck next time!')
                self.characters.append(random_three2)


if __name__ == "__main__":
    account_one = Account('something')
    account_one.Intertwined(3)

    account_one_pull = IntertwinedPull()
    account_one_pull.Intertwinedchances()

    account_one.checkcharacters()
    # account_one.Intertwined(3)
    # print(account_one.characters)


# if __name__ == "__main__":
#     account_one = Account('something')
#     account_one.Intertwined(2)


#        ------class Account---------
#        |                          |
# class AcquaintPull    class IntertwinedPull
