command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print ('car is already stopped')
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print(''' 
        start - to start
        stop - to stop
        quit - to end
        ''')
    elif command == 'quit':
        print('THE END')
