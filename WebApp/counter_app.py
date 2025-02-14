import operator
def count(article):
    words = article.split()
    words_count = len(words)
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    sorted_dict = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return words_count, sorted_dict