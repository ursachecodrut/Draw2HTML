const express = require('express');
// const bodyParser = require('body-parser');

const app = express();

const PORT = process.env.PORT || 5000;

// app.use(bodyParser.urlencoded());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

let runPy = (image) => {
	return new Promise((resolve, reject) => {
		const { spawn } = require('child_process');
		const pyprog = spawn('python3', ['./pythonScripts/main.py', image]);

		pyprog.stdout.on('data', (data) => {
			resolve(data);
		});

		pyprog.stderr.on('err', (err) => {
			reject(err);
		});
	});
};

app.post('/', (req, res) => {
	res.write('welcome\n');
	res.write(req.body.image);
	runPy(req.body.image).then((fromRunPy) => {
		console.log(fromRunPy.toString());
		res.end(fromRunPy);
	});
});

app.listen(PORT, (err) => {
	if (err) console.error(err);
	else console.log(`App listening on port ${PORT}`);
});
