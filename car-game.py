command = ""
is_car_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if not is_car_started:
            print("Car started...Ready to go!")
            is_car_started = True
        else:
            print("Car is already started")
    elif command == "stop":
        if is_car_started:
            print("Car stopped.")
            is_car_started = False
        else:
            print("Car is already stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")
    
    
