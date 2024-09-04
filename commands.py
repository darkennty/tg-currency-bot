from telebot.types import BotCommand

default_commands = [
    BotCommand('start', 'Начало работы'),
    BotCommand('help', 'Помощь в использовании команд'),
    BotCommand('curse', 'Услышать про себя правду'),
    BotCommand('single_joke', 'Случайная шутка'),
    BotCommand('two_part_joke', 'Случайная шутка с каламбуром'),
    BotCommand('jpy_to_rub', 'Конвертировать валюту из JPY (йены) в RUB (рубли)'),
    BotCommand('convert', 'Конвертировать любую указанную валюту'),
    BotCommand('set_currency', 'Установить основную для конвертации валюту'),
]