const express = require('express');
const { PythonShell } = require('python-shell');

const app = express();
const port = 3000;

app.get('/generate-powerball', (req, res) => {
    PythonShell.run('powerball.py', null, (err, results) => {
        if (err) {
            res.status(500).send('Error running Python script');
            console.error(err);
        } else {
            res.send({
                message: "Generated Powerball Numbers",
                powerballNumbers: results
            });
        }
    });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
