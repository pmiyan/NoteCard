from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import CardTitle, CardType
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CardCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

def hello_world(request):
    return HttpResponse("Hello World")

# def detail(request, card_id):
#     card = get_object_or_404(CardTitle, pk=card_id)
#     context = {'card':card}
#     return render(request, 'card/detail.html', context)

# def home(request):
#     cards = get_list_or_404(CardTitle)
#     context = {'cards':cards}
#     return render(request, 'card/home.html', context)

class CardListView(ListView):
    model = CardTitle
    template_name = 'card/home.html'
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
        return reverse("cards-home")

class CardUpdateView(UpdateView):
    model = CardTitle
    fields = ['title', 'content', 'categories']
    # form_class = CardCreationForm

    def form_valid(self, form):
        form.instance.author = User.objects.get(id=1) #TODO
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("cards-home")
    
class CardDeleteView(DeleteView):
    model = CardTitle

    def get_success_url(self):
        return reverse("cards-home")