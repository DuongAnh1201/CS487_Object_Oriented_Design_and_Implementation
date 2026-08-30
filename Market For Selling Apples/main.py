from Apple import Apple
from Barrel import Barrel


def main():
    print("The Market Test Program")
    print()
    # while True:
    #     capacity = float(input("Enter capacity of barrel: "))
    #     barrel = Barrel(capacity)
    #     while True:
    #         type = input("Enter apple type: ")
    #         weight = float(input("Enter weight: "))
    #         price = float(input("Enter price: "))
    #         apple = Apple(type, weight, price) 
    #         barrel.add_app(apple)
    #         choice = input("Add more apples? (y/n): ")
    #         print()
    #         if choice != "y":
    #             print("Your barrel has these apples: ")
    #             print(barrel)
    #             break
    #     choice = input("Get another barrel? (y/n): ")
    #     print()
    #     if choice != "y":
    #         print("Bye!")
    #         break

    b = Barrel(capacity = 20.0)
    b.add_apple(Apple('Fuji', 1, 3))
    b.add_apple(Apple('Gala', 2, 2.5))
    b.add_apple(Apple('Granny Smith', 3, 2))
    b.add_apple(Apple('Honeycrisp', 4, 4))
    b.add_apple(Apple('Pink Lady', 0.5, 3.5))
    b.add_apple(Apple('Golden Delicious', 0.2, 2.8))
    b.add_apple(Apple('Red Delicious', 0.3, 2.2))
    b.add_apple(Apple('Ambrosia', 5, 3.2))
    print(f"Apple before filtering:")
    b_list = b.list
    for i in range(len(b_list)):
        print(f"Apple {i+1} - Weight: {b_list[i].weight} - Price: {b_list[i].price}")
    print(f"Apple after filtering: ")
    b.remove_small_apples()
    for i in range(len(b.list)):
        print(f"Apple {i+1} - Weight: {b.list[i].weight} - Price: {b.list[i].price}")
  
if __name__ == "__main__":
    main()
        