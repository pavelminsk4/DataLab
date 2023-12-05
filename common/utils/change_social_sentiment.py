from project_social.models import ChangingTweetbinderSentiment
from common.utils.change_sentiment import ChangeSentiment


class ChangeSocialSentiment(ChangeSentiment):
    def changeset(self):
        department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=self.department_id).values()
        dict_changing = {x['post_id']: x['sentiment'] for x in department_changing}
        return dict_changing
