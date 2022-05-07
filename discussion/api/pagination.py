# from rest_framework.pagination import LimitOffsetPagination

# class CustomPagination(LimitOffsetPagination):
#     pass
#     # default_limit = 1000
#     # max_limit = 100000
#     # min_limit = 1
#     # min_offset = 0
#     # max_offset = 10000

#     # def paginate_queryset(self, queryset, request, view=None):
#     #     limit = request.query_params.get('limit')
#     #     offset = request.query_params.get('offset')

#     #     if limit:
#     #         limit = int(limit)
#     #         if limit > self.max_limit:
#     #             raise 
#     #     return super().paginate_queryset(queryset, request, view)