import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

#adcione o nome da empresa 
empresa = ''
#link do pagamento
link =''
dono =input("o whattsapp já está aberto no seu computador? \n").strip().lower()
#confirmação
if dono in ["sim", "s","sin","sin"]:
    print ("Ok não mexa no seu computador!")
    n = 15 
else:
    webbrowser.open('https://web.whatsapp.com/') #abrir o zap 
    sleep(20) #tempo de espera para o verigicar o qrcode 
    n = 8 
try:
    arquivo_clientes = openpyxl.load_workbook(r'BotDoZap\clientes.xlsx')#coloque o caminho do aquivo dentro das aspas
    pagina_clientes = arquivo_clientes[r'Planilha1']#abrir a planilha certa. E VERIFIQUE A LINGUA 
except:
    print("O arquivo não foi encontrado!")
    exit()
erros = []


for linha in pagina_clientes.iter_rows(min_row=2):#verificar onde começa o nomes validos
    try:
        nome = linha[0].value
        telefone = linha[1].value
        vencimento = linha[2].value
        verificando_data = vencimento.strftime('%d/%m/%Y') if vencimento else "DATA INDISPONÍVEL!"
        mensagem_cliente =( 
            f"Olá somos da {empresa} temos uma cobrança no nome de {nome}"
            f"na data de vencimento {vencimento.strftime('%d/%m/%Y')}, pedimos que o senhor pague o boleto nesse link "
            f"\n{link} \nObrigado pela atenção" 
        )
            #mensagem enviada para o usário
        link_zap= f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem_cliente)}"#link não mexer
        webbrowser.open(link_zap)
        sleep(n)
        
        seta = pyautogui.locateCenterOnScreen('./image/seta.png')#arquivo da seta
        sleep(4)
        if seta: 
        
            pyautogui.click(seta[0],seta[1])
            sleep(5)
            pyautogui.hotkey("ctrl","w")#fechar zap 
            sleep(5)
        else:
            print("Não foi possível encontrar a seta")

    except:#usuarios que não tiveram o envio da mensagem
        print(f"Esses usários não tiveram a mensagem enviada corretamente para {nome}")
if erros:
     with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
        print("Algumas mensagens falharam. Confira 'erros.csv'.")
print("mensagens enviadas")
#não mexer no Computador quando o codigo tiver sendo executado 

