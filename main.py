# from random import choice
# from Acquaint import Acquaint
# import choice
import random
from random import choice


class Account:
    def __init__(self, name, wish, attempts=0, primogem=1600):
        self.name = name
        self.wish = wish
        self.attempts = attempts
        self.primogem = primogem

    # This takes in the parameter "wish" in order to see which type of wish is chosen. Whichever is chosen, attempts is then sent to the method chosen.
    def choosewish(self, wish, attempts, primogem):
        if self.wish == 'Acquaint':
            return self.Acquaint(self.attempts, self.primogem)
        elif self.wish == 'Intertwined':
            return self.Intertwined(self.attempts, self.primogem)

    # This takes away 160 primogems from the user and runs the Intertwined wish
    def Intertwined(self, attempts, primogems):
        for attempt in range(attempts):
            self.primogem -= 160
            # return self.Intertwinedpull(1)

    # This takes away 160 primogems from the user and runs the Acquaint wish
    def Acquaint(self, attempts, primogems):
        for attempt in range(attempts):
            self.primogem -= 160
            # return self.AcquaintPull(1)

    class AcquaintPull(Account):

        def __init__(self, chance, attempts):
            self.chance = chance
            super(attempts)

        # This takes in
        def Acquaintchances(self, chance, attempts):
            for attempt in range(self.attempts):
                self.chance = random.randrange(0, 10000, 3)
                if self.chance >= 0 and self.chance <= 50:
                    five = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona', 'Qiqi', 'Amos\' Bow', 'Lost Prayer to the Sacred Winds',
                            'Wolf\'s Gravestone', 'Skyward Blade', 'Skyward Harp', 'Skyward Atlas', 'Skyward Spine', 'Skyward Pride', 'Aquila Favonia']
                    random_five = choice(five)
                    print(f'CONGRATULATIONS! YOU GOT A 5 STAR {random_five}.')
                if self.chance >= 51 and self.chance <= 510:
                    four = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                            'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
                    random_four = choice(four)
                    print(f'Nice! You got a 4 star {random_four}.')
                else:
                    three = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                             'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                    random_three = choice(three)
                    print(
                        f'Oof... You got a 3 star {random_three}. Better Luck next time!')

        def Intertwinedchances(self):
            for attempt in range(self.attempts):
                self.chance = random.randrange(0, 10000, 3)
                if self.chance >= 0 and self.chance <= 50:
                    five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
                             'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
                    random_five2 = choice(five2)
                    print(
                        f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five2}**.')
                if self.chance >= 51 and self.chance <= 510:
                    four2 = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                             'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
                    random_four2 = choice(four2)
                    print(f'Nice! You got a 4 star *{random_four2}*.')
                else:
                    three2 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                              'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                    random_three2 = choice(three2)
                    print(
                        f'Oof... You got a 3 star {random_three2}. Better Luck next time!')


    # def pull(self, wish):
    #     if wish == 'Acquaint':
    #         print('Pulled with Acquaint')
    #     elif wish == 'Intertwined':
    #         print('Pulled with Intertwined')
    #         # Pull for Intertwined
    #     else:
    #         print(
    #             'This is not a type of fate. Try again (Check your spelling and capitalization!)')
# When you do
if __name__ == "__main__":
    account_one = Account("acc1", 'Acquaint')
    accounttwo = Account("acc2", 'Intertwined')
    account_one.Intertwined(10, 1600)


#   Questions:

# 1. How do I pass the values to a subclass's method

# 2. For choice(), I got the error "Too many positional arguments for method callpylint(too-many-function-args)" How can I fix this?
