from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView, NewEventsView, EventView, MainView


urlpatterns =[
    path("", MainView.as_view()),
    path("registration", RegisterView.as_view()),
    path("events", NewEventsView.as_view()),
    path("event/<int:pk>", EventView.as_view(), name="event")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
