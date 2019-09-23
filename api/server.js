const http = require('http');
const app = require('./app');

const port = process.env.PORT || 3000;

const server = http.createServer(app);

console.log("Starting node server on port: " + port);
console.log(`Navigate your browser to http://localhost:${port}/ to use thisiship.`);
server.listen(port);

