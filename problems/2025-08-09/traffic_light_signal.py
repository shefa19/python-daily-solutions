# Problem Name: Traffic Light Signal
# Description: Take a traffic signal color as input and display the corresponding action.

light_color = input("Enter a traffic signal light color: ").strip()

if len(light_color.split()) != 1:
    print("Enter a single light color.")
else:
    light_color = light_color.lower()
    
    match light_color:
        case 'red':
            print("Stop")
        case 'yellow':
            print("Ready")
        case 'green':
            print("Go")
        case _:
            print("Invalid light color.")