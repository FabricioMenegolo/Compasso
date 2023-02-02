MANIPULAÇÃO DE CONTEÚDOS COM COMANDOS SHELL

- Visualizadores de texto

    cat [arquivo]
        exibe todo conteudo do arquivo em texto

    more [arquivo]
        corre pagina a pagina aparece porcentagem para concluir, ele nao volta

    less [arquivo]
        ja é possivel navegar por todo o conteudo do texto oe voltar ou pesquisar linha com "/" e voltar com Shift + N

    head [arquivo]
        visualiza as primeiras linhas do arquivo (default: 10)
        flag -n [nº]
            mostra número especifico de linhas
    
    tail [arquivo]
        visualiza as ultimas linhas do arquivo ( default: 10)
        flag -n [nº]
            mostra número especifico de linhas 

        flag -f
            permanece aberto na tela e atualiza a visualização caso houver alteração
            ex.: tail -f /var/log/auth.log

- Redirecionadores

    - Entrada Padrão stdin

        “>”: Envia a saída para um arquivo ou dispositivo, porém, se o 
arquivo já existir, o seu conteúdo é sobrescrito.

        “>>”: Envia a saída para um arquivo ou dispositivo, porém, se o 
arquivo já existir, a saída do comando é ADICIONADA no final do arquivo 
especificado.

    - Saida padrão stdout

        “<”: Faz com que determinado comando receba algo como entrada

        “<<”: Utilizado para determinar o final de um “bloco” de dados

    - Saida de erro padrão stderr

        “2>”: Envia apenas os sinais de erro para um arquivo ou dispositivo, 
porém, se o arquivo já existir, o seu conteúdo é sobrescrito.

        “2>>”: Envia apenas os sinais de erro para um arquivo ou 
dispositivo, porém, se o arquivo já existir, a saída (apenas os erros) será 
ADICIONADA no final do arquivo

     “/dev/null” é um arquivo especial que descarta toda informação enviada para ele, além de 
não retornar nenhuma informação caso seja acessado

- Concatenação de comandos

    Para realizar a concatenação, devemos utilizar dutos (duto = PIPE = | )
        “pegar” a saída de um comando e utilizá-la como “entrada” para o comando seguinte

    - Conectores e Operadores
        Ponto e vírgula “;” para execução de comandos em sequência
            não há relação entre sucesso das execuções ou não

        Operador “&&” (AND), caso o primeiro comando execute com sucesso (código de retorno = 0), o 
segundo comando também será executado

    Operador “||” (OR), caso o primeiro comando não execute com sucesso (código de retorno ≠ 0), o segundo comando será executado. RESUMINDO, quando um dos comandos for executado com sucesso, os comandos seguintes não são verificados

Filtros de conteúdo

Empacotadores e Compactadores
