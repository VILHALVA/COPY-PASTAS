import os
import platform
import unicodedata
import ctypes
import customtkinter as ctk
from tkinter import filedialog
import threading
import time

def is_oculto_ou_sistema(path):
    if os.name == "nt":  
        try:
            atributos = ctypes.windll.kernel32.GetFileAttributesW(str(path))
            if atributos == -1:
                return False
            FILE_ATTRIBUTE_HIDDEN = 0x2
            FILE_ATTRIBUTE_SYSTEM = 0x4
            return bool(atributos & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
        except Exception:
            return False
    else:  
        return os.path.basename(path).startswith(".")

class Explorador:
    def __init__(self, parent):
        self.parent = parent

        self.label_dir = ctk.CTkLabel(parent, text="EXPLORADOR", font=("Arial", 32, "bold"))
        self.label_dir.pack(pady=10)

        self.dir_path = ctk.StringVar(value="SELECIONE UM DIRETÓRIO!")
        self.entry_dir = ctk.CTkEntry(parent, textvariable=self.dir_path, state="readonly", justify="center")
        self.entry_dir.pack(fill="x", padx=20, pady=(0, 10))

        dir_frame = ctk.CTkFrame(parent, fg_color="transparent")
        dir_frame.pack(pady=(0, 10))

        self.btn_select_dir = ctk.CTkButton(dir_frame, text="SELECIONAR", command=self.select_directory)
        self.btn_select_dir.pack(side="left", padx=5)

        self.btn_generate = ctk.CTkButton(dir_frame, text="GERAR", command=self.generate_names, state="disabled")
        self.btn_generate.pack(side="left", padx=5)

        self.tipo = ctk.StringVar(value="MP3")
        tipos = ["MP3", "TODOS", "JSON", "TXT"]

        tipo_frame = ctk.CTkFrame(parent)
        tipo_frame.pack(pady=10, anchor="center")  

        botoes_frame = ctk.CTkFrame(tipo_frame, fg_color="transparent")
        botoes_frame.pack(anchor="center") 

        for t in tipos:
            ctk.CTkRadioButton(botoes_frame, text=t, variable=self.tipo, value=t).pack(side="left", padx=10)

        self.text_area = ctk.CTkTextbox(parent)
        self.text_area.pack(expand=True, fill="both", padx=20, pady=(0, 10))

        button_frame = ctk.CTkFrame(parent, fg_color="transparent")
        button_frame.pack(pady=(0, 10))
        self.btn_copy = ctk.CTkButton(button_frame, text="COPIAR", command=self.copy_names, state="disabled")
        self.btn_copy.pack(side="left", padx=5)
        self.btn_clear = ctk.CTkButton(button_frame, text="LIMPAR", command=self.clear_text, state="disabled")
        self.btn_clear.pack(side="left", padx=5)

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
                if not is_oculto_ou_sistema(os.path.join(dir_path, name))
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
                return [
                    f for f in os.listdir(path)
                    if f.lower().endswith('.mp3') and not is_oculto_ou_sistema(os.path.join(path, f))
                ]
            elif tipo == "TODOS":
                return [
                    f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f)) and not is_oculto_ou_sistema(os.path.join(path, f))
                ]

        def listar_diretorios(path_atual, path_relativo=''):
            subdirs = [
                d for d in os.listdir(path_atual)
                if os.path.isdir(os.path.join(path_atual, d)) and not is_oculto_ou_sistema(os.path.join(path_atual, d))
            ]
            if subdirs:
                for subdir in subdirs:
                    novo_path = os.path.join(path_relativo, subdir)
                    listar_diretorios(os.path.join(path_atual, subdir), novo_path)
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
        toast = ctk.CTkToplevel(self.parent)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)

        x = self.parent.winfo_x() + 100
        y = self.parent.winfo_y() + 100
        toast.geometry(f"250x50+{x}+{y}")

        label = ctk.CTkLabel(toast, text=msg, bg_color="black", text_color="white")
        label.pack(expand=True, fill="both")

        threading.Thread(
            target=lambda: (time.sleep(duration), toast.destroy()),
            daemon=True
        ).start()

    def copy_names(self):
        names = self.text_area.get("1.0", "end")
        self.parent.clipboard_clear()
        self.parent.clipboard_append(names)
        self.parent.update()
        self.show_toast()

    def clear_text(self):
        self.text_area.delete("1.0", "end")
        self.btn_copy.configure(state="disabled")
        self.btn_clear.configure(state="disabled")

