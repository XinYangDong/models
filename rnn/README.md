refers to: https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html

## First download dataset 
```bash
wget https://download.pytorch.org/tutorial/data.zip
unzip data.zip
```

## run rnn predict demo
```bash
python3 predict.py
```

## run rnn train demo
```bash
python3 train_rnn_oneflow.py
```

## run speed test against pytorch
```bash
python3 compare_oneflow_and_pytoch_rnn_speed.py
optional arguments:
  -h, --help     show this help message and exit
  --seed [SEED]  specify random seed
```
