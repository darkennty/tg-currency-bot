from io import StringIO
import random
from telebot import TeleBot
from telebot import types
from telebot import custom_filters
from telebot import formatting
from telebot import util

import config
import jokes
import messages
import my_filters
import currencies
from commands import default_commands
from currencies import default_currency_key

bot = TeleBot(config.BOT_TOKEN)
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.ForwardFilter())
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(my_filters.IsUserBotAdmin())
bot.add_custom_filter(my_filters.ContainsWordFilter())
bot.add_custom_filter(my_filters.ContainsEntities())
bot.add_custom_filter(my_filters.ContainsOneOfTheWords())
# bot.add_custom_filter(custom_filters.TextContainsFilter())

CURSES = [
    "OMG, you're such a bitch",
    "STFU lil' nigga",
    "You gotta kill yourself",
    "Your momma is so fat, her AirPods are located in two different countries",
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '*OK now*\.\.\. _hold on\.\.\._ ||nigga||',
        parse_mode='MarkdownV2',
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id,
        messages.help_message,
    )

@bot.message_handler(commands=['curse'])
def send_random_curse(message):
    bot.send_message(
        message.chat.id,
        formatting.hcite(random.choice(CURSES)),
        parse_mode='HTML'
    )

@bot.message_handler(commands=['single_joke'])
def send_random_single_joke(message):
    bot.send_message(
        message.chat.id,
        formatting.hcite(jokes.get_joke('single')),
        parse_mode='HTML'
    )

@bot.message_handler(commands=['two_part_joke'])
def send_random_two_part_joke(message):
    setup, delivery = jokes.get_joke('twopart')
    joke = formatting.format_text(
        formatting.escape_html(setup),
        formatting.hspoiler(delivery)
    )
    bot.send_message(
        message.chat.id,
        # formatting.hcite(joke),
        joke,
        parse_mode='HTML'
    )

@bot.message_handler(commands=['gimme_doc'])
def send_curry_as_doc(message: types.Message):
    photo_file = types.InputFile("C:\\Users\\victus\\OneDrive\\Pictures\\1200x0.jpg")
    bot.send_document(
        message.chat.id,
        document=photo_file,
    )

@bot.message_handler(commands=['file'])
def send_text_file(message: types.Message):
    file_doc = types.InputFile('config.py')
    bot.send_document(
        message.chat.id,
        document=file_doc
    )

@bot.message_handler(commands=['text'], is_forwarded=True)
def handle_forwarded_text_command(message: types.Message):
    bot.send_message(
        message.chat.id,
        text="Do not forward commands!",
    )

@bot.message_handler(commands=['text'])
def send_generated_text_file(message: types.Message):
    file = StringIO()
    file.write("Hello World!\n")
    file.write("Your random number: ")
    file.write(str(random.randint(1, 100)))
    file.seek(0)
    file_text_doc = types.InputFile(file)
    bot.send_document(
        chat_id=message.chat.id,
        document=file_text_doc,
        visible_file_name="my_text.txt",
    )

@bot.message_handler(commands=['gimme_steph_file'])
def send_curry_from_disk(message: types.Message):
    photo_file = types.InputFile("C:\\Users\\victus\\OneDrive\\Pictures\\1200x0.jpg")
    bot.send_photo(
        message.chat.id,
        photo=photo_file
    )

@bot.message_handler(commands=['gimme'])
def send_curry_using_id(message: types.Message):
    bot.send_photo(
        message.chat.id,
        photo=config.PHOTO_FROM_DISK_ID
    )

@bot.message_handler(commands=['curry'])
def send_curry_photo(message: types.Message):
    bot.send_photo(message.chat.id, config.PHOTO_CURRY, reply_to_message_id=message.id)

@bot.message_handler(text=custom_filters.TextFilter(
    contains=["weather"],
    ignore_case=True
))
def handle_weather_request(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=formatting.mbold('windy'),
        parse_mode='MarkdownV2',
    )


@bot.message_handler(commands=['secret'], is_bot_admin=True)
def handle_admin_secret_request(message: types.Message):
    bot.send_message(
        message.chat.id,
        'aboba'
    )

@bot.message_handler(commands=['md'])
def send_markdown_message(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.md,
        parse_mode='MarkdownV2'
    )

@bot.message_handler(commands=['html'])
def send_html_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.html_text,
        parse_mode='HTML',
    )

@bot.message_handler(commands=['chat_id'])
def handle_chat_id(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="<code>" + str(message.chat.id) + "</code> \n",
        parse_mode='HTML',
    )

@bot.message_handler(commands=['cat'])
def send_pussy_pic(message: types.Message):
    bot.send_photo(
        chat_id=message.chat.id,
        photo=config.PHOTO_CAT
    )

