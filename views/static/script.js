async function logg(){
    var password = document.getElementById("password").value;
    var status = await eel.login(password)();
    if (status){
        window.location.href = "../templates/index.html";
    }
    else{
        $("#error_code").css("display", "inline-block");
    }
}


function show_change_pass(){
    $("#success").css("display", "none");
    $("#pass_data").css("display", "block");
    $("#new_password, #confirmation").css({"border" : "black solid 1px", "outline" : "none"});
    $("#new_password, #confirmation").val("")
    var show = document.getElementById("change_pass");
    if (show.style.top === "-25%" || !(show.style.top)){
        $("#change_pass").css({"display":"block", "top" : "10%"})
    }
    else{
        show.style.top = "-25%";
    }
    validate();
}

async function validate(){
    var NewPassword = document.getElementById("new_password");
    var confirmation = document.getElementById("confirmation");
    var changeBtn = document.getElementById("changeP");
    changeBtn.disabled = true;
    if (NewPassword.value.trim() === "" || confirmation.value.trim() === ""){
        changeBtn.disabled = true;
    }
    else{
        if (NewPassword.value.trim() != confirmation.value.trim() || await eel.login(confirmation.value.trim())()){
            $("#new_password, #confirmation").css({"border" : "red solid 1px", "outline":"red solid 1px"})
            changeBtn.disabled = true;
        }
        else{
            $("#new_password, #confirmation").css({"border" : "green solid 1px", "outline":"green solid 1px"})
            changeBtn.disabled = false;
        }
    }
}

async function passChange(){
    var confirmed = document.getElementById("confirmation").value;
    await eel.change_pass(confirmed);
    $("#pass_data").css("display", "none");
    $("#success").css("display", "block"); 
    $("#change_pass").css("top", "-25%");
}   

function loan(){
    var table = document.querySelector("table");
    if (!(table.style.filter) || table.style.filter === "blur(0px)"){
        $("#add_loan").css("display", "revert");
        $("table").css({"-webkit-filter": "blur(6px)", "filter" : "blur(6px)"});
    }
}

function close_win(){
    $("table").css({"-webkit-filter": "blur(0)", "filter" : "blur(0)"})
    $("#add_loan").css("display", "none");
    $("#loan_amount").val("");
    $("#loan_name").val("");
}

function ensure_no_space(){
    var val = document.getElementById("loan_name");
    if (val.value.trim() === ""){
        $("#loan_name").css({"outline":"red solid 1px", "border":"solid red 1px"});
    }
    else{
        val.style = "revert";
    }
}

function ensure_number(){
    alert($("#loan_amount").val())
}

async function add_person(){

}