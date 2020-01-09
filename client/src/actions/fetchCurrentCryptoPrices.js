// Returns a mapping of all cryptocurrencies to unique CoinMarketCap ids.
// Per our Best Practices we recommend utilizing CMC ID instead of 
// cryptocurrency symbols to securely identify cryptocurrencies with 
// our other endpoints and in your own application logic.
// Each cryptocurrency returned includes typical identifiers such as name,
// symbol, and token_address for flexible mapping to id.

import axios from 'axios';

export function fetchCurrentCryptoPrices(){
   
    // created proxy in package.json  
    return axios.get('/v1/cryptocurrency/listings/latest', {
        method: 'GET',
        mode: 'CORS',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'X-CMC_PRO_API_KEY': '7155cca9-767d-407f-a471-d6f276559849'
        },
        json: true,
        gzip: true
    });

}

// Additional curl request:
// curl -H "X-CMC_PRO_API_KEY: b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" -H "Accept: application/json" -d "symbol=BTC,USDT,BNB" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/map
// url: https://api.coinmarketcap.com/v1/ticker/