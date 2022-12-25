from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "content") # 模型中需要序列化的字段
        model = Note # 指定模型类