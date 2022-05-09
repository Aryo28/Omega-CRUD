//Datatable
function listarDatos(){
    $.ajax({
        url: "/accidentes-data/",
        type: 'get',  
        dataType: 'json',
        processing: true,
        dataSrc:"",
        success: function(response){
            if($.fn.DataTable.isDataTable('#accidentes1')){
                $('#accidentes1').DataTable().destroy();
                
            }
            if($.fn.DataTable.isDataTable('#accidentes2')){
                $('#accidentes2').DataTable().destroy();
               
            }
            if($.fn.DataTable.isDataTable('#accidentes3')){
                $('#accidentes3').DataTable().destroy();
               
            }
            if($.fn.DataTable.isDataTable('#accidentes4')){
                $('#accidentes4').DataTable().destroy();
                
            }
            console.log(response);
        $('#accidentes1 tbody').html("");
        for(let i=0; i<response.length; i++){
            
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus_accidente'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
            fila += '<td>' + response[i]["fields"]['colonia'] + '</td>';
            fila += '<td>' + response[i]["fields"]['sector'] + '</td>';
            fila += '<td>' + response[i]["fields"]['jurisdiccion'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-accidente/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg> ABRIR</button>';
            fila+='<button class="btn btn-danger" id= "modalButton" onclick="delete_modal(\'/delete-accidentes/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += '<path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#accidentes1 tbody').append(fila);
        }
        $('#accidentes2 tbody').html("");
        for(let i=0; i<response.length; i++){
            
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus_accidente'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
            fila += '<td>' + response[i]["fields"]['colonia'] + '</td>';
            fila += '<td>' + response[i]["fields"]['sector'] + '</td>';
            fila += '<td>' + response[i]["fields"]['jurisdiccion'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-accidente/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg> ABRIR</button>';
            fila+='<button class="btn btn-danger" id= "modalButton" onclick="delete_modal(\'/delete-accidentes/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += '<path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#accidentes2 tbody').append(fila);
        }
        $('#accidentes3 tbody').html("");
        for(let i=0; i<response.length; i++){
            
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus_accidente'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
            fila += '<td>' + response[i]["fields"]['colonia'] + '</td>';
            fila += '<td>' + response[i]["fields"]['sector'] + '</td>';
            fila += '<td>' + response[i]["fields"]['jurisdiccion'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-accidente/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg> ABRIR</button>';
            fila+='<button class="btn btn-danger" id= "modalButton" onclick="delete_modal(\'/delete-accidentes/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += '<path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#accidentes3 tbody').append(fila);
        }

        $('#accidentes4 tbody').html("");
        for(let i=0; i<response.length; i++){
            let fila = '<tr>';
            fila += '<td>' + (i+1) + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus'] + '</td>';
            fila += '<td>' + response[i]["fields"]['estatus_accidente'] + '</td>';
            fila += '<td>' + response[i]["fields"]['fecha'] + '</td>';
            fila += '<td>' + response[i]["fields"]['hora'] + '</td>';
            fila += '<td>' + response[i]["fields"]['unidad'] + '</td>';
            fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
            fila += '<td>' + response[i]["fields"]['colonia'] + '</td>';
            fila += '<td>' + response[i]["fields"]['sector'] + '</td>';
            fila += '<td>' + response[i]["fields"]['jurisdiccion'] + '</td>';
            fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
            fila += '<td style ="width:15%">';

            fila+='<button class="btn btn-primary" id= "modalButton" onclick="abrir_view_modal(\'/show-accidente/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>';
            fila += ' <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>';
            fila += ' </svg> ABRIR</button>';
            fila+='<button class="btn btn-success" id= "modalButton" onclick="activate_modal(\'/activate-accidentes/'+ response[i]['pk']+'/\')">';
            fila +=' <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">';
            fila += ' <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>';
            fila += ' </svg></button>';

            fila+='</td>';
            fila += '</tr>';
            $('#accidentes4 tbody').append(fila);
        }

        $('#accidentes1').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
                {
                    "targets": [ 2 ], //Corresponde
                    "visible": false,
                }
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
        $('#accidentes2').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
                {
                    "targets": [ 2 ], //Corresponde
                    "visible": false,
                }
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
        $('#accidentes3').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
                {
                    "targets": [ 2 ], //Corresponde
                    "visible": false,
                }
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
        $('#accidentes4').DataTable({

            //La columna de estatus se utiliza para filtrar pero no es visible al uruario
            "columnDefs": [
                {
                    "targets": [ 1 ], //Corresponde a la posicion de la columna estatus
                    "visible": false,
                    
                },
                {
                    "targets": [ 2 ], //Corresponde
                    "visible": false,
                }
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
        $('#accidentes1').DataTable().columns(1)
        .search('^ACTIVO$', true, false).columns(2).search('^ATENDIDO$', true, false)
        .draw();

        $('#accidentes2').DataTable().columns(1)
        .search('^ACTIVO$', true, false).columns(2).search('^NO ATENDIDO$', true, false)
        .draw();

        $('#accidentes3').DataTable().columns(1)
        .search('^ACTIVO$', true, false)
        .draw()

        $('#accidentes4').DataTable().columns(1)
        .search('^INACTIVO$', true, false)
        .draw();

     

    }
});    

}

//Filtro de busqueda por fechas
var minDate1, maxDate1;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate1.val();
        var max = maxDate1.val();
        var date = new Date( data[3] );
 
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


//Filtro de busqueda por fechas
var minDate2, maxDate2;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate2.val();
        var max = maxDate2.val();
        var date = new Date( data[3] );
 
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
//Filtro de busqueda por fechas
var minDate3, maxDate3;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate3.val();
        var max = maxDate3.val();
        var date = new Date( data[3] );
 
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

//Filtro de busqueda por fechas
var minDate4, maxDate4;

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate4.val();
        var max = maxDate4.val();
        var date = new Date( data[3] );
 
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

    minDate1 = new DateTime($('#filtrar_fecha1'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate1 = new DateTime($('#filtrar_fecha2'), {
        format: 'dddd, MMMM Do YYYY',
    });

    minDate2 = new DateTime($('#filtrar_fecha3'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate2 = new DateTime($('#filtrar_fecha4'), {
        format: 'dddd, MMMM Do YYYY',
    });
    minDate3 = new DateTime($('#filtrar_fecha5'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate3 = new DateTime($('#filtrar_fecha6'), {
        format: 'dddd, MMMM Do YYYY',
    });
    minDate4 = new DateTime($('#filtrar_fecha7'), {
        format: 'dddd, MMMM Do YYYY',
    });

    maxDate4 = new DateTime($('#filtrar_fecha8'), {
        format: 'dddd, MMMM Do YYYY',
    });

    listarDatos();

    $('#filtrar_fecha1, #filtrar_fecha2').on('change', function () {
        $('#accidentes1').DataTable().draw();
    });

    $('#filtrar_fecha3, #filtrar_fecha4').on('change', function () {
        $('#accidentes2').DataTable().draw();
    });

    $('#filtrar_fecha5, #filtrar_fecha6').on('change', function () {
        $('#accidentes3').DataTable().draw();
    });

    $('#filtrar_fecha7, #filtrar_fecha8').on('change', function () {
        $('#accidentes4').DataTable().draw();
    });
});