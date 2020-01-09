import React, {Component} from "react";
// styling
import {MDBCol, MDBContainer, MDBFormInline, MDBNavbarNav, MDBNavItem, MDBRow} from 'mdbreact';
// actions
import {fetchOutputsData} from '../../actions/outputPageActions';
import {fetchInputsData} from '../../actions/inputPageActions';
import {fetchBlocksData} from '../../actions/blockPageActions';
import {fetchTransactionsData} from '../../actions/transactionPageActions';

class HeaderComponents extends Component {

    constructor(props){
        super(props);

        this.state = {
           blocks_count: null,
           txs_count: null,
           inputs_count: null,
           outputs_count: null,
        };

        this.getData = this.getData.bind(this);
    };

    // Method for fetching data

    getData() {
        const {blocks_count, txs_count, inputs_count, outputs_count} = this.state;

        fetchTransactionsData()
                    .then(json => {
                        
                        const transactions = json.data;

                        this.setState({
                            txs_count: transactions.length
                        });
                    })
                    .catch(err => {
                        console.error('err', err);
                    });

        fetchBlocksData()
                            .then(json => {
                                
                                const blocks = json.data;

                                this.setState({
                                    blocks_count: blocks.length
                                });
                            })
                            .catch(err => {
                                console.error('err', err);
                            });

        fetchInputsData()
                            .then(json => {
                                
                                const inputs = json.data;

                                this.setState({
                                    inputs_count: inputs.length
                                });
                            })
                            .catch(err => {
                                console.error('err', err);
                            });

        fetchOutputsData()
                             .then(json => {
                                
                                 const outputs = json.data;

                                 this.setState({
                                     outputs_count: outputs.length
                                 });
                             })
                             .catch(err => {
                                 console.error('err', err);
                             });
    };

    componentDidMount() { // lifecycle method
        this.getData();
    };

    render() {
        const {blocks_count, txs_count, inputs_count, outputs_count} = this.state;

        return (
            <MDBContainer className="header_components_container">
                <MDBRow className="header_components_upper_row">
                    <MDBCol className="header_components_col">
                        <MDBRow className="header_components_upper_row">current blocks</MDBRow>
                        <MDBRow className="header_components_lower_row">{blocks_count}</MDBRow>
                    </MDBCol>
                    <MDBCol className="header_components_col">
                        <MDBRow className="header_components_upper_row">transactions</MDBRow>
                        <MDBRow className="header_components_lower_row">{txs_count}</MDBRow>
                    </MDBCol>
                    <MDBCol className="header_components_col">
                        <MDBRow className="header_components_upper_row">inputs</MDBRow>
                        <MDBRow className="header_components_lower_row">{inputs_count}</MDBRow>
                    </MDBCol>
                    <MDBCol className="header_components_col">
                        <MDBRow className="header_components_upper_row">outputs</MDBRow>
                        <MDBRow className="header_components_lower_row">{outputs_count}</MDBRow>
                    </MDBCol>
                </MDBRow>
            </MDBContainer>

        );
    };
}

export default HeaderComponents;
