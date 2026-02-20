# 🎓 APRENDA CONSTRUINDO: Validação de Data e Envio de Email

## ⚠️ COMO USAR ESTE GUIA

**IMPORTANTE:** Você vai digitar CADA linha do código. Não vou dar código pronto. Vou:
1. Explicar O QUÊ você está fazendo
2. Explicar POR QUÊ você está fazendo
3. Explicar COMO fazer
4. Você digita e testa

---

## 📚 LIÇÃO 1: O QUE É UMA DATA QUINZENAL?

Antes de programar, entenda o problema:

**Cenário:** Você precisa enviar relatórios a cada 15 dias:
- Data inicial: `20/02/2026` (primeiro envio)
- Próxima data: `06/03/2026` (20 + 15 dias)
- Próxima data: `21/03/2026` (06 + 15 dias)
- E assim vai...

**O problema:** Você precisa verificar se TODAY (a data de hoje) é UM DESSES DIAS de envio.
- Se hoje for `20/02/2026` → ENVIAR relatório ✅
- Se hoje for `21/02/2026` → NÃO enviar (não é dia quinzenal) ❌
- Se hoje for `06/03/2026` → ENVIAR relatório ✅

**A solução:** 
1. Definir uma data inicial de envio
2. Gerar uma lista de datas quinzenais
3. Verificar se a data atual está nessa lista

**Qual é a biblioteca certa?** 
→ `datetime` (padrão do Python) + `timedelta` (para adicionar dias)

---

## 🔧 LIÇÃO 2: Testando datetime.timedelta (você escreve)

### Passo 1: Abra um terminal Python
Execute no PowerShell:
```
python
```

### Passo 2: Teste como adicionar dias
Digite LINHA POR LINHA no terminal Python:

**Linha 1:**
```python
from datetime import datetime, timedelta
```

**Por que?**
- `from datetime import datetime, timedelta` = Importar duas coisas
- `datetime` = classe para trabalhar com data e hora
- `timedelta` = classe para trabalhar com diferenças de tempo (dias, horas, etc)

**Linha 2:** Criar uma data inicial
```python
data_inicial = datetime(2026, 2, 20)
```

**Por que?**
- `datetime(2026, 2, 20)` = criar um objeto de data
- 2026 = ano
- 2 = mês (fevereiro)
- 20 = dia
- Resultado: 20/02/2026

**Linha 3:** Adicionar 15 dias
```python
proxima_data = data_inicial + timedelta(days=15)
```

**Por que?**
- `timedelta(days=15)` = criar "15 dias"
- `data_inicial + ...` = somar a data com 15 dias
- Resultado: 06/03/2026

**Linha 4:** Ver o resultado
```python
print(proxima_data)
```

**Linha 5:** Adicionar mais 15 dias
```python
proxima_data_2 = proxima_data + timedelta(days=15)
print(proxima_data_2)
```

**Linha 6:** Pegar a data de hoje
```python
hoje = datetime.now()
print(hoje)
```

**Por que?**
- `datetime.now()` = pegar data e hora do computador AGORA
- Inclui a hora também (00:00:00 se for meia-noite)

**Linha 7:** Comparar datas
```python
hoje.date() == data_inicial.date()
```

**Por que?**
- `hoje.date()` = pegar só a data (sem a hora)
- `.date()` = transforma em apenas dia/mês/ano
- `==` = comparar se são iguais
- Resultado: `True` ou `False`

**Linha 8:** Saia do Python
```python
exit()
```

---

## 💡 ENTENDENDO COMO GERAR DATAS QUINZENAIS

Você precisa:
1. **Definir uma data inicial** (ex: 20/02/2026)
2. **Gerar as próximas datas** adicionando 15 dias repetidamente
3. **Guardar em uma lista**
4. **Verificar se a data atual está nessa lista**

**Código mental (não digite ainda):**
```
Data inicial: 20/02/2026
+ 15 dias = 06/03/2026
+ 15 dias = 21/03/2026
+ 15 dias = 05/04/2026
... e assim vai
```

---

## 👨‍💻 AGORA VOCÊ ESCREVE: Função que Gera Datas Quinzenais

