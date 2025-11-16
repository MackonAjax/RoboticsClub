from django.urls import path
from .views import MemberCreateView, MemberListView, ProjectCreateView, ProjectListView



urlpatterns = [
    path('/', MemberListView.as_view(), name='list_members'),
    path('create_member/', MemberCreateView.as_view(), name='create_member'),
    path('list_members/', MemberListView.as_view(), name='list_members'),

    path('create_project/', ProjectCreateView.as_view(), name='create_project'),
    path('list_projects/', ProjectListView.as_view(), name='list_projects'),
]