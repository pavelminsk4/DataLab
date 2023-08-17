from deep_translator import GoogleTranslator
import nltk


def translate_long_text(text, target):
    if len(text) >= 5000:
        sentences = nltk.tokenize.sent_tokenize(text)
        text = ''
        for sentence in sentences:
            text = text + GoogleTranslator(source='auto', target=target).translate(sentence)
    else:
        text = GoogleTranslator(target=target).translate(text)
    return text
