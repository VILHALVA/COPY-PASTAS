import os
import tkinter as tk
from tkinter import filedialog, messagebox
import unicodedata
import ctypes
import platform

class NomeArquivosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COPY PASTAS")

        self.dir_path = tk.StringVar()
        self.dir_path.set("SELECIONE UM DIRETÓRIO")

        self.label_dir = tk.Label(root, text="DIRETÓRIO")
        self.label_dir.pack(pady=5)

        self.entry_dir = tk.Entry(root, textvariable=self.dir_path, state="readonly", width=40)
        self.entry_dir.pack(pady=5)

        dir_frame = tk.Frame(root)
        dir_frame.pack(pady=5)

        self.btn_select_dir = tk.Button(dir_frame, text="SELECIONAR", command=self.select_directory)
        self.btn_select_dir.pack(side=tk.LEFT, padx=5)

        self.btn_generate = tk.Button(dir_frame, text="GERAR", command=self.generate_names, state=tk.DISABLED)
        self.btn_generate.pack(side=tk.LEFT, padx=5)

        self.tipo = tk.StringVar(value="MP3")
        tipos = ["MP3", "TODOS", "JSON", "TXT"]
        radio_frame = tk.Frame(root)
        radio_frame.pack(pady=5)
        for tipo in tipos:
            tk.Radiobutton(radio_frame, text=tipo, variable=self.tipo, value=tipo).pack(side=tk.LEFT, padx=10)

        self.text_area = tk.Text(root, wrap="word", height=15, width=50)
        self.text_area.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.btn_copy = tk.Button(button_frame, text="COPIAR", command=self.copy_names, state=tk.DISABLED)
        self.btn_copy.pack(side=tk.LEFT, padx=5)

        self.btn_clear = tk.Button(button_frame, text="LIMPAR", command=self.clear_text, state=tk.DISABLED)
        self.btn_clear.pack(side=tk.LEFT, padx=5)

        self.footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X)

        self.root.geometry('800x600')

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.dir_path.set(dir_path)
            self.btn_generate.config(state=tk.NORMAL)

    def generate_names(self):
        tipo = self.tipo.get()
        dir_path = self.dir_path.get()
        self.text_area.delete("1.0", tk.END)

        if not os.path.isdir(dir_path):
            messagebox.showwarning("Aviso", "Por favor, selecione um diretório válido.")
            return

        if tipo in ["JSON", "TXT"]:
            file_names = [os.path.splitext(name)[0] for name in os.listdir(dir_path)]
            content = '[\n' + ', '.join([f'"{name}"' for name in file_names]) + '\n];' if tipo == "JSON" else '\n'.join(file_names)
            self.text_area.insert(tk.END, content)
            self.btn_copy.config(state=tk.NORMAL)
            self.btn_clear.config(state=tk.NORMAL)
            return

        directory_list = []
        faixa_inicial = 1
        total_musicas = 0
        total_arquivos = 0

        def contar_itens(path):
            if tipo == "MP3":
                return [f for f in os.listdir(path) if f.lower().endswith('.mp3')]
            elif tipo == "TODOS":
                return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        def listar_diretorios(path_atual, path_relativo=''):
            subdirs = [d for d in os.listdir(path_atual) if os.path.isdir(os.path.join(path_atual, d))]
            if subdirs:
                for subdir in subdirs:
                    if subdir.lower() == "system volume information":
                        continue
                    novo_path = os.path.join(path_relativo, subdir)
                    listar_diretorios(os.path.join(path_atual, subdir), novo_path)
            else:
                itens = contar_itens(path_atual)
                directory_list.append((path_relativo.replace(os.path.sep, '/'), itens))

        listar_diretorios(dir_path)
        directory_list.sort(key=lambda s: unicodedata.normalize('NFKD', s[0]).encode('ASCII', 'ignore').decode('ASCII'))

        formatted_list = []
        total_faixas = 0
        for index, (path, itens) in enumerate(directory_list):
            faixa_atual = faixa_inicial + total_faixas
            count = len(itens)

            if tipo == "MP3":
                if all("track" in f.lower() for f in itens):
                    label = f"{count} TRACKS"
                elif all("faixa" in f.lower() for f in itens):
                    label = f"{count} FAIXAS"
                else:
                    label = f"{count} MUSICAS"
                total_musicas += count
            else:
                label = f"{count} ARQUIVOS"
                total_arquivos += count

            formatted_list.append(f"{{{str(index + 1).zfill(2)} - {str(faixa_atual).zfill(2)}}} <-> {path} <-> {{{label}}}")
            total_faixas += count

        result_text = '\n'.join(formatted_list)

        def get_drive_space(folder):
            if platform.system() != "Windows":
                return 0, 0, 0
            _, total_bytes, free_bytes = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), ctypes.byref(_), ctypes.byref(total_bytes), ctypes.byref(free_bytes))
            total = total_bytes.value // (1024 ** 2)
            livre = free_bytes.value // (1024 ** 2)
            usada = total - livre
            return total, livre, usada

        total_memoria, memoria_livre, memoria_usada = get_drive_space(dir_path)
        estatisticas = f"""
==========================================
            ESTATISTICAS:
------------------------------------------
TOTAL DE PASTAS: {len(directory_list)}
{"TOTAL DE MUSICAS" if tipo == "MP3" else "TOTAL DE ARQUIVOS"}: {total_musicas if tipo == "MP3" else total_arquivos}
MEMORIA USADA: {memoria_usada} MB
MEMORIA LIVRE: {memoria_livre} MB
TOTAL DE MEMORIA: {total_memoria} MB
------------------------------------------
==========================================
"""
        self.text_area.insert(tk.END, result_text + '\n' + estatisticas)
        self.btn_copy.config(state=tk.NORMAL)
        self.btn_clear.config(state=tk.NORMAL)

    def copy_names(self):
        names = self.text_area.get("1.0", tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(names)
        self.root.update()

        messagebox.showinfo("Copiado", "Texto copiado para a área de transferência.")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.btn_copy.config(state=tk.DISABLED)
        self.btn_clear.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NomeArquivosApp(root)
    root.mainloop()
