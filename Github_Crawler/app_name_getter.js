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
    // const browser = await puppeteer.launch()
    // let bad_tags = ['Type-Enhancement', 'Type-FeatureRequest'];
    //
    // let text = await tools.readTextFile('file:///Users/personanongrata/Documents/USC/RecDroid-Improvements/Github_Crawler/0_issues.txt');
    // // console.log(text);
    // let lines = text.split('\n');
    // // console.log(lines);
    // let issue_list = [];
    // // let issue_page_size = [];
    // for(let i = 0; i < lines.length; i++){
    //     issue_list.push(lines[i]);
    // }

    const link = "https://raw.githubusercontent.com/pcqpcq/open-source-android-apps/master/categories/";
    let categories = ['communication','education','finance','game','health_fitness','life_style','multi_media','news_and_magazines','personalization','productivity','social_network','tools','travel_and_local','business'];
    // console.log(project_issue_list);
    // console.log(issue_page_size);
    // const browser_0 = await puppeteer.launch({headless:false});
    // const page_0 = await browser_0.newPage();
    // await page_0.goto("http://code.google.com/p/android/issues/detail?id=" + issue_list[0]);
    // await page_0.waitFor(25000);

    const browser = await puppeteer.launch({headless:false});
    // const browser = await puppeteer.launch();
    const page = await browser.newPage();
    // await page.goto("http://code.google.com/p/android/issues/detail?id=" + issue_list[0]);
    // await page.waitFor(25000);



    for(let i = 0; i < categories.length; i++){
        await page.goto(link + categories[i] + ".md");
        // await page.waitFor(15000);
        let re = /\((https:\/\/github\.com\/(?:.*?)\/(?:.*?))\)/g;
        // console.log(page.url());

        // console.log(typeof page.url());
        const html = await page.content();
        // console.log(html)

        let matches = re.exec(html);
        // console.log(matches.length)
        while(matches != null){
            let match = matches[1].charAt(matches[1].length - 1) === '/' ? matches[1] : matches[1] + '/';
            if((match.split("/").length - 1)  === 5) {
                console.log(match);
            }
            matches = re.exec(html);
        }

        // if(i > 100) break;
    }

    await browser.close();
    // await browser_0.close();
})();