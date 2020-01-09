import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import moment from 'moment';
// styling
import {MDBBtn, MDBCol, MDBContainer, MDBRow} from 'mdbreact';
// components
import Pagination from '../../paginationComponent/pagination';
// actions
import ScrollButton from '../../scrollButtonComponent/scrollButton';
import {fetchTransactionsData} from '../../../actions/transactionPageActions';



class Transactions extends Component {


    constructor(props) {
        super(props);

        this.state = { // set initial state
            allTransactions: [],
            currentTransactions: [],
            currentPage: null,
            totalPages: null
        };

        this.getData = this.getData.bind(this);
    };


    // Method for fetching data

    getData() {
        const {allTransactions} = this.state;

        fetchTransactionsData()
            .then(json => {
                this.setState({
                    allTransactions: json.data
                })
            })
            .catch(err => {
                console.error('err', err)
            });

    };


    componentDidMount() { // lifecycle method
        this.getData();
    };

    onPageChanged = data => {
        const {allTransactions} = this.state;
        const {currentPage, pageLimit} = data;

        const offset = (currentPage - 1) * pageLimit;
        const currentTransactions = allTransactions.slice(offset, offset + pageLimit);

        this.setState({currentPage, currentTransactions});
    };

    // Render the page

    render() {
        const { allTransactions, currentTransactions, currentPage} = this.state;

        const totalTransactions = allTransactions.length;

        if (totalTransactions === 0) return null;

        const headerClass = [
            "text-dark py-2 pr-4 m-0",
            currentPage ? "border-gray border-right" : ""
        ]
            .join(" ")
            .trim();

        return (

            <MDBContainer>

                {currentTransactions.map((transaction, index) => {
                    return (

                        <MDBContainer className="page_content_container" key={index}>
                            <Link to={'/transaction/' + `${transaction.tx_index}`}>

                                <MDBRow className="upper_row">
                                    <MDBCol className="col-lg-6 hash">{transaction.currency} address</MDBCol>

                                    <MDBCol className="col-2 col-sm-3">
                                        <MDBBtn className="transactions">Transaction {transaction.tx_index}</MDBBtn>
                                    </MDBCol>

                                    <MDBCol className="col-2 col-sm-1">Block</MDBCol>

                                    <MDBCol className="col-lg">Received time:</MDBCol>
                                </MDBRow>

                                <MDBRow className="lower_row">
                                    <MDBCol className="col-lg-6 hash">{transaction.hash}</MDBCol>

                                    <MDBCol className="col-2 col-sm-3"></MDBCol>

                                    <MDBCol className="col-2 col-sm-1">{transaction.block_number}</MDBCol>

                                    <MDBCol className="col-lg">
                                        {moment(transaction.time).format('DD-MM-YYYY h:mm:ss')}
                                    </MDBCol>
                                </MDBRow>

                            </Link>
                        </MDBContainer>

                    );
                })}

                <ScrollButton scrollStepInPx="50" delayInMs="16"/>

                <Pagination
                    totalRecords={totalTransactions}
                    pageLimit={30}
                    pageNeighbours={1}
                    onPageChanged={this.onPageChanged}
                />


            </MDBContainer>
        );

    };

}


export default Transactions;

