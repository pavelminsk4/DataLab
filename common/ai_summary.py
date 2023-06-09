from deep_translator import GoogleTranslator
from transformers import pipeline
import re


def create_src_lang_summary(text, summarizer, lang):
    english_text = GoogleTranslator(source=lang, target='english').translate(text)
    summary_text = summarizer(english_text, do_sample=False)[0]['summary_text']
    result_text = GoogleTranslator(source='english', target=lang).translate(summary_text)
    return result_text


def create_en_summary(text, summarizer):
    summary_text = summarizer(text, min_length=30, do_sample=False)[0]['summary_text']
    return summary_text


def ai_summary(text, lang):
    lang = re.subn(r'\([^()]*\)', '', lang)[0].lower().replace(' ', '')
    langs_list = GoogleTranslator().get_supported_languages()
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    if lang == 'english':
        return create_en_summary(text, summarizer)
    if lang in langs_list:
        return_text = create_src_lang_summary(text, summarizer, lang)
    else:
        return_text = create_en_summary(text, summarizer)
    return return_text
