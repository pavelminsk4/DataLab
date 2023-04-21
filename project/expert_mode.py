import re
from boolean_parser import parse
from django.db.models import Q
from functools import reduce

class Parser:
  def __init__(self, query):
    self.query = query


  def can_parse(self):
    try:
      parse(self.__get_expression())
    except:
      return False
    else:
      return True

  def get_filter_query(self):
    return self.__simple_parse(parse(self.__get_expression()))

  def __simple_parse(self, cond):
    if hasattr(cond, 'data'):
      return Q(**{cond.name : cond.value})
    if not hasattr(cond, 'logicop'):
      return cond
    elif(cond.logicop == 'or'):
      return (reduce(lambda x, y: self.__simple_parse(x) | self.__simple_parse(y), cond.conditions))
    elif(cond.logicop == 'and'):
      return (reduce(lambda x, y: self.__simple_parse(x) & self.__simple_parse(y), cond.conditions))
    elif(cond.logicop == 'not'):
      return ~Q(self.__simple_parse(cond.conditions[0]))

  def __get_expression(self):
    parsed_query = self.query.replace('\'','\"').lower()
    regex = r'([a-z_]+((:\s+)|:)([a-z_]+|\"(.*?)\"))|[a-z_]+|\"(.*?)\"|\S' # a | 'a' | a:b | a:'b' | a: 'b' | : | ( | )
    words = re.finditer(regex, parsed_query)
    tokens = map(lambda w: self._Token(w.group()).define(), words)
    return reduce(lambda x, y: x + y.tostring(), tokens, '')

  class _Token:
    def __init__(self, value):
      self.value = value

    def tostring(self):
      pass

    def define(self):
      regex = r'[a-z_]+((:\s+)|:)([a-z_]+|\"(.*?)\")' # key:value | key: value | key: 'value' | key:'value'
      special = [':','(',')','/','or','and','not']
      if self.value in special:
        return Parser._SpecialToken(self.value)
      elif re.match(regex, self.value):
        return Parser._FieldToken(self.value)
      else:
        return Parser._KeywordToken(self.value)

  class _SpecialToken(_Token):
    def tostring(self):
      return self.value + ' '

  class _KeywordToken(_Token):
    def tostring(self):
      return 'entry_title__contains = ' + self.value + ' '

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