Vamos construir do zero. Crie/abra o arquivo de utilitários de datas:
`src/utils/dates.py`

### Seção 1: Imports (VOCÊ DIGITA ISSO)

No arquivo `src/utils/dates.py` adicione:

**Linhas a digitar:**
```
from datetime import datetime, timedelta
```

**Por quê?**
- `datetime` = trabalhar com datas
- `timedelta` = adicionar/subtrair dias de uma data

---

### Seção 2: Função que GERA datas quinzenais (VOCÊ DIGITA ISSO)

Após os imports, adicione:

**Linha 1:**
```
def gerar_datas_quinzenais(data_inicial_str, quantidade_datas=12):
```

**O que é?**
- `data_inicial_str` = texto com a data inicial (ex: "20/02/2026")
- `quantidade_datas=12` = quantas datas quinzenais gerar (padrão: 12, ou seja, 6 meses)

**Linha 2 (indentado 4 espaços):**
```
    """Gera uma lista de datas a cada 15 dias."""
```

**Linha 3:**
```
    datas_quinzenais = []
```

**O que é?**
- `datas_quinzenais` = lista vazia para guardar as datas

**Linha 4:**
```
    data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
```

**O que é?**
- `strptime()` = converter texto ("20/02/2026") em data real
- `"%d/%m/%Y"` = o formato do texto (dia/mês/ano)

**Linha 5:**
```
    for i in range(quantidade_datas):
```

**O que é?**
- `for i in range(quantidade_datas)` = repetir de 0 até quantidade_datas-1
- `i` = número atual da repetição (0, 1, 2, 3...)

**Linha 6 (indentado 8 espaços):**
```
        data_atual = data_inicial + timedelta(days=15*i)
```
# CONTINUAR

**O que é?**
- `15*i` = 15 vezes o número da repetição
- Repetição 0: 15*0 = 0 dias (data inicial)
- Repetição 1: 15*1 = 15 dias (primeira data quinzenal)
- Repetição 2: 15*2 = 30 dias (segunda data quinzenal)
- Etc...

**Linha 7 (indentado 8 espaços):**
```
        datas_quinzenais.append(data_atual.date())
```

**O que é?**
- `append()` = adicionar à lista
- `.date()` = pegar só a data (sem hora)

**Linha 8 (indentado 4 espaços):**
```
    return datas_quinzenais
```

**O que é?**
- Retorna a lista de datas quinzenais

---

### Seção 3: Função que VALIDA se é uma data quinzenal (VOCÊ DIGITA ISSO)

**Linha 1:**
```
def validar_data_quinzenal(data_para_verificar_str, data_inicial_str):
```

**O que é?**
- `data_para_verificar_str` = a data que quer verificar (ex: hoje)
- `data_inicial_str` = a data inicial de referência

**Linha 2 (indentado 4 espaços):**
```
    """Verifica se a data é um dia de envio quinzenal."""
```

**Linha 3:**
```
    datas_quinzenais = gerar_datas_quinzenais(data_inicial_str, quantidade_datas=12)
```

**O que é?**
- Chamar a função anterior para gerar as datas quinzenais
- Armazena em `datas_quinzenais`

**Linha 4:**
```
    try:
```

**Linha 5 (indentado 8 espaços):**
```
        data_verificar = datetime.strptime(data_para_verificar_str, "%d/%m/%Y").date()
```

**O que é?**
- Converter o texto em data real
- `.date()` = pegar só a data, sem hora

**Linha 6 (indentado 8 espaços):**
```
        if data_verificar in datas_quinzenais:
```

**O que é?**
- `in` = verificar se está dentro da lista
- Se a data está na lista de datas quinzenais...

**Linha 7 (indentado 12 espaços):**
```
            return True
```

**O que é?**
- ...retorna True (é um dia de envio!)

**Linha 8 (indentado 8 espaços):**
```
        else:
```

**Linha 9 (indentado 12 espaços):**
```
            return False
```

**O que é?**
- ... senão retorna False (não é dia de envio)

**Linha 10 (indentado 4 espaços):**
```
    except ValueError:
```

**Linha 11 (indentado 8 espaços):**
```
        print("❌ Formato de data inválido!")
        return False
```

