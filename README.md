# Projeto-em-grupo-2
Projeto em grupo do segundo módulo
Script de Pesquisa com Armazenamento em CSV

Este é um script em Python que permite a realização de uma pesquisa com perguntas e respostas, e salva as respostas em um arquivo CSV. O script foi desenvolvido para coletar informações de pesquisa de uma maneira simples e eficaz.
Funcionalidades

    Coleta respostas para uma série de perguntas.
    Valida as respostas e armazena as informações em um arquivo CSV.
    Permite a inclusão de novas respostas toda vez que uma informação é inserida.

Requisitos

Para executar este script, você precisará ter Python instalado em seu sistema. Além disso, não é necessário instalar bibliotecas adicionais, pois o script utiliza as bibliotecas padrão do Python, como csv e datetime.
Utilização

    Execute o script utilizando o Python. Certifique-se de que o arquivo de script (por exemplo, pesquisa.py) e o arquivo CSV (por exemplo, pesquisa.csv) estejam no mesmo diretório.

    O script iniciará a pesquisa, fazendo uma série de perguntas.

    Para cada pergunta, o participante da pesquisa deve fornecer uma resposta válida. Respostas inválidas não serão registradas.

    Após cada resposta válida, a informação será armazenada no arquivo CSV. O arquivo CSV será atualizado a cada nova resposta.

    Você pode encerrar a pesquisa a qualquer momento digitando 's' quando solicitado.

Estrutura do Arquivo CSV

O arquivo CSV contém as seguintes colunas:

    idade: A idade do participante.
    genero: O gênero do participante (M/F/NB).
    pergunta_1, pergunta_2, ...: As respostas para cada pergunta, onde "pergunta_1" se refere à primeira pergunta, "pergunta_2" à segunda, e assim por diante.
    data: A data em que a resposta foi registrada.
    hora: A hora em que a resposta foi registrada.

Exemplo de Uso

    Coletar informações para pesquisas acadêmicas.
    Realizar pesquisas de mercado.
    Coletar dados de usuários sobre produtos ou serviços.

Observações

Certifique-se de que o arquivo CSV exista no mesmo diretório que o script antes de executá-lo. O script armazenará as respostas no arquivo CSV a cada nova entrada de informações.

Este script é uma ferramenta versátil para coletar informações de pesquisa de forma eficaz e manter um registro organizado das respostas.
