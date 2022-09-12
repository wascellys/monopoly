# Banco Imobiliário

- [Instalação](#instalação)
  - [Usando ambiente virtual](#usando-ambiente-virtual)
  - [Instalação das Dependências ](#instalação-das-dependências)
- [Rodar Projeto](#rodar-projeto)
- [Cobertura de Testes](#cobertura-de-testes)

## Instalação

### Clonar repositório
```
git clone https://github.com/wascellys/monopoly.git
```
## Usando ambiente virtual
#### Instalação do Python em terminal Linux
```
sudo apt install python3-pip python3-dev libpq-dev virtualenv
```
#### Criando virtualenv
```
virtualenv myenv --python=python3
```
#### Ativação da  virtualenv
```
source myenv/bin/activate
```
## Instalação das Dependências
```
pip install -r requirements.txt
```

## Rodar Projeto
No diretório do projeto execute o comando:
```
python main.py
```

## Cobertura de testes
No diretório do projeto execute o comando:
```
coverage run -m pytest
```

Para ver os testes em detalhe, execute o comando:
```
coverage report -m
```

Para gerar um relatório com os testes em um arquivo HTML, execute o comando:
```
coverage html
```
Será criada uma nova pasta com o nome "htmlcov", basta abrir no arquivo index.html no navegador.
