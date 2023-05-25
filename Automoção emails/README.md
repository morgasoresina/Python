# Automoção de Emails

Este é um código Python que utiliza as bibliotecas pandas, pathlib, smtplib e openpyxl para realizar uma análise de faturamento diário de lojas e enviar um e-mail com um relatório das lojas que atingiram a meta estabelecida.

O código lê os dados de uma planilha de lojas, filtra aquelas que alcançaram a meta de faturamento diário especificada e gera um arquivo Excel com as informações dessas lojas. Em seguida, anexa o arquivo ao e-mail e o envia para um destinatário específico.

Para utilizar este código, é necessário instalar as dependências mencionadas acima e fornecer um arquivo de planilha com os dados das lojas. Além disso, é preciso configurar as informações do servidor SMTP e as credenciais de e-mail do remetente.

Este código é útil para automatizar a análise e o envio de relatórios por e-mail, permitindo monitorar o desempenho diário das lojas de forma eficiente. Ele pode ser adaptado para atender a diferentes metas e critérios de filtragem, conforme necessário.
