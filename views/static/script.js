//Deactivated as of now as it is in devlopment
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
//     if (e.ctrlKey && e.shiftKey && e.key == 'N' || e.ctrlKey && e.shiftKey && e.key == 'n') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.shiftKey && e.key == 'T' || e.ctrlKey && e.shiftKey && e.key == 't') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.key == 'U' || e.ctrlKey && e.key == 'u') {
//         e.preventDefault();
//     }
//     if (e.ctrlKey && e.key == 'T' || e.ctrlKey && e.key == 't') {
//         e.preventDefault();
//     if (e.ctrlKey && e.key == 'N' || e.ctrlKey && e.key == 'n') {
//         e.preventDefault();
//     if (e.ctrlKey && e.key == 'H' || e.ctrlKey && e.key == 'h') {
//         e.preventDefault();  
//     if (e.ctrlKey && e.key == 'S' || e.ctrlKey && e.key == 's') {
//         e.preventDefault();
// };

let SORT_BY = "name";

async function add_person(due_date_id, loan_amount_id){
    if (ensure_no_space() && ensure_number(loan_amount_id) && await ensure_date(due_date_id)){
        var date = $("#due_date").val();
        var loan = $("#loan_amount").val()
        var name = $("#loan_name").val();
        await eel.add_debt(name, loan, date);
        $("#unsuccessful").css("display", "none")
        $("#add_success").css("display", "inline-block");
        setTimeout(() => {
            $("#add_success").css("display", "none");
        }, 2000)
        await order_page(SORT_BY);
        $("#loan_amount, #loan_name, #due_date").val("");
        $("#debt_data")

    }
    else{
        $("#unsuccessful").css("display", "inline-block")
        $("#add_success").css("display", "none");
    }
}

function close_payment(){
    $("#payment_con").css("display","none");
    document.getElementById("payment_con").innerHTML = [];
}

function close_confirm(id){
    var close_id = "#"+id;
    $(close_id).css("display","none");
}

function close_win(){
    $("table").css({"-webkit-filter": "blur(0)", "filter" : "blur(0)"})
    $("#add_loan, #add_success, #unsuccessful").css("display", "none");
    $("#loan_amount, #loan_name, #due_date").val("");
    $("#loan_amount, #loan_name, #due_date").css({"border" : "black solid 1px", "outline" : "none"})
}

