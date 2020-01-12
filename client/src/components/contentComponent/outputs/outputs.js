import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import moment from 'moment';
// styling
import {MDBCol, MDBContainer, MDBRow} from 'mdbreact';
// components
import Pagination from '../../paginationComponent/pagination';
import ScrollButton from '../../scrollButtonComponent/scrollButton';
// actions
import {fetchOutputsData} from '../../../actions/outputPageActions';

class Outputs extends Component {


    constructor(props) {
        super(props);
        this.state = { // set initial state
            allOutputs: [],
            currentOutputs: [],
            currentPage: null,
            totalPages: null
        };

        this.getData = this.getData.bind(this);
    }


    // Method for fetching data

    getData() {
        const {allOutputs} = this.state;

        fetchOutputsData()
            .then(json => {
             
                this.setState({
                    allOutputs: json.data
                })
            })
            .catch(err => {
                throw new Error('fetchOutputData', err.message);
            });
    };


    componentDidMount() { // lifecycle method
        this.getData();
    };

    // Pagination

    onPageChanged = data => {
        const {allOutputs} = this.state;
        const {currentPage, totalPages, pageLimit} = data;

        const offset = (currentPage - 1) * pageLimit;
        const currentOutputs = allOutputs.slice(offset, offset + pageLimit);

        this.setState({currentPage, currentOutputs, totalPages});
    };

    // Render the page

    render() {
        const {
            allOutputs,
            currentOutputs,
            currentPage,
            totalPages
        } = this.state;

        const totalOutputs = allOutputs.length;

        if (totalOutputs === 0) return null;

        const headerClass = [
            "text-dark py-2 pr-4 m-0",
            currentPage ? "border-gray border-right" : ""
        ]
            .join(" ")
            .trim();

        return (

            <MDBContainer>

                {currentOutputs.map((output, index) => {
                    return (
                        <MDBContainer className="page_content_container" key={index}>
                            <Link to={'/output/' + `${output.id_output}`}>
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

                    );
                })}

                <ScrollButton scrollStepInPx="50" delayInMs="16"/>

                <Pagination
                    totalRecords={totalOutputs}
                    pageLimit={15}
                    pageNeighbours={1}
                    onPageChanged={this.onPageChanged}
                />

            </MDBContainer>


        );

    }
}


export default Outputs;

