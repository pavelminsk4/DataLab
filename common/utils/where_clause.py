def where_clause(q):
    posts_query   = str(q.query).split('WHERE (')[1].split(') ORDER BY')[0]
    project_query = posts_query.split('AND')[0]
    date_query    = posts_query.split('BETWEEN')[1].split('AND')

    return f"{project_query} AND p.entry_published BETWEEN '{str(date_query[0])}' AND '{str(date_query[1])}'"
