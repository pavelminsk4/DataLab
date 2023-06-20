from twenty_four_seven.models import WARecipient
import factory


class WARecipientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WARecipient

    name = 'Paul Smith'
    mobile_number = '+375291234578'
