import tkinter as tk
from tkinter import Frame, Label, YES, BOTH
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

class TemperatureConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Konverter Suhu")

        self.label = tk.Label(master, text="Masukkan suhu:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.convert_button = tk.Button(master, text="Konversi", command=self.convert_temperature)
        self.convert_button.pack()

    def convert_temperature(self):
        try:
            nilai_suhu = float(self.entry.get())
            result = celsius_to_fahrenheit(nilai_suhu)
            self.result_label.config(text=f"Hasil konversi: {result:.2f} Fahrenheit")
        except ValueError:
            self.result_label.config(text="Masukkan suhu yang valid.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
