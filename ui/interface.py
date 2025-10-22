import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
from src.xml_reader import read_folder
from src.excel_generator import generate_excel_report
import threading
from datetime import datetime

ctk.set_appearance_mode("Dark")  # Modo escuro elegante
ctk.set_default_color_theme("blue")  # Tema azul minimalista

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Leitor de NF-e")
        self.geometry("600x360")
        self.resizable(False, False)

        # Variáveis
        self.folder_path = ctk.StringVar()
        self.start_date = ctk.StringVar()
        self.end_date = ctk.StringVar()
        self.min_value = ctk.StringVar()
        self.progress = ctk.DoubleVar()

        # Layout
        self._build_ui()

    def _build_ui(self):
        # Título
        ctk.CTkLabel(self, text="Leitor de NF-e", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(15,10))

        # Frame principal
        frm = ctk.CTkFrame(self, corner_radius=10)
        frm.pack(padx=20, pady=10, fill="both", expand=True)

        # Pasta de XML
        ctk.CTkLabel(frm, text="Pasta com XMLs:").grid(row=0, column=0, sticky="w", pady=(10,0))
        ctk.CTkEntry(frm, textvariable=self.folder_path, width=380).grid(row=1, column=0, padx=(0,10))
        ctk.CTkButton(frm, text="Selecionar", width=100, command=self.select_folder).grid(row=1, column=1)

        # Filtros
        ctk.CTkLabel(frm, text="Filtros (opcional):").grid(row=2, column=0, sticky="w", pady=(15,0))

        ctk.CTkLabel(frm, text="Data Inicial (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", pady=(5,0))
        ctk.CTkEntry(frm, textvariable=self.start_date, width=150).grid(row=3, column=1, padx=(0,10))

        ctk.CTkLabel(frm, text="Data Final (YYYY-MM-DD):").grid(row=4, column=0, sticky="w", pady=(5,0))
        ctk.CTkEntry(frm, textvariable=self.end_date, width=150).grid(row=4, column=1, padx=(0,10))

        ctk.CTkLabel(frm, text="Valor mínimo:").grid(row=5, column=0, sticky="w", pady=(5,0))
        ctk.CTkEntry(frm, textvariable=self.min_value, width=150).grid(row=5, column=1, padx=(0,10))

        # Botões
        ctk.CTkButton(frm, text="Gerar Relatório", command=self.generate_report, width=200).grid(row=6, column=0, columnspan=2, pady=(20,10))
        ctk.CTkButton(frm, text="Sair", command=self.quit, width=80).grid(row=7, column=0, columnspan=2)

        # Barra de progresso
        self.progressbar = ctk.CTkProgressBar(frm, variable=self.progress)
        self.progressbar.grid(row=8, column=0, columnspan=2, pady=(20,10), sticky="ew")

        # Status
        self.status_label = ctk.CTkLabel(frm, text="Pronto")
        self.status_label.grid(row=9, column=0, columnspan=2, pady=(5,10))

        # Ajustes de grid
        for i in range(10):
            frm.grid_rowconfigure(i, pad=5)
        frm.grid_columnconfigure(0, weight=1)
        frm.grid_columnconfigure(1, weight=0)

    # Selecionar pasta
    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    # Atualiza status e barra de progresso
    def _set_status(self, text):
        self.status_label.configure(text=text)
        self.update_idletasks()

    def _update_progress(self, current, total):
        percent = (current / total) * 100
        self.progress.set(percent)
        self.update_idletasks()

    # Função principal
    def generate_report(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("Atenção", "Escolha a pasta que contém os XMLs.")
            return

        # Thread para não travar UI
        threading.Thread(target=self._run_generation, args=(folder,), daemon=True).start()

    def _run_generation(self, folder):
        self._set_status("Lendo XMLs...")
        notas = read_folder(folder, update_progress=self._update_progress)
        if not notas:
            self._set_status("Nenhuma nota processada.")
            messagebox.showinfo("Resultado", "Nenhuma nota processada. Verifique a pasta.")
            return

        # Aplicar filtros
        notas_filtradas = []
        for n in notas:
            # Filtro por data
            try:
                if self.start_date.get():
                    dt_start = datetime.fromisoformat(self.start_date.get())
                    dt_nota = datetime.fromisoformat(n['data_emissao'])
                    if dt_nota < dt_start:
                        continue
                if self.end_date.get():
                    dt_end = datetime.fromisoformat(self.end_date.get())
                    dt_nota = datetime.fromisoformat(n['data_emissao'])
                    if dt_nota > dt_end:
                        continue
            except Exception:
                pass  # ignora erro de conversão de data

            # Filtro por valor mínimo
            try:
                if self.min_value.get():
                    if n['valor_total'] is None or n['valor_total'] < float(self.min_value.get()):
                        continue
            except Exception:
                pass

            notas_filtradas.append(n)

        self._set_status("Gerando Excel...")
        output_dir = Path(folder) / "relatorio_output"
        out = generate_excel_report(notas_filtradas, str(output_dir))
        self._set_status("Relatório gerado com sucesso!")
        messagebox.showinfo("Concluído", f"Relatório gerado:\n{out}")
        self.progress.set(0)

def run_app():
    app = App()
    app.mainloop()
