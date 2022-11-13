import requests
from bs4 import *
import re

def movi_protocolo(ListaDeProtocolo):
    try:
        movimentacao = []
        andamento = []
        TEOR = []
        reqs = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

        htmls = reqs.text
        soups = BeautifulSoup(htmls, "html.parser")
        for tag in soups.find_all(re.compile("^tr")):

            TEOR.append(tag)
        
        del TEOR[0:5]

        for i in TEOR[ListaDeProtocolo]:
            andamento.append(i)
        
        a = str(andamento[2])
        for i in a.split():
            movimentacao.append(i)
        
        return movimentacao[1]
        

    except Exception as e:
        print(e)
        pass

def movi_andamento(ListaDeAndamento):
    try:
        movimentacao = []
        andamento = []
        TEOR = []
        reqs = requests.get("https://www10.tjrj.jus.br/sei/modulos/pesquisa/md_pesq_processo_exibir.php?LyFApQuxweZlHTLXUD6u1y7tX4d3oMBqI068jRzh-jmD6lRsMfC_MSxrkq7qMXzIfz0u57sxCObxfxX7102s0OPclxe8lW1cZe2v7-DLgdDvkB0gDy6lhfwnU-GWM4wV")

        htmls = reqs.text
        soups = BeautifulSoup(htmls, "html.parser")
        for tag in soups.find_all(re.compile("^tr")):

            TEOR.append(tag)
        
        TEOR.reverse()

        
       

        for i in TEOR[(ListaDeAndamento - 1)]:
            andamento.append(i)
        
        for i in andamento:
            movimentacao.append(i)
        
        return movimentacao[3],movimentacao[5]
        

        
        
        

    except Exception as e:
        print(e)
        pass

