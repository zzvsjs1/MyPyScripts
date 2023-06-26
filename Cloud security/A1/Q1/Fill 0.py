while True:
    ui = input('Enter: ')
    while len(ui) < 128:
        ui += '0'

    print(ui, end='\n\n')
