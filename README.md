# MediCare-Prime 
<div align="center">

<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
<a href="https://github.com/IIITKalyaniFOSC/"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-GNU-blue.svg?v=103"></a>

<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/graphs/contributors"><img src="https://img.shields.io/github/contributors/IIITKalyaniFOSC/MediCare-Prime?color=brightgreen"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/stargazers"><img src="https://img.shields.io/github/stars/IIITKalyaniFOSC/MediCare-Prime?color=0059b3"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/network/members"><img src="https://img.shields.io/github/forks/IIITKalyaniFOSC/MediCare-Prime?color=yellow"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/issues"><img src="https://img.shields.io/github/issues/IIITKalyaniFOSC/MediCare-Prime?color=0059b3"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed-raw/IIITKalyaniFOSC/MediCare-Prime?color=yellow"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/pulls"><img src="https://img.shields.io/github/issues-pr/IIITKalyaniFOSC/MediCare-Prime?color=brightgreen"></a>
<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/pulls?q=is%3Apr+is%3Aclosed"><img src="https://img.shields.io/github/issues-pr-closed-raw/IIITKalyaniFOSC/MediCare-Prime?color=0059b3"></a> 
</div>

<img src="./static/images/MEDICARE.gif" align="right" height="450px" width="450px">
Prediction or detection of various medical ailments. Deployed locally using Flask 2.0.

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

## ✨ Contributors

<a href="https://github.com/IIITKalyaniFOSC/MediCare-Prime/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=IIITKalyaniFOSC/MediCare-Prime" />
</a>

## License
[GPL](https://github.com/IIITKalyaniFOSC/MediCare-Prime/blob/main/LICENSE)
 
