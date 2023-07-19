from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import CardTitle, CardType
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CardCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

def hello_world(request):
    return HttpResponse("Hello World")

class TypeListView(ListView):
    model = CardType
    template_name = 'card/homeview.html'
    context_object_name = 'categories'

class TypeDetailView(DetailView):
    model = CardType
    template_name = 'card/typedetail.html'
    context_object_name = 'type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_object = self.get_object()
        cards = CardTitle.objects.filter(categories=type_object).order_by('-date_created')
        context['cards'] = cards
        return context
    
class TypeCreateView(CreateView):
    model = CardType
    fields = ['category', 'color']

    def get_success_url(self):
        return reverse('cards-homeview')
    
class TypeUpdateView(UpdateView):
    model = CardType
    fields = ['category', 'color']

    def get_success_url(self):
        return reverse('cards-homeview')
    
class TypeDeleteView(DeleteView):
    model = CardType

    def get_success_url(self):
        return reverse("cards-homeview")

class CardListView(ListView):
    model = CardTitle
    template_name = 'card/cards_home.html'
    context_object_name = 'cards'
    ordering = ['-date_created']
    paginate_by = 4

class CardDetailView(DetailView):
    model = CardTitle
    template_name = 'card/detail.html'
    context_object_name = 'card'

class CardCreateView(CreateView):
    model = CardTitle
    fields = ['title', 'content', 'categories']
    # form_class = CardCreationForm

    def form_valid(self, form):
        form.instance.author = User.objects.get(id=1) #TODO change to self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("cards-homeview")

class CardUpdateView(UpdateView):
    model = CardTitle
    fields = ['title', 'content', 'categories']
    # form_class = CardCreationForm

    def form_valid(self, form):
        form.instance.author = User.objects.get(id=1) #TODO
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("cards-homeview")
    
class CardDeleteView(DeleteView):
    model = CardTitle

    def get_success_url(self):
        return reverse("cards-homeview")