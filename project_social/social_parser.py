import re
from common.query_parser import Parser

class SocialParser(Parser):
  class _Token:
    def __init__(self, value):
      self.value = value

    def define(self):
      reg_field = r'[a-z_]+((:\s+)|:)([a-z_]+|\"(.*?)\")' # key:value | key: value | key: 'value' | key:'value'
      reg_num = r'[a-z_]+((:\s+)|:)((>|<|=)[0-9]+)' # key:<value | key: >value | key: =value
      special = [':','(',')','/','or','and','not']
      if self.value in special:
        return SocialParser._SpecialToken(self.value)
      elif re.match(reg_field, self.value):
        return SocialParser._FieldToken(self.value)
      elif re.match(reg_num, self.value):
        return SocialParser._NumToken(self.value)
      else:
        return SocialParser._KeywordToken(self.value)

  class _SpecialToken(_Token):
    def tostring(self):
      return self.value + ' '

  class _KeywordToken(_Token):
    def tostring(self):
      return f'(text__contains = {self.value} or user_name__contains = {self.value} or user_alias__contains = {self.value})'

  class _FieldToken(_Token):
    fields = {
      'location': 'locationString__icontains',
      'author': 'user_name__iexact',
      'sentiment': 'sentiment',
      'language': 'language__icontains',
    }

    def tostring(self):
      values = self.value.split(':')
      return self.fields[values[0]] + ' = ' + values[1] + ' '

  class _NumToken(_Token):
    fields = {
      'followers': 'user_followers',
    }

    operators = {
      '<' : '__lte',
      '>' : '__gte',
      '=' : '__exact',
    }

    def tostring(self):
      field = self.fields[re.search(r'[a-z_]+', self.value).group()]
      value = re.search(r'[0-9]+', self.value).group()
      op = self.operators[re.search(r'<|>|=', self.value).group()]
      return f'{field}{op} = {value}'
