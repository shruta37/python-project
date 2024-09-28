import tkinter as tk
from tkinter import ttk

# Conversion factors for length and weight
conversion_factors = {
    'Length': {
        'Meter': 1.0,
        'Kilometer': 0.001,
        'Mile': 0.000621371
    },
    'Weight': {
        'Gram': 1.0,
        'Kilogram': 0.001,
        'Pound': 0.00220462
    }
}

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Unit Converter")

        # Set up a main frame with larger padding for a bigger look
        self.main_frame = ttk.Frame(root, padding="20 20 20 20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add styles with larger fonts
        style = ttk.Style()
        style.configure('TFrame', background='#E0E0E0')
        style.configure('TLabel', background='#E0E0E0', font=('Helvetica', 16))
        style.configure('TButton', font=('Helvetica', 16))
        style.configure('TCombobox', font=('Helvetica', 16))
        style.configure('TEntry', font=('Helvetica', 16))

        # Category selection
        self.category_label = ttk.Label(self.main_frame, text="Select Category:")
        self.category_label.grid(row=0, column=0, padx=10, pady=10)

        self.category_combobox = ttk.Combobox(self.main_frame, values=['Length', 'Weight'], state="readonly", font=('Helvetica', 16))
        self.category_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.select_button = ttk.Button(self.main_frame, text="Select Category", command=self.select_category)
        self.select_button.grid(row=0, column=2, padx=10, pady=10)

        # Conversion widgets (hidden initially)
        self.value_label = ttk.Label(self.main_frame, text="Value:")
        self.value_entry = ttk.Entry(self.main_frame)
        self.from_unit_label = ttk.Label(self.main_frame, text="From Unit:")
        self.from_unit_combobox = ttk.Combobox(self.main_frame, state="readonly")
        self.to_unit_label = ttk.Label(self.main_frame, text="To Unit:")
        self.to_unit_combobox = ttk.Combobox(self.main_frame, state="readonly")
        self.convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert)
        self.result_label = ttk.Label(self.main_frame, text="Result:")
        self.result_entry = ttk.Entry(self.main_frame, state="readonly")
        self.back_button = ttk.Button(self.main_frame, text="Back", command=self.go_back)

        # Start with the category selection view
        self.show_category_widgets()

    def show_category_widgets(self):
        # Show category selection widgets
        self.category_label.grid()
        self.category_combobox.grid()
        self.select_button.grid()

        # Hide conversion widgets
        self.value_label.grid_remove()
        self.value_entry.grid_remove()
        self.from_unit_label.grid_remove()
        self.from_unit_combobox.grid_remove()
        self.to_unit_label.grid_remove()
        self.to_unit_combobox.grid_remove()
        self.convert_button.grid_remove()
        self.result_label.grid_remove()
        self.result_entry.grid_remove()
        self.back_button.grid_remove()

    def show_conversion_widgets(self):
        # Hide category selection widgets
        self.category_label.grid_remove()
        self.category_combobox.grid_remove()
        self.select_button.grid_remove()

        # Show conversion widgets
        self.value_label.grid(row=1, column=0, padx=10, pady=10)
        self.value_entry.grid(row=1, column=1, padx=10, pady=10)
        self.from_unit_label.grid(row=2, column=0, padx=10, pady=10)
        self.from_unit_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.to_unit_label.grid(row=3, column=0, padx=10, pady=10)
        self.to_unit_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.convert_button.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
        self.result_label.grid(row=5, column=0, padx=10, pady=10)
        self.result_entry.grid(row=5, column=1, padx=10, pady=10)
        self.back_button.grid(row=6, column=0, columnspan=3, padx=10, pady=20)

    def select_category(self):
        # Get the selected category
        category = self.category_combobox.get()
        if category not in conversion_factors:
            return

        # Update the unit comboboxes based on the selected category
        units = list(conversion_factors[category].keys())
        self.from_unit_combobox.config(values=units)
        self.to_unit_combobox.config(values=units)

        # Clear previous selections
        self.from_unit_combobox.set('')
        self.to_unit_combobox.set('')
        self.value_entry.delete(0, tk.END)
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.config(state="readonly")

        # Show the conversion widgets
        self.show_conversion_widgets()

    def go_back(self):
        # Go back to the category selection view
        self.show_category_widgets()

    def convert(self):
        # Get the user input
        try:
            category = self.category_combobox.get()
            value = float(self.value_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            # Calculate the conversion
            from_unit_factor = conversion_factors[category][from_unit]
            to_unit_factor = conversion_factors[category][to_unit]
            result = value * (to_unit_factor / from_unit_factor)  # Corrected calculation

            # Display the result
            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, f"{result:.4f}")
            self.result_entry.config(state="readonly")
        except Exception as e:
            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Error")
            self.result_entry.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  # Increased window size for better appearance
    app = UnitConverterApp(root)
    root.mainloop()
