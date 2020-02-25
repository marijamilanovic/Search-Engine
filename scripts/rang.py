
def rang(graph, result):
    rang_result = {}

    for html in result.keys():

        incoming = graph.incoming_links(html)
        number_links = len(incoming)
        number_words_in_links = 0
        for link in incoming:
            if link in result.keys():
                number_words_in_links += result[link]

        rang_result[html] = int(result[html] + number_links * 0.7 + number_words_in_links * 0.5)

    # print(rang_result)

    return rang_result
