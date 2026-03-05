# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import datetime

# Unidade básica da lista
class Nodo:
    def __init__(self, consulta):
        self.consulta = consulta
        self.proximo = None

# Operações da lista encadeada
class ListaConsultas:
    def __init__(self):
        self.cabeca = None

    # Cadastro com verificação de agenda
    def adicionar_consulta(self, nova_consulta):
        novo_horario = nova_consulta.obter_datetime()
        
        if novo_horario is None:
            return False

        # Percorre a lista para evitar choques de 30 minutos
        atual = self.cabeca
        while atual is not None:
            horario_existente = atual.consulta.obter_datetime()
            
            if horario_existente:
                if abs(horario_existente - novo_horario) < datetime.timedelta(minutes=30):
                    return False
            
            atual = atual.proximo

        # Insere novo elemento no início
        novo_nodo = Nodo(nova_consulta)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        return True

    # Filtragem por paciente
    def buscar_por_nome(self, nome):
        resultados = []
        nome_busca = nome.strip().lower()
        atual = self.cabeca
        
        while atual is not None:
            if atual.consulta.nomePaciente.lower() == nome_busca:
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # Filtragem por dia
    def buscar_por_data(self, data):
        resultados = []
        try:
            data_normalizada = datetime.datetime.strptime(data.strip(), "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            return resultados

        atual = self.cabeca
        while atual is not None:
            if atual.consulta.data == data_normalizada:
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # Exclusão por ID
    def remover_consulta(self, id_paciente):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.consulta.codPaciente == id_paciente:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    # Atualização de dados e revalidação
    def alterar_consulta(self, id_paciente, nome=None, data=None, horario=None, medico=None, tipo=None):
        atual = self.cabeca
        nodo_alvo = None

        while atual is not None:
            if atual.consulta.codPaciente == id_paciente:
                nodo_alvo = atual
                break
            atual = atual.proximo

        if not nodo_alvo:
            return False

        consulta = nodo_alvo.consulta
        original = (consulta.nomePaciente, consulta.data, consulta.horario, consulta.nomeMedico, consulta.tipoConsulta)

        try:
            if nome: consulta.nomePaciente = nome
            if medico: consulta.nomeMedico = medico
            if tipo: consulta.tipoConsulta = tipo
            if data: consulta.data = data
            if horario: consulta.horario = horario

            if not consulta.validar_tudo():
                raise ValueError()

            if data or horario:
                novo_dt = consulta.obter_datetime()
                checa = self.cabeca
                while checa is not None:
                    if checa != nodo_alvo:
                        dt_existente = checa.consulta.obter_datetime()
                        if dt_existente and abs(dt_existente - novo_dt) < datetime.timedelta(minutes=30):
                            raise ValueError()
                    checa = checa.proximo
            
            return True

        except ValueError:
            # Reverte alterações em caso de erro
            consulta.nomePaciente, consulta.data, consulta.horario, consulta.nomeMedico, consulta.tipoConsulta = original
            return False

    def obter_cabeca(self):
        return self.cabeca
