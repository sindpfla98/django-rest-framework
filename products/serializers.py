from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    def get_imgUrl(self,obj):
        return "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{}.jpg".format(obj.imageId)
    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales',)

class ProductDetailSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    def get_imgUrl(self,obj):
        return "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/{}.jpg".format(obj.imageId)

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales',)

class ProductRecomndSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    def get_imgUrl(self,obj):
        return "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/{}.jpg".format(obj.imageId)

    class Meta:
        model = Product
        fields = ('id', 'imgUrl', 'name', 'price',)
