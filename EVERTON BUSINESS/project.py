import time

# list of tuples
Models = [
    Toyota := (
        'Toyota Prius- 1',
        'Toyota Supra- 2',
        'Toyota Hilux- 3',
    ),

    Honda := (
        'Honda Civic- 1',
        'Honda Accord- 2',
        'Honda Insight- 3',
    ),

    Benz := (
        'Benz GLE- 1',
        'Benz EQE SUV- 2',
        'Benz Maybach- 3',
    ),

    Lexus := (
        'Lexus ES300- 1',
        'Lexus HS- 2',
        'Lexus IS 350- 3',
    ),

    Porsche := (
        'Porsche Panamera- 1',
        'Porsche Macan- 2',
        'Porsche Taycan- 3',
    ),

    Volkswagen := (
        'Volkswagen Golf- 1',
        'Volkswagen Passat- 2',
        'Volkswagen Jetta- 3',
    ),

    Audi := (
        'Audi R8- 1',
        'Audi A4- 2',
        'Audi Quattro- 3',
    ),

    Lamborghini := (
        'Lamborghini Aventador- 1',
        'Lamborghini huracan- 2',
        'Lamborghini Urus- 3',
    ),

    Ferrari := (
        'Ferrari Enzo- 1',
        'Ferrari Testarossa- 2',
        'Ferrari Daytona- 3',
    ),

    Bugatti := (
        'Bugatti Chiron- 1',
        'Bugatti Veyron- 2',
        'Bugatti Royale- 3',
    ),

]

cars = [
        'Toyota',
        'Honda',
        'Benz',
        'Lexus',
        'Porsche',
        'Volkswagen',
        'Audi',
        'Lamborghini',
        'Ferrari',
        'Bugatti'
        ]
