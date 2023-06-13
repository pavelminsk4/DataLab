def descending_sort(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
