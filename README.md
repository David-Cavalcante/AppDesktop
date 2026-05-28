# 🎵 DaveTickets Pro - Painel Administrativo

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-purple)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%20(Aiven)-blue)

O **DaveTickets Pro** é uma aplicação desktop desenvolvida em Python para o gerenciamento de vendas de ingressos e shows de forma centralizada. O sistema conecta-se a um banco de dados PostgreSQL para recuperar dados em tempo real sobre os últimos shows, bandas contratadas, clientes e o faturamento das vendas.

<img width="948" height="485" alt="image" src="https://github.com/user-attachments/assets/477d037d-84e8-41b6-9a5b-ac55dbfbc8a9" />

---

## 🚀 Funcionalidades

* **Painel de Monitoramento:** Visualização rápida e organizada das últimas vendas de ingressos.
* **Atualização em Tempo Real:** Sincronização automática com o banco de dados a cada 3 segundos, mantendo as informações sempre frescas.
* **Indicador de Status:** Monitoramento visual integrado para indicar se a conexão com o banco de dados está `ONLINE` ou se ocorreu algum `ERRO`.
* **Interface Moderna:** Visual escuro (Dark Mode) customizado utilizando Tkinter e estilos aprimorados do TTK para uma experiência de usuário elegante.

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem principal de desenvolvimento.
* **[Tkinter / TTK](https://docs.python.org/3/library/tkinter.html):** Criação da interface gráfica de usuário (GUI).
* **[PostgreSQL](https://www.postgresql.org/):** Sistema de gerenciamento de banco de dados relacional.
* **[Psycopg2](https://www.psycopg.org/):** Adaptador de banco de dados PostgreSQL para Python.

---

## 📋 Pré-requisitos

Antes de executar a aplicação, você precisará ter instalado em sua máquina:
* Python 3.x
* Banco de dados PostgreSQL configurado.

---

## ⚙️ Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/dave-tickets-pro.git](https://github.com/seu-usuario/dave-tickets-pro.git)
   cd dave-tickets-pro
## Instale as dependências necessárias:

Bash
pip install psycopg2
(Nota: Se tiver problemas na instalação do psycopg2, tente usar pip install psycopg2-binary)

## Configuração do Banco de Dados:
Certifique-se de que a variável DB_CONFIG no código contém as credenciais corretas do seu banco de dados PostgreSQL, apontando para as tabelas equivalentes:

vendas_ingressos

shows

bandas

clientes

Execute a aplicação:

Bash
python nome_do_seu_arquivo.py
🛠️ Estrutura de Dados (Esquema SQL Utilizado)
Para que a aplicação funcione corretamente, o banco de dados deve seguir a seguinte estrutura de relacionamentos para a query de consulta:

bandas: id_banda, nome_banda

shows: id_show, id_banda, local_show, cidade, data_show

clientes: id_cliente, nome_cliente

vendas_ingressos: id_venda, id_show, id_cliente, quantidade, valor_total

## ✒️ Autores
Desenvolvedor: David Cavalcante

## LinkedIn: [LinkedIn](https://www.linkedin.com/in/davidcavalcante)

## Baixe o app e verifique o projeto [projeto original](https://david-cavalcante.github.io/AppDesktop/)
