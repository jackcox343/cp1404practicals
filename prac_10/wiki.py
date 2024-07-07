import wikipedia


def main():
    page_title = input("Enter a Wikipedia page title: ")
    while page_title != "":
        try:
            summary = wikipedia.summary(page_title)
            page = wikipedia.page(page_title)
            print(summary)
            print(page.title)
            print(page.url)
            page_title = input("Enter a Wikipedia page title: ")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            page_title = input("Enter a Wikipedia page title: ")


main()
