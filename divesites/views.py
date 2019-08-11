from django.views import generic

from .models import Location


class IndexView(generic.ListView):
    template_name = 'divesites/index.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        """
        Return the all locations alphabetically
        """
        return Location.objects.order_by('location_name')


class DetailView(generic.DetailView):
    model = Location
    template_name = 'divesites/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Location.objects
