from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class CensorMiddleware(MiddlewareMixin):

    CENSORED_WORDS = ['мир', 'Мир', 'мИр', 'миР', 'МИр', 'мИР', 'МиР', 'МИР', 'world']

    def process_response(self, request, response):
        if response.streaming:
            return response
        for word in self.CENSORED_WORDS:
            response.content = response.content.replace(bytes(word, encoding='utf8'), bytes('*'*len(word), encoding='utf8'))
        return response