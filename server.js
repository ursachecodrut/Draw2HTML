const express = require('express');
const fileUpload = require('express-fileupload');

const app = express();

app.use(fileUpload());
app.use(express.json());

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

// Upload Endpoint
app.post('/upload', async (req, res) => {
	if (req.files === null) {
		return res.status(400).json({ msg: 'No file uploaded' });
	}

	const file = req.files.file;

	await file.mv(`${__dirname}/client/public/uploads/${file.name}`, (err) => {
		if (err) {
			console.error(err);
			return res.status(500).send(err);
		}
		res.json({ fileName: file.name, filePath: `/uploads/${file.name}` });
	});
	runPy(file.name).then((fromRunPy) => {
		console.log(fromRunPy.toString());
		res.end(fromRunPy);
	});
});

app.listen(5000, () => console.log('Server Started...'));
