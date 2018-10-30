# Lesson 5 Chapter 30


def get_next_target(page):
    start_link = page.find('<a href=')

    # if the link tag sequence is not found, find returns a -1
    if start_link == -1:
        # return the error codes of None, 0 now and skip the rest!
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_link(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break


print_link('print_all_<a href="https://udacity.com">valid link</a>links must keep going until there are no more links to print. Think about looping forever (set while loop condition) until there are no more links (i.e. else:). What do you do when there are no more links (body of else: condition)?')
