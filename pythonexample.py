import tkinter as tk


root = tk.Tk()
root.title("Simple Window")


window_width = 300
window_height = 200


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)


root.geometry(f"{window_width}x{window_height}+{x}+{y}")


label = tk.Label(root, text="Hello World", font=("Arial", 20))
label.pack(expand=True)  


root.mainloop()
