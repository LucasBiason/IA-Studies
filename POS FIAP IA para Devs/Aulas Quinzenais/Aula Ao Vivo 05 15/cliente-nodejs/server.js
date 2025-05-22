const express = require('express');
const path = require('path');

const app = express();

// Serve os arquivos estáticos na pasta 'public'
app.use(express.static(path.join(__dirname, 'public')));

// Roda o servidor na porta 3000
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Site rodando em http://localhost:${PORT}`);
});
