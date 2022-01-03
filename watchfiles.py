#!/usr/bin/python
import os,time

def gerarbastao(diferenca):
    for f in diferenca:
        print("Arquivo",f,"criado ou alterado")

path='teste'

anterior = os.listdir(path)

while True :
    atual = os.listdir(path)
    diferenca = list(set(atual) - set(anterior))
    gerarbastao(diferenca)
    anterior = atual

