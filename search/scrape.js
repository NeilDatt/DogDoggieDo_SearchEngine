const puppeteer = require('puppeteer');

async function scrapeProduct(url){
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    page.goto(url);

    const [el] = await page.$x('//*[@id="rso"]/div[1]/div/div[1]');
    const txt = await el.getProperty('txtContent');
    const rawTxt = await txt.jsonValue();

    console.log('rawTxt')
}

scrapeProduct('https://www.google.com/search?q=what%20is%20the%20time')