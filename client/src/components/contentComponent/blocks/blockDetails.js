import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import CopyText from 'react-copy-text';
import moment from 'moment';
// styling
import {MDBBtn, MDBCol, MDBContainer, MDBRow} from 'mdbreact';
// components
import Pagination from '../../paginationComponent/pagination';
import ScrollButton from '../../scrollButtonComponent/scrollButton';
// actions
import {fetchBlockDataById} from '../../../actions/blockPageActions';
import {fetchTransactionsData} from "../../../actions/transactionPageActions";

class BlockDetails extends Component {


    constructor(props) {
        super(props);

        this.state = { // set initial state
            block: [],
            allTransactionsInBlock: [],
            currentTransactionsInBlock: [],
            currentPage: null,
            totalPages: null,
            textToCopy: ''
        };

        this.getData = this.getData.bind(this);
    };


    // Method for fetching data

    getData() {
        const {block, allTransactionsInBlock} = this.state;
        const {id} = this.props.match.params;

        fetchBlockDataById(id)
            .then(json => {
                
                this.setState({
                    block: json.data
                });
            })
            .catch(err => {
                throw new Error('fetchBlockDataById');
            });

        fetchTransactionsData()
            .then(json => {
                console.log('data', json);
                const transactions = json.data;

                var filtered = transactions.filter(function (el) {
                    return el.block_number === parseInt(id);
                });

                this.setState({
                    allTransactionsInBlock: filtered
                });
            })
            .catch(err => {
                throw new Error('fetchTransactionsData');
            });
    };


    componentDidMount() { // lifecycle method
        this.getData();
    };

    onPageChanged = data => {
        const {allTransactionsInBlock} = this.state;
        const {currentPage, totalPages, pageLimit} = data;

        const offset = (currentPage - 1) * pageLimit;
        const currentTransactionsInBlock = allTransactionsInBlock.slice(offset, offset + pageLimit);

        this.setState({currentPage, currentTransactionsInBlock, totalPages});
    };

    // Button OnClick

    onButtonClick = (value) => {
        if (value !== undefined && value !== null) {
            this.setState({
                textToCopy: `${value}`
            });
        }
    };

    // Copy on clipboard

    onCopied = (text) => {
        console.log(`${text} was copied to the clipboard`);
    };

    render() {
        const {block, allTransactionsInBlock, currentTransactionsInBlock, currentPage} = this.state;
        const {id} = this.props.match.params;

        const totalTransactionsInBlock = allTransactionsInBlock.length;

        if (totalTransactionsInBlock === 0) return null;

        const headerClass = [
            "text-dark py-2 pr-4 m-0",
            currentPage ? "border-gray border-right" : ""
        ]
            .join(" ")
            .trim();

        return (

            <MDBContainer>

                <MDBContainer className="page_label_container">
                    <MDBRow>
                        <Link to={`/blocks/`}>
                            <MDBCol className="col_back ">
                                Back
                            </MDBCol>
                        </Link>
                        <MDBCol className="col_title">
                            {block.title}
                        </MDBCol>
                    </MDBRow>
                </MDBContainer>


                <MDBContainer className="page_content_container">

                    <MDBRow className="upper_row">
                        <MDBCol className="col-lg-6 hash">{block.currency} address</MDBCol>
                        <MDBCol className="col-2 col-sm-1">Block</MDBCol>
                        <MDBCol className="col-2 col-sm-2">TX count</MDBCol>
                        <MDBCol className="col-lg-3">Received time:</MDBCol>

                    </MDBRow>

                    <MDBRow className="lower_row">
                        <MDBCol className="col-lg-6 hash">{block.hash}</MDBCol>
                        <MDBCol className="col-2 col-sm-1">{block.block_index}</MDBCol>
                        <MDBCol className="col-2 col-sm-2">{block.n_tx}</MDBCol>
                        <MDBCol className="col-lg-3">
                            {moment(block.time).format('MM-DD-YYYY h:mm:ss')}
                        </MDBCol>
                    </MDBRow>


                    <MDBRow className="upper_row hash">
                        <MDBCol className="col-lg-6 hash">merkle root</MDBCol>
                        <MDBCol className="col-lg-6 hash">previous block</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row_info hash">
                        <MDBCol className="col-lg-6 hash">{block.merkle_root}</MDBCol>
                        <MDBCol className="col-lg-6 hash">{block.previous_block}</MDBCol>
                    </MDBRow>


                    <MDBRow className="upper_row hash">
                        <MDBCol className="col-2 col-sm-3 hash">nonce</MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">size</MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">{block.difficulty ? "difficulty" : ""}</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row_info hash">
                        <MDBCol className="col-2 col-sm-3 hash">
                            {block.nonce ? block.nonce : (0)}
                        </MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">{block.size}</MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">
                            {block.difficulty ? block.difficulty : ""}
                        </MDBCol>
                    </MDBRow>
                </MDBContainer>


                <MDBContainer className="page_content_container">

                    <MDBRow className="lower_row_info unhash">

                        <MDBCol>Copy info:</MDBCol>

                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(block.hash)}>
                            hash
                        </MDBBtn>

                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(block.size)}>
                            size
                        </MDBBtn>

                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(block.nonce ? block.nonce : (0))}>
                            nonce
                        </MDBBtn>

                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(block.previous_block)}>
                            previous block
                        </MDBBtn>

                        <CopyText text={this.state.textToCopy} onCopied={this.onCopied}/>

                    </MDBRow>

                </MDBContainer>

                    <MDBContainer className="page_label_container">
                        <MDBRow>
                            <MDBCol className="label_title">
                                Transactions in the Block
                            </MDBCol>
                        </MDBRow>
                    </MDBContainer>

                <MDBContainer>

                    {currentTransactionsInBlock.map((transaction, index) => {
                        return (

                            <MDBContainer className="page_content_container" key={index}>
                                <Link to={'/transaction/' + `${transaction.tx_index}`}>
                                    <MDBRow className="upper_row">

                                        <MDBCol className="col-2 col-sm-4">
                                            <MDBBtn className="transactions">Transaction {transaction.tx_index}</MDBBtn>
                                        </MDBCol>

                                        <MDBCol className="col-lg-6 hash">address</MDBCol>

                                        <MDBCol className="col-sm-2">fee</MDBCol>

                                    </MDBRow>

                                    <MDBRow className="lower_row_info">

                                        <MDBCol className="col-2 col-sm-4"></MDBCol>

                                        <MDBCol className="col-lg-6 hash">0x{transaction.hash}</MDBCol>

                                        <MDBCol
                                            className="col-2 col-sm-2">{transaction.currency === "ETH" ? (transaction.fee * Math.pow(10, -18)).toFixed(6) : transaction.fee} {transaction.currency}</MDBCol>

                                    </MDBRow>

                                </Link>
                            </MDBContainer>

                        );
                    })}

                    <ScrollButton scrollStepInPx="50" delayInMs="16"/>

                    <Pagination
                        totalRecords={totalTransactionsInBlock}
                        pageLimit={50}
                        pageNeighbours={1}
                        onPageChanged={this.onPageChanged}
                    />

                </MDBContainer>

            </MDBContainer>
        );
    };
}

export default BlockDetails;