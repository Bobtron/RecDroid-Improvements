var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const fs = require('fs');
const tools = this;
const LONG_DELAY = 2000;
const HUMAN_DELAY = 100;

var exports = module.exports = {
    readTextFile: function (file)
    {
        return new Promise(function (resolve) {
            let rawFile = new XMLHttpRequest();
            rawFile.open("GET", file, true);
            rawFile.onreadystatechange = function () {
                if (rawFile.readyState === 4) {
                    if (rawFile.status === 200 || rawFile.status === 0) {
                        resolve(rawFile.responseText);
                    }
                }
            };
            rawFile.send(null);
        })
    },

    writeTextFile: function (file, text)
    {
        fs.writeFile(file, text, (err) => {
            // throws an error, you could also catch it here
            if (err) throw err;

            // success case, the file was saved
            // console.log('Lyric saved!');
        });
    },

    // distanceBetweenPoints: function(xone, yone, xtwo, ytwo){
    //     // return new Promise(function (resolve) {
    //     //     resolve(Math.sqrt(Math.pow(xone - xtwo,2) + Math.pow(yone - ytwo, 2)));
    //     // })
    //     return Math.sqrt(Math.pow(xone - xtwo,2) + Math.pow(yone - ytwo, 2));
    // },
    //
    // getDistance: function(page){
    //     return new Promise(async function (resolve){
    //         let distanceResult = await page.evaluate(() => {
    //             let element = document.querySelector('#locationInner > div:nth-child(2) > div:nth-child(2)');
    //             return element.textContent;
    //         });
    //
    //         let re = /Distance: \n(.+?) squares/g;
    //         let matches = re.exec(distanceResult);
    //
    //         let distStr = matches[1].replace(/[^0-9.]+/g, '');
    //
    //         let distance = parseFloat(distStr);
    //         resolve(distance);
    //     })
    // },
    //
    // sendHarvesters: function(page, harvesterType, amount, x, y){
    //     return new Promise(async function (resolve) {
    //         await Promise.all([page.waitForNavigation(), page.goto('https://elgea.illyriad.co.uk/#/Trade/Orders/' + x + '/' + y + '?ActionTypeID=2'),]);
    //         await page.waitFor(LONG_DELAY);
    //
    //         let distance = await exports.getDistance(page);/*parseFloat(matches[1].replace(/[^0-9.]+/g, ''));*/
    //
    //         if(distance > 300){
    //             /*console.log('ERROR IN LOCATION CALCULATION...SHUTTING DOWN');
    //             await browser.close();*/
    //             resolve(false);
    //         }
    //
    //         let sendMenuText = await
    //             page.evaluate(() => {
    //                 let elements = Array.from(document.querySelectorAll('table.center > tbody:nth-child(1) > tr > td'));
    //                 return elements.map(td => td.innerHTML);
    //             });
    //
    //         // console.log(sendMenuText);
    //
    //         //find which row the miners/herbalists/skinners should be sent
    //         let row = 2;
    //         for (let l = 1; l < sendMenuText.length; l += 10) {
    //             if (sendMenuText[l] === harvesterType) {
    //                 break;
    //             }
    //             row++;
    //         }
    //
    //         // console.log(row);
    //         // console.log(amount);
    //         console.log("SENDING " + amount + " " + harvesterType + "s to (" + x + ", " + y + "), distance: " + distance);
    //
    //         //sending harvester code, with the given row
    //         await
    //             page.type('table.center > tbody:nth-child(1) > tr:nth-child(' + row + ') > td:nth-child(10) > form:nth-child(1) > input:nth-child(4)', amount.toString(), {delay: HUMAN_DELAY});
    //         await
    //             page.click('table.center > tbody:nth-child(1) > tr:nth-child(' + row + ') > td:nth-child(10) > form:nth-child(1) > input:nth-child(6)', {delay: HUMAN_DELAY});
    //         await
    //             page.waitFor(LONG_DELAY);
    //
    //         resolve(true);
    //     })
    // }
};