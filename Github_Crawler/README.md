# Node-js files used for crawling

First download then do npm init.

Then do npm install puppeteer.

Lots of the .js files are specific files I wrote for extracting details about github issues from specific apps so I don't have to do it by hand, and unless you're doing that they're pretty useless.

Since the github issues page have separate tags for each project, and I dont have the time/processing power to open up every single issue, you kind of have to hand write code for each project, to determine whether or not an issue is worth looking into just by their title/tags.

Otherwise, project_crawler.js is what you want to use for getting stuff off of google-code archive.