@bot.message_handler(commands=['cat_file'])
def send_pussy_file(message: types.Message):
    photo_file = types.InputFile(config.PHOTO_CAT_DISK)
    bot.send_document(
        message.chat.id,
        photo_file
    )

@bot.message_handler(commands=['me'])
def send_user_info(message: types.Message):
    file = StringIO()
    file.write("Your username: " + message.from_user.username + "\n")
    file.write("Your first name: " + message.from_user.first_name + "\n")
    file.write("Your last name: " + message.from_user.last_name + "\n")
    file.write("Your id: " + str(message.from_user.id))
    file.seek(0)
    file_text_doc = types.InputFile(file)
    bot.send_document(
        chat_id=message.chat.id,
        document=file_text_doc,
        visible_file_name="your_info.txt",
        caption=messages.your_data
    )













@bot.message_handler(commands=['jpy_to_rub'])
def convert_jpy_to_rub(message: types.Message):
    arguments = util.extract_arguments(message.text)
    if not arguments:
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.jpy_to_rub_convert_how_to,
            parse_mode='HTML'
        )
        return

    if not arguments.isdigit():
        convert_invalid_argument = formatting.format_text(
            'Неправильный аргумент:',
            formatting.hcode(arguments),
            '\n',
            messages.jpy_to_rub_convert_how_to,
            separator=' '
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=convert_invalid_argument,
            parse_mode='HTML'
        )
        return

    jpy_amount = int(arguments)
    rub_amount = jpy_amount * currencies.get_currency_ratio('jpy', 'rub')
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.format_currency_message(jpy_amount, rub_amount, 'jpy', 'rub'),
        parse_mode='HTML'
    )


@bot.message_handler(commands=['convert'], regexp='/convert [1-9][0-9]*( )+[a-zA-z]+(( )+[a-zA-z]+)?')
def convert_currency_message(message: types.Message):
    arguments = util.extract_arguments(message.text)
    amount, _, currency = arguments.partition(" ")

    default_currency = "RUB"
    user_data = bot.current_states.get_data(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )
    if user_data and default_currency_key in user_data:
        default_currency = user_data[default_currency_key]

    currency = currency.strip()
    currency_from, currency_to = currencies.get_correct_currencies(
        currency,
        default_to=default_currency,
    )
    ratio = currencies.get_currency_ratio(
        currency_from=currency_from,
        currency_to=currency_to,
    )
    if ratio == currencies.ERROR_FETCHING_VALUE:
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_fetching_currencies_text,
        )
        return
    if ratio in {
        currencies.ERROR_CURRENCY_FROM_NOT_FOUND,
        currencies.ERROR_CURRENCY_TO_NOT_FOUND,
    }:
        bad_currency = currency_from
        if ratio == currencies.ERROR_CURRENCY_TO_NOT_FOUND:
            bad_currency = currency_to
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_no_such_currency.format(
                currency=formatting.hcode(bad_currency),
            ),
            parse_mode="HTML",
        )
        return

    from_amount = int(amount)
    result_amount = from_amount * ratio
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.format_currency_message(
            from_amount=from_amount,
            to_amount=result_amount,
            currency_from=currency_from,
            currency_to=currency_to,
        ),
        parse_mode="HTML",
    )

@bot.message_handler(commands=['convert'])
def convert_currency_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.convert_how_to,
        parse_mode='HTML',
    )

def has_no_arguments(message: types.Message):
    return not util.extract_arguments(message.text)

@bot.message_handler(commands=['set_currency'], func=has_no_arguments)
def handle_set_currency_with_no_args(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.set_currency_help_text,
        parse_mode='HTML',
    )

@bot.message_handler(commands=["set_currency"])
def set_default_currency(message: types.Message):
    currency: str = util.extract_arguments(message.text)
    if not currencies.is_currency_available(currency.strip()):
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.error_no_such_currency.format(currency=formatting.hcode(currency)),
            parse_mode="HTML",
        )
        return

    if bot.get_state(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
    ) is None:
        bot.set_state(
            user_id=message.from_user.id,
            chat_id=message.chat.id,
            state=0,
        )

    bot.add_data(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        default_currency=currency,
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=messages.set_my_currency_success_message.format(currency=formatting.hcode(currency)),
        parse_mode="HTML",
    )












@bot.message_handler(contains_one_of_the_words=['пока', 'бб'])
def send_lol(message: types.Message):
    bot.send_message(
        message.chat.id,
        '<i>Всё, пока!</i> <b>ПОКА!</b> <u>(...этО гОлОс... <tg-spoiler>ДЕТИ!</tg-spoiler>)</u>',
        parse_mode='HTML'
    )

