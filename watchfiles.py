#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,time,argparse
from datetime import datetime

class Monitoramento:
    def __init__(self, path, anterior):
        self.path = path
        self.anterior = anterior
    def getPath(self):
        return self.path
    def getAnterior(self):
        return self.anterior
    def setAnterior(self,anterior):
        self.anterior=anterior

parser = argparse.ArgumentParser(description="Monitora diretorios e gera arquivos de bastão conforme arquivos são recepcionados")
parser.add_argument("directory",nargs='+', help="Diretorios a serem monitorados")
args = parser.parse_args()

def gerarbastao(diferenca):
    for f in diferenca:
        print("Arquivo",f,"criado ou alterado")

monitores=[]

for dir in args.directory :
    monitores.append(Monitoramento(dir,os.listdir(dir)))

while True :
    for i in range(0,len(monitores)):
        print(monitores[i].getPath())
        print("comecei a olhar as", datetime.now())
        atual = os.listdir(monitores[i].getPath())
        diferenca = list(set(atual) - set(monitores[i].getAnterior()))
        gerarbastao(diferenca)
        monitores[i].setAnterior(atual)
        print("ja terminei. Vo pro proximo.",datetime.now())
    time.sleep(5)

