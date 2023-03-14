from time import sleep

word = "bottles"

for bottles in range(99, 0, -1):
    print(bottles, word, "of beer on the board")
    print(bottles, word, "of beer")
    print("Take one down")
    print("Pass it around")
    if bottles == 1:
        print("No more bottles of beer on the board")
    else:
        new_bottles = bottles - 1
        if new_bottles == 1:
            word = "bottle"
        print(new_bottles, word, "of beer on the board")
    print()
    sleep(0.2)
        
        
