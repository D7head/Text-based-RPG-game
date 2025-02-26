import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает {damage} урона! Осталось здоровья: {self.health}")

class Player(Character):
    def __init__(self, name, player_class):
        super().__init__(name, 100, 20)
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.player_class = player_class
        self.skills = {
            "Атака": 1,
            "Защита": 1,
            "Магия": 1
        }

    def gain_experience(self, amount):
        self.experience += amount
        print(f"Ты получил {amount} опыта! Текущий опыт: {self.experience}")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.attack += 5
        print(f"Поздравляем! Ты достиг уровня {self.level}! Здоровье: {self.health}, Атака: {self.attack}")

    def upgrade_skill(self, skill):
        if skill in self.skills:
            self.skills[skill] += 1
            print(f"Навык '{skill}' улучшен до уровня {self.skills[skill]}!")
        else:
            print("Такого навыка не существует.")

    def use_item(self, item):
        if item in self.inventory:
            if item == "Зелье здоровья":
                self.health += 20
                self.inventory.remove(item)
                print("Ты использовал Зелье здоровья! Здоровье восстановлено на 20.")
            else:
                print("Этот предмет не может быть использован.")
        else:
            print("У тебя нет такого предмета!")

class Monster(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

def battle(player, monster):
    print(f"\nТы встретил {monster.name}!")
    while player.is_alive() and monster.is_alive():
        action = input("Что ты хочешь сделать? (атаковать/использовать предмет): ").strip().lower()
        
        if action == "атаковать":
            monster.take_damage(player.attack)
            if monster.is_alive():
                player.take_damage(monster.attack)
        elif action == "использовать предмет":
            item = input("Какой предмет ты хочешь использовать? ").strip()
            player.use_item(item)
        else:
            print("Неверное действие!")

    if player.is_alive():
        print(f"Ты победил {monster.name}!")
        player.gain_experience(50)  
        loot = random.choice(["Зелье здоровья", "Золотая монета", None])
        if loot:
            player.inventory.append(loot)
            print(f"Ты нашел {loot}!")
        
        
        skill_choice = input("Выберите навык для улучшения (Атака/Защита/Магия): ").strip()
        player.upgrade_skill(skill_choice)

    else:
        print("Ты был повержен...")

def choose_class():
    classes = {
        "1": ("Воин", 30),
        "2": ("Маг", 20),
        "3": ("Стрелок", 25)
    }
    print("Выберите класс:")
    for key, value in classes.items():
        print(f"{key}. {value[0]} (Атака: {value[1]})")
    
    choice = input("Введите номер класса: ")
    if choice in classes:
        return Player(classes[choice][0], classes[choice][1])
    else:
        print("Неверный выбор! Выбран Воин по умолчанию.")
        return Player("Воин", 20)

def main():
    print("Добро пожаловать в текстовую RPG!")
    player_name = input("Введите имя вашего персонажа: ")
    player = choose_class()

    monsters = [
        Monster("Паук", 30, 5),
        Monster("Зомби", 50, 10),
                Monster("Дракон", 100, 15)
    ]

    while player.is_alive():
        monster = random.choice(monsters)
        battle(player, monster)

    print("Игра окончена. Спасибо за игру!")

if __name__ == "__main__":
    main()