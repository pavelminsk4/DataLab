import re
from common.query_parser import Parser

class OnlineParser(Parser):
  class _Token:
    def __init__(self, value):
      self.value = value

    def tostring(self):
      pass

    def define(self):
      regex = r'[a-z_]+((:\s+)|:)([a-z_]+|\"(.*?)\")' # key:value | key: value | key: 'value' | key:'value'
      special = [':','(',')','/','or','and','not']
      if self.value in special:
        return OnlineParser._SpecialToken(self.value)
      elif re.match(regex, self.value):
        return OnlineParser._FieldToken(self.value)
      else:
        return OnlineParser._KeywordToken(self.value)

  class _SpecialToken(_Token):
    def tostring(self):
      return self.value + ' '

  class _KeywordToken(_Token):
    def tostring(self):
      return f'(entry_title__icontains = {self.value} or entry_summary__icontains = {self.value}) '

  class _FieldToken(_Token):
    fields = {
      'source': 'feedlink__source1__iexact',
      'country': 'feedlink__country__iexact',
      'author': 'entry_author__iexact',
      'sentiment': 'sentiment',
      'language': 'feed_language__language__icontains'
    }

    def tostring(self):
      values = self.value.split(':')
      return self.fields[values[0]] + ' = ' + values[1] + ' '
