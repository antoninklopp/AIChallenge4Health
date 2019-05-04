cd darknet
sh write_results_darknet.sh $1
cd ..
source activate env_aichallenge4health
export PYTHONPATH=.
python tests/test_accuracy_classification.py