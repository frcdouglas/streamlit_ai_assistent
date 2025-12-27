import pandas as pd
from datetime import datetime

EXCEL_PATH = "horarios_lojas.xlsx"

MAPA_DIAS = {
    0: "segunda",
    1: "terca",
    2: "quarta",
    3: "quinta",
    4: "sexta",
    5: "sabado",
    6: "domingo",
}

def consultar_horario_loja(data: str) -> str:
    try:
        data_ref = datetime.strptime(data, "%Y-%m-%d").date()
    except ValueError:
        return "Data inválida. Use o formato YYYY-MM-DD."

    df_padrao = pd.read_excel(EXCEL_PATH, sheet_name="horarios_padrao")
    df_excecoes = pd.read_excel(EXCEL_PATH, sheet_name="excecoes")

    # ---------- exceções ----------
    excecao = df_excecoes[df_excecoes["data"] == pd.Timestamp(data_ref)]

    if not excecao.empty:
        row = excecao.iloc[0]
        if str(row["abre"]).lower() == "fechado":
            return (
                f"Em {data_ref.strftime('%d/%m/%Y')}, a loja estará fechada"
                f"{' (' + row.get('motivo','') + ')' if row.get('motivo') else ''}."
            )
        return (
            f"Em {data_ref.strftime('%d/%m/%Y')}, a loja funciona "
            f"das {row['abre']} às {row['fecha']}"
            f"{' (' + row.get('motivo','') + ')' if row.get('motivo') else ''}."
        )

    # ---------- horário padrão ----------
    dia_pt = MAPA_DIAS[data_ref.weekday()]

    df_dia = df_padrao[df_padrao["dia_semana"].str.lower() == dia_pt]

    if df_dia.empty:
        return f"Não há horário cadastrado para {dia_pt}."

    row = df_dia.iloc[0]

    if str(row["abre"]).lower() == "fechado":
        return f"Em {dia_pt}, a loja não funciona."

    return (
        f"Em {dia_pt}, a loja funciona "
        f"das {row['abre']} às {row['fecha']}."
    )
