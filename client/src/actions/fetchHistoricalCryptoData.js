
import axios from 'axios';


export function fetchHistoricalCryptoData(cryptocoin){
    var moment = require('moment');
    var displayMonthsBack = 12;

    // Returns an array of dates between the two dates
    var getDates = function(startDate, endDate) {
        var dates = [],
            currentDate = startDate,
            addDays = function(days) {
            var date = new Date(this.valueOf());
            date.setDate(date.getDate() + days);
            return date;
            };
        while (currentDate <= endDate) {
        dates.push(currentDate);
        currentDate = addDays.call(currentDate, 1);
        }
        return dates;
    };

    // Fetching data
    var dates = getDates(moment(new Date()).subtract(displayMonthsBack, 'month'), new Date());                                                                                                           
    dates.forEach(function(date) {
   
        axios.get(`https://api.coingecko.com/api/v3/coins/${cryptocoin}/history?date=${moment(date).format('DD-MM-YYYY')}`, {
            method: 'GET',
            mode: 'CORS',
            json: true
        }).then(response => { 
            console.log('fetchHistoricalCryptoData API call response:', response);
        });

    });
}

// Additional information:
// https://www.coingecko.com/en/api#explore-api