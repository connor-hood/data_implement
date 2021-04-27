import secrets


class Sweepstakes:
    def __init__(self):
        self.contestants = []

    def enter_contest(self, name):
        self.contestants.append(name)
        print(self.contestants)

    def draw_winner(self):
        print(f'The winner is: {secrets.choice(self.contestants)}')

