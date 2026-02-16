from django.contrib import admin
from api.views import QuoteViewset,CommentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from api import views

router = DefaultRouter()
router.register(r'quote',QuoteViewset)
router.register(r'comment',CommentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",views.CommentViewSet.as_view()),
]
