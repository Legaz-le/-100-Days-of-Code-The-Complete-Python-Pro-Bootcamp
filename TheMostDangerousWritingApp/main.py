import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self._after_id = None
        self.restart_button = None  # Initialize restart button reference
        self.create_widgets()

    def create_widgets(self):
        # Create entry widget
        self.entry = tk.Entry(self, width=50, font=("default", 20))
        self.entry.pack(pady=20)
        self.entry.bind('<Key>', self.handle_wait)
        self.entry.focus_set()

        # Remove restart button if it exists
        if self.restart_button:
            self.restart_button.destroy()

    def handle_wait(self, event):
        # Cancel the old job
        if self._after_id:
            self.after_cancel(self._after_id)

        # Create a new job
        self._after_id = self.after(5000, self.clean_up)

    def clean_up(self):
        # Destroy entry widget
        self.entry.destroy()

        # Create restart button
        self.restart_button = tk.Button(
            self,
            text="Restart Prompt",
            command=self.restart,
            font=("default", 14),
            bg="#4CAF50",
            fg="white"
        )
        self.restart_button.pack(pady=20)

    def restart(self):
        # Reset the application
        self._after_id = None
        self.create_widgets()


root = tk.Tk()
root.geometry("500x300")
root.title("Focus Writer App")
root.configure(bg="#f0f0f0")

app = Application(root)
app.mainloop()





