
/*Sidebar*******************************************/

var hamburger = document.querySelector(".hamburger");
hamburger.addEventListener("click", function(){
    document.querySelector("body").classList.toggle("active");
})


/*Modals************************** */
function abrir_modal_edit(url){
    $('#edit').load(url, function(){
        $(this).modal('show');
    });
}   

function abrir_view_modal(url){
    $('#view').load(url, function(){
        $(this).modal('show');
    });
}

function delete_modal(url){
    $('#delete').load(url, function(){
        $(this).modal('show');
    });
}

function activate_modal(url){
    $('#activate').load(url, function(){
        $(this).modal('show');
    });
}


function abrir_modal_create(url){
    $('#create').load(url, function(){
        $(this).modal('show');
    });
}

function cerrar_modal_create(){
    $('#create').modal('hide');
}

function abrir_modal_accidenteAtendido(url){
    $('#atendido').load(url, function(){
        $(this).modal('show');
    });
}

function cerrar_modal_create(){
    $('#atendido').modal('hide');
}

/*
Validar texto
*/
/*
function validateText(){

    let regEx = /^[A-Z0-9_ ]+$/;
    let texto = document.getElementById('id_placas_vehiculo')

    if(texto.value.match(regEx)){
       
        activarBoton();
        return true;
    }else{
        texto.innerHTML.value = "ERROR";
        bloquearBoton();
        return false;
    }
}
*/

function bloquearBoton(){
    $('#guardar').prop('disabled', true);
}

function activarBoton(){
    $('#guardar').prop('disabled', false);
}