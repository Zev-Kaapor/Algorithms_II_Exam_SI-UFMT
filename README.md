# Sistema de Gestão de Consultas Médicas – UFMT

Este repositório contém o projeto de **Lista Simplesmente Encadeada**, desenvolvido para a disciplina de **Algoritmos II**.

O objetivo deste guia é garantir que:
- ninguém apague o código de outra pessoa,
- o histórico do projeto fique organizado,
- todo mundo consiga trabalhar sem conflitos.

Para isso, utilizaremos um fluxo de trabalho profissional baseado em **Branches** e **Pull Requests (PRs)**.

---

## 🚀 Guia de Contribuição (Extremamente Detalhado)

Antes de tudo, entenda uma regra fundamental:

> **NUNCA programe diretamente na branch `main`.**  
> A `main` é a versão oficial e estável do projeto.  
> Todo trabalho deve ser feito em uma **branch separada**.

---

## ⭐ Opção A: GitHub Desktop (Recomendado para iniciantes)

Essa opção é a mais segura para quem está começando, pois tudo é visual e o risco de erro é menor.

---

### 🔹 Passo 1 – Clonar o projeto (baixar para o seu computador)

Clonar significa criar uma **cópia completa do projeto** no seu computador.

Existem **duas formas equivalentes** de fazer isso usando o GitHub Desktop.

---

#### ✅ Forma A – Pelo próprio GitHub Desktop

1. Abra o **GitHub Desktop**
2. Vá em `File` → `Clone Repository`
3. Procure pelo repositório do projeto
4. Escolha a pasta onde ele será salvo
5. Clique em **Clone**

---

#### ✅ Forma B – Diretamente pelo site do GitHub (mais comum)

1. Abra o repositório no navegador:  
   https://github.com/Zev-Lonewolf/Algorithms_II_Exam_SI-UFMT
2. Clique no botão verde **Code**
3. Selecione a opção **Open with GitHub Desktop**
4. O GitHub Desktop abrirá automaticamente
5. Escolha a pasta onde o projeto será salvo
6. Clique em **Clone**

---

#### O que acontece em ambas as formas:
- Todos os arquivos do projeto são baixados
- Você passa a ter uma cópia idêntica do repositório
- A partir daqui, o código pode ser editado normalmente no VS Code

---

### 🔹 Passo 2 – Criar uma branch (sua área de trabalho)

Uma **branch** é uma linha de desenvolvimento isolada.

> Pense assim:
> - `main` = versão oficial do trabalho  
> - `branch` = sua área de trabalho pessoal

#### Como criar:
1. No topo do GitHub Desktop, clique em `Current Branch`
2. Clique em **New Branch**
3. Dê um nome descritivo para a tarefa

#### Exemplos de nomes:
- `feature-atributos-consulta`
- `feature-cadastro-paciente`
- `feature-validacao-horario`

> **Regra:** uma branch deve conter apenas uma tarefa.

---

### 🔹 Passo 3 – Programar normalmente

Agora:
- Abra o projeto no **VS Code**
- Faça sua implementação
- Salve os arquivos

Nenhum comando Git é usado aqui. Apenas código.

---

### 🔹 Passo 4 – Commit (registrar o que foi feito)

Um **commit** é um ponto de salvamento do seu trabalho.

#### Como fazer:
1. Volte ao **GitHub Desktop**
2. No canto inferior esquerdo, preencha:
   - **Summary:** descrição curta do que foi feito  
     Exemplo: `Adicionado campo de horário`
3. Clique em **Commit to <nome-da-branch>**

#### Importante:
- O commit salva apenas no seu computador
- Nada ainda foi enviado para o GitHub

---

### 🔹 Passo 5 – Push (enviar para o GitHub)

O **push** envia sua branch para o repositório online.

#### Como fazer:
- Clique em **Publish Branch** ou **Push Origin** no topo

Após isso:
- Seu código estará no GitHub
- Ainda não fará parte da `main`

---

### 🔹 Passo 6 – Pull Request (pedido de aprovação)

O **Pull Request** serve para pedir que sua branch seja analisada e integrada à `main`.

#### Como fazer:
1. Clique em **Create Pull Request**
2. O navegador abrirá o GitHub
3. Clique novamente em **Create Pull Request**

Agora o código:
- será revisado
- poderá receber comentários
- só será integrado após aprovação

---

---

### 💻 Opção B: Terminal (CMD / PowerShell / Bash)

Se preferir usar comandos, siga esta ordem lógica:

**1. Preparação Inicial (Só na primeira vez)** `git clone https://github.com/Zev-Lonewolf/Algorithms_II_Exam_SI-UFMT.git`

**2. Criar e entrar na branch** `git checkout -b feature-nome-da-tarefa`  
- *O comando `checkout` muda de branch, e o `-b` cria essa branch nova e já te coloca dentro dela.*

**3. Preparar os arquivos** `git add .`  
- *O ponto `.` diz ao Git para separar todos os arquivos que você alterou para o próximo salvamento.*

**4. Commit (Salvar localmente)** `git commit -m "Descrição clara do que foi feito"`  
- *Isso registra suas mudanças com uma mensagem explicativa no banco de dados local.*

**5. Push (Enviar para a nuvem)** `git push origin feature-nome-da-tarefa`  
- *Isso "empurra" o seu trabalho para o GitHub para que todos vejam.*

**6. Abrir o PR** Após o push, entre no site do GitHub e clique no botão amarelo `Compare & pull request`.

---

### 🔄 Ciclo de Continuidade (Após o merge ser aceito)

Depois que o seu Pull Request é aceito por mim, o código vai para a `main`. Nesse momento, a `main` do seu computador fica desatualizada em relação ao servidor.

**Passo 1 – Voltar para a main** `git checkout main`  
- *Sai da sua branch de tarefa e volta para o tronco principal.*

**Passo 2 – Atualizar a main local** `git pull origin main`  
- *Isso traz para o seu PC: o seu código já aprovado e as alterações feitas por outros integrantes.*

**Passo 3 – Criar nova branch** Com a `main` atualizada, você está pronto para a próxima tarefa. Repita o processo criando uma branch nova.  
- **Atenção:** Nunca reutilize uma branch antiga que já teve o PR aceito.

---

## 💡 Dicas Importantes
* **Comentários:** Mantenham os comentários minimalistas e diretamente acima do bloco de código.
* **Sem numeração:** Não use "1. faz isso", "2. faz aquilo" nos comentários.
* **Sincronia:** Sempre dê um `git pull` antes de começar qualquer tarefa nova.
