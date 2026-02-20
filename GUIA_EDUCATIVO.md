# 📚 GUIA EDUCATIVO: VALIDAÇÃO DE DATA E ENVIO DE EMAIL

## 🎯 Objetivo Geral
Você vai aprender a:
1. **Validar datas** - Verificar se uma data é real/válida
2. **Enviar emails** - Usar Python para enviar emails automáticos
3. **Integrar as duas** - Só enviar email se a data for válida

---

## 💡 PARTE 1: VALIDAÇÃO DE DATA

### Por que validar uma data?
Quando você recebe uma data como texto (ex: "20/02/2026"), você precisa verificar se:
- **É uma data real**: Como fevereiro tem 28 dias, "32/02/2026" é INVÁLIDA
- **Está no formato correto**: "20/02/2026" vs "2026-02-20" são formatos diferentes
- **Pode ser processada**: Se não validar, seu programa pode quebrar

### Como funciona a função `validar_data()`

```python
from datetime import datetime
```
**O que é?** Importar a biblioteca `datetime` - ela trabalha com datas no Python
**Por que?** Porque não dá para validar data com string normal, precisa de uma ferramenta específica

```python
formatos_aceitos = [
    '%Y-%m-%d',      # 2026-02-20
    '%d/%m/%Y',      # 20/02/2026
    '%d-%m-%Y',      # 20-02-2026
]
```
**O que é?** Uma lista dos formatos de data que você aceita
**Por que?** Porque diferentes pessoas/sistemas usam diferentes formatos
**Como ler:** 
- `%Y` = Ano com 4 dígitos (2026)
- `%m` = Mês com 2 dígitos (02)
- `%d` = Dia com 2 dígitos (20)

```python
for formato in formatos_aceitos:
```
**O que é?** Um loop que percorre cada formato da lista
**Por que?** Porque você quer tentar cada formato até encontrar um que funcione

```python
datetime.strptime(data_string, formato)
```
**O que é?** Tentar converter a string (texto) para um objeto de data
**Como funciona:**
- `strptime` = "string parse time" = converter texto em tempo/data
- Se conseguir converter = data é válida
- Se der erro = data não é válida nesse formato, tenta o próximo

```python
return True
```
**O que é?** Retorna True (verdadeiro) - a data é válida!
**Por que?** Para esse código sair da função e avisar "deu certo"

```python
except ValueError:
    continue
```
**O que é?** Se houver erro (ValueError), pula para o próximo formato
**Por que?** A data pode ser válida em outro formato, então não desiste

```python
return False
```
**O que é?** Se nenhum formato funcionou, retorna False
**Por que?** Para avisar que a data é inválida

---

## 📧 PARTE 2: ENVIO DE EMAIL

### Por que é complicado enviar email?

Enviar email é como enviar uma carta:
1. **Precisa de um servidor** (agência dos Correios)
2. **Precisa de autenticação** (CPF/documento)
3. **Precisa de um endereço correto** (CEP/email)
4. **Precisa do conteúdo bonitinho** (Envelope com as regras)

### Imports Necessários

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

**O que são?**
- `smtplib` = Biblioteca para conectar ao servidor SMTP
- `MIMEText` = Para criar o corpo do email em texto
- `MIMEMultipart` = Para criar um email que pode ter múltiplas partes (texto, anexos, etc)

**Por que?** Porque o Python precisa essas ferramentas para lidar com emails

### Carregando Configurações

```python
email_remetente = os.getenv('EMAIL_REMETENTE')
senha_email = os.getenv('SENHA_EMAIL')
servidor_smtp = os.getenv('SERVIDOR_SMTP')
porta_smtp = int(os.getenv('PORTA_SMTP', '587'))
```

**O que é?** Pegar informações do arquivo `.env`
**Por que?** Para não deixar a senha no código! Isso é uma prática de segurança

**`os.getenv()`** = Pega uma variável de ambiente
**`int(...)`** = Converte para número inteiro (a porta precisa ser número, não texto)
**`'587'`** = Valor padrão se não encontrar a variável

### Validação das Configurações

```python
if not all([email_remetente, senha_email, servidor_smtp]):
    print("❌ Erro: Faltam configurações de email no arquivo .env")
    return False
```

**O que é?** Verificar se todas as configurações foram carregadas
**`all([...])`** = Verifica se TODOS os itens da lista têm valor (não são vazios)
**Por que?** Se falta alguma configuração, o email não pode ser enviado

### Criar o Email

```python
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = destinatario
msg['Subject'] = assunto
msg.attach(MIMEText(mensagem, 'plain', 'utf-8'))
```

**O que é?** Construir a estrutura do email como se fosse um envelope

**Explicação de cada linha:**
1. `msg = MIMEMultipart()` = Criar um objeto email vazio
2. `msg['From']` = Adicionar o campo "De:" 
3. `msg['To']` = Adicionar o campo "Para:"
4. `msg['Subject']` = Adicionar o assunto
5. `msg.attach(...)` = Cola o corpo do email no envelope
   - `MIMEText(...)` = Cria o corpo em texto
   - `'plain'` = Texto simples (sem HTML)
   - `'utf-8'` = Codificação com acentos/caracteres especiais

