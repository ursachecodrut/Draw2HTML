const express = require('express');
const fileUpload = require('express-fileupload');
let cors = require('cors');

const app = express();

const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(fileUpload());
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

app.post('/upload', (req, res) => {
	if (req.files === null) {
		return res.status(400).json({ msg: 'No file was uploaded' });
	}

	const file = req.files.file;

	file.mv(`${__dirname}/../frontend/public/uploads/${file.name}`, (err) => {
		if (err) {
			console.error(err);
			return res.status(500).send(err);
		}
		res.json({ fileName: file.name, filePath: `/uploads/${file.name}` });
	});
});

app.listen(PORT, (err) => {
	if (err) console.error(err);
	else console.log(`App listening on port ${PORT}`);
});
