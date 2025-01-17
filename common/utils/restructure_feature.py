from comparison.widgets_names import WIDGETS_NAMES


def restructure_feature(feature_widgets, decriptions):
    result_list = []
    for project_dict in feature_widgets:
        project = project_dict['project_name']
        widgets = project_dict['widgets']
        project_id = project_dict['project_id']
        for wg in widgets:
            exist = False
            for dct in result_list:
                if dct['widget_name'] == wg['name']:
                    dct['projects_data'].append({
                        'project': project,
                        'project_id': project_id,
                        'widget_id': wg['widget_id'],
                        'data': wg['data'],
                    })
                    exist = True
            if not exist:
                result_list.append({
                    'widget_name': wg['name'],
                    'projects_data': [{'project': project, 'project_id': project_dict['project_id'], 'widget_id': wg['widget_id'], 'data': wg['data']}],
                    'description': decriptions[WIDGETS_NAMES[wg['name']]] | { 'module': project_dict['module']},
                })
    return result_list
