# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

# Lógica da lista e gerenciamento de nós

import datetime

# Nodo da lista simplesmente encadeada
class Nodo:
    def __init__(self, consulta):
        self.consulta = consulta
        self.proximo = None


class ListaConsultas:
    def __init__(self):
        self.cabeca = None

    # Converte data + horário para datetime
    def _converter_para_datetime(self, consulta):
        return datetime.datetime.strptime(
            f"{consulta.data} {consulta.horario}",
            "%d/%m/%Y %H:%M"
        )

    # Adicionar consulta respeitando intervalo de 30 minutos
    def adicionar_consulta(self, nova_consulta):
        novo_horario = self._converter_para_datetime(nova_consulta)

        atual = self.cabeca

        while atual is not None:
            horario_existente = self._converter_para_datetime(atual.consulta)
            diferenca = abs(horario_existente - novo_horario)

            if diferenca < datetime.timedelta(minutes=30):
                print("Já existe uma consulta nesse intervalo de 30 minutos.")
                return False

            atual = atual.proximo

        # Inserção no início da lista
        novo_nodo = Nodo(nova_consulta)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

        print("Consulta adicionada com sucesso.")
        return True

    # Buscar por nome
    def buscar_por_nome(self, nome):
        resultados = []
        atual = self.cabeca

        while atual is not None:
            if atual.consulta.nomePaciente.lower() == nome.lower():
                resultados.append(atual.consulta)

            atual = atual.proximo

        return resultados

    # Buscar por data
    def buscar_por_data(self, data):
        resultados = []
        atual = self.cabeca

        while atual is not None:
            if atual.consulta.data == data:
                resultados.append(atual.consulta)

            atual = atual.proximo

        return resultados

    # Método opcional para listar todas
    def listar_todas(self):
        atual = self.cabeca

        while atual is not None:
            print(atual.consulta)
            atual = atual.proximo
