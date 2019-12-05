//   Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell a browser to let a web
//   application running at one origin (domain) have permission to access selected resources from a server at a different
//   origin. A web application executes a cross-origin HTTP request when it requests a resource that has a different
//   origin (domain, protocol, and port) than its own origin.

import axios from 'axios';

export function fetchTransactionsData() {
    return axios.get('https://cryptochain-server.herokuapp.com/transactions/', {
        method: 'GET', // "Accept": "application/json"
        mode: 'CORS'
    });
}

export function fetchTransactionDataById(id) {
    return axios.get(`https://cryptochain-server.herokuapp.com/transaction/${id}`, {
        method: 'GET',
        mode: 'CORS'
    });
}
