from rest_framework import serializers

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    def get_logged_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        validated_data['customer'] = self.get_logged_user()
        return super().create(validated_data)

    class Meta:
        model = Order
        fields = ('address', 'pizza', 'pizza_size')
