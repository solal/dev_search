from rich.style   import Style
from rich.console import Console



class Result:
    """Creates a result instance capable of displaying a result's UI
    Args:
        link:String
        title:String
        domain:String
        description:String
    """

    def __init__(self, link, title, domain, description):
        self.link        = link
        self.title       = title
        self.domain      = domain
        self.description = description
        self.console     = Console()


    def __title_style(self):
        return Style(color="deep_sky_blue1", bold=True)


    def __description_style(self):
        return Style(color="white", bold=False)


    def print_as_ui(self, index=0):
        """Outputs the result's UI to the terminal
        Args:
            index:Int:The result's index as displayed on the UI
        """
        self.console.print( f"{index} . {self.title}.", style=self.__title_style() )
        self.console.print( f"{self.description}.",     style=self.__description_style() )
        self.console.print( "[dim gray100 link="+ self.link +"]"+ self.link +"[/dim gray100 link]" )
        print("\n")
