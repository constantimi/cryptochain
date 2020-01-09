// @ts-nocheck
//   Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell a browser to let a web
//   application running at one origin (domain) have permission to access selected resources from a server at a different
//   origin. A web application executes a cross-origin HTTP request when it requests a resource that has a different
//   origin (domain, protocol, and port) than its own origin.


import axios from 'axios';


export function fetchBitcoin(){
    var moment = require('moment');
    var displayMonthsBack = 12;

    return axios.get(`https://api.coindesk.com/v1/bpi/historical/close.json?start=${moment(new Date()).subtract(displayMonthsBack, 'month').format('YYYY-MM-DD')}&end=${moment(new Date()).format('YYYY-MM-DD')}`, {
        method: 'GET',
        mode: 'CORS',
        json: true
    });
}

// Additional information:
// https://kapeli.com/cheat_sheets/Axios.docset/Contents/Resources/Documents/index