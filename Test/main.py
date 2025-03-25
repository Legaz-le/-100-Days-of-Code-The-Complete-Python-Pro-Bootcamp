import tkinter as tk
import random

# Create the root window
root = tk.Tk()
root.title("Random Word Positions")
root.geometry("600x400")  # Set window size

# List of words
words = [
    "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
    "the", "a", "an", "and", "but", "or", "so", "because", "if", "although", "while",
    "in", "on", "at", "by", "for", "to", "with", "about", "from", "over", "under",
    "be", "have", "do", "say", "get", "make", "go", "know", "take", "see", "think",
    "come", "give", "use", "find", "want", "good", "new", "old", "big", "small",
    "great", "high", "long", "different", "important", "very", "really", "only",
    "just", "always", "never", "often", "usually", "sometimes", "also", "people",
    "time", "year", "way", "day", "thing", "man", "woman", "life", "child", "world",
    "school", "place", "work", "yes", "no", "please", "thank you", "hello", "goodbye",
    "sorry", "excuse me"
]

# Function to display all words at random positions
def display_words_randomly():
    # Clear all existing labels (if any)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget != button:
            widget.destroy()

    # Display words in random positions
    for word in words:
        x = random.randint(10, 550)  # Random x position
        y = random.randint(10, 350)  # Random y position
        label = tk.Label(root, text=word, font=("Arial", 10))
        label.place(x=x, y=y)  # Place the label at the random position

# Create a Button to trigger the random placement
button = tk.Button(root, text="Randomize Words", command=display_words_randomly, font=("Arial", 14))
button.pack(pady=10)

# Run the application
root.mainloop()