// using CommonJS modules
import React, {Component} from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {MDBContainer} from 'mdbreact';

// navigation
import Navigation from '../navigationComponent/navigation';

// transactions
import Transactions from '../contentComponent/transactions/transactions';
import Transaction from '../contentComponent/transactions/transactionDetails';
// blocks
import Blocks from '../contentComponent/blocks/blocks';
import Block from '../contentComponent/blocks/blockDetails';
// inputs
import Inputs from '../contentComponent/inputs/inputs';
import Input from '../contentComponent/inputs/inputDetails';
// outputs
import Outputs from '../contentComponent/outputs/outputs';
import Output from '../contentComponent/outputs/outputDetails';
// chart page
import LineGraph from '../contentComponent/charts/lineGraph';

// error boundery
import ErrorBoundary from '../errorBoundary/errorBoundary';
// network detector
import NetworkDetector from '../errorBoundary/networkDetector';



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
                <Router>
                    <div className="content">
                        <ErrorBoundary>
                        {/* Navigation */}
                        <Navigation />

                            {/* Content */}
                            <MDBContainer className="content-inside">

                                {/* Homepage links to Blocks*/}
                                <Route exact path={'/'} component={LineGraph}/>
                                
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

                                <Route exact path={'/prices'} component={LineGraph}/>

                            </MDBContainer>
                        </ErrorBoundary>
                    </div>

                    <div className="push"></div>
                </Router>
        );
    }
}

export default Main;