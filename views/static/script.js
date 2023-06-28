// document.onkeydown = (e) => {
//     if (e.ctrlKey && e.shiftKey && e.key == 'I' || e.ctrlKey && e.shiftKey && e.key == 'i') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.shiftKey && e.key == 'C'|| e.ctrlKey && e.shiftKey && e.key == 'c') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.shiftKey && e.key == 'J' || e.ctrlKey && e.shiftKey && e.key == 'j') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.key == 'U' || e.ctrlKey && e.key == 'u') {
//         e.preventDefault();
//     }
// };

let SORT_BY = "name";

async function add_person(){
    if (ensure_no_space() && ensure_number() && await ensure_date()){
        var date = $("#due_date").val();
        var loan = $("#loan_amount").val()
        var name = $("#loan_name").val();
        await eel.add_debt(name, loan, date);
        $("#unsuccessful").css("display", "none")
        $("#add_success").css("display", "inline-block");
        await order_page(SORT_BY);
        $("#debt_data")

    }
    else{
        $("#unsuccessful").css("display", "inline-block")
    }
}

function close_win(){
    $("table").css({"-webkit-filter": "blur(0)", "filter" : "blur(0)"})
    $("#add_loan").css("display", "none");
    $("#loan_amount, #loan_name, #due_date").val("");
    $("#loan_amount, #loan_name, #due_date").css({"border" : "black solid 1px", "outline" : "none"})
}

async function ensure_date(){
    var datetime = $("#due_date").val();
    if (datetime){
        if(await eel.date_checker(datetime)()){
            $("#due_date").css({"border" : "black solid 1px", "outline" : "none"})
            return true
        }
        $("#due_date").css({"border" : "red solid 1px", "outline" : "red solid 1px"})
        return false
    }
    $("#due_date").css({"border" : "red solid 1px", "outline" : "red solid 1px"})
    return false
}

function ensure_no_space(){
    var val = document.getElementById("loan_name");
    if (val.value.trim() === ""){
        $("#loan_name").css({"outline":"red solid 1px", "border":"solid red 1px"});
        return false
    }
    else{
        val.style = "revert";
        return true
    }
}

function ensure_number(){
    var amount = $("#loan_amount").val()
    if ($.isNumeric(amount)){
        if (amount <= 0 ){
            $("#loan_amount").css({"border" : "red solid 1px", "outline" : "red solid 1px"});
            return false;
        }
        else{
            $("#loan_amount").css({"border" : "black solid 1px", "outline" : "none"});
            return true;
        }
    }
    else{
        $("#loan_amount").css({"border" : "red solid 1px", "outline" : "red solid 1px"});
        return false;
    }
}

function loan(){
    var table = document.querySelector("table");
    if (!(table.style.filter) || table.style.filter === "blur(0px)"){
        $("#add_loan").css("display", "revert");
        $("table").css({"-webkit-filter": "blur(6px)", "filter" : "blur(6px)"});
    }
}

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

async function order_page(event){
    let inner = [];
    try{
        var order = event.srcElement.innerHTML;
    }
    catch(err){
        var order = event;
    }
    SORT_BY = order;
    var datas = await eel.fetch_data(order)();
    for (data of datas){
        var name = data.name.replace('<', '&lt;').replace('&', '&amp;');
        var due_date = data.due_date.replace('<', '&lt;').replace('&', '&amp;');
        inner+= '<tr>' + 
                    '<td id="hasdhhj_v">' + name + '</td>' + 
                    '<td>' + data.loan + '</td>'+
                    '<td>' + data.balance + '</td>'+
                    '<td>' + due_date + '</td>'+
                    '<td class=actions>'+
                        '<b onclick=lessen_debt()>ADD</b> | '+
                        '<b onclick="remove('+ data.id +')">REMOVE</b>'+
                    '</td>'+
                '</tr>'
    }
    document.querySelector("tbody").innerHTML = inner;
}

async function passChange(){
    var confirmed = document.getElementById("confirmation").value;
    await eel.change_pass(confirmed);
    $("#pass_data").css("display", "none");
    $("#success").css("display", "block"); 
    $("#change_pass").css("top", "-25%");
}

async function remove(id){
    await eel.remover(id);
    await order_page(SORT_BY);
    $("#debt_data")
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