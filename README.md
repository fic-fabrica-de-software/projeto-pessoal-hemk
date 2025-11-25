2# Monitr: Plataforma de Gerenciamento de Usuários e Tarefas

## Descrição do Projeto

O **Monitr** é uma plataforma ambiciosa em desenvolvimento, projetada para ser uma solução completa de **gerenciamento de usuários e atribuição de tarefas**, visando otimizar o fluxo de trabalho e fornecer uma visão clara do progresso de projetos.

### Visão e Problema Resolvido

A visão final do Monitr é oferecer aos usuários a capacidade de:

*   **Gerenciar Usuários:** Criar, editar e excluir perfis de usuários.
*   **Atribuir e Acompanhar Tarefas:** Distribuir tarefas e monitorar seu status em tempo real.
*   **Dashboards Interativos:** Visualizar o progresso das tarefas e a porcentagem de conclusão através de painéis dinâmicos.

A motivação é resolver o problema da falta de visibilidade e controle no acompanhamento de tarefas, fornecendo uma ferramenta centralizada e intuitiva para a gestão de equipes e projetos.

### Fase Atual: O Embrião do Monitr

O código presente neste repositório representa a **fase inicial (MVP - Minimum Viable Product)** do Monitr, focada na funcionalidade essencial de **CRUD (Create, Read, Update, Delete) de Usuários**.

Esta etapa serve como a fundação para a camada de autenticação e gerenciamento de perfis que será expandida para suportar a atribuição e o monitoramento de tarefas.

## Tecnologias Utilizadas

O projeto está sendo construído com foco em escalabilidade e robustez, utilizando as seguintes tecnologias na fase atual:

| Categoria | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Backend** | **Python** | Linguagem de programação principal. |
| **Framework** | **Django 5.2.7** | Framework web robusto para o desenvolvimento do backend e da lógica de negócios. |
| **Banco de Dados** | **SQLite** | Banco de dados padrão do Django, ideal para o desenvolvimento inicial e testes. |
| **Frontend** | **HTML/CSS** | Utilizado para a estrutura e estilização das páginas de CRUD (será expandido com frameworks modernos). |

## Estrutura do Repositório

O código da aplicação de CRUD de usuários está contido no diretório `crud_django`.

```
projeto-pessoal-hemk/
├── app/                # Aplicação Django (Modelos, Views, Templates)
├── config/             # Configurações do Projeto (settings, urls)
├── db.sqlite3          # Banco de Dados SQLite (Ignorado pelo .gitignore)
└── manage.py           # Utilitário de Linha de Comando do Django

```

## Instruções de Uso (Fase Inicial)

Siga os passos abaixo para configurar e rodar a fase inicial do Monitr (CRUD de Usuários) localmente.

### Pré-requisitos

Você precisará ter o **Python** e o gerenciador de pacotes **pip** instalados em sua máquina.

### 1. Clonar o Repositório

Abra o terminal e clone o repositório:

```bash
git clone https://github.com/fic-fabrica-de-software/projeto-pessoal-hemk.git
cd projeto-pessoal-hemk/crud_django
```

### 2. Criar e Ativar o Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências:

```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ativar o ambiente virtual (Windows)
# venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale o framework Django:

```bash
pip install django
```

### 4. Aplicar as Migrações

Crie a tabela de usuários no banco de dados:

```bash
python manage.py makemigrations app
python manage.py migrate
```

### 5. Rodar o Servidor

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

### 6. Acessar a Aplicação

Com o servidor rodando, acesse a aplicação no seu navegador:

```
http://127.0.0.1:8000/
```

Você será direcionado para a página de login (`/login`). Navegue para `/cadastro` para criar seu primeiro usuário e testar as funcionalidades de CRUD.

## Próximos Passos (Roadmap do Monitr)

O desenvolvimento do Monitr seguirá as seguintes etapas:

1.  **Refatoração do Frontend:** Implementação de um framework moderno (ex: React/Vue.js) para criar uma interface de usuário mais rica e interativa.
2.  **Módulo de Tarefas:** Criação do modelo de dados para tarefas e implementação das funcionalidades de atribuição e acompanhamento.
3.  **Dashboards Interativos:** Desenvolvimento de visualizações de dados para exibir a porcentagem de conclusão e métricas de produtividade.
4.  **Autenticação Avançada:** Implementação de recursos de segurança e permissões de usuário mais robustos.

## Link de Deploy

Atualmente, o projeto está em fase de desenvolvimento local. O link de deploy será adicionado aqui quando a primeira versão estável for hospedada.


