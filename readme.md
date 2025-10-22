Leitor de NF-e

Um projeto em Python para leitura de Notas Fiscais Eletrônicas (NF-e) a partir de arquivos XML, geração de relatórios em Excel com resumo e detalhes dos produtos, e interface gráfica moderna minimalista.

Funcionalidades

- Leitura automática de XMLs de NF-e a partir de uma pasta.

- Interface gráfica minimalista e moderna usando customtkinter.

- Filtros opcionais antes da geração do relatório:

- Data inicial e final da emissão.

- Valor mínimo da nota.

  *Relatório em Excel com:*

- Aba de Resumo das notas.

- Aba de Detalhes com todos os produtos de cada nota.

- Formatação elegante: cabeçalho em negrito, cores alternadas, colunas ajustadas automaticamente.

- Barra de progresso durante a leitura dos XMLs.

- Logs de erros gravados em logs.txt.

*Tecnologias e Bibliotecas*

Python 3.9+
pandas – manipulação de dados
openpyxl – criação de Excel
lxml – parsing de XML
customtkinter – interface gráfica moderna

*Como Usar*

Clone ou baixe este repositório.

Instale as dependências:

pip install -r requirements.txt


Execute o projeto:

python main.py


Na interface:

Clique em Selecionar pasta e escolha a pasta com os XMLs.

Ajuste filtros opcionais (data inicial/final, valor mínimo).

Clique em Gerar Relatório.

O Excel será gerado na pasta relatorio_output dentro da pasta selecionada.

Qualquer XML que apresentar erro será registrado em logs.txt.

Exemplo de Saída

Resumo: mostra todas as notas com chave, emitente, destinatário, data, valor total e total de itens.

Detalhes: lista todos os produtos de cada nota, com descrição, quantidade, valor unitário e total do item.

Observações

Compatível com NF-e (modelo 55) e NFC-e (modelo 65) em formato XML.

Projeto feito para fins de estudo e portfólio, sem uso de dados fiscais reais.

Interface minimalista e clean para melhor experiência de usuário.

Licença

MIT License – livre para uso e modificação.
