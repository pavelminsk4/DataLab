def get_tw_query(instance):
    query = ''
    if instance.expert_mode:
        query = instance.query_filter
    else:
        keywords = [f'\"{kw}\"' for kw in instance.keywords]
        query = ' OR '.join(keywords)
    return query
