#!/bin/bash

#automated email with bookmarks - Gmail

#declares array
nameScript=( 
"00 - SolarView"   
"01 - RotinaCompusisWebFl01" 
"02 - RotinaCompusisWebFl02" 
"03 - RotinaLinxLinxPDV"
"04 - RotinaLinxSupplies" 
"05 - RotinaLinxReceipts" 
"06 - RotinaLinxDiscount" 
"07 - RotinaLinxScounting" 
"08 - RotinaLinxPortal" 
"09 - RotinaShell" 
"10 - RotinaVibra" 
"11 - RotinaIpiranga" 
"12 - StartWorkSpaceBrave"
)

#loop for array nameScript
for i in {0..12}; do
    echo "Start ${nameScript[$i]}"
    python3 "/home/fk/Documents/fuchsDev/rpaChappie/scripts/$i.py"
    sleep 1
done

#move prints
echo 'Move .png'
mv *.png ~/Downloads

#rename files .xls
echo 'Rename .xls'
mv ~/Downloads/PesquisaTitulos_3.xlsx ~/Downloads/pagamentos.xls
mv ~/Downloads/SangriaSuprimento_3.xlsx ~/Downloads/suprimentos.xls