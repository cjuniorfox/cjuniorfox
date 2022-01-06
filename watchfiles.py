#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,time,argparse
from datetime import datetime

class Filetime:
    def __init__(self,path,file):
        self.file = file
        self.path = path
        self.ctime = os.path.getctime(os.path.join(path,file)) if os.path.isfile(os.path.join(path,file)) else None 
    
    def __eq__(self, other):
        return other.file == self.file and other.ctime == self.ctime

    def __hash__(self):
        return hash (self.file) + hash(self.ctime)

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

    def __eq__(self, other):
        return self.path == other.path and self.anterior == other.anterior
    def __hash__(self):
        return hash(self.path) + hash(self.anterior)

def gerarbastao(diferenca,output_dir):
    for f in diferenca:
        if(os.path.isdir(os.path.join(f.path,f.file))):
            add_dirs(os.path.join(f.path,f.file))
        else :
            path = os.path.join(output_dir,f.path)
            if(not os.path.isdir(path)):
                os.makedirs(path)
            fp = open(os.path.join(path,f.file),"w")
            message = "Arquivo " + os.path.join(f.path,f.file) +" " + str(f.ctime) + " criado ou alterado"
            fp.write(message)
            fp.close
            print(message)

def listdir_filetime(path):
    files = []
    try:
        for f in os.listdir(path):
            filetime = Filetime(path,f)
            files.append(filetime)
    except Exception:
        print(path,"Arquivo ou diretorio a ser monitorado não existe mais")
    return files

def add_dirs(path):
    files = listdir_filetime(path)
    for f in files:
        if os.path.isdir(os.path.join(path,f.file)):
            add_dirs(os.path.join(path,f.file))
    monitores.append(Monitoramento(path,files))

#Codigo
monitores=[]
parser = argparse.ArgumentParser(description="Monitora diretorios e gera arquivos de bastão conforme arquivos são recepcionados")
parser.add_argument("directory",nargs='+', help="Diretorios a serem monitorados")
parser.add_argument("--output","-o",help="Diretório de saída",required=True)
args = parser.parse_args()

output_dir = args.output


for paths in args.directory :
    add_dirs(paths)

while True :
    print(" Comecei as", datetime.now())
    for i in range(0,len(monitores)):        
        atual = listdir_filetime(monitores[i].getPath())
        diferenca = list(set(atual) - set(monitores[i].getAnterior()))
        gerarbastao(diferenca,output_dir)
        monitores[i].setAnterior(atual)
    print("Terminei as", datetime.now())
    time.sleep(5)

