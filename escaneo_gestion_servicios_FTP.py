#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox, filedialog
from ftplib import FTP
import subprocess
import os


class SimpleMenuEscaner:
    def __init__(self, root):
        self.root = root
        self.current_path_file = ""

        # Resultados
        self.frame_resultados = tk.Frame(root, bd=3, bg="gray")
        self.text_area = tk.Text(self.frame_resultados, bg="white")
        self.frame_resultados.pack(side=tk.RIGHT, padx=10,
                                   pady=5, fill=tk.BOTH, expand=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Campos de entrada
        self.frame_escaneo = tk.Frame(root, borderwidth=3)
        self.frame_escaneo.pack(side=tk.LEFT, padx=10, pady=5)

        self.label_ip = tk.Label(self.frame_escaneo, text="IP:")
        self.label_ip.pack()

        self.entry_ip = tk.Entry(self.frame_escaneo, fg="green")
        self.entry_ip.pack()

        self.label_usuario = tk.Label(self.frame_escaneo,
                                      text="(Opcional para escaneo) Usuario:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self.frame_escaneo, fg="green")
        self.entry_usuario.pack()

        self.btn_escanear_FTP = tk.Button(self.frame_escaneo,
                                          text="Escanear FTP",
                                          command=self.escanear_ftp)
        self.btn_escanear_FTP.pack(pady=10)

        self.btn_forzar_passw_FTP = tk.Button(self.frame_escaneo,
                                              text="Forzar contraseñas",
                                              command=self.forzar_contrasenas)
        self.btn_forzar_passw_FTP.pack(pady=10)

    def escanear_ftp(self):
        ip = self.entry_ip.get()
        if not ip:
            messagebox.showwarning("Advertencia", "La IP no puede estar vacía")
            return
        self.clear()
        self.text_area.insert(tk.END, f"Iniciando escaneo de FTP en {ip}\n")
        try:
            ftp = FTP(ip)
            ftp.login()
            self.text_area.insert(tk.END,
                                  f"Conexión FTP anónima exitosa en {ip}\n")
            ftp.quit()
        except Exception as e:
            self.text_area.insert(tk.END, f"Error en la conexión FTP: {e}\n")

    def forzar_contrasenas(self):
        ip = self.entry_ip.get()
        user = self.entry_usuario.get()
        rockyou_path = "/usr/share/wordlists/rockyou.txt"
        if not ip or not user:
            messagebox.showwarning("Advertencia",
                                   "La IP y el Usuario no pueden estar vacíos")
            return

        if not os.path.exists(rockyou_path):
            messagebox.showwarning("Recurso faltante",
                                   "El archivo rockyou.txt no se encuentra en"
                                   "/usr/share/wordlists/."
                                   "Por favor, descárgalo e intenta de nuevo.")
            return

        self.clear()
        self.text_area.insert(tk.END,
                              f"Iniciando fuerza bruta de contraseñas en {ip}"
                              f" para el usuario {user}\n")

        hydra_command = f"hydra -l{user} -P{rockyou_path} ftp://{ip} -t 16"

        try:
            result = subprocess.run(hydra_command, shell=True,
                                    capture_output=True, text=True)
            self.text_area.insert(tk.END, result.stdout)
            self.text_area.insert(tk.END, result.stderr)
        except Exception as e:
            self.text_area.insert(tk.END, f"Error al ejecutar Hydra: {e}\n")

    def nuevo_archivo(self):
        self.clear()
        self.entry_ip.delete(0, tk.END)
        self.entry_usuario.delete(0, tk.END)
        print("\n[*] Nuevo archivo iniciado")

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[
                                                   ("Text files",
                                                    "*.txt"),
                                                   ("All files", "*.*")])
        if file_path:
            self.current_path_file = file_path
            with open(file_path, 'r') as file:
                content = file.read()
                self.clear()
                self.text_area.insert(tk.END, content)

    def guardar_archivo(self):
        if not self.current_path_file:
            self.guardar_como_archivo()
        else:
            with open(self.current_path_file, 'w') as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)

    def guardar_como_archivo(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[
                                                     ("Text files",
                                                      "*.txt"),
                                                     ("All files", "*.*")])
        if file_path:
            self.current_path_file = file_path
            self.guardar_archivo()

    def obtener_ayuda(self):
        messagebox.showinfo("Ayuda",
                            "Esta es una aplicación para escanear"
                            "y gestionar servicios FTP.")

    def clear(self):
        self.text_area.delete('1.0', 'end')


root = tk.Tk()
root.geometry("1000x600")
root.title("Aplicación de Escaneo y Gestión de Servicios FTP")
escaner = SimpleMenuEscaner(root)

# Menú
menu_bar = tk.Menu(root, border=5, foreground="green")
root.config(menu=menu_bar)

sub_menu_archivo = tk.Menu(menu_bar, tearoff=0)
sub_menu_ayuda = tk.Menu(menu_bar, tearoff=0)

sub_menu_archivo.add_command(label="Nuevo", command=escaner.nuevo_archivo)
sub_menu_archivo.add_command(label="Abrir", command=escaner.abrir_archivo)
sub_menu_archivo.add_command(label="Guardar", command=escaner.guardar_archivo)
sub_menu_archivo.add_command(label="Guardar como...",
                             command=escaner.guardar_como_archivo)

sub_menu_ayuda.add_command(label="Acerca de", command=escaner.obtener_ayuda)

menu_bar.add_cascade(label="Archivo", menu=sub_menu_archivo)
menu_bar.add_cascade(label="Ayuda", menu=sub_menu_ayuda)

root.mainloop()
