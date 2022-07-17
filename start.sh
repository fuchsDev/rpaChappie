#!/bin/bash

nameScript=( 
"00 - EnergiaSolar"   
"01 - RotinaCompusisWebFl01" 
"02 - RotinaCompusisWebFl02" 
"03 - RotinaLinxLinxPDV"
"04 - RotinaLinxSuprimentos" 
"05 - RotinaLinxRecebimentos" 
"06 - RotinaLinxDescontos" 
"07 - RotinaLinxAfericoes" 
"08 - RotinaLinxPortal" 
"09 - RotinaShell" 
"10 - RotinaVibra" 
"11 - RotinaIpiranga" 
"12 - StartWorkSpaceBrave"
)

#loop pelo array rodando os scripts
for i in {0..12}; do
    echo "Start ${nameScript[$i]}"
    python3 "/home/fk/Documents/fuchsDev/rpaChappie/scripts/$i.py"
    sleep 1
done

#move prints
echo 'Move .png'
mv *.png ~/Downloads

#renomeia arquivos .xls
echo 'Rename .xls'
mv ~/Downloads/PesquisaTitulos_3.xlsx ~/Downloads/pagamentos.xls
mv ~/Downloads/SangriaSuprimento_3.xlsx ~/Downloads/suprimentos.xls