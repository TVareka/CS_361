var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');
var path = require('path');

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 11285);

app.get('/',function(req,res){
  if(!req.query.url) {
  	res.status(404).send("Error")
  } else if (!req.query.header) {
  	res.status(404).send("Error")
  }
  else { 
  	url_str = req.query.url;
  	header_str = req.query.header;
  	const spawn = require("child_process").spawn;
  	const pythonProcess = spawn('python', ["Web_Scraper.py", url_str, header_str]);
  // move this python file in the same file as node.js

  	pythonProcess.stdout.on('data', (data) => {
    // Do something with the data returned from python script
    res.setHeader('Content-Type', 'application/json');
    res.end(data);
});
};
});

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});