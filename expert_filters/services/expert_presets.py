from project.online_parser import OnlineParser


class ExpertPresets:
    def __init__(self, project):
        self.project = project

    def apply_presets(project):
        module = project.__class__.__name__

        if module == 'Project':
            posts = project.posts.all()
            presets = project.expert_presets.all()
            for preset in presets:
                query = ''.join(preset.query)
                parser = OnlineParser(query)
                posts = posts.filter(parser.get_filter_query())
            return posts
        if module == 'ProjectSocial':
            return False
