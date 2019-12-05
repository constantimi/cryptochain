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
                        Blockchain
                    </MDBNavbarBrand>

                    <MDBNavbarToggler onClick={this.toggleCollapse}/>

                    <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
                        <MDBNavbarNav left>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/blocks">Blocks</MDBNavLink> */}
                                <a href="/blocks" class="nav-link">Blocks</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/transactions">Transactions</MDBNavLink> */}
                                <a href="/transactions" class="nav-link">Transactions</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/inputs">Inputs</MDBNavLink> */}
                                <a href="/inputs" class="nav-link">Inputs</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/outputs">Ouputs</MDBNavLink> */}
                                <a href="/outputs" class="nav-link">Outputs</a>
                            </MDBNavItem>

                            <MDBNavItem>
                                {/* <MDBNavLink to="/about">About</MDBNavLink> */}
                                <a href="/about" class="nav-link">About</a>
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
