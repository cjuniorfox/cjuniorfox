#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,time,argparse
from datetime import datetime

class Filetime:
    def __init__(self,path,file):
        self.file = file
        self.ctime = os.path.getctime(os.path.join(path,file))
    
    def __eq__(self, other):
        return other.file == self.file and other.ctime == self.ctime

    def __hash__(self):
        return int(str(hash (self.file)) + str(hash(self.ctime)))

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
        print("Arquivo",f.file,f.ctime,"criado ou alterado")

monitores=[]

def listdir(path):
    return  os.listdir(path)

def listdir2(path):
    files = []
    for f in listdir(path):
        files.append(Filetime(path,f))
    return files

def add_dirs(path):
    files = listdir2(path)
    for f in files:
        if os.path.isdir(os.path.join(path,f.file)):
            add_dirs(os.path.join(path,f.file))
    monitores.append(Monitoramento(path,files))

for paths in args.directory :
    add_dirs(paths)

while True :
    print(" Eu comecei as", datetime.now())
    for i in range(0,len(monitores)):        
        atual = listdir2(monitores[i].getPath())
        diferenca = list(set(atual) - set(monitores[i].getAnterior()))
        gerarbastao(diferenca)
        monitores[i].setAnterior(atual)
    print("ja terminei as",datetime.now())
    time.sleep(5)

