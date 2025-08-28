invertory = []

def start_screen():
    while True:
        user_input = (input("Ты стоишь перед темной зловещей пещерой? Войти в нее? ")).lower()
        if user_input == "да":
            cave()
            return
        elif user_input == "нет":
            print("Ты недостаточно храбр. Попробуй другое приключение.")
            return
        elif user_input == "взять факел":
            if "факел" not in invertory:
                print("Зная что в пещере темно ты взял факел.")
                invertory.append("факел")
            else:
                print("У тебя уже есть факел.")
            continue
        else:
            print("Твой выбор непонятен.")
            continue

def cave():
        if "факел" not in invertory:
            print("Ты внутри пещеры и забыл взять факел. Даже вход не видно и довольно скоро ты погибаешь")
            print("В следующий раз попробуй взять факел")
        else:
            print("Ты зажег факел и смог выбаться. Победа.")

start_screen()