**O que é?**
- Se o formato da data for errado, avisa e retorna False

---

### Seção 4: Função para verificar se é HOJE (VOCÊ DIGITA ISSO)

Essa função é mais simples: se é hoje, você não precisa passar a data manualmente.

**Linha 1:**
```
def eh_dia_de_envio(data_inicial_str):
```

**O que é?**
- Recebe só a data inicial
- Vai verificar se hoje é um dia de envio

**Linha 2 (indentado 4 espaços):**
```
    """Verifica se hoje é um dia de envio quinzenal."""
```

**Linha 3:**
```
    hoje = datetime.now().date()
```

**O que é?**
- `datetime.now()` = pegar data e hora AGORA
- `.date()` = pegar só a data

**Linha 4:**
```
    datas_quinzenais = gerar_datas_quinzenais(data_inicial_str, quantidade_datas=12)
```

**Linha 5:**
```
    return hoje in datas_quinzenais
```

**O que é?**
- Verifica se hoje está na lista
- Retorna True ou False direto

---

---

## 📧 AGORA: FUNÇÃO DE ENVIO DE EMAIL

Vamos fazer do mesmo jeito.

### Seção 1: Imports (VOCÊ ADICIONA)

No topo do arquivo, após os imports anteriores:

```
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```

**Por quê cada um?**
- `smtplib` = conectar ao servidor de email (agência dos Correios)
- `MIMEText` = criar corpo de texto do email
- `MIMEMultipart` = criar um email com múltiplas partes (se precisar)

---

### Seção 2: Estrutura da Função (VOCÊ DIGITA)

```
def enviar_email(destinatario, assunto, mensagem):
    """Envia um email."""
```

**O que é?**
- A função recebe 3 parâmetros:
  - `destinatario` = para quem enviar
  - `assunto` = assunto do email
  - `mensagem` = corpo do email

---

### Seção 3: Carregando Configurações (VOCÊ DIGITA)

```
    email_remetente = os.getenv('EMAIL_REMETENTE')
    senha_email = os.getenv('SENHA_EMAIL')
    servidor_smtp = os.getenv('SERVIDOR_SMTP')
    porta_smtp = int(os.getenv('PORTA_SMTP', '587'))
```

**O que é?**
- `os.getenv('CHAVE')` = pegar valor do arquivo `.env`
- Exemplo: `.env` tem `EMAIL_REMETENTE=seu_email@gmail.com`
- Então `email_remetente` recebe esse valor
- `int(...)` = converter para número (porta é número)
- `'587'` = valor padrão se não encontrar

**Por quê usar .env?**
- Sua senha NÃO fica no código
- Se vazar o código, a senha não vaza
- Segurança!

---

### Seção 4: Validação (VOCÊ DIGITA)

```
    if not all([email_remetente, senha_email, servidor_smtp]):
        print("❌ Faltam configurações!")
        return False
```

**O que é?**
- `all([...])` = verifica se TODOS têm valor
- `not all(...)` = se NÃO tem todos os valores
- Se falta algo, avisa e sai (`return False`)

---

### Seção 5: Criar o Email (VOCÊ DIGITA)

```
    try:
        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain', 'utf-8'))
```

**O que é cada parte?**
- `msg = MIMEMultipart()` = criar um email vazio (um envelope)
- `msg['From']` = adicionar o campo "De:"
- `msg['To']` = adicionar o campo "Para:"
- `msg['Subject']` = adicionar o assunto
- `msg.attach(MIMEText(...))` = colar o corpo do email
  - `'plain'` = texto simples (não HTML)
  - `'utf-8'` = com suporte a acentos

---

### Seção 6: Enviar (VOCÊ DIGITA)

```
        with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
            server.starttls()
            server.login(email_remetente, senha_email)
            server.send_message(msg)
```

**O que é cada linha?**
- `with ... as server:` = conectar e lembrar de fechar depois
- `server.starttls()` = ativar criptografia (segurança)
- `server.login(...)` = fazer login (provar identidade)
- `server.send_message(msg)` = ENVIAR!

---

### Seção 7: Tratamento de Erros (VOCÊ DIGITA)

