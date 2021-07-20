from dearpygui.core import *
from dearpygui.simple import *

# have a list you want to search
list_of_items = ['a', 'ab', 'abc', 'b', 'bc', 'bcd']


def search():
    modified_list = []
    if get_value('Search'):
        for item in list_of_items:
            if get_value('Search') in item:
                modified_list.append(item)
    else:
        modified_list = list_of_items
    configure_item('Results', items=modified_list)


with window('Main Window'):
    add_input_text('Search', hint='Start typing to search', callback=search)
    add_listbox("Results", items=list_of_items)
start_dearpygui(primary_window='Main Window')