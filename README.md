# 22610097_Yash-Potdar
TY BTech Practical Exam - Deep Learning and MLOps Laboratory
---
# How to use

1. First clone the repository using:
    ```bash
    git clone https://github.com/ty-prct-ai-ds/22610097_Yash-Potdar.git
    ```
2. Move to repo directory:
   ```bash
   cd 22610097_Yash-Potdar
   ```
3. Create a Python virtual environment:
    ```python
    python -m venv .venv
    #for windows
    .venv\Scripts\activate
    #for linux/mac os
    source .venv/Scripts/activate
4. To run DLL Code use the Jupyter Notebook and run all the cells
5. To run the MLOps Code run the python code using:
   ```bash
   python "22610097_Yash Potdar - MLOps.py"
   ```
6. To make changes and share to GitHub use the following commands:
   ```bash
   git add <filename>
   git commit -m "<msg>"
   git push origin <branch>
    ```
7. To use the model from pickle file use:
   ```python
    loaded_model = joblib.load(filename="model.pkl")
    y_pred = loaded_model.predict([<data>])
    print(f"{accuracy_score(pred, y_test)}")
    ```
