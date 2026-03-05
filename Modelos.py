# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import datetime

# representacao da consulta
class Consulta:
    def __init__(self, cod, nomePaciente, data, horario, nomeMedico, tipoConsulta):
        self.codPaciente = cod
        self.nomePaciente = str(nomePaciente).strip().title()
        self.data = str(data).strip()
        self.horario = str(horario).strip()
        self.nomeMedico = str(nomeMedico).strip().title()
        self.tipoConsulta = str(tipoConsulta).strip().capitalize()

    # conversao para datetime
    def obter_datetime(self):
        try:
            return datetime.datetime.strptime(f"{self.data} {self.horario}", "%d/%m/%Y %H:%M")
        except:
            return None

    # formatacao visual
    def __str__(self): 
        return (f"ID: {self.codPaciente:03d} | "
                f"Paciente: {self.nomePaciente:<20} | "
                f"Médico: {self.nomeMedico:<15} | "
                f"Data: {self.data} às {self.horario} | "
                f"Tipo: {self.tipoConsulta}")
