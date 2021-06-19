const WebSocket = require('ws')
users=[]
const wss = new WebSocket.Server({ port: 669 });

wss.on('connection',ws=>{
    users.push(ws)
    ws.on('message',msg=>{
        users.forEach(element => {
            
            element.send(msg)
        });
    })


});