def car_list():
    for a in range(len(Models)):
        for i in Models[a]:
            print(f'{a+1} {i}')
            time.sleep(.5)
            continue
    print('0. Return')
    choice = input('Select Car in the format 1.1, 7.3, etc\n'
                   'Select Car: ')
    if choice.isalpha() == True:
        print('USSD must be in digits')
        return car_list()
    elif choice.isdecimal() == True:
        print('USSD must have a decimal point')
        return car_list()
    elif choice == '1.1':
        print(f'You have chosen to buy {Models[0][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[0][0]}\n'
              f'2. Buy {Models[0][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[0][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Toyota \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[0][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The Toyota Prius (/ˈpriːəs/) (Japanese: トヨタ・プリウス, Hepburn: Toyota Puriusu) is a compact/small family liftback (supermini/subcompact sedan until 2003) produced by Toyota. The Prius has a hybrid drivetrain, combined with an internal combustion engine and an electric motor.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $26,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[0][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '1.2':
        print(f'You have chosen to buy {Models[0][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[0][1]}\n'
              f'2. Buy {Models[0][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[0][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Toyota \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[0][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The most impressive fact is that with some relatively simple modifications, this engine could reach 600 horsepower without breaking. All engines have a certain limit regarding how much you can tune them before they break. That limit on the 2JZ is extremely high and this is mainly due to its design.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $30,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[0][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '1.3':
        print(f'You have chosen to buy {Models[0][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[0][2]}\n'
              f'2. Buy {Models[0][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[0][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Toyota \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[0][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $15,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('invalid input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[0][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '2.1':
        print(f'You have chosen to buy {Models[1][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[1][0]}\n'
              f'2. Buy {Models[1][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[1][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Honda \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[1][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $10,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[1][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '2.2':
        print(f'You have chosen to buy {Models[1][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[1][1]}\n'
              f'2. Buy {Models[1][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[1][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Honda \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[1][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2019\n'
                  f'{time.sleep(1)}'
                  'Price: $16,500')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[1][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '2.3':
        print(f'You have chosen to buy {Models[1][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[1][2]}\n'
              f'2. Buy {Models[1][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[1][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Honda \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[1][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2011\n'
                  f'{time.sleep(1)}'
                  'Price: N200,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[1][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '3.1':
        print(f'You have chosen to buy {Models[2][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[2][0]}\n'
              f'2. Buy {Models[2][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[2][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Benz \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[2][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $50,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[2][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '3.2':
        print(f'You have chosen to buy {Models[2][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[2][1]}\n'
              f'2. Buy {Models[2][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[2][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Benz \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[2][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $220,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[2][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '3.3':
        print(f'You have chosen to buy {Models[2][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[2][2]}\n'
              f'2. Buy {Models[2][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[2][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Benz \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[2][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2023\n'
                  f'{time.sleep(1)}'
                  'Price: $500,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[2][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '4.1':
        print(f'You have chosen to buy {Models[3][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[3][0]}\n'
              f'2. Buy {Models[3][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[3][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Lexus \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[3][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2019\n'
                  f'{time.sleep(1)}'
                  'Price: $7500')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[3][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '4.2':
        print(f'You have chosen to buy {Models[3][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[3][1]}\n'
              f'2. Buy {Models[3][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[3][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Lexus \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[3][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2018\n'
                  f'{time.sleep(1)}'
                  'Price: $8500')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[3][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '4.3':
        print(f'You have chosen to buy {Models[3][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[3][2]}\n'
              f'2. Buy {Models[3][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[3][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Lexus \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[3][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $11,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[3][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '5.1':
        print(f'You have chosen to buy {Models[4][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[4][0]}\n'
              f'2. Buy {Models[4][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[0][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Porsche \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[4][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $110,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[4][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '5.2':
        print(f'You have chosen to buy {Models[4][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[4][1]}\n'
              f'2. Buy {Models[4][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[4][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Porsche \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[4][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $45,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[4][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '5.3':
        print(f'You have chosen to buy {Models[4][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[4][2]}\n'
              f'2. Buy {Models[4][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[4][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Porsche \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[4][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $50,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[4][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '6.1':
        print(f'You have chosen to buy {Models[5][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[5][0]}\n'
              f'2. Buy {Models[5][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[5][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Volkswagen \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[5][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $200,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[5][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '6.2':
        print(f'You have chosen to buy {Models[5][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[5][1]}\n'
              f'2. Buy {Models[5][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[5][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Volkswagen \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[5][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $150,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[5][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '6.3':
        print(f'You have chosen to buy {Models[5][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[5][2]}\n'
              f'2. Buy {Models[5][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[5][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Volkswagen \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[5][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2019\n'
                  f'{time.sleep(1)}'
                  'Price: $120,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[5][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '7.1':
        print(f'You have chosen to buy {Models[6][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[6][0]}\n'
              f'2. Buy {Models[6][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[6][0]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Audi \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[6][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $200,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[6][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '7.2':
        print(f'You have chosen to buy {Models[6][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[6][1]}\n'
              f'2. Buy {Models[6][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[6][1]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Audi \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[6][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $250,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[6][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '7.3':
        print(f'You have chosen to buy {Models[6][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[6][2]}\n'
              f'2. Buy {Models[6][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[6][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Audi \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[6][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $320,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[6][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '8.1':
        print(f'You have chosen to buy {Models[7][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[7][0]}\n'
              f'2. Buy {Models[7][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[7][0]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Lamborghini \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[7][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $250,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[7][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '8.2':
        print(f'You have chosen to buy {Models[7][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[7][1]}\n'
              f'2. Buy {Models[7][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[7][1]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Lamborghini \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[7][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $220,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[7][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '8.3':
        print(f'You have chosen to buy {Models[7][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[7][2]}\n'
              f'2. Buy {Models[7][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[7][2]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Lamborghini \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[7][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2023\n'
                  f'{time.sleep(1)}'
                  'Price: $350,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[7][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '9.1':
        print(f'You have chosen to buy {Models[8][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[8][0]}\n'
              f'2. Buy {Models[8][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[8][0]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Ferrari \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[8][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $310,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[8][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '9.2':
        print(f'You have chosen to buy {Models[8][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[8][1]}\n'
              f'2. Buy {Models[8][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[8][1]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Ferrari \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[8][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2021\n'
                  f'{time.sleep(1)}'
                  'Price: $280,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[8][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '9.3':
        print(f'You have chosen to buy {Models[8][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[8][2]}\n'
              f'2. Buy {Models[8][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[8][2]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Ferrari \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[8][2]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $230,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[8][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '10.1':
        print(f'You have chosen to buy {Models[9][0]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[9][0]}\n'
              f'2. Buy {Models[9][0]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[9][0]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Bugatti \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[9][0]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2022\n'
                  f'{time.sleep(1)}'
                  'Price: $350,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[9][0]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '10.2':
        print(f'You have chosen to buy {Models[9][1]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[9][1]}\n'
              f'2. Buy {Models[9][1]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[9][1]} Details\n'
                  f'{time.sleep(1)}'
                  'Manufacturers Name: Bugatti \n'
                  f'{time.sleep(1)}'
                  f'Model: {Models[9][1]}\n'
                  f'{time.sleep(1)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2020\n'
                  f'{time.sleep(1)}'
                  'Price: $200,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[9][1]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
    elif choice == '10.3':
        print(f'You have chosen to buy {Models[9][2]}')
        print(f'Would you like too: \n'
              f'1. See more details on {Models[9][2]}\n'
              f'2. Buy {Models[9][2]}\n'
              f'0. Return')
        purchasing = input('Select Option: ')
        if purchasing == '0':
            return car_models()
        elif purchasing == '1':
            print(f'{Models[9][2]} Details\n'
                  f'{time.sleep(2)}'
                  'Manufacturers Name: Bugatti \n'
                  f'{time.sleep(0.5)}'
                  f'Model: {Models[9][2]}\n'
                  f'{time.sleep(0.5)}'
                  f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                  f'{time.sleep(1)}'
                  'Year: 2023\n'
                  f'{time.sleep(1)}'
                  'Price: $250,000')
            cow = input('0 . Return')
            if cow == '0':
                return car_list()
            else:
                print('Invalid Input')
                return car_list()
        elif purchasing == '2':
            print(f'You have requested to purchase {Models[9][2]}')
            input(f'You can make your payment to the account number: 4194194190\n'
                  f'In the description Box, input your location and whatsapp number (if any).\n'
                  f'and we\'ll send you an SMS as soon as we confirm payment')
        elif purchasing == '3':
            return car_list()
        else:
            print('Invalid input')
            return car_list()
    elif choice == '0':
        time.sleep(2)
        return car_lot()
    else:
        print('Invalid Input')
        return car_list()

def car_models():
    print('You\'ve chosen to Search Car Brands.')
    time.sleep(2)
    print('To select a car brand, write the car\'s respective index number.')
    time.sleep(2)
    print('That is, the number the car brand falls on the list.\n'
          'Input the number in the space provided')
    time.sleep(3)
    for car in range(len(cars)):
        print(f'{car+1}. {cars[car]}')
        time.sleep(1)
        continue
    print('0. Return')
    choice = input('Select Car-Model: ')
    if choice.isalpha() == True:
        print('USSD must be in digits')
        return car_lot()
    elif choice == '0':
        return car_models()
    elif choice == '1':
        # Toyota
        for i in Models[0]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[0][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on Toyota1\n'
                  f'2. Buy Toyota 1\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[0][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Toyota \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[0][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The Toyota Prius (/ˈpriːəs/) (Japanese: トヨタ・プリウス, Hepburn: Toyota Puriusu) is a compact/small family liftback (supermini/subcompact sedan until 2003) produced by Toyota. The Prius has a hybrid drivetrain, combined with an internal combustion engine and an electric motor.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[0][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[0][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on Toyota 2\n'
                  f'2. Buy Toyota 2\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[0][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Toyota \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[0][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The most impressive fact is that with some relatively simple modifications, this engine could reach 600 horsepower without breaking. All engines have a certain limit regarding how much you can tune them before they break. That limit on the 2JZ is extremely high and this is mainly due to its design.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[0][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[0][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on Toyota 3\n'
                  f'2. Buy Toyota 3\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[0][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Toyota \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[0][2]}\n'
                      f'{time.sleep(1)}\n'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[0][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Honda
    elif choice == '2':
        for i in Models[1]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[1][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on Honda 1\n'
                  f'2. Buy Honda 1\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[1][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Honda \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[1][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The first ever Honda Civic model was launched in Japan in 1972. It is the car model that garnered Honda a place in the auto market, thanks to its unique features including fuel efficiency, comfort, spacious interior, safety features, engine performance and road prowess.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[1][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[1][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[1][1]}\n'
                  f'2. Buy {Models[1][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[1][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Honda \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[1][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[1][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[1][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[1][2]}\n'
                  f'2. Buy {Models[1][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[1][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Honda \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[1][2]}\n'
                      f'{time.sleep(1)}\n'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[1][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Benz
    elif choice == '3':
        for i in Models[2]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[2][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[2][0]}\n'
                  f'2. Buy {Models[2][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[2][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Benz \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[2][0]}\n'
                      f'{time.sleep(1)}\n'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[2][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[2][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[2][1]}\n'
                  f'2. Buy {Models[2][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[2][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Benz \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[2][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[2][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[2][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[2][2]}\n'
                  f'2. Buy {Models[2][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[2][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Benz \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[2][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[2][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Lexus
    elif choice == '4':
        for i in Models[3]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[3][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[3][0]}\n'
                  f'2. Buy {Models[3][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[3][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Lexus \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[3][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[3][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[3][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[3][1]}\n'
                  f'2. Buy {Models[3][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[3][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Lexus \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[3][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[3][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[3][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[3][2]}\n'
                  f'2. Buy {Models[3][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[3][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Lexus \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[3][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[3][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Porsche
    elif choice == '5':
        for i in Models[4]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[4][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[4][0]}\n'
                  f'2. Buy {Models[4][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[4][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Porsche \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[4][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[4][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[4][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[4][1]}\n'
                  f'2. Buy {Models[4][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[4][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Porsche \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[4][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[4][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[4][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[4][2]}\n'
                  f'2. Buy {Models[4][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[4][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Porsche \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[4][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[4][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Volkswagen
    elif choice == '6':
        for i in Models[5]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[5][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[5][0]}\n'
                  f'2. Buy {Models[5][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[5][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Volkswagen \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[5][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[5][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[5][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[5][1]}\n'
                  f'2. Buy {Models[5][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[5][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Volkswagen \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[5][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[5][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[5][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[5][2]}\n'
                  f'2. Buy {Models[5][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[5][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Volkswagen \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[5][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[5][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Audi
    elif choice == '7':
        for i in Models[6]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[6][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[6][0]}\n'
                  f'2. Buy {Models[6][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[6][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Benz \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[6][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[6][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[6][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[6][1]}\n'
                  f'2. Buy {Models[6][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[6][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Audi \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[2][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[6][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[6][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[6][2]}\n'
                  f'2. Buy {Models[6][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[6][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Audi \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[6][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[6][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Lamborghini
    elif choice == '8':
        for i in Models[7]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[7][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[7][0]}\n'
                  f'2. Buy {Models[7][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[7][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Lamborghini \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[7][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[7][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[7][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[7][1]}\n'
                  f'2. Buy {Models[7][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[7][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Lamborghini \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[7][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[7][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[7][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[7][2]}\n'
                  f'2. Buy {Models[7][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[7][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Lamborghini \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[7][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[7][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Ferrari
    elif choice == '9':
        for i in Models[8]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[8][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[8][0]}\n'
                  f'2. Buy {Models[8][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[8][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Ferrari \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[8][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[8][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[8][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[8][1]}\n'
                  f'2. Buy {Models[8][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[8][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Ferrari \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[8][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $200, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[8][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[8][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[8][2]}\n'
                  f'2. Buy {Models[8][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[8][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Ferrari \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[8][2]}\n'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[8][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()
            # Bugatti
    elif choice == '10':
        for i in Models[9]:
            print(i)
            time.sleep(1)
        selected = input('Select car: ')
        if selected == '1':
            print(f'You have chosen to buy {Models[9][0]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[9][0]}\n'
                  f'2. Buy {Models[9][0]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[9][0]} Details\n'
                      f'{time.sleep(2)}'
                      'Manufacturers Name: Bugatti \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[9][0]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: N200,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[9][0]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '2':
            print(f'You have chosen to buy {Models[9][1]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[9][1]}\n'
                  f'2. Buy {Models[9][1]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[9][1]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Bugatti \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[9][1]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $500, 000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[9][1]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        elif selected == '3':
            print(f'You have chosen to buy {Models[9][2]}')
            print(f'Would you like too: \n'
                  f'1. See more details on {Models[9][2]}\n'
                  f'2. Buy {Models[9][2]}\n'
                  f'0. Return')
            purchasing = input('Select Option: ')
            if purchasing == '0':
                return car_models()
            if purchasing == '1':
                print(f'{Models[9][2]} Details\n'
                      f'{time.sleep(1)}'
                      'Manufacturers Name: Bugatti \n'
                      f'{time.sleep(1)}'
                      f'Model: {Models[9][2]}\n'
                      f'{time.sleep(1)}'
                      f'Description: The 2755 cc Diesel engine generates a power of 201.15bhp@3000-3400rpm and a torque of 500Nm@1600-2800rpm. Toyota Hilux is available in both Manual & Automatic transmission. The kerb weight of Hilux is 1860 Kg. In configurations, Toyota Hilux has a dimensions of 5325 mm in length, 1855 mm in width and 1815 mm in height.'
                      f'{time.sleep(1)}'
                      'Year: 2011\n'
                      f'{time.sleep(1)}'
                      'Price: $1,000,000')
                cow = input('0 . Return')
                if cow == '0':
                    return car_models()
                else:
                    print('Invalid Input')
                    return car_models()
            elif purchasing == '2':
                print(f'You have requested to purchase {Models[9][2]}')
                input(f'You can make your payment to the account number: 4194194190\n'
                      f'In the description Box, input your location and whatsapp number (if any).\n'
                      f'and we\'ll send you an SMS as soon as we confirm payment')
            elif purchasing == '3':
                return car_models()
            else:
                print('Invalid input')
                return car_models()
        else:
            print('Invalid Input')
            return car_models()

    elif choice == '0':
        time.sleep(2)
        return car_lot()
    else:
        print('Invalid Input')
        return car_models()

def car_lot():
    print('Welcome to the Car lot')
    time.sleep(2)
    print('Here, you can scroll through the list of our cars\n'
          'or you can search for a car by brand.')
    time.sleep(2)
    choice = input(
        '1. View Car List\n'
        '2. Select Car Brands\n'
        '0. Return\n'
        'Select Option: '
    )
    if choice.isalpha() == True:
        print('USSD must be in digits')
        return car_lot()
    elif choice == '1':
        return car_list()
    elif choice == '2':
        return car_models()
    elif choice == '0':
        time.sleep(2)
        return choices()
    else:
        print('Invalid Input')
        return car_lot()

def car_dealership():
    print('Welcome to the Car Dealership')
    time.sleep(2)
    print('You are free to select from our several varieties of cars.')
    time.sleep(2)
    print('You no longer have to go to a car lot to purchase a car.')
    time.sleep(2)
    print('All can be done at the comfort of your home.')
    time.sleep(2)
    return choices()

def about():
    print("A USSD car dealership is a modern and convenient solution for buying and selling vehicles. Instead of having to visit multiple physical dealerships, customers can browse through a wide range of cars on the USSD from the comfort of their own homes.\n"+

"One of the most significant advantages of an online car dealership is the vast inventory available at one's fingertips. Customers can easily filter their search by brand, model, year, price, and even specific features they are looking for in a vehicle.\n"+
"This extensive selection ensures that there is something for every budget and preference.\n"+

"Moreover, an online car dealership often offers competitive prices and deals that may not be available at traditional brick-and-mortar dealerships./n+"
"With lower overhead costs, they can pass on these savings to customers.\n"+
"Additionally, customers have the opportunity to compare prices from various dealerships and private sellers, allowing them to make an informed decision about their purchase.\n"+

"Another essential aspect of an online car dealership is the convenience it offers. Customers can easily schedule test drives, apply for financing, and even have the vehicle delivered directly to their doorstep.\n"+
"This eliminates the time-consuming process of visiting different dealerships to find the right car and negotiate a deal.\n"+

"Furthermore, online car dealerships provide comprehensive information about each vehicle, including a detailed description, high-resolution images, and vehicle history reports.\n"+
"This transparency allows customers to have a clear understanding of the vehicle's condition before making a purchase.\n"+

"While buying a car online may seem daunting for some, reputable online car dealerships often have excellent customer service and support teams to assist customers throughout the buying process.\n"+
"With thorough assistance and clear communication, any concerns or questions can be addressed promptly. \n"+

"In conclusion, an online car dealership is a convenient platform that offers a wide selection, competitive prices, and ease of purchase.\n"+
"It is an ideal solution for individuals looking to buy or sell a vehicle while saving time and effort."
    )

def choices():
    choice = input(
        'Would you like to:\n'
        '1. Learn more\n'
        '2. Visit Car Lot\n'
        '3. Repeat the prompt\n'
        '4. Quit\n'
        'Select Option: '
    )
    if choice.isalpha() == True:
        print('USSD must be in digits')
        return choices()
    elif choice == '1':
        return about()
    elif choice == '2':
        return car_lot()
    elif choice == '3':
        time.sleep(2)
        return choices()
    elif choice == '4':
        pass
    else:
        print('Invalid Input')
        return choices()




def startProject():
    ussd = input('Enter USSD:' )
    if ussd.isalpha() == True:
        print('USSD must be digits')
        return startProject()
    elif ussd == '*121#':
        return car_dealership()
    elif ussd == '*122#':
        return about()
    else:
        print('Invalid USSD')
        return startProject()

startProject()