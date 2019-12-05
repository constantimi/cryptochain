import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
// includes
import './assets/css/default.min.css';

import React from 'react';
import ReactDOM from 'react-dom';
import Main from './components/mainComponent/main';
import Footer from './components/footerComponent/footer';

ReactDOM.render(<Main />, document.getElementById('main'));
ReactDOM.render(<Footer />, document.getElementById('footer'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

