import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry_item.get()
    if item:
        listbox_items.insert(tk.END, item)
        entry_item.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite um item para adicionar!")

def delete_item():
    try:
        selected_item_index = listbox_items.curselection()[0]
        listbox_items.delete(selected_item_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um item para excluir!")

def clear_list():
    listbox_items.delete(0, tk.END)

def save_list():
    with open("shopping_list.txt", "w") as file:
        items = listbox_items.get(0, tk.END)
        for item in items:
            file.write(f"{item}\n")
    messagebox.showinfo("Informação", "Lista de compras salva com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("Lista de Compras")
root.geometry("400x400")

# Widgets
label_item = tk.Label(root, text="Item:")
label_item.pack(pady=5)

entry_item = tk.Entry(root, width=50)
entry_item.pack(pady=5)

button_add = tk.Button(root, text="Adicionar", command=add_item)
button_add.pack(pady=5)

listbox_items = tk.Listbox(root, width=50, height=10)
listbox_items.pack(pady=5)

button_delete = tk.Button(root, text="Excluir", command=delete_item)
button_delete.pack(pady=5)

button_clear = tk.Button(root, text="Limpar Lista", command=clear_list)
button_clear.pack(pady=5)

button_save = tk.Button(root, text="Salvar Lista", command=save_list)
button_save.pack(pady=5)

# Execução da janela principal
root.mainloop()
