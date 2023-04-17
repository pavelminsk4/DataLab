import re
from boolean_parser import parse
from django.db.models import Q
from functools import reduce

class Parser:
  def __init__(self, query):
    self.query = query

  def get_boolean_expression(self):
    parsed_query = self.query
    parsed_query = self.query.replace('\'','\"').lower()
    count = len(list(re.finditer(r"\"(.*?)\"", parsed_query)))
    for c in range(count):
      ind = list(re.finditer(r"\"(.*?)\"", parsed_query))[c].start()
      parsed_query = parsed_query[:ind] + 'x = ' + parsed_query[ind:]
    return parsed_query

  def can_parse(self):
    try:
      parse(self.get_boolean_expression())
    except:
      return False
    else:
      return True

  def get_filter_query(self):
    return self.simple_parse(parse(self.get_boolean_expression()))

  def simple_parse(self, cond):
    if hasattr(cond, 'data'):
      return Q(entry_title__contains = cond.value)
    if not hasattr(cond, 'logicop'):
      return cond
    elif(cond.logicop == 'or'):
      return (reduce(lambda x, y: self.simple_parse(x) | self.simple_parse(y), cond.conditions))
    elif(cond.logicop == 'and'):
      return (reduce(lambda x, y: self.simple_parse(x) & self.simple_parse(y), cond.conditions))
    elif(cond.logicop == 'not'):
      return ~Q(self.simple_parse(cond.conditions[0]))
