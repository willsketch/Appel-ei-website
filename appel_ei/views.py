from django.shortcuts import render
from .models import Images
# om info van de pagina's te editen , check de bijhorende html template
# Create your views here.
def index(request):
    """ home page of the website """
    images= Images.objects.order_by('date_added')
    context= {'images': images}
    return render(request, 'appel_ei/index.html', context)

def klant(request):
    """pagina voor klanten """
    return render(request, 'appel_ei/klant.html')
def vrijwilliger(request):
    """pagina voor vrijwilligers"""
    return render(request, 'appel_ei/vrijwilliger.html')

def contact(request):
    """pagina voor contact info """
    return render(request, 'appel_ei/contact.html')

def huidige_sponsors(request):
    """pagina voor huidige sponsors"""
    return render(request, 'appel_ei/huidige_sponsors.html')

def word_sponsor(request):
    """apgina voor word sponsor"""
    return render(request, 'appel_ei/word_sponsor.html')

def babbel_toren(request):
    """babbel toren pagina """
    return render(request, 'appel_ei/babbel_toren.html')

def kleding(request):
    """pagina voor kleding verkoop"""
    return render(request, 'appel_ei/kleding.html')

def speelgoed(request):
    """pagina voor speelgoed actie"""
    return render(request, 'appel_ei/speelgoed.html')

def kapper(request):
    """pagina voor kapper"""
    return render(request, 'appel_ei/kapper.html')

def sport(request):
    """pagina voor sport"""
    return render(request, 'appel_ei/sport.html')

def huiswerk(request):
    """pagina voor huiswerk begeleiding"""
    return render(request, 'appel_ei/huiswerk.html')

def ontspanning(request):
    """pagina voor ontspanning"""
    return render(request, 'appel_ei/ontspanning.html')

def about(request):
    """pagina voor ons verhaal """
    return render(request, 'appel_ei/about.html')

def winkel(request):
    """pagina voor onze winkel"""
    return render(request, 'appel_ei/winkel.html')

def ontmoetingsruimte(request):
    """pagina voor ontmoetingsruimte"""
    return render(request, 'appel_ei/ontmoetingsruimte.html')

def homepage1(request):
    """home page 1 trial page"""
    return render(request, 'appel_ei/homepage1.html')

def homepage2(request):
    """home page 2 trial page"""
    return render(request, 'appel_ei/homepage2.html')