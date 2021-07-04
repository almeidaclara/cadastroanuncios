import mysql.connector
from datetime import datetime


def diff_days(date1, date2):
    fmt = '%Y-%m-%d'
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return str((d2 - d1).days)


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='anuncios',
    charset='utf8')
cursor = connection.cursor()

print('SISTEMA DE CADASTRO DE ANUNCIOS')
print('-'*30)
print('{:>15}'.format('MENU '))
print('[1] Para inserir novos dados')
print('[2] Para SAIR')
while True:
    print('-'*30)
    escolha = int(input('Digite o código desejado '))
    if escolha == 1:
        nome = input('Nome do anúncio: ')
        cliente = input('Cliente: ')
        dinicio = input('Data início (AAAA-MM-DD): ')
        dtermino = input('Data término (AAAA-MM-DD): ')
        investdia = float(input('Investimento por dia: R$'))

        qtdias = int(diff_days(dinicio, dtermino))

        visuOrig = investdia * 30  # codigo da calculadora.py adaptado
        totvisuNova = totcomp = totclique = 0
        for c in range(3):
            if c == 0:
                clique = visuOrig * 12 / 100  # calculando o valor de cliques na 1a iteração (a partir de visuOrig)
                totclique += clique  # armazenando o valor de clique da 1 iteração em totclique
            comp = clique * 3 / 20
            visu = comp * 40
            clique = visu * 12 / 100

            totvisuNova += visu  # total de visualizações novas DIA
            totcomp += comp  # total de compartilhamentos DIA
            totclique += clique  # total de cliques DIA

            visualizacoes = totvisuNova +visuOrig

            investot = round(investdia * qtdias)
            qtvisu = round(qtdias * visualizacoes)
            qtcomp = round(qtdias * totcomp)
            qtclique = round(qtdias * totclique)

        add_anuncios = ("INSERT INTO cad_anuncios"
                        "(nome, cliente, data_inicio, data_fim, invest_dia, qt_dias, invest_tot, qt_visu, qt_clique, qt_comp)"
                        "VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, cliente, dinicio, dtermino, investdia, qtdias, investot, qtvisu, qtclique, qtcomp))

        cursor.execute(add_anuncios)
        connection.commit()

    elif escolha == 2:
        break

sql = "SELECT id, cliente, qt_dias, invest_tot, qt_visu, qt_clique, qt_comp FROM cad_anuncios ORDER BY qt_dias, cliente"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

print('-'*100)
print('{:>50}'.format('RELATÓRIO '))
print('[{:^2}] [{:^7}] [{:^6}] [{:^13}] [{:^14}] [{:^8}] [{:^18}] '.format('ID', 'NOME', 'TEMPO', 'INVESTIMENTO', 'VISUALIZAÇÕES', 'CLIQUES', 'COMPARTILHAMENTOS'))
for result in results:
    print(result)
print('-'*100)