from calendar import day_name


def displayMenu():
    print('welcome')
    print('-------------------')
    print('1. Add contact')
    print('2. Edit contact')
    print('3. delete contact')
    print('4. search contact')
    print('5. quit')
    print('-------------------')
    print('ENTER YOUR CHOICE(NUMBER IS VALID): ')

    cmd = input()
    if cmd in ['1', '2', '3','4', '5']:
        return cmd
    else :
        print('invalid choice')


def saveFile(contact_list):
    with open ('list.csv', 'w') as f:
        for name, number in contact_list.items():
            f.write(f'{name}, {number},\n')
    print('done')

def loadFile():
    result = dict()
    try:
        with open('list.csv', 'r') as f:
            for line in f:
                name , number = line.split(',')
                result[name] = number
    except:
        print('failed')
        return dict()
    
contact_list = dict()
while True:
    cmd = displayMenu()
    if cmd == '1':
        name = input('please enter name: ').lower()
        if name in contact_list:
            print('this name already exists')
            continue
        number = input('please enter phone number')
        contact_list[name] = number
        print('added to the list')

    if cmd == '2':
        name = input('please enter name to edit contact: ').lower()
        if name not in contact_list:
          print('this name does not exist')
          continue
        number = input('enter new number: ')
        contact_list[name] = number
        print('list updated')

    if cmd == '3':
        name = input('enter name: ').lower()
        if name not in contact_list:
            print('this name does not exist')
            continue
        del contact_list[name]
        print('done')
    
    if cmd == '4':
        name = input('enter name: ').lower()
        if name not in contact_list:
            print('this name does not exist')
            continue
        print(f'{name}: {contact_list}')
    if cmd == '5':
        break



