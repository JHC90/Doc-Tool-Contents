<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Chrun-Example">Chrun-Example<a class="anchor-link" href="#Chrun-Example">&#182;</a></h1><p><a href="https://towardsdatascience.com/churn-prediction-770d6cb582a5">https://towardsdatascience.com/churn-prediction-770d6cb582a5</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>hier geht es darum vorherzusagen ob ein Kunde das Unternehmen verlässt oder nicht. Es ist ein Supvised Problem. Der datensatz kommt von hier: "<a href="https://www.kaggle.com/blastchar/telco-customer-churn">https://www.kaggle.com/blastchar/telco-customer-churn</a>"</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bibliotheken</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/WA_Fn-UseC_-Telco-Customer-Churn.csv&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">how</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">)</span> <span class="c1"># remove samples with all missing values</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="o">~</span><span class="n">df</span><span class="o">.</span><span class="n">duplicated</span><span class="p">()]</span> <span class="c1"># remove duplicates</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(7043, 21)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">total_charges_filter</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">TotalCharges</span> <span class="o">==</span> <span class="s2">&quot; &quot;</span> <span class="c1"># würde mir das subsetz geben wo &quot; &quot; in dem Feature &quot;TotalCharges&quot; ist</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="o">~</span><span class="n">total_charges_filter</span><span class="p">]</span> <span class="c1"># = altes df ohne die vorher detektierten Leerwerte</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="o">~</span><span class="n">total_charges_filter</span><span class="p">]</span>
<span class="n">df</span><span class="o">.</span><span class="n">TotalCharges</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_numeric</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">TotalCharges</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">total_charges_filter</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(7032, 21)
(7043,)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\ipykernel_launcher.py:1: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
  &#34;&#34;&#34;Entry point for launching an IPython kernel.
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Exploratory-Data-Analysis">Exploratory Data Analysis<a class="anchor-link" href="#Exploratory-Data-Analysis">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Index([&#39;customerID&#39;, &#39;gender&#39;, &#39;SeniorCitizen&#39;, &#39;Partner&#39;, &#39;Dependents&#39;,
       &#39;tenure&#39;, &#39;PhoneService&#39;, &#39;MultipleLines&#39;, &#39;InternetService&#39;,
       &#39;OnlineSecurity&#39;, &#39;OnlineBackup&#39;, &#39;DeviceProtection&#39;, &#39;TechSupport&#39;,
       &#39;StreamingTV&#39;, &#39;StreamingMovies&#39;, &#39;Contract&#39;, &#39;PaperlessBilling&#39;,
       &#39;PaymentMethod&#39;, &#39;MonthlyCharges&#39;, &#39;TotalCharges&#39;, &#39;Churn&#39;],
      dtype=&#39;object&#39;)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">())</span>
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
Int64Index: 7032 entries, 0 to 7042
Data columns (total 21 columns):
customerID          7032 non-null object
gender              7032 non-null object
SeniorCitizen       7032 non-null int64
Partner             7032 non-null object
Dependents          7032 non-null object
tenure              7032 non-null int64
PhoneService        7032 non-null object
MultipleLines       7032 non-null object
InternetService     7032 non-null object
OnlineSecurity      7032 non-null object
OnlineBackup        7032 non-null object
DeviceProtection    7032 non-null object
TechSupport         7032 non-null object
StreamingTV         7032 non-null object
StreamingMovies     7032 non-null object
Contract            7032 non-null object
PaperlessBilling    7032 non-null object
PaymentMethod       7032 non-null object
MonthlyCharges      7032 non-null float64
TotalCharges        7032 non-null float64
Churn               7032 non-null object
dtypes: float64(2), int64(2), object(17)
memory usage: 1.2+ MB
None
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>       SeniorCitizen       tenure  MonthlyCharges  TotalCharges
count    7032.000000  7032.000000     7032.000000   7032.000000
mean        0.162400    32.421786       64.798208   2283.300441
std         0.368844    24.545260       30.085974   2266.771362
min         0.000000     1.000000       18.250000     18.800000
25%         0.000000     9.000000       35.587500    401.450000
50%         0.000000    29.000000       70.350000   1397.475000
75%         0.000000    55.000000       89.862500   3794.737500
max         1.000000    72.000000      118.750000   8684.800000
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(7032, 21)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Split-in-Datentypen">Split in Datentypen<a class="anchor-link" href="#Split-in-Datentypen">&#182;</a></h1><p>hab ich hier laut tutorial übernommen, kann man besser lösen indem ich das hier mache " <a href="https://github.com/JHC90/Basic-DataScience-Skills/blob/master/1_SplitDataByDataType.ipynb">https://github.com/JHC90/Basic-DataScience-Skills/blob/master/1_SplitDataByDataType.ipynb</a> "</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">categorical_features</span> <span class="o">=</span> <span class="p">[</span>
 <span class="s2">&quot;gender&quot;</span><span class="p">,</span>
 <span class="s2">&quot;SeniorCitizen&quot;</span><span class="p">,</span>
 <span class="s2">&quot;Partner&quot;</span><span class="p">,</span>
 <span class="s2">&quot;Dependents&quot;</span><span class="p">,</span>
 <span class="s2">&quot;PhoneService&quot;</span><span class="p">,</span>
 <span class="s2">&quot;MultipleLines&quot;</span><span class="p">,</span>
 <span class="s2">&quot;InternetService&quot;</span><span class="p">,</span>
 <span class="s2">&quot;OnlineSecurity&quot;</span><span class="p">,</span>
 <span class="s2">&quot;OnlineBackup&quot;</span><span class="p">,</span>
 <span class="s2">&quot;DeviceProtection&quot;</span><span class="p">,</span>
 <span class="s2">&quot;TechSupport&quot;</span><span class="p">,</span>
 <span class="s2">&quot;StreamingTV&quot;</span><span class="p">,</span>
 <span class="s2">&quot;StreamingMovies&quot;</span><span class="p">,</span>
 <span class="s2">&quot;Contract&quot;</span><span class="p">,</span>
 <span class="s2">&quot;PaperlessBilling&quot;</span><span class="p">,</span>
 <span class="s2">&quot;PaymentMethod&quot;</span><span class="p">,</span>
