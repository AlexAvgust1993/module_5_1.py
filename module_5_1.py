class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название
        self.number_of_floors = number_of_floors  # Количество этажей (18 и 2 этажа)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)




# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#         self.say_info()    #<===========================================#
#                                                                         #
#     def say_info(self):                                                 #
#         print(f'Привет, меня зовут {self.name}, мне {self.age} лет')    #
#                                                                         #
#                                                                         #
# den = Human('Денис', 22)                                     #
# max = Human('Макс', 23)                                      #
# den.say_info()  #======================================================>#
# max.say_info()
