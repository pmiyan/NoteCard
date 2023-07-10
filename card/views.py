from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import CardTitle, CardContent, CardType
from django.views.generic import ListView, DetailView, CreateView
from .forms import CardCreationForm
from django.urls import reverse

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
    ordering = '-date_created'

class CardDetailView(DetailView):
    model = CardTitle
    pk_url_kwarg = 'card_id'
    template_name = 'card/detail.html'
    context_object_name = 'card'

class CardCreateView(CreateView):
    model = CardTitle
    template_name = 'card/create.html'
    form_class = CardCreationForm

    def form_valid(self, form):
        # card_title = form.save(commit=False) #TODO
        # card_title.author = self.request.user
        # card_title.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("card-detail", kwargs={'card_id': self.object.id})
