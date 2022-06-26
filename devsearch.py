import click
import time
import os
import webbrowser
from rich.status import Status
from result import Result
from search_results_page import SearchResultsPage
from install_data import InstallData
from user_prompt import UserPrompt
from whitelist import Whitelist



def display_results(results, search_time):
    links_list      = []
    whitelist       = Whitelist(results)
    white_list_dict = whitelist.get_domain_whitelist_dict()

    for index, res in enumerate(results):
        if index == 0: status.stop()
        if len(links_list) > 9: break

        # Only display results if they appear in whitelist
        if res['domain'] in white_list_dict:
            result = Result(
                res['link'],
                res['title'],
                res['domain'],
                res['description']
            )

            result.print_as_ui( len(links_list) )
            links_list.append(res['link'])

    print("--- %s seconds ---" % (time.time() - search_time))
    open_link(links_list)


def open_link(links_list):
    pick_res_prompt   = UserPrompt()
    selected_page_num = pick_res_prompt.select_page()

    if selected_page_num is not None:
        if selected_page_num >= len(links_list):
            print( "Please select a result between 0 and " + str(len(links_list) - 1) )
            open_link(links_list)

        webbrowser.open(links_list[selected_page_num])
        open_link(links_list)

    start_search()


def do_search(query):
    """Executes search query by calling the Google search lib
    Args:
        Arg1:String:User's search query
    Returns:
        List:Dict:Result of a call to `search()` for from Google search lib
            ```
            [{
                'link': String,
                'title': String,
                'domain': String,
                'description': String
            }]
            ```
    """
    tab_title = 'echo "\033]0;%s | Dev Search\007"' % query
    os.system(tab_title)
    status.update("[bold green]" + query)
    status.start()

    results_page = SearchResultsPage(query)
    return results_page.results()


status = Status("[bold green]Searching...")
def start_search():
    install = InstallData()
    install.async_check_whitelist_version()

    user_prompt = UserPrompt()
    query       = user_prompt.search_prompt()

    display_results(
        do_search(query),
        time.time()
    )


def main():
    start_search()


if __name__ == "__main__":
    main()


@click.command()
def cli():
    """Example script."""
    start_search()