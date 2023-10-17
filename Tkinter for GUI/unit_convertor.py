import tkinter as tk

class UnitConvertorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Unit Converter")
        master.config(padx=20, pady=20)

        # labels
        self.inp_unit = tk.Label(text="Input Unit", font=("Arial", 12))
        self.inp_unit.grid(column=0, row=0, padx=5, pady=5)

        self.inp_value = tk.Label(text="Input Value", font=("Arial", 12))
        self.inp_value.grid(column=1, row=0, padx=5, pady=5)

        self.out_unit = tk.Label(text="Output Unit", font=("Arial", 12))
        self.out_unit.grid(column=2, row=0, padx=5, pady=5)

        self.out_value = tk.Label(text="Output Value", font=("Arial", 12))
        self.out_value.grid(column=3, row=0, padx=5, pady=5)

        # entry
        self.inp = tk.Entry(width=10, font=("Arial", 12))
        self.inp.grid(column=1, row=1, padx=5, pady=5)

        # dropdown menus
        self.unit_options = ["Miles", "Kilometers", "Meters", "Yards", "Feet", "Inches"]
        self.input_unit = tk.StringVar(master)
        self.input_unit.set(self.unit_options[0])
        self.input_unit_dropdown = tk.OptionMenu(master, self.input_unit, *self.unit_options)
        self.input_unit_dropdown.config(font=("Arial", 12))
        self.input_unit_dropdown.grid(column=0, row=1, padx=5, pady=5)

        self.output_unit = tk.StringVar(master)
        self.output_unit.set(self.unit_options[1])
        self.output_unit_dropdown = tk.OptionMenu(master, self.output_unit, *self.unit_options)
        self.output_unit_dropdown.config(font=("Arial", 12))
        self.output_unit_dropdown.grid(column=2, row=1, padx=5, pady=5)

        # buttons
        self.button = tk.Button(text="Calculate", command=self.convert, font=("Arial", 12))
        self.button.grid(column=1, row=2, padx=5, pady=5)

    def convert(self):
        inp_value = float(self.inp.get())
        inp_unit = self.input_unit.get()
        out_unit = self.output_unit.get()

        converter = UnitConverter()
        out_value = converter.calculate_val(inp_value, inp_unit, out_unit)

        self.out_value.config(text=f"{out_value:.2f}")


class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            "Miles": 1609.34,
            "Kilometers": 1000,
            "Meters": 1,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        }

    def calculate_val(self, inp_value, inp_unit, out_unit):
        inp_value_m = inp_value * self.conversion_factors[inp_unit]
        out_value = inp_value_m / self.conversion_factors[out_unit]
        return out_value


window = tk.Tk()
app = UnitConvertorGUI(window)
window.mainloop()
