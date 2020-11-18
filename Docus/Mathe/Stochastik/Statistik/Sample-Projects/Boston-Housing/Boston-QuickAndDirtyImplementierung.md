<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Algemeines-Vorgehen-SK-Learn">Algemeines Vorgehen SK-Learn<a class="anchor-link" href="#Algemeines-Vorgehen-SK-Learn">&#182;</a></h2><ol>
<li><a href="https://github.com/JHC90/Basic-DataScience-Skills/wiki/EDA_Landingpage">EDA</a><br>
Aus der EDA lese ich unter anderem ab, was im Data-Preprocessing bzw Feature Engineering zu tun ist.</li>
<li>[Data-Preprocessing] // entfällt hier. Der DS ist etwas wie Hello-World =&gt; easy zu implemeniteren, kein Fokus auf Preprocessing</li>
<li><a href="./Literatur_Quellen/1_UDC/original/Python-DataScience-MachineLearning-v10/5-Machine%20Learning/1-Linear%20Regression/1-Lineare%20Regression%20Mit%20Python.ipynb">Modellierung Regression (SK-Learn), Predicten, MSE, MAE, RMSE</a></li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[160]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[93]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.datasets</span> <span class="kn">import</span> <span class="n">load_boston</span>
<span class="n">boston</span> <span class="o">=</span> <span class="n">load_boston</span><span class="p">()</span>
<span class="n">boston_df</span> <span class="o">=</span> <span class="n">boston</span><span class="o">.</span><span class="n">data</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[94]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">boston</span><span class="o">.</span><span class="n">DESCR</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>.. _boston_dataset:

Boston house prices dataset
---------------------------

**Data Set Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000&#39;s

    :Missing Attribute Values: None

    :Creator: Harrison, D. and Rubinfeld, D.L.

This is a copy of UCI ML housing dataset.
https://archive.ics.uci.edu/ml/machine-learning-databases/housing/


This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.

The Boston house-price data of Harrison, D. and Rubinfeld, D.L. &#39;Hedonic
prices and the demand for clean air&#39;, J. Environ. Economics &amp; Management,
vol.5, 81-102, 1978.   Used in Belsley, Kuh &amp; Welsch, &#39;Regression diagnostics
...&#39;, Wiley, 1980.   N.B. Various transformations are used in the table on
pages 244-261 of the latter.

The Boston house-price data has been used in many machine learning papers that address regression
problems.   
     
