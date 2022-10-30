from django.views import generic

from .forms import RegisterForm
from .models import Event


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