### Conectar ao Servidor

```python
with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
    server.starttls()
    server.login(email_remetente, senha_email)
    server.send_message(msg)
```

**Linha por linha:**
1. `with ... as server:` = Conectar ao servidor e garantir que feche depois
   - `with` = "use isso, mas limpe quando terminar"
   - `smtplib.SMTP(...)` = Conectar ao servidor SMTP

2. `server.starttls()` = Começar criptografia (deixa seguro)
   - TLS = Transport Layer Security
   - Como colocar o envelope em um saco de segurança

3. `server.login(...)` = Fazer login (provar que você é quem diz ser)
   - Passa email e senha para autenticar

4. `server.send_message(msg)` = Enviar o email
   - Equivalente a colocar na carta na caixa de correios

### Tratamento de Erros

```python
except smtplib.SMTPAuthenticationError:
    print("❌ Erro: Email ou senha incorretos")
    return False
```

**O que é?** Se der erro de autenticação (senha errada)
**`except`** = "se acontecer um erro específico"

```python
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
    return False
```

**O que é?** Se der qualquer outro erro que não foi previsto
**`Exception`** = Qualquer tipo de erro Python
**`as e`** = Guardar o erro em uma variável chamada `e`
**Por que?** Para poder imprimir a mensagem de erro

---

## 🔗 PARTE 3: INTEGRAÇÃO (Data → Email)

```python
if validar_data(data):
    print(f"✅ Data '{data}' é válida!")
    resultado = enviar_email(...)
    return resultado
else:
    print(f"❌ Data '{data}' é inválida!")
    return False
```

**Como funciona:**
1. Primeiro valida a data
2. **SE válida** → Envia o email
3. **SE inválida** → Não envia e avisa

Isso garante que você só processe datas reais!

---

## 🚀 COMO USAR PRATICAMENTE

### Passo 1: Configurar o `.env`
1. Copie o arquivo `.env.exemplo` e renomeie para `.env`
2. Preencha com suas credenciais reais

### Passo 2: Usar no seu código
```python
# Exemplo simples
processar_com_validacao_data(
    data="2026-02-20",
    destinatario="pessoa@email.com",
    assunto="Notificação",
    mensagem="Olá! Este é um email automático."
)
```

### Passo 3: Com dados do DataFrame
```python
# Se quiser enviar para cada linha do seu CSV
for index, row in df.iterrows():
    data = row['coluna_data']
    email = row['coluna_email']
    
    processar_com_validacao_data(
        data=data,
        destinatario=email,
        assunto="Seu Assunto",
        mensagem=f"Olá {row['nome']}, mensagem automática"
    )
```

---

## 🎓 CONCEITOS IMPORTANTES QUE VOCÊ APRENDEU

| Conceito | O que é | Por que importa |
|----------|---------|-----------------|
| **datetime** | Ferramenta para trabalhar com datas | Validação de datas |
| **try/except** | Capturar erros sem quebrar | Programa não para com problemas |
| **SMTP** | Protocolo para envio de email | Padrão universal |
| **Variáveis de ambiente** | Dados guardados fora do código | Segurança (senhas) |
| **with statement** | Abre e fecha recursos automaticamente | Garante que tudo seja limpo |
| **return** | Sai da função e passa o resultado | Comunica sucesso/falha |

---

## ❓ DÚVIDAS COMUNS

**P: Posso usar minha senha normal do Gmail?**
R: Não recomendo. Use "Senha de app" (mais segura). Se usar senha normal, habilite "Acesso de apps menos seguros"

**P: Como adiciono anexos?**
R: Adicione depois de `msg.attach(MIMEText(...))`:
```python
from email.mime.base import MIMEBase
from email import encoders

part = MIMEBase('application', 'octet-stream')
part.set_payload(open('arquivo.pdf', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='arquivo.pdf')
msg.attach(part)
```

**P: Posso enviar HTML no lugar de texto?**
R: Sim! Mude `'plain'` para `'html'`:
```python
msg.attach(MIMEText(mensagem, 'html', 'utf-8'))
```

**P: E se eu quiser testar sem enviar de verdade?**
R: Comente a linha `server.send_message(msg)` ou crie um modo "debug"

---

## 📝 RESUMO FINAL

Você agora sabe:
✅ Validar datas com múltiplos formatos
✅ Enviar emails com autenticação
✅ Tratar erros sem quebrar o código
✅ Integrar validação com ações
✅ Usar variáveis de ambiente com segurança

**Próximos passos para praticar:**
1. Configure seu `.env` com dados reais
2. Teste a validação de data com vários exemplos
3. Teste o envio de email para seu próprio email
4. Integre com seus dados do DataFrame
5. Trate casos especiais (emails inválidos, datas nulas, etc)

Boa sorte! 🚀
