# [ATUALIZAÇÕES:](./UPDATES.md#vers%C3%A3o-10---01122023)
## VERSÃO 1.5 - 16/09/2025:
* ✅Nesta atualização, os dois aplicativos foram integrados em uma única interface usando o recurso de **abas**, oferecendo uma navegação mais organizada entre diferentes funcionalidades. Além da aba `EXPLORADOR`, que preserva as funcionalidades do aplicativo original `COPY PASTAS`, foi adicionada a aba **“COMPARADOR”**, que permite identificar rapidamente quais pastas ou arquivos estão faltando entre dois diretórios selecionados.
* ✅**Sobre o COMPARADOR:**
  * 🔹Adicionado o botão **COPIAR** para enviar o resultado diretamente para a área de transferência.
  * 🔹Implementado um sistema de validação, onde os botões ficam **desabilitados** em determinados estados.
  * 🔹O aplicativo antigo **"COMPARADOR DE FILES"** foi apagado.
* ✅Ambas agora possuem cores mais escuras e harmoniosas.
* ✅A seção de **footer** foi removido de ambos.
---

## VERSÃO 1.4 - 09/06/2025:
* ✅Arquivos ocultos e de sistema são ignorados automaticamente durante o processo — mesmo que estejam visíveis no Explorador do Windows.
---

## VERSÃO 1.3 - 05/06/2025:
* ✅**Migração para `CustomTkinter`:** A interface foi atualizada para utilizar o *CustomTkinter*, uma versão moderna e estilizada do tkinter, trazendo um visual mais agradável, com suporte nativo a temas escuros, cantos arredondados e design responsivo.
* ✅**Interface Maximizada por Padrão:** Ao iniciar, a janela do aplicativo é exibida automaticamente em modo *maximizado* (zoom total).
* ✅**Notificação Toast ao Copiar:** O botão "COPIAR" agora exibe uma notificação *toast* (janela flutuante no estilo do Windows) para confirmar que o conteúdo foi copiado com sucesso para a área de transferência. Isso foi implementado com um sistema próprio usando CustomTkinter, dispensando bibliotecas externas como win10toast.
---

## VERSÃO 1.2 - 20/05/2025:
* ✅Adicionados botões de filtro por tipo (`MP3`, `TODOS`, `JSON`, `TXT`) e novos modos de listagem com contagens personalizadas por categoria.
* ✅O aplicativo "COPY NAME" (01/12/2023) foi apagado. 
---

## VERSÃO 1.1 - 04/09/2024:
* ✅**O APLICATIVO FOI LANÇADO OFICIALMENTE:** O aplicativo "COPY PASTAS" é uma ferramenta simples e intuitiva, criada com a biblioteca Tkinter em Python, para listar e gerenciar caminhos de diretórios e subdiretórios, exibindo a quantidade de arquivos .mp3 em cada pasta. Além disso, o aplicativo oferece estatísticas detalhadas sobre a quantidade de pastas, músicas e o espaço de armazenamento usado, livre e total do diretório selecionado. A principal funcionalidade é listar os caminhos dos diretórios de um caminho raiz selecionado e exibi-los de forma organizada, incluindo o número de músicas em cada diretório, permitindo fácil cópia desses caminhos para a área de transferência.
---

## VERSÃO 1.0 - 01/12/2023:
* ✅**PRECISEI CRIAR OUTRO APLICATIVO PARA DESKTOP:** Para que eu possa colocar mais de 200 músicas sugeridas dentro de uma array no buscador de BOAS MÚSICAS, precisei automatizar essa tarefa (Eu não ia escrever o nome de cada música na mão, né). Então eu automatizei essa tarefa chata: Criei um executável que você seleciona um diretório e ele salva o nome de todos os arquivos no campo (Funciona pra pastas também), depois só bastou copiar dentro da array do meu script.js de sugestão de músicas!
* ✅**Em `18/12/2023`, foram feitas algumas melhorias no aplicativo (1.0.1):**
  * 🔹Adição de um rodapé com meu nome e meu username do GitHub.
  * 🔹Refatoração e revisão do código para maior clareza e eficiência.
  * 🔹Inclusão do nome e do ícone oficial do aplicativo.
  * 🔹Alteração no parâmetro de compilação, eliminando a necessidade de o usuário ter pacotes do módulo `_internal` instalados no sistema. Agora, o aplicativo é totalmente autônomo.