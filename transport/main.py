from transport import Client, Truck, Train, TransportCompany

Status = True
all_clients = []
all_vehicles = []
all_company = []


def print_menu():
    print("Меню")
    print(f"1 - Создать клиента")
    print(f"2 - Управлять транспортом")
    print(f"3 - Управлять компаниями")
    print(f"4 - Вывести информацию о всех клиентах")
    print(f"5 - Вывести информацию о всех транспортах")
    print(f"6 - Вывести информацию о всех компаниях")
    print(f"7 - Выход")

def print_vehicle_menu():
    print(" Управлять транспортом ")
    print(f"1 - Создать грузовик")
    print(f"2 - Создать поезд")
    print(f"3 - Загрузить груз клиента в транспорт")

def print_company_menu():
    print(" Управлять компаниями ")
    print(f"1 - Создать компанию")
    print(f"2 - Добавить транспортное средство в компанию")
    print(f"3 - Список всех транспортных средств компании")
    print(f"4 - Добавить клиента в компанию")
    print(f"5 - Распределить грузы клиентов по транспортным средствам")

while Status:
    print_menu()
    input_data = input("Введите номер: ")
    try:
        input_data = int(input_data)
    except ValueError:
        print("Введите корректное значение!")
    if input_data == 1:
        name = input("Введите имя нового клиента: ")
        cargo = input("Введите вес груза нового клиента: ")
        while True:
            is_vip = input("Укажите, является ли новый клиент VIP? (1 - да / 2 - нет) ")
            if is_vip == "1":
                is_vip = True
                break
            elif is_vip == "2":
                is_vip = False
                break
            else:
                print("Введите корректное значени (1 или 2)")
        try:
            cargo = int(cargo)
            if cargo >= 0:
                all_clients.append(Client(name, cargo, is_vip))
                print("Новый клиент был успешно создан!")
            else:
                print("Введите корректное значение веса груза нового клиента!")
        except ValueError as e:
            print(f"Ошибка: {e}")
    elif input_data == 2:
        print_vehicle_menu()
        input_data = input("Введите номер: ")
        try:
            input_data = int(input_data)
        except ValueError:
            print("Введите корректное значение!")
        if input_data == 1:
            capacity = input("Введите грузоподъемность грузовика: ")
            color = input("Введите цвет грузовика: ")
            try:
                capacity = int(capacity)
                if capacity >= 0:
                    if not color.isalpha():
                        raise ValueError("Цвет грузовика должен содержать только буквы.")
                    all_vehicles.append(Truck(capacity, color))
                    print("Грузовик создан!")
                else:
                    print("Введите корректное значение грузоподъемности!")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif input_data == 2:
            capacity = input("Введите грузоподъемность поезда: ")
            number_of_cars = input("Введите количество вагонов: ")
            try:
                capacity = int(capacity)
                number_of_cars = int(number_of_cars)
                if capacity >= 0 and number_of_cars >= 0:
                    all_vehicles.append(Train(capacity, number_of_cars))
                    print("Поезд создан!")
                else:
                    print("Введите корректное значение грузоподъемности и количества вагонов!")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif input_data == 3:
            target_vehicle = input("Введите номер транспорта, в который хотите загрузить груз клиента: ")
            target_client = input("Введите номер клиента, груз которого хотите загрузить: ")
            try:
                target_vehicle = int(target_vehicle)
                target_client = int(target_client)
                all_vehicles[target_vehicle - 1].load_cargo(all_clients[target_client - 1])
                print("Груз успешно загружен!")
            except Exception as e:
                print(f"Возникла ошибка! Проверьте корректность введенных данных! Ошибка: {e}")
    elif input_data == 3:
        print_company_menu()
        input_data = input("Введите номер: ")
        try:
            input_data = int(input_data)
        except ValueError:
            print("Введите корректное значение!")
        if input_data == 1:
            name = input("Введите название компании: ")
            company = TransportCompany(name)
            all_company.append(company)
            print("Компания успешно создана!")
        elif input_data == 2:
            target_vehicle = input("Введите номер транспорта, который хотите добавить в компанию: ")
            target_company = input("Введите номер компании, к которой хотите добавить транспорт: ")
            try:
                target_company = int(target_company)
                target_vehicle = int(target_vehicle)
                all_company[target_company - 1].add_vehicle(all_vehicles[target_vehicle - 1])
                print("Транспорт успешно добавлен!")
            except Exception as e:
                print(f"Произошла ошибка! Проверьте корректность введенных данных! Ошибка: {e}")
        elif input_data == 3:
            target_company = input("Введите номер компании, список транспорта которой вы хотите посмотреть: ")
            try:
                target_company = int(target_company)
                print(f"Список транспорта компании с идентификатором {target_company}:")
                target_company -= 1
                id = 0
                for vehicle in all_company[target_company].list_vehicles():
                    id += 1
                    print(f"{id}. {vehicle}")
            except ValueError:
                print("Введите корректное значение!")
        elif input_data == 4:
            target_company = input("Введите номер компании, куда хотите добавить клиента: ")
            target_client = input("Введите номер клиента, которого хотите добавить в компанию: ")
            try:
                target_company = int(target_company)
                target_client = int(target_client)
                all_company[target_company - 1].add_client(all_clients[target_client - 1])
                print("Клиент успешно добавлен!")
            except ValueError:
                print("Введите корректное значение!")
        elif input_data == 5:
            target_company = input("Введите номер компании, где хотите распределить груз: ")
            try:
                target_company = int(target_company)
                all_company[target_company - 1].optimize_cargo_distribution()
            except ValueError:
                print("Введите корректное значение номера компании!")
    elif input_data == 4:
        id = 0
        for client in all_clients:
            id += 1
            vip = "Да" if client.is_vip else "Нет"
            print(f"{id}. Имя: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip}")
    elif input_data == 5:
        id_number = 0
        for vehicle in all_vehicles:
            id_number += 1
            print(f"{id_number}. {vehicle}")
        print()
    elif input_data == 6:
        id = 0
        for company in all_company:
            id += 1
            print(f"{id}. Название компании: {company.name}")
            print(f"| Список транспортных средств: ")
            for vehicle in company.list_vehicles():
                print(f"| {vehicle}")
            print(f"| Список клиентов компании: ")
            for client in company.list_clients():
                vip = "Да" if client.is_vip else "Нет"
                print(f"| Имя клиента: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip}")
    elif input_data == 7:
        Status = False
        print("Выход.")
