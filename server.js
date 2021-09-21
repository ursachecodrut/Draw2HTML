const express = require('express');
const fileUpload = require('express-fileupload');

const app = express();

app.use(fileUpload());
app.use(express.json());

let runPy = (image) => {
	return new Promise((resolve, reject) => {
		console.log('am intrat in script');
		const { spawn } = require('child_process');
		console.log(__dirname);
		const pyprog = spawn('python3', ['./pythonScripts/main.py', image]);

		console.log('test');
		pyprog.stdout.on('data', (data) => {
			resolve(data);
		});

		pyprog.stderr.on('err', (err) => {
			reject(err);
		});
	});
};

// Upload Endpoint
app.post('/upload', async (req, res) => {
	if (req.files === null) {
		return res.status(400).json({ msg: 'No file uploaded' });
	}

	const file = req.files.file;
	console.log(file);
	console.log('aici', `${__dirname}/client/public/uploads/${file.name}`);

	await file.mv(`${__dirname}/client/public/uploads/${file.name}`, (err) => {
		if (err) {
			console.error(err);
			return res.status(500).send(err);
		}
		// res.json({ fileName: file.name, filePath: `/uploads/${file.name}` });
		console.log({ fileName: file.name, filePath: `/uploads/${file.name}` });
	});
	runPy(file.name).then((fromRunPy) => {
		console.log(fromRunPy.toString());
		res.end(fromRunPy);
	});
	res.send('orice');
});

app.listen(5000, () => console.log('Server Started...'));
