from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include

urlpatterns = format_suffix_patterns([
    path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('users/', views.UserList.as_view(),name='user-list'),   
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('', views.api_home),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name='snippet-highlight'),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
