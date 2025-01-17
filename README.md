# Roboflow Python Library

---
![roboflow logo](https://i.imgur.com/lXCoVt5.png)

[Website](https://docs.roboflow.com/python) • [Docs](https://docs.roboflow.com/python) • [Blog](https://blog.roboflow.com)
• [Twitter](https://twitter.com/roboflow) • [Linkedin](https://www.linkedin.com/company/roboflow-ai)
• [Universe](https://universe.roboflow.com)

**Roboflow** makes managing, preprocessing, augmenting, and versioning datasets for computer vision seamless. This is
the official Roboflow python package that interfaces with the [Roboflow API](https://docs.roboflow.com). Key features of
Roboflow:

- Import and Export image datasets into any supported [formats](https://roboflow.com/formats)
- [Preprocess](https://docs.roboflow.com/image-transformations/image-preprocessing)
  and [augment](https://docs.roboflow.com/image-transformations/image-augmentation) data using Roboflow's dataset
  management tools
- Train computer vision models using [Roboflow Train](https://docs.roboflow.com/train) and deploy
  to [production](https://docs.roboflow.com/inference)
- Use [community curated projects](https://universe.roboflow.com/) to start building your own vision-powered products

## Installation:

To install this package, please use `Python 3.6` or higher. We provide three different ways to install the Roboflow
package to use within your own projects.

Install from PyPi (Recommended):

```
pip install roboflow
```

Install from Source:

```
git clone https://github.com/roboflow-ai/roboflow-python.git
cd roboflow-python
python3 -m venv env
source env/bin/activate 
pip3 install -r requirements.txt
```

## Quickstart

```python
import roboflow

# Instantiate Roboflow object with your API key
rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)

# List all projects for your workspace
workspace = rf.workspace()

# Load a certain project, workspace url is optional
project = rf.project("PROJECT_ID")

# List all versions of a specific project
project.versions()

# Upload image to dataset
project.upload("UPLOAD_IMAGE.jpg")

# Retrieve the model of a specific project
project.version("1").model

# predict on a local image
prediction = model.predict("YOUR_IMAGE.jpg")

# Predict on a hosted image
prediction = model.predict("YOUR_IMAGE.jpg", hosted=True)

# Plot the prediction
prediction.plot()

# Convert predictions to JSON
prediction.json()

# Save the prediction as an image
prediction.save(output_path='predictions.jpg')
```

## Using this package for a specifc project

If you have a specific project from your workspace you'd like to run in a notebook follow along on this tutorial [Downloading Datasets from Roboflow for Training (Python)](https://www.youtube.com/watch?v=76E6esnez8E)

Selecting the format you'd like your project to be exported as while choosing the `show download code` option will display code snippets you can use in either Jupyter or your terminal. These code snippets will include your `api_key`, project, and workspace names.

![Alt Text](https://media.giphy.com/media/I5g06mUnVzdX7iT2Gf/giphy.gif)
