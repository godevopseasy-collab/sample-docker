const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello from Sample App!'));
app.listen(3000, () => console.log('Sample app running on port 3000'));
