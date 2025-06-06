# COPY PASTAS
🎈COPIE O NOME DE TODOS OS ARQUIVOS, DIRETÓRIOS E SUBDIRETÓRIOS.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O aplicativo **"COPY PASTAS"** é uma ferramenta simples e intuitiva, criada com a biblioteca **CustomTkinter** em Python, para listar e gerenciar caminhos de diretórios e subdiretórios, exibindo a quantidade de arquivos em cada pasta. O usuário pode escolher entre quatro tipos de exibição: apenas arquivos `.mp3`, todos os arquivos (incluindo `.mp3`), nomes em formato JSON ou TXT.

Além disso, o aplicativo oferece:

* Estatísticas detalhadas sobre a quantidade de pastas, arquivos e o espaço de armazenamento usado, livre e total do diretório selecionado.
* Comportamento inteligente dos botões: **"GERAR"** só é habilitado após a seleção de um diretório, e os botões **"LIMPAR"** e **"COLAR"** são ativados apenas após a geração do texto.
* O botão **"COPIAR"** exibe uma notificação visual do sistema (Windows/Linux) informando que o conteúdo foi copiado para a área de transferência.

## FUNCIONALIDADES:
1. **Selecionar Diretório**
   * **Botão "SELECIONAR"**: Abre uma janela para o usuário escolher o diretório base. O caminho é exibido em um campo de texto.

2. **Escolher Tipo de Arquivo**
   * **Botões de Seleção (MP3, TODOS, JSON, TXT)**: Permitem definir como os arquivos serão listados:
      * **MP3**: Lista apenas arquivos `.mp3`.
      * **TODOS**: Lista todos os arquivos, inclusive `.mp3`.
      * **JSON**: Exibe somente os nomes (sem caminhos) em formato de array JSON.
      * **TXT**: Exibe somente os nomes (sem caminhos) como lista simples de texto.

3. **Gerar Lista de Diretórios e Arquivos**
   * **Botão "GERAR"**:
      * Fica desabilitado até um diretório ser selecionado.
      * Processa a estrutura do diretório e lista os arquivos conforme o tipo selecionado.
      * Organiza os diretórios com numeração padronizada.
      * **Formato da Listagem** (MP3 ou TODOS):
      `{01 - 01} <-> PASTA/SUBPASTA <-> {X MUSICAS}` ou `{X ARQUIVOS}`
      * **Exemplo**:

      ```
      {01 - 01} <-> PASTA 1/SUBPASTA 1 <-> {5 MUSICAS}
      {02 - 06} <-> PASTA 1/SUBPASTA 2 <-> {2 MUSICAS}
      {03 - 08} <-> PASTA 2/SUBPASTA <-> {5 MUSICAS}
      {04 - 13} <-> PASTA 3 <-> {2 MUSICAS}
      ```
      * Ignora acentos nos nomes e a pasta `System Volume Information`.

4. **Exibir Estatísticas**
   * Após a geração da lista, exibe:

   * **TOTAL DE PASTAS**
   * **TOTAL DE MUSICAS/ARQUIVOS** (conforme o tipo selecionado)
   * **MEMÓRIA USADA, LIVRE e TOTAL** da unidade de armazenamento
   * **Formato**:

   ```
   =============================
               ESTATISTICAS:
   =============================
   TOTAL DE PASTAS: 10
   TOTAL DE ARQUIVOS: 171
   MEMÓRIA USADA: 5955 MB
   MEMÓRIA LIVRE: 2108 MB
   TOTAL DE MEMÓRIA: 8064 MB
   =============================
   =============================
   ```

5. **Copiar para a Área de Transferência**
   * **Botão "COPIAR"**:
      * Copia o conteúdo da área de texto (lista + estatísticas).
      * Exibe a mensagem do sistema informando que o conteúdo foi copiado com sucesso.

6. **Limpar Texto**
   * **Botão "LIMPAR"**:
      * Apaga o conteúdo atual exibido na tela.
      * Só é ativado após a geração do texto.

