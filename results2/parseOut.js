fs = require('fs');

ramsize = process.argv[2];
clients = [];
seconds = [];
var TIMEOFFSET = 4;

var thisClients;

fs.readdirSync(".").forEach(function(fileName)
	{
		var i = 0;
		while(fileName[i] != 'c'){
		 	i++;
		 	if(i == fileName.length - 1)
		 	{
		 		return;
		 	} 
		 };

		thisClients = fileName.slice(0, i);

		thisFile = fs.readFileSync(fileName).toString().split('\n');
		for(var j = 0; j < thisFile.length; j++)
		{
			if(thisFile[j].split(',')[TIMEOFFSET] == undefined)
			{
				continue;
			}
			clients.push(thisClients);
			seconds.push(thisFile[j].split(',')[TIMEOFFSET]);

		}

	});
finString = [];
for(var i = 0; i < seconds.length; i++)
{
	finString.push(ramsize + ',' + clients[i] + ',' + seconds[i] + '\n');
}
fs.writeFileSync("everythingout.csv", finString.join('\n'));