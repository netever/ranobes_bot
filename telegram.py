import telebot
import ranobes

token = ''
ranobe_page = {}


def listener(messages):
    for message in messages:
        if message.content_type == 'text':
            if message.text == '/next':
                if str(message.chat.id) in ranobe_page:
                    url = ranobes.main(ranobe_page[str(message.chat.id)], 'next')
                    ranobe_page[str(message.chat.id)] = url
                    text = ranobes.main(url)
                    if len(text) > 4096:
                        for x in range(0, len(text), 4096):
                            bot.send_message(message.chat.id, text[x:x+4096])
                        else:
                            bot.send_message(message.chat.id, text)
                else:
                    bot.send_message(message.chat.id, 'Для начала укажите ссылку на нужную страницу произведения')
            
            elif message.text == '/prev':
                if str(message.chat.id) in ranobe_page:
                    url = ranobes.main(ranobe_page[str(message.chat.id)], 'prev')
                    ranobe_page[str(message.chat.id)] = url
                    text = ranobes.main(url)
                    if len(text) > 4096:
                        for x in range(0, len(text), 4096):
                            bot.send_message(message.chat.id, text[x:x+4096])
                        else:
                            bot.send_message(message.chat.id, text)
                else:
                    bot.send_message(message.chat.id, 'Для начала укажите ссылку на нужную страницу произведения')
            
            elif message.text == '/exit':
                if str(message.chat.id) in ranobe_page:
                    bot.send_message(message.chat.id, 'Выход успешно выполнен, ваша текущая страница: \n' + ranobe_page[str(message.chat.id)])
                    del ranobe_page[str(message.chat.id)]
                else:
                    bot.send_message(message.chat.id, 'Вы пока ничего не читаете')

            elif message.text == '/info':
                if str(message.chat.id) in ranobe_page:
                    bot.send_message(message.chat.id, 'Ваша текущая страница: \n' + ranobe_page[str(message.chat.id)])
                else:
                    bot.send_message(message.chat.id, 'Вы пока ничего не читаете')
                

            else:
                text = ranobes.main(message.text)
                ranobe_page[str(message.chat.id)] = message.text
                if len(text) > 4096:
                    for x in range(0, len(text), 4096):
                        bot.send_message(message.chat.id, text[x:x+4096])
                    else:
                        bot.send_message(message.chat.id, text)


bot = telebot.TeleBot(token)
bot.set_update_listener(listener)
bot.polling(none_stop=True, interval=0)