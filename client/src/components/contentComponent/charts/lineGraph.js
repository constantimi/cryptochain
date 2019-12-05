import React, {Component} from 'react';
import { MDBContainer } from 'mdbreact';

import Chart from "chart.js";


class LineGraph extends Component{

    chartRef = React.createRef();
    
    componentDidMount() {
        const myChartRef = this.chartRef.current.getContext("2d");
        
        new Chart(myChartRef, {
            type: "line",
            data: {
                //Bring in data
                labels: ["Jan", "Feb", "March"],
                datasets: [
                    {
                        label: "Sales",
                        data: [86, 67, 91],
                    }
                ]
            },
            options: {
                //Customize chart options
            }
        });
    }

    render () {
        return(
            <MDBContainer className="graphContainer">
                <canvas id="myChart" ref={this.chartRef}/>
            </MDBContainer>
        );
    };
}

export default LineGraph;