# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

# Lógica da lista e gerenciamento de nós

import datetime

# Estrutura do nó
class Nodo:
    def __init__(self, consulta):
        self.consulta = consulta
        self.proximo = None

# Gerenciamento da lista encadeada
class ListaConsultas:
    def __init__(self):
        self.cabeca = None

    # Conversão segura de data e hora
    def _converter_para_datetime(self, consulta):
        try:
            return datetime.datetime.strptime(
                f"{consulta.data} {consulta.horario}",
                "%d/%m/%Y %H:%M"
            )
        except (ValueError, AttributeError):
            return None

    # Inserção com validação de conflito
    def adicionar_consulta(self, nova_consulta):
        novo_horario = self._converter_para_datetime(nova_consulta)
        
        if novo_horario is None:
            return False

        atual = self.cabeca
        while atual is not None:
            horario_existente = self._converter_para_datetime(atual.consulta)
            
            if horario_existente:
                diferenca = abs(horario_existente - novo_horario)
                if diferenca < datetime.timedelta(minutes=30):
                    return False # Conflito de horário
            
            atual = atual.proximo

        # Alocação dinâmica no início
        novo_nodo = Nodo(nova_consulta)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        return True

    # Busca por nome
    def buscar_por_nome(self, nome):
        resultados = []
        nome_busca = nome.strip().lower()
        atual = self.cabeca
        
        while atual is not None:
            if atual.consulta.nomePaciente.lower() == nome_busca:
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # Busca por data
    def buscar_por_data(self, data):
        resultados = []
        data_busca = data.strip()
        atual = self.cabeca
        
        while atual is not None:
            if atual.consulta.data == data_busca:
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # Retorna o nó inicial para o relatório do Hallan
    def obter_cabeca(self):
        return self.cabeca
