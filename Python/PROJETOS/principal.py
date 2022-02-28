import os
from time import sleep
from sys import stderr, stdin, stdout
from unittest import result
import paramiko

def myping(host):         #FUNÇÃO PARA PINGAR HOSTS E VERIFICAR SE ESTÃO ATIVOS NA REDE
    resposta_ping = (os.system('ping -n 1 ' +host ))
    return resposta_ping

def ssh_connect(command):   #FUNÇÃO PARA SE CONECTAR AO LINUX POR SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=adress, username=username, password=password)
    stdin, stdout, stderr, = ssh.exec_command(command)
    stdin.close()
    resposta_ssh = stdout.readlines()
    return resposta_ssh

def windows(adress):     #FUNÇÃO PARA EXECUTAR A CONEXÃO E COMANDOS NAS MAQUINAS WINDOWS
    parametro=0
    parametro = 'paexec.exe \\\\'+adress+' -u MIXHC\\fernando -p @mix080117 wmic'
    c1 = 'paexec.exe \\\\'+adress+' -u MIXHC\\fernando -p @mix080117 product get name'
    resposta_windows = os.system(parametro)
    resposta_windows = os.system(c1)
    return resposta_windows

ipsvalidos = []   # LISTA PARA GUARDAR OS IPS VALIDOS, E COLOCAR NO ARQUIVO IPS_VALIDOS.TXT
ips_tratamento = [] #LISTA PARA GUARDAR OS IPS
teste = []

username = "root" #input(print("DIGITE O USUÁRIO ADMINISTRADOR DA REDE: "))
password =  "teste123!!" #input(print("DIGITE A SENHA: "))

print("Digite a sua rede Ex: 192.168.0")
rede = input("REDE: ")

for i in range(0,1):
    ip = rede+'.'+str(46)
    ipsvalidos = myping(ip)
    
    
    if ipsvalidos == 0 :
        
        resposta_funcao = windows(str(ip))
        if resposta_funcao == 0:
            maquina = "MAQUINA WINDOWS:"
            ip_valido = open('ipswindows.txt','a')
            ip_valido.write(str(ip)+'\n')
        else :
            maquina = "Linux"
            ip_valido = open('ipslinux.txt','a')
            ip_valido.write(str(ip)+'\n')
            
        ip_valido = open('ips_validos.txt','a')
        ip_valido.write(str(ip)+'\n')
        ip_valido.write(str(maquina)+'\n\n')