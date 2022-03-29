from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'lenta/index.html', {})


class AboutView(View):
    def get(self, request):
        return render(request, 'lenta/about.html', {})


# class TestView(View):
#     data = {
#         'name': 'Nikita',
#         'place': 'Russia'
#     }

countries = [{"id": "australia", "title": "Австралия", "continent": "aus"},
             {"id": "india", "title": "Индия", "continent": "asi"},
             {"id": "poland", "title": "Польша", "continent": "eur"},
             {"id": "mexico", "title": "Мексика", "continent": "amr"}, ]


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lenta/index.html', {})


def TestView1(request):
    context = {'countries': countries}
    return render(request, 'lenta/index.html', context=context)


def tags(request, tags: str):
    return render(request, 'lenta/about.html', context={'tags': tags})

# def main(request):
#     return render(request, 'lenta/index.html')
