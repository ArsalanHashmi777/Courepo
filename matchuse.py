keep_looping = True
while keep_looping == True:
    name = input("Enter your name: ")
    match name:
        case "Arsalan" | "Raheel" | "Zafeer" | "Hamna":
            print("Family")
            keep_looping = False
        case _:
            print("Not in sry")