import React, {Component} from 'react';
import { MDBContainer, MDBCol, MDBRow } from 'mdbreact';

import Chart from "chart.js";
import { fetchBitcoin } from '../../../actions/fetchBitcoinPriceActions';
import { fetchCurrentCryptoPrices } from '../../../actions/fetchCurrentCryptoPrices';
import { fetchCoinsList } from '../../../actions/fetchCoinsList';
import { fetchHistoricalCryptoData } from '../../../actions/fetchHistoricalCryptoData';


class LineGraph extends Component{

    chartRef = React.createRef();

    constructor(props) {
        super(props);
        this.state = {
          currentPrices: [],
        };

        this.getData = this.getData.bind(this);
    }

    // Method for fetching data

    getData() {
      const {currentPrices} = this.state;

        let linedata = [];
        let data = [];
        let labels = [];    
        
        // Additional methods
        // CURRENT ERROR MESSAGE WITH PROXY
        // fetchCurrentCryptoPrices().then(json => {
          
        //   console.log('CurrentCryptoPrices API call response: ', json);
          
        //   this.setState({
        //     currentPrices: json.data
        //   })
          
        // }).catch((err) => {
        //   throw new Error('fetchCurrentCryptoPrices', err.message);
        // });
        

        // fetchCoinsList().then(json => {
        //   console.log('CoinsList API call response:', json);
        // }).catch((err) => {
        //   throw new Error('fetchCoinsList', err.message);
        // });


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
              throw new Error('fetchBitcoinPriceActions', err.message);
            });

    };

    componentDidMount() { // lifecycle method
        this.getData();        
    }

    render () {
      const {currentPrices} = this.state;

        return(
            <MDBContainer className="graph_container">

              <MDBRow>
              
                <MDBCol className="col col-9">
                  {/* Bitcoin chart */}
                  <canvas id="myChart" ref={this.chartRef}/>
                </MDBCol>

                <MDBCol className="col col-3">

                  {/* {currentPrices.map((price, index) => {

                    return (
                      <MDBContainer> */}
                        <MDBRow>
                          <MDBCol className="col-2 col-sm-3"></MDBCol>
                          <MDBCol className="col-2 col-sm-3 table-bordered">name</MDBCol>
                          <MDBCol className="col-2 col-sm-3 table-bordered">price</MDBCol>
                        </MDBRow>
                      {/* </MDBContainer>
                    );
                    
                  })} */}
                  

                </MDBCol>
              
              </MDBRow>

            </MDBContainer>
        );
    };
}

export default LineGraph;