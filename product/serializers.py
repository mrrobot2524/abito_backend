from rest_framework import serializers
from .models import Item
import datetime

RU_MONTHS = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
    5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
    9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря',
}

class ItemSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    img = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'address', 'date', 'img']

    def get_date(self, obj):
        if not obj.date:
            return None
        dt = obj.date
        # Пример формата: "10 июля 11:39"
        day = dt.day
        month = RU_MONTHS.get(dt.month, dt.strftime('%B'))
        time = dt.strftime('%H:%M')
        return f"{day} {month} {time}"
