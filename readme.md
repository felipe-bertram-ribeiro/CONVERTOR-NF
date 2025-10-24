
  <h1>Leitor de NF-e</h1>

  <h2>Descrição</h2>
  <p>Projeto desenvolvido em Python para leitura de Notas Fiscais Eletrônicas (NF-e) a partir de arquivos XML, com geração automática de relatórios em Excel e interface gráfica moderna e minimalista.</p>

  <h2>Funcionalidades</h2>
  <ul>
    <li>Leitura automática de arquivos XML de NF-e a partir de uma pasta especificada.</li>
    <li>Interface gráfica moderna e minimalista, desenvolvida com CustomTkinter.</li>
    <li>Filtros opcionais antes da geração do relatório:
      <ul>
        <li>Data inicial e final da emissão.</li>
        <li>Valor mínimo da nota.</li>
      </ul>
    </li>
    <li>Relatório em Excel contendo:
      <ul>
        <li>Aba de Resumo com informações gerais das notas.</li>
        <li>Aba de Detalhes com os produtos de cada nota.</li>
      </ul>
    </li>
    <li>Formatação aprimorada do relatório:
      <ul>
        <li>Cabeçalhos em negrito.</li>
        <li>Cores alternadas nas linhas.</li>
        <li>Ajuste automático das larguras das colunas.</li>
      </ul>
    </li>
    <li>Barra de progresso durante a leitura dos arquivos XML.</li>
    <li>Registro automático de erros no arquivo <code>logs.txt</code>.</li>
  </ul>

  <h2>Tecnologias e Bibliotecas Utilizadas</h2>
  <ul>
    <li>Python 3.9+</li>
    <li>pandas – manipulação e organização de dados</li>
    <li>openpyxl – criação e formatação de planilhas Excel</li>
    <li>lxml – leitura e parsing de arquivos XML</li>
    <li>customtkinter – desenvolvimento da interface gráfica</li>
  </ul>

  <h2>Como Utilizar</h2>
  <ol>
    <li>Clone ou baixe este repositório:
      <pre><code>git clone https://github.com/seuusuario/LeitorNFe.git
cd LeitorNFe</code></pre>
    </li>
    <li>Instale as dependências:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Execute o projeto:
      <pre><code>python main.py</code></pre>
    </li>
    <li>Na interface:
      <ul>
        <li>Clique em "Selecionar pasta" e escolha a pasta com os arquivos XML.</li>
        <li>Ajuste os filtros opcionais de data ou valor mínimo, se desejar.</li>
        <li>Clique em "Gerar Relatório".</li>
      </ul>
    </li>
    <li>O relatório em Excel será criado automaticamente na pasta <code>relatorio_output</code> dentro do diretório selecionado. Erros encontrados durante o processamento serão registrados em <code>logs.txt</code>.</li>
  </ol>

  <h2>Estrutura do Relatório Gerado</h2>
  <ul>
    <li><strong>Resumo:</strong> apresenta todas as notas com chave, emitente, destinatário, data, valor total e número de itens.</li>
    <li><strong>Detalhes:</strong> lista todos os produtos de cada nota, incluindo descrição, quantidade, valor unitário e total do item.</li>
  </ul>

  <h2>Observações</h2>
  <ul>
    <li>Compatível com NF-e (modelo 55) e NFC-e (modelo 65) no formato XML.</li>
    <li>Desenvolvido com finalidade educacional e de portfólio, sem utilização de dados fiscais reais.</li>
    <li>Interface limpa e responsiva, com foco na simplicidade e clareza para o usuário.</li>
  </ul>

  <h2>Licença</h2>
  <p>Este projeto é distribuído sob a Licença MIT. O uso, modificação e redistribuição são permitidos, desde que mantidos os devidos créditos ao autor.</p>

</body>
</html>
