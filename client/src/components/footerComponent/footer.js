import React from "react";
import {MDBContainer, MDBFooter} from "mdbreact";

const Footer = () => {
    return (
        <MDBFooter color="indigo" className="font-small pt-0">
            <div className="footer-copyright text-center">
                <MDBContainer className="footer_content">
                    &copy; {new Date().getFullYear()} Copyright:
                    <a href="https://github.com/constantinss?tab=repositories"> GitHub.com </a>
                </MDBContainer>
            </div>
        </MDBFooter>
    );
};

export default Footer;