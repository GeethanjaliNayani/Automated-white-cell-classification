# Automated White Blood Cell classification
Developed a deep learning pipeline leveraging Convolutional Neural Networks (CNNs) to classify white blood cells from microscopic blood smear images, aiding early detection of hematological conditions. Collaborated with domain experts to ensure clinical relevance, optimized model performance through rigorous evaluation, and presented findings to both technical and non-technical stakeholders for deployment readiness, bridging AI innovation with healthcare impact.
**Key Features:**
1. Neural Network Pipeline: Designed and implemented an end-to-end CNN-based model for classifying white blood cells from microscopic smear images.
2. Model Training & Validation: Optimized hyperparameters, applied data augmentation, and ensured high accuracy in distinguishing between multiple cell types.
3. Domain Collaboration: Partnered with hematology experts to align performance metrics with clinical diagnostic requirements.
4. Evaluation & Reporting: Conducted rigorous testing and residual analysis; prepared technical documentation and visual reports for diverse stakeholders.
5. Healthcare Impact: Developed a deployable AI model supporting early detection of hematological conditions and potential integration into diagnostic workflows.

**Features & Highlights**

- Image preprocessing: resizing, normalization, augmentation  
- Detection & segmentation of WBCs in images  
- Classification of WBC subtypes (e.g. neutrophils, lymphocytes, monocytes, eosinophils, basophils)  
- Model evaluation with metrics: accuracy, precision, recall, F1-score  
- Visual output: annotated images with predicted class labels  

**Usage**

1. Clone this repository  
2. Place raw WBC images in `data/raw_images/`  
3. Open the notebooks in sequence:  
   - `WBC_detection_and_classification.ipynb` → detection and segmentation  
   - `WBC_Classification.ipynb` → train classification model and evaluate  
4. Run cells to preprocess images, train models, and produce annotated predictions  
5. Review outputs, evaluation metrics, and sample results in `images/`

**Tools & Libraries**

1. Python (TensorFlow / PyTorch / Keras, OpenCV, scikit-image, NumPy, etc.)
2. Jupyter Notebooks
3. GitHub version control  

**Insights & Outcomes**

- Segmented WBC regions accurately from microscope images  
- Classification accuracy, precision, recall, F1-score measured for each subtype  
- Visual outputs with bounding boxes / masks and class labels for test images  

**How to Contribute / Extend**

- Add more data and augment classes  
- Improve model architecture (e.g. deeper CNN, transfer learning)  
- Add cross-validation or ensembling  
- Deploy model via API or GUI  

**Version History**

See [`docs/version_log.md`](./docs/version_log.md) for change history and updates  


