from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price', 'id']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    # настройте сериализатор для склада

    def create(self, validated_data):

        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for i in positions:
            StockProduct.objects.create(
                stock=stock,
                product=i['product'],
                quantity=i['quantity'],
                price=i['price']
            )

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # обновляем связанные таблицы
        for position in positions:
            stock_product = StockProduct.objects.get(
                stock=stock, product=position["product"]
            )
            stock_product.quantity = position["quantity"]
            stock_product.price = position["price"]
            stock_product.save()
        return stock
