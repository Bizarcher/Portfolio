import tkinter as tk
from tkinter import ttk, messagebox
import random

class UnachiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unachi")
        self.root.minsize(450, 400)
        self.root.maxsize(450, 400)

        self.setup_gui()

    def setup_gui(self):
        notebook = ttk.Notebook(self.root)

        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)

        notebook.add(tab1, text="Encryption")
        notebook.add(tab2, text="Decryption")
        notebook.add(tab3, text="Result")

        self.create_encryption_tab(tab1)
        self.create_decryption_tab(tab2)
        self.create_result_tab(tab3)

        notebook.grid(row=0, column=0, padx=5, pady=5)

    def create_encryption_tab(self, tab):
        label1 = tk.Label(tab, text="Enter the text to encrypt:")
        label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.input_text = tk.Text(tab, height=5, width=60)
        self.input_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        encrypt_button = tk.Button(tab, text="Encrypt", command=self.encrypt_text)
        encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def create_decryption_tab(self, tab):
        label2 = tk.Label(tab, text="Enter the encrypted text:")
        label2.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.input_text2 = tk.Text(tab, height=5, width=60)
        self.input_text2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        label3 = tk.Label(tab, text="Enter the combined keys (key1|key2):")
        label3.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.keys_entry = tk.Entry(tab)
        self.keys_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        decrypt_button = tk.Button(tab, text="Decrypt", command=self.decrypt_text)
        decrypt_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def create_result_tab(self, tab):
        label4 = tk.Label(tab, text="Result:")
        label4.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.result_text = tk.Text(tab, height=8, width=60)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def clear_text(self, text_widget):
        text_widget.delete("1.0", "end")

    def encrypt_text(self):
        input_text = self.input_text
        keys_text = self.keys_text
        encrypted_text = self.encrypted_text

        self.clear_text(keys_text)
        self.clear_text(encrypted_text)

        user_str = input_text.get("1.0", "end-1c")
        if not user_str:
            messagebox.showerror("Error", "Please enter a text to encrypt.")
            return

        usr_str_list = list(user_str)
        cusr_str_list = [ord(char) for char in user_str]
        rand_sum_list = [random.randint(1, 15) for _ in user_str]
        rand_op = [random.randint(0, 3) for _ in user_str]
        key1 = rand_sum_list
        key2 = rand_op

        scr_usr_str = []
        for i in range(len(user_str)):
            if rand_op[i] == 0 or rand_op[i] == 2:
                value = (cusr_str_list[i] + rand_sum_list[i])
            if rand_op[i] == 1 or rand_op[i] == 3:
                value = (cusr_str_list[i] - rand_sum_list[i])
            scr_usr_str.append(value)

        conscr_usr_str = [chr(value) for value in scr_usr_str]

        key1_str = ' '.join(map(str, key1))
        key2_str = ' '.join(map(str, key2))
        combined_keys = key1_str + '|' + key2_str
        encrypted_text_str = ''.join(conscr_usr_str)

        keys_text.insert("1.0", f"Combined Keys: {combined_keys}")
        encrypted_text.insert("1.0", f"Encrypted text: {encrypted_text_str}")
        self.result_text.delete("1.0", "end")

    def decrypt_text(self):
        input_text = self.input_text2
        keys_entry = self.keys_entry
        decrypted_text = self.decrypted_text

        self.clear_text(decrypted_text)

        encrypted_text = input_text.get("1.0", "end-1c")
        if not encrypted_text:
            messagebox.showerror("Error", "Please enter encrypted text to decrypt.")
            return

        combined_keys = keys_entry.get()

        if not combined_keys or '|' not in combined_keys:
            messagebox.showerror("Error", "Please enter the combined keys (key1|key2).")
            return

        key1_str, key2_str = combined_keys.split('|')
        key1 = list(map(int, key1_str.split()))
        key2 = list(map(int, key2_str.split()))

        scr_usr_str = [ord(char) for char in encrypted_text]
        decrypted_text_str = ""
        value = 0

        for i in range(len(scr_usr_str)):
            if key2[i] == 0 or key2[i] == 2:
                value = (scr_usr_str[i] - key1[i])
            if key2[i] == 1 or key2[i] == 3:
                value = (scr_usr_str[i] + key1[i])
            decrypted_text_str += chr(value)

        decrypted_text.insert("1.0", f"Decrypted text: {decrypted_text_str}")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", f"Result: {decrypted_text_str}")

    def run(self):
        self.keys_text = tk.Text(self.root, height=5, width=60)
        self.keys_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.encrypted_text = tk.Text(self.root, height=5, width=60)
        self.encrypted_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.decrypted_text = tk.Text(self.root, height=5, width=60)
        self.decrypted_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = UnachiApp(root)
    app.run()
