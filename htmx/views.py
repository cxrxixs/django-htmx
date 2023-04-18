from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


def index(request):
    title = "Home"
    return render(request, "index.html", {"title": title})


def pokemon(request):
    title = "Pokemon"
    if request.META.get("HTTP_HX_REQUEST"):
        return render(request, "pages/pokemon.html", {"title": title})

    template = Template(
        """
        {% extends 'base.html' %}
        {% block content %}
        {% include 'pages/pokemon.html' %}
        {% endblock %}
        """
    )
    context = Context({"title": title})
    return HttpResponse(template.render(context))


'''
def htmx_page(request):
    return render(request, "htmx.html", {})

    if not request.META.get("HTTP_HX_REQUEST"):
        return render(request, "htmx.html", {"title": "first"})

    template = Template(
        """
        {% extends 'base.html' %}
        {% block content %}
        <div class="row">
        <h1 class='display-1'>hello</h1>
        </div>
        <div class='row'>{#% include 'search.html' %#}</div>
        {% endblock %}
        """
    )
    context = Context({"title": "This index"})
    return HttpResponse(template.render(context))
'''
