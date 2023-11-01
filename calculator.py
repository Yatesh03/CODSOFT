import tkinter as tk

def on_button_click(event):
    current_text = result_var.get()
    clicked_text = event.widget.cget("text")

    if clicked_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif clicked_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + clicked_text)

root = tk.Tk()
root.title("Simple Calculator")

result_var = tk.StringVar()
result_var.set("")

result_label = tk.Label(root, textvariable=result_var, anchor="e", font=("Helvetica", 20))
result_label.pack(fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row = 0
col = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 15))
    button.grid(row=row, column=col, padx=10, pady=10)
    button.bind("<Button-1>", on_button_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
