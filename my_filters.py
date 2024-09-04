from operator import truediv

from telebot import types
from telebot.custom_filters import (
    SimpleCustomFilter,
    AdvancedCustomFilter
)

import config

class IsUserBotAdmin(SimpleCustomFilter):
    key = 'is_bot_admin'

    def check(self, message: types.Message):
        return message.from_user.id in config.BOT_ADMIN_USER_IDS

class ContainsEntities(SimpleCustomFilter):
    key = 'has_entities'
    def check(self, message: types.Message):
        if message.entities:
            return True
        return False



class ContainsWordFilter(AdvancedCustomFilter):
    key = 'contains_word'

    def check(self, message, word) -> bool:
        text = message.text or message.caption
        if not text:
            return False

        return word in text.lower()



class ContainsOneOfTheWords(AdvancedCustomFilter):
    key='contains_one_of_the_words'

    def check(self, message, words):
        text = message.text or message.caption

        if not text:
            return False

        # for word in words:
        #     if word in text.lower():
        #         return True
        #
        # return False

        return any(word.lower() in text.lower() for word in words)