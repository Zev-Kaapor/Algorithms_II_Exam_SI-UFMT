# Sistema de Gestão de Consultas Médicas – UFMT

Este repositório contém o projeto de **Lista Simplesmente Encadeada**, desenvolvido para a disciplina de **Algoritmos II**.

## 📋 Objetivo deste Guia

Este guia garante que:
- ✅ Ninguém apague o código de outra pessoa
- ✅ O histórico do projeto fique organizado
- ✅ Todo mundo consiga trabalhar sem conflitos

Para isso, utilizaremos um fluxo de trabalho profissional baseado em **Branches** e **Pull Requests (PRs)**.

---

## ⚠️ Regra Fundamental

> **NUNCA programe diretamente na branch `main`.**  
> 
> A `main` é a versão oficial e estável do projeto.  
> Todo trabalho deve ser feito em uma **branch separada**.

---

## 🚀 Guia de Contribuição

Escolha uma das duas opções abaixo:

---

## ⭐ Opção A: GitHub Desktop (Recomendado para Iniciantes)

Essa opção é a mais segura para quem está começando, pois tudo é visual e o risco de erro é menor.

### 🔹 Passo 1 – Clonar o Projeto

**Clonar** significa criar uma cópia completa do projeto no seu computador.

Existem duas formas equivalentes:

#### ✅ Forma A – Pelo GitHub Desktop

1. Abra o **GitHub Desktop**
2. Vá em `File` → `Clone Repository`
3. Procure pelo repositório do projeto
4. Escolha a pasta onde ele será salvo
5. Clique em **Clone**

#### ✅ Forma B – Pelo Site do GitHub

1. Abra o repositório no navegador:  
   ```
   https://github.com/Zev-Lonewolf/Algorithms_II_Exam_SI-UFMT
   ```
2. Clique no botão verde **Code**
3. Selecione **Open with GitHub Desktop**
4. O GitHub Desktop abrirá automaticamente
5. Escolha a pasta onde o projeto será salvo
6. Clique em **Clone**

**Resultado:** Todos os arquivos do projeto são baixados e você pode editá-los no VS Code.

---

### 🔹 Passo 2 – Criar uma Branch

Uma **branch** é sua área de trabalho isolada.

> **Analogia:**
> - `main` = versão oficial do trabalho  
> - `branch` = sua área de trabalho pessoal

#### Como criar:

1. No topo do GitHub Desktop, clique em `Current Branch`
2. Clique em **New Branch**
3. Dê um nome descritivo para a tarefa

#### Exemplos de nomes:

```
feature-atributos-consulta
feature-cadastro-paciente
feature-validacao-horario
```

> **Regra:** Uma branch deve conter apenas **uma tarefa específica**.

---

### 🔹 Passo 3 – Programar

Agora é hora de codar:

1. Abra o projeto no **VS Code**
2. Faça sua implementação
3. Salve os arquivos

> Nenhum comando Git é necessário nesta etapa. Apenas código!

---

### 🔹 Passo 4 – Commit

Um **commit** é um ponto de salvamento do seu trabalho.

#### Como fazer:

1. Volte ao **GitHub Desktop**
2. No canto inferior esquerdo, preencha:
   - **Summary:** Descrição curta do que foi feito  
     *Exemplo:* `Adicionado campo de horário`
3. Clique em **Commit to `<nome-da-branch>`**

> **Importante:** O commit salva apenas no seu computador local.

---

### 🔹 Passo 5 – Push

O **push** envia sua branch para o repositório online.

#### Como fazer:

- Clique em **Publish Branch** ou **Push Origin** no topo

**Resultado:** Seu código agora está no GitHub, mas ainda não faz parte da `main`.

---

### 🔹 Passo 6 – Pull Request

O **Pull Request (PR)** é um pedido para que sua branch seja revisada e integrada à `main`.

#### Como fazer:

1. Clique em **Create Pull Request** no GitHub Desktop
2. O navegador abrirá a página do GitHub
3. Clique novamente em **Create Pull Request**

**Resultado:** 
- O código será revisado pela equipe
- Poderá receber comentários e sugestões
- Só será integrado após aprovação

---

## 💻 Opção B: Terminal (CMD / Git Bash)

Essa opção é mais rápida e amplamente usada no mercado, mas exige atenção aos comandos.

### 🔹 Passo 1 – Clonar o Projeto

```bash
git clone https://github.com/Zev-Lonewolf/Algorithms_II_Exam_SI-UFMT.git
```

### 🔹 Passo 2 – Criar e Entrar na Branch

```bash
git checkout -b feature-nome-da-tarefa
```

### 🔹 Passo 3 – Preparar os Arquivos

```bash
git add .
```

### 🔹 Passo 4 – Commit

```bash
git commit -m "Descrição clara do que foi feito"
```

### 🔹 Passo 5 – Push

```bash
git push origin feature-nome-da-tarefa
```

> Depois disso, abra o **Pull Request** pelo site do GitHub.

---

## 🔄 Ciclo de Continuidade (Após o Merge)

Depois que o Pull Request é aceito, a `main` do seu computador fica desatualizada.

### 🔹 Passo 1 – Voltar para a Main

```bash
git checkout main
```

### 🔹 Passo 2 – Atualizar a Main

```bash
git pull origin main
```

**Isso traz:**
- Seu código já aprovado
- Alterações feitas por outros integrantes

### 🔹 Passo 3 – Criar Nova Branch

Com a `main` atualizada, crie uma nova branch para a próxima tarefa.

> **⚠️ Importante:** Nunca reutilize uma branch antiga!

---

## 📚 Resumo do Fluxo de Trabalho

```
1. Clone o projeto (apenas na primeira vez)
2. Crie uma branch para sua tarefa
3. Programe e salve
4. Faça commit
5. Faça push
6. Abra Pull Request
7. Aguarde revisão e aprovação
8. Após merge, atualize sua main local
9. Repita o processo para novas tarefas
```

---

## 🆘 Precisa de Ajuda?

Em caso de dúvidas ou problemas:
- Entre em contato com a equipe
- Revise este guia novamente
- Consulte a documentação oficial do Git

---

**Bom trabalho! 🚀**
