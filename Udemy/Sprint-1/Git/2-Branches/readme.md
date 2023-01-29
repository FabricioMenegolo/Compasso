inicia a partir da branch main/master

Branch é ramificação de um projeto
    como forma de separa versões do projeto
    após finalizado as implementações, as branchs podem ser unidas (merge)
    
Facilita manutenção e diagnostico de erro ao código

- Criando e visualizando branches
    git branch <nome_da_branch>

- Deletando branches
    git branch
        flag -d ou --delete
        git branc -d <nome_da_branch>
    não é normal deletar uma branch, geralmente usado para consulta de historico
    geralmente ocorre quando ele é criado com nome errado
    
- Mudando de branch
    git checkout <nome_da_branch>
    - muda e cria o branch
        git checkout -b <nome_da_branch>
    - também é usado para dispensar mudanças de um arquivo
        git checkout <nome_do_arquivo>

- Unindo branches

- Stash

- Recuperando stash

- Removendo a stash

- Utilizando tags

- Verificando e alterando tags

- Enviando e compartilhando tags