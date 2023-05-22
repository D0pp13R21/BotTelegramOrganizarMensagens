# Bot de Mensagens do Telegram

Este é um bot para o Telegram que organiza mensagens com base em códigos específicos e permite filtrá-las por período.

## Funcionalidades

- Permite adicionar mensagens com códigos específicos (01, 02, 03, 04 ou 05).
- Exibe uma tabela com opções de filtragem por período:
    - Último mês
    - Última semana
    - Último dia
    - Últimos 3 meses

## Pré-requisitos

- Python 3.x
- Biblioteca python-telegram-bot

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instale as dependências:

    pip install python-telegram-bot

## Utilização

1. Crie um novo bot no Telegram usando o BotFather e obtenha o token do bot.

2. Abra o arquivo bot_telegram.py e substitua 'SEU_TOKEN_AQUI' pelo token do seu bot.

3. Execute o arquivo bot_telegram.py:
    python bot_telegram.py

4. No Telegram, inicie uma conversa com o seu bot.

5. Digite o código da mensagem (01, 02, 03, 04 ou 05) seguido do conteúdo da mensagem para adicioná-la.

6. Use o comando /tabela para exibir a tabela com opções de filtragem por período.

7. Selecione o período desejado na tabela e a lista de mensagens será exibida.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.