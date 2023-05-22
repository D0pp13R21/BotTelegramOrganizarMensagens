import datetime
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Dicionário para armazenar as mensagens por código
messages = {
    '01': [],
    '02': [],
    '03': [],
    '04': [],
    '05': []
}

# Função para lidar com o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Bem-vindo ao seu bot de mensagens. Digite o código da mensagem (01, 02, 03, 04 ou 05) seguido do conteúdo da mensagem.")

# Função para lidar com as mensagens recebidas
def handle_message(update, context):
    text = update.message.text.strip()
    code = text[:2]
    content = text[2:].strip()

    if code in messages:
        messages[code].append(content)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Mensagem adicionada com sucesso!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Código inválido. Por favor, use um dos códigos permitidos (01, 02, 03, 04 ou 05).")

# Função para lidar com o comando /tabela
def show_table(update, context):
    keyboard = [['Último mês', 'Última semana'], ['Último dia', 'Últimos 3 meses']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Selecione o período:", reply_markup=reply_markup)

# Função para lidar com as opções da tabela
def handle_table_option(update, context):
    text = update.message.text.lower()
    chat_id = update.effective_chat.id

    if text == 'último mês':
        period = datetime.timedelta(days=30)
    elif text == 'última semana':
        period = datetime.timedelta(weeks=1)
    elif text == 'último dia':
        period = datetime.timedelta(days=1)
    elif text == 'últimos 3 meses':
        period = datetime.timedelta(days=90)
    else:
        context.bot.send_message(chat_id=chat_id, text="Opção inválida.")
        return

    now = datetime.datetime.now()
    filtered_messages = []

    for code, msgs in messages.items():
        filtered_msgs = [msg for msg in msgs if (now - msg.timestamp) <= period]
        filtered_messages.extend(filtered_msgs)

    if filtered_messages:
        table = '\n'.join(filtered_messages)
        context.bot.send_message(chat_id=chat_id, text=f"Tabela de mensagens:\n\n{table}")
    else:
        context.bot.send_message(chat_id=chat_id, text="Nenhuma mensagem encontrada para o período selecionado.")

    # Remove o teclado de opções
    reply_markup = ReplyKeyboardRemove()
    context.bot.send_message(chat_id=chat_id, text="Selecione outra opção:", reply_markup=reply_markup)

def main():
    # Inicializa o updater com o token do seu bot
    updater = Updater(token='SEU_TOKEN_AQUI', use_context=True)

    # Obtém o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Registra os handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CommandHandler('tabela', show_table))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_table_option))

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot em execução até pressionar Ctrl + C
    updater.idle()

if __name__ == '__main__':
    main()
