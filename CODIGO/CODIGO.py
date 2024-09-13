import os
import tkinter as tk
from tkinter import filedialog
import unicodedata
import ctypes

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

        self.btn_select_dir = tk.Button(root, text="SELECIONAR", command=self.select_directory)
        self.btn_select_dir.pack(pady=10)

        self.btn_generate = tk.Button(root, text="GERAR", command=self.generate_names)
        self.btn_generate.pack(pady=10)

        self.text_area = tk.Text(root, wrap="word", height=15, width=50)
        self.text_area.pack(pady=10)

        self.btn_copy = tk.Button(root, text="COPIAR", command=self.copy_names)
        self.btn_copy.pack(side=tk.TOP, padx=5)

        self.btn_clear = tk.Button(root, text="LIMPAR", command=self.clear_text)
        self.btn_clear.pack(side=tk.TOP, padx=5)

        self.footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.root.geometry('800x600')

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.dir_path.set(dir_path)

    def generate_names(self):
        dir_path = self.dir_path.get()
        if os.path.isdir(dir_path):
            directory_list = []
            faixa_inicial = 1  
            total_faixas = 0
            total_musicas = 0

            def contar_mp3(path):
                return len([f for f in os.listdir(path) if f.lower().endswith('.mp3')])

            def listar_diretorios(path_atual, path_relativo=''):
                subdiretorios = [d for d in os.listdir(path_atual) if os.path.isdir(os.path.join(path_atual, d))]
                if subdiretorios:
                    for subdir in subdiretorios:
                        if subdir == "System Volume Information":
                            continue
                        novo_path_relativo = os.path.join(path_relativo, subdir)
                        listar_diretorios(os.path.join(path_atual, subdir), novo_path_relativo)
                else:
                    mp3_count = contar_mp3(path_atual)  
                    directory_list.append((path_relativo.replace(os.path.sep, '/'), mp3_count))

            listar_diretorios(dir_path)
            directory_list.sort(key=lambda s: unicodedata.normalize('NFKD', s[0]).encode('ASCII', 'ignore').decode('ASCII'))

            formatted_list = []
            for index, (path, mp3_count) in enumerate(directory_list):
                faixa_atual = faixa_inicial + total_faixas
                formatted_list.append(f"{{{str(index + 1).zfill(2)} - {str(faixa_atual).zfill(2)}}} <-> {path} <-> {{{mp3_count} MÚSICAS}}")
                total_faixas += mp3_count
                total_musicas += mp3_count

            names_str = '\n'.join(formatted_list)

            def get_drive_space(folder):
                _, total_bytes, free_bytes = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), ctypes.byref(_), ctypes.byref(total_bytes), ctypes.byref(free_bytes))
                total_memoria = total_bytes.value // (1024 ** 2)  
                memoria_livre = free_bytes.value // (1024 ** 2)  
                memoria_usada = total_memoria - memoria_livre  
                return total_memoria, memoria_livre, memoria_usada

            total_memoria, memoria_livre, memoria_usada = get_drive_space(dir_path)

            estatisticas = f"""
==========================================
            ESTATÍSTICAS:
------------------------------------------
TOTAL DE PASTAS: {len(directory_list)}
TOTAL DE MUSICAS: {total_musicas}
MEMORIA USADA: {memoria_usada} MB
MEMORIA LIVRE: {memoria_livre} MB
TOTAL DE MEMORIA: {total_memoria} MB
------------------------------------------
==========================================
"""

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, names_str + "\n" + estatisticas)

    def copy_names(self):
        names = self.text_area.get("1.0", tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(names)
        self.root.update()

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NomeArquivosApp(root)
    root.mainloop()
