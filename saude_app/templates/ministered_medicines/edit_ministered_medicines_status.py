{% extends 'base.html' %}

{% load widget_tweaks %}

{% block title %}

    Adicionar Item de Medicamento Ministrado - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
        <h5><b>Alterar Status do Medicamento Ministrado</b></h5>
        <div class="row">
            <div class ="col-md-12">
                <form action="" method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="{{ form.status.id_for_label }}">Status</label>
                    {{ form.status|add_class:"form-control" }}
                </div>
                    <button type="submit" class="btn btn-primary">Alterar</button>       
                </form>
            </div>
        </div>
    </div>

{% endblock body %}
