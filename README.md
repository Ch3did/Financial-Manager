# Monetary Maid
** Esse repositorio foi criado com intuito de extrair extratos bancarios e controle financeiro automatico utilizando o pynubank. Por conta do bloqueio ao acesso da api publica do banco, o codigo foi ajustado para receber OFX e realizar o mesmo controle financeiro**

## Init

Monetary Maid é uma Interface de Linha de Comando (CLI) projetada para ajudá-lo a gerenciar suas finanças. Com ele, você pode importar arquivos OFX de seus bancos, criar categorias para associar às transações e definir valores esperados para cada tipo de despesa. Isso permite acompanhar quais despesas estão ultrapassando as expectativas ao longo do mês.

O projeto também inclui um comando para exportar todos os dados inseridos e categorizados para um arquivo CSV, permitindo obter quaisquer insights adicionais que você precisar.

## Requirements

- Sistema Operacional baseado em Debian
- Python3.8 ou superior

## Install
 Para instalar o projeto, basta entrar na pasta do projeto e rodar o comando asseguir:

> ./install.sh

Isso ira criar uma venv e um alias (fmanager) dentro do seu bash para acesso em qualquer terminal e um database emm sqlite3 dentro do `~/.local` pra lidar com os dados da aplicação. 

## Commands:

### <strong> ```migrate```</strong>:
Cria as tabelas do banco de dados.
Uso: Pode ser usado sozinho.

### <strong> ```import```</strong>:
Importa um arquivo ou um diretório contendo arquivos OFX.
Uso: Passar um arquivo ou diretório.

### <strong> ```top```</strong>:
Retorna o número de registros no banco de dados.
Uso: Pode ser usado sozinho para retornar os últimos 10 registros ou com um parâmetro numérico para especificar o número de registros a serem exibidos.

### <strong> ```export```</strong>:
Exporta o banco de dados como um CSV para um novo arquivo.
Uso: Passar o caminho onde o arquivo deve ser gravado.

### <strong> ```category```</strong>:
Imprime a lista de categorias existentes no banco de dados.
Uso: Nenhum argumento adicional necessário.

### <strong> ```create```</strong>:
Cria uma nova categoria.
Uso: Irá solicitar o nome, descrição e valor esperado.

### <strong> ```home```</strong>:
Mostra a porcentagem do orçamento esperado que já foi gasto no mês atual.
Uso: Nenhum argumento adicional necessário.