class Comparador:
    def __init__(self, parent):
        self.parent = parent

        self.diretorio1 = ""
        self.diretorio2 = ""

        self.label_titulo = ctk.CTkLabel(parent, text="COMPARADOR", font=("Arial", 32, "bold"))
        self.label_titulo.pack(pady=(20, 10))

        frame_top = ctk.CTkFrame(parent)
        frame_top.pack(pady=10, padx=20, fill="x")

        frame_botoes = ctk.CTkFrame(frame_top)
        frame_botoes.pack(anchor="center")

        self.btn_dir1 = ctk.CTkButton(frame_botoes, text="DIRETÓRIO 1", command=self.selecionar_diretorio1)
        self.btn_dir1.pack(side="left", padx=10)

        self.btn_dir2 = ctk.CTkButton(frame_botoes, text="DIRETÓRIO 2", command=self.selecionar_diretorio2, state="disabled")
        self.btn_dir2.pack(side="left", padx=10)

        self.result_box = ctk.CTkTextbox(parent, width=600, height=250)
        self.result_box.pack(pady=10, padx=20, expand=True, fill="both")

        frame_bottom = ctk.CTkFrame(parent)
        frame_bottom.pack(pady=10)

        self.btn_copiar = ctk.CTkButton(frame_bottom, text="COPIAR", command=self.copy_names, state="disabled")
        self.btn_copiar.pack(side="left", padx=10)

        self.btn_limpar = ctk.CTkButton(frame_bottom, text="LIMPAR", command=self.limpar_resultado, state="disabled")
        self.btn_limpar.pack(side="left", padx=10)

    def show_toast(self, msg="Texto copiado!", duration=3):
        toast = ctk.CTkToplevel(self.parent)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)

        x = self.parent.winfo_x() + 100
        y = self.parent.winfo_y() + 100
        toast.geometry(f"250x50+{x}+{y}")

        label = ctk.CTkLabel(toast, text=msg, fg_color="black", text_color="white")
        label.pack(expand=True, fill="both")

        threading.Thread(
            target=lambda: (time.sleep(duration), toast.destroy()),
            daemon=True
        ).start()

    def copy_names(self):
        names = self.result_box.get("1.0", "end").strip()
        if names:
            self.parent.clipboard_clear()
            self.parent.clipboard_append(names)
            self.parent.update()
            self.show_toast("Texto copiado!")

    def selecionar_diretorio1(self):
        self.diretorio1 = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO 1 (PAI)")
        if self.diretorio1:
            self.result_box.insert("end", f"DIRETÓRIO 1 (PAI): {self.diretorio1}\n")
            self.btn_dir2.configure(state="normal")

    def selecionar_diretorio2(self):
        self.diretorio2 = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO 2 (FILHO)")
        if self.diretorio2:
            self.result_box.insert("end", f"DIRETÓRIO 2 (FILHO): {self.diretorio2}\n\n")
            self.comparar_pastas()

    def listar_subpastas(self, raiz):
        subpastas = set()
        for dirpath, dirnames, _ in os.walk(raiz):
            dirnames[:] = [d for d in dirnames if not is_oculto_ou_sistema(os.path.join(dirpath, d))]
            for dirname in dirnames:
                caminho_relativo = os.path.relpath(os.path.join(dirpath, dirname), raiz)
                subpastas.add(caminho_relativo.replace("\\", "/"))
        return subpastas

    def listar_arquivos(self, raiz):
        arquivos = set()
        for dirpath, _, filenames in os.walk(raiz):
            for filename in filenames:
                caminho_completo = os.path.join(dirpath, filename)
                if not is_oculto_ou_sistema(caminho_completo):
                    caminho_relativo = os.path.relpath(caminho_completo, raiz)
                    arquivos.add(caminho_relativo.replace("\\", "/"))
        return arquivos

    def comparar_pastas(self):
        if not self.diretorio1 or not self.diretorio2:
            return

        pastas1 = self.listar_subpastas(self.diretorio1)
        pastas2 = self.listar_subpastas(self.diretorio2)

        arquivos1 = self.listar_arquivos(self.diretorio1)
        arquivos2 = self.listar_arquivos(self.diretorio2)

        faltando_pastas = pastas1 - pastas2
        faltando_arquivos = arquivos1 - arquivos2

        if faltando_pastas:
            self.result_box.insert("end", "📁 PASTAS/SUBPASTAS FALTANDO NO DIRETÓRIO 2:\n\n")
            for pasta in sorted(faltando_pastas):
                self.result_box.insert("end", f"- {pasta}/\n")
            self.result_box.insert("end", "\n")

        if faltando_arquivos:
            self.result_box.insert("end", "📄 ARQUIVOS FALTANDO NO DIRETÓRIO 2:\n\n")
            for arquivo in sorted(faltando_arquivos):
                self.result_box.insert("end", f"- {arquivo}\n")
            self.result_box.insert("end", "\n")

        if not faltando_pastas and not faltando_arquivos:
            self.result_box.insert("end", "✅ NENHUMA PASTA OU ARQUIVO FALTANDO. OS DIRETÓRIOS ESTÃO SINCRONIZADOS!\n")

        self.btn_dir1.configure(state="disabled")
        self.btn_dir2.configure(state="disabled")
        self.btn_copiar.configure(state="normal")
        self.btn_limpar.configure(state="normal")

    def limpar_resultado(self):
        self.result_box.delete("1.0", "end")
        self.btn_copiar.configure(state="disabled")
        self.btn_limpar.configure(state="disabled")
        self.btn_dir1.configure(state="normal")
        self.btn_dir2.configure(state="disabled")
        self.diretorio1 = ""
        self.diretorio2 = "" 

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("COPY PASTAS")
        self.after(100, lambda: self.state("zoomed"))

        tabview = ctk.CTkTabview(
            self,
            width=1100,
            height=600,
            corner_radius=15,  
            border_width=2,
            border_color="#222222",
            fg_color="#0D0D0D",
            segmented_button_fg_color="#333333",
            segmented_button_selected_color="#28a745", 
            segmented_button_selected_hover_color="#3ac169",  
            segmented_button_unselected_color="#007bff",  
            segmented_button_unselected_hover_color="#339cff"  
        )
        tabview.pack(expand=True, fill="both", padx=20, pady=20)

        abas = {
            "🔍 EXPLORAR": Explorador,
            "📂 COMPARAR": Comparador
        }

        for nome, app_class in abas.items():
            tab = tabview.add(nome)              
            tab.grid_columnconfigure(0, weight=1)  
            app_class(tab)                       

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = MainApp()
    app.mainloop()
