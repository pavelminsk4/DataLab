from project.models import ChangingOnlineSentiment


class ChangeSentiment():
    def __init__(self, department_id=None, posts_list=None):
        self.department_id = department_id
        self.posts_list = posts_list

    def change_sentiment(self, post, dict_changing):
        if post['id'] in dict_changing:
            new_sentiment = dict_changing[post['id']]
            post['sentiment'] = new_sentiment
        return post        
    
    def changeset(self):
        department_changing = ChangingOnlineSentiment.objects.filter(department_id=self.department_id).values()
        dict_changing = {x['post_id']: x['sentiment'] for x in department_changing}
        return dict_changing

    def execute(self):
        dict_changing = self.changeset()
        for post in self.posts_list:
            post = self.change_sentiment(post, dict_changing)
        return self.posts_list
