from datetime import datetime


def parse_date(date_str: str) -> datetime:
    """Converte uma string de data no formato 'YYYYMMDDHHMMSS[-3:BRT]'
    para um objeto datetime, ignorando qualquer notação de fuso horário."""
    if "[" in date_str and "]" in date_str:
        date_str = date_str.split("[")[0]

    dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")

    return dt
