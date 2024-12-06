import torch

from torch.utils import data


class Dataset(data.Dataset):
    def __init__(self, dataset, transformation, encoder):
        self._dataset = dataset
        self._transformation = transformation
        self._encoder = encoder

    def __getitem__(self, index):
        img, lbl = self._dataset[index]
        img_, bboxes_, labels_ = self._transformation(img, lbl["boxes"], lbl["labels"])
        lbl_encoded = self._encoder(bboxes_, labels_)
        return img_, torch.from_numpy(lbl_encoded)

    def __len__(self):
        return len(self._dataset)
