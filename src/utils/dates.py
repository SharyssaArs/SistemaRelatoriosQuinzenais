from datetime import datetime, timedelta

#A função de criação das datas de envio de relatorio vao funcionar como uma lista,
#a primeira data é a data inicial, e por ela a proxima data sera gerada,
#e assim faremos ate que a fila seja preenchida com 4 espaços,
#quanto houver a comparação e ela for verdadeira, essa data sera excluida e a proxima data entrara na variavel "proximo_envio",
#quando houver um espaço no fnal da fila, a proxima data sera gerada de acordo com a ultima data presente na fila

#Data inicial
DATA_INICIAL = datetime(2026, 2, 18)
print("data inicial:", DATA_INICIAL)

#Proxima data, loop ainda em construção, mas já tem a lógica de adicionar 15 dias
PROXIMA_DATA = DATA_INICIAL + timedelta(days=15)
print("próxima data:", PROXIMA_DATA)

#Data de hoje
hoje = datetime.now()
print("hoje:", hoje)

#Função de verificação (Today = data quinzenal)
if hoje.date() == PROXIMA_DATA.date():
    print("Hoje é dia de enviar o relatório!")
else:
    print("Hoje não é dia de enviar o relatório.")

#Função de geração da fila de datas quinzenais
#Gera uma lista de datas e se renova a cada 15 dias
def gerar_datas(data_inicial_str, qntd_datas=6):
    datas_quinzenais = []
    data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
    for i in range(qntd_datas):
        proxima_data = data_inicial + timedelta(days=15*i)

