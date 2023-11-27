from project_social.social_parser import SocialParser


class SocialExpertPresets:
    def apply_presets(self, project, posts):
        presets = project.expert_presets.all()
        for preset in presets:
            query = ''.join(preset.query)
            parser = SocialParser(query)
            posts = posts.filter(parser.get_filter_query())
        return posts
