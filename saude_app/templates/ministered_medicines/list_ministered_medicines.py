{% extends 'base.html' %}

{% block title %}

    Lista de Medicamentos Ministrados - {{ block.super }}

{% endblock title %}

{% block body %}

    <div class="container">
        <br />
        <h5><b>Lista de Medicamentos Ministrados</b></h5>
        <div class="row">
            <div class ="col-md-12">
            <br />
                <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Status</th>
                    <th scope="col">Paciente</th>
                    <th scope="col">Preco Total</th>
                    <th scope="col">Itens de Medicamentos Ministrados</th>
                    <th scope="col"></th>
                    <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    {% for ministered_medicines in ministered_medicines %}
                        <tr>
                            <th scope="row">
                                {% if ministered_medicines.status == 'Finalizado' or ministered_medicines.status == 'Cancelado' %}
                                    <p style="color:darkgray;" >{{ ministered_medicines.id }}</p>
                                {% else %}
                                    {{ ministered_medicines.id }}
                                {% endif %}
                            </th>
                            <td>
                                {% if ministered_medicines.status == 'Finalizado' or ministered_medicines.status == 'Cancelado' %}
                                    <p style="color:darkgray;" >{{ ministered_medicines.status }}</p>
                                {% else %}
                                    {{ ministered_medicines.status }}
                                {% endif %}
                            </td>
                            <td>
                                {% for patient in patients %}
                                    {% if ministered_medicines.patient_id == patient.id %}
                                        {% if ministered_medicines.status == 'Finalizado' or ministered_medicines.status == 'Cancelado' %}
                                            <p style="color:darkgray;" >{{ patient.first_name }} {{ patient.last_name }}</p>
                                        {% else %}
                                            {{ patient.first_name }} {{ patient.last_name }}
                                        {% endif %}
                                    {% endif %}
                                {% endfor %}   
                            </td>
                            <td>
                                {% if ministered_medicines.status == 'Finalizado' or ministered_medicines.status == 'Cancelado' %}
                                    <p style="color:darkgray;" >R$ {{ ministered_medicines.total_price }}</p>
                                {% else %}
                                    R$ {{ ministered_medicines.total_price }}
                                {% endif %}
                            </td>
                            <td>
                                {% if ministered_medicines.status == 'Finalizado' or ministered_medicines.status == 'Cancelado' %}
                                    <a href="#" class="btn btn-primary btn-sm disabled">Adicionar itens</a>
                                {% else %}
                                    <a href="{% url 'ministered_medicines:add_ministered_medicines_item' ministered_medicines.id %}" class="btn btn-primary btn-sm">Adicionar itens</a>
                                {% endif %}
                                <br /><br />
                                {% for ministered_medicines_item in ministered_medicines_items %}
                                    {% if ministered_medicines_item.ministered_medicines_id == ministered_medicines.id %}
                                        Quantidade: {{ ministered_medicines_item.quantity}}<br />
                                        Valor Unitario: R$ {{ ministered_medicines_item.unitary_price }}<br />
                                        <a href="{% url 'ministered_medicines:delete_ministered_medicines_item' ministered_medicines_item.id %}">Excluir Item</a><br /><br />
                                    {% endif %}
                                {% endfor %}
                            </td>
                            <td>
                                <a href="{% url 'ministered_medicines:edit_ministered_medicines_status' ministered_medicines.id %}" class="btn btn-danger btn-sm ">Alterar Status</a>
                            </td>
                            <td>
                                <a href="{% url 'ministered_medicines:delete_ministered_medicines' ministered_medicines.id %}" class="btn btn-danger btn-sm ">Excluir</a>
                            </td>
                        </tr> 
                    {% endfor %}
                </tbody>
                </table>
            </div>
        </div>
    </div>

{% endblock body %}