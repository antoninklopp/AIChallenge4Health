rm -rf DataChallenge/train_individuals
mkdir DataChallenge/train_individuals
echo "Removed files"
export PYTHONPATH=.
source activate env_aichallenge4health
python src/import_data.py
python src/create_weights_yolo.py
echo "exports python done"
cd rescaling_cpp/bin
make
./rescaling
echo "Finished"