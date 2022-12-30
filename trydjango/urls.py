from django.contrib import admin
from django.urls import path
from article.views import article_detail_view,article_search_view, article_create_view,mail
from . import views
from accounts.views import login_view,logout_view,register_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', views.home,name="home"),
    path('article/',article_search_view),
    path('article/create/', article_create_view),
    path('login/', login_view, name='login.view'),
    path('logout/', logout_view, name='logout.view'),
    path('register/', register_view, name='register.view'),
    path('article/create1/', mail,name='mail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('article/<int:id>/',article_detail_view),
    path('admin/', admin.site.urls),


]
