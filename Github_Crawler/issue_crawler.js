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

    let text = await tools.readTextFile('file:///Users/personanongrata/Documents/USC/RecDroid-Improvements/Github_Crawler/projects_list.txt');
    // console.log(text);
    let lines = text.split('\n');
    // console.log(lines);
    let project_issue_list = [];
    let issue_page_size = [];
    for(let i = 0; i < lines.length; i++){
        let args = lines[i].split(" ");
        project_issue_list.push(args[0]);
        issue_page_size.push(Math.ceil(parseFloat(args[1])/100));
    }
    // console.log(project_issue_list);
    // console.log(issue_page_size);

    // const browser = await puppeteer.launch({headless:false});
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    let pot_dup_issue = [];
    let pot_dup_app = [];

    for(let i = 0; i < project_issue_list.length; i++){
        for(let pg_i = 1; pg_i <= issue_page_size[i]; pg_i++){
            await page.goto(project_issue_list[i] + "?page=" + pg_i);

            let issue_ids = null;
            let issue_desc = null;
            let issue_tag = null;
            let start = Date.now();
            do {

                issue_ids = await
                    page.evaluate(() => {
                        let elements = Array.from(document.querySelectorAll(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > div > div > table > tbody > tr > td:nth-child(1) > a'));
                        return elements.map(td => td.textContent);
                    });
                issue_desc = await
                    page.evaluate(() => {
                        let elements = Array.from(document.querySelectorAll(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > div > div > table > tbody > tr > td:nth-child(2) > code'));
                        return elements.map(td => td.textContent);
                    });
                issue_tag = await
                    page.evaluate(() => {
                        let elements = Array.from(document.querySelectorAll(
                            '#maia-main > div > div.maia-cols > div:nth-child(2) > div > div > div > table > tbody > tr > td.ng-binding > span:nth-child(1) > span'));
                        return elements.map(td => td.textContent);
                    });

                // await page.waitFor(100);
                if(Date.now() - start > 4888){
                    break;
                }
            } while (issue_ids.length === 0 || issue_desc.length === 0);

            // console.log(issue_ids);
            // console.log(issue_desc);
            let eval_tag = true;
            if(issue_tag.length !== issue_desc.length){
                // console.log("ERROR");
                console.log("TAG/DESC MISMATCH " + project_issue_list[i] + "?page=" + pg_i);
                eval_tag = false;
            }


            for(let j = 0; j < issue_desc.length; j++){
                let issue_good = true;
                if(issue_desc[j] === "Duplicate"){
                    // console.log(issue_tag[j]);
                    if(eval_tag) {
                        for (let k = 0; k < bad_tags.length; k++) {
                            if (issue_tag[j] === bad_tags[k]) {
                                console.log(
                                    "BAD TAG: " + project_issue_list[i] + "/" +
                                    issue_ids[j]);
                                issue_good = false;
                            }
                        }
                    }
                    if(issue_good) {
                        pot_dup_issue.push(
                            project_issue_list[i] + "/" + issue_ids[j]);
                        if (pot_dup_app.length === 0 ||
                            pot_dup_app[pot_dup_app.length - 1] !==
                            project_issue_list[i]) {
                            pot_dup_app.push(project_issue_list[i]);
                        }
                    }
                }
            }
        }
    }
    console.log(pot_dup_app);
    console.log(pot_dup_issue);

    let output_app = "";
    for(let i = 0; i < pot_dup_app.length; i++){
        output_app += pot_dup_app[i] + "\n";
    }

    let output_issue = ""
    for(let i = 0; i < pot_dup_issue.length; i++){
        output_issue += pot_dup_issue[i] + "\n";
    }

    tools.writeTextFile('rm_fr_app.txt', output_app);
    tools.writeTextFile('rm_fr_issue.txt', output_issue);

    await browser.close();
})();