from talkwalker.classes.livestream import Livestream


class StopLivestreamService:
    def execute(self, id):
        ls = Livestream(id, 'Project')
        ls.delete()
