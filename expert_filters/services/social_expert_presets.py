from project_social.social_parser import SocialParser


class SocialExpertPresets:
    def __init__(self, project):
        self.project = project

    def apply_presets(project):
        posts = project.posts.all()
        presets = project.expert_presets.all()
        for preset in presets:
            query = ''.join(preset.query)
            parser = SocialParser(query)
            posts = posts.filter(parser.get_filter_query())
        return posts
