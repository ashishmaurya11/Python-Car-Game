choice = ""
started = False
while True:
    choice = input('>')
    if choice.lower() == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started.')
    elif choice.lower() == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car stopped.')
    elif choice.lower() == 'help':
        print('''
start - to start
stop - to stop
quit - quit
        ''')
    elif choice.lower() == 'quit':
        break
    else:
        print("I can't understand that...")
