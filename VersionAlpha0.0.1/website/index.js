const express = require('express');
const app = express();

// create route handler and asociate it with a given route
app.get('/', (req, res) => {
   res.send({ hi: 'there' });
});

app.listen(5000);