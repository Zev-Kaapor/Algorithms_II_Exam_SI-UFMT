# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import datetime

# Estrutura de dados da consulta
class Consulta:
    contador_id = 0 

    def __init__(self, nomePaciente, data, horario, nomeMedico, tipoConsulta):
        # Sanitização e padronização
        Consulta.contador_id += 1
        self.codPaciente = Consulta.contador_id
        self.nomePaciente = nomePaciente.strip().title()
        self.data = data.strip()
        self.horario = horario.strip()
        self.nomeMedico = nomeMedico.strip().title()
        self.tipoConsulta = tipoConsulta.strip().capitalize()

        # Validações obrigatórias
        if not self.nomePaciente or any(char.isdigit() for char in self.nomePaciente):
            raise ValueError("Nome do paciente inválido ou contém números.")
            
        if not self.nomeMedico or any(char.isdigit() for char in self.nomeMedico):
            raise ValueError("Nome do médico inválido ou contém números.")

        if not self.validar_data(): 
            raise ValueError("Data inválida ou em formato incorreto.")
              
        if not self.validar_horario(): 
            raise ValueError("Horário inválido.")
            
        if not self.validar_tipo_consulta():
            raise ValueError("O tipo deve ser 'Conveniado' ou 'Particular'.")

    # Validação de data real
    def validar_data(self):
        try:
            if len(self.data) != 10:
                return False
                
            data_obj = datetime.datetime.strptime(self.data, "%d/%m/%Y")
            if data_obj.year < 2026:
                return False
            if data_obj.date() < datetime.date.today():
                return False
                
            self.data = data_obj.strftime("%d/%m/%Y")
            return True
        except ValueError:
            return False

    # Validação apenas do formato do horário
    def validar_horario(self):
        try:
            horario_obj = datetime.datetime.strptime(self.horario, "%H:%M")
            self.horario = horario_obj.strftime("%H:%M")
            return True
        except ValueError:
            return False

    # Validação do tipo de atendimento
    def validar_tipo_consulta(self):
        return self.tipoConsulta in ['Conveniado', 'Particular']

    # Representação textual para relatórios
    def __str__(self): 
        return (f"ID: {self.codPaciente:03d} | "
                f"Paciente: {self.nomePaciente:<20} | "
                f"Médico: {self.nomeMedico:<15} | "
                f"Data: {self.data} às {self.horario} | "
                f"Tipo: {self.tipoConsulta}")
