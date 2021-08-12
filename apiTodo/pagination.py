from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'MyPage'
    
class LargePagination(PageNumberPagination):
    page_size = 5