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