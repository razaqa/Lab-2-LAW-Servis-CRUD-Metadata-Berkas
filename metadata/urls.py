from .apis import router
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include(router.urls)),
]