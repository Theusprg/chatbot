# 🟢 Automação de Envio de Mensagens pelo WhatsApp com Excel

Este script automatiza o envio de mensagens no WhatsApp usando uma planilha `.xlsx` com nomes e números de clientes.

---

## 🛠️ Dependências

Você precisa instalar os seguintes pacotes Python:

```bash
pip install openpyxl
pip install pyautogui
❗ O webbrowser e time são bibliotecas nativas do Python, não precisam ser instaladas.

📁 Estrutura da Planilha
Crie um arquivo .xlsx com pelo menos duas colunas:

Coluna A: Nome do cliente

Coluna B: Número do cliente (com DDD e sem símbolos, ex: 5599999999999)

✏️ Configuração do Código
Abra o arquivo .py e configure os seguintes pontos:

🔹 Linha 7 e Linha 9
Adicione:

O nome da empresa

O link de pagamento

python
Copiar
Editar
nome_empresa = "Minha Empresa"
link_pagamento = "https://linkdopagamento.com"
🔹 Linha 20
Coloque o caminho completo do arquivo .xlsx:

python
Copiar
Editar
caminho = r"C:\Users\SeuNome\Documents\clientes.xlsx"
⚠️ Atenção com o idioma do Excel:
Se o nome da aba estiver em português (como Planilha1) ou inglês (Sheet1), edite isso no código conforme necessário.

🔹 Linha 28
Ajuste o número da linha de início da leitura dos dados:

Se os nomes começarem na linha 2, o final da linha do código será:

python
Copiar
Editar
for linha in planilha.iter_rows(min_row=2, ...)
Se os dados começarem na linha 5, mude para min_row=5.

🖱️ PyAutoGUI e Imagem do Botão de Enviar
O pyautogui é usado para clicar automaticamente no botão de enviar do WhatsApp Web.

Você precisa fazer um print da imagem do botão de envio do WhatsApp (ícone de “seta” de enviar) e salvar como, por exemplo:

Copiar
Editar
enviar.png
Deixe essa imagem no mesmo diretório do seu script .py.

✅ Como usar
Instale as dependências.

Configure os dados no código.

Salve seu arquivo .xlsx com nomes e números válidos.

Execute o script e não mexa no mouse/teclado enquanto ele estiver rodando.

O script abrirá o WhatsApp Web e enviará as mensagens automaticamente.

📝 Observações
O WhatsApp Web precisa estar logado.

Evite mexer no computador durante a execução.

Teste com poucos contatos antes de rodar com todos.

💡 Exemplo de comando para iniciar:
bash
Copiar
Editar
python enviar_mensagens.py
