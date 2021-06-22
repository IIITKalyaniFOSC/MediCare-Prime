# MediCare-Prime
Prediction or detection of various medical ailments. Deployed locally using Flask 2.0.

<center><img src="./static/images/MEDICARE.gif"></center>

## Setup

Assuming you have Ananconda or Miniconda3 already working, create a tensorflow conda environment and install a few libraries into it, and then we're ready to go.

* Install the current release of CPU-only TensorFlow, recommended for beginners:

```bash
conda create -n tf tensorflow
conda activate tf
```

* Or, to install the current release of GPU TensorFlow on Linux or Windows:

```bash
conda create -n tf-gpu tensorflow-gpu
conda activate tf-gpu
```

* Cd into your newly created environment (from command line or terminal)
```bash
cd C:\...\path-to-your-conda-environment\
```

* Installing modules we will need 
Though your virtual env will have all required modules, here are some extra ones required to setup this project locally
```bash
pip install flask
pip install pillow
```

## Running the code

* Fork and clone the project.

```bash
git clone https://github.com/IIITKalyaniFOSC/MediCare-Prime
```
* Cd into your cloned repo (folder with the same name as the repo on your system)
```bash
cd C:\...\path-to-your-cloned-repo\
```
* After making sure your tf conda environment we just created above, is activated, run the app.py file
```bash
python app.py
```

Succesfull installation and running will give you a link you can visit locally. For any exceptions, kindly recheck the entire process and try again, or feel free to create an issue.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://github.com/IIITKalyaniFOSC/MediCare-Prime/blob/main/LICENSE)
 
