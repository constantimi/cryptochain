import React, {Component} from "react";
import {BrowserRouter as Router, Route} from 'react-router-dom';
import { MDBCollapse, MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavbarToggler, MDBNavItem, MDBNavLink } from "mdbreact";
import HeaderComponents from './header_components';

class Navigation extends Component {

    constructor() {
        super();

        this.state = {
            isOpen: false
        };

    }


    toggleCollapse = () => {
        this.setState({isOpen: !this.state.isOpen});
    };


    render() {

        return (
            <Router>
                <MDBNavbar dark expand="md">

                    <MDBNavbarBrand>
                        Cryptochain
                    </MDBNavbarBrand>

                    <MDBNavbarToggler onClick={this.toggleCollapse}/>

                    <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
                        <MDBNavbarNav left>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/prices">Prices</MDBNavLink> */}
                                <a href="/prices" className="nav-link">Pirces</a>
                            </MDBNavItem>


                            <MDBNavItem>
                                {/* <MDBNavLink to="/blocks">Blocks</MDBNavLink> */}
                                <a href="/blocks" className="nav-link">Blocks</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/transactions">Transactions</MDBNavLink> */}
                                <a href="/transactions" className="nav-link">Transactions</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/inputs">Inputs</MDBNavLink> */}
                                <a href="/inputs" className="nav-link">Inputs</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/outputs">Ouputs</MDBNavLink> */}
                                <a href="/outputs" className="nav-link">Outputs</a>
                            </MDBNavItem>

                        </MDBNavbarNav>

                    </MDBCollapse>

                </MDBNavbar>

                <HeaderComponents/>
            </Router>
        );
    }
}

export default Navigation;
