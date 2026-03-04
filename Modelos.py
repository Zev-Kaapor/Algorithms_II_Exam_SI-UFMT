# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

# Estrutura de dados da consulta

import datetime

# Estrutura de dados da consulta
class Consulta:
    contador_id = 0 

    def __init__(self, nome_paciente, data, horario, nome_medico, tipo_consulta):
        # Sanitização e padronização
        Consulta.contador_id += 1
        self.codPaciente = Consulta.contador_id
        self.nomePaciente = nome_paciente.strip().title()
        self.data = data.strip()
        self.horario = horario.strip()
        self.nome_medico = nome_medico.strip().title()
        self.tipoConsulta = tipo_consulta.strip().capitalize()

        # Validações obrigatórias
        if not self.nomePaciente or any(char.isdigit() for char in self.nomePaciente):
            raise ValueError("Nome do paciente inválido ou contém números.")
            
        if not self.nome_medico or any(char.isdigit() for char in self.nome_medico):
            raise ValueError("Nome do médico inválido ou contém números.")

        if not self.validar_data(): 
            raise ValueError("Data inválida ou em formato incorreto.")
              
        if not self.validar_horario(): 
            raise ValueError("Horário fora do padrão (intervalos de 30min).")
            
        if not self.validar_tipo_consulta():
            raise ValueError("O tipo deve ser 'Conveniado' ou 'Particular'.")

    # Validação de data real
    def validar_data(self):
        try:
            data_obj = datetime.datetime.strptime(self.data, "%d/%m/%Y")
            # Impede datas retroativas (opcional, mas recomendado)
            if data_obj.date() < datetime.date.today():
                return False
            self.data = data_obj.strftime("%d/%m/%Y")
            return True
        except ValueError:
            return False

    # Validação de horário e intervalo
    def validar_horario(self):
        try:
            horario_obj = datetime.datetime.strptime(self.horario, "%H:%M")
            if horario_obj.minute in [0, 30]:
                self.horario = horario_obj.strftime("%H:%M")
                return True
            return False
        except ValueError:
            return False

    # Validação do tipo de atendimento
    def validar_tipo_consulta(self):
        return self.tipoConsulta in ['Conveniado', 'Particular']

    # Representação textual simplificada
    def __str__(self): 
        return (f"ID: {self.codPaciente:03d} | "
                f"Paciente: {self.nomePaciente:<20} | "
                f"Médico: {self.nome_medico:<15} | "
                f"Data: {self.data} {self.horario} | "
                f"Tipo: {self.tipoConsulta}")