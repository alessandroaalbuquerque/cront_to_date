from croniter import croniter
from datetime import datetime
import sys

def converter_crontab_para_horario(crontab_expression, num_ocorrencias=5):
    horario_atual = datetime.now().replace(second=0, microsecond=0)

    cron = croniter(crontab_expression, horario_atual)
    datas_horarios = [cron.get_next(datetime) for _ in range(num_ocorrencias)]
    return datas_horarios

if __name__ == "__main__":
    # Defina a expressão Cron como uma variável
    expressao_cron = "*/5 * * * *"

    # Ou, se fornecido como argumento, substitua o valor padrão
    if len(sys.argv) == 2:
        expressao_cron = sys.argv[1]

    ocorrencias = 1
    horarios_convertidos = converter_crontab_para_horario(expressao_cron, ocorrencias)

   # print(f"Próximas {ocorrencias} ocorrências para a expressão Cron '{expressao_cron}' a partir do momento exato atual:")
    for horario in horarios_convertidos:
        hora_sem_dois_pontos = horario.strftime("%H%M%S")
        print(hora_sem_dois_pontos)
