import re
from boolean_parser import parse
from django.db.models import Q
from functools import reduce

class Parser:
  def __init__(self, query):
    self.query = query

  fields = {
    'source': 'feedlink__source1',
    'country': 'feedlink__country',
    'author': 'entry_author',
    'sentiment': 'sentiment',
    'language': 'feed_language__language__icontains'
  }

  def get_expression(self):
    parsed_query = self.query.replace('\'','\"').lower()
    special = ['!',':','@',',','#','$','%','^','&','*','(',')','-','+','?','_','=','<','>','/','or','and','not']
    filter_list = list(map(lambda w: w.group(), re.finditer(r'[a-z]+|\"(.*?)\"|\'(.*?)\'|\S', parsed_query)))
    res = ''
    i = 0
    while i < len(filter_list):
      if filter_list[i] in special:
        res += filter_list[i] + ' '
      elif i+2 < len(filter_list) and filter_list[i] in self.fields.keys() and  filter_list[i+1] == ':':
        res += self.fields[filter_list[i]] + ' = ' + filter_list[i+2] + ' '
        i +=2
      else:
        res += 'entry_title__icontains = ' + filter_list[i] + ' '
      i += 1
    return res

  def can_parse(self):
    try:
      parse(self.get_expression())
    except:
      return False
    else:
      return True

  def get_filter_query(self):
    return self.simple_parse(parse(self.get_expression()))

  def simple_parse(self, cond):
    if hasattr(cond, 'data'):
      return Q(**{cond.name : cond.value})
    if not hasattr(cond, 'logicop'):
      return cond
    elif(cond.logicop == 'or'):
      return (reduce(lambda x, y: self.simple_parse(x) | self.simple_parse(y), cond.conditions))
    elif(cond.logicop == 'and'):
      return (reduce(lambda x, y: self.simple_parse(x) & self.simple_parse(y), cond.conditions))
    elif(cond.logicop == 'not'):
      return ~Q(self.simple_parse(cond.conditions[0]))
