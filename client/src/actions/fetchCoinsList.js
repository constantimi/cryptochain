
import axios from 'axios';


export function fetchCoinsList(cryptocoin, date){

    return axios.get(`https://api.coingecko.com/api/v3/coins/list`, {
        method: 'GET',
        mode: 'CORS',
        json: true
    });
}

// Additional information:
// https://www.coingecko.com/en/api#explore-api
//
// Example:
//
// [
//       {
//         "id": "bitclassic",
//         "symbol": "b2c",
//         "name": "BitClassic"
//       }
// ]