# pattern_drawing.py

def main():
    # Prompt the user to enter the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Validate input to ensure it's a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end="")
            col += 1
        print()  # Move to the next line after completing the row
        row += 1

if __name__ == "__main__":
    main()
