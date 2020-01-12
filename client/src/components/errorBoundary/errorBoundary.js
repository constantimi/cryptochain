import React, {Component} from 'react';
import {MDBContainer} from 'mdbreact';

class ErrorBoundary extends Component {
    constructor(props) {
      super(props);
      this.state = { error: null, errorInfo: null };
    }
  
    componentDidCatch(error, errorInfo) {
      // log the error to our server with loglevel
      this.setState({
        error: error,
        errorInfo: errorInfo,
      })
      
    }
  
    render() {
      if (this.state.errorInfo) {
        // You can render any custom fallback UI
        return (
          <MDBContainer>          
            <h2>Something went wrong.</h2>
            <details style={{ whiteSpace: 'pre-wrap' }}>
              {this.state.error && this.state.error.toString()}
              <br />
              {this.state.errorInfo.componentStack}
            </details>
          </MDBContainer>        
        );
      }

      return this.props.children;
    }
}

export default ErrorBoundary;