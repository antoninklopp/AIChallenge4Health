[![Build Status](https://travis-ci.com/antoninklopp/AIChallenge4Health.svg?token=8pPsJszYyD4F2sH8gLrb&branch=master)](https://travis-ci.com/antoninklopp/AIChallenge4Health)
[![CodeFactor](https://www.codefactor.io/repository/github/antoninklopp/aichallenge4health/badge)](https://www.codefactor.io/repository/github/antoninklopp/aichallenge4health)

## AI Challenge for Health

## Goal of the challenge

*The purpose of this challenge is to carry out spot detection in X-ray medical images in the surgical field. The scanned object is a calibration chart composed of 61 radiopaque steel balls. The nature and geometry of this object are perfectly known and the aim is to accurately determine the center position of the steel balls in the images. This information is then used to calibrate the acquisition device. In the future, the final goal of this operation is to bring patient 3D image reconstruction inside the medical operation rooms, based on acquisition machines such as the mobile C-Arm (2D radiology images) that are less expensive and more practical than other larger machines.* from the site description : https://competitions.codalab.org/competitions/21639#learn_the_details-evaluation  

You can find all the informations here : https://competitions.codalab.org/competitions/21639#learn_the_details-overview

## Run and test

```console
me@machine:~$ pip install -e . # Only first time
me@machine:~$ export PYTHONPATH=. 
me@machine:~$ python3 setup.py test # To test all unit tests
me@machine:~$ python3 tests/__test_test_you_want.py
```

## Contribute

To create a new model, have a look at : [Models' README](src/models/README.md)