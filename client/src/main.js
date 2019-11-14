// using CommonJS modules
import React, {Component} from 'react'
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {MDBContainer} from 'mdbreact';
// components
import Header from './components/headerComponent/header';
import HeaderComponents from './components/headerComponent/header_components';
// transactions
import Transactions from './components/contentComponent/transactions/transactions';
import Transaction from './components/contentComponent/transactions/transactionDetails';
// blocks
import Blocks from './components/contentComponent/blocks/blocks';
import Block from './components/contentComponent/blocks/blockDetails';
// inputs
import Inputs from './components/contentComponent/inputs/inputs';
import Input from './components/contentComponent/inputs/inputDetails';
// outputs
import Outputs from './components/contentComponent/outputs/outputs';
import Output from './components/contentComponent/outputs/outputDetails';
// about page
import About from './components/contentComponent/about/about';
// includes
import './assets/css/default.min.css';


class Main extends Component {

    // Sort by transaction block_number

    sortByBlockNumber() {
        const {transactions} = this.state;
        let newTransactions = transactions;

        if (this.state.isOldestFirst) {
            newTransactions = transactions.sort((a, b) => a.block_number > b.block_number);
        } else {
            newTransactions = transactions.sort((a, b) => a.block_number < b.block_number);
        }

        this.setState({
            isOldestFirst: !this.state.isOldestFirst,
            transactions: newTransactions
        });
    }


    // Reverse transaction order

    toggleListReverse(event) {
        const {transactions} = this.state;
        let newTransactions = transactions.reverse();
        this.setState({
            transactions: newTransactions
        })
    }


    render() {
        return (
            <div className="app">
                <Router>
                    <div className="content">

                        {/* Navbar */}
                        <Header/>
                        <HeaderComponents/>

                        {/* Content */}
                        <MDBContainer className="content-inside">

                            {/* Homepage links to Blocks*/}
                            <Route exact path={'/'} component={Blocks}/>

                            {/* About page*/}
                            <Route exact path={'/about'} component={About}/>

                            {/* List of Blocks & Block/id Details */}
                            <Route exact path={'/blocks'} component={Blocks}/>
                            <Route exact path={'/block/:id'} component={Block}/>

                            {/* List of Transactions & Transaction/id Details */}
                            <Route exact path={'/transactions'} component={Transactions}/>
                            <Route exact path={'/transaction/:id'} component={Transaction}/>

                            {/* List of Inputs & Input/id Details */}
                            <Route exact path='/inputs' component={Inputs}/>
                            <Route exact path='/input/:id' component={Input}/>

                            {/* List of Transactions & Transaction/id Details */}
                            <Route exact path={'/outputs'} component={Outputs}/>
                            <Route exact path={'/output/:id'} component={Output}/>

                        </MDBContainer>

                    </div>
                </Router>
            </div>
        );
    }
}

export default Main;

