from django.shortcuts import render


# Create your views here.
def test_template(request):
    myapp_data = {'test': 'aaa'}
    return render(request, 'test.html', myapp_data)
