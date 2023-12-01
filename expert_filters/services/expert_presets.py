from project.online_parser import OnlineParser


class ExpertPresets:
    def __init__(self, project, posts):
        self.project = project
        self.presets = project.expert_presets
        self.posts   = self.apply_presets(posts)

    def apply_presets(self, posts):
        for preset in self.presets.all():
            posts  = posts.filter(OnlineParser(''.join(preset.query)).get_filter_query())
        return posts
