import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}"

class Paciente(Pessoa):
    pass

class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, especialidade):
        super().__init__(nome, cpf, telefone)
        self.especialidade = especialidade


    def __str__(self):
        return f"{super().__str__()}, Especialidade: {self.especialidade}"

class Consulta:
    def __init__(self, paciente, medico, data_hora, motivo):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.motivo = motivo

    def __str__(self):
        data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return (f"Consulta em {data_formatada} - Paciente: {self.paciente.nome} "
                f"com Dr(a). {self.medico.nome} ({self.medico.especialidade}) - Motivo: {self.motivo}")

class Clinica:
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.consultas = []

    def cadastrar_paciente(self, paciente):
        if paciente.cpf in self.pacientes:
            return False
        self.pacientes[paciente.cpf] = paciente
        return True

    def cadastrar_medico(self, medico):
        if medico.cpf in self.medicos:
            return False
        self.medicos[medico.cpf] = medico
        return True

    def agendar_consulta(self, cpf_paciente, cpf_medico, data_str, hora_str, motivo):
        if cpf_paciente not in self.pacientes:
            return "Paciente não encontrado."
        if cpf_medico not in self.medicos:
            return "Médico não encontrado."
        try:
            data_hora = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
        except ValueError:
            return "Data ou hora em formato inválido."

        consulta = Consulta(self.pacientes[cpf_paciente], self.medicos[cpf_medico], data_hora, motivo)
        self.consultas.append(consulta)
        return "Consulta agendada com sucesso!!"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Clínica Médica")
        self.geometry("700x500")

        self.clinica = Clinica()

        self.tabControl = ttk.Notebook(self)
        self.tab_cad_medico = ttk.Frame(self.tabControl)
        self.tab_cad_paciente = ttk.Frame(self.tabControl)
        self.tab_agendar = ttk.Frame(self.tabControl)
        self.tab_consultas = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_cad_medico, text='Cadastrar Médico')
        self.tabControl.add(self.tab_cad_paciente, text='Cadastrar Paciente')
        self.tabControl.add(self.tab_agendar, text='Agendar Consulta')
        self.tabControl.add(self.tab_consultas, text='Consultas Agendadas')
        self.tabControl.pack(expand=1, fill="both")

        self.create_widgets_cad_medico()
        self.create_widgets_cad_paciente()
        self.create_widgets_agendar()
        self.create_widgets_listar_consultas()

    def create_widgets_cad_medico(self):
        frame = self.tab_cad_medico
        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky='w', pady=5)
        self.med_nome = ttk.Entry(frame, width=40)
        self.med_nome.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="CPF:").grid(row=1, column=0, sticky='w', pady=5)
        self.med_cpf = ttk.Entry(frame, width=40)
        self.med_cpf.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Telefone:").grid(row=2, column=0, sticky='w', pady=5)
        self.med_telefone = ttk.Entry(frame, width=40)
        self.med_telefone.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Especialidade:").grid(row=3, column=0, sticky='w', pady=5)
        self.med_especialidade = ttk.Entry(frame, width=40)
        self.med_especialidade.grid(row=3, column=1, pady=5)

        btn_cadastrar = ttk.Button(frame, text="Cadastrar Médico", command=self.cadastrar_medico)
        btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=15)

    def cadastrar_medico(self):
        nome = self.med_nome.get().strip()
        cpf = self.med_cpf.get().strip()
        telefone = self.med_telefone.get().strip()
        especialidade = self.med_especialidade.get().strip()


        if not all([nome, cpf, telefone, especialidade]):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        medico = Medico(nome, cpf, telefone, especialidade)
        if self.clinica.cadastrar_medico(medico):
            messagebox.showinfo("Sucesso", f"Médico {nome} cadastrado com sucesso.")
            self.med_nome.delete(0, tk.END)
            self.med_cpf.delete(0, tk.END)
            self.med_telefone.delete(0, tk.END)
            self.med_especialidade.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Médico já cadastrado com esse CPF.")

    def create_widgets_cad_paciente(self):
        frame = self.tab_cad_paciente
        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky='w', pady=5)
        self.pac_nome = ttk.Entry(frame, width=40)
        self.pac_nome.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="CPF:").grid(row=1, column=0, sticky='w', pady=5)
        self.pac_cpf = ttk.Entry(frame, width=40)
        self.pac_cpf.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Telefone:").grid(row=2, column=0, sticky='w', pady=5)
        self.pac_telefone = ttk.Entry(frame, width=40)
        self.pac_telefone.grid(row=2, column=1, pady=5)

        btn_cadastrar = ttk.Button(frame, text="Cadastrar Paciente", command=self.cadastrar_paciente)
        btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=15)

    def cadastrar_paciente(self):
        nome = self.pac_nome.get().strip()
        cpf = self.pac_cpf.get().strip()
        telefone = self.pac_telefone.get().strip()

        if not all([nome, cpf, telefone]):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        paciente = Paciente(nome, cpf, telefone)
        if self.clinica.cadastrar_paciente(paciente):
            messagebox.showinfo("Sucesso", f"Paciente {nome} cadastrado com sucesso.")
            self.pac_nome.delete(0, tk.END)
            self.pac_cpf.delete(0, tk.END)
            self.pac_telefone.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Paciente já cadastrado com esse CPF.")

    def create_widgets_agendar(self):
        frame = self.tab_agendar
        ttk.Label(frame, text="CPF do Paciente:").grid(row=0, column=0, sticky='w', pady=5)
        self.agn_cpf_paciente = ttk.Entry(frame, width=40)
        self.agn_cpf_paciente.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="CPF do Médico:").grid(row=1, column=0, sticky='w', pady=5)
        self.agn_cpf_medico = ttk.Entry(frame, width=40)
        self.agn_cpf_medico.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Data (dd/mm/aaaa):").grid(row=2, column=0, sticky='w', pady=5)
        self.agn_data = ttk.Entry(frame, width=40)
        self.agn_data.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Hora (HH:MM):").grid(row=3, column=0, sticky='w', pady=5)
        self.agn_hora = ttk.Entry(frame, width=40)
        self.agn_hora.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Motivo:").grid(row=4, column=0, sticky='w', pady=5)
        self.agn_motivo = ttk.Entry(frame, width=40)
        self.agn_motivo.grid(row=4, column=1, pady=5)

        btn_agendar = ttk.Button(frame, text="Agendar Consulta", command=self.agendar_consulta)
        btn_agendar.grid(row=5, column=0, columnspan=2, pady=15)

    def agendar_consulta(self):
        cpf_paciente = self.agn_cpf_paciente.get().strip()
        cpf_medico = self.agn_cpf_medico.get().strip()
        data = self.agn_data.get().strip()
        hora = self.agn_hora.get().strip()
        motivo = self.agn_motivo.get().strip()

        if not all([cpf_paciente, cpf_medico, data, hora, motivo]):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        resultado = self.clinica.agendar_consulta(cpf_paciente, cpf_medico, data, hora, motivo)
        if resultado == "Consulta agendada com sucesso.":
            messagebox.showinfo("Sucesso", resultado)
            self.agn_cpf_paciente.delete(0, tk.END)
            self.agn_cpf_medico.delete(0, tk.END)
            self.agn_data.delete(0, tk.END)
            self.agn_hora.delete(0, tk.END)
            self.agn_motivo.delete(0, tk.END)
            self.atualizar_lista_consultas()
        else:
            messagebox.showerror("Erro", resultado)

    def create_widgets_listar_consultas(self):
        frame = self.tab_consultas
        self.consultas_text = tk.Text(frame, state='disabled', width=80, height=25)
        self.consultas_text.pack(padx=10, pady=10)

    def atualizar_lista_consultas(self):
        self.consultas_text.config(state='normal')
        self.consultas_text.delete(1.0, tk.END)
        if not self.clinica.consultas:
            self.consultas_text.insert(tk.END, "Nenhuma consulta agendada")
        else:
            for c in self.clinica.consultas:
                self.consultas_text.insert(tk.END, str(c) + "\n\n")
        self.consultas_text.config(state='disabled')

if __name__ == "__main__":
    app = App()
    app.mainloop()
