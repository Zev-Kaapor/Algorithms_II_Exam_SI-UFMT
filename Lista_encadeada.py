# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

# Lógica da lista e gerenciamento de nós

import datetime

class ListaConsultas:
    def __init__(self):
        self.consultas = []

    # Converte data + horário da consulta para objeto datetime
    def _converter_para_datetime(self, consulta):
        return datetime.datetime.strptime(
            f"{consulta.data} {consulta.horario}",
            "%d/%m/%Y %H:%M"
        )

    # Adiciona consulta respeitando a regra dos 30 minutos
    def adicionar_consulta(self, nova_consulta):
        novo_horario = self._converter_para_datetime(nova_consulta)

        for consulta in self.consultas:
            horario_existente = self._converter_para_datetime(consulta)

            diferenca = abs(horario_existente - novo_horario)

            if diferenca < datetime.timedelta(minutes=30):
                print("Já existe uma consulta nesse intervalo de 30 minutos.")
                return False

        self.consultas.append(nova_consulta)
        print("Consulta adicionada com sucesso.")
        return True

    # Busca por nome do paciente
    def buscar_por_nome(self, nome):
        resultados = []

        for consulta in self.consultas:
            if consulta.nomePaciente.lower() == nome.lower():
                resultados.append(consulta)

        return resultados

    # Busca por data
    def buscar_por_data(self, data):
        resultados = []

        for consulta in self.consultas:
            if consulta.data == data:
                resultados.append(consulta)

        return resultados
