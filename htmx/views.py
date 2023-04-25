import time

from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


def index(request):
    title = "Home"
    return render(request, "index.html", {"title": title})


def render_component(request, component):
    request.status_code = 200
    context = Context({})

    if component == "instant":
        template = Template(
            """
            <h1>Instant loading component</h1>
            """
        )

        return HttpResponse(template.render(context))

    if component == "fast":
        time.sleep(0.9)
        template = Template(
            """
            <h1>Fast loading component</h1>
            """
        )

        return HttpResponse(template.render(context))

    if component == "slow":
        time.sleep(3.6)
        template = Template(
            """
            <h1>Slow loading component</h1>
            """
        )

        return HttpResponse(template.render(context))

    template = Template(
        """
        <h1>Not found</h1>
        """
    )

    return HttpResponse(template.render(context))


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
