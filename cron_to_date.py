import sys
from croniter import croniter
from datetime import datetime

def converter_crontab_para_horario(crontab_expression, num_ocorrencias=5):
    # Obtenha o momento exato atual com minutos e segundos zerados
    horario_atual = datetime.now().replace(second=0, microsecond=0)

    cron = croniter(crontab_expression, horario_atual)
    datas_horarios = [cron.get_next(datetime) for _ in range(num_ocorrencias)]
    return datas_horarios

if __name__ == "__main__":
    # Verifique se a expressão Cron foi fornecida como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <expressao_cron>")
        sys.exit(1)

    expressao_cron = sys.argv[1]

    # Exemplo de uso
    ocorrencias = 1
    horarios_convertidos = converter_crontab_para_horario(expressao_cron, ocorrencias)

    #print(f"Próximas {ocorrencias} ocorrências para a expressão Cron '{expressao_cron}' a partir do momento exato atual:")
    for horario in horarios_convertidos:
        print(horario)

