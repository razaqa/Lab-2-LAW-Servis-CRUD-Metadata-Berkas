from django.urls import include, path
from django.contrib import admin
from .apis import router

urlpatterns = [
    path('', include(router.urls)),
]