.. topic:: References

   - Belsley, Kuh &amp; Welsch, &#39;Regression diagnostics: Identifying Influential Data and Sources of Collinearity&#39;, Wiley, 1980. 244-261.
   - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[74]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">boston_df</span><span class="p">))</span> <span class="c1"># =&gt; umwandeln in Pandas</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;numpy.ndarray&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">colnames</span> <span class="o">=</span> <span class="p">(</span><span class="n">boston</span><span class="o">.</span><span class="n">feature_names</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[76]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span>  <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">boston_df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[77]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># umwandeln in Pandasdf</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">colnames</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">boston_df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[78]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">tail</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(506, 13)
      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \
0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   
1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   
2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   
3  0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0   
4  0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0   

   PTRATIO       B  LSTAT  
0     15.3  396.90   4.98  
1     17.8  396.90   9.14  
2     17.8  392.83   4.03  
3     18.7  394.63   2.94  
4     18.7  396.90   5.33  
        CRIM   ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \
501  0.06263  0.0  11.93   0.0  0.573  6.593  69.1  2.4786  1.0  273.0   
502  0.04527  0.0  11.93   0.0  0.573  6.120  76.7  2.2875  1.0  273.0   
503  0.06076  0.0  11.93   0.0  0.573  6.976  91.0  2.1675  1.0  273.0   
504  0.10959  0.0  11.93   0.0  0.573  6.794  89.3  2.3889  1.0  273.0   
505  0.04741  0.0  11.93   0.0  0.573  6.030  80.8  2.5050  1.0  273.0   

     PTRATIO       B  LSTAT  
501     21.0  391.99   9.67  
502     21.0  396.90   9.08  
503     21.0  396.90   5.64  
504     21.0  393.45   6.48  
505     21.0  396.90   7.88  
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[79]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span>
<span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span>
<span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[79]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>False</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[80]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 506 entries, 0 to 505
Data columns (total 13 columns):
CRIM       506 non-null float64
ZN         506 non-null float64
INDUS      506 non-null float64
CHAS       506 non-null float64
NOX        506 non-null float64
RM         506 non-null float64
AGE        506 non-null float64
DIS        506 non-null float64
RAD        506 non-null float64
TAX        506 non-null float64
PTRATIO    506 non-null float64
B          506 non-null float64
LSTAT      506 non-null float64
dtypes: float64(13)
memory usage: 51.5 KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[81]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[81]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody123 tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody123 tr th {
        vertical-align: top;
    }

    .dataframe thead123 th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead123>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>count</th>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
      <td>506.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.613524</td>
      <td>11.363636</td>
      <td>11.136779</td>
      <td>0.069170</td>
      <td>0.554695</td>
      <td>6.284634</td>
      <td>68.574901</td>
      <td>3.795043</td>
      <td>9.549407</td>
      <td>408.237154</td>
      <td>18.455534</td>
      <td>356.674032</td>
      <td>12.653063</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.601545</td>
      <td>23.322453</td>
      <td>6.860353</td>
      <td>0.253994</td>
      <td>0.115878</td>
      <td>0.702617</td>
      <td>28.148861</td>
      <td>2.105710</td>
      <td>8.707259</td>
      <td>168.537116</td>
      <td>2.164946</td>
      <td>91.294864</td>
      <td>7.141062</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.006320</td>
      <td>0.000000</td>
      <td>0.460000</td>
      <td>0.000000</td>
      <td>0.385000</td>
      <td>3.561000</td>
      <td>2.900000</td>
      <td>1.129600</td>
      <td>1.000000</td>
      <td>187.000000</td>
      <td>12.600000</td>
      <td>0.320000</td>
      <td>1.730000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.082045</td>
      <td>0.000000</td>
      <td>5.190000</td>
      <td>0.000000</td>
      <td>0.449000</td>
      <td>5.885500</td>
      <td>45.025000</td>
      <td>2.100175</td>
      <td>4.000000</td>
      <td>279.000000</td>
      <td>17.400000</td>
      <td>375.377500</td>
      <td>6.950000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.256510</td>
      <td>0.000000</td>
      <td>9.690000</td>
      <td>0.000000</td>
      <td>0.538000</td>
      <td>6.208500</td>
      <td>77.500000</td>
      <td>3.207450</td>
      <td>5.000000</td>
      <td>330.000000</td>
      <td>19.050000</td>
      <td>391.440000</td>
      <td>11.360000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.677083</td>
      <td>12.500000</td>
      <td>18.100000</td>
      <td>0.000000</td>
      <td>0.624000</td>
      <td>6.623500</td>
      <td>94.075000</td>
      <td>5.188425</td>
      <td>24.000000</td>
      <td>666.000000</td>
      <td>20.200000</td>
      <td>396.225000</td>
      <td>16.955000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>88.976200</td>
      <td>100.000000</td>
      <td>27.740000</td>
      <td>1.000000</td>
      <td>0.871000</td>
      <td>8.780000</td>
      <td>100.000000</td>
      <td>12.126500</td>
      <td>24.000000</td>
      <td>711.000000</td>
      <td>22.000000</td>
      <td>396.900000</td>
      <td>37.970000</td>
    </tr>
  </tbody123>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[82]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Visualisierungen</span>
<span class="n">sns</span><span class="o">.</span><span class="n">pairplot</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[82]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;seaborn.axisgrid.PairGrid at 0x182b5216ef0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[83]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[83]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody123 tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody123 tr th {
        vertical-align: top;
    }

    .dataframe thead123 th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead123>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>501</th>
      <td>0.06263</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.593</td>
      <td>69.1</td>
      <td>2.4786</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>391.99</td>
      <td>9.67</td>
    </tr>
    <tr>
      <th>502</th>
      <td>0.04527</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.120</td>
      <td>76.7</td>
      <td>2.2875</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>9.08</td>
    </tr>
    <tr>
      <th>503</th>
      <td>0.06076</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.976</td>
      <td>91.0</td>
      <td>2.1675</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>5.64</td>
    </tr>
    <tr>
      <th>504</th>
      <td>0.10959</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.794</td>
      <td>89.3</td>
      <td>2.3889</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>393.45</td>
      <td>6.48</td>
    </tr>
    <tr>
      <th>505</th>
      <td>0.04741</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.030</td>
      <td>80.8</td>
      <td>2.5050</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>7.88</td>
    </tr>
  </tbody123>
</table>
<p>506 rows × 13 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[85]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">colNames</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[85]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;CRIM&#39;,
 &#39;ZN&#39;,
 &#39;INDUS&#39;,
 &#39;CHAS&#39;,
 &#39;NOX&#39;,
 &#39;RM&#39;,
 &#39;AGE&#39;,
 &#39;DIS&#39;,
 &#39;RAD&#39;,
 &#39;TAX&#39;,
 &#39;PTRATIO&#39;,
 &#39;B&#39;,
 &#39;LSTAT&#39;,
 &#39;MEDV&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[90]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;CRIM&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[90]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x182c00ea3c8&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[91]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># hier würde ich normalerweise zuerst eine PCA-machen um den Feature raum runterzuskalieren</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[92]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">corr</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[92]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x182c00df048&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Data-Split">Data Split<a class="anchor-link" href="#Data-Split">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[115]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">y</span> <span class="o">=</span> <span class="p">(</span><span class="n">boston</span><span class="o">.</span><span class="n">target</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">[[</span><span class="s1">&#39;Price&#39;</span><span class="p">]],</span> <span class="n">data</span> <span class="o">=</span> <span class="n">y</span><span class="p">)</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">colnames</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">boston_df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[116]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">X</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(506, 1)
(506, 13)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[117]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Split Train test</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.4</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">101</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Lineare-Regression">Lineare Regression<a class="anchor-link" href="#Lineare-Regression">&#182;</a></h1><h2 id="OLS">OLS<a class="anchor-link" href="#OLS">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[120]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>
<span class="n">lm</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">lm</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span><span class="n">y_train</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[120]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Achsenabschnitt ausgeben</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lm</span><span class="o">.</span><span class="n">intercept_</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[41.28149654]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[147]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">lm</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">lm</span><span class="o">.</span><span class="n">coef_</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">X</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[-7.75583711e-02  4.20310157e-02  9.11529473e-02  4.13304932e+00
  -1.99765575e+01  2.89019042e+00  1.61533256e-02 -1.26474745e+00
   2.60170760e-01 -1.11251993e-02 -8.80555502e-01  7.02445445e-03
  -6.43482813e-01]]
