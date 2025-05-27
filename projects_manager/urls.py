"""
URL configuration for projects_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from projects.views import (
    projects_list_view,
    projects_create_view,
    project_detail_view,
    feedback_create_view,
    feedback_delete_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", projects_list_view, name="projects-list"),
    path("projects/create/", projects_create_view, name="project-create"),
    path("projects/<int:project_id>/", project_detail_view, name="project-detail"),
    path("projects/<int:project_id>/feedbacks/create/", feedback_create_view, name="feedback-create"),
    path("feedbacks/<int:feedback_id>/delete/", feedback_delete_view, name="feedback-delete"),
]
