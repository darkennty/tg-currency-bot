from telebot import formatting
from telebot import types

your_data = 'I got sum info \'bout you'

help_message = """
Доступные команды:
/start - Начало работы с ботом
/help - Помощь в использовании команд (это сообщение)
/curse - Услышать про себя правду
/single_joke - Случайная шутка
/two_part_joke - Случайная шутка с каламбуром
/jpy_to_rub 100 - Конвертировать 100 JPY (йен) в RUB (рубль)
/convert 100 usd JPY - Конвертировать 100 USD (доллар) в JPY (йен)
/convert 100 eur - Конвертировать 100 EUR (евро) в RUB (рубль)
/set_currency rub - Установить RUB (рубли) как основную для конвертации валюту
"""

jpy_to_rub_convert_how_to = formatting.format_text(
    'Укажите аргумент для конвертации, например:',
    formatting.hcode('/jpy_to_rub 100')
)

convert_how_to = formatting.format_text(
    'Укажите аргументы для конвертации, например:',
    formatting.hcode('/convert 100 usd JPY'),
    formatting.hcode('/convert 100 eur')
)

error_fetching_currencies_text = 'Something went wrong, sorry... Try again later!'
error_no_such_currency = 'Currency "{currency}" not found. Check your input and try again.'

def format_message_content_currency_convertion(
    from_curr: str,
    to_curr: str,
    amount_str,
    result_amount_str,
):
    content = types.InputTextMessageContent(
        message_text=formatting.format_text(
            f"{formatting.hcode(amount_str)} {from_curr} в {to_curr}",
            formatting.hcode(result_amount_str)
        ),
        parse_mode='HTML',
    )
    return content

def format_content_to_result_article(
    from_currency: str,
    to_currency: str,
    amount,
    result_amount,
):
    from_curr = from_currency.upper()
    to_curr = to_currency.upper()
    amount_str = f"{amount:,}"
    result_amount_str = f"{result_amount:,.2f}"
    content = format_message_content_currency_convertion(from_curr=from_curr, to_curr=to_curr, amount_str=amount_str, result_amount_str=result_amount_str)
    result = types.InlineQueryResultArticle(
        id=f"{from_currency}-{to_curr}-{amount_str}",
        title=f"{result_amount_str} {to_curr}",
        description=f"{amount_str} {from_curr} = {result_amount_str} {to_curr}",
        input_message_content=content,
    )
    return result


def format_currency_message(from_amount, to_amount, currency_from, currency_to):
    return formatting.format_text(
        formatting.hcode(f"{from_amount:,}"),
        f'{currency_from.upper()} ~',
        formatting.hcode(f"{to_amount:,.2f}"),
        f'{currency_to.upper()}',
        separator=' '
    )

set_currency_help_text = formatting.format_text(
    'Пожалуйста, укажите основную валюту, например: ',
    formatting.hcode('/set_currency rub')
)

set_my_currency_success_message = 'Валюта {currency} установлена как валюта по умолчанию.'


md = """
*bold \*text*
_italic \_text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=552685235)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
# pre-formatted fixed-width code block written in the Python programming language
@bot.message_handler(commands=['md'])
def send_markdown_message(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.md,
        parse_mode='MarkdownV2'
    )
```
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity
>Expandable block quotation continued
>Hidden by default part of the expandable block quotation started
>Expandable block quotation continued
>The last line of the expandable block quotation with the expandability mark||
"""

html_text = """
<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=552685235">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python"># pre-formatted fixed-width code block written in the Python programming language

@bot.message_handler(commands=['html'])
def send_html_message(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.html_text,
        parse_mode='HTML',
    )
</code></pre>
<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>
"""