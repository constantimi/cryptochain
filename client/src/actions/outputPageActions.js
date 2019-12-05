//   Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell a browser to let a web
//   application running at one origin (domain) have permission to access selected resources from a server at a different
//   origin. A web application executes a cross-origin HTTP request when it requests a resource that has a different
//   origin (domain, protocol, and port) than its own origin.

import axios from 'axios';

export function fetchOutputsData() {
    return axios.get('https://cryptochain-server.herokuapp.com/outputs/', {
        method: 'GET',
        mode: 'CORS'
    });
}

export function fetchOutputDataById(id) {
    return axios.get('https://cryptochain-server.herokuapp.com/output/' + `${id}`, {
        method: 'GET',
        mode: 'CORS'
    });
}