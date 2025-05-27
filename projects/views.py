from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Avg
from django.db.models.functions import Round

from projects.models import Project, Feedback
from projects.forms import ProjectForm, FeedbackForm


def projects_create_view(request: HttpRequest):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("projects-list")
    else:
        context = {
            "form": form,
        }
    return render(request, "project_form.html", context=context)

def projects_list_view(request: HttpRequest):
  projects_list = (Project.objects.all()
                   .select_related("owner")
                   .prefetch_related("employees")
                   .annotate(avg_rating=Round(Avg("feedback__rating"), 1))
                   )
  context = {
    "projects_list": projects_list,
  }
  return render(request, "projects_list.html", context=context)

def project_detail_view(request: HttpRequest, project_id: int):
    project = (Project.objects.all()
                .select_related("owner")
                .prefetch_related("employees")
                .annotate(avg_rating=Round(Avg("feedback__rating"), 1))
                .get(id=project_id)
               )
    feedbacks_list = Feedback.objects.filter(project=project)
    context = {
        "project": project,
        "feedbacks_list": feedbacks_list
    }
    return render(request, "project_detail.html", context=context)

def feedback_create_view(request: HttpRequest, project_id: int):
    project = Project.objects.get(id=project_id)
    form = FeedbackForm(request.POST)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.project = project
        feedback.save()
        return redirect("project-detail", project_id)
    else:
        context = {
            "form": form,
        }
        return render(request, "feedback_form.html", context=context)

def feedback_delete_view(request: HttpRequest, feedback_id: int):
  feedback = Feedback.objects.get(id=feedback_id)
  project_id = feedback.project.id
  feedback.delete()
  return redirect("project-detail", project_id)
