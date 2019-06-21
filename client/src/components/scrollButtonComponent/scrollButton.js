import React, {Component} from 'react';

class ScrollButton extends Component {

    constructor(props) {
        super(props);

        this.state = {
            intervalId: 0
        };
    };

    scrollStep() {
        if (window.pageYOffset === 0) {
            clearInterval(this.state.intervalId)
        }
        window.scroll(0, window.pageYOffset - this.props.scrollStepInPx);
    };

    scrollToTop() {
        let intervalId = setInterval(this.scrollStep.bind(this), this.props.delayInMs);
        this.setState({intervalId: intervalId});
    };

    render() {
        return (

            <button title='scrollButton' className='scroll'
                    onClick={() => {
                        this.scrollToTop()
                    }}>
                <span className='arrow-up fa fa-lg fa-chevron-up'/>
            </button>

        );
    };
}

export default ScrollButton;
