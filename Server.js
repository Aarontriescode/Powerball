const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;

// Replace 'https://api.powerballdata.com/results' with the actual Powerball API endpoint
const POWERBALL_API_URL = 'https://api.powerballdata.com/results';

app.get('/fetch-powerball-results', async (req, res) => {
    try {
        const response = await axios.get(POWERBALL_API_URL);
        res.json({
            status: 'success',
            data: response.data
        });
    } catch (error) {
        console.error('Failed to fetch Powerball results:', error);
        res.status(500).json({
            status: 'error',
            message: 'Failed to fetch Powerball results'
        });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
