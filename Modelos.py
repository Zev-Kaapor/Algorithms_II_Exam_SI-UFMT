# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

# Estrutura de dados da consulta

import datetime

class consulta:
    """
    Representa uma consulta médica no sistema do consultório
    Responsável por armazenar dados do paciente e validar regras de negócio
    """
    
    contador_id = 0 
    def __init__(self,nomePaciente,data,horario,nome_medico,tipoConsulta):
        
        """
        Inicializa o objeto Consulta e dispara as validações automáticas.
        
        Args:
            codPaciente (int/str): Identificador único do paciente.
            nomePaciente (str): Nome completo.
            data (str): Data no formato DD/MM/AAAA.
            horario (str): Horário no formato HH:MM (intervalos de 30min).
            nome_medico (str): Nome do profissional.
            tipoConsluta (str): 'conveniado' ou 'particular'.
        """
        
        consulta.contador_id+=1
        
        # Sanitização inicial: remove espaços e garante consistência
        self.codPaciente = consulta.contador_id
        self.nomePaciente = nomePaciente.strip()
        self.data = data.strip()
        self.horario = horario.strip()
        self.nome_medico = nome_medico.strip()
        self.tipoConsulta = tipoConsulta.strip().capitalize()

        if not self.validar_data(): 
            self.data = None
              
        if not self.validar_horario(): 
            self.horario = None
            
        if not self.validar_tipo_consulta():
            self.tipoConsulta = None
            
    
    def validar_data(self):
        '''Validação se a data existe e formata no padrão dia/mês/ano'''
        try:
            data = self.data 
            data = datetime.datetime.strptime(data,"%d/%m/%Y") # usando a biblioteca datetime ele padroniza e formata a data em dia/mês/ano
            return True
            
        except ValueError as e:
            print(f'\nErro: {e} - Data Inexistente!\n')
            return False
    
    def validar_horario(self):
        '''Validação do horário existente, formata em hora/minuto e verifica se está nos 30 min de uma consulta anterior '''
        try:
            horario = self.horario
            horario = datetime.datetime.strptime(horario,"%H:%M") # Formata o horário da classe
            
            if horario.minute == 00 or horario.minute == 30:
                return True
            else: 
                return False
            
        except ValueError:
            return False
        
    def validar_tipo_consulta(self):
        '''Validação se a consulta é convênio ou particular'''
        
        consulta_obj = self.tipoConsulta
        if(consulta_obj == 'Conveniado' or consulta_obj == 'Particular'): 
            return True
        else: 
            return False
            
        
    
    def __str__(self): 
        '''Função que imprime cada consulta individualmente com todas as informações do paciente e sua consulta'''
        return (f"=== Detalhes da Consulta ===\n"
                f"Paciente: {self.nomePaciente} (Cód: {self.codPaciente})\n"
                f"Médico: {self.nome_medico}\n"
                f"Data: {self.data} às {self.horario}\n"
                f"Tipo: {self.tipoConsulta}\n"
                f"============================")