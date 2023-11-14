from project.online_parser import OnlineParser


class ExpertPresets:
    def __init__(self, project):
        self.project = project

    def apply_presets_for_online_project(project):
        posts = project.posts.all()
        presets = project.exp_filter_presets
        for preset in presets:
            parser = OnlineParser(preset.query)
            posts = posts.filter(parser.get_filter_query())
        return posts

    def apply_presets_for_social_project(project):
        return False
