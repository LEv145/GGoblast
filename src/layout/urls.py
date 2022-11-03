from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    RegisterView,
    NewEventsView,
    EventView,
    MainView,
    event_view,
    events_view,
)


app_name = "layout"
urlpatterns = [
    path("", MainView.as_view()),
    path("events", events_view, name="events"),
    path("event/<int:pk>", event_view, name="event"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
