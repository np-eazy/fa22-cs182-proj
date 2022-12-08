# Collaborators:
Joey Zhu (3034710771, joey.j.zhu@berkeley.edu)  
Calvin Yan (3034728022, calvinyan@berkeley.edu)  
Alec James (3034541355, alehero@berkeley.edu)  
Anthony Zhang (3036218223, anthony_zhang1234@berkeley.edu)  

# Writeup:
Our full writeup can be found [here.](https://docs.google.com/document/d/11M-RaV-CoSOn_s33ZAN3cl8BvORWqM5JV4Jn7KMgf9A/edit?usp=sharing)

# What your repository should look like
`Data_Generation.ipynb` - produces and stores mock sequence of quantum wavelet images
`Schrodinger_Network.ipynb` - runs generated data through a convolutional autoencoder
`Schrodinger_Visualization.ipynb` - toy code to visualize model input and output, no need to run
`small_data_0.npy` and `big_data_5.npy` - the necessary input data for the model. You must add this yourself; see instructions for more details.

# Instructions
### BEFORE RUNNING ANYTHING:
The model requires input data that was too large to upload to Github. You must download it manually, [here](https://drive.google.com/file/d/1LSFFQ69SqGq7GAMg-7BeM5VD_VwT1pyD/view?usp=sharing) and [here](https://drive.google.com/file/d/10cq1oGturd_qx-uUPOeScVw73KwPNpwS/view?usp=sharing).  
You can also produce the data by running `Data_Generation.ipynb`. This will add the files to your mounted Google Drive, which you should download into this repository.  
To verify our model performance, run `Schrodinger_Network.ipynb` and observe the resulting plots, discussed in our writeup.