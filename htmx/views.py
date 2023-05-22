import time

from core.context_processors import git_version
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


def index(request):
    title = "Home"

    context = {
        "title": title,
    }
    return render(request, "pages/index.html", context=context)


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
        {% extends 'layout/base.html' %}
        {% block content %}
        {% include 'pages/pokemon.html' %}
        {% endblock %}
        """
    )
    context = Context(
        {
            "title": title,
        }
    )
    context.update(git_version(request))

    return HttpResponse(template.render(context))


def pokemon_page(request, name):
    title = "Pokemon Solo"
    pokemon_name = name

    payload = {
        "title": title,
        "pokemonName": pokemon_name,
    }

    if request.META.get("HTTP_HX_REQUEST"):
        return render(request, "pages/pokemon-solo-view.html", {"payload": payload})

    template = Template(
        """
        {% extends 'layout/base.html' %}
        {% block content %}
        {% include 'pages/pokemon-solo-view.html' %}
        {% endblock %}
        """
    )

    context = Context(
        {
            "payload": payload,
        }
    )

    context.update(git_version(request))

    return HttpResponse(template.render(context))
