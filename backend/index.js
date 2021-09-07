const express = require('express');

const app = express();

const PORT = process.env.PORT || 5000;

let runPy = new Promise((resolve, reject) => {
	const { spawn } = require('child_process');
	const pyprog = spawn('python3', ['./main.py']);

	pyprog.stdout.on('data', (data) => {
		resolve(data);
	});

	pyprog.stderr.on('err', (err) => {
		reject(err);
	});
});

app.get('/', (req, res) => {
	res.write('welcome\n');
	runPy.then((fromRunPy) => {
		console.log(fromRunPy.toString());
		res.end(fromRunPy);
	});
});

app.listen(PORT, () => {
	console.log(`App listening on port ${PORT}`);
});
// const { spawn } = require('child_process');
