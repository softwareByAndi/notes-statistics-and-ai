---
tags: 
links:
  - "[[Statistics]]"
---
see hypothesis testing section of [[statistics/lecture_notes.ipynb]] #TODO 

# exam notes 

- [[logistic regression]] = binary yes/no answers & [[Linear Regression]] = continuous (4.123) number answers

# steps
1. prelim checks
	1. check feature types
	2. check value counts for each feature & note low values or category mistakes
	3. convert categorical features to `category` type
	4. check which features have missing values
2. perform univariate analysis to look at patterns in data.
3. split data between input features and target features
	1. remove any features that won't be available during prediction time
4. impute missing values in input set
	1. median for continuous features 
	2. most frequent for categorical features
	3. etc...
5. split input data into training set and test set
6. check that no values are missing anymore
7. datatype conversions
	1. some categorical data was converted into floats... not sure why
	2. convert categorical features into dummies 
		1. `df = pd.get_dummies(df, columns=dummy_cols, drop_first=True`
8. define possible consequences of incorrect predictions
	1. consequence of false positive v.s. false negative
	2. which consequence is more important? -- i.e. which error to minimize.
		2. maximize recall or precision
9. build models
	1. in this example, 4 models were built:
		1. logistic regression
		2. support vector machine (SVM)
		3. decision tree
		4. random forest
10. tune models
	1. evaluate model recall v.s. precision
	2. 
# notebook code snippets
``` python
# Importing the basic libraries we will require for the project

# Libraries to help with reading and manipulating data
import pandas as pd
import numpy as np

# Libaries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Importing the Machine Learning models we require from Scikit-Learn
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# Importing the other functions we may require from Scikit-Learn
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

# To get diferent metric scores
from sklearn.metrics import confusion_matrix,classification_report,roc_auc_score,precision_recall_curve,roc_curve,make_scorer

# Code to ignore warnings from function usage
import warnings;
import numpy as np
warnings.filterwarnings('ignore')
```

``` python
# Separating target variable and other variables
Y=data['TARGET']
X=(
   data
   .drop(columns='TARGET')
   .drop(columns=[
	   'features',
	   'not available',
	   'at time of prediction'
	])
)

# Splitting the data into train and test sets
X_train,X_test,y_train,y_test = train_test_split(
	X,
	Y,
	test_size=0.30,
	random_state=1,
	stratify=Y # keep same ratios of TARGET categories when sampling 
)
```
- `SimpleImputer` can be used to easily impute values

### scoring function / classification report example
``` python
# Creating metric function 
def metrics_score(actual, predicted):
    print(classification_report(actual, predicted))

    cm = confusion_matrix(actual, predicted)
    plt.figure(figsize=(8,5))
    
    sns.heatmap(cm, annot=True,  fmt='.2f')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()
```

### see also:
```dataview
LIST FROM [[standard error]] SORT file.name ASC
```
