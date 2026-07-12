def main():
    print("Tell Your Country:")
    country = input()
    
    floor = int(input())

    if country == "India":
        print("you are on floor number:", floor)

    if country == "USA":
        if floor == 0:
            print("you are on ground floor")
        else:
            print("you are on floor number:", floor)

    if country == "Uk":
        print("you are on floor number:", floor + 1)

    if country == "China":
        if floor == 13:
            print("you are on floor number: 12A")
        else:
            print("you are on floor number:", floor)



if __name__ == "__main__":
    main()
