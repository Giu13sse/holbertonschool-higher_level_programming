
Sign up
BennettDixon /
holbertonschool-higher_level_programming
Public

    Code
    Issues
    Pull requests
    Actions
    Projects
    Wiki
    Security
    Insights

holbertonschool-higher_level_programming/0x03-python-data_structures/4-new_in_list.py
@BennettDixon
BennettDixon Fixed function to return original list on index out of range error
1 contributor
15 lines (12 sloc) 333 Bytes
#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    Without modifying the original list
    """
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
