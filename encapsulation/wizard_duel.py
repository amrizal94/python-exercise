class Wizard:    
    def cast_fireball(self, target):
        # cast fireball cost 30 mana
        # If the wizard doesn't have enough mana, raise the exception {} cannot cast fireball
        if self.__mana < 20:
            raise Exception(f"{self.name} cannot cast fireball")
        
        # Otherwise, {1} casts fireball at {2} where {1} is the caster's     name and {2} is the target's name, then make sure the target is "fireballed"
        self.__mana -= 20
        print(f"{self.name} casts fireball at {target.name}")
        target.get_fireballed()

    # don't touch below this line

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        print(f"{self.name} is hit by a fireball")
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        print(f"{self.name} drinks a mana potion")
        self.__mana += 40


def main():
    merlin = Wizard("Merlin")
    madame_mim = Wizard("Madame Mim")

    while madame_mim.get_health() > 0:
        if merlin.get_mana() < 10:
            merlin.drink_mana_potion()

        try:
            print_status(merlin)
            print_status(madame_mim)
            merlin.cast_fireball(madame_mim)
        except Exception as e:
            print(e)


def print_status(wizard):
    print(
        f"{wizard.name} has {wizard.get_health()} health and {wizard.get_mana()} mana"
    )


main()
