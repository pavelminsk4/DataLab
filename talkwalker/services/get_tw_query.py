def get_tw_query(instance):
    query = ''
    if instance.expert_mode:
        query = instance.query_filter
    else:
        keywords = [f'\"{kw}\"' for kw in instance.keywords]
        query = ' OR '.join(keywords)
    print(query)
    return query