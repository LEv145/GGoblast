from django.views import generic

from .forms import RegisterForm
from .models import Event


class MainView(generic.TemplateView):
    template_name = "main.html"


class RegisterView(generic.FormView):
    template_name = "register.html"
    form_class = RegisterForm
    # success_url = '/thanks/'


class NewEventsView(generic.ListView):
    template_name = "new-events.html"
    model = Event


class EventView(generic.DetailView):
    template_name = "event.html"
    model = Event
