from django.urls import path, include
from rest_framework import routers

from task.views import TaskView


router = routers.DefaultRouter()
router.register("", TaskView)
urlpatterns = [
    path("", include(router.urls))
]

app_name = "task"
