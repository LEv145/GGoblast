import typing as t

from django.views import generic
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from .forms import RegisterForm
from .models import Event


class MainView(generic.TemplateView):
    template_name = "layout/main.html"


class RegisterView(generic.FormView):
    template_name = "layout/register.html"
    form_class = RegisterForm


class NewEventsView(generic.ListView):
    template_name = "layout/events.html"
    model = Event


class EventView(generic.DetailView):
    template_name = "layout/event.html"
    model = Event


def events_view(request: HttpRequest) -> HttpResponse:
    object_list = Event.objects.order_by("-start_at")[:5]

    return render(request, "layout/events.html", {"object_list": object_list})


def event_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        object_ = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404()

    return render(request, "layout/event.html", {"object": object_})
