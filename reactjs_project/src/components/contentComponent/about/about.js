import React, {Component} from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBCard, MDBCardBody, MDBInput, MDBBtn, MDBIcon, MDBModalFooter } from 'mdbreact';


class About extends Component{
    render () {
        return(
            <MDBContainer className="about">
              <MDBRow>
                <MDBCol className="col-lg">
                  <MDBCard>
                    <MDBCardBody className="mx-4">
                      <div className="text-center">
                        <h3 className="dark-grey-text mb-5">
                          <strong>How does a blockchain technology work?</strong>
                        </h3>
                        </div>
                        <div className="text">
                        <p>A central aspect of blockchain technology is the distributed ledger, which contains a record of all previous transactions. It is called a distributed ledger because it is not stored in a central location, rather it is stored across a network of computers across the world. Key to the operation of a distributed ledger is ensuring the entire network collectively agrees with the contents of the ledger; this is the job of the consensus mechanism.</p>
                        <p>&nbsp;</p>
                        <p>Behind many cryptoassets, there is a consensus mechanism. The purpose of a consensus mechanism is to verify that information being added to the ledger is valid i.e. the network is in consensus. This ensures that the next block being added represents the most current transactions on the network, preventing double spending and other invalid data from being appended to the blockchain. In addition, the consensus mechanism keeps the network from being derailed through constant forking.</p>
                        <p>&nbsp;</p>
                        <p>There have been a number of different consensus mechanisms devised, each with their own pros and cons. They all serve the same core purpose as described above, but differ in methodology. The primary difference between varying consensus mechanisms is the way in which they delegate and reward the verification of transactions.</p>
                      </div>
                    </MDBCardBody>
                  </MDBCard>
                </MDBCol>
              </MDBRow>
            </MDBContainer>
        );
    };
}
export default About;