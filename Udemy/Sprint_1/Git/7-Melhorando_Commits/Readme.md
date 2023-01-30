MELHORANDO OS COMMITS DO PROJETO

- A importãncia do commit
    Commits sem sentido atrapalham o projeto
        ideal é padronizar commits, auxiliando em
            Review do Pull Request
            Melhoria dos log
            manutenção do projeto
                ex. voltar código
    interesante é realizar o commit apenas quando a tarefa for finalizada e
    tentar minimizar ao maximo a quantidade de commits desnecessários.

- Branchs com commits ruins (resolução)
    Private branches
        branches não são compartilhados no repo
        após a solução e possivel reorganizar com rebase de forma interativa
            $ git rebase <branch_atual> <fbranch_privado> -i
        escolhemos as branches à excluir (na verdade vai se juntar ao próximo)
            squash
        escolhamos as branches à renomear
            reword