@bot.message_handler(has_entities=True)
def send_lol(message: types.Message):

    our_entities = {formatting.hcode(entity.type) for entity in message.entities}
    text = formatting.format_text(
        message.text,
        f"Entities: {', '.join(our_entities)}",
        separator='\n\n'
    )

    bot.send_message(
        message.chat.id,
        text,
        entities=message.entities,
    )

# def is_curry_in_caption(message: types.Message):
#     return message.caption and 'curry' in message.caption.lower()

@bot.message_handler(content_types=['photo'], contains_word='curry')
    # text=custom_filters.TextFilter(
    # contains=["curry"],
    # ignore_case=True
#)) func=is_curry_in_caption
def handle_photo_with_curry_caption(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Look at *_Curry_* man\. So inspirational\!",
        reply_to_message_id=message.id,
        parse_mode='MarkdownV2',
    )

@bot.message_handler(content_types=['photo'])
def handle_photo(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    caption_text = 'What a photo!'
    if message.caption:
        caption_text += " Подпись:\n" + message.caption
    bot.send_photo(
        message.chat.id,
        photo_file_id,
        reply_to_message_id=message.id,
        caption=caption_text,
    )

@bot.message_handler(is_reply=False, content_types=['sticker'])
def handle_sticker(message: types.Message):
    bot.send_sticker(
        chat_id=message.chat.id,
        sticker=message.sticker.file_id,
        reply_to_message_id=message.id
    )


def is_hi_in_text(message: types.Message):
    return message.text and ('hi' in message.text.lower() or 'hello' in message.text.lower())

@bot.message_handler(func=is_hi_in_text)
def handle_hi_message_text(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Word up, coolio!'
    )

content_type_to_ru = {
    'text': '<текст>',
    'photo': 'фото',
    'sticker': 'стикер',
    'document': 'документ',
}

@bot.message_handler(is_reply=True)
def handle_reply(message: types.Message):
    message_type = message.reply_to_message.content_type
    if message_type in content_type_to_ru:
        message_type = content_type_to_ru[message_type]
    bot.send_message(
        message.chat.id,
        "<i>Your</i> <b>reply</b> <u>type</u>: <tg-spoiler>" + formatting.escape_html(message_type) + "</tg-spoiler>",
        #f"<i>Your</i> <b>reply</b> <u>type</u>: <tg-spoiler>{formatting.escape_html(message_type)}</tg-spoiler>",
        parse_mode='HTML',
    )

@bot.message_handler(contains_word='проверка')
def copy_incoming_message(message: types.Message):
    # if message.entities:
    #     print("message entities: \n")
    #     for entity in message.entities:
    #         print(entity)
    bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.id,
    )


@bot.message_handler()
def send_echo_message(message: types.Message):
    answer = message.text

    bot.send_message(
        message.chat.id,
        formatting.escape_markdown(answer) + ', __niggggga__',
        entities=message.entities,
        parse_mode='MarkdownV2'
    )

def is_query_only_digits(query: types.InlineQuery):
    if query and query.query:
        return query.query.isdigit()
    return False

@bot.inline_handler(func=is_query_only_digits)
def handle_convert_inline_query(query: types.InlineQuery):
    amount = int(query.query)

    target_currencies = currencies.FAVOURITE_CURRENCIES
    from_currency = currencies.DEFAULT_LOCAL_CURRENCY

    ratios = currencies.get_currencies_ratios(from_currency, target_currencies)
    results=[]

    for currency_rate, currency_name in zip(
        ratios,
        target_currencies,
    ):
        total_amount = amount * currency_rate
        result = messages.format_content_to_result_article(
            from_currency=from_currency,
            to_currency=currency_name,
            amount=amount,
            result_amount=total_amount
        )
        results.append(result)

    bot.answer_inline_query(
        inline_query_id=query.id,
        results=results,
        cache_time=10
    )






def any_query(query: types.InlineQuery):
    print(query)
    return True

@bot.inline_handler(func=any_query)
def handle_any_inline_query(query: types.InlineQuery):
    content = types.InputTextMessageContent(
        message_text=formatting.format_text(
            formatting.hbold("Сообщение из inline-запроса"),
            f"id inline-запроса: {formatting.hcode(query.id)}",
        ),
        parse_mode='HTML',
    )
    result = types.InlineQueryResultArticle(
        id="default-answer",
        title="Inline Message",
        description='Info about query and answer',
        input_message_content=content
    )
    results=[
        result,
    ]
    bot.answer_inline_query(
        inline_query_id=query.id,
        results=results,
        cache_time=10,
    )



if __name__ == "__main__":
    bot.enable_saving_states()
    bot.set_my_commands(default_commands)
    bot.infinity_polling(skip_pending=True, allowed_updates=[])
