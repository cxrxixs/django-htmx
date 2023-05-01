import time

from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


def index(request):
    title = "Home"
    return render(request, "pages/index.html", {"title": title})


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
    context = Context({"title": title})
    return HttpResponse(template.render(context))


def pokemon_page(request, name):
    title = "Pokemon Solo"
    pokemon_name = name
    template_1 = Template(
        f"""
        Pokemon: {name}
        """
    )

    template_2 = Template(
        """
        {% extends 'layout/base.html' %}
        {% block content %}
        {% include 'components/pokemon-details.html' %}
        {% endblock %}
        """
    )

    template_3 = Template(
        """
        {% extends 'layout/base.html' %}
        {% block content %}
        <div x-data="{ visible: true, title: '{{ title }}' }"
        x-init="document.title = `${document.title.split('|')[0]} | ${title}`"
        class="row">
        <template x-if="visible">
        {% include "pages/pokemon.html" %}
        </template>
        </div>
        {% endblock %}
        """
    )
    context = Context({"title": title})
    # return HttpResponse(template_2.render(context))

    payload = {
        "title": title,
        "pokemonName": pokemon_name,
    }

    return render(request, "pages/pokemon-solo-view.html", context={"payload": payload})
