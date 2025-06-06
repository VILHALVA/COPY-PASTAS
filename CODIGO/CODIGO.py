import os
import platform
import unicodedata
import ctypes
import customtkinter as ctk
from tkinter import filedialog
import threading
import time

class NomeArquivosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COPY PASTAS")

        self.label_dir = ctk.CTkLabel(
            root, text="COPY PASTAS", font=("Arial", 32, "bold")
        )
        self.label_dir.pack(pady=10)

        self.dir_path = ctk.StringVar(value="SELECIONE UM DIRETÓRIO!")
        self.entry_dir = ctk.CTkEntry(
            root,
            textvariable=self.dir_path,
            state="readonly",
            justify="center"
        )
        self.entry_dir.pack(fill="x", padx=20, pady=(0, 10))

        dir_frame = ctk.CTkFrame(root, fg_color="transparent")
        dir_frame.pack(pady=(0, 10))

        self.btn_select_dir = ctk.CTkButton(
            dir_frame, text="SELECIONAR", command=self.select_directory
        )
        self.btn_select_dir.pack(side="left", padx=5)

        self.btn_generate = ctk.CTkButton(
            dir_frame, text="GERAR", command=self.generate_names, state="disabled"
        )
        self.btn_generate.pack(side="left", padx=5)

        self.tipo = ctk.StringVar(value="MP3")
        tipos = ["MP3", "TODOS", "JSON", "TXT"]

        tipo_frame = ctk.CTkFrame(root)
        tipo_frame.pack(pady=10, anchor="center")  

        botoes_frame = ctk.CTkFrame(tipo_frame, fg_color="transparent")
        botoes_frame.pack(anchor="center") 

        for t in tipos:
            ctk.CTkRadioButton(
                botoes_frame, text=t, variable=self.tipo, value=t
            ).pack(side="left", padx=10)

        self.text_area = ctk.CTkTextbox(root)
        self.text_area.pack(expand=True, fill="both", padx=20, pady=(0, 10))

        button_frame = ctk.CTkFrame(root, fg_color="transparent")
        button_frame.pack(pady=(0, 10))
        self.btn_copy = ctk.CTkButton(
            button_frame, text="COPIAR", command=self.copy_names, state="disabled"
        )
        self.btn_copy.pack(side="left", padx=5)
        self.btn_clear = ctk.CTkButton(
            button_frame, text="LIMPAR", command=self.clear_text, state="disabled"
        )
        self.btn_clear.pack(side="left", padx=5)

        self.footer_label = ctk.CTkLabel(
            root,
            text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA",
            text_color="white",
            bg_color="gray",
        )
        self.footer_label.pack(side="bottom", fill="x", pady=(10, 0))

        self.root.after(0, lambda: self.root.state('zoomed'))

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.dir_path.set(dir_path)
            self.btn_generate.configure(state="normal")

    def generate_names(self):
        tipo = self.tipo.get()
        dir_path = self.dir_path.get()
        self.text_area.delete("1.0", "end")

        if not os.path.isdir(dir_path):
            return

        if tipo in ["JSON", "TXT"]:
            file_names = [
            os.path.splitext(name)[0]
            for name in os.listdir(dir_path)
            if name.lower() != "system volume information"
        ]

            content = '{\n' + ', '.join([f'"{name}"' for name in file_names]) + '\n};' if tipo == "JSON" else '\n'.join(file_names)
            self.text_area.insert("end", content)
            self.btn_copy.configure(state="normal")
            self.btn_clear.configure(state="normal")
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
            subdirs = [
                d for d in os.listdir(path_atual)
                if os.path.isdir(os.path.join(path_atual, d))
            ]
            if subdirs:
                for subdir in subdirs:
                    if subdir.lower() == "system volume information":
                        continue
                    novo_path = os.path.join(path_relativo, subdir)
                    listar_diretorios(
                        os.path.join(path_atual, subdir), novo_path
                    )
            else:
                itens = contar_itens(path_atual)
                directory_list.append(
                    (path_relativo.replace(os.path.sep, '/'), itens)
                )

        listar_diretorios(dir_path)
        directory_list.sort(
            key=lambda s: unicodedata.normalize('NFKD', s[0])
                              .encode('ASCII', 'ignore')
                              .decode('ASCII')
        )

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

            formatted_list.append(
                f"{{{str(index + 1).zfill(2)} - {str(faixa_atual).zfill(2)}}} "
                f"<-> {path} <-> {{{label}}}"
            )
            total_faixas += count

        result_text = '\n'.join(formatted_list)

        def get_drive_space(folder):
            if platform.system() != "Windows":
                return 0, 0, 0
            _, total_bytes, free_bytes = (
                ctypes.c_ulonglong(),
                ctypes.c_ulonglong(),
                ctypes.c_ulonglong()
            )
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                ctypes.c_wchar_p(folder),
                ctypes.byref(_),
                ctypes.byref(total_bytes),
                ctypes.byref(free_bytes)
            )
            total = total_bytes.value // (1024 ** 2)
            livre = free_bytes.value // (1024 ** 2)
            usada = total - livre
            return total, livre, usada

        total_memoria, memoria_livre, memoria_usada = get_drive_space(dir_path)
        estatisticas = (
            "\n=============================\n"
            "            ESTATISTICAS:\n"
            "=============================\n"
            f"TOTAL DE PASTAS: {len(directory_list)}\n"
            f"{'TOTAL DE MUSICAS' if tipo == 'MP3' else 'TOTAL DE ARQUIVOS'}: "
            f"{total_musicas if tipo == 'MP3' else total_arquivos}\n"
            f"MEMORIA USADA: {memoria_usada} MB\n"
            f"MEMORIA LIVRE: {memoria_livre} MB\n"
            f"TOTAL DE MEMORIA: {total_memoria} MB\n"
            "=============================\n"
            "=============================\n"
        )
        self.text_area.insert("end", result_text + estatisticas)
        self.btn_copy.configure(state="normal")
        self.btn_clear.configure(state="normal")

    def show_toast(self, msg="Texto copiado!", duration=3):
        toast = ctk.CTkToplevel(self.root)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)

        x = self.root.winfo_x() + 100
        y = self.root.winfo_y() + 100
        toast.geometry(f"250x50+{x}+{y}")

        label = ctk.CTkLabel(toast, text=msg, bg_color="black", text_color="white")
        label.pack(expand=True, fill="both")

        threading.Thread(
            target=lambda: (time.sleep(duration), toast.destroy()),
            daemon=True
        ).start()

    def copy_names(self):
        names = self.text_area.get("1.0", "end")
        self.root.clipboard_clear()
        self.root.clipboard_append(names)
        self.root.update()
        self.show_toast()

    def clear_text(self):
        self.text_area.delete("1.0", "end")
        self.btn_copy.configure(state="disabled")
        self.btn_clear.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = NomeArquivosApp(root)
    root.mainloop()