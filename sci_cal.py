import tkinter as tk
import sqlite3
import math

conn = sqlite3.connect('calc_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS history (expression TEXT, result TEXT)''')
conn.commit()

def evaluate_expression():
    try:
        expr = entry.get()
        expr = expr.replace('^', '**')
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        c.execute('INSERT INTO history (expression, result) VALUES (?, ?)', (expr, str(result)))
        conn.commit()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

def insert_value(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def toggle_mode():
    if scientific_frame.winfo_viewable():
        scientific_frame.grid_remove()
        mode_button.config(text="Scientific Mode")
    else:
        scientific_frame.grid()
        mode_button.config(text="Basic Mode")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    c.execute('SELECT * FROM history')
    records = c.fetchall()
    for i, (expression, result) in enumerate(records):
        tk.Label(history_window, text=f"{expression} = {result}").pack()

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#0A0A0A")

entry = tk.Entry(root, font=('Arial', 24), bg="#333333", fg="white", borderwidth=5, relief="flat")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="we")

button_frame = tk.Frame(root, bg="#0A0A0A")
button_frame.grid(row=1, column=0, sticky="nsew")

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    action = lambda x=text: evaluate_expression() if x == '=' else insert_value(x)
    tk.Button(button_frame, text=text, command=action, font=('Arial', 18), bg="#1C1C1C", fg="white", width=5, height=2).grid(row=row, column=col, padx=5, pady=5)

tk.Button(button_frame, text="C", command=clear_entry, font=('Arial', 18), bg="#D72638", fg="white", width=5, height=2).grid(row=5, column=0, padx=5, pady=5)
mode_button = tk.Button(button_frame, text="Scientific Mode", command=toggle_mode, font=('Arial', 16), bg="#3D348B", fg="white")
mode_button.grid(row=5, column=1, columnspan=2, sticky="we", padx=5, pady=5)
tk.Button(button_frame, text="History", command=show_history, font=('Arial', 16), bg="#FF5700", fg="white").grid(row=5, column=3, padx=5, pady=5)

scientific_frame = tk.Frame(root, bg="#0A0A0A")
scientific_frame.grid(row=2, column=0, sticky="nsew")
scientific_frame.grid_remove()

scientific_buttons = [
    ('sin',0,0), ('cos',0,1), ('tan',0,2), ('sqrt',0,3),
    ('log',1,0), ('ln',1,1), ('exp',1,2), ('^',1,3)
]

for (text, row, col) in scientific_buttons:
    def create_func(t=text):
        if t == 'sin':
            return lambda: insert_value(f"math.sin(math.radians({entry.get()}))")
        elif t == 'cos':
            return lambda: insert_value(f"math.cos(math.radians({entry.get()}))")
        elif t == 'tan':
            return lambda: insert_value(f"math.tan(math.radians({entry.get()}))")
        elif t == 'sqrt':
            return lambda: insert_value(f"math.sqrt({entry.get()})")
        elif t == 'log':
            return lambda: insert_value(f"math.log10({entry.get()})")
        elif t == 'ln':
            return lambda: insert_value(f"math.log({entry.get()})")
        elif t == 'exp':
            return lambda: insert_value(f"math.exp({entry.get()})")
        else:
            return lambda: insert_value("^")
    tk.Button(scientific_frame, text=text, command=create_func(), font=('Arial', 18), bg="#1C1C1C", fg="white", width=5, height=2).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
