import random
from random import choice


class Account:

    shared_attempts = 0

    def __init__(self, name, attempts=0):
        self.name = name
        self.attempts = attempts

    # This takes away 160 primogems from the user and runs the Intertwined wish

    def Intertwined(self, attempts):
        limit = 20
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = IntertwinedPull()
                account_one_pull.Intertwinedchances()
        else:
            print('Not enough to primogems to wish this many times')

    # This takes away 160 primogems from the user and runs the Acquaint wish

    def Acquaint(self, attempts):
        limit = 20
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = AcquaintPull()
                account_one_pull.Acquaintchances()
        else:
            print('Not enough to primogems to wish this many times')

    def Weapon(self, attempts):
        limit = 20
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = WeaponPull()
                account_one_pull.Weaponchances()
        else:
            print('Not enough to primogems to wish this many times')


class Whale(Account):
    shared_attempts = 0

    def __init__(self, name, attempts=0):
        self.name = name
        self.attempts = attempts

    # This takes away 160 primogems from the user and runs the Intertwined wish

    def Intertwined(self, attempts):
        limit = 20000000000
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = IntertwinedPull()
                account_one_pull.Intertwinedchances()
        else:
            print('Not enough to primogems to wish this many times')

    # This takes away 160 primogems from the user and runs the Acquaint wish

    def Acquaint(self, attempts):
        limit = 200000000000
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = AcquaintPull()
                account_one_pull.Acquaintchances()
        else:
            print('Not enough to primogems to wish this many times')

    def Weapon(self, attempts):
        limit = 200000000000
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = WeaponPull()
                account_one_pull.Weaponchances()
        else:
            print('Not enough to primogems to wish this many times')


class F2P(Account):
    shared_attempts = 0

    def __init__(self, name, attempts=0):
        self.name = name
        self.attempts = attempts

    # This takes away 160 primogems from the user and runs the Intertwined wish
    def Intertwined(self, attempts):
        limit = 10
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = IntertwinedPull()
                account_one_pull.Intertwinedchances()
        else:
            print('Not enough to primogems to wish this many times')

    # This takes away 160 primogems from the user and runs the Acquaint wish

    def Acquaint(self, attempts):
        limit = 10
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = AcquaintPull()
                account_one_pull.Acquaintchances()
        else:
            print('Not enough to primogems to wish this many times')

    def Weapon(self, attempts):
        limit = 10
        if attempts <= limit:
            for attempt in range(attempts):
                Account.shared_attempts = attempts
                account_one_pull = WeaponPull()
                account_one_pull.Weaponchances()
        else:
            print('Not enough to primogems to wish this many times')


class AcquaintPull:

    def __init__(self):
        self.characters = list()

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


class IntertwinedPull:
    def __init__(self):
        self.characters = list()

    def Intertwinedchances(self):
        for attempt in range(Account.shared_attempts):
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


class WeaponPull:
    def __init__(self):
        self.characters = list()
        # super(attempts).__init__()
        # self.attempts = attempts

    def Weaponchances(self):
        for attempt in range(Account.shared_attempts):
            chance = random.randrange(0, 10000, 3)
            if chance >= 0 and chance <= 50:
                five3 = ['Vortex Vanquisher', 'The Unforged', 'Amos\' Bow', 'Skyward Harp', 'Lost Prayer to the Sacred Winds',
                         'Skyward Atlas', 'Primordial Jade Winged-Spear', 'Skyward Spine', 'Wolf\'s Gravestone', 'Skyward Pride', 'Skyward Blade', 'Aquila Favonia']
                random_five3 = choice(five3)
                print(
                    f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five3}**.')
                return self.characters.append(random_five3)
            if chance >= 51 and chance <= 510:
                four3 = ['Favonius Warbow', 'Favonius Codex', 'Dragon\' Bane', 'The Bell', 'Lion\'s Roar', 'Rust', 'Sacrificial Bow', 'The Stringless',
                         'Eye of Perception', 'Sacrificial Fragments', 'The Widsith', 'Favonius Lance', 'Rainslasher', 'Sacrificial Greatsword', 'Favonius Greatsword', 'Sacrificial Sword', 'The Flute', 'Favonius Sword']
                random_four3 = choice(four3)
                print(f'Nice! You got a 4 star *{random_four3}*.')
                return self.characters.append(random_four3)
            else:
                three3 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                          'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
                random_three3 = choice(three3)
                print(
                    f'Oof... You got a 3 star {random_three3}. Better Luck next time!')
                return self.characters.append(random_three3)


if __name__ == "__main__":
    account_one = Account('something')
    account_one.Weapon(5)


# import random
# from random import choice


# class Account:

#     shared_attempts = 0
#     shared_characters = ['']

#     def __init__(self, name, characters=[], attempts=0, primogem=1600):
#         self.name = name
#         self.attempts = attempts
#         self.primogem = primogem
#         self.characters = list()

