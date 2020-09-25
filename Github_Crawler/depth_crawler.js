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
    // let bad_tags = ['Type-Enhancement', 'Type-FeatureRequest'];

    let text = await tools.readTextFile('file:///Users/personanongrata/Documents/USC/RecDroid-Improvements/Github_Crawler/rm_fr_issue.txt');
    // console.log(text);
    let issue_list = text.split('\n');
    // console.log(lines);
    // let issue_list = [];
    // for(let i = 0; i < lines.length; i++){
    //     let args = lines[i].split(" ");
    //     project_issue_list.push(args[0]);
    //     issue_page_size.push(Math.ceil(parseFloat(args[1])/100));
    // }
    // console.log(project_issue_list);
    // console.log(issue_page_size);

    // const browser = await puppeteer.launch({headless:false});
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    let good_text = ['What steps will reproduce the problem?', 'What is the expected output?'];
    let filtered_issue = [];

    for(let i = 0; i < issue_list.length; i++){
        // console.log(issue_list[i]);
        await page.goto(issue_list[i]);
        await page.waitFor(250);
        let text = "";
        let start = Date.now();
        do {
            text = await
                page.evaluate(() => {
                    let element = document.querySelector(
                        '#maia-main > div > div > div.maia-cols > div:nth-child(2) > div > div.maia-col-8');
                    return element.textContent;
                });
            if(Date.now() - start > 4888){
                console.log("ERROR: " + issue_list[i]);
                break;
            }
        }while(text.length === 0);

        for(let j = 0; j < good_text.length; j++){
            if(text.includes(good_text[j])){
                filtered_issue.push(issue_list[i]);
                console.log("GOOD: " + issue_list[i]);
                break;
            }
        }
        // console.log(issue_list[i]);
        // console.log(text);
        // break;
    }
    console.log(filtered_issue);
    //
    // let output_app = "";
    // for(let i = 0; i < pot_dup_app.length; i++){
    //     output_app += pot_dup_app[i] + "\n";
    // }
    //
    let output_issue = "";
    for(let i = 0; i < filtered_issue.length; i++){
        output_issue += filtered_issue[i] + "\n";
    }
    //
    // tools.writeTextFile('rm_fr_app.txt', output_app);
    tools.writeTextFile('fl_issue.txt', output_issue);

    await browser.close();
})();