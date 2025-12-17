const express = require('express');
const app = express();
//listen
app.listen(5001, () => {
    console.log('Server is running on port 5001');
});
//route
app.get('/', (req, res) => {
    res.send('<h1> Hello Sharda World!');
});


