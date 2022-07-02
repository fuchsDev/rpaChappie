# Projeto de RPA em Python

Este é um projeto de automação pessoal para simplificar algumas tarefas do meu trabalho;

Processos automatizados:
- 0: verifica funcionamento dos painéis de energia solar
- 1: abre dia para movimentações e verifica sincronizações do dia anterior (filial 01)
- 2: abre dia para movimentações e verifica sincronizações do dia anterior (filial 02)
- 3: fecha os PDVs utilizados no dia anterior (matriz)
- 4: faz download de arquivo utilizado para conferir os caixas (matriz)
- 5: faz download de arquivo utilizado para conferir as quitações dos clientes (matriz)
- 6: verifica os valores de descontos aplicados no dia anterior (matriz)
- 7: verifica relação de aferições lançadas no dia anterior (matriz)
- 8: verifica as duplicatas e chamados de suporte em aberto com o sistema ERP (matriz)
- 9: verifica duplicatas em aberto e preços de produtos vendidos com a rede bandeirada (filial 02)
- 10: verifica duplicatas em aberto e preços de produtos vendidos com a rede bandeirada (matriz)
- 11: verifica duplicatas em aberto e preços de produtos vendidos com a rede bandeirada (filial 01)
- 12: deixa o meu ambiente de trabalho no navegador brave pronto para utilização


Ferrmantas utilizadas:
- python
- vs code / github
- ambiente linux ubuntu


Organização do Projeto:
- rpaChappie/
    diretório raiz do projeto 
    arquivo start.sh utilizado para iniciar a automação
- scrips/ 
    possuí todas as tarefas salvas e numeradas
    há dois arquivos de posições por que utilizo o sistema em dois computadores diferentes
    arquivo variables.py possui dados sensíveis que constam apenas em ambiente local
- tests/
    novas implementações que estão em estudo e produção se encontram aqui
    script mouse.py é utilizado para mapear as posições na tela


Ideias de novas funcionalidades:
- lembretes dos clientes que tem faturamento agendado para o dia (Auto Posto);
- fechamento dos PDVs pelo Compusis Web (3817);
- rotina de LMC Compusis Web (3779);
- download de relatórios mensais usados no DRE Gerencial;
- print dos produtos cadastrados no dia anterior nos sistemas Linx e Compusis;
- verificar se planilha de cobranças dos clientes foi atualizada;
- conciliar inventários utilizando arquivos .txt;
- elaborar escalas dos funcionários (Auto Posto);
- calcular e projetar o mês de recebimento de bônus contratual;
- refatorar e limpar o código (simplificar);
- melhorar este readme.md (organização do projeto está estranho no github)

Manutenções a fazer:
- Portais bandeiras
- Atualização layout linx