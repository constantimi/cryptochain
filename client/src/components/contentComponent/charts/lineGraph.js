import React, {Component} from 'react';
import { MDBContainer } from 'mdbreact';

import Chart from "chart.js";
import { fetchBitcoin } from '../../../actions/fetchBitcoinPriceActions';
import { fetchCurrentCryptoPrices } from '../../../actions/fetchCurrentCryptoPrices';
import { fetchCoinsList } from '../../../actions/fetchCoinsList';
import { fetchHistoricalCryptoData } from '../../../actions/fetchHistoricalCryptoData';


class LineGraph extends Component{

    chartRef = React.createRef();

    constructor(props) {
        super(props);
    }

    // Method for fetching data

    getData() {

        let linedata = [];
        let data = [];
        let labels = [];    
        
        // Additional methods
        fetchCurrentCryptoPrices().then(response => {
          console.log('CurrentCryptoPrices API call response:', response);
        }).catch((err) => {
          console.log('CurrentCryptoPrices API call error:', err.message);
        });
        
        fetchCoinsList().then(response => {
          console.log('CoinsList API call response:', response);
        }).catch((err) => {
          console.log('CoinsList API call error:', err.message);
        });

        fetchHistoricalCryptoData('bitcoin');
                
        
        // Fetching bitcoin price
        fetchBitcoin().then((json) => {
                
                linedata = json.data.bpi;
                data = Object.keys(linedata).map(key => linedata[key]);
                labels = Object.keys(linedata);
                
                const myChartRef = this.chartRef.current.getContext("2d");
        
                new Chart(myChartRef, {
                    type: 'line',
                    data: {
                    labels: labels,
                    datasets: [
                        {
                        label: 'Bitcoin',
                        data: data,
                        borderColor: "#80ffaa",
                        fill: false,
                        }
                    ]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'Information for current Bitcoin price'
                        },
                        tooltips: {
                            mode: 'index',
                            intersect: false,
                          },
                         hover: {
                            mode: 'nearest',
                            intersect: true
                          },
                          scales: {
                            xAxes: [{
                              display: true,
                              scaleLabel: {
                                display: true,
                              },
                              type: 'time',
                                time: {
                                    unit: 'month'
                                }
                            }],
                            yAxes: [{
                              display: true,
                              scaleLabel: {
                                display: true,
                                labelString: 'USD'
                              }
                            }]
                          }
                    }
                });

            })
            .catch(err => {
                console.error('err', err)
            });

    };

    componentDidMount() { // lifecycle method
        this.getData();        
    }

    render () {
        return(
            <MDBContainer className="graph_container">
                <canvas id="myChart" ref={this.chartRef}/>
            </MDBContainer>
        );
    };
}

export default LineGraph;