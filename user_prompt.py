import os
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as ptStyles
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.validation import Validator, ValidationError



class StartSearchValidator(Validator):
    def validate(self, document):
        text = document.text
        if text is None or text == "" or text == " ":
            raise ValidationError(message="Please type in your query to start searching.", cursor_position=0)



class OpenLinkValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            if (len(text) == 1) and (text == 'n' or text == 'q'):
                return

            # Get index of first non numeric character.
            # We want to move the cursor here.
            i = 0
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            validation_message = "<" + text + "> is not a valid option | [page num.] open page -- [n] new search -- [q] quit"
            raise ValidationError(message=validation_message, cursor_position=i)



class UserPrompt:
    def __init__(self):
        return


    def __clear_screen(self):
        return os.system('cls' if os.name == 'nt' else 'clear')


    def __ui_bottom_toolbar(self):
        """Defines the text of the bottom UI toolbar
        Returns:
            HTML:UI bar with relevant text
        """
        return HTML("[page num.] open page -- [n] new search -- [q] quit")


    def __get_rprompt(self):
        return '<enter page num.>'


    def __open_res_style(self):
        return ptStyles.from_dict({
            'rprompt': 'bg:#ff0066 #ffffff',
        })


    def search_prompt(self):
        """Prompts the user for search query

        Returns:
            String:User search query
        """
        self.__clear_screen()
        query = prompt('search > ', cursor=CursorShape.BLINKING_BLOCK, validator=StartSearchValidator())

        if query == 'q':
            self.__clear_screen()
            exit()

        return query


    def select_page(self):
        selected_page = prompt('open [page num.] > ',
            bottom_toolbar=self.__ui_bottom_toolbar,
            cursor=CursorShape.BLINKING_BLOCK,
            rprompt=self.__get_rprompt(),
            style=self.__open_res_style(),
            validator=OpenLinkValidator()
        )

        try:
            return int(selected_page)
        except ValueError:
            return self.non_int_select(selected_page)


    def non_int_select(self, selected_option=None):
        if selected_option == 'q':
            self.__clear_screen()
            exit()

        return