```
        print("✅ Email enviado!")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Email ou senha incorretos!")
        return False

    except smtplib.SMTPException as e:
        print(f"❌ Erro ao enviar: {e}")
        return False

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False
```

**Por quê?**
- `SMTPAuthenticationError` = senha errada
- `SMTPException` = problema no servidor de email
- `Exception` = qualquer outro erro

---

## 🔗 AGORA A INTEGRAÇÃO

Crie uma função que une tudo:

```
def processar_envio_quinzenal(data_inicial_str):
    """Se hoje é dia quinzenal, envia o relatório."""
    if eh_dia_de_envio(data_inicial_str):
        print(f"✅ Hoje é dia de envio!")
        return enviar_email(
            destinatario="seu_email@gmail.com",
            assunto="Relatório Quinzenal",
            mensagem="Segue anexo o relatório"
        )
    else:
        print(f"❌ Hoje não é dia de envio.Próximo envio: consultar a lista")
        return False
```

**O que faz?**
- Verifica se hoje é um dia quinzenal
- Se SIM → envia email
- Se NÃO → não faz nada

---

---

## ⚙️ CONFIGURAR O .env

1. Abra `config/.env`
2. Adicione (substitua pelos seus dados):

```
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_EMAIL=sua_senha_de_app
SERVIDOR_SMTP=smtp.gmail.com
PORTA_SMTP=587
```

**Nota:** Para Gmail, use "Senha de app": https://myaccount.google.com/apppasswords

---

## 🧪 TESTE FINAL

Quando terminar de digitar, teste no Python:

```python
datas = gerar_datas_quinzenais("20/02/2026", quantidade_datas=5)
from src.utils.dates import gerar_datas_quinzenais, eh_dia_de_envio
from src.scripts.modulo_a_sender import processar_envio_quinzenal

# Teste 1: Gerar datas quinzenais
datas = gerar_datas_quinzenais("20/02/2026", quantidade_datas=5)
print("Datas quinzenais:", datas)

# Teste 2: Verificar se hoje é um dia de envio
resultado = eh_dia_de_envio("20/02/2026")
print(f"Hoje é dia de envio? {resultado}")

# Teste 3: Executar tudo integrado (se hoje for dia de envio, envia email)
# resultado = processar_envio_quinzenal("20/02/2026")
# (descomente quando tiver o .env configurado)
```

**O que esperar:**
- Teste 1: Uma lista como `[datetime.date(2026, 2, 20), datetime.date(2026, 3, 6), ...]`
- Teste 2: `True` se hoje for 20/02 ou 06/03 etc., `False` caso contrário
- Teste 3: "Hoje é dia de envio!" se for uma data quinzenal

---

## 📋 CHECKLIST: VOCÊ COMPLETOU?

- [ ] Digitou a função `gerar_datas_quinzenais()`
- [ ] Digitou a função `validar_data_quinzenal()`
- [ ] Digitou a função `eh_dia_de_envio()`
- [ ] Digitou a função `enviar_email()`
- [ ] Digitou a função `processar_envio_quinzenal()`
- [ ] Configurou o arquivo `.env`
- [ ] Testou tudo no terminal Python
- [ ] Entendeu cada linha

**Se sim, parabéns!** Você construiu isso sozinho! 🎉

---

## ❓ PRÓXIMAS DÚVIDAS

**P: Como mudar a data inicial de envio?**
R: Mude o parâmetro:
```python
eh_dia_de_envio("01/03/2026")  # Começa no dia 1 de março
```

**P: Como gerar mais datas no futuro?**
R: Aumente o `quantidade_datas`:
```python
datas = gerar_datas_quinzenais("20/02/2026", quantidade_datas=24)  # 12 meses
```

**P: Como testar sem enviar email de verdade?**
R: Comente a linha `server.send_message(msg)` ou crie uma flag de teste.

**P: Posso visualizar quais são as próximas 5 datas de envio?**
R: Sim! Use:
```python
datas = gerar_datas_quinzenais("20/02/2026", quantidade_datas=5)
for i, data in enumerate(datas, 1):
    print(f"Envio {i}: {data.strftime('%d/%m/%Y')}")
```
