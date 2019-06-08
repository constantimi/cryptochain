//   Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell a browser to let a web
//   application running at one origin (domain) have permission to access selected resources from a server at a different
//   origin. A web application executes a cross-origin HTTP request when it requests a resource that has a different
//   origin (domain, protocol, and port) than its own origin.

import axios from 'axios';

export function fetchInputsData() {
    return axios.get('http://localhost:8000/inputs/', {
        method: 'GET',
        mode: 'CORS'
    });
}

export function fetchInputDataById(id) {
    return axios.get('http://localhost:8000/input/' + `${id}`, {
        method: 'GET',
        mode: 'CORS'
    });
}