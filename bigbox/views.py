from django.http import Http404
from .models import Box, Activity
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.conf import settings


def home(request):
    return render(request, 'bigbox/home.html')

def search_form(request):
    # Se que agregar los slugs en el context para facilitar la busqueda por slug no es requerido por la consigna.
    context = { 'slugs': Box.objects.all().values('slug') }
    template_name = 'bigbox/search_form.html'

    slug = request.GET.get('q')

    if slug:
        try:
            Box.objects.get(slug=slug)
            return redirect('box-search-result', slug=slug)
        except:
            context['error'] = f'No hay ninguna box con el slug {slug}'

    return render(request, template_name, context)


class BoxList(ListView):
    model = Box


class BoxDetail(DetailView):
    model = Box


class ActivityList(ListView):
    model = Activity
    paginate_by = settings.ACTIVITY_LIST_PAGINATOR

    def get_queryset(self):
        queryset = self.model.objects.filter(box__pk=self.kwargs['pk'])

        if queryset == []:
            raise Http404('box no encontrado')

        return queryset


class ActivityDetail(DetailView):
    model = Activity