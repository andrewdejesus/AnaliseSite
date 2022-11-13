import requests
from bs4 import *
import time
import smtplib
import email.message
from movi import *

def enviar_email_prot():

    EMAILS = ['andrewdias2016@gmail.com']

    for mail in EMAILS:
        corpo_email = f"""
        <p>OLÁ,</p>
        <p>A última movimentação foi: {movi_protocolo(ListaDeProtocolo)}.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "ANDAMENTO NO SEI"
        msg['From'] = 'andrewdias2016@gmail.com'
        msg['To'] = mail
        password = 'senha' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {mail}')

def enviar_email_and():

    EMAILS = ['andrewdias2016@gmail.com']

    for mail in EMAILS:
        corpo_email = f"""
        <p>OLÁ,</p>
        <p>A última movimentação foi: {movi_andamento(ListaDeAndamento)}.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "ANDAMENTO NO SEI"
        msg['From'] = 'andrewdias2016@gmail.com'
        msg['To'] = mail
        password = 'sasdxkbawhllrjec' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {mail}')




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

print(f"Andamento: {ListaDeProtocoloInicial}")
print(f"Protocolo: {ListaDeAndamentoInicial}" )
print("Procurando andamentos no processo...")

while True:
    try:
        andamento = []
        TEOR = []
        reqs = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

        htmls = reqs.text
        soups = BeautifulSoup(htmls, "html.parser")
        tags = soups.findAll("caption")


        for t in tags:
            for i in t:
                try:
                    numero = "".join(char for char in i if char.isdigit())
                    andamento.append(numero)
                except:
                    pass



        VALORES = []
        for val in andamento:
            VALORES.append(int(val))

            
        ListaDeProtocolo = VALORES[0]
        ListaDeAndamento = VALORES[1]

        if ListaDeAndamento != ListaDeAndamentoInicial:
            ListaDeAndamentoInicial = ListaDeAndamento
            enviar_email_and()
            print("TEVE ANDAMENTO NO PROCESSO")
            print(f"Andamento Atual: {ListaDeProtocolo}")
            print(f"Protocolo Atual: {ListaDeAndamento}")
            print("Procurando andamentos no processo...")

        if ListaDeProtocolo != ListaDeProtocoloInicial:
            ListaDeProtocoloInicial = ListaDeProtocolo
            enviar_email_prot()
            print("TEVE ANDAMENTO NO PROCESSO")
            print(f"Andamento Atual: {ListaDeProtocolo}")
            print(f"Protocolo Atual: {ListaDeAndamento}")
            print("Procurando andamentos no processo...")
            
            
            
        time.sleep(20)

    except Exception as e:
        print(e)
        pass







