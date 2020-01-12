import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import moment from 'moment';
// styling
import {MDBCol, MDBContainer, MDBRow} from 'mdbreact';
// components
import Pagination from '../../paginationComponent/pagination';
import ScrollButton from '../../scrollButtonComponent/scrollButton';
// actions
import {fetchInputsData} from '../../../actions/inputPageActions';

class Inputs extends Component {


    constructor(props) {
        super(props);
        this.state = { // set initial state
            allInputs: [],
            currentInputs: [],
            currentPage: null,
            totalPages: null
        };

        this.getData = this.getData.bind(this);
    }


    // Method for fetching data

    getData() {
        const {allInputs} = this.state;

        fetchInputsData()
            .then(json => {
               
                this.setState({
                    allInputs: json.data
                })
            })
            .catch(err => {
                throw new Error('fetchInputData', err.message);
            });
    };


    componentDidMount() { // lifecycle method
        this.getData();
    };

    // Pagination

    onPageChanged = data => {
        const {allInputs} = this.state;
        const {currentPage, totalPages, pageLimit} = data;

        const offset = (currentPage - 1) * pageLimit;
        const currentInputs = allInputs.slice(offset, offset + pageLimit);

        this.setState({currentPage, currentInputs, totalPages});
    };

    // Render the page

    render() {
        const {
            allInputs,
            currentInputs,
            currentPage,
            totalPages
        } = this.state;

        const totalInputs = allInputs.length;

        if (totalInputs === 0) return null;

        const headerClass = [
            "text-dark py-2 pr-4 m-0",
            currentPage ? "border-gray border-right" : ""
        ]
            .join(" ")
            .trim();

        return (

            <MDBContainer>

                {currentInputs.map((input, index) => {
                    return (
                        <MDBContainer className="page_content_container" key={index}>
                            <Link to={'/input/' + `${input.id_input}`}>
                                <MDBRow className="upper_row">
                                    <MDBCol className="col-lg-10 hash">transaction address</MDBCol>
                                    <MDBCol className="col-2 col-sm-1">transaction</MDBCol>
                                </MDBRow>
                                <MDBRow className="lower_row">
                                    <MDBCol className=" st col-lg-10 hash">{input.tx_hash}</MDBCol>
                                    <MDBCol className="col-2 col-sm-1">{input.transaction}</MDBCol>
                                </MDBRow>
                            </Link>
                        </MDBContainer>

                    );
                })}

                <ScrollButton scrollStepInPx="50" delayInMs="16"/>

                <Pagination
                    totalRecords={totalInputs}
                    pageLimit={15}
                    pageNeighbours={1}
                    onPageChanged={this.onPageChanged}
                />

            </MDBContainer>


        );

    }
}


export default Inputs;

