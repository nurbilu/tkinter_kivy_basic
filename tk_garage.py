import tkinter as tk
from tkinter import ttk

class GarageCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Garage CRUD App")

        self.tree = ttk.Treeview(root, columns=("Model", "Color", "Year"), show="headings")
        self.tree.heading("Model", text="Model")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Year", text="Year")
        self.tree.pack(pady=10)

        self.model_entry = tk.Entry(root, width=20)
        self.color_entry = tk.Entry(root, width=20)
        self.year_entry = tk.Entry(root, width=20)

        self.model_label = tk.Label(root, text="Model:")
        self.color_label = tk.Label(root, text="Color:")
        self.year_label = tk.Label(root, text="Year:")

        self.model_label.pack()
        self.model_entry.pack()

        self.color_label.pack()
        self.color_entry.pack()

        self.year_label.pack()
        self.year_entry.pack()

        self.add_button = tk.Button(root, text="Add", command=self.add_car)
        self.update_button = tk.Button(root, text="Update", command=self.update_car)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_car)

        self.add_button.pack(pady=5)
        self.update_button.pack(pady=5)
        self.delete_button.pack(pady=5)

        # Sample data
        self.sample_data()

    def add_car(self):
        model = self.model_entry.get()
        color = self.color_entry.get()
        year = self.year_entry.get()

        if model and color and year:
            self.tree.insert("", "end", values=(model, color, year))
            self.clear_entries()

    def update_car(self):
        selected_item = self.tree.selection()

        if selected_item:
            model = self.model_entry.get()
            color = self.color_entry.get()
            year = self.year_entry.get()

            self.tree.item(selected_item, values=(model, color, year))
            self.clear_entries()

    def delete_car(self):
        selected_item = self.tree.selection()

        if selected_item:
            self.tree.delete(selected_item)
            self.clear_entries()

    def clear_entries(self):
        self.model_entry.delete(0, "end")
        self.color_entry.delete(0, "end")
        self.year_entry.delete(0, "end")

    def sample_data(self):
        data = [("Sedan", "Blue", 2020),
                ("SUV", "Red", 2019),
                ("Truck", "Black", 2022)]

        for car in data:
            self.tree.insert("", "end", values=car)

if __name__ == "__main__":
    root = tk.Tk()
    app = GarageCRUDApp(root)
    root.mainloop()
