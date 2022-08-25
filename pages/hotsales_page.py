from page_objects import PageObject, PageElement


class HotSalesPage(PageObject):

    hot_sales_banner = PageElement(xpath='// *[ @ id = "8518692380"] / div / div')