# Project Name

# **Establishing bioinformatic benchmarks for in vitro engineered thymus from human pluripotent stem cells**

## Table of Contents
- Description
- Features
- Usage
- FAQ
- Contacts

## Description
Advancements in regenerative medicine have facilitated the development of fully human artificial thymic organoids (ATO) derived from human pluripotent stem cells (hPSCs) *in vitro*. Here we present a comprehensive bioinformatic framework for characterizing the engineered thymic tissue. The computational analyses employed include Gene Set Enrichment Analysis (GSEA), Principal Component Analysis (PCA), and Transcription Factor Network (TFN) analysis. These techniques are applied to evaluate the transcriptional profile of the ATO, comparing it to its native counterpart. Our results demonstrate that while GSEA had limited benefit, it still provides insights in the analysis of apoptosis over time, indicating that the neural crest cells (NCC) and hPSC-hNCC-derived mesenchyme (NCC-M) are generally enhancing cell survival. Additionally, PCA reveals that our thymic epithelial progenitor cells (TEPC) are progressing along a trajectory towards primary thymic epithelial cells (TEC), and that our NCC and NCC-M samples are transitioning towards the primary mesenchyme over time. TFN analysis uncovers underlying molecular mechanisms governing cell identities. Our discoveries emphasize the distinct benefits and drawbacks of each methodology, and all three approaches contribute to different aspects of guiding the tissue engineering process, addressing questions about long-term survival, lineage commitment, and the fundamental cellular identity. These integrated methods not only enhance our comprehension of thymic tissue dynamics, but also hold potential for broader applications in tissue engineering and regenerative medicine.

## Features
- Differential Expression Analysis (DEA) - statistical method used in genomics and bioinformatics to identify genes that show significant differences in expression levels between different experimental conditions. DEA is crucial for understanding which genes are potentially associated with specific biological processes or conditions

## Usage
A distinct Jupyter Lab Notebook with detailed and annotated code is included for each of the features:

- DEA  

<span style="color: blue;"><strong>Leiden Clustering</strong></span>

![Alt text](image-1.png)
![Alt text](image.png)

<span style="color: blue;"><strong>DEG</strong></span>  

![Alt text](image-2.png)
![Alt text](image-3.png)

## FAQ
- **How do I run the Jupyter Lab Notebooks?**  

To run the Jupyter Lab Notebooks, follow these steps:  

1. Install Jupyter Lab: If you haven't already, install Jupyter Lab by following the official installation instructions provided on the Jupyter website.

2. Clone the Repository: Clone the project repository to your local machine using a Git client or by downloading the ZIP file from the repository's GitHub page.

3. Navigate to the Directory: Using your preferred file explorer or command line interface, navigate to the directory where you've cloned or downloaded the repository.

4. Launch Jupyter Lab: Open a command prompt or terminal window and enter the following command:
```
jupyter lab
```
or
```
python -m jupyter lab
```
This will start the Jupyter Lab environment in your default web browser.

1. Access the Notebooks: In the Jupyter Lab interface, navigate to the directory containing the provided Jupyter Lab Notebooks. You should see a list of notebook files with the .ipynb extension.

2. Select and Run a Notebook: Click on the desired notebook file to open it. You can now read through the code, run individual cells, or execute the entire notebook by using the "Run" button or keyboard shortcut.

Note: Update the file paths in the config.csv file with your own.

- **What are the system requirements?**

All statistical computations were conducted using Python (v3.11.0) in conjunction with JupyterLab Notebooks (v 1.0.0)

- **How do I report a bug or issue?**

If you need further assistance or have specific inquiries, feel free to reach out to us using the contact information provided below. We're here to help and welcome your feedback!

## Contacts
- Mladenova, Tsvetelina <tsvetelina.mladenova@wyss.harvard.edu>