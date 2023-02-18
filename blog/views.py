from django.views.generic import View, ListView
from taxonomies.models import Category

titre = "Bienvenue à Djangoland !"


class HomeView(ListView):
    """La page d'accueil de notre site."""

    model = Category
    context_object_name = "categories"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = titre
        return context


home = HomeView.as_view()


class MaNouvelleView(HomeView):
    template_name = "manouvellevue.html"


nouvelle_page = MaNouvelleView.as_view()
