#!/bin/dash
# Desenvolvido por Tchelo Noob
atualizar='\033[1;32m'
echo "$atualizar Atualizando repositório..."
apt update && upgrade -y
apt install -y wget
clear
k='\033[01;32m'
toilet -f big -F metal "PT - lub"
toilet -f big -F gay "ngRok"
echo "Подтвердите устоновку[Y/n]"
read opcao
case $opcao in
y)
echo
echo "Загрузка Termux-ngrok..."
clear
toilet -f big -F gay "Install"

case `dpkg --print-architecture` in
aarch64)
    architectureURL="arm64" ;;
arm)
    architectureURL="arm" ;;
armhf)
    architectureURL="armhf" ;;
amd64)
    architectureURL="amd64" ;;
i*86)
    architectureURL="i386" ;;
x86_64)
    architectureURL="amd64" ;;
*)
    echo "Arquitetura desconhecida"
esac
 
wget "https://github.com/tchelospy/NgrokTest/blob/master/ngrok-stable-linux-${architectureURL}.zip?raw=true" -O ngrok.zip
unzip ngrok.zip
cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
chmod 700 /data/data/com.termux/files/usr/bin/ngrok
rm ngrok ngrok.zip
clear
toilet -f big -F gay "Install"

echo "Напиши (ngrok http 8080)"
;;
 
n)
clear
echo "Ngrok não instalado :("
echo
esac

ngrok http 8080
 
 
 