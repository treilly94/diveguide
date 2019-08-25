"""
The views for the dive site app
"""
import os

from django.views import generic

from .models import Location


class IndexView(generic.ListView):  # pylint: disable=R0901
    """The view for the apps Index page"""

    template_name = 'divesites/index.html'
    context_object_name = 'locations'

    def get_queryset(self):
        """
        Applies filters and returns location objects

        :return:
        """

        search_query = self.request.GET.get('search')

        if search_query:
            return Location.objects.filter(location_name__icontains=search_query)

        return Location.objects.all()


class DetailView(generic.DetailView):  # pylint: disable=R0901
    """The detail view for the sites"""

    model = Location
    template_name = 'divesites/detail.html'

    def get_context_data(self, **kwargs):
        """Adds additional context to the template"""
        context = super(DetailView, self).get_context_data(**kwargs)
        context['api_key'] = os.getenv("GOOGLE_MAPS_API")
        return context
