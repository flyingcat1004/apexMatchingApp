from django.shortcuts import render
from .forms import TestForm
from .models import SiteUser

# Create your views here.
def test_template(request):
    form = TestForm()
    siteusers = SiteUser.objects.all()
    context = {'test': 'aaa', 'form': form, 'siteusers': siteusers}
    return render(request, 'matchapp/test.html', context)
