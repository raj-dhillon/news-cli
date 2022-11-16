from newscatcherapi import NewsCatcherApiClient
from results_manager import ResultsManager

newscatcherapi = NewsCatcherApiClient(
    x_api_key='DbMXiEAzP-MU_9qtgOXvN77bXtPiomH0_-YKGH2-9uk')


def get_results():
    results = newscatcherapi.get_search(q='Elon Musk',
                                        lang='en',
                                        countries='US',
                                        page_size=10)
    m = ResultsManager(results)
    m.export_results()


def get_top_results():
    results = newscatcherapi.get_latest_headlines(lang='en',
                                                  countries='US',
                                                  page_size=10)
    m = ResultsManager(results)
    m.export_results()


def category_input(manager):
    print("Categories:")
    categories = dict()
    curr_num = 1
    for i in manager.results:
        print(f"{curr_num}. {i}")
        categories[curr_num] = i
        curr_num += 1
    selection = int(input("Select a category: "))
    print()
    return manager.results[categories[selection]]


def get_title_selection(articles):
    num = 1
    print("Articles: ")
    for i in articles:
        print(f"{num}. {i['title']}")
        num += 1
    selection = input("Select a title for link (or Q to quit): ")
    print()
    if selection.lower() != "q":
        print(articles[int(selection) - 1]["link"])


def get_new_articles():
    selection = input(
        "Type N for new articles, otherwise cached articles will be shown: ")
    print()
    if selection.lower() == "n":
        get_top_results()


def read_results():
    get_new_articles()
    m = ResultsManager()
    m.import_results()
    articles = category_input(m)
    get_title_selection(articles)


read_results()