<span class="p">]</span>
<span class="n">numerical_features</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;tenure&quot;</span><span class="p">,</span> <span class="s2">&quot;MonthlyCharges&quot;</span><span class="p">,</span> <span class="s2">&quot;TotalCharges&quot;</span><span class="p">]</span>
<span class="n">target</span> <span class="o">=</span> <span class="s2">&quot;Churn&quot;</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="n">numerical_features</span><span class="p">]</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>



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
      <th>tenure</th>
      <th>MonthlyCharges</th>
      <th>TotalCharges</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>count</th>
      <td>7032.000000</td>
      <td>7032.000000</td>
      <td>7032.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>32.421786</td>
      <td>64.798208</td>
      <td>2283.300441</td>
    </tr>
    <tr>
      <th>std</th>
      <td>24.545260</td>
      <td>30.085974</td>
      <td>2266.771362</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>18.250000</td>
      <td>18.800000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>9.000000</td>
      <td>35.587500</td>
      <td>401.450000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>29.000000</td>
      <td>70.350000</td>
      <td>1397.475000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>55.000000</td>
      <td>89.862500</td>
      <td>3794.737500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>72.000000</td>
      <td>118.750000</td>
      <td>8684.800000</td>
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
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Numerical EDA</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="n">numerical_features</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">bins</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[27]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A3009F6668&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A300A6A7F0&gt;],
       [&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A300A9CD68&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A300ADA358&gt;]],
      dtype=object)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlwAAAGrCAYAAAAVY0mMAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nO3de5hlVX3n//dH8IK2CIhWkCY2zhAToCORHqIxY5qgEa/oMyGDQQXFkOSHETOd0UbziyZOzzCJmBiNJq0YUdBOBzUQBZWQVBwzAgE1aS4SGmmxoaW9ANJo0Mbv/LF3yemiqrqqTu1Tp06/X89Tzzl77cv6rtNVq7977bX3SVUhSZKk7jxksQOQJEkadSZckiRJHTPhkiRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy7NS5JK8h+nWXdqks8tUD1vSXL+QhxLkhZKkke0/eDyWW5/fJLNXcel4WXCNQKSbEny/SQHTir/UtshrOjz+ONJXt3PMXZz/F9NcnWSHUm2Jbk0yc93VZ+k0dT2IRM/P0zyvZ7lk3ezb98JUZKfS/KZJHcn+VaSK3ZXr/YcJlyj4xbgpRMLSVYC+yxeOLOT5L8BfwL8T2AM+HHg3cAJHdS190IfU9LwqKplEz/ArcALe8ou6LLuJKuBzwCfAg4FDgReCzy/g7rsy5YgE67R8SHgFT3LpwAfnFhI8pgkH0zyjSRfTfK7SR7Srjs1yeeSvC3JnUluSfLcdt064D8D72rPEt/VU8ezktzU7vNnSTI5qLb8nEllf5vkdUkeA/wBcEZVfayq7q2qH1TV31bVf+/Z5WFt7PckuS7Jqp5jrU1yc7vu+iQv6Vl3apJ/SvLHSb4NvCXJXknOSfLNtp2vaUcB9+75nM5tR9puS/I/kuzVrvuPSf6xPXv9ZpK/mts/kaTFlGSftk/almRrkj9K8tAkjwU+DjypZ0TssUmekeTK9m/+9rYvmS7ZeRvwF1X19qr6djWuqqpfnRTDG9t++Lbe0a8kL0nyL0m+0/bRb+xZ95NJdib5tSRfAy5py1+d5Nb2eK9P8vWJqwNtX/f/J/lK219dkGS/dt2jkmxI8u0kd7Vt3H9BP2w9iAnX6LgC2DfJT7UJwn8Feuc+vRN4DPAk4BdokrNX9qz/WeBGmrOyPwTOTZKqehPwf4DXtGeJr+nZ5wXAfwKeAvwK8Jwp4joPeGlPcncgcBzwEeDpwCNoOrqZvAjYAOwHXAz0Jn030ySEjwF+Hzg/yUGT2vUV4PHAOuDXgOcCRwFPBV48Rbw7gf8I/AzwS8DE5dS30pzB7g8sp/lMJS0dvw/8NLASOBpYDby+qr4FvAT4Ss+I2LeAHwCvAQ6g6WdeyAP9wY+0iczRwIW7qf+JQIAntMf98yTL2nXfAX6Vpp97CfA7SY7v2Xcvmv7sycAJSY4C3k7T9y5vf3qnlfx3mv7r59t1PwD+uF33amBv4OB2n9cA399N7OqTCddomRjlejbwZeC2tnwiATurqu6pqi3AOcDLe/b9alW9t6rup0k6DqK5xDeTs6vqrqq6FfgHmiRmF1V1FXA3TZIFcBIwXlV3AI8FvllVO3dTz+eq6pI2tg/RJHgTx//rqrq9qn5YVX8F3AQc07Pv7VX1zqraWVXfo+mc3lFVW6vqTuDsiQ2TjNEkY69rR9u203RQJ7Wb/ICmw3xCVf17VS3IjQGSBuZk4M1V9c22D/of7NoP7qIdofrnqrq/qm4G3kdzwjrZY9vXbbup/7vA/2pH8j8OFM3JHVV1eVVd1/ZlXwA2TlHX71XVd3v6so9W1RVVdR/wu+z6f/qvA2vb/vHfaZLN/9peifgB8DjgP7R94z9X1b27iV19MuEaLR+iOUM6lZ7LiTRnMA8DvtpT9lWas5sJX594U1Xfbd8uY2Zf73n/3Rm2Pw94Wfv+ZW2cAN8CDpzFfITJ9Tyi5xLgK9LcHHBXkruAI9n1LO9rk471hEllve+fCDwU2NZzvL+gGR0DeD3N2elV7aXNV+0mbklDok00foyZ+8HJ+xye5iaeO5J8B/g9du1fJnyrfT1oinW9vlFVP+xZ/lG/2V6+/Mf28uDdNP14b10/rKrbe5Z36cuq6js0J7cTbT0EuKSnL/sizf/5jwXOBf4RuLC9tPo/J6ZOqDsmXCOkqr5KM3n+ecDHelZ9kwdGZyb8OA+MgO320H2Gdj7NEPhTgJ8C/qYt/zzw7zz4st6sJHki8F6a4fDHVtV+wLU0SdGEybFvoxlen3BIz/uvAfcBB1bVfu3PvlV1BEBVfb2qfq2qnkBz9vjuTPNoDEnDpaqK5uRtun5wqn7uvcAXaEaC9qWZc/qguapVdRdwDfBf+ghxI/BXwCFV9RjgA8yhL0uyL83Uiom23gb8Yk9ftl9VPaId3buvqn6vqn4SeCZwIg+M5KsjJlyj5zSaP7Le4eH7af6Y1yV5dJuo/Dd2neM1kzto5n7NS1VtBf6ZZmTro+1wOFV1N80Z458leXGSR7YTWJ+b5A9ncehH0XRC3wBI8kqaEa6ZbATOTHJwO+/iDT1xbqOZo3VOkn2TPCTJf0jyC+3xT8wDz9y5s637/ll9CJKGwUeAN7cT4h8PvIkH+sE7gMf3zKkCeDRwd1XtSHIEzRzQ6fwO8Btpbgg6II2jM4vnCLYjUsuAb1XVvyf5OZokaCYbgf+S5D8leRhNMtg7evbnwNlJDmnreHySF7bvn9WO3j2EZu7YTuzLOmfCNWKq6uaqunqKVb8F3EszgfxzwIeB98/ysO8AfjnN3Yh/Os/QzqOZqPqh3sKqejtN8ve7NInT12hGrP5m8gEmq6rraeaifZ6ms1wJ/NNudnsvTVL1rzRD7Jewa2fzCprLr9fTJFUX8sBlgv8EXJlkB83k/TOr6pbdxSlpaPwezd/2dcCXaPqLiZO7f6H5u/5qexnuAOC3gVe3f/N/RjMCNaWqGqeZpP48YAvNlYV3AZ/cXVDtiNRvAG9Lcg/N9IW/3s0+X6SZGP9xmtGsbTSXFO9rN/lD4O+Av2+P+X9pbhSC5jLqRcA9NFcFLqFJ4NShNP/OUreSPJPmTHLFpDkMiyrN4y/+vKqeuNuNJWlItY91+DbNTT27m7yvReAIlzqX5KHAmcD7FjvZSvMcnucl2TvJwcCb2f1jKSRp6CR5UdunLaN5RMSVJlvDy4RLnUryU8BdNJfl/mSRw4FmEurv01wu/CJwA81lBklaak6kuRFgK81lQr9GaIh5SVGSJKljjnBJkiR1bOi/APPAAw+sFStWzGvfe++9l0c96lELG1BHllKsYLxdG7V4r7nmmm9W1eMGGNKSM5e+bqn9fsxkVNoyKu0A29Kv6fq7oU+4VqxYwdVXT/WUg90bHx9n9erVCxtQR5ZSrGC8XRu1eJN8ddqVAubW1y2134+ZjEpbRqUdYFv6NV1/t9tLiknen2R7kmt7yv4oyZeT/GuSj098A3m77qwkm5PcmOQ5PeVHJ9nUrvvT9kFvkiRJI282c7g+ABw/qewy4Miq+mng34CzoPneKZqvBzii3efdPd/P9B7gdOCw9mfyMSVJkkbSbhOuqvoszcPUess+U1U728UreOD7nE4ANrTf03QLsBk4JslBwL5V9fn2ibofZJ7fnydJkrTULMQcrlfxwNcdHEyTgE2YeDbID9r3k8unlOR0mtEwxsbGGB8fn1dgO3bsmPe+g7aUYgXj7ZrxStJo6SvhSvImmu+hu2CiaIrNaobyKVXVemA9wKpVq2q+E96W0sS/pRQrGG/XjFeSRsu8E64kpwAvAI6rB56euhU4pGez5cDtbfnyKcolSZJG3rwSriTHA28AfqGqvtuz6mLgw0neDjyBZnL8VVV1f5J7kjwNuBJ4BfDO/kJ/sBVrd/1S9jUrd3JqW7bl7OcvdHWSRkyS99OcSG6vqiPbsrcAvwZ8o93sjVV1SbvuLOA04H7gtVX16bb8aJobjvYBLgHOrAX8Wo9Nt939o75tMvs6aTjN5rEQHwE+Dzw5ydYkpwHvAh4NXJbkS0n+HKCqrgM2AtcDnwLOqKr720P9JvA+mon0NwOXLnRjJKlPH2DqO6j/uKqOan8mki3vypY0a7sd4aqql05RfO4M268D1k1RfjVw5Jyik6QBqqrPJlkxy81/dFc2cEuSibuyt9DelQ2QZOKubE8ypT3Y0D9pXpKGwGuSvAK4GlhTVXeyAHdlz/eO7LF9mikTU1lqd4uOyh2uo9IOsC1dMeGSpJm9B3grzZ3VbwXOoXkcTt93Zc/3jux3XnAR52yauvvecvLsjjEsRuUO11FpB9iWrszmSfOStMeqqjuq6v6q+iHwXuCYdpV3ZUuaNRMuSZpB+00ZE14CTHyv7MXASUkenuRQHrgrextwT5Kntd8Z+wrgooEGLWnoeElRklrtXdmrgQOTbAXeDKxOchTNZcEtwK9Dc1d2kom7snfy4LuyP0DzWIhLccK8tMcz4ZKklndlS+qKlxQlSZI6ZsIlSZLUMRMuSZKkjplwSZIkdcyES5IkqWMmXJIkSR0z4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdWy3CVeS9yfZnuTanrIDklyW5Kb2df+edWcl2ZzkxiTP6Sk/Osmmdt2fJsnCN0eSJGn4zGaE6wPA8ZPK1gKXV9VhwOXtMkkOB04Cjmj3eXeSvdp93gOcDhzW/kw+piRJ0kjabcJVVZ8Fvj2p+ATgvPb9ecCLe8o3VNV9VXULsBk4JslBwL5V9fmqKuCDPftIkiSNtL3nud9YVW0DqKptSR7flh8MXNGz3da27Aft+8nlU0pyOs1oGGNjY4yPj88qqDUrd+4a5D4PlM32GItlx44dQx9jL+PtlvFK0miZb8I1nanmZdUM5VOqqvXAeoBVq1bV6tWrZ1X5qWs/ucvympU7OWdT08QtJ8/uGItlfHyc2bZzGBhvt4x3cSR5P/ACYHtVHdmW/RHwQuD7wM3AK6vqriQrgBuAG9vdr6iq32j3OZpmOsY+wCXAme3ovqQ91HzvUryjvUxI+7q9Ld8KHNKz3XLg9rZ8+RTlkjRMPsCD55deBhxZVT8N/BtwVs+6m6vqqPbnN3rKnbMqaRfzTbguBk5p358CXNRTflKShyc5lKajuaq9/HhPkqe1dye+omcfSRoKU81ZrarPVNXEfIUr2PXk8UGcsyppKrN5LMRHgM8DT06yNclpwNnAs5PcBDy7XaaqrgM2AtcDnwLOqKr720P9JvA+mon0NwOXLnBbJKlrr2LXvuvQJF9M8o9J/nNbdjBzmLMqac+w2zlcVfXSaVYdN83264B1U5RfDRw5p+gkaUgkeROwE7igLdoG/HhVfauds/U3SY5gDnNW53uDUO8NQZMttZsXRuWGi1FpB9iWriz0pHlJGjlJTqGZTH/cxOT3qroPuK99f02Sm4GfYA5zVud7g9A7L7joRzcETTbsNwhNNio3XIxKO8C2dMWv9pGkGSQ5HngD8KKq+m5P+eMmHuyc5Ek0c1a/4pxVSVNxhEuSWu2c1dXAgUm2Am+muSvx4cBl7TeSTTz+4ZnAHyTZCdwP/EZVTUy4/00eeCzEpThnVdrjmXBJUmuaOavnTrPtR4GPTrPOOauSduElRUmSpI6ZcEmSJHXMhEuSJKljJlySJEkdM+GSJEnqmAmXJElSx0y4JEmSOmbCJUmS1DETLkmSpI6ZcEmSJHXMhEuSJKljJlySJEkdM+GSJEnqmAmXJElSx/pKuJL8dpLrklyb5CNJHpHkgCSXJbmpfd2/Z/uzkmxOcmOS5/QfviRJ0vCbd8KV5GDgtcCqqjoS2As4CVgLXF5VhwGXt8skObxdfwRwPPDuJHv1F74kSdLw6/eS4t7APkn2Bh4J3A6cAJzXrj8PeHH7/gRgQ1XdV1W3AJuBY/qsX5IkaejtPd8dq+q2JG8DbgW+B3ymqj6TZKyqtrXbbEvy+HaXg4Ereg6xtS17kCSnA6cDjI2NMT4+PquY1qzcucvy2D4PlM32GItlx44dQx9jL+PtlvEujiTvB14AbG9H7klyAPBXwApgC/ArVXVnu+4s4DTgfuC1VfXptvxo4APAPsAlwJlVVYNsi6ThMu+Eq52bdQJwKHAX8NdJXjbTLlOUTdkBVdV6YD3AqlWravXq1bOK6dS1n9xlec3KnZyzqWnilpNnd4zFMj4+zmzbOQyMt1vGu2g+ALwL+GBP2cQ0ibOTrG2X3zBpmsQTgL9L8hNVdT/wHpqTxitoEq7jgUsH1gpJQ6efS4rPAm6pqm9U1Q+AjwE/B9yR5CCA9nV7u/1W4JCe/ZfTXIKUpKFQVZ8Fvj2peE7TJNp+b9+q+nw7qvXBnn0k7aHmPcJFcynxaUkeSXNJ8TjgauBe4BTg7Pb1onb7i4EPJ3k7zdngYcBVfdQvSYMw12kSP2jfTy5/kPlOn+idLjHZUru0OyqXo0elHWBbutLPHK4rk1wIfAHYCXyR5jLgMmBjktNokrIT2+2vS7IRuL7d/ox26F2SlqLppkl0Pn3inRdc9KPpEpMN+/SJyUblcvSotANsS1f6GeGiqt4MvHlS8X00o11Tbb8OWNdPnZI0YHckOagd3ZrNNImt7fvJ5ZL2YD5pXpJmdjHN9Ah48DSJk5I8PMmhtNMk2suP9yR5WpIAr+jZR9Ieqq8RLkkaJUk+AqwGDkyylWYE/2zmPk3iN3ngsRCX4h2K0h7PhEuSWlX10mlWzWmaRFVdDRy5gKFJWuK8pChJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6pgJlyRJUsf6SriS7JfkwiRfTnJDkqcnOSDJZUlual/379n+rCSbk9yY5Dn9hy9JkjT8+h3hegfwqar6SeApwA3AWuDyqjoMuLxdJsnhwEnAEcDxwLuT7NVn/ZIkSUNv3glXkn2BZwLnAlTV96vqLuAE4Lx2s/OAF7fvTwA2VNV9VXULsBk4Zr71S9KgJHlyki/1/HwnyeuSvCXJbT3lz+vZxxF9ST+ydx/7Pgn4BvCXSZ4CXAOcCYxV1TaAqtqW5PHt9gcDV/Tsv7Ute5AkpwOnA4yNjTE+Pj6rgNas3LnL8tg+D5TN9hiLZceOHUMfYy/j7ZbxDpequhE4CqAdmb8N+DjwSuCPq+ptvdtPGtF/AvB3SX6iqu4faOCShkY/CdfewFOB36qqK5O8g/by4TQyRVlNtWFVrQfWA6xatapWr149q4BOXfvJXZbXrNzJOZuaJm45eXbHWCzj4+PMtp3DwHi7ZbxD7Tjg5qr6ajJVtwb0jOgDtySZGNH//IBilDRk+km4tgJbq+rKdvlCmoTrjiQHtaNbBwHbe7Y/pGf/5cDtfdQvSYvhJOAjPcuvSfIK4GpgTVXdySxH9Oc7mt87ej/ZUhtpHJXR0VFpB9iWrsw74aqqryf5WpInt8PtxwHXtz+nAGe3rxe1u1wMfDjJ22mG2A8DruoneEkapCQPA14EnNUWvQd4K81o/VuBc4BXMcsR/fmO5r/zgot+NHo/2bCP5k82KqOjo9IOsC1d6WeEC+C3gAvaTugrNPMZHgJsTHIacCtwIkBVXZdkI01CthM4w/kMkpaY5wJfqKo7ACZeAZK8F/hEu+iIvqRd9JVwVdWXgFVTrDpumu3XAev6qVOSFtFL6bmcODF9ol18CXBt+94RfUm76HeES5L2CEkeCTwb+PWe4j9MchTN5cItE+sc0Zc0mQmXJM1CVX0XeOykspfPsL0j+pJ+xO9SlCRJ6pgJlyRJUse8pChJI2TFpAdAT7bl7OcPKBJJvRzhkiRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6pgJlyRJUsdMuCRJkjrmdylqZPV+p9yalTs5tWfZ75OTJA1S3yNcSfZK8sUkn2iXD0hyWZKb2tf9e7Y9K8nmJDcmeU6/dUuSJC0FC3FJ8Uzghp7ltcDlVXUYcHm7TJLDgZOAI4DjgXcn2WsB6pckSRpqfSVcSZYDzwfe11N8AnBe+/484MU95Ruq6r6qugXYDBzTT/2SNChJtiTZlORLSa5uyxzRlzQr/c7h+hPg9cCje8rGqmobQFVtS/L4tvxg4Iqe7ba2ZQ+S5HTgdICxsTHGx8dnFcyalTt3WR7b54Gy2R5jsezYsWPoY+y1FOLt/X3o/V0Afx8W2lKLtw/HVtU3e5YnRvTPTrK2XX7DpBH9JwB/l+Qnqur+wYcsaRjMO+FK8gJge1Vdk2T1bHaZoqym2rCq1gPrAVatWlWrV8/m8OwyKRqa/2DP2dQ0ccvJszvGYhkfH2e27RwGSyHeUydNmp/4XQB/HxbaUot3AZ0ArG7fnweMA2+gZ0QfuCXJxIj+5xchxl2smNRP9vJmEqk7/YxwPQN4UZLnAY8A9k1yPnBHkoPa0a2DgO3t9luBQ3r2Xw7c3kf9kjRIBXwmSQF/0Z4Y9jWiP9/R/MkjtgtlMUYpR2V0dFTaAbalK/NOuKrqLOAsgHaE63eq6mVJ/gg4BTi7fb2o3eVi4MNJ3k4zxH4YcNX8Q5ekgXpGVd3eJlWXJfnyDNvOakR/vqP577zgol1GbBfKYoz8jsro6Ki0A2xLV7p4DtfZwMYkpwG3AicCVNV1STYC1wM7gTOczyDwEoeWhqq6vX3dnuTjNJcIHdGXNCsLknBV1TjN3AWq6lvAcdNstw5YtxB1SovFBHHPk+RRwEOq6p72/S8Bf0Azcu+IvqTd8knzkrR7Y8DHk0DTb364qj6V5J8ZoRH9mU4mwBMKqR8mXJK0G1X1FeApU5TvUSP6ju5K8+eXV0uSJHXMhEuSJKljXlKUhsSKSQ9qnfwgXy/ZSNLS5QiXJElSx0y4JEmSOmbCJUmS1DHncGmoLbXnAi21eCVJg2HCNYJ8Vo4kScPFhEt7JEeiJEmD5BwuSZKkjplwSZIkdcyES5IkqWPO4ZKWCG+GkKSly4RLktQ3TwikmZlwSVPY3V2MkiTNhQkXPiJAkiR1a94JV5JDgA8CPwb8EFhfVe9IcgDwV8AKYAvwK1V1Z7vPWcBpwP3Aa6vq031Frz2eI1GSpKWgnxGuncCaqvpCkkcD1yS5DDgVuLyqzk6yFlgLvCHJ4cBJwBHAE4C/S/ITVXV/f03QoPQmN2tW7uTUnmVHATXKZjjBfAvwa8A32k3fWFWXtPt4gtma6cRozcqdrB5cKNKimXfCVVXbgG3t+3uS3AAcDJwAP/r7OQ8YB97Qlm+oqvuAW5JsBo4BPj/fGKSlxhG5JWu6E0yAP66qt/Vu7AmmpMkWZA5XkhXAzwBXAmNtMkZVbUvy+Hazg4Erenbb2pZNdbzTgdMBxsbGGB8fn1Uca1bu3GV5bJ8HymY6xuT9Jptt/f3YsWPHgtUzU3v6qaP3uL2f7UIetyuT4x12c413EL+jM1nI399hNMMJ5nQ8wZS0i74TriTLgI8Cr6uq7ySZdtMpymqqDatqPbAeYNWqVbV69epZxXLqpNGDNSt3cs6mtomb7p1hz5k/hi0nz67+foyPjzPbdu7O5M+hVz9tOXXSJcUffbYLeNyuTI532M013kH8js5kIX9/h92kE8xnAK9J8grgappRsDuZ5QnmfE8ul9oJxEzG9ln8E4aFMEonHbalG339D5TkoTTJ1gVV9bG2+I4kB7WjWwcB29vyrcAhPbsvB27vp37NnXdkjiafgTQYU5xgvgd4K83J41uBc4BXMcsTzPmeXL7zgouW1AnETNas3MmvjECyPkonHbalG/P+ap80Q1nnAjdU1dt7Vl0MnNK+PwW4qKf8pCQPT3IocBhw1Xzrl6RBmuoEs6ruqKr7q+qHwHtpLhuCJ5iSJunnuxSfAbwc+MUkX2p/ngecDTw7yU3As9tlquo6YCNwPfAp4AwnkEpaCqY7wWxH8Se8BLi2fe8JpqRd9HOX4ueYetgc4Lhp9lkHrJtvneqed9GNHi8jL4iJE8xNSb7Ulr0ReGmSo2guF24Bfh2aE8wkEyeYO/EEU9rjjcYkAEnq0AwnmJfMsI8nmLPkHETtCUy4hpSjEpJkMqbRYcIlSRpJJmsaJiZcS5RzrSTt6ewHtZSYcGlB2PFJWkr6Gf2aat+J75ftZ+TMEbnR1s9jISRJkjQLjnBJktSjnxH7YRylGsaY9kQmXJIkDcAwTr2Y6fIomJAtJBMuSZKWsGFM5PRgJlyLqPePpPeMQpKkXiZVS58J1yx4/VuStCfqKtHbE//vNOGS9nCeUEhS90y4OuQQsCRJD7YnnuiZcEmSpKExqsmYCZekaY1qxydpaZrrlaNhesSFCVefvGwoSZJ2x6/2kSRJ6pgjXJIkaeQt9hSJgSdcSY4H3gHsBbyvqs4edAyS1DX7Omnp2N30oIVIyAZ6STHJXsCfAc8FDgdemuTwQcYgSV2zr5M02aDncB0DbK6qr1TV94ENwAkDjkGSumZfJ2kXqarBVZb8MnB8Vb26XX458LNV9ZpJ250OnN4uPhm4cZ5VHgh8c577DtpSihWMt2ujFu8Tq+pxgwpmsQ2gr1tqvx8zGZW2jEo7wLb0a8r+btBzuDJF2YMyvqpaD6zvu7Lk6qpa1e9xBmEpxQrG2zXjXfI67etG6fMelbaMSjvAtnRl0JcUtwKH9CwvB24fcAyS1DX7Okm7GHTC9c/AYUkOTfIw4CTg4gHHIElds6+TtIuBXlKsqp1JXgN8muZW6fdX1XUdVtn3ZckBWkqxgvF2zXiXsAH0daP0eY9KW0alHWBbOjHQSfOSJEl7Ir/aR5IkqWMmXJIkSR0biYQrySFJ/iHJDUmuS3JmW35AksuS3NS+7r/YsfZKsleSLyb5RLs8tPEm2S/JhUm+3H7OTx/WeJP8dvt7cG2SjyR5xLDFmuT9SbYnubanbNoYk5yVZHOSG5M8Z0ji/aP29+Ffk3w8yX7DEu+oSnJ8+5luTrJ2seOZynz64+l+X5IcnWRTu+5Pk0z1uI2u2zPrfnrI2zGnPnzI2zKnPn5o2lJVS/4HOAh4avv+0cC/0Xydxh8Ca9vytaj1AVsAABhUSURBVMD/XuxYJ8X934APA59ol4c2XuA84NXt+4cB+w1jvMDBwC3APu3yRuDUYYsVeCbwVODanrIpY2x/l/8FeDhwKHAzsNcQxPtLwN7t+/89TPGO4g/N5PubgSe1f4P/Ahy+2HFNEeec+uOZfl+Aq4Cn0zzX7FLguYvQnln100ugHbPuw4e5LXPt44epLQP9Bx/gP8hFwLNpntp8UFt2EHDjYsfWE+Ny4HLgF3v+kIcyXmDf9hc8k8qHLt72j/FrwAE0d+F+giYxGMZYV7BrAjNljMBZwFk9230aePpixztp3UuAC4Yp3lH7af9j+HTP8i6f87D+7K4/nu73pd3myz3lLwX+YsCxz7qfHvJ2zKkPH/K2zKmPH6a2jMQlxV5JVgA/A1wJjFXVNoD29fGLF9mD/AnweuCHPWXDGu+TgG8Af9kOrb8vyaMYwnir6jbgbcCtwDbg7qr6DEMY6xSmi3Gig5mwtS0bJq+iOUOEpRHvUrTkPtdZ9sfTtevg9v3k8kGaSz89zO2Yax8+tG2ZRx8/NG0ZqYQryTLgo8Drquo7ix3PdJK8ANheVdcsdiyztDfN5aT3VNXPAPfSDNkOnfa6/Qk0Q8dPAB6V5GWLG1XfZvU1MYslyZuAncAFE0VTbDY08S5hS+pznUN/PF27FrW98+inh7Idrbn24UPblnn08UPTlpFJuJI8lOaP+4Kq+lhbfEeSg9r1BwHbFyu+SZ4BvCjJFmAD8ItJzmd4490KbK2qK9vlC2n+eIcx3mcBt1TVN6rqB8DHgJ9jOGOdbLoYh/ZrYpKcArwAOLnacXmGON4lbsl8rnPsj6dr19b2/eTyQZlrPz2s7YC59+HD3Ja59vFD05aRSLjaOwvOBW6oqrf3rLoYOKV9fwrNXIJFV1VnVdXyqlpB85Uff19VL2N44/068LUkT26LjgOuZzjjvRV4WpJHtr8XxwE3MJyxTjZdjBcDJyV5eJJDgcNoJnsuqiTHA28AXlRV3+1ZNZTxjoAl8XVB8+iPp/x9aS8L3ZPkae0xX8EA/27n0U8PZTvatsy1Dx/atjD3Pn542jLIyW5d/QA/TzMU+K/Al9qf5wGPpZnweFP7esBixzpF7Kt5YDLm0MYLHAVc3X7GfwPsP6zxAr8PfBm4FvgQzd0pQxUr8BGa+Qc/oDnTOm2mGIE30dxdcyOLc4fTVPFuppkbMfE39+fDEu+o/rT92r+1n+2bFjueaWKcc3883e8LsKr9O74ZeBeTJn0PsE2z6qeHuR1z7cOHvC1z6uOHpS1+tY8kSVLHRuKSoiRJ0jAz4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdcyES5IkqWMmXJIkSR0z4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdcyES5IkqWMmXJIkSR0z4ZIkSeqYCZfmJcmWJM9a7DgkSVoKTLi0pCTZe7FjkCRprky4NGdJPgT8OPC3SXYkeX2SpyX5v0nuSvIvSVb3bD+e5K1J/inJPUk+k+TAdt3qJFsnHf9Ho2dJ3pLkwiTnJ/kOcGqShyRZm+TmJN9KsjHJAYP7BCRJmhsTLs1ZVb0cuBV4YVUtAy4APgn8D+AA4HeAjyZ5XM9uvwq8Eng88LB2m9k6AbgQ2K+t67XAi4FfAJ4A3An8WR9NkiSpUyZcWggvAy6pqkuq6odVdRlwNfC8nm3+sqr+raq+B2wEjprD8T9fVX/THvt7wK8Db6qqrVV1H/AW4Je93ChJGlb+B6WF8ETgxCQv7Cl7KPAPPctf73n/XWDZHI7/tSnq+3iSH/aU3Q+MAbfN4biSJA2ECZfmq3refw34UFX92jyOcy/wyImFJHsBj5u0TU1a/hrwqqr6p3nUJ0nSwHlJUfN1B/Ck9v35wAuTPCfJXkke0U6GXz6L4/wb8Igkz0/yUOB3gYfvZp8/B9YleSJAksclOWGe7ZAkqXMmXJqv/wX8bpK7gP9KM7H9jcA3aEag/juz+P2qqruB/w94H83lwHuBrTPuBO8ALgY+k+Qe4ArgZ+fXDEmSupeqyVdrJEmStJAc4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUsaF/DteBBx5YK1asmHb9vffey6Me9ajBBWTd1m3dc3bNNdd8s6omP19NkvYYQ59wrVixgquvvnra9ePj46xevXpwAVm3dVv3nCX56sJEI0lLk5cUJUmSOmbCJUmS1DETLkmSpI6ZcEmSJHXMhEuSJKljJlySJEkdG/rHQszFirWfnHbdlrOfP8BIJEmSHuAIlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSO7TbhSvL+JNuTXNtTdkCSy5Lc1L7u37PurCSbk9yY5Dk95Ucn2dSu+9MkWfjmSJIkDZ/ZjHB9ADh+Utla4PKqOgy4vF0myeHAScAR7T7vTrJXu897gNOBw9qfyceUJEkaSbtNuKrqs8C3JxWfAJzXvj8PeHFP+Yaquq+qbgE2A8ckOQjYt6o+X1UFfLBnH0mSpJGWJv/ZzUbJCuATVXVku3xXVe3Xs/7Oqto/ybuAK6rq/Lb8XOBSYAtwdlU9qy3/z8AbquoF09R3Os1oGGNjY0dv2LBh2th27NjBsmXLANh0293Tbrfy4Mfstp1z1Vv3oFm3dS+luo899thrqmrVAoUkSUvOQj/4dKp5WTVD+ZSqaj2wHmDVqlW1evXqaSscHx9nYv2pMz349OTpjzFfvXUPmnVb955QtySNivnepXhHe5mQ9nV7W74VOKRnu+XA7W358inKJUmSRt58E66LgVPa96cAF/WUn5Tk4UkOpZkcf1VVbQPuSfK09u7EV/TsI0mSNNJ2e0kxyUeA1cCBSbYCbwbOBjYmOQ24FTgRoKquS7IRuB7YCZxRVfe3h/pNmjse96GZ13XpgrZEkiRpSO024aqql06z6rhptl8HrJui/GrgyDlFJ0mSNAJ80rwkSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdcyES5IkqWMmXJIkSR0z4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdcyES5IkqWMmXJIkSR0z4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjplwSZIkdayvhCvJbye5Lsm1ST6S5BFJDkhyWZKb2tf9e7Y/K8nmJDcmeU7/4UuSJA2/eSdcSQ4GXgusqqojgb2Ak4C1wOVVdRhwebtMksPb9UcAxwPvTrJXf+FLkiQNv34vKe4N7JNkb+CRwO3ACcB57frzgBe3708ANlTVfVV1C7AZOKbP+iVJkoZeqmr+OydnAuuA7wGfqaqTk9xVVfv1bHNnVe2f5F3AFVV1flt+LnBpVV04xXFPB04HGBsbO3rDhg3TxrBjxw6WLVsGwKbb7p52u5UHP2YeLZxZb92DZt3WvZTqPvbYY6+pqlULFJIkLTl7z3fHdm7WCcChwF3AXyd52Uy7TFE2ZbZXVeuB9QCrVq2q1atXT3vQ8fFxJtafuvaT02635eTpjzFfvXUPmnVb955QtySNin4uKT4LuKWqvlFVPwA+BvwccEeSgwDa1+3t9luBQ3r2X05zCVKSJGmk9ZNw3Qo8LckjkwQ4DrgBuBg4pd3mFOCi9v3FwElJHp7kUOAw4Ko+6pckSVoS5n1JsaquTHIh8AVgJ/BFmsuAy4CNSU6jScpObLe/LslG4Pp2+zOq6v4+45ckSRp68064AKrqzcCbJxXfRzPaNdX262gm2UuSJO0xfNK8JElSx0y4JEmSOmbCJUmS1DETLkmSpI6ZcEmSJHXMhEuSJKljJlySJEkdM+GSJEnqmAmXJElSx0y4JEmSOmbCJUmS1DETLkmSpI6ZcEmSJHXMhEuSJKljJlySJEkdM+GSJEnq2N6LHYCk4bVi7SdZs3Inp6795IPWbTn7+YsQkSQtTY5wSZIkdcyES5IkqWMmXJIkSR0z4ZIkSepYXwlXkv2SXJjky0luSPL0JAckuSzJTe3r/j3bn5Vkc5Ibkzyn//AlSZKGX78jXO8APlVVPwk8BbgBWAtcXlWHAZe3yyQ5HDgJOAI4Hnh3kr36rF+SJGnozTvhSrIv8EzgXICq+n5V3QWcAJzXbnYe8OL2/QnAhqq6r6puATYDx8y3fkmSpKUiVTW/HZOjgPXA9TSjW9cAZwK3VdV+PdvdWVX7J3kXcEVVnd+WnwtcWlUXTnHs04HTAcbGxo7esGHDtHHs2LGDZcuWAbDptrun3W7lwY+ZaxN3q7fuQbNu6x6ETbfdzdg+cMf3HrxuLn9Txx577DVVtWoBQ5OkJaWfB5/uDTwV+K2qujLJO2gvH04jU5RNme1V1XqaZI5Vq1bV6tWrpz3o+Pg4E+unejjjhC0nT3+M+eqte9Cs27oH4dT2wafnbHpwV9HF35Qkjap+5nBtBbZW1ZXt8oU0CdgdSQ4CaF+392x/SM/+y4Hb+6hfkiRpSZh3wlVVXwe+luTJbdFxNJcXLwZOactOAS5q318MnJTk4UkOBQ4Drppv/ZIkSUtFv9+l+FvABUkeBnwFeCVNErcxyWnArcCJAFV1XZKNNEnZTuCMqrq/z/olSZKGXl8JV1V9CZhqIuxx02y/DljXT52SJElLjU+alyRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6pgJlyRJUsdMuCRJkjpmwiVJktQxEy5JkqSO9Z1wJdkryReTfKJdPiDJZUlual/379n2rCSbk9yY5Dn91i1JkrQULMQI15nADT3La4HLq+ow4PJ2mSSHAycBRwDHA+9OstcC1C9JkjTU+kq4kiwHng+8r6f4BOC89v15wIt7yjdU1X1VdQuwGTimn/olSZKWglTV/HdOLgT+F/Bo4Heq6gVJ7qqq/Xq2ubOq9k/yLuCKqjq/LT8XuLSqLpziuKcDpwOMjY0dvWHDhmlj2LFjB8uWLQNg0213T7vdyoMfM48Wzqy37kGzbusehE233c3YPnDH9x68bi5/U8cee+w1VbVqAUOTpCVl7/numOQFwPaquibJ6tnsMkXZlNleVa0H1gOsWrWqVq+e/vDj4+NMrD917Sen3W7LybMJcW566x4067buQTh17SdZs3In52x6cFfRxd+UJI2qeSdcwDOAFyV5HvAIYN8k5wN3JDmoqrYlOQjY3m6/FTikZ//lwO191C9JkrQkzHsOV1WdVVXLq2oFzWT4v6+qlwEXA6e0m50CXNS+vxg4KcnDkxwKHAZcNe/IJUmSloh+RrimczawMclpwK3AiQBVdV2SjcD1wE7gjKq6v4P6JUmShsqCJFxVNQ6Mt++/BRw3zXbrgHULUedCWjHD3C+ALWc/f0CRSJKkUeST5iVJkjpmwiVJktQxEy5JkqSOmXBJkiR1zIRLkiSpYyZckiRJHTPhkiRJ6lgXDz4dSrt71pYkSVJXHOGSJEnqmAmXJElSx0y4JEmSOrbHzOFaDH5HoyRJAke4JEmSOmfCJUmS1DEvKUojzkvbkrT4HOGSJEnqmAmXJElSx0y4JEmSOmbCJUmS1DEnzc/CdJOO16zcyerBhtI3J1BLkjR4JlxL1Kbb7ubUaZInkyZJkobLvBOuJIcAHwR+DPghsL6q3pHkAOCvgBXAFuBXqurOdp+zgNOA+4HXVtWn+4p+COxuxEijZ6Z/c5NdSdJU+pnDtRNYU1U/BTwNOCPJ4cBa4PKqOgy4vF2mXXcScARwPPDuJHv1E7wkSdJSMO8RrqraBmxr39+T5AbgYOAE+NHUpvOAceANbfmGqroPuCXJZuAY4PPzjUGar2GcyzZTTEtxvqAk6QGpqv4PkqwAPgscCdxaVfv1rLuzqvZP8i7giqo6vy0/F7i0qi6c4ninA6cDjI2NHb1hw4Zp696xYwfLli0DmnlNgzS2D9zxvfnvv/Lgx8x73+3fvnvaumc67u4+o9nE1PuZL+RxZ2OquudjPvFO1D3Tvv20c6bjju0Djz9gfsfu599m0213T/t7Ppe2HnvssddU1apZ7yBJI6bvSfNJlgEfBV5XVd9JMu2mU5RNme1V1XpgPcCqVatq9erV09Y/Pj7OxPrpJpF3Zc3KnZyzaf4f4ZaTV89733decNG0dc903N19RrOJqfczX8jjTmXyqM+alfdzzufufeC48xyJmk+8E+2ead9+/k1nOu6alTv5lRn+DuZ7XAA23TvDyr2n/T3vp62StKfp6zlcSR5Kk2xdUFUfa4vvSHJQu/4gYHtbvhU4pGf35cDt/dQvSZK0FPRzl2KAc4EbqurtPasuBk4Bzm5fL+op/3CStwNPAA4Drppv/Zqed05KkjRc+rmk+Azg5cCmJF9qy95Ik2htTHIacCtwIkBVXZdkI3A9zR2OZ1TV/X3UP9J2lzStWTmgQCRJUt/6uUvxc0w9LwvguGn2WQesm2+do8aRKEmS9gx+l6IkSVLH/GofaQQ4WipJw82ESxqgfhIjkypJWrpMuDRrE//hr1m5c87PPPP7ByVJezITLu1iqY2idJXITXXc2SSaS+3zkyQNhgmXFp1JiiRp1HmXoiRJUscc4dLIcuRMkjQsHOGSJEnqmAmXJElSx0y4JEmSOmbCJUmS1DETLkmSpI6ZcEmSJHXMhEuSJKljJlySJEkdM+GSJEnqmAmXJElSx0y4JEmSOmbCJUmS1DETLkmSpI4NPOFKcnySG5NsTrJ20PVLkiQN2kATriR7AX8GPBc4HHhpksMHGYMkSdKgDXqE6xhgc1V9paq+D2wAThhwDJIkSQOVqhpcZckvA8dX1avb5ZcDP1tVr5m03enA6e3ik4EbZzjsgcA3Owh3Nqzbuq17dp5YVY9biGAkaSnae8D1ZYqyB2V8VbUeWD+rAyZXV9WqfgObD+u2buuWJM3GoC8pbgUO6VleDtw+4BgkSZIGatAJ1z8DhyU5NMnDgJOAiwccgyRJ0kAN9JJiVe1M8hrg08BewPur6ro+DzurS48dsW7rtm5J0m4NdNK8JEnSnsgnzUuSJHXMhEuSJKljSzbhGuRXBCV5f5LtSa7tKTsgyWVJbmpf9++o7kOS/EOSG5Jcl+TMQdWf5BFJrkryL23dvz+ounti2CvJF5N8YpB1J9mSZFOSLyW5esB175fkwiRfbv/dnz7Aup/ctnni5ztJXjfIf3NJGkVLMuFahK8I+gBw/KSytcDlVXUYcHm73IWdwJqq+ingacAZbVsHUf99wC9W1VOAo4DjkzxtQHVPOBO4oWd5kHUfW1VH9TyDalB1vwP4VFX9JPAUmvYPpO6qurFt81HA0cB3gY8Pqn5JGlVLMuFiwF8RVFWfBb49qfgE4Lz2/XnAizuqe1tVfaF9fw/Nf74HD6L+auxoFx/a/tQg6gZIshx4PvC+nuKB1D2NzutOsi/wTOBcgKr6flXdNYi6p3AccHNVfXWR6pekkbFUE66Dga/1LG9tywZprKq2QZMUAY/vusIkK4CfAa4cVP3tJb0vAduBy6pqYHUDfwK8HvhhT9mg6i7gM0muab9qalB1Pwn4BvCX7aXU9yV51IDqnuwk4CPt+8WoX5JGxlJNuGb1FUGjJMky4KPA66rqO4Oqt6ruby8vLQeOSXLkIOpN8gJge1VdM4j6pvCMqnoqzWXrM5I8c0D17g08FXhPVf0McC+LcPmufTDxi4C/HnTdkjSKlmrCNQxfEXRHkoMA2tftXVWU5KE0ydYFVfWxQdcP0F7WGqeZyzaIup8BvCjJFppLxr+Y5PwB1U1V3d6+bqeZw3TMgOreCmxtRxIBLqRJwAb6702TaH6hqu5olwddvySNlKWacA3DVwRdDJzSvj8FuKiLSpKEZj7PDVX19kHWn+RxSfZr3+8DPAv48iDqrqqzqmp5Va2g+ff9+6p62SDqTvKoJI+eeA/8EnDtIOquqq8DX0vy5LboOOD6QdQ9yUt54HIii1C/JI2UJfuk+STPo5njM/EVQes6rOsjwGrgQOAO4M3A3wAbgR8HbgVOrKrJE+sXou6fB/4PsIkH5jK9kWYeV6f1J/lpmgnSe9Ek5xur6g+SPLbruifFsRr4nap6wSDqTvIkmlEtaC7xfbiq1g2q3UmOorlR4GHAV4BX0n7+Xdfd1v9ImjmST6qqu9uygf6bS9KoWbIJlyRJ0lKxVC8pSpIkLRkmXJIkSR0z4ZIkSeqYCZckSVLHTLgkSZI6ZsIlSZLUMRMuSZKkjv0/L071iz1zxCgAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">Churn</span> <span class="o">==</span> <span class="s2">&quot;No&quot;</span><span class="p">][</span><span class="n">numerical_features</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">bins</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">Churn</span> <span class="o">==</span> <span class="s2">&quot;Yes&quot;</span><span class="p">][</span><span class="n">numerical_features</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">bins</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[30]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A303741208&gt;,
       &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A302DABB38&gt;,
       &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000002A3035BBC50&gt;],
      dtype=object)</pre>
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
<h2 id="Categorical-EDA">Categorical EDA<a class="anchor-link" href="#Categorical-EDA">&#182;</a></h2><h1 id="Anaylse-der-Kategorischen-Variablen.-Das-vorgehen-hier-ist-gut,-da-wir-in-jedem-Feature-nicht-zuviele-ausp&#228;gungen-haben">Anaylse der Kategorischen Variablen. Das vorgehen hier ist gut, da wir in jedem Feature nicht zuviele ausp&#228;gungen haben<a class="anchor-link" href="#Anaylse-der-Kategorischen-Variablen.-Das-vorgehen-hier-ist-gut,-da-wir-in-jedem-Feature-nicht-zuviele-ausp&#228;gungen-haben">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ROWS</span><span class="p">,</span> <span class="n">COLS</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">4</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">ROWS</span><span class="p">,</span> <span class="n">COLS</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">18</span><span class="p">,</span> <span class="mi">18</span><span class="p">))</span>
<span class="n">row</span><span class="p">,</span> <span class="n">col</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">categorical_feature</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">categorical_features</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">col</span> <span class="o">==</span> <span class="n">COLS</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">row</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="n">col</span> <span class="o">=</span> <span class="n">i</span> <span class="o">%</span> <span class="n">COLS</span>
    <span class="n">df</span><span class="p">[</span><span class="n">categorical_feature</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="n">row</span><span class="p">,</span> <span class="n">col</span><span class="p">])</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">categorical_feature</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\ipykernel_launcher.py:8: FutureWarning: `Series.plot()` should not be called with positional arguments, only keyword arguments. The order of positional arguments will change in the future. Use `Series.plot(kind=&#39;bar&#39;)` instead of `Series.plot(&#39;bar&#39;,)`.
  
