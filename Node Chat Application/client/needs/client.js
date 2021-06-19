


let ws=new WebSocket('ws://5c74b64afa35.ngrok.io:669');
ws.onopen=()=>{

    ws.onmessage=({data})=>{
        console.log(data)
        let myobj=JSON.parse(data);
        if (myobj.name!==localStorage.getItem('username')){
            client_change(myobj.name,myobj.msg);
        }
    }
}

    
let user_name=prompt('Enter your name to chat');
if(user_name!=='' || user_name!=='null'){
    localStorage.setItem('username',user_name);
    
}




let keyboard=document.querySelector('.text');
keyboard.addEventListener('keypress',clicked,false);




function change_msg(value){
let send=`<div class="container1">
<div class="right">
${value}
</div>
</div>`;

let main_div=document.querySelector('.main-section');
let all_element=main_div.innerHTML;

main_div.innerHTML=all_element+send;

}




function clicked(n){
if(n.key=='Enter'){
    let msg=document.querySelector('.text');
    if(msg.value!==''){
        change_msg(msg.value)
        send_msg(msg.value);
        msg.value=''
        
    }
}
}

function send_msg(value){
    user_info={};
    user_info['name']=localStorage.getItem('username');
    user_info['msg']=value
    ws.send(JSON.stringify(user_info));
}

function client_change(a,b){
    let receive=`<div class="container">
    <div class="left">
        <b>${a}:</b>
        ${b}
    </div>
    </div>`;
    let main_div=document.querySelector('.main-section');
    let all_element=main_div.innerHTML;
    
    main_div.innerHTML=all_element+receive;
}