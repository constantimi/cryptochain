import React, {Component} from "react";
import {
    MDBCollapse,
    MDBDropdown,
    MDBDropdownItem,
    MDBDropdownMenu,
    MDBDropdownToggle,
    MDBFormInline,
    MDBNavbar,
    MDBNavbarBrand,
    MDBNavbarNav,
    MDBNavbarToggler,
    MDBNavItem,
    MDBNavLink
} from "mdbreact";

class Header extends Component {

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
            <MDBNavbar dark expand="md">

                <MDBNavbarBrand>
                    Blockchain
                </MDBNavbarBrand>

                <MDBNavbarToggler onClick={this.toggleCollapse}/>

                <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
                    <MDBNavbarNav left>

                        <MDBNavItem>
                            <MDBNavLink to="/blocks">Blocks</MDBNavLink>
                        </MDBNavItem>

                        <MDBNavItem>
                            <MDBNavLink to="/transactions">Transactions</MDBNavLink>
                        </MDBNavItem>

                        <MDBNavItem>
                            <MDBNavLink to="/inputs">Inputs</MDBNavLink>
                        </MDBNavItem>

                        <MDBNavItem>
                            <MDBNavLink to="/outputs">Ouputs</MDBNavLink>
                        </MDBNavItem>

                        <MDBNavItem>
                            <MDBNavLink to="/about">About</MDBNavLink>
                        </MDBNavItem>

                    </MDBNavbarNav>

                </MDBCollapse>
            </MDBNavbar>
        );
    }
}

export default Header;
