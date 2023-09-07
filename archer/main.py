class Archer:
    def __init__(self, num_arrows, health, name):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        self.health -= 1
        if self.health <= 0: print(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows <= 0: raise Exception(f"{self.name} can't shoot")
        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.get_shot()
    


# don't touch below this line


def main():
    bard = Archer(1, 3, "Bard")
    legolas = Archer(10000, 3, "Legolas")

    while bard.health > 0 and legolas.health > 0:
        try:
            print_status(bard)
            print_status(legolas)
            bard.shoot(legolas)
        except Exception as e:
            print(e)

        try:
            print_status(bard)
            print_status(legolas)
            legolas.shoot(bard)
        except Exception as e:
            print(e)


def print_status(archer):
    print(f"{archer.name} has {archer.health} health and {archer.num_arrows} arrows")


main()