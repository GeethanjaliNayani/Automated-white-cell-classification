# Data Dictionary – WBC Classification Project

Below are the main data artifacts and variables used:

1. **Image** → Raw microscopy image of blood smear (RGB or grayscale).
2. **Mask / Segmented Mask** → Binary mask indicating location of WBC in image.
3. **BoundingBox / ROI Coordinates** → Coordinates of detected cell region(s).
4. **Features** → Extracted quantitative metrics per cell (e.g. area, perimeter, texture features, shape descriptors).
5. **Label** → Ground truth class of WBC (e.g. Neutrophil, Lymphocyte, Monocyte, Eosinophil, Basophil).
6. **Predicted Label** → Model’s predicted class for the cell.
7. **Probability Scores** → Confidence scores for each class output by model.
8. **Accuracy / Precision / Recall / F1** → Evaluation metrics computed on test set.
9. **Loss** → Training loss per epoch (if deep learning model used).
10. **Epoch** → Training epoch index.  
