$(document).ready(function() {
    $('#id_birth').mask('00/00/0000', {placeholder: "__/__/____"});
    $('#id_date').mask('00/00/0000', {placeholder: "__/__/____"});
    $('#id_date_fabrication').mask('00/00/0000', {placeholder: "__/__/____"});
    $('#id_cell_phone').mask('(00) 00000-0000');
    $('.cpf-mask').mask('000.000.000-00');
});
