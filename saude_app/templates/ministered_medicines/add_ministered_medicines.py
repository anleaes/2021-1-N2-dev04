{% extends 'base.html' %}

{% load widget_tweaks %}

{% block title %}

    Adicionar Medicamento Ministrado - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
    <h5><b>Deseja abrir um pedido? </b></h5>
        <div class="row">
            <div class ="col-md-12">
                <form action="" method="POST">
                {% csrf_token %}
                    <button type="submit" class="btn btn-primary btn-sm">Sim</button>   <a href="{% url 'patients:list_patients' %}" class="btn btn-primary btn-sm">Nao</a>     
                </form>
                
            </div>
        </div>
    </div>

{% endblock body %}