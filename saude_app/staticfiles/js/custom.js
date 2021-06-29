$(document).ready(function(){
    $('#id_professional_specialty').select2({
        placeholder: 'Especialidades',
        allowClear: true
    });
    $('#id_health_professional').select2();
    $('#id_patients').select2();
    $('#id_patient').select2();
});