import requests
from bs4 import *
import time
import smtplib
import email.message

def enviar_email():

    EMAILS = ['andrewdias2016@gmail.com','arthurnascifar@outlook.com','vivianprodrigues@gmail.com']

    for mail in EMAILS:
        corpo_email = """
        <p>OLÁ,</p>
        <p>TEVE ANDAMENTO NO SEI, CORRE LÁ PARA CONFERIR.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "ANDAMENTO NO SEI"
        msg['From'] = 'andrewdias2016@gmail.com'
        msg['To'] = mail
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {mail}')



print("Procurando andamentos no processo...")
ANDAMENTO = []

req = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

html = req.text
soup = BeautifulSoup(html, "html.parser")
tags_a = soup.findAll("caption")




for tag in tags_a:
    for i in tag:
        try:
            numeros = "".join(char for char in i if char.isdigit())
            ANDAMENTO.append(numeros)
        except:
            pass



valores = []
for val in ANDAMENTO:
    valores.append(int(val))

  
ListaDeProtocoloInicial = valores[0]
ListaDeAndamentoInicial = valores[1]


while True:
    try:
        andamento = []

        req = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.findAll("caption")




        for tag in tags_a:
            for i in tag:
                try:
                    numeros = "".join(char for char in i if char.isdigit())
                    andamento.append(numeros)
                except:
                    pass



        VALORES = []
        for val in ANDAMENTO:
            VALORES.append(int(val))

        
        ListaDeProtocolo = VALORES[0]
        ListaDeAndamento = VALORES[1]

        if ListaDeAndamento != ListaDeAndamentoInicial:
            print("TEVE ANDAMENTO NO PROCESSO")
            enviar_email()
            ListaDeAndamentoInicial = ListaDeAndamento
        if ListaDeProtocolo != ListaDeProtocoloInicial:
            print("TEVE ANDAMENTO NO PROCESSO")
            enviar_email()
            ListaDeProtocoloInicial = ListaDeProtocolo
        
        time.sleep(15)

    except Exception as e:
        print(e)
        pass








