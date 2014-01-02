var fs = require('fs');

var baseURL = "http://192.168.2.11:3000"
if(process.argv.length < 4)
{
	console.log("Usage: node makeURLs.js numUrls outfile");
	return;
}

var urlList = "";
var numUrls = process.argv[2];

for(var i = 0; i < numUrls; i++)
{
	urlList += baseURL + "/" + i + '\n';
}

urlList = urlList.substring(0, urlList.length - 1);


fs.writeFileSync(process.argv[3], urlList);

