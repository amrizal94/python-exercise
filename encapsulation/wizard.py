class Wizard:
    def __init__(self, name):
        self.name = name
        self.__mana = 45
        self.__health = 65

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health
# don't touch below this line


def main():
    merlin = Wizard("Merlin")
    madame_mim = Wizard("Madame Mim")

    print_status(merlin)
    print_status(madame_mim)


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()