## POR QUE CRIEI ESTE APP?
Após usar o [DRIVESORT](https://www.anerty.net/software/file/DriveSort/) para manter a ordem dos diretórios e subdiretórios do meu PC em sistemas embarcados, percebi a necessidade de criar um novo aplicativo que armazenasse e listasse os nomes desses diretórios em ordem.

Eu utilizo meus pendrives em diversos sistemas embarcados, como caixas de som e DVDs, que geralmente não têm tela, apenas saídas de áudio. Isso tornava cansativo ter que adivinhar ou memorizar o número dos diretórios/faixas de cada álbum.

## EXECUTANDO O PROJETO:
1. **Instale as bibliotecas necessárias:** Antes de executar o app, certifique-se de instalar todas as dependências necessárias. No terminal, execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt em `CODIGO`:
   ```bash
   pip install -r requirements.txt
   ```
   
2. **Inicie o Aplicativo**:
   * Para executar o script Python, navegue até o diretório `./CODIGO` e use o comando:

   ```bash
   python CODIGO.py
   ```

3. **Selecione o Diretório**:
   * Clique no botão **"SELECIONAR"** para abrir a janela de escolha de diretório. Selecione o diretório base desejado. O caminho será exibido no campo de entrada.
   * O botão **"GERAR"** só será habilitado após a seleção de um diretório válido.

4. **Escolha o Tipo de Listagem**:
   * Antes de gerar a lista, selecione o tipo de conteúdo que deseja listar usando um dos botões:

     * **MP3**: Apenas arquivos `.mp3`.
     * **TODOS**: Todos os arquivos.
     * **JSON**: Apenas os nomes dos arquivos em formato de array JSON.
     * **TXT**: Apenas os nomes dos arquivos em formato de lista simples (um por linha).

5. **Gerar a Lista**:
   * Clique no botão **"GERAR"** para processar o diretório. O aplicativo percorrerá os subdiretórios e exibirá a listagem conforme o tipo selecionado.
   * Para MP3 ou TODOS, cada linha exibirá a contagem de arquivos no formato:

     ```
     {01 - XX} <-> PASTA/SUBPASTA <-> {X MUSICAS/ARQUIVOS}
     ```
   * Abaixo da listagem, serão exibidas as estatísticas de:

     * Total de pastas
     * Total de arquivos (ou músicas)
     * Espaço usado, livre e total do armazenamento
   * Os botões **"LIMPAR"** e **"COLAR"** só serão habilitados após essa geração.

6. **Copie a Lista**:
   * Após a geração, clique no botão **"COPIAR"** para copiar todo o conteúdo exibido (lista e estatísticas) para a área de transferência.
   * Uma notificação do sistema será exibida informando que o conteúdo foi copiado com sucesso.

7. **Limpe o Texto**:
   * Para limpar a área de texto e começar novamente, clique no botão **"LIMPAR"**.
   * Esse botão ficará habilitado somente após a geração da lista.

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO:
   * O instalador está disponível  em `./APP`. Para instala-lo, basta dar dois cliques e seguir as orientações na tela. 

### 2. GERANDO O EXECUTAVEL:
   **1. Instalação do PyInstaller:**
   * Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   * No diretório `./CODIGO`, utilize o comando abaixo para gerar o executável:

   ```bash
   pyinstaller EXECUTAVEL.spec
   ```

   * O executável `COPY PASTAS.exe` será criado na pasta `./CODIGO/dist`.
   * Após a geração, você pode excluir a pasta `./CODIGO/build`.

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O INSTALADOR:
1. **Editar o arquivo do instalador**
   No diretório `./CODIGO`, abra o arquivo `INSTALADOR.iss` e atualize os seguintes trechos:

   * **Ícone do instalador:**
     Substitua o caminho atual da linha `SetupIconFile=` pelo caminho correto do seu ícone:

     ```ini
     SetupIconFile=C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\COPY PASTAS\CODIGO\imagem.ico
     ```

   * **Caminho do executável a ser empacotado:**
     Atualize a seção `[Files]` com o caminho do executável gerado:

     ```ini
     [Files]
     Source: "C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\COPY PASTAS\CODIGO\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
     ```

2. **Gerar o instalador no Inno Setup:**
   * Abra o arquivo `./CODIGO/INSTALADOR.iss` com o **Inno Setup**.
   * Clique em **"Compile"** para gerar o instalador.

3. **Limpar arquivos temporários:**
   * Após a criação do instalador, você pode excluir o executável temporário:

     ```
     ./CODIGO/dist/COPY PASTAS.exe
     ```

4. **Instalando o Aplicativo:**
   * Execute o instalador gerado, localizado em:

   ```
   ./APP/COPY PASTAS.exe
   ```

   * O assistente de instalação será iniciado e, por padrão, o aplicativo será instalado em:

   ```
   C:\Program Files\COPY PASTAS
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [DOCUMENTAÇÃO OFICIAL DO PYINSTALLER](https://pyinstaller.org/en/stable/)
* [DOCUMENTAÇÃO OFICIAL DO INNO SETUP](http://www.jrsoftware.org/isinfo.php)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)

