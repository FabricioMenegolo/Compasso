- criando repositório
    git init

- enviar nossos repos
    touch text.txt
    git add text.txt
    git commit -m "first commit"
- adiciona origem
    git remote add origin https://github.com/FabricioMenegolo/Compasso.git
    
            visualizar origens
            git remote -v
        remover origem
            git remote rm origin

- enviar conteúdo do repositório local para um repositório remoto     
    git push -u origin main

- exibe as condições do diretório de trabalho e da área de staging
    git status

- realiza a inclusão ou modificação do arquivo no diretório local, preparando ele para ser entregue ao servidor remoto para a mesma aplicação que está sincronizada na máquina local.
    - arquivo único
        git add nomeArquivo.ext
    - diversos arquivo
        git add .

- snapshot do seu repositório em determinado momento
    git commit -a -m "mensagem"
        - arquivo especifico
            commit -a nomeArquivo.ext -m "mensagem"
            