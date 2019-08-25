"""
The views for the dive site app
"""

from django.views import generic

from .models import Location


class IndexView(generic.ListView):  # pylint: disable=R0901
    """The view for the apps Index page"""

    template_name = 'divesites/index.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        """Return the all locations alphabetically"""

        return Location.objects.order_by('location_name')


class DetailView(generic.DetailView):  # pylint: disable=R0901
    """The detail view for the sites"""

    model = Location
    template_name = 'divesites/detail.html'

    def get_queryset(self):
        """Returns the location objects"""

        return Location.objects
