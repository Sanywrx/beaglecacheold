/*
 * GET home page.
 */

exports.index = function (req, res) {

  fs.readFile(__dirname + '/views/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}
