ADMINISTRAÇÃO DO REPOSITÓRIO

- Limpando arquivos untracked
    para arquivos que são gerados automaticamente
        Ou todos que você não utilizou git add
    git clean
        flag -f
            forçar ação

- Otimizando o repositório
    git gc

- Chegando integridade de arquivos
    git fsck

- Reflog
    git reflog

- Recuperando arquivos com reflog
    git reset --hard <hash>
    git stash
    *Lembrando: o reflog expira com o tempo!

- Transformando o repo para arquivo
    git archive --format zip --output master_files.zip master