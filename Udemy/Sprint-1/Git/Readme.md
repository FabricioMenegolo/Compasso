- criando repositório
    git init

- enviar nossos repos
    touch text.txt
    git add text.txt
    git commit -m "first commit"
- adiciona origem
    git remote add origin https://github.com/FabricioMenegolo/Compasso.git
    
    git push -u origin main
            visualizar origens
            git remote -v
        remover origem
            git remote rm origin

- Verificando mudanças do projeto
    git status

- Adicionando arquivos ao projeto
    - arquivo único
        git add nomeArquivo.ext
    - diversos arquivo
        git add .

- Salvando alterações do projeto
    git commit -a -m "mensagem"
        - arquivo especifico
            commit nomeArquivo.ext -m "mensagem"
            
- Enviando código ao repo remoto    
    git push

- Recebendo as mudanças
    git pull

- Clonando repositórios via HTTPS
    git clone https://github.com/usuario/repo.git

- Removendo arquivos do repo
    git rm nomeArquivo.ext

- Histórico de alterações
    git log

- Renomeando arquivos
    git mv