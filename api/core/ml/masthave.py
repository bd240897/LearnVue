
# загрузка
# !pip install -q kaggle
# import os
# os.environ['KAGGLE_USERNAME'] = "bd240897" # username from the json file
# os.environ['KAGGLE_KEY'] = "244bce19a6b711ef86b470417e0b30da" # key from the json file
# ! kaggle competitions download -c journey-springfield
# ! unzip -q /content/journey-springfield.zip
# data_dir = './'
# data_train_dir = './train/simpsons_dataset'
# data_testset_dir = './testset'
# sample_submission_file = './sample_submission.csv'

# получение кол-ва классов
# n_classes = len(np.unique(train_val_labels))

# получение имена меток
# labels = np.unique(train_val_labels)

# сохранение меток в пикл
# with open("labels", "wb") as fp:   #Pickling
#   pickle.dump(labels, fp)


##сохранение меток в json
# labels_list = labels.tolist()
#
# import json
#
# with open("labels.json", 'w') as f:
#   # indent=2 is not needed but makes the file human-readable
#   # if the data is nested
#   json.dump(labels_list, f, indent=2)


# probs_im = predict_one_sample(model, ex_img.unsqueeze(0)) # добавляет новое измерения для [Channel, Row, Intensity]к [Batch, Channel, Row, Intensity]

# что делает x = x.view(x.size(0), -1)
# "Что делает команда: x.view(x.size(0), -1)?" https://ru.stackoverflow.com/questions/962937/Что-делает-команда-x-viewx-size0-1
# данная строка кода отвечает за изменение размерности тензора x таким образом что размерность первой оси (первого измерения) остается неизменной, а все остальные измерения упаковываются в одно, так чтобы получился 2D тензор с сохранением общего числа элементов.
# (2, 3, 4) в (2, 12)

# modal.eval - переводит режим модели на предсказание