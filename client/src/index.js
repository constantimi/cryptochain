import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
// includes
import './assets/css/default.min.css';

import React from 'react';
import ReactDOM from 'react-dom';
import Main from './components/mainComponent/main';

ReactDOM.render(<Main />, document.getElementById('main'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

