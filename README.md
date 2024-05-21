![author](https://img.shields.io/badge/author-mohd--faizy-red)
![made-with-Markdown](https://img.shields.io/badge/Made%20with-markdown-blue)
![Language](https://img.shields.io/github/languages/top/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)
![Platform](https://img.shields.io/badge/platform-Visual%20Studio%20Code-blue)
![Maintained](https://img.shields.io/maintenance/yes/2024)
![Last Commit](https://img.shields.io/github/last-commit/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)
[![GitHub issues](https://img.shields.io/github/issues/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)](https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/issues)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://opensource.com/resources/what-open-source)
![Stars GitHub](https://img.shields.io/github/stars/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)
[![GitHub license](https://img.shields.io/github/license/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)](https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/LICENSE)
![Size](https://img.shields.io/github/repo-size/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI)

---
<strong> 
    <h1 align='center'>Hyperparameter Tuning with Microsoft Neural Network Intelligence Toolkit</h1> 
</strong>

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/Proj_img.png'></a>
</p>

This repository demonstrates how to perform hyperparameter tuning using Microsoft’s NNI toolkit. NNI automates feature engineering, neural architecture search, hyperparameter tuning, and model compression for deep learning tasks.


**The below diagram illustrates high-level Architecture of NNI**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/0_high-level%20architecture%20of%20NNI.png' width = 700 height = 400></a>
</p>

## ➤ Prerequisites

- NNI requires `Python >= 3.7`. It is tested and supported on `Ubuntu >= 18.04`, `Windows 10 >= 21H2`, and `macOS >= 11`
- Pip (Python package manager)

## ➤ Setup Instructions

### 🟢 Create a Virtual Environment

1. Open your terminal or command prompt.
2. Clone the repository `git clone https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI.git`
`
3. Navigate to your project directory.
4. Run the following command to create a virtual environment (replace `<environment_name>` with your desired name):

   ```sh
   python -m venv venv
   ```

### 🟢 Activate the Virtual Environment

- On Windows:

   ```sh
   .\venv\Scripts\activate
   ```

- On macOS/Linux:

   ```sh
   source ./venv/bin/activate
   ```

### 🟢 Install Dependencies

```sh
pip install -r requirements.txt
```

## ➤ Run the Hyperparameter Tuning Experiment

1. Creating the Hyperparameter Search Space:
   1. In order to perform the hyper-parameter tunning, we first need to create the **search space** that describs the value range of each hyper-parameter.
   2. we can use the `.json` code to describe the range & this is the dictionary of all the hyper-parameter values that we want to run for our experiment.

`search_space.json`
```json
{
  "dropout_rate": {
    "_type": "uniform",
    "_value": [0.1, 0.9]
    },
  "num_units": {
    "_type": "choice",
    "_value": [ 32, 64, 128, 256, 512]
    },
  "lr": {
    "_type": "choice",
    "_value": [ 0.1, 0.01, 0.001, 0.03, 0.003, 0.06, 0.006]
    },
  "batch_size": {
    "_type": "choice",
    "_value": [ 16, 32, 64, 128, 256, 512]
    },
  "activation": {
    "_type": "choice",
    "_value": [ "relu", "sigmoid", "tanh"]
    }
}
```

2. Then we need to create another file called `config.yml` & which contain all the information regarding the configuration information of our experiment.
   
`config.yml`

```yml
experimentName: mnist
trialConcurrency: 1
maxExperimentDuration: 1h
maxTrialNumber: 10
searchSpaceFile: search_space.json
useAnnotation: false
trialCommand: python main.py
trialCodeDirectory: .
tuner:
  name: TPE
  classArgs:
    optimize_mode: maximize
trainingService:
  platform: local
```

3. Then at last we need to Execute the following command to start the NNI experiment:

   ```sh
   nnictl create --config config.yml    
   ```

## ➤ Monitor the Experiment

1. Open the NNI dashboard in your web browser (usually at <http://localhost:8080>).
   ```
   [2024-05-22 00:52:19] Web portal URLs: http://192.168.0.106:8080 http://172.25.208.1:8080 http://127.0.0.1:8080
   [2024-05-22 00:52:19] To stop experiment run "nnictl stop c8usp7bz" or "nnictl stop --all"
   [2024-05-22 00:52:19] Reference: <https://nni.readthedocs.io/en/stable/reference/nnictl.html>
   ```
2. Observe the trial jobs, intermediate results, and final results.




## 📄Launching the NNI Dashboard

### **Hyperparameter Visualization**
<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/1.png?raw=true'></a>
</p>

#### **Top 100% percent**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/2.png?raw=true'></a>
</p>

#### **Top 20% percent**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/3.png?raw=true'></a>
</p>

#### **Top 5% percent**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/4.png?raw=true'></a>
</p>

#### **Top 1% percent**

- ` default metric: 0.9793`

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/7.png?raw=true'></a>
</p>

#### **Duration**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/5.png?raw=true'></a>
</p>

#### **Intermediate result**

<p align='center'>
  <a href="#"><img src='https://github.com/mohd-faizy/Hyperparameter-Tuning-with-Microsoft-Network-Intelligence-Toolkit-NNI/blob/main/img_NNI/6.png?raw=true'></a>
</p>


## 🍰 Contributing

Contributions are welcome!

## ➤ Additional Resources

- 👉[NNI Documentation](https://nni.readthedocs.io/en/latest/index.html)
- 👉[NNI GitHub Repository](https://github.com/microsoft/nni)
- 👉[NNI Experiment Config Reference](https://nni.readthedocs.io/en/latest/reference/experiment_config.html)
- 👉[nnictl Commands](https://nni.readthedocs.io/en/latest/reference/nnictl.html)


## ⚖ ➤ License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## ❤️ Support

If you find this repository helpful, show your support by starring it! For questions or feedback, reach out on [Twitter(`X`)](https://twitter.com/F4izy).

#### $\color{skyblue}{\textbf{Connect with me:}}$

➤ If you have questions or feedback, feel free to reach out!!!

[<img align="left" src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/twitter_circle-512.png" width="32px"/>][twitter]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="32px"/>][linkedin]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/2626/2626299.png" width="32px"/>][Portfolio]

[Portfolio]: https://ai.stackexchange.com/users/36737/faizy?tab=profile

---

<img src="https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true" width=380px height=200px />

