import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

CONFIG_FILE = "multilauncher_config.json"

class MultiLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("MultiLauncher")
        self.root.geometry("600x450")
        self.root.configure(bg="#1e272e")
        
        tk.Label(root, text="🚀 MultiLauncher", font=("Arial", 18, "bold"), fg="#00d2d3", bg="#1e272e").pack(pady=10)
        
        self.buttons_frame = tk.Frame(root, bg="#1e272e")
        self.buttons_frame.pack(pady=10)
        
        self.listbox = tk.Listbox(self.buttons_frame, width=55, height=12, font=("Arial", 12), bg="#485460", fg="white", selectbackground="#00d2d3")
        self.listbox.pack(side=tk.LEFT, padx=5)
        
        self.scrollbar = tk.Scrollbar(self.buttons_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.button_frame = tk.Frame(root, bg="#1e272e")
        self.button_frame.pack(pady=10)
        
        self.add_button = tk.Button(self.button_frame, text="➕ Agregar", font=("Arial", 12), bg="#10ac84", fg="white", command=self.add_program, width=15)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.remove_button = tk.Button(self.button_frame, text="❌ Eliminar", font=("Arial", 12), bg="#ee5253", fg="white", command=self.remove_program, width=15)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.launch_button = tk.Button(root, text="🚀 Lanzar Programas", font=("Arial", 14, "bold"), bg="#0abde3", fg="white", command=self.launch_programs, width=20)
        self.launch_button.pack(pady=10)
        
        self.clear_button = tk.Button(root, text="🧹 Limpiar Lista", font=("Arial", 12), bg="#576574", fg="white", command=self.clear_list, width=20)
        self.clear_button.pack(pady=5)
        
        self.programs = []
        self.load_programs()
    
    def add_program(self):
        filepath = filedialog.askopenfilename(title="Selecciona un programa")
        if filepath:
            self.programs.append(filepath)
            self.listbox.insert(tk.END, os.path.basename(filepath))
            self.save_programs()
    
    def remove_program(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.programs[index]
            self.listbox.delete(index)
            self.save_programs()
    
    def launch_programs(self):
        if not self.programs:
            messagebox.showwarning("Advertencia", "No hay programas agregados para ejecutar.")
            return
        for program in self.programs:
            os.startfile(program)
    
    def clear_list(self):
        self.programs = []
        self.listbox.delete(0, tk.END)
        self.save_programs()
    
    def save_programs(self):
        with open(CONFIG_FILE, "w") as file:
            json.dump(self.programs, file)
    
    def load_programs(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                self.programs = json.load(file)
                for program in self.programs:
                    self.listbox.insert(tk.END, os.path.basename(program))

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiLauncher(root)
    root.mainloop()
