#!/bin/bash
#variable warna
#gunakan script ini dengan bijak
#created by K1M4K-ID
#github : https://github.com/K1M4K-ID
#thanks to : E99 & Gafar Rizky
#terimakasih
#recode tidak akan membuat mu bisa menjadi seorang programer

me="\033[31;1m"
hi="\033[32;1m"
ku="\033[33;1m"
bi="\033[34;1m"
un="\033[35;1m"
cy="\033[36;1m"
pu="\033[37;1m"

clear

awal(){
echo $bi
banner
sleep 0.01
echo $hi"[1]$ku Install Bahan";
sleep 0.01
echo $hi"[2]$ku Sudah Install";
sleep 0.01
echo $hi"[3]$ku Updates Script";
sleep 0.01
echo $hi"[4]$ku Contact Person";
sleep 0.01
echo $hi"[0]$ku exit";
sleep 0.01
echo $hi
read -p "masukan pilihan : " pilih
}

ulang(){
ulang="s"
while [ $ulang = "s" ];
do
	sleep 0.01
done
}

banner(){
echo """
              ███╗   ███╗███████╗███████╗
              ████╗ ████║██╔════╝██╔════╝
              ██╔████╔██║███████╗█████╗
              ██║╚██╔╝██║╚════██║██╔══╝
              ██║ ╚═╝ ██║███████║██║
              ╚═╝     ╚═╝╚══════╝╚═╝
        ██╗  ██╗██╗███╗   ███╗ █████╗ ██╗  ██╗
        ██║ ██╔╝██║████╗ ████║██╔══██╗██║ ██╔╝
        █████╔╝ ██║██╔████╔██║███████║█████╔╝
        ██╔═██╗ ██║██║╚██╔╝██║██╔══██║██╔═██╗
        ██║  ██╗██║██║ ╚═╝ ██║██║  ██║██║  ██╗
        ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
$bi"————————————————————————————————————————————————————"
$me"Author"     ":"    	              $pu"K1M4K-ID"
$me"Thanks To"  ":"	                  $pu"E99" | "Gafar Rizky"
$me"Youtube"    ":"	                  $pu"Fadillah Ramadhan"
"""
}

log(){
echo """
   