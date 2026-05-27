# 🎵 DaveTickets Pro - Painel Administrativo

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
   import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2


def carregar_vendas():

    try:

        tabela.delete(*tabela.get_children())

        conexao = psycopg2.connect(**DB_CONFIG)

        conexao.autocommit = True

        cursor = conexao.cursor()

        query = """
            SELECT
                v.id_venda,
                b.nome_banda,
                s.local_show,
                s.cidade,
                c.nome_cliente,
                v.quantidade,
                v.valor_total,
                s.data_show

            FROM vendas_ingressos v

            INNER JOIN shows s
                ON v.id_show = s.id_show

            INNER JOIN bandas b
                ON s.id_banda = b.id_banda

            INNER JOIN clientes c
                ON v.id_cliente = c.id_cliente

            ORDER BY v.id_venda DESC;
        """

        cursor.execute(query)

        vendas = cursor.fetchall()

        for venda in vendas:

            tabela.insert(
                "",
                tk.END,
                values=(
                    venda[0],
                    venda[1],
                    venda[2],
                    venda[3],
                    venda[4],
                    venda[5],
                    f"R$ {venda[6]:,.2f}",
                    venda[7].strftime("%d/%m/%Y")
                )
            )

        cursor.close()
        conexao.close()

        status_label.config(
            text="● ONLINE",
            fg="#00ff88"
        )

    except Exception as erro:

        print(erro)

        status_label.config(
            text="● ERRO",
            fg="#ff1744"
        )

    janela.after(3000, carregar_vendas)

janela = tk.Tk()

janela.title("DaveTickets Pro")
janela.geometry("1450x780")
janela.configure(bg="#0b1120")


style = ttk.Style()
style.theme_use("clam")


style.configure(
    "Treeview",
    background="#111827",
    foreground="white",
    rowheight=26,
    fieldbackground="#111827",
    borderwidth=0,
    font=("Segoe UI", 10)
)

style.map(
    "Treeview",
    background=[("selected", "#7c3aed")]
)

style.configure(
    "Treeview.Heading",
    background="#1f2937",
    foreground="white",
    relief="flat",
    font=("Segoe UI", 10, "bold")
)


style.configure(
    "Vertical.TScrollbar",
    background="#111827",
    troughcolor="#0b1120",
    bordercolor="#0b1120",
    arrowcolor="white"
)


sidebar = tk.Frame(
    janela,
    bg="#111827",
    width=230
)

sidebar.pack(side=tk.LEFT, fill=tk.Y)


logo = tk.Label(
    sidebar,
    text="🎵 DAVE\nTICKETS",
    bg="#111827",
    fg="white",
    justify="left",
    font=("Segoe UI", 24, "bold")
)

logo.pack(
    padx=25,
    pady=(30, 5),
    anchor="w"
)

sublogo = tk.Label(
    sidebar,
    text="Painel Administrativo",
    bg="#111827",
    fg="#94a3b8",
    font=("Segoe UI", 10)
)

sublogo.pack(
    padx=27,
    anchor="w"
)


btn_refresh = tk.Button(
    sidebar,
    text="⟳ Atualizar",
    command=carregar_vendas,
    bg="#7c3aed",
    fg="white",
    activebackground="#6d28d9",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=10,
    cursor="hand2",
    font=("Segoe UI", 10, "bold")
)

btn_refresh.pack(
    padx=25,
    pady=35,
    fill=tk.X
)


status_label = tk.Label(
    sidebar,
    text="● CONECTANDO...",
    bg="#111827",
    fg="#facc15",
    font=("Segoe UI", 10, "bold")
)

status_label.pack(
    padx=25,
    anchor="w"
)


main = tk.Frame(
    janela,
    bg="#0b1120"
)

main.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


topo = tk.Frame(
    main,
    bg="#0b1120",
    height=70
)

topo.pack(fill=tk.X)

titulo = tk.Label(
    topo,
    text="Concert's Here",
    bg="#0b1120",
    fg="white",
    font=("Segoe UI", 24, "bold")
)

titulo.pack(
    anchor="w",
    padx=25,
    pady=(10, 0)
)

subtitulo = tk.Label(
    topo,
    text="Controle completo de ingressos e shows",
    bg="#0b1120",
    fg="#94a3b8",
    font=("Segoe UI", 10)
)

subtitulo.pack(
    anchor="w",
    padx=27
)


card = tk.Frame(
    main,
    bg="#111827"
)

card.pack(
    fill=tk.BOTH,
    expand=True,
    padx=20,
    pady=15
)

card_title = tk.Label(
    card,
    text="Últimas Vendas",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 13, "bold")
)

card_title.pack(
    anchor="w",
    padx=10,
    pady=10
)

frame_tabela = tk.Frame(
    card,
    bg="#111827"
)

frame_tabela.pack(
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=(0, 10)
)


colunas = (
    "ID",
    "Banda",
    "Local",
    "Cidade",
    "Cliente",
    "Qtd",
    "Valor",
    "Data"
)

tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings"
)

larguras = {
    "ID": 50,
    "Banda": 170,
    "Local": 190,
    "Cidade": 130,
    "Cliente": 170,
    "Qtd": 60,
    "Valor": 100,
    "Data": 90
}

for col in colunas:

    tabela.heading(col, text=col)

    tabela.column(
        col,
        width=larguras[col],
        anchor=tk.CENTER,
        stretch=True
    )


scroll_y = ttk.Scrollbar(
    frame_tabela,
    orient="vertical",
    command=tabela.yview
)

tabela.configure(
    yscrollcommand=scroll_y.set
)

scroll_y.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

tabela.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


janela.after(1000, carregar_vendas)

janela.mainloop()
   
Instale as dependências necessárias:

Bash
pip install psycopg2
(Nota: Se tiver problemas na instalação do psycopg2, tente usar pip install psycopg2-binary)

Configuração do Banco de Dados:
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

✒️ Autores
Desenvolvedor: David Cavalcante

LinkedIn: [LinkedIn](https://www.linkedin.com/in/davidcavalcante)


---

