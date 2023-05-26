import mimetypes
import email.message
import smtplib
import pandas as pd
import pathlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Carrega o arquivo de planilha 'Lojas.xlsx' usando a biblioteca pandas
lojas = pd.read_excel(r'Lojas.xlsx')

# Define a meta de faturamento anual
metaFaturamentoAnual = 1675082.50

# Filtra as lojas que atingiram a meta anual de faturamento
lojasBateramMetaAno = lojas.loc[lojas['Faturamento Ano']
                                >= metaFaturamentoAnual]

# Ordena as lojas com base no faturamento anual em ordem decrescente
lojasBateramMetaAno = lojasBateramMetaAno.sort_values(
    by='Faturamento Ano', ascending=False)
display(lojasBateramMetaAno)

# Calcula a porcentagem de lojas que atingiram a meta anual em relação ao total de lojas
porcBateuMetaAno = len(lojasBateramMetaAno) / len(lojas)
print(f'{porcBateuMetaAno * 100}% das lojas bateram a meta do ano.')
lojasBateramMetaAno.to_excel('Lojas que bateram a meta anual.xlsx')

# Define a meta de faturamento diário
metaFaturamentoDia = 3500

# Filtra as lojas que atingiram a meta diária de faturamento
lojasBateramMetaDia = lojas.loc[lojas['Faturamento Dia'] >= metaFaturamentoDia]

# Ordena as lojas com base no faturamento diário em ordem decrescente
lojasBateramMetaDia = lojasBateramMetaDia.sort_values(
    by='Faturamento Dia', ascending=False)
display(lojasBateramMetaDia)

# Calcula a porcentagem de lojas que atingiram a meta diária em relação ao total de lojas
porcBateuMetaDia = len(lojasBateramMetaDia) / len(lojas)
print(f'{porcBateuMetaDia * 100}% das lojas bateram a meta do dia.')
lojasBateramMetaDia.to_excel('Lojas que bateram a meta diaria.xlsx')

# Define os caminhos dos arquivos anexos
attachmentPathAno = pathlib.Path.cwd() / 'Lojas que bateram a meta anual.xlsx'
attachmentPathDia = pathlib.Path.cwd() / 'Lojas que bateram a meta diaria.xlsx'

# Cria o corpo do e-mail
body = """
"""

# Cria uma instância de MIMEMultipart para compor a mensagem de e-mail
msg = MIMEMultipart()
msg['From'] = '***@***.***'
msg['To'] = '***@***.***'
msg['Subject'] = 'Assunto'
password = '***'

# Adiciona o corpo do e-mail à mensagem
msg.attach(MIMEText(body, 'plain'))

# Configura o nome dos arquivos anexos
filenameAno = 'Lojas que bateram a meta anual'
filenameDia = 'Lojas que bateram a meta diaria'

# Abre o arquivo do dia para anexar ao e-mail
attachmentDia = open(attachmentPathDia, 'rb')

# Cria uma instância de MIMEBase para o arquivo do dia
attachmentPackage = MIMEBase('application', 'octet-stream')
attachmentPackage.set_payload((attachmentDia).read())
encoders.encode_base64(attachmentPackage)
attachmentPackage.add_header(
    'Content-Disposition', "attachment; filename = " + filenameDia)
msg.attach(attachmentPackage)

# Abre o arquivo do ano para anexar ao e-mail
attachmentAno = open(attachmentPathAno, 'rb')

# Cria uma instância de MIMEBase para o arquivo do ano
attachmentPackage = MIMEBase('application', 'octet-stream')
attachmentPackage.set_payload((attachmentAno).read())
encoders.encode_base64(attachmentPackage)
attachmentPackage.add_header(
    'Content-Disposition', "attachment; filename = " + filenameAno)
msg.attach(attachmentPackage)

# Converte a mensagem em formato string
text = msg.as_string()

# Conecta ao servidor SMTP do Gmail
print("Conectando com o servidor")
print()
TIEServer = smtplib.SMTP("smtp.gmail.com", 587)
TIEServer.starttls()
TIEServer.login(msg['From'], password)
print("Conectado com o servidor")

# Envia o e-mail
TIEServer.sendmail(msg['From'], msg['To'], text)
print(f"Email enviado para {msg['To']}")
print()

# Encerra a conexão com o servidor SMTP
TIEServer.quit()
