from django.shortcuts import render
from rest_framework.generics import ListAPIView
from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,)
from .serializers import (
    ClassListSerializer,
    ClassDetailSerializer,
    ClassCreateUpdateSerializer,)



class ClassListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    
    

class ClassDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    


class ClassCreateView(CreateAPIView):
    serializer_class = ClassCreateUpdateSerializer
   

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    


class ClassDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    