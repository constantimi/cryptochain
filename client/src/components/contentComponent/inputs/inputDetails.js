import React, {Component} from 'react';
import CopyText from 'react-copy-text';
import moment from 'moment';
// actions
import {fetchInputDataById} from '../../../actions/inputPageActions';
// styling
import {MDBBtn, MDBCol, MDBContainer, MDBRow} from 'mdbreact';
import {Link} from 'react-router-dom';


class InputDetails extends Component {


    constructor(props) {
        super(props);

        this.state = { // set initial state
            input: [],
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
        const {input} = this.state;
        const {id} = this.props.match.params;

        fetchInputDataById(id)
            .then(json => {
                
                this.setState({
                    input: json.data
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

        const {input} = this.state;
        const {id} = this.props.match.params;


        return (
            <MDBContainer>

                <MDBContainer className="page_label_container">
                    <MDBRow>
                        <Link to={'/inputs/'}>
                            <MDBCol className="col_back ">
                                Back
                            </MDBCol>
                        </Link>
                        <MDBCol className="col_title">
                            Input {input.id_input}
                        </MDBCol>
                    </MDBRow>
                </MDBContainer>

                <MDBContainer className="page_content_container">

                        <MDBRow className="upper_row">
                            <MDBCol className="col-lg-7 hash">from address</MDBCol>
                            <MDBCol className="col-2 col-sm-3">transaction inx</MDBCol>
                        </MDBRow>

                        <MDBRow className="lower_row">
                            <MDBCol className=" st col-lg-7 hash">{input.address}</MDBCol>
                            <MDBCol className="col-2 col-sm-3">{input.transaction}</MDBCol>
                        </MDBRow>
                </MDBContainer>

                 <MDBContainer className="page_content_container">
                        <MDBRow className="upper_row unhash">
                            <MDBCol>Copy info: </MDBCol>

                            <MDBBtn className="unhash" onClick={() => this.onButtonClick(input.address)}>
                                <i className="fas fa-address-card"></i> from address
                            </MDBBtn>

                            <CopyText text={this.state.textToCopy} onCopied={this.onCopied}/>
                        </MDBRow>
                 </MDBContainer>
            </MDBContainer>
        );
    }
}

export default InputDetails