async function ensure_date(id, due=""){
    if (due != ""){
        var due_id = "#"+due;
        var due_d = $(due_id).val();
    }
    else{
        due_d = "";
    }
    var ids = "#"+id;
    var datetime = $(ids).val();
    if (datetime){
        if(await eel.date_checker(datetime, due_d)()){
            $(ids).css({"border" : "black solid 1px", "outline" : "none"})
            return true
        }
        $(ids).css({"border" : "red solid 1px", "outline" : "red solid 1px"})
        return false
    }
    $(ids).css({"border" : "red solid 1px", "outline" : "red solid 1px"})
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

function ensure_number(input_id){
    var inputID = "#"+input_id;
    var amount = $(inputID).val()
    if (!($.isNumeric(amount)) || !(amount)){
        $(inputID).css({"border" : "red solid 1px", "outline" : "red solid 1px"});
        return false;
    }
    else{
        if (amount <= 0 ){
            $(inputID).css({"border" : "red solid 1px", "outline" : "red solid 1px"});
            return false;
        }
        else{
            $(inputID).css({"border" : "black solid 1px", "outline" : "none"});
            return true;
        }
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
    var stats = await eel.login(password)();
    var obj = JSON.parse(stats)
    if (obj.code === 200){
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
    catch{
        var order = event;
    }
    SORT_BY = order;
    var name_to_search = $("#name_search").val();
    var datas = JSON.parse(await eel.fetch_data(order, name_to_search+"%")());
    for (let data of datas){
        var name = data.name.replace('<', '&lt;').replace('&', '&amp;');
        var due_date = data.due_date.replace('<', '&lt;').replace('&', '&amp;');
        inner+= '<tr>' + 
                    '<td id="hasdhhj_v">' + name + '</td>' + 
                    '<td>' + data.loan + '</td>'+
                    '<td>' + data.balance + '</td>'+
                    '<td>' + due_date + '</td>'+
                    '<td class=actions>'+
                        '<b onclick=payment_function('+ data.id +')>PAY</b> | '+
                        '<b onclick="remove_show('+ data.id +')">REMOVE</b>'+
                    '</td>'+
                '</tr>'
    }
    if (inner != ""){
        document.querySelector("tbody").innerHTML = inner;
        $("#no_data").css("display", "none");
    }
    else{
        document.querySelector("tbody").innerHTML = []
        $("#no_data").css("display", "block");
    }
}

async function passChange(){
    var confirmed = document.getElementById("confirmation").value;
    await eel.change_pass(confirmed);
    $("#pass_data").css("display", "none");
    $("#success").css("display", "block"); 
    $("#change_pass").css("top", "-25%");
}

async function payment_function(id){
    var conElement = document.getElementById('payment_con');
    conElement.innerHTML = [];
    var user_data = JSON.parse(await eel.fetch_single_user(id)())[0];
    var safe_name = user_data.name.replace('<', '&lt;').replace('&', '&amp;');
    var safe_due_date = user_data.due_date.replace('<', '&lt;').replace('&', '&amp;');
    let template = '<div class="payment_content">' +
                        '<span onclick="close_payment()" class="close">✖</span>' +
                        '<b>Payment For: ' + safe_name + '</b>' +
                        '<p id="balansya">Balance: '+ user_data.balance +'</p>' +
                        '<p id="lastP">Due Date: '+ safe_due_date +'</p>' +
                        '<input type="hidden" id="due_val" value='+ safe_due_date+'>'+
                        '<input type="hidden" id="user_id" value='+ user_data.id+'>' +
                        '<form>' +
                            '<div>' +
                                '<p>Payment Amount</p>' +
                                '<input type="number" id="paymentAmount" autofocus autocomplete="off" placeholder="Amount" onkeyup="ensure_number(\'paymentAmount\')">'+
                            '</div>' +
                            '<div>' +
                                '<p>Date Paid</p>' +
                                '<input type="date" id="tryMe" onchange="ensure_date(id=\'tryMe\',due=\'due_val\')">'+
                            '</div>' +
                            '<button type="button" onclick="paydebt()">' +
                                '<p id="paymentBTN">Add Payment</p>'+
                                '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>' +
                            '</button>'+
                            '<b id="pay_success" style="display: none">Paid!</b><b id="pay_error" style="display: none">Check Your Input!</b>'
                        '</form>' +
                    '</div>';
    conElement.innerHTML = template.trim();
    conElement.style.display = "block";
}

async function paydebt(){
    if (await ensure_date(id='tryMe',due='due_val') && ensure_number('paymentAmount')){
        $("#paymentBTN").css("display", "none")
        var user_id = $("#user_id").val();
        var amount_paid = $("#paymentAmount").val();
        var datepaid = $("#tryMe").val();
        $(".lds-ellipsis").css("display", "block")
        var stats = await eel.debtpay(user_id, amount_paid, datepaid);
        setTimeout(() => {
            $(".lds-ellipsis").css("display", "none");
            $("#paymentBTN").css("display", "block")
        }, 3000);
    }
    else{
        $("#pay_error").css("display", "inline-block");
    }
}

async function remove(){
    var id_rmf = $("#hid").val();
    var passWord = $("#pasd").val();
    if (await eel.login(passWord)()){
        $("#pasd").css({"border" : "black solid 1px", "outline" : "none"});
        await eel.remover(id_rmf);
        await order_page(SORT_BY);
    }
    else{
        $("#pasd").css({"border" : "red solid 1px", "outline" : "red solid 1px"});
    }
    close_confirm("confirm_div");

}

function remove_show(id){
    $("#confirm_div").css("display","block");
    $("#hid").val(id);
}

async function search_p(){
    var name_to_search = $("#name_search").val();
    var datas = JSON.parse(await eel.fetch_data(SORT_BY, name_to_search+"%")());
    let inner = [];
    for (let data of datas){    
        var name = data.name.replace('<', '&lt;').replace('&', '&amp;');
        var due_date = data.due_date.replace('<', '&lt;').replace('&', '&amp;');
        inner+= '<tr>' + 
                    '<td id="hasdhhj_v">' + name + '</td>' + 
                    '<td>' + data.loan + '</td>'+
                    '<td>' + data.balance + '</td>'+
                    '<td>' + due_date + '</td>'+
                    '<td class=actions>'+
                        '<b onclick=payment_function('+ data.id +')>PAY</b> | '+
                        '<b onclick="remove_show('+ data.id +')">REMOVE</b>'+
                    '</td>'+
                '</tr>'
    }
    if (inner != ""){
        document.querySelector("tbody").innerHTML = inner;
        $("#no_data").css("display", "none");
    }
    else{
        document.querySelector("tbody").innerHTML = []
        $("#no_data").css("display", "block");
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