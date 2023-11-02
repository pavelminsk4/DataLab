from tweet_binder.models import EnterpriseSearchProject
from datetime import datetime
import factory


class EnterpriseSearchProjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EnterpriseSearchProject

    title = ''
    limit = 1000
    keyword = 'Elon'
    keyword_and = ['Musk']
    keyword_or = ['SpaceX']
    keyword_nor = ['Tesla']
    start_date = datetime.datetime(2023, 7, 14, 12, 30)
    end_date = datetime.now()
