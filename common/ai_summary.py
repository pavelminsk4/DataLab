from common.translator.translate_long_text import translate_long_text
from transformers import pipeline
import re


def create_en_summary(text, summarizer):
    summary_text = summarizer(text, min_length=30, do_sample=False)[0]['summary_text']
    return summary_text


def ai_summary(text, lang):
    lang = re.subn(r'\([^()]*\)', '', lang)[0].lower().replace(' ', '')
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    if lang != 'english':
        text = translate_long_text(text, 'english')
    return create_en_summary(text, summarizer)