&lt;class &#39;numpy.ndarray&#39;&gt;
Index([&#39;CRIM&#39;, &#39;ZN&#39;, &#39;INDUS&#39;, &#39;CHAS&#39;, &#39;NOX&#39;, &#39;RM&#39;, &#39;AGE&#39;, &#39;DIS&#39;, &#39;RAD&#39;, &#39;TAX&#39;,
       &#39;PTRATIO&#39;, &#39;B&#39;, &#39;LSTAT&#39;],
      dtype=&#39;object&#39;)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[155]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># umwandeln in Pandasdf</span>
<span class="n">dfCoef</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">colnames</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">lm</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>
<span class="n">dfCoef</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[155]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody123 tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody123 tr th {
        vertical-align: top;
    }

    .dataframe thead123 th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead123>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>-0.077558</td>
      <td>0.042031</td>
      <td>0.091153</td>
      <td>4.133049</td>
      <td>-19.976557</td>
      <td>2.89019</td>
      <td>0.016153</td>
      <td>-1.264747</td>
      <td>0.260171</td>
      <td>-0.011125</td>
      <td>-0.880556</td>
      <td>0.007024</td>
      <td>-0.643483</td>
    </tr>
  </tbody123>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[166]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_t</span> <span class="o">=</span> <span class="n">dfCoef</span><span class="o">.</span><span class="n">T</span>
<span class="n">df_t</span><span class="o">.</span><span class="n">colu</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[166]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody123 tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody123 tr th {
        vertical-align: top;
    }

    .dataframe thead123 th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead123>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>CRIM</th>
      <td>-0.077558</td>
    </tr>
    <tr>
      <th>ZN</th>
      <td>0.042031</td>
    </tr>
    <tr>
      <th>INDUS</th>
      <td>0.091153</td>
    </tr>
    <tr>
      <th>CHAS</th>
      <td>4.133049</td>
    </tr>
    <tr>
      <th>NOX</th>
      <td>-19.976557</td>
    </tr>
    <tr>
      <th>RM</th>
      <td>2.890190</td>
    </tr>
    <tr>
      <th>AGE</th>
      <td>0.016153</td>
    </tr>
    <tr>
      <th>DIS</th>
      <td>-1.264747</td>
    </tr>
    <tr>
      <th>RAD</th>
      <td>0.260171</td>
    </tr>
    <tr>
      <th>TAX</th>
      <td>-0.011125</td>
    </tr>
    <tr>
      <th>PTRATIO</th>
      <td>-0.880556</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.007024</td>
    </tr>
    <tr>
      <th>LSTAT</th>
      <td>-0.643483</td>
    </tr>
  </tbody123>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Predictions">Predictions<a class="anchor-link" href="#Predictions">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[161]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">lm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[162]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="n">predictions</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[162]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x182c25904e0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[163]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">((</span><span class="n">y_test</span><span class="o">-</span><span class="n">predictions</span><span class="p">),</span><span class="n">bins</span><span class="o">=</span><span class="mi">50</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[164]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">metrics</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;MAE:&#39;</span><span class="p">,</span> <span class="n">metrics</span><span class="o">.</span><span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;MSE:&#39;</span><span class="p">,</span> <span class="n">metrics</span><span class="o">.</span><span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;RMSE:&#39;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">metrics</span><span class="o">.</span><span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MAE: 3.9051448026275213
MSE: 29.416365467453012
RMSE: 5.423685598138318
</pre>
</div>
</div>

</div>
</div>

</div>
 
