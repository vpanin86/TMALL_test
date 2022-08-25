from page_objects import PageObject, PageElement

class HelpCenterPage(PageObject):

    help_center_header = PageElement(tag_name='h2')