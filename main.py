# from random import choice
# from Acquaint import Acquaint
# import choice
import random


class Account:
    def __init__(self, name, attempts=0, primogem=1600):
        self.name = name
        self.attempts = attempts
        self.primogem = primogem

    def Intertwined(self, attempts, primogems):
        for attempt in range(attempts):
            self.primogem -= 160
        print(self.primogem)

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
