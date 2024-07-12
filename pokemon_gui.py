import tkinter as tk

class PokedexGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokedex")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="red")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        #Label
        self.label = tk.Label(self.root, text="P O K E D E X", font="Arial 18 bold", fg="white", bg="red")
        self.label.pack(pady=30)

        #Entry
        self.entry_pokemon_name = tk.Entry(self.root, width=50)
        self.entry_pokemon_name.place(x=100, y=400)

        #Button
        self.search_button = tk.Button(self.root, text="Buscar Pokemon", bg="red", fg="white", command=self.search_pokemon)
        self.search_button.place(x=200, y=450)


    def search_pokemon(self):
        # Aquí puedes agregar la funcionalidad de búsqueda
        pokemon_name = self.entry_pokemon_name.get()
        print(f"Buscando información para {pokemon_name}")
        # Lógica de búsqueda

if __name__ == "__main__":
    PokedexGUI()

