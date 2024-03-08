var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
    fs.stat("./server.js", (error, stats) => { 
        console.log(stats); 
      });
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(body);
    return res.end();
}).listen(9090); 