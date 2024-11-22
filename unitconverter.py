import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert_units():
    try:
        input_value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()

        if category == "Length":
            conversion_factors = {
                "Meters": 1,
                "Kilometers": 0.001,
                "Centimeters": 100,
                "Feet": 3.28084,
                "Inches": 39.3701,
            }
        elif category == "Weight":
            conversion_factors = {
                "Kilograms": 1,
                "Grams": 1000,
                "Pounds": 2.20462,
                "Ounces": 35.274,
            }
        elif category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (input_value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (input_value - 32) * 5/9
            else:
                result = input_value  # Same unit
            result_label.config(text=f"Result: {result:.2f} {to_unit}")
            return
        else:
            result_label.config(text="Invalid category")
            return

        # Perform conversion
        result = input_value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

def update_units(event):
    category = combo_category.get()
    if category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Feet", "Inches"]
    elif category == "Weight":
        units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit"]
    else:
        units = []

    combo_from['values'] = units
    combo_to['values'] = units
    combo_from.set(units[0])
    combo_to.set(units[1])

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Title
title_label = tk.Label(root, text="Unit Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Category selection
category_label = tk.Label(root, text="Select Category:", font=("Arial", 12))
category_label.pack()

combo_category = ttk.Combobox(root, values=["Length", "Weight", "Temperature"], state="readonly", font=("Arial", 12))
combo_category.pack(pady=5)
combo_category.bind("<<ComboboxSelected>>", update_units)
combo_category.set("Length")

# From unit
from_label = tk.Label(root, text="From:", font=("Arial", 12))
from_label.pack()

combo_from = ttk.Combobox(root, state="readonly", font=("Arial", 12))
combo_from.pack(pady=5)

# Input value
entry_value = tk.Entry(root, font=("Arial", 12))
entry_value.pack(pady=5)

# To unit
to_label = tk.Label(root, text="To:", font=("Arial", 12))
to_label.pack()

combo_to = ttk.Combobox(root, state="readonly", font=("Arial", 12))
combo_to.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12), bg="blue", fg="white", command=convert_units)
convert_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Populate initial units
update_units(None)

# Run the application
root.mainloop()