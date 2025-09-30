# User Guide – Automated WBC Classification

This guide helps you run, interpret, and use the notebooks and models in this project.

## Notebooks

- **WBC_detection_and_classification.ipynb**  
  - Preprocessing of raw images  
  - Segmentation / detection of WBCs  
  - Visual output: input image overlaid with detected cell regions  

- **WBC_Classification.ipynb**  
  - Feature extraction or CNN pipeline  
  - Training, validation, and testing of classification models  
  - Visualization: confusion matrix, metrics, sample predictions  

## How to Use

1. Load your raw microscopy images into the `data/` folder  
2. In detection notebook: run segmentation cells and verify output  
3. In classification notebook: train or load existing model  
4. Predict classes on new images and view output overlays  

## Interpretation

- **Confusion Matrix** → Shows how many cells of each true class got misclassified  
- **Accuracy / Precision / Recall / F1** → Metrics to gauge model performance  
- **Sample Predictions** → Display images with predicted labels to visually inspect results  
- Use data augmentation for small datasets (rotation, flipping, scaling)  
- Regularize or dropout to avoid overfitting  
- Use cross-validation or hold-out test sets for evaluation  
- Check misclassified images manually to spot patterns  
