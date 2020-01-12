import React, {Component} from 'react';
import CopyText from 'react-copy-text';
import moment from 'moment';
// actions
import {fetchTransactionDataById} from '../../../actions/transactionPageActions';
// styling
import {MDBBtn, MDBCol, MDBContainer, MDBRow} from 'mdbreact';
import {Link} from 'react-router-dom';


class TransactionDetails extends Component {


    constructor(props) {
        super(props);

        this.state = { // set initial state
            transaction: [],
            textToCopy: '' // onButtonClick method
        };

        this.getData = this.getData.bind(this);
    };

    // Check if the value is null

    isNull = (value) => {

        if (value === null) {
            return true;
        }

        return false;
    };

    // Button OnClick

    onButtonClick = (value) => {

        this.setState({
            textToCopy: `${value}`
        });
    };

    // Copy on clipboard

    onCopied = (text) => {
        console.log(`${text} was copied to the clipboard`);
    };

    // Method for fetching data

    getData() {
        const {transaction} = this.state;
        const {id} = this.props.match.params;

        fetchTransactionDataById(id)
            .then(json => {
            
                this.setState({
                    transaction: json.data
                })
            })
            .catch(err => {
                throw new Error('fetchTransactionDataById', err.message);
            });

    };


    componentDidMount() { // lifecycle method
        this.getData();
    };


    render() {

        const {transaction} = this.state;
        const {id} = this.props.match.params;


        return (
            <MDBContainer>
                <MDBContainer className="page_label_container">
                    <MDBRow>
                        <Link to={`/transactions/`}>
                            <MDBCol className="col_back ">
                                Back
                            </MDBCol>
                        </Link>
                        <MDBCol className="col_title">
                            {transaction.title}
                        </MDBCol>
                    </MDBRow>
                </MDBContainer>

                <MDBContainer className="page_content_container">

                    <MDBRow className="upper_row">
                        <MDBCol className="col-lg-7">address</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">fee</MDBCol>
                        <MDBCol className="col-lg-3 received_time">Received time:</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row">
                        <MDBCol className="col-lg-7">{transaction.hash}</MDBCol>
                          <MDBCol className="col-2 col-sm-2 hash">{transaction.currency === "ETH" ? (transaction.fee * Math.pow(10, -18)).toFixed(6) : transaction.fee} {transaction.currency}</MDBCol>
                        <MDBCol className="col-lg-3 received_time">
                            {moment(transaction.time).format('MM-DD-YYYY h:mm:ss')}
                        </MDBCol>
                    </MDBRow>

                    <MDBRow className="upper_row hash">
                        <MDBCol className="col-lg-7 hash">block {transaction.block_number} hash</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">gas</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">gas price</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row_info hash">
                        <MDBCol className="col-lg-7 hash">{transaction.block_hash}</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">{transaction.gas}</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">{transaction.gas_price}</MDBCol>
                    </MDBRow>

                    <MDBRow className="upper_row hash">
                        <MDBCol className="col-lg-7 hash">from address</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">value</MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">nonce</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row_info hash">
                        <MDBCol className="col-lg-7 hash">{(() => this.isNull(transaction.belonging_to)) ? "0x" : transaction.belonging_to}</MDBCol>
                        <MDBCol className="col-2 col-sm-2 hash">
                            {(() => this.isNull(transaction.value)) ? (0) : (transaction.value)}
                        </MDBCol>
                        <MDBCol className="col-2 col-sm-3 hash">
                            {(() => this.isNull(transaction.nonce)) ? (0) : (transaction.nonce)}
                        </MDBCol>
                    </MDBRow>

                    <MDBRow className="upper_row hash">
                        <MDBCol className="col-lg-7 hash">to contract address</MDBCol>
                    </MDBRow>

                    <MDBRow className="lower_row_info hash">
                        <MDBCol className="col-lg-7 hash">{(() => this.isNull(transaction.relayed_by)) ? "0x" : transaction.relayed_by}</MDBCol>
                    </MDBRow>

                </MDBContainer>

                <MDBContainer className="page_content_container">
                    <MDBRow className="upper_row unhash">
                        <MDBCol>Copy info: </MDBCol>

                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(transaction.belonging_to)}>
                            <i className="fas fa-address-card"></i> from address
                        </MDBBtn>


                        <MDBBtn className="unhash" onClick={() => this.onButtonClick(transaction.relayed_by)}>
                            <i className="fas fa-address-card"></i> to contract address
                        </MDBBtn>

                        <MDBBtn className="unhash"
                                onClick={() => this.onButtonClick((() => this.isNull(transaction.gas)) ? (0) : transaction.gas)}>
                            gas
                        </MDBBtn>

                        <CopyText text={this.state.textToCopy} onCopied={this.onCopied}/>

                    </MDBRow>

                </MDBContainer>

            </MDBContainer>
        );
    }
}

export default TransactionDetails