//Datatable
function listarDatos(){
    $.ajax({
        url: "/data-bitacora/",
        type: 'get',  
        dataType: 'json',
        processing: true,
        dataSrc:"",
        success: function(response){
            if($.fn.DataTable.isDataTable('#bitacora_table')){
                $('#bitacora_table').DataTable().destroy();
                console.log("TABLA 1 DESTRUIDA")
            }
            if($.fn.DataTable.isDataTable('#bitacora_table2')){
                $('#bitacora_table2').DataTable().destroy();
                console.log("TABLA 2 DESTRUIDA")
            }
            console.log(response);
        $('#bitacora_table tbody').html("");
        for(let i=0; i<response.length; i++){
            
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['motivo'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-bitacora/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg></button>';
            fila+='<button class="btn btn-warning" id= "modalButton" onclick="abrir_modal_edit(\'/update-bitacora/'+ response[i]['pk']+'/\')">';
            fila +='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">';
            fila += '<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>';
            fila += ' <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>';
            fila += ' </svg></button>';
            fila+='<button class="btn btn-danger" id= "modalButton" onclick="delete_modal(\'/delete-bitacora/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += '<path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#bitacora_table tbody').append(fila);
        }

        $('#bitacora_table2 tbody').html("");
        for(let i=0; i<response.length; i++){
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';   
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['motivo'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-bitacora/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg></button>';
            fila+='<button class="btn btn-warning" id= "modalButton" onclick="abrir_modal_edit(\'/update-bitacora/'+ response[i]['pk']+'/\')">';
            fila +='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">';
            fila += '<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>';
            fila += ' <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>';
            fila += ' </svg></button>';
            fila+='<button class="btn btn-success" id= "modalButton" onclick="activate_modal(\'/activate-bitacora/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#bitacora_table2 tbody').append(fila);
        }
        
        $('#bitacora_table').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
            ],

            language: {
                decimal: "",
                emptyTable: "No hay información",
                info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                infoFiltered: "(Filtrado de _MAX_ total entradas)",
                infoPostFix: "",
                thousands: ",",
                lengthMenu: "Mostrar _MENU_ Entradas",
                loadingRecords: "Cargando...",
                processing: "Procesando...",
                search: "Buscar:",
                searchPlaceholder: "Buscar palabras incluidas en el folio",
                zeroRecords: "Sin resultados encontrados",
                paginate: {
                  first: "Primero",
                  last: "Ultimo",
                  next: "Siguiente",
                  previous: "Anterior",
                },
              },    
        });

        $('#bitacora_table2').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
            ],


            language: {
                decimal: "",
                emptyTable: "No hay información",
                info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                infoFiltered: "(Filtrado de _MAX_ total entradas)",
                infoPostFix: "",
                thousands: ",",
                lengthMenu: "Mostrar _MENU_ Resultados",
                loadingRecords: "Cargando...",
                processing: "Procesando...",
                search: "Buscar:",
                searchPlaceholder: "Buscar palabras incluidas en el folio",
                zeroRecords: "Sin resultados encontrados",
                paginate: {
                  first: "Primero",
                  last: "Ultimo",
                  next: "Siguiente",
                  previous: "Anterior",
                },
              },    
        });


        /*
        FILTRAR REGISTROS ACTIVOS E INACTIVOS,
        LA INFORMACION SE CARGA 1 SOLA VEZ Y SE FILTRA PARA CADA TABLA
        */

        $('#bitacora_table').DataTable().columns(1)
        .search('^ACTIVO$', true, false)
        .draw();

        $('#bitacora_table2').DataTable().columns(1)
        .search('^INACTIVO$', true, false)
        .draw();

    }
});    

}

//Filtro de busqueda por fechas
var minDate, maxDate;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate.val();
        var max = maxDate.val();
        var date = new Date( data[2] );
 
        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);


var minDate2, maxDate2;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate2.val();
        var max = maxDate2.val();
        var date = new Date( data[2] );
 
        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);


$(document).ready(function(){

    minDate = new DateTime($('#filtrar_fecha'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate = new DateTime($('#filtrar_fecha2'), {
        format: 'dddd, MMMM Do YYYY',
    });


    minDate2 = new DateTime($('#filtrar_fecha3'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate2 = new DateTime($('#filtrar_fecha4'), {
        format: 'dddd, MMMM Do YYYY',
    });


    listarDatos();

    $('#filtrar_fecha, #filtrar_fecha2').on('change', function () {
        $('#bitacora_table').DataTable().draw();
    });

    $('#filtrar_fecha3, #filtrar_fecha4').on('change', function () {
        $('#bitacora_table2').DataTable().draw();
    });

});
