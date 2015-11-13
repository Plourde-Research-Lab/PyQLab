var express = require('express');
var compress = require('compression');
var path = require('path');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

///////////////////////////////////////////////////////////////
////////////////// SET UP EXPRESS SERVER //////////////////////
///////////////////////////////////////////////////////////////

var app = express();

app.set('port', process.env.PORT || 80);

app.use(compress());
// app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cookieParser());

app.use(express.static(path.join(__dirname, '/client')));
app.use('/bower_components', express.static(__dirname + '/bower_components'));
app.use('/views', express.static(__dirname + '/client/views'));

app.listen(app.get('port'), function() {
    console.log('Express server listening on port ' + app.get('port'));
});

///////////////////////////////////////////////////////////////
/////////////////// LOAD CONFIG FILES  ////////////////////////
///////////////////////////////////////////////////////////////

var channels = require('./server/Config/ChannelParams.json');
var instruments = require('./server/Config/Instruments.json');
var measurements = require('./server/Config/Measurements.json');
var sweeps = require('./server/Config/Sweeps.json')
var settings = require('./server/DefaultExpSettings.json');

app.get('/settings', function (req, res) {
	res.json(settings);
});

app.get('/libraries', function (req, res) {
	res.json({
		"instrs": instruments,
		"measurements": measurements,
		"sweeps": sweeps,
		"channels": channels
	})
})