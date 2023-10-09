import logging
import fasttext

fasttext.FastText.eprint = lambda x: None

DEBUG = True

logging.disable(logging.CRITICAL)
