from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Member, Project
from .serializers import MemberSerializer, ProjectSerializer

# Create your views here.

# uses a post request
class MemberCreateView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# uses a get request
class MemberListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# uses a post request
class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# uses a get request
class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer