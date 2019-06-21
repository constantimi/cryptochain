import React, {Component} from 'react';
import CopyText from 'react-copy-text';
import moment from 'moment';
// actions
import {fetchOutputDataById} from '../../../actions/outputPageActions';
// styling
import {MDBBtn, MDBCol, MDBContainer, MDBRow} from 'mdbreact';
import {Link} from 'react-router-dom';


class OutputDetails extends Component {


    constructor(props) {
        super(props);

        this.state = { // set initial state
            output: [],
            textToCopy: '' // onButtonClick method
        };

        this.getData = this.getData.bind(this);
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
        const {output} = this.state;
        const {id} = this.props.match.params;

        fetchOutputDataById(id)
            .then(json => {
                console.log('data', json);
                this.setState({
                    output: json.data
                })
            })
            .catch(err => {
                console.error('err', err)
            });

    };


    componentDidMount() { // lifecycle method
        this.getData();
    };


    render() {

        const {output} = this.state;
        const {id} = this.props.match.params;


        return (
            <MDBContainer>

                <MDBContainer className="page_label_container">
                    <MDBRow>
                        <Link to={`/outputs/`}>
                            <MDBCol className="col_back ">
                                Back
                            </MDBCol>
                        </Link>
                        <MDBCol className="col_title">
                            Output {output.id_output}
                        </MDBCol>
                    </MDBRow>
                </MDBContainer>

            <MDBContainer className="page_content_container">
                 <Link to={'/outputs/'}>
                     <MDBRow className="upper_row">
                         <MDBCol className="col-lg-6 hash">transaction address</MDBCol>
                         <MDBCol className="col-2 col-sm-2">transaction</MDBCol>
                         <MDBCol className="col-2 col-sm-4">value</MDBCol>
                     </MDBRow>

                     <MDBRow className="lower_row">
                         <MDBCol className=" st col-lg-6 hash">{output.tx_hash}</MDBCol>
                         <MDBCol className="col-2 col-sm-2">{output.transaction}</MDBCol>
                         <MDBCol className="col-2 col-sm-4">{output.value} satoshis</MDBCol>
                     </MDBRow>
                 </Link>
            </MDBContainer>

                 <MDBContainer className="page_content_container">
                        <MDBRow className="upper_row unhash">
                            <MDBCol>Copy info: </MDBCol>

                            <MDBBtn className="unhash" onClick={() => this.onButtonClick(output.tx_hash)}>
                                <i className="fas fa-address-card"></i> transaction address
                            </MDBBtn>

                            <CopyText text={this.state.textToCopy} onCopied={this.onCopied}/>
                        </MDBRow>
                 </MDBContainer>
            </MDBContainer>
        );
    }
}

export default OutputDetails