</pre>
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
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">feature</span> <span class="o">=</span> <span class="s1">&#39;Contract&#39;</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">Churn</span> <span class="o">==</span> <span class="s2">&quot;No&quot;</span><span class="p">][</span><span class="n">feature</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;not churned&#39;</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">Churn</span> <span class="o">==</span> <span class="s2">&quot;Yes&quot;</span><span class="p">][</span><span class="n">feature</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;churned&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\ipykernel_launcher.py:3: FutureWarning: `Series.plot()` should not be called with positional arguments, only keyword arguments. The order of positional arguments will change in the future. Use `Series.plot(kind=&#39;bar&#39;)` instead of `Series.plot(&#39;bar&#39;,)`.
  This is separate from the ipykernel package so we can avoid doing imports until
C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\ipykernel_launcher.py:4: FutureWarning: `Series.plot()` should not be called with positional arguments, only keyword arguments. The order of positional arguments will change in the future. Use `Series.plot(kind=&#39;bar&#39;)` instead of `Series.plot(&#39;bar&#39;,)`.
  after removing the cwd from sys.path.
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[42]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;churned&#39;)</pre>
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
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="n">target</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="s1">&#39;bar&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;churned&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: `Series.plot()` should not be called with positional arguments, only keyword arguments. The order of positional arguments will change in the future. Use `Series.plot(kind=&#39;bar&#39;)` instead of `Series.plot(&#39;bar&#39;,)`.
  &#34;&#34;&#34;Entry point for launching an IPython kernel.
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[43]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;churned&#39;)</pre>
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
<h1 id="Preprocessing">Preprocessing<a class="anchor-link" href="#Preprocessing">&#182;</a></h1><p>hier wird eine Pipeline aufgebaut. Diese setzt OHE auf die Kategorialen Werte und Standard Scaler auf die Numerischen Werte. Dazu wird eine Pipeline aufgebaut. Jedoch werden hier lediglich die "normalen" und keine individuellen Transformer verwendet.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="kn">import</span> <span class="n">FeatureUnion</span><span class="p">,</span> <span class="n">Pipeline</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">tree</span>
<span class="kn">from</span> <span class="nn">sklearn.base</span> <span class="kn">import</span> <span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>


<span class="k">class</span> <span class="nc">ItemSelector</span><span class="p">(</span><span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">key</span> <span class="o">=</span> <span class="n">key</span>

    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">df</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">df</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">key</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pipeline</span> <span class="o">=</span> <span class="n">Pipeline</span><span class="p">(</span>
    <span class="p">[</span>
        <span class="p">(</span>
            <span class="s2">&quot;union&quot;</span><span class="p">,</span>
            <span class="n">FeatureUnion</span><span class="p">(</span>
                <span class="n">transformer_list</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">(</span>
                        <span class="s2">&quot;categorical_features&quot;</span><span class="p">,</span>
                        <span class="n">Pipeline</span><span class="p">(</span>
                            <span class="p">[</span>
                                <span class="p">(</span><span class="s2">&quot;selector&quot;</span><span class="p">,</span> <span class="n">ItemSelector</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">categorical_features</span><span class="p">)),</span>
                                <span class="p">(</span><span class="s2">&quot;onehot&quot;</span><span class="p">,</span> <span class="n">OneHotEncoder</span><span class="p">()),</span>
                            <span class="p">]</span>
                        <span class="p">),</span>
                    <span class="p">)</span>
                <span class="p">]</span>
                <span class="o">+</span> <span class="p">[</span>
                    <span class="p">(</span>
                        <span class="s2">&quot;numerical_features&quot;</span><span class="p">,</span>
                        <span class="n">Pipeline</span><span class="p">(</span>
                            <span class="p">[</span>
                                <span class="p">(</span><span class="s2">&quot;selector&quot;</span><span class="p">,</span> <span class="n">ItemSelector</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">numerical_features</span><span class="p">)),</span>
                                <span class="p">(</span><span class="s2">&quot;scalar&quot;</span><span class="p">,</span> <span class="n">StandardScaler</span><span class="p">()),</span>
                            <span class="p">]</span>
                        <span class="p">),</span>
                    <span class="p">)</span>
                <span class="p">]</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="p">(</span><span class="s2">&quot;classifier&quot;</span><span class="p">,</span> <span class="n">tree</span><span class="o">.</span><span class="n">DecisionTreeClassifier</span><span class="p">(</span><span class="n">max_depth</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)),</span>
    <span class="p">]</span>
<span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Split-des-DF">Split des DF<a class="anchor-link" href="#Split-des-DF">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>

<span class="n">df_train</span><span class="p">,</span> <span class="n">df_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.25</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="n">pipeline</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">df_train</span><span class="p">,</span> <span class="n">df_train</span><span class="p">[</span><span class="n">target</span><span class="p">])</span>
<span class="n">pred</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">df_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">classification_report</span>

<span class="nb">print</span><span class="p">(</span><span class="n">classification_report</span><span class="p">(</span><span class="n">df_test</span><span class="p">[</span><span class="n">target</span><span class="p">],</span> <span class="n">pred</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>              precision    recall  f1-score   support

          No       0.81      0.94      0.87      1300
         Yes       0.67      0.37      0.48       458

    accuracy                           0.79      1758
   macro avg       0.74      0.65      0.67      1758
weighted avg       0.77      0.79      0.77      1758

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">sklearn.tree</span> <span class="k">as</span> <span class="nn">tree</span>
<span class="kn">import</span> <span class="nn">pydotplus</span>
<span class="kn">from</span> <span class="nn">sklearn.externals.six</span> <span class="kn">import</span> <span class="n">StringIO</span> 
<span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">Image</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\externals\six.py:31: FutureWarning: The module is deprecated in version 0.21 and will be removed in version 0.23 since we&#39;ve dropped support for Python 2.7. Please rely on the official version of six (https://pypi.org/project/six/).
  &#34;(https://pypi.org/project/six/).&#34;, FutureWarning)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">classifier</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">NameError</span>                                 Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-51-b1e7795e1236&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>print<span class="ansi-yellow-intense-fg ansi-bold">(</span>classifier<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-red-intense-fg ansi-bold">NameError</span>: name &#39;classifier&#39; is not defined</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dot_data</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span>
<span class="n">tree</span><span class="o">.</span><span class="n">export_graphviz</span><span class="p">(</span><span class="n">clf</span><span class="p">,</span> 
 <span class="n">out_file</span><span class="o">=</span><span class="n">dot_data</span><span class="p">,</span> 
 <span class="n">class_names</span><span class="o">=</span><span class="n">breast_cancer</span><span class="o">.</span><span class="n">target_names</span><span class="p">,</span> <span class="c1"># the target names.</span>
 <span class="n">feature_names</span><span class="o">=</span><span class="n">breast_cancer</span><span class="o">.</span><span class="n">feature_names</span><span class="p">,</span> <span class="c1"># the feature names.</span>
 <span class="n">filled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="c1"># Whether to fill in the boxes with colours.</span>
 <span class="n">rounded</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="c1"># Whether to round the corners of the boxes.</span>
 <span class="n">special_characters</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">graph</span> <span class="o">=</span> <span class="n">pydotplus</span><span class="o">.</span><span class="n">graph_from_dot_data</span><span class="p">(</span><span class="n">dot_data</span><span class="o">.</span><span class="n">getvalue</span><span class="p">())</span> 
<span class="n">Image</span><span class="p">(</span><span class="n">graph</span><span class="o">.</span><span class="n">create_png</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

</div>
 

