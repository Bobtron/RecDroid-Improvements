// var gs = require('github-scraper');
//
// var start = 1;
// var url = 'samuelclay/NewsBlur/issues/'; // a random username
//
// for(var i = start; i < 2; i++) {
//     gs(url + i, function(err, data) {
//         console.log(data); // or what ever you want to do with the data
//     });
// }

// var gs  = require('github-scraper');
// var url = '/dwyl/tudo/issues/51';
// gs(url, function (err, data) {
//     console.log(data); // use the data how ever you like
// });

const puppeteer = require('puppeteer');
const tools = require('./Tools');

(async () => {

    // const browser = await puppeteer.launch({headless:false});
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    let issue_size = [];
    let good_proj = [];
    let error_proj = [];

    for(let result_page = 1; result_page <= 51; result_page++) {
        console.log("Results Page: " + result_page);
        await page.goto(
            'https://code.google.com/archive/search?q=domain:code.google.com%20label:Android&page=' + result_page);
        // await page.screenshot({path: 'example.png'});
        // await Promise.all([page.waitForNavigation(),]);
        let projectURLs = null;
        let start = Date.now();
        do {
            projectURLs = await
                page.evaluate(() => {
                    let elements = Array.from(document.querySelectorAll(
                        '#maia-main > div > div.maia-cols > div > div.ng-scope > div > project-search-result-widget > div > div > div.maia-col-8 > p:nth-child(1) > a'));
                    return elements.map(td => td.href);
                });
            if(Date.now() - start > 8888){
                break;
            }
        } while (projectURLs.length === 0);

        // await page.waitFor(10000);

        for (let i = 0; i < projectURLs.length; i++) {
            await page.goto(projectURLs[i] + '/issues');
            let header = null;
            let error_msg = null;
            start = Date.now();
            do {

                header = await
                    page.evaluate(() => {
                        let elements = Array.from(document.querySelectorAll(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > div > div > table > tbody > tr:nth-child(1) > th:nth-child(1)'));
                        return elements.map(td => td.textContent);
                    });
                error_msg = await
                    page.evaluate(() => {
                        let elements = Array.from(document.querySelectorAll(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > p'));
                        return elements.map(td => td.textContent);
                    });

                // await page.waitFor(100);
                if(Date.now() - start > 4888){
                    break;
                }
            } while (header.length === 0 && error_msg.length === 0);

            if (header.length) {
                let num_issues = await
                    page.evaluate(() => {
                        let element = document.querySelector(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a');
                        return element.textContent;
                    });
                issue_size.push(num_issues);
                good_proj.push(projectURLs[i] + '/issues');
            } else {
                error_proj.push(projectURLs[i])
            }
        }
    }

    console.log(issue_size);
    console.log();
    console.log(good_proj);
    console.log();
    console.log(error_proj);

    let output_string = "";
    for(let i = 0; i < good_proj.length; i++){
        output_string += good_proj[i] + " " + issue_size[i] + "\n"
    }

    tools.writeTextFile('projects_list.txt', output_string);

    await browser.close();
})();