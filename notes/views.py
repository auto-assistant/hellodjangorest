# notes/views.py
from rest_framework import viewsets
from rest_framework import permissions
from .models import Note
from .serializers import NoteSerializer
from rest_framework.exceptions import PermissionDenied


# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all() # 指定 queryset
#     serializer_class = NoteSerializer # 指定序列化类

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = (IsOwner,)

    # 确保用户只能看到自己的 Note 数据。
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user)
        raise PermissionDenied()

    # 设置当前用户为 Note 对象的所有者
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
