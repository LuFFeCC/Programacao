import os
from time import sleep
from sys import stderr, stdin, stdout
from unittest import result
import paramiko

def myping(host):         #FUNÇÃO PARA PINGAR HOSTS E VERIFICAR SE ESTÃO ATIVOS NA REDE
    resposta_ping = (os.system('ping -n 1 ' +host ))
    return resposta_ping

def windows_check(adress):     #FUNÇÃO PARA EXECUTAR A CONEXÃO E VERIFICAR SE A MAQUINA É WINDOWS OU LINUX
    parametro=0
    parametro = 'paexec.exe \\\\'+adress+' -u MIXHC\\fernando -p @mix080117 whoami' 
    resposta_windows = os.system(parametro)
    return resposta_windows

def windows_list(adress):     #FUNÇÃO PARA EXECUTAR A CONEXÃO E COMANDOS NAS MAQUINAS WINDOWS
    parametro=0
    #LISTANDO PROGRAMAS INSTALADOS NAS MAQUINAS E COLOCANDO DENTRO DE UM ARQUIVO NA MAQUINA CENTRAL
    parametro = 'paexec.exe \\\\'+adress+' -u MIXHC\\fernando -p @mix080117 copy NUL D:/REDE/'+ip+'/programas_instalados.txt'
    parametro = 'paexec.exe \\\\'+adress+' -u MIXHC\\fernando -p @mix080117 wmic product get name > D:/REDE/'+ip+'/programas_instalados.txt' 
    resposta_windows = os.system(parametro)
    return resposta_windows

ipsvalidos = []   # LISTA PARA GUARDAR OS IPS VALIDOS, E COLOCAR NO ARQUIVO IPS_VALIDOS.TXT
ips_tratamento = [] #LISTA PARA GUARDAR OS IPS
teste = []

username = "root" #input(print("DIGITE O USUÁRIO ADMINISTRADOR DA REDE: "))
password =  "teste123!!" #input(print("DIGITE A SENHA: "))

print("Digite a sua rede Ex: 192.168.0")
rede = input("REDE: ")

for i in range(0,255):
    ip = rede+'.'+str(i)
    ipsvalidos = myping(ip)
    
    
    if ipsvalidos == 0 :

        os.system('mkdir D:\\REDE\\'+ ip)
        
        resposta_funcao = windows_check(str(ip))
        if resposta_funcao == 0:
            maquina = "MAQUINA WINDOWS:"
            ip_valido = open('ipswindows.txt','a')
            ip_valido.write(str(ip)+'\n')
            executado=windows_list(str(ip))

        else :
            maquina = "Linux"
            ip_valido = open('ipslinux.txt','a')
            ip_valido.write(str(ip)+'\n')
            
        ip_valido = open('ips_validos.txt','a')
        ip_valido.write(str(ip)+'\n')
        ip_valido.write(str(maquina)+'\n\n')

