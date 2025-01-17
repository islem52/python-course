import pathlib


print("Welcome to the Unique Word Counter!")
print("Type words one by one. Entering a duplicate word will end the program.\n")

unique_words = set()  # To store unique words
total_words = 0  # To track total words entered

while True:
    word = input("Enter a word: ").strip().lower()  # Convert to lowercase
    if word in unique_words:  # Check for duplicate
        print(f"\nDuplicate word entered: '{word}'")
        print(f"You typed in {len(unique_words)} unique words.")
        print(f"Total words entered: {total_words}")
        print(f"Unique words (alphabetical order): {', '.join(sorted(unique_words))}")

        # Bonus: Save unique words to a file
        save = input("Do you want to save unique words to a file? (y/n): ").lower()
        if save == "y":
            script_dir = pathlib.Path(__file__).parent  # Get the script's directory
            filename = script_dir / "unique_words.txt"
            with open(filename, "w") as file:
                file.write("\n".join(sorted(unique_words)))
            print(f"Unique words saved to {filename}.")
        break

    unique_words.add(word)  # Add the word to the set
    total_words += 1  # Increment total word count



