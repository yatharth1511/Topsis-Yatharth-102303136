# TOPSIS- Yatharth- 102303136

This repository contains a complete implementation of the TOPSIS
(Technique for Order Preference by Similarity to Ideal Solution) method by **Yatharth Sharma** (Roll No.: 102303136)

The project includes:
- Full TOPSIS implementation in **R**
- A **Colab notebook** explaining methodology and results
- A **FastAPI backend**
- A **Streamlit frontend**
- Email delivery of results

---

## Methodology

TOPSIS ranks alternatives based on their distance from:
- Ideal best solution
- Ideal worst solution

Steps:
1. Normalize decision matrix
2. Apply weights
3. Identify ideal best and worst values
4. Compute separation measures (S⁺ and S⁻)
5. Calculate performance score
6. Rank alternatives
---

## R Implementation

The `R/topsis_full.R` file displays:
- Normalized matrix
- Weighted normalized matrix
- Ideal best & worst values
- S⁺ and S⁻
- Performance score
- Final rank
- Result graph

---

## Colab Notebook

The `notebook/TOPSIS_Assignment.ipynb` notebook:
- Explains methodology step by step
- Displays all intermediate matrices
- Shows result table and graph

---

## Images

### Normalized Decision Matrix
![Normalized Matrix](images/normalized_matrix.png)

### Weighted Normalized Matrix
![Weighted Matrix](images/weighted_matrix.png)

### Ideal Best and Ideal Worst Values
![Ideal Values](images/ideal_values.png)

### Separation Measures (S⁺ and S⁻)
![Separation Measures](images/separation_measures.png)

### Performance Scores and Ranking
![TOPSIS Scores](images/topsis_scores.png)

### Result Visualization Graph
![Result Graph](images/result_graph.png)

### Website UI
![Website UI](images/website_ui.png)

### Website Result
![Website Result](images/website_result.png)

## Web Service

### Frontend
- Streamlit (centrally aligned UI)
- Upload CSV
- Enter weights, impacts, email
- Display result table
- Download output.csv

### Backend
- FastAPI
- High performance
- Sends output.csv via email

---

## Publishing to PyPI

### Build
```bash
pip -m build
```
### Upload
```bash
python -m twine upload dist/*
```
### Test Installation
```bash
pip install Topsis-Yatharth-102303136
topsis-cli --help
```
## Author
### Yatharth Sharma, Roll No. 102303136 ###
