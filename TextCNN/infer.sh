set -aux

MODEL_PATH="checkpoints"
VOCAB_PATH="vocab.pkl"
CONFIG_PATH="config.json"
TEXT="My boyfriend and I went to watch The Guardian.At first I didn't want to watch it, but I loved the movie- It was definitely the best movie I have seen in sometime.They portrayed the USCG very well, it really showed me what they do and I think they should really be appreciated more.Not only did it teach but it was a really good movie. The movie shows what the really do and how hard the job is.I think being a USCG would be challenging and very scary. It was a great movie all around. I would suggest this movie for anyone to see.The ending broke my heart but I know why he did it. The storyline was great I give it 2 thumbs up. I cried it was very emotional, I would give it a 20 if I could!"

python3 infer.py --model_path $MODEL_PATH --vocab_path $VOCAB_PATH --config_path $CONFIG_PATH --text $TEXT
