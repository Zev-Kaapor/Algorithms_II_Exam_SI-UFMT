# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import json
import os
import datetime
from Modelos import Consulta

# estrutura do nodo
class Nodo:
    def __init__(self, consulta):
        self.consulta = consulta
        self.proximo = None

# gerenciamento da lista encadeada
class ListaConsultas:
    def __init__(self):
        self.cabeca = None
        self.diretorio = "data"
        self.arquivo = os.path.join(self.diretorio, "consultas.json")
        
        if not os.path.exists(self.diretorio):
            os.makedirs(self.diretorio)
            
        self.carregar_dados()

    # persistencia json ordenada por id
    def salvar_dados(self):
        dados = []
        atual = self.cabeca
        while atual:
            c = atual.consulta
            dados.append({
                "cod": c.codPaciente,
                "paciente": c.nomePaciente,
                "data": c.data,
                "horario": c.horario,
                "medico": c.nomeMedico,
                "tipo": c.tipoConsulta
            })
            atual = atual.proximo
        
        dados.sort(key=lambda x: x["cod"])
        
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    # carregamento de dados json
    def carregar_dados(self):
        if not os.path.exists(self.arquivo):
            return

        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                for item in dados:
                    c = Consulta(item["cod"], item["paciente"], item["data"], 
                                 item["horario"], item["medico"], item["tipo"])
                    self.adicionar_consulta(c, salvar=False)
        except:
            pass

    # busca menor id disponivel
    def gerar_proximo_id(self):
        ids_ocupados = []
        atual = self.cabeca
        while atual:
            ids_ocupados.append(atual.consulta.codPaciente)
            atual = atual.proximo
        
        novo_id = 1
        while novo_id in ids_ocupados:
            novo_id += 1
        return novo_id

    # geracao de tag para nomes
    def gerar_tag_nome(self, nome_novo):
        tags_ocupadas = []
        atual = self.cabeca
        while atual:
            if " #" in atual.consulta.nomePaciente:
                partes = atual.consulta.nomePaciente.split(" #")
                if partes[0].lower() == nome_novo.lower():
                    tags_ocupadas.append(int(partes[1]))
            atual = atual.proximo
        
        tag_livre = 0
        while tag_livre in tags_ocupadas:
            tag_livre += 1
        return f"{tag_livre:04d}"

    # validacao de conflito de horario
    def verificar_conflito_imediato(self, data_alvo, horario_alvo):
        try:
            nova_dt = datetime.datetime.strptime(f"{data_alvo} {horario_alvo}", "%d/%m/%Y %H:%M")
        except:
            return None

        atual = self.cabeca
        while atual:
            existente_dt = atual.consulta.obter_datetime()
            if existente_dt:
                diferenca = abs((nova_dt - existente_dt).total_seconds() / 60)
                if diferenca < 30:
                    return atual.consulta
            atual = atual.proximo
        return None

    # insercao na lista
    def adicionar_consulta(self, nova, salvar=True):
        novo_nodo = Nodo(nova)
        if not self.cabeca:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo
        
        if salvar:
            self.salvar_dados()
        return True

    # remocao por id
    def remover_consulta(self, id_c):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.consulta.codPaciente == id_c:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                self.salvar_dados()
                return True
            anterior = atual
            atual = atual.proximo
        return False

    # busca por nome
    def buscar_por_nome(self, nome):
        resultados = []
        atual = self.cabeca
        nome = nome.lower()
        while atual:
            if nome in atual.consulta.nomePaciente.lower():
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # busca por data
    def buscar_por_data(self, data):
        resultados = []
        atual = self.cabeca
        while atual:
            if atual.consulta.data == data:
                resultados.append(atual.consulta)
            atual = atual.proximo
        return resultados

    # acesso ao primeiro nodo
    def obter_cabeca(self):
        return self.cabeca

    # atualizacao de registro
    def alterar_consulta(self, id_c, n, d, h, m, t):
        atual = self.cabeca
        while atual:
            if atual.consulta.codPaciente == id_c:
                if n: atual.consulta.nomePaciente = n
                if d: atual.consulta.data = d
                if h: atual.consulta.horario = h
                if m: atual.consulta.nomeMedico = m
                if t: atual.consulta.tipoConsulta = t
                self.salvar_dados()
                return True
            atual = atual.proximo
        return False
