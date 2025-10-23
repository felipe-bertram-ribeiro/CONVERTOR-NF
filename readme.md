Leitor de NF-e

Projeto desenvolvido em Python para leitura de Notas Fiscais Eletrônicas (NF-e) a partir de arquivos XML, com geração automática de relatórios em Excel e interface gráfica moderna e minimalista.

Funcionalidades

Leitura automática de arquivos XML de NF-e a partir de uma pasta especificada.

Interface gráfica moderna e minimalista, desenvolvida com CustomTkinter.

Filtros opcionais antes da geração do relatório:

Data inicial e final da emissão.

Valor mínimo da nota.

Relatório em Excel contendo:

Aba de Resumo com informações gerais das notas.

Aba de Detalhes com os produtos de cada nota.

Formatação aprimorada do relatório:

Cabeçalhos em negrito.

Cores alternadas nas linhas.

Ajuste automático das larguras das colunas.

Barra de progresso durante a leitura dos arquivos XML.

Registro automático de erros no arquivo logs.txt.

Tecnologias e Bibliotecas Utilizadas

Python 3.9+

pandas – manipulação e organização de dados

openpyxl – criação e formatação de planilhas Excel

lxml – leitura e parsing de arquivos XML

customtkinter – desenvolvimento da interface gráfica

Como Utilizar

Clone ou baixe este repositório:

git clone https://github.com/seuusuario/LeitorNFe.git
cd LeitorNFe


Instale as dependências:

pip install -r requirements.txt


Execute o projeto:

python main.py


Na interface:

Clique em Selecionar pasta e escolha a pasta com os arquivos XML.

Ajuste os filtros opcionais de data ou valor mínimo, se desejar.

Clique em Gerar Relatório.

O relatório em Excel será criado automaticamente na pasta relatorio_output dentro do diretório selecionado.
Erros encontrados durante o processamento serão registrados em logs.txt.

Estrutura do Relatório Gerado

Resumo: apresenta todas as notas com chave, emitente, destinatário, data, valor total e número de itens.

Detalhes: lista todos os produtos de cada nota, incluindo descrição, quantidade, valor unitário e total do item.

Observações

Compatível com NF-e (modelo 55) e NFC-e (modelo 65) no formato XML.

Desenvolvido com finalidade educacional e de portfólio, sem utilização de dados fiscais reais.

Interface limpa e responsiva, com foco na simplicidade e clareza para o usuário.

Licença

Este projeto é distribuído sob a Licença MIT.
O uso, modificação e redistribuição são permitidos, desde que mantidos os devidos créditos ao autor.
