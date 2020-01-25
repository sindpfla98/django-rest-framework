from .models import Product, Ingredient
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductRecomndSerializer
from django.http import Http404
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import views

def product_score(id):
    score = []
    oily_score = 0
    dry_score = 0
    sensitive_score = 0

    product_ingrdnts = Product.objects.get(pk=id).ingredients
    product_ingrdnts = product_ingrdnts.split(',')

    for ingrdnt in product_ingrdnts:
        benefit = Ingredient.objects.get(name=ingrdnt)

        if benefit.oily == "O":
            oily_score += 1
        elif benefit.oily == "X":
            oily_score -= 1

        if benefit.dry == "O":
            dry_score += 1
        elif benefit.dry == "X":
            dry_score -= 1

        if benefit.sensitive == "O":
            sensitive_score += 1
        elif benefit.sensitive == "X":
            sensitive_score -= 1

    score.append(oily_score)
    score.append(dry_score)
    score.append(sensitive_score)
    return score

def insert_score():
    OILY = 0
    DRY = 1
    SENSITIVE = 2

    for product in Product.objects.all():
        score = product_score(product.id)
        product.oily = score[OILY]
        product.dry = score[DRY]
        product.sensitive = score[SENSITIVE]
        product.save()

    print("complete")

class ProductList(views.APIView):
    """
    상품 목록 조회
    """
    def get(self, request, format=None):
        skin_type = self.request.query_params.get('skin_type')
        category = self.request.query_params.get('category')
        page = self.request.query_params.get('page')
        exclude_ingrdnt = self.request.query_params.get('exclude_ingredient')
        include_ingrdnt = self.request.query_params.get('include_ingredient')

        skin_type_desc = "-"+skin_type
        queryset = Product.objects.order_by(skin_type_desc, 'price')

        if category is not None:
            queryset = queryset.filter(category=category)

        if include_ingrdnt != None:
            if "," in include_ingrdnt:
                in_ingrdnts = include_ingrdnt.split(',')
            else:
                in_ingrdnts = []
                in_ingrdnts.append(include_ingrdnt)

            for in_ingrdnt in in_ingrdnts:
                queryset = queryset.filter(ingredients__icontains=in_ingrdnt)

        if exclude_ingrdnt != None:
            if "," in exclude_ingrdnt:
                ex_ingrdnts = exclude_ingrdnt.split(',')
            else:
                ex_ingrdnts = []
                ex_ingrdnts.append(exclude_ingrdnt)

            for ex_ingrdnt in ex_ingrdnts:
                queryset = queryset.exclude(ingredients__icontains=ex_ingrdnt)

        if page != None:
            page_number = self.request.query_params.get('page_number ', page)
        else:
            page_number = self.request.query_params.get('page_number ', 1)
        page_size = self.request.query_params.get('page_size ', 50)

        paginator = Paginator(queryset, page_size)
        serializer = ProductListSerializer(paginator.page(page_number), many=True)
        return Response(serializer.data)

class ProductDetail(views.APIView):
    """
    상품 상세 정보 조회
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detail_queryset = self.get_object(pk)
        detail_serializer = ProductDetailSerializer(detail_queryset)

        skin_type = self.request.query_params.get('skin_type')
        skin_type_desc = "-" + skin_type
        recomnd_queryset = Product.objects.order_by(skin_type_desc, 'price')[:3]
        recomnd_serializer = ProductRecomndSerializer(recomnd_queryset, many=True)

        product_detail = []
        product_detail.append(detail_serializer.data)

        for i in range(3):
            product_detail.append(recomnd_serializer.data[i])

        return Response(product_detail)
