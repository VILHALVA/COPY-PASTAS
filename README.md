# COPY PASTAS
🎈COPIE O NOME DE TODOS OS DIRETÓRIOS E SUBDIRETÓRIOS.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O aplicativo "COPY PASTAS" é uma ferramenta simples e intuitiva criada com a biblioteca Tkinter em Python para listar e gerenciar caminhos de diretórios e subdiretórios. A principal funcionalidade é listar os caminhos dos diretórios de um caminho raiz selecionado e exibi-los de forma organizada, permitindo fácil cópia desses caminhos para a área de transferência.

## FUNCIONALIDADES:
1. **Selecionar Diretório**:
   - **Botão "SELECIONAR"**: Abre uma janela de diálogo para que o usuário selecione o diretório base do qual deseja listar os subdiretórios. O caminho do diretório selecionado é exibido em um campo de entrada de texto.

2. **Gerar Lista de Diretórios**:
   - **Botão "GERAR"**: Após a seleção do diretório, este botão processa a estrutura de diretórios e subdiretórios a partir do diretório selecionado. A aplicação lista apenas os caminhos completos dos subdiretórios e os diretórios que não possuem subdiretórios.
   - **Durante a Geração:** O aplicativo desconsidera a pasta `System Volume Information` e ignora acentos nos nomes dos diretórios.

3. **Copiar para a Área de Transferência**:
   - **Botão "COPIAR"**: Copia a lista formatada de caminhos de diretórios que foi gerada para a área de transferência do sistema operacional, permitindo fácil colagem em outros aplicativos.

4. **Limpar Texto**:
   - **Botão "LIMPAR"**: Limpa o conteúdo da área de texto onde os caminhos dos diretórios são exibidos.

## POR QUE CRIEI ESTE APP?
Após usar o [DRIVESORT](https://www.anerty.net/software/file/DriveSort/) para manter a ordem dos diretórios e subdiretórios do meu PC em sistemas embarcados, percebi a necessidade de criar um novo aplicativo que armazenasse e listasse os nomes desses diretórios em ordem.

Eu utilizo meus pendrives em diversos sistemas embarcados, como caixas de som e DVDs, que geralmente não têm tela, apenas saídas de áudio. Isso tornava cansativo ter que adivinhar ou memorizar o número dos diretórios de cada álbum.

Com este aplicativo, agora posso facilmente localizar o número do álbum que desejo acessar no sistema embarcado, tornando o processo rápido e prático.

## COMO USAR?
1. **Inicie o Aplicativo**:
   - Para executar o script Python, navegue até o diretório `./CODIGO`, e execute o comando:
   ```bash
   python CODIGO.py
   ```

2. **Selecione o Diretório**:
   - Clique no botão "SELECIONAR" para abrir uma janela de seleção de diretório. Navegue até o diretório base desejado e selecione-o. O caminho selecionado aparecerá no campo de entrada de texto.

3. **Gere a Lista de Diretórios**:
   - Clique no botão "GERAR" para processar o diretório selecionado. O aplicativo percorrerá todos os subdiretórios e exibirá uma lista numerada no campo de texto principal. Cada linha representará um caminho completo dos subdiretórios.

4. **Copie a Lista**:
   - Após a geração da lista, clique no botão "COPIAR" para copiar o conteúdo da área de texto para a área de transferência. Isso permitirá que você cole os caminhos em outro aplicativo ou documento.

5. **Limpe o Texto**:
   - Se precisar começar de novo ou simplesmente limpar a área de texto, clique no botão "LIMPAR".

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO BASEADO NO "COPY NAME"](https://github.com/VILHALVA/COPY-NAME)
- [PROJETO FEITO PELO VILHALVA](https://github.com/VILHALVA)

