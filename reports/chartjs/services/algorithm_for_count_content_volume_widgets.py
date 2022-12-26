def algorithm_for_count_volume_widgets(top_list, results):
    dates = set()
    for elem in range(len(results)):
        for i in range(len(results[elem][top_list[elem]])):
            dates.add(str(results[elem][top_list[elem]][i]['date']))
    res = []
    for elem in range(len(results)):
        list_dates = []
        for date in sorted(list(dates)):
            if date in sorted(list({str(results[elem][top_list[elem]][i]['date']) for i in range(len(results[elem][top_list[elem]]))})):
                for i in range(len(results[elem][top_list[elem]])):
                    if date == str(results[elem][top_list[elem]][i]['date']): 
                        list_dates.append({"date": date, "post_count": results[elem][top_list[elem]][i]['created_count']})
            else:
                list_dates.append({"date": date, "post_count": 0})
        if (top_list[elem] == '') or (top_list[elem] == None) or ('img' in top_list[elem]) or (top_list[elem] == 'None') or (top_list[elem] == 'null') or not top_list[elem]:    
            res.append({'Missing in source': list_dates})    
        else:
            res.append({top_list[elem]: list_dates})   
    colors = ['rgba(19,64,145,255)', 'rgba(78,97,143,255)', 'rgba(45,105,85,255)', 'rgba(52,141,79,255)', 'rgba(134,221,66,255)', 'rgba(138,141,53,255)', 'rgba(139,102,45,255)', 'rgba(110,43,46,255)', 'rgba(167,47,98,255)', 'rgba(115,40,130,255)']            
    return res, colors
