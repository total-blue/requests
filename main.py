import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text_from, text_to, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    text_from = open(text_from)
    text_to = open(text_to, 'w')
    params = {
        'key': API_KEY,
        'text': text_from,
        'lang': '{0}-{1}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    res = ''.join(json_['text'])
    text_to.write(res)
    text_to.close()



# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':

    texts_from = ['in/DE.txt', 'in/ES.txt', 'in/FR.txt']
    texts_to = ['out' + name[2:] for name in texts_from]
    langs = [name[3:5].lower() for name in texts_from]

    for i in range(len(texts_from)):
        translate_it(texts_from[i], texts_to[i], langs[i], 'ru')
