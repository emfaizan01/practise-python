# 1. Create a program to manage student names.
students = []

while True:
    print("Menu")
    print("1. Add student")
    print("2. Remove student")
    print("3. View all studet")
    print("4. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name to add: ")
        students.append(name)
        print(name + "has been added.")

    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print(name + " has been removed.")
        else:
            print("Student not found.") 

    elif choice == "3":
        print("\nList of Students:")
        if len(students) == 0:
            print("No students in the list.")
        else:
            for s in students:
                print("- " + s)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter again.")

# 2.Build a text-based to-do list manager.

tasks = []
while True:
    print("\n--- Simple To-Do List ---")
    print("1. Add task")
    print("2. Delete task")
    print("3. View tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added:", task)

    elif choice == "2":
        task = input("Enter the task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed:", task)
        else:
            print("Task not found.")

    elif choice == "3":
        print("\nYour To-Do List:")
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for t in tasks:
                print("- " + t)
    elif choice == "4":
        print("Goodbye! Exiting To-Do List.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

# 3. Count how many vowels are in a sentence.

sentence = input("Enter a sentence: ")

vowel_count = 0

vowels = "aeiouAEIOU"

for char in sentence:
    
    if char in vowels:
        vowel_count = vowel_count + 1 
print("Total number of vowels in the sentence:", vowel_count)


# 4.Display only long words from a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Words longer than 4 letters:")

for word in words:
    
    if len(word) > 4:
        print(word)


# 5.Reverse each word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_words = []

for word in words:
    reversed_word = word[::-1]  
    reversed_words.append(reversed_word)  
result = " ".join(reversed_words)

print("Reversed sentence:", result)



# 6.Perform calculations until user exits.

while True:
    
    num1 = input("Enter first number : ")

    if num1 == "exit":
        print("Calculator closed.")
        break

    num2 = input("Enter second number: ")

    operator = input("Enter operator (+, -, *, /): ")

    number1 = float(num1)
    number2 = float(num2)

    
    if operator == "+":
        result = number1 + number2
        print("Result:", result)

    elif operator == "-":
        result = number1 - number2
        print("Result:", result)

    elif operator == "*":
        result = number1 * number2
        print("Result:", result)

    elif operator == "/":
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = number1 / number2
            print("Result:", result)

    else:
        print("Invalid operator. Please use +, -, *, or /.")