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
    // const browser = await puppeteer.launch();
    // const page = await browser.newPage();
    //
    //
    //
    // await browser.close();
    let bad_tags = ['Type-Enhancement', 'Type-FeatureRequest'];

    let text = await tools.readTextFile('file:///Users/personanongrata/Documents/USC/RecDroid-Improvements/Github_Crawler/0_issues.txt');
    // console.log(text);
    let lines = text.split('\n');
    // console.log(lines);
    let issue_list = [];
    // let issue_page_size = [];
    for(let i = 0; i < lines.length; i++){
        issue_list.push(lines[i]);
    }
    // console.log(project_issue_list);
    // console.log(issue_page_size);
    // const browser_0 = await puppeteer.launch({headless:false});
    // const page_0 = await browser_0.newPage();
    // await page_0.goto("http://code.google.com/p/android/issues/detail?id=" + issue_list[0]);
    // await page_0.waitFor(25000);

    const browser = await puppeteer.launch({headless:false});
    // const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("http://code.google.com/p/android/issues/detail?id=" + issue_list[0]);
    await page.waitFor(25000);


    for(let i = 213; i < issue_list.length; i++){
        await page.goto("http://code.google.com/p/android/issues/detail?id=" + issue_list[i]);
        // await page.waitFor(15000);

        console.log(page.url());
        // console.log(typeof page.url());
        // const html = await page.content();
        // console.log(html)

        // if(i > 100) break;
    }

    await browser.close();
    // await browser_0.close();
})();