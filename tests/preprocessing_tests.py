import pytest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

from toolbox.preprocessing import numerical_features

def test_numerical_features(df):
    df = pd.DataFrame({'number':[2,3,4,5,6], 'float':[1.1,1.2,1.3,1.4,1.5],
        'string':['a','b','c','d','e']})

    assert numerical_features(df) == ['number','float']

