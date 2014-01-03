fs = require('fs');

ramsize = process.argv[2];
clients = [];
seconds = [];
var TIMEOFFSET = 4;

thisClients;

fs.readdirSync(".").forEach(function(fileName)
	{
		var i = 0;
		while(fileName[i] != 'c'){ i++ };
		thisClients = fileName.slice(0, i);

		thisFile = fs.readFileSync(fileName).toString().split('\n');

		for(var j = 0; j < thisFile.length; j++)
		{
			clients.append(thisClients);
			ramsize.append(ramsize);
			seconds.append(thisFile[j].split(',')[TIMEOFFSET]);
		}


	});

finString = [];
for(var i = 0; i < seconds.length; i++)
{
	finString.append(ramsize[i] + ',' + clients[i] + ',' + seconds[i] + '\n');
}
console.log(finString.slice(1,5).toString());
//fs.writeFileSync("everythingout.csv", finString.toString());