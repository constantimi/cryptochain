import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import moment from 'moment';
// styling
import {MDBCol, MDBContainer, MDBRow} from 'mdbreact';
// components
import Pagination from '../../paginationComponent/pagination';
import ScrollButton from '../../scrollButtonComponent/scrollButton';
// actions
import {fetchBlocksData, fetchBlockDataById} from '../../../actions/blockPageActions';


class Blocks extends Component {


    constructor(props) {
        super(props);
        this.state = { // set initial state
            allBlocks: [],
            currentBlocks: [],
            currentPage: null,
            totalPages: null
        };

        this.getData = this.getData.bind(this);
    }


    // Method for fetching data

    getData() {
        const {allBlocks} = this.state;

        fetchBlocksData()
            .then(json => {
                
                this.setState({
                    allBlocks: json.data
                })
            })
            .catch(err => {
                throw new Error('block.js');
            });

    };


    componentDidMount() { // lifecycle method
        this.getData();
    };

    // Pagination

    onPageChanged = data => {
        const {allBlocks} = this.state;
        const {currentPage, totalPages, pageLimit} = data;

        const offset = (currentPage - 1) * pageLimit;
        const currentBlocks = allBlocks.slice(offset, offset + pageLimit);

        this.setState({currentPage, currentBlocks, totalPages});
    };

    // Render the page

    render() {
        const {
            allBlocks,
            currentBlocks,
            currentPage,
            totalPages
        } = this.state;

        const totalBlocks = allBlocks.length;

        if (totalBlocks === 0) return null;

        const headerClass = [
            "text-dark py-2 pr-4 m-0",
            currentPage ? "border-gray border-right" : ""
        ]
            .join(" ")
            .trim();

        return (

            <MDBContainer>

                {currentBlocks.map((block, index) => {
                    return (
                        <MDBContainer className="page_content_container" key={index}>
                            <Link to={'/block/' + `${block.block_index}`}>
                                <MDBRow className="upper_row">
                                    <MDBCol className="col-lg-6 hash">{block.currency} address</MDBCol>
                                    <MDBCol className="col-2 col-sm-1">Block</MDBCol>
                                    <MDBCol className="col-2 col-sm-2">TX count</MDBCol>
                                    <MDBCol className="col-lg">Recieved time:</MDBCol>
                                </MDBRow>
                                <MDBRow className="lower_row">
                                    <MDBCol className="col-lg-6 hash">{block.hash}</MDBCol>
                                    <MDBCol className="col-2 col-sm-1">{block.block_index}</MDBCol>
                                    <MDBCol className="col-2 col-sm-2">{block.n_tx}</MDBCol>
                                    <MDBCol className="col-lg">
                                        {moment(block.time).format('DD-MM-YYYY h:mm:ss')}
                                    </MDBCol>
                                </MDBRow>
                            </Link>
                        </MDBContainer>

                    );
                })}

                <ScrollButton scrollStepInPx="50" delayInMs="16"/>

                <Pagination
                    totalRecords={totalBlocks}
                    pageLimit={15}
                    pageNeighbours={1}
                    onPageChanged={this.onPageChanged}
                />

            </MDBContainer>


        );

    }
}


export default Blocks;

