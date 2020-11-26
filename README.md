[![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![made-with-Markdown](https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white)](http://commonmark.org)
[![GitHub license](https://img.shields.io/github/license/mohd-faizy/DataScience-Projects)](https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/mohd-faizy/DataScience-Projects)](https://github.com/mohd-faizy/DataScience-Projects/issues)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://opensource.com/resources/what-open-source)

<strong> 
    <h1 align='center'>Hyperparameter Tuning with Microsoft Neural Network Intelligence Toolkit</h1> 
</strong>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/Proj_img.png'></a>
</p>

When you hear the words **“automated machine learning”**, what comes to your mind first? For me, it’s usually **H2O.ai’s Driverless AI**, or **Google’s Cloud AutoML**. Microsoft has also released an **Open-source automated machine learning toolkit** on GitHub that helps a user perform neural architecture search and hyperparameter tuning. Microsoft is calling the toolkit ‘Neural Network Intelligence (NNI)’.

**The below diagram illustrates high-level Architecture of NNI**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/0_high-level%20architecture%20of%20NNI.png' width = 700 height = 400></a>
</p>

## Overview

- Neural Network Intelligence (NNI) is Microsoft’s open-source toolkit for automated machine learning.
- The tool dispatches and runs trial jobs generated by tuning algorithms to search the best neural architecture and/or hyper-parameters in different environments.
- It helps you perform ML tasks like hyperparameter tuning and neural architecture search.
- You need to have Python 3.5 or greater to use NNI

## Installation

### Prerequires

- Python 3.6 (or above) 64-bit. Anaconda or Miniconda is highly recommended to manage multiple Python environments on Windows.
- If it’s a newly installed Python environment, it needs to install Microsoft C++ Build Tools to support build NNI dependencies like `scikit-learn`.

```
pip install cython wheel
```

### Install NNI

- From pip package

```
python -m pip install --upgrade nni
```

- From source code

```
git clone -b v1.9 https://github.com/Microsoft/nni.git
cd nni
powershell -ExecutionPolicy Bypass -file install.ps1
```

## What is Hyperparameter Tuning?

### Hyperparameters

- **Hyperparameters** are parameters that control the model training process (e.g. **learning rate, batch size**) • **Hyperparameters** are not learned from the model training process itself

### Hyperparameter Tuning

- Finding hyperparameter values that **Optimize** one or more evaluation metrics (e.g. **Accuracy on a test set**).

### Neural Network Intelligence (NNI) Toolkit

Set of tools to manage automated machine learning experiments to perform:

- **Feature Engineering**
- **Hyperparameter Tuning**
- **Neural Architecture Search**
- **Model Compression**

### NNI supports:

- Most popular ML frameworks (**PyTorch, TensorFlow, MXNet** and more) • Local machines, remote servers, k8 clusters or cloud solutions.

### NNI has several appealing properties: ease-of-use, scalability, flexibility, and efficiency.

- **Ease-of-use:** NNI can be easily installed through python pip. Only several lines need to be added to your code in order to use NNI’s power. You can use both the commandline tool and WebUI to work with your experiments.

- **Scalability:** Tuning hyperparameters or the neural architecture often demands a large number of computational resources, while NNI is designed to fully leverage different computation resources, such as remote machines, training platforms (e.g., OpenPAI, Kubernetes). Hundreds of trials could run in parallel by depending on the capacity of your configured training platforms.

- **Flexibility:** Besides rich built-in algorithms, NNI allows users to customize various hyperparameter tuning algorithms, neural architecture search algorithms, early stopping algorithms, etc. Users can also extend NNI with more training platforms, such as virtual machines, kubernetes service on the cloud. Moreover, NNI can connect to external environments to tune special applications/models on them.

- **Efficiency:** We are intensively working on more efficient model tuning on both the system and algorithm level. For example, we leverage early feedback to speedup the tuning procedure.

### Creating the Hyper-parameter Experiment

- we first need the search space that describs the value range . we can use the `.json`

```json
{
  "dropout_rate": {
    "_type": "uniform",
    "_value": [0.1, 0.9]
  },

  "num_units": {
    "_type": "choice",
    "_value": [32, 64, 128, 256, 512]
  },

  "lr": {
    "_type": "choice",
    "_value": [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 0.01, 0.03, 0.06]
  },

  "batch_size": {
    "_type": "choice",
    "_value": [32, 64, 128, 256, 512, 1024]
  },

  "activation": {
    "_type": "choice",
    "_value": ["relu", "sigmoid"]
  }
}
```

```bash
nnictl create --config /content/config.yml
```

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/1.png'></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/2.png' width=750 height=500></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/3.png' width=750 height=400></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/4.png' width=750 height=400 ></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/5.png' width=750 height=400></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/6_Top100percent.png' width=750 height=400></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/7_Top50percent.png' width=750 height=500></a>
</p>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/8_Top20percent.png' width=750 height=400></a>
</p>

### Connect with me:

[<img align="left" alt="codeSTACKr | Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />][twitter]
[<img align="left" alt="codeSTACKr | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="codeSTACKr.com" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />][stackexchange ai]

[twitter]: https://twitter.com/F4izy
[linkedin]: https://www.linkedin.com/in/faizy-mohd-836573122/
[stackexchange ai]: https://ai.stackexchange.com/users/36737/cypher

---

![Faizy's github stats](https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=mohd-faizy&layout=compact)](https://github.com/mohd-faizy/github-readme-stats)
