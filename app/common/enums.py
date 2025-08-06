from enum import Enum

class ProductSortField(str, Enum):
    price = "price"
    title = "title"

class SortOrder(str, Enum):
    asc = "ASC"
    desc = "DESC"