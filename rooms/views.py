from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
