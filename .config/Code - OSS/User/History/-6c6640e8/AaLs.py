from django.contrib import admin
from django.urls import path,include
from snippet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/snippet/',views.SnippetViewAPI.as_view()),
]
