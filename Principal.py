# Participantes: ALISON RODRIGUES PASTANA (202311316003), ARTUR FERREIRA SALES (202511316008), GLEIDSON GONZAGA DA SILVA (202511316022), HALLAN DIAS FERNANDES (202111316013), LEONARDO VINICIUS XAVIER NEVES (202511316034)
# Algoritmos II - NELCILENO VIRGÍLIO DE SOUZA ARAÚJO

import os
import datetime
from Modelos import Consulta
from Lista_encadeada import ListaConsultas

# utilitarios de interface
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")

# validacao de nome
def ler_nome(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor and all(c.isalpha() or c.isspace() for c in valor):
            return valor.title()
        print("Erro: Use apenas letras.")

# validacao de data
def ler_data(mensagem, verificar_futuro=True):
    while True:
        valor = input(mensagem).strip()
        try:
            dt_obj = datetime.datetime.strptime(valor, "%d/%m/%Y")
            if verificar_futuro and dt_obj.date() < datetime.date.today():
                print("Erro: A data já passou.")
                continue
            return valor
        except:
            print("Erro: Use o formato DD/MM/AAAA.")

# validacao de horario
def ler_horario(mensagem, data_escolhida, lista, id_ignorar=None):
    while True:
        valor = input(mensagem).strip()
        try:
            datetime.datetime.strptime(valor, "%H:%M")
            conflito = lista.verificar_conflito_imediato(data_escolhida, valor)
            if conflito and conflito.codPaciente != id_ignorar:
                sugestao = (conflito.obter_datetime() + datetime.timedelta(minutes=30)).strftime("%H:%M")
                print(f"Erro: Conflito com {conflito.nomePaciente} às {conflito.horario}.")
                print(f"Sugestão: A partir das {sugestao}.")
                continue
            return valor
        except:
            print("Erro: Use o formato HH:MM.")

# validacao de tipo
def ler_tipo(mensagem):
    while True:
        valor = input(mensagem).strip().capitalize()
        if valor in ["Conveniado", "Particular"]:
            return valor
        print("Erro: Escolha 'Conveniado' ou 'Particular'.")

# fluxo principal
def menu():
    lista = ListaConsultas()
    
    while True:
        limpar_tela()
        print("=== SISTEMA DE AGENDAMENTO MÉDICO ===")
        print("1. Agendar\n2. Buscar Paciente\n3. Buscar Data\n4. Remover\n5. Alterar\n6. Listar\n0. Sair")
        op = input("\nOpção: ")

        if op == "1":
            print("\n--- NOVO AGENDAMENTO ---")
            nome = ler_nome("Paciente: ")
            tag = lista.gerar_tag_nome(nome)
            n_completo = f"{nome} #{tag}"
            id_vago = lista.gerar_proximo_id()
            
            d = ler_data("Data (DD/MM/AAAA): ")
            h = ler_horario("Horário (HH:MM): ", d, lista)
            m = ler_nome("Médico: ")
            t = ler_tipo("Tipo (Conveniado/Particular): ")
            
            if lista.adicionar_consulta(Consulta(id_vago, n_completo, d, h, m, t)):
                print(f"\nSucesso! ID: {id_vago:03d} | Tag: #{tag}")
            pausar()

        elif op == "2":
            res = lista.buscar_por_nome(input("Nome: "))
            for c in res: print(c)
            if not res: print("Nenhum registro.")
            pausar()

        elif op == "3":
            res = lista.buscar_por_data(ler_data("Data: ", False))
            for c in res: print(c)
            if not res: print("Sem consultas.")
            pausar()

        elif op == "4":
            try:
                if lista.remover_consulta(int(input("ID: "))):
                    print("\nRemovido!")
                else: print("\nNão encontrado.")
            except: print("\nEntrada inválida.")
            pausar()

        elif op == "5":
            try:
                id_c = int(input("ID para alterar: "))
                nodo = lista.obter_cabeca()
                atual = next((n.consulta for n in iter(lambda: nodo, None) if n.consulta.codPaciente == id_c), None)
                
                if not atual:
                    print("ID não localizado."); pausar(); continue

                print(f"\n--- EDITANDO: {atual.nomePaciente} ---")
                novo_n = input("Novo nome (Enter p/ manter): ").strip()
                if novo_n:
                    tag = lista.gerar_tag_nome(novo_n)
                    novo_n = f"{novo_n.title()} #{tag}"

                novo_d = input("Nova data (Enter p/ manter): ").strip() or None
                novo_h = input("Novo horário (Enter p/ manter): ").strip() or None
                if novo_h:
                    novo_h = ler_horario("Confirme o horário: ", novo_d or atual.data, lista, id_c)

                novo_m = input("Novo médico (Enter p/ manter): ").strip() or None
                novo_t = input("Novo tipo (Enter p/ manter): ").strip().capitalize() or None

                if lista.alterar_consulta(id_c, novo_n, novo_d, novo_h, novo_m, novo_t):
                    print("\nAtualizado!")
            except: print("\nErro na operação.")
            pausar()

        elif op == "6":
            print("\n--- RELATÓRIO GERAL ---")
            nodo = lista.obter_cabeca()
            if not nodo: print("Lista vazia.")
            while nodo:
                print(nodo.consulta)
                nodo = nodo.proximo
            pausar()

        elif op == "0": break

if __name__ == "__main__":
    menu()
