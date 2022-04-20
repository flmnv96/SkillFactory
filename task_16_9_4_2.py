from task_16_9_4_1 import Volunteer

print("СПИСОК ГОСТЕЙ:\n")
with open('volunteers.txt', 'r', encoding='utf8') as file:
    for item in file:
        print(Volunteer(*item.split()))

guest = input("\nВы нашли себя в списке?\n")

if guest == "да" or guest =="yes" or guest == "Да" or guest =="Yes":
    print("\nОтлично!")
else:
    print("\nЕсли Вас нет в списке, мы готовы вас добавить\n")
    p1 = input("Введите своё имя - ")
    p2 = input("Введите свою фамилию - ")
    p3 = input("Из какого вы города?  - ")
    p4 = input("Какой у вас статус? - ")
    new_guest = p1 + ' ' + p2 + ' ' + p3 + ' ' + p4 + '\n'
    myFile = open("volunteers.txt", 'a+', encoding='utf8')
    myFile.write(new_guest)
    myFile.close()
    print("\nВы добавлены в список гостей.\n")
    with open('volunteers.txt', 'r', encoding='utf8') as file:
        for item in file:
            print(Volunteer(*item.split()))