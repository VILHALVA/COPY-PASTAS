# COPY PASTAS
🎈COPIE O NOME DE TODOS OS ARQUIVOS, DIRETÓRIOS E SUBDIRETÓRIOS.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O aplicativo "COPY PASTAS" é uma ferramenta simples e intuitiva, criada com a biblioteca Tkinter em Python, para listar e gerenciar caminhos de diretórios e subdiretórios, exibindo a quantidade de arquivos em cada pasta. O usuário pode escolher entre quatro tipos de exibição: apenas arquivos `.mp3`, todos os arquivos (incluindo `.mp3`), nomes em formato JSON ou TXT. Além disso, o aplicativo oferece estatísticas detalhadas sobre a quantidade de pastas, arquivos e o espaço de armazenamento usado, livre e total do diretório selecionado. A principal funcionalidade é listar os caminhos dos diretórios de um caminho raiz e exibi-los de forma organizada, permitindo fácil cópia para a área de transferência.

## FUNCIONALIDADES:
1. **Selecionar Diretório**:
   * **Botão "SELECIONAR"**: Abre uma janela para o usuário escolher o diretório base. O caminho é exibido em um campo de texto.

2. **Escolher Tipo de Arquivo**:
   * **Botões de Seleção (MP3, TODOS, JSON, TXT)**: Permitem definir como os arquivos serão listados:

     * **MP3**: Lista apenas arquivos `.mp3`.
     * **TODOS**: Lista todos os arquivos, inclusive `.mp3`.
     * **JSON**: Exibe somente os nomes (sem caminhos) em formato de array JSON.
     * **TXT**: Exibe somente os nomes (sem caminhos) como lista simples de texto.

3. **Gerar Lista de Diretórios e Arquivos**:
   * **Botão "GERAR"**: Processa a estrutura do diretório e lista os arquivos conforme o tipo selecionado. Organiza os diretórios com numeração padronizada.
   * **Formato da Listagem**:
     * Para MP3 ou TODOS: `{01 - 01} <-> PASTA/SUBPASTA <-> {X MUSICAS}` ou `{X ARQUIVOS}`
   * **Exemplo**:

     ```
     {01 - 01} <-> PASTA 1/SUBPASTA 1 <-> {5 MUSICAS}
     {02 - 06} <-> PASTA 1/SUBPASTA 2 <-> {2 MUSICAS}
     {03 - 08} <-> PASTA 2/SUBPASTA <-> {5 MUSICAS}
     {04 - 13} <-> PASTA 3 <-> {2 MUSICAS}
     ```
   * Ignora acentos nos nomes e a pasta `System Volume Information`.

4. **Exibir Estatísticas**:
   * Após a geração da lista, exibe:
     * **TOTAL DE PASTAS**: Número total de pastas.
     * **TOTAL DE MUSICAS/ARQUIVOS**: Conforme o tipo selecionado.
     * **MEMÓRIA USADA, LIVRE e TOTAL**: Informações da unidade de armazenamento.
   * **Formato**:

     ```
     ==========================================
                 ESTATÍSTICAS:
     ------------------------------------------
     TOTAL DE PASTAS: 10
     TOTAL DE ARQUIVOS: 171
     MEMÓRIA USADA: 5955 MB
     MEMÓRIA LIVRE: 2108 MB
     TOTAL DE MEMÓRIA: 8064 MB
     ------------------------------------------
     ==========================================
     ```

5. **Copiar para a Área de Transferência**:
   * **Botão "COPIAR"**: Copia o conteúdo da área de texto (lista e estatísticas) para a área de transferência.

6. **Limpar Texto**:
   * **Botão "LIMPAR"**: Apaga o conteúdo atual exibido na tela.

## POR QUE CRIEI ESTE APP?
Após usar o [DRIVESORT](https://www.anerty.net/software/file/DriveSort/) para manter a ordem dos diretórios e subdiretórios do meu PC em sistemas embarcados, percebi a necessidade de criar um novo aplicativo que armazenasse e listasse os nomes desses diretórios em ordem.

Eu utilizo meus pendrives em diversos sistemas embarcados, como caixas de som e DVDs, que geralmente não têm tela, apenas saídas de áudio. Isso tornava cansativo ter que adivinhar ou memorizar o número dos diretórios/faixas de cada álbum.

## EXECUTANDO O PROJETO:
1. **Inicie o Aplicativo**:
   * Para executar o script Python, navegue até o diretório `./CODIGO` e use o comando:

   ```bash
   python CODIGO.py
   ```

2. **Selecione o Diretório**:
   * Clique no botão **"SELECIONAR"** para abrir a janela de escolha de diretório. Selecione o diretório base desejado. O caminho será exibido no campo de entrada.

3. **Escolha o Tipo de Listagem**:
   * Antes de gerar a lista, selecione o tipo de conteúdo que deseja listar usando um dos botões:

     * **MP3**: Apenas arquivos `.mp3`.
     * **TODOS**: Todos os arquivos.
     * **JSON**: Apenas os nomes dos arquivos em formato de array JSON.
     * **TXT**: Apenas os nomes dos arquivos em formato de lista simples (um por linha).

4. **Gerar a Lista**:
   * Clique no botão **"GERAR"** para processar o diretório. O aplicativo percorrerá os subdiretórios e exibirá a listagem conforme o tipo selecionado. Para MP3 ou TODOS, cada linha exibirá a contagem de arquivos:

     ```
     {01 - XX} <-> PASTA/SUBPASTA <-> {X MUSICAS/ARQUIVOS}
     ```
   * Abaixo da listagem, serão exibidas as estatísticas de pastas, arquivos e armazenamento.

5. **Copie a Lista**:
   * Após a geração, clique no botão **"COPIAR"** para copiar todo o conteúdo exibido (lista e estatísticas) para a área de transferência.

6. **Limpe o Texto**:
   * Para limpar a área de texto e começar novamente, clique no botão **"LIMPAR"**.

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO:
   - O instalador está disponível apenas para `Windows X64`. Para instala-lo, basta dar dois cliques e seguir as orientações na tela. 

   - O executável está disponível apenas para `Windows X64` (No diretório `APP`). Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

   - É importante explicar que ao executar o arquivo executável deste programa, é possível que o antivírus dispare um alerta de segurança. Isso ocorre porque o programa executa comandos do sistema operacional e pode abrir outros aplicativos ou acessar a rede.

   **Para lidar com isso, há 2 alternativas:**

   1. **Adicionar exceção ao antivírus:** Você pode optar por adicionar uma exceção ao antivírus para permitir que o programa execute comandos do sistema sem disparar alertas. Isso geralmente pode ser feito acessando as configurações do antivírus e adicionando o arquivo executável do programa à lista de exceções.

   2. **Executar apenas o `CODIGO.py`:** Uma alternativa é optar por executar apenas o arquivo de código-fonte Python (`CODIGO.py`). Isso evita que o antivírus dispare alertas, já que você e o sistema podem inspecionar o código fonte diretamente.

### 2. GERANDO O EXECUTAVEL:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O SCRIPT DO INSTALADOR:
1. **Abrir o Inno Setup**: Após a instalação, abra o Inno Setup.
2. **Novo Script**: Na tela inicial, clique em "New Script" e selecione "Next" no assistente que aparecer.
3. **Informações Básicas**:
   - **Application Information**: Preencha as informações da sua aplicação, como nome, versão, nome do publisher e website.
   - **Application Destination Base Folder**: Normalmente, você pode deixar como "{pf}\YourAppName" (para instalar no diretório de Program Files).
   - **Application Directory**: Selecione a pasta onde estão os arquivos da sua aplicação. Em `./CODIGO` desse repositório.
   - **Application Files**: Adicione todos os arquivos necessários para a instalação da sua aplicação (executáveis, DLLs, etc).
   - **Application Shortcuts**: Escolha se deseja criar atalhos no menu Iniciar, na área de trabalho, etc.
   - **Application Documentation**: Adicione arquivos de licença e outros documentos necessários.
4. **Output**: Escolha onde o arquivo de instalação (.exe) será salvo.
5. **Create Script**: Clique em "Finish" para gerar o script base.

#### PASSO 3: EDITAR O SCRIPT:
O Inno Setup irá abrir o script gerado automaticamente. Aqui, você pode fazer ajustes se necessário. O script terá uma estrutura básica como esta:

```pascal
[Setup]
AppName=Your Application Name
AppVersion=1.0
DefaultDirName={pf}\YourAppName
DefaultGroupName=YourAppName
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Path\To\YourApp\*"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\YourApp.exe"
Name: "{commondesktop}\YourAppName"; Filename: "{app}\YourApp.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YourApp.exe"; Description: "{cm:LaunchProgram,YourAppName}"; Flags: nowait postinstall skipifsilent
```

#### PASSO 4: COMPILAR O SCRIPT:
1. **Compilar**: Com o script aberto no Inno Setup, clique no botão "Compile" na barra de ferramentas.
2. **Verificar**: O Inno Setup irá compilar o script e criar o arquivo de instalação na pasta especificada.
3. **Testar**: Execute o instalador gerado para testar e verificar se tudo está funcionando corretamente.

#### PASSO 5: PERSONALIZAÇÕES ADICIONAIS (OPCIONAL):
Você pode adicionar customizações ao seu instalador, como adicionar telas personalizadas, verificações de pré-requisitos, etc. A documentação oficial do Inno Setup tem exemplos e explicações detalhadas para essas funcionalidades.

#### RECURSOS ÚTEIS:
- **Documentação Oficial**: [Inno Setup Documentation](http://www.jrsoftware.org/isinfo.php)
- **Exemplos de Scripts**: O Inno Setup inclui exemplos de scripts que podem ser muito úteis para entender como implementar certas funcionalidades.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)

