from torchvision import transforms, utils, datasets
import nibabel as nib
import numpy as np

# dataroot = "../data/metastasises_dataset/train"

class NiiFolder(datasets.DatasetFolder):

    EXTENSIONS = '.nii'

    def __init__(self, root, transform=None, target_transform=None, loader=None):
        
        if loader is None:
            loader = self.__nii_loader

        super(NiiFolder, self).__init__(root, loader, self.EXTENSIONS, transform=transform)
        
#     def __getitem__(self, index):
#         ob = super(NiiFolder, self).__getitem__(index)
#         return (ob[0].transpose(3,2,0,1), ob[1]) #меняем порядок, что бы каналы были на втором месте

    @staticmethod
    def __nii_loader(path):
        img3d = nib.load(path)
        return np.asarray(img3d.get_fdata())