#     # This takes away 160 primogems from the user and runs the Intertwined wish
#     def Intertwined(self, attempts):
#         for attempt in range(attempts):
#             self.primogem -= 160
#             Account.shared_attempts = attempts
#             account_one_pull = IntertwinedPull()
#             account_one_pull.Intertwinedchances()

#     # This takes away 160 primogems from the user and runs the Acquaint wish
#     def Acquaint(self, attempts):
#         for attempt in range(attempts):
#             self.primogem -= 160
#             Account.shared_attempts = attempts
#             account_one_pull = AcquaintPull()
#             account_one_pull.Acquaintchances()

#     def Weapon(self, attempts):
#         for attempt in range(attempts):
#             self.primogem -= 160
#             Account.shared_attempts = attempts
#             account_one_pull = WeaponPull()
#             account_one_pull.Weaponchances()

#     def listCharacters(self):
#         print(self.name)
#         print(f'You currently have {self.characters}')


# class AcquaintPull:

#     def __init__(self):
#         self.characters = list()

#     # This takes in attempts and uses the corresponding method from what is called for above. It will keep attempting and will print out what the result of each wish is
#     def Acquaintchances(self):
#         for attempt in range(Account.shared_attempts):
#             chance = random.randrange(0, 10000, 3)
#             if chance >= 0 and chance <= 50:
#                 five = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona', 'Qiqi', 'Amos\' Bow', 'Lost Prayer to the Sacred Winds',
#                         'Wolf\'s Gravestone', 'Skyward Blade', 'Skyward Harp', 'Skyward Atlas', 'Skyward Spine', 'Skyward Pride', 'Aquila Favonia']
#                 random_five = choice(five)
#                 print(
#                     f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five}**.')
#                 return self.characters.append(random_five)
#             if chance >= 51 and chance <= 510:
#                 four = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
#                         'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
#                 random_four = choice(four)
#                 print(f'Nice! You got a 4 star *{random_four}*.')
#                 return self.characters.append(random_four)
#             else:
#                 three = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
#                          'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
#                 random_three = choice(three)
#                 print(
#                     f'Oof... You got a 3 star {random_three}. Better Luck next time!')
#                 return self.characters.append(random_three)


# class IntertwinedPull:
#     def __init__(self):
#         self.characters = list()

#     def Intertwinedchances(self):
#         for attempt in range(Account.shared_attempts):
#             chance = random.randrange(0, 10000, 3)
#             if chance >= 0 and chance <= 50:
#                 five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
#                          'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
#                 random_five2 = choice(five2)
#                 print(
#                     f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five2}**.')
#                 return self.characters.append(random_five2)
#             if chance >= 51 and chance <= 510:
#                 four2 = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
#                          'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
#                 random_four2 = choice(four2)
#                 print(f'Nice! You got a 4 star *{random_four2}*.')
#                 return self.characters.append(random_four2)
#             else:
#                 three2 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
#                           'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
#                 random_three2 = choice(three2)
#                 print(
#                     f'Oof... You got a 3 star {random_three2}. Better Luck next time!')
#                 return self.characters.append(random_three2)


# class WeaponPull:
#     def __init__(self):
#         self.characters = list()
#         # super(attempts).__init__()
#         # self.attempts = attempts

#     def Weaponchances(self):
#         for attempt in range(Account.shared_attempts):
#             chance = random.randrange(0, 10000, 3)
#             if chance >= 0 and chance <= 50:
#                 five3 = ['Vortex Vanquisher', 'The Unforged', 'Amos\' Bow', 'Skyward Harp', 'Lost Prayer to the Sacred Winds',
#                          'Skyward Atlas', 'Primordial Jade Winged-Spear', 'Skyward Spine', 'Wolf\'s Gravestone', 'Skyward Pride', 'Skyward Blade', 'Aquila Favonia']
#                 random_five3 = choice(five3)
#                 print(
#                     f'CONGRATULATIONS! YOU GOT A 5 STAR **{random_five3}**.')
#                 return self.characters.append(random_five3)
#             if chance >= 51 and chance <= 510:
#                 four3 = ['Favonius Warbow', 'Favonius Codex', 'Dragon\' Bane', 'The Bell', 'Lion\'s Roar', 'Rust', 'Sacrificial Bow', 'The Stringless',
#                          'Eye of Perception', 'Sacrificial Fragments', 'The Widsith', 'Favonius Lance', 'Rainslasher', 'Sacrificial Greatsword', 'Favonius Greatsword', 'Sacrificial Sword', 'The Flute', 'Favonius Sword']
#                 random_four3 = choice(four3)
#                 print(f'Nice! You got a 4 star *{random_four3}*.')
#                 return self.characters.append(random_four3)
#             else:
#                 three3 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
#                           'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
#                 random_three3 = choice(three3)
#                 print(
#                     f'Oof... You got a 3 star {random_three3}. Better Luck next time!')
#                 return self.characters.append(random_three3)


# if __name__ == "__main__":
#     account_one = Account('something')
#     account_one.Acquaint(3)


#  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------

#  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------
