username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus" 
    icon_right: "android"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 350
    multiline: False 
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: 'Item 1'
"""