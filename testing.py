import random
from random import choice


def Acquaintchances(attempts):
    for attempt in range(attempts):
        chance = random.randrange(0, 10000, 3)
        if chance >= 0 and chance <= 50:
            five = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona', 'Qiqi', 'Amos\' Bow', 'Lost Prayer to the Sacred Winds',
                    'Wolf\'s Gravestone', 'Skyward Blade', 'Skyward Harp', 'Skyward Atlas', 'Skyward Spine', 'Skyward Pride', 'Aquila Favonia']
            random_five = choice(five)
            print(f'CONGRATULATIONS! YOU GOT A 5 STAR {random_five}.')

        if chance >= 51 and chance <= 510:
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


characters = []


def Intertwinedchances(attempts):

    for attempt in range(attempts):
        chance = random.randrange(0, 10000, 3)
        if chance >= 0 and chance <= 50:
            five2 = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona',
                     'Qiqi', 'Tartaglia (Childe)', 'Venti', 'Xiao', 'Zhongli']
            random_five2 = choice(five2)
            print(
                f'CONGRATULATIONS! YOU GOT A 5 STAR ** {random_five2} **.')
            characters.append(random_five2)

        if chance >= 51 and chance <= 510:
            four2 = ['Amber', 'Lisa', 'Kaeya', 'Barbara', 'Razor', 'Bennett', 'Noelle', 'Fischl',
                     'Sucrose', 'Beidou', 'Ningguang', 'Xiangling', 'Xingqiu', 'Chongyun', 'Diona', 'Xinyan']
            random_four2 = choice(four2)
            print(f'Nice! You got a 4 star * {random_four2} *.')
            characters.append(random_four2)
        else:
            three2 = ['Sling shot', 'Raven Bow', 'Thrillingg Tales of Dragon Slayers', 'Black Tassel', 'Bloodtainted Greatsword',
                      'Skyrider Sword', 'Cool Steel', 'Sharpshooter\'s Oath', 'Emerald orb', 'Magic Guide', 'Debate Club', 'Ferrous Shadow', 'Harbinger of Dawn']
            random_three2 = choice(three2)
            print(
                f'Oof... You got a 3 star {random_three2}. Better Luck next time!')
            characters.append(random_three2)


Intertwinedchances(2)
print(str(characters))
