# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import datetime

# Objeto com dados e regras da consulta
class Consulta:
    contador_id = 0 

    def __init__(self, nomePaciente, data, horario, nomeMedico, tipoConsulta):
        Consulta.contador_id += 1
        self.codPaciente = Consulta.contador_id
        
        self.nomePaciente = nomePaciente
        self.data = data
        self.horario = horario
        self.nomeMedico = nomeMedico
        self.tipoConsulta = tipoConsulta

        if not self.validar_tudo():
            raise ValueError("Dados inválidos.")

    # Converte strings em objeto de tempo
    def obter_datetime(self):
        try:
            return datetime.datetime.strptime(f"{self.data} {self.horario}", "%d/%m/%Y %H:%M")
        except (ValueError, AttributeError):
            return None

    # Executa todas as verificações
    def validar_tudo(self):
        return (self.validar_nomes() and 
                self.validar_data() and 
                self.validar_horario() and 
                self.validar_tipo_consulta())

    # Formatação e checagem de nomes
    def validar_nomes(self):
        self.nomePaciente = str(self.nomePaciente).strip().title()
        self.nomeMedico = str(self.nomeMedico).strip().title()
        
        if not self.nomePaciente or any(char.isdigit() for char in self.nomePaciente):
            return False
        if not self.nomeMedico or any(char.isdigit() for char in self.nomeMedico):
            return False
        return True

    # Checagem de calendário e ano
    def validar_data(self):
        try:
            self.data = str(self.data).strip()
            if len(self.data) != 10:
                return False
                
            data_obj = datetime.datetime.strptime(self.data, "%d/%m/%Y")
            if data_obj.year < 2026 or data_obj.date() < datetime.date.today():
                return False
                
            self.data = data_obj.strftime("%d/%m/%Y")
            return True
        except ValueError:
            return False

    # Checagem de formato de hora
    def validar_horario(self):
        try:
            self.horario = str(self.horario).strip()
            horario_obj = datetime.datetime.strptime(self.horario, "%H:%M")
            self.horario = horario_obj.strftime("%H:%M")
            return True
        except ValueError:
            return False

    # Regras de tipo de atendimento
    def validar_tipo_consulta(self):
        self.tipoConsulta = str(self.tipoConsulta).strip().capitalize()
        return self.tipoConsulta in ['Conveniado', 'Particular']

    # Formatação para impressão
    def __str__(self): 
        return (f"ID: {self.codPaciente:03d} | "
                f"Paciente: {self.nomePaciente:<20} | "
                f"Médico: {self.nomeMedico:<15} | "
                f"Data: {self.data} às {self.horario} | "
                f"Tipo: {self.tipoConsulta}")
