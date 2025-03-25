import tkinter as tk
import random
import time

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
    "sorry", "excuse"
]

text = """How fast are your fingers? Do the one-minute typing test to find out! Press the space bar
after each word. At the end, you'll get your typing speed in CPM and WPM. Good luck!"""



# Global variables
correct_words = []
current_position = 0
start_time = None


def display_words_randomly():
    global correct_words, current_position, start_time
    random.shuffle(words)
    correct_words = words.copy()
    shuffled_text = " ".join(correct_words)
    text_to_display.config(text=shuffled_text)
    current_position = 0
    entry.delete(0, tk.END)
    start_time = None


def check_input(event):
    global current_position, start_time
    if start_time is None:
        start_time = time.time()
    # Get the input text and remove extra spaces
    input_text = entry.get().strip()
    # Check if space was pressed
    if event.keysym == "space" and input_text:
        if current_position >= len(correct_words):
            entry.delete(0, tk.END)
            return
        # Get current word and compare
        current_word = correct_words[current_position]
        if input_text == current_word:
            print(f"Correct! ({current_position + 1}/{len(correct_words)})")
            current_position += 1
            entry.delete(0, tk.END)
            # Check if all words are completed
            if current_position >= len(correct_words):
                total_time = time.time() - start_time
                wpm = len(correct_words) / (total_time / 60)
                print(f"\nTest complete! WPM: {wpm:.1f}")
        else:
            print(f"Wrong! Expected '{current_word}', got '{input_text}'")
            entry.delete(0, tk.END)



def speed_test():
    global text_to_display, entry

    top = tk.Frame(root)
    top.pack()

    text_label = tk.Label(top, text=text)
    text_label.pack(pady=20)

    type_window = tk.Frame(width=500, height=525, background="#F5F5F5", borderwidth=2)
    type_window.pack(pady=10)
    type_window.pack_propagate(0)

    top_level = tk.Label(type_window, background="#CECECE")
    top_level.pack(fill=tk.BOTH, side=tk.TOP)

    restart_button = tk.Button(top_level, text="Restart", width=10, command=display_words_randomly)
    restart_button.pack(padx=50, side=tk.RIGHT)

    text_to_display = tk.Label(type_window, text=text, font=("Arial", 20),
                               wraplength=460, justify="left")
    text_to_display.pack(fill=tk.BOTH)

    entry = tk.Entry(type_window, font=("Helvetica", 20),
                     background="#CECECE", borderwidth=2)
    entry.insert(0, "Start typing here...")
    entry.pack(side=tk.BOTTOM, fill=tk.BOTH)

    # Event bindings
    entry.bind("<FocusIn>", lambda e: entry.delete(0, tk.END))
    entry.bind("<KeyRelease>", check_input)

    display_words_randomly()


root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("800x800")
speed_test()
root.mainloop()