import Search_Methods
import random
import sys
# Mohamed Bagayoko
# 4/13/2020
# Exam 2

# Empty Unsorted List
rand_list = []

# Method Loops
run = True
run2 = True

# Welcoming Statement
print("""Hello user. Please select the following 
Sorting Algorithm you would like to use:""")

# Algorithm Menu
while run:
    print("""1 for Bubble Sort
2 for Selection Sort
3 for Insertion Sort
4 for Merge Sort
5 for Quick Sort
6 to Exit""")
    chose = int(input("> "))

# Bubble Sort Method
    if chose == 1:
        print("You have selected the Bubble Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        # Generates random numbers within chosen user's limit
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"""Your generated list is:
{rand_list}""")
        print("(Input anything to start sorting)")
        input("> ")
        # Uses sorting method
        y = Search_Methods.bubble_sort(x)
        print(f"""Your Bubble Sorted list is:
{y}""")
        menu = input("(Input anything to go back to menu)")
        # Clears list
        rand_list.clear()
        run = True

# Selection Sort Method
    elif chose == 2:
        print("You have selected the Selection Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        # Generates random numbers within chosen user's limit
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"""Your generated list is:
{rand_list}""")
        print("(Input anything to start sorting)")
        input("> ")
        # Uses sorting method
        y = Search_Methods.selection_sort(x)
        print(f"""Your Selection Sorted list is:
{y}""")
        menu = input("(Input anything to go back to menu)")
        # Clears list
        rand_list.clear()
        run = True

# Insertion Sort Method
    elif chose == 3:
        print("You have selected the Insertion Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        # Generates random numbers within chosen user's limit
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"""Your generated list is:
{rand_list}""")
        print("(Input anything to start sorting)")
        input("> ")
        # Uses sorting method
        y = Search_Methods.insertion_sort(x)
        print(f"""Your Insertion Sorted list is:
{y}""")
        menu = input("(Input anything to go back to menu)")
        # Clears list
        rand_list.clear()
        run = True

# Merge Sort Method
    elif chose == 4:
        print("You have selected the Merge Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        # Generates random numbers within chosen user's limit
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"""Your generated list is:
{rand_list}""")
        print("(Input anything to start sorting)")
        input("> ")
        # Uses sorting method
        y = Search_Methods.merge_sort(x)
        print(f"""Your Merge Sorted list is:
{y}""")
        menu = input("(Input anything to go back to menu)")
        # Clears list
        rand_list.clear()
        run = True

# Quick Sort Method
    elif chose == 5:
        print("You have selected the Quick Sort Method")
        run = False
        print("How many numbers would you like to sort?")
        chose2 = int(input("> "))
        # Generates random numbers within chosen user's limit
        x = random.sample(range(1, 100000), chose2)
        rand_list.append(x)
        print(f"""Your generated list is:
{rand_list}""")
        print("(Input anything to start sorting)")
        input("> ")
        # Uses sorting method
        y = Search_Methods.quick_sort(x)
        print(f"""Your Quick Sorted list is:
{y}""")
        menu = input("(Input anything to go back to menu)")
        # Clears list
        rand_list.clear()
        run = True

# Quit Option
    elif chose == 6:
        print("Have a nice day!")
        sys.exit()

# Wrong Menu Selection
    else:
        print("You selected the wrong input. Please try again.")
        run = True




