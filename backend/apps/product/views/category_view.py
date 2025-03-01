from rest_framework import viewsets, decorators, response, status
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema 
from product.models import Category
from product.serializers.category_serializer import CategorySerializer


@extend_schema(tags=['Category'])
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['restaurant__name']

    @decorators.action(detail=False, methods=["post"], url_path="update_order")
    def post_update(self, request):
        category_ids = request.data
        for index, category_id in enumerate(category_ids):
            category = Category.objects.get(id=category_id)
            category.order = index
            category.save()
        return response.Response({"message": "success"}, status=status.HTTP_206_PARTIAL_CONTENT)