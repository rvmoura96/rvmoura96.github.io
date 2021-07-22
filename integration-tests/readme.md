## Testes de integração

Os testes de integração da solução foram desenvolvidos utilizando Python.

O framework utilizado foi o Behave um framework BDD foi escolhido tal
ferramenta para os testes, pois é uma ótima ferramenta para validar o comportamento
de aplicações. Também foram usadas algumas ferramentas de apoio ao Behave como
Selenium, Selenium-wire, Selenium standalone (Imagem docker) e Faker. Os testes foram realizados
para garantir que o comportamento solicitado no desafio está cumprindo seus
requisitos.

Todos os testes criados podem ser encontrados no diretório **bdd/features**.
Qualquer pessoa pode fazer a leitura dos testes, pois foram escritos em uma linguagem natural onde não é esperado
o conhecimento técnico para o entendimento dos cenários.

Para o controle das dependências do projeto foi utilizado o Poetry, para detalhes de instalação [clique aqui](https://python-poetry.org/docs/#installation).

**É necessário que tenha instalado Python 3.9, Docker e Poetry.**

Para as instruções de instalação do Docker [clique aqui](https://docs.docker.com/engine/install/)

Para o download da imagem do docker do selenium-standalone-firefox use o seguinte comando no seu terminal:
```
docker pull selenium/standalone-firefox
```

Para a execução do container do selenium baixado no passo anterior, use o comando no seu terminal:
```
docker run -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-firefox
```

Com o container inicializado, edite a chave **local_machine_ip** do arquivo **behave.ini**, seu endereço de rede local(deverá ser algo  como 192.168.X.X).

No diretório integration-tests, execute o comando seguinte comando para instalar as
depêndencias do projeto:
```
poetry install
```

Para ativar o ambiente virtual criado pelo poetry, no diretório integration-tests
execute o seguinte comando:
```
poetry shell
```

Feito esses passos no diretório integration-tests, execute o comando:
```
behave bdd/features/
```


### Notas
Caso queira que os testes sejam executados em outro navegador além do firefox, será
necessário instalar a imagem standalone do browser desejado, aqui fica um exemplo
para a alteração para o Google Chrome.

```
docker pull selenium/standalone-chrome
```

Para executar o container:
```
docker run -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome
```

Para a execução dos testes execute o seguinte comando no diretório integration-tests:
```
behave bdd/features/ -D browser=chrome
```
