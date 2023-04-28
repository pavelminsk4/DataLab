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
    elif not hasattr(cond, 'logicop'):
      return cond
    elif(cond.logicop == 'or'):
      return (reduce(lambda x, y: self.__simple_parse(x) | self.__simple_parse(y), cond.conditions))
    elif(cond.logicop == 'and'):
      return (reduce(lambda x, y: self.__simple_parse(x) & self.__simple_parse(y), cond.conditions))
    elif(cond.logicop == 'not'):
      return ~Q(self.__simple_parse(cond.conditions[0]))

  def __get_expression(self):
    parsed_query = self.query.replace('\'','\"').lower()
    regex = r'([a-z_]+((:\s+)|:)(>|<|=)[0-9]+)|([a-z_]+((:\s+)|:)([a-z_]+|\"(.*?)\"))|[a-z_]+|\"(.*?)\"|\S' # a | 'a' | a:b | a:'b' | a: 'b' | : | ( | )
    words = re.finditer(regex, parsed_query)
    tokens = map(lambda w: self._Token(w.group()).define(), words)
    return reduce(lambda x, y: x + y.tostring(), tokens, '')

  class _Token:
    def __init__(self, value):
      self.value = value

    def tostring(self):
      return self.value

    def define(self):
      return self
