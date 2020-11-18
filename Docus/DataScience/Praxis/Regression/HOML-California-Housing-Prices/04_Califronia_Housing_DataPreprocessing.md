'''''

{
"title": "Data-Preprocessing-Checklist",
"keywords": "DataPreprocessing, ",
"categories": "",
"description": "Hier geht es um die individuelle Abarbeitung der <em>EDA</em>-Checkliste im Kontext der California-Housing Problematik",
"level": "30",
"pageID": "16112020-10-California-Housing-Data-Preprocessing-Checklist"
}
'''''
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<center><h1>California Housing <br> Data Preprocessing</h1></center><p><img src="imgs/2020-11-14-21-31-19.png" alt=""></p>
<p>In diesem Notebook wird die <a href="16112020-EDA-Checklite">EDA-Checkliste</a> im Kontext des California-Housing Problem abgeabreitet. Bei dieser Checkliste geht es darum, die Datenstruktur grundlegend zu verstehen. Hier werden die Daten lediglich beschrieben, das ist wichtig bevor die Modellierung startet.</p>
<h1 id="Laden-der-Daten">Laden der Daten<a class="anchor-link" href="#Laden-der-Daten">&#182;</a></h1><p>Die Daten wurden bereits im vorherigen <a href="14112020-10-California-Housing-Data">Notebook - California Housing Priceses Data</a> gesplittet und persistent auf der Festplatte gespeichert. Somit müssen diese Daten in diesem Notebook zunächst geladen werden. Die Funktion Daten-Laden wurde in diesem Notebook der übersichtlichkeit wegen ebenfalls ausgelagert.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># To support both python 2 and python 3</span>

<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">tarfile</span>
<span class="kn">from</span> <span class="nn">six.moves</span> <span class="kn">import</span> <span class="n">urllib</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="kn">import</span> <span class="nn">FunctionFileCalifornia</span> <span class="k">as</span> <span class="nn">ffc</span>

<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">matplotlib</span> <span class="k">as</span> <span class="nn">mpl</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Basic Variables</span>
<span class="n">DOWNLOAD_ROOT</span> <span class="o">=</span> <span class="s2">&quot;https://raw.githubusercontent.com/ageron/handson-ml/master/&quot;</span>
<span class="n">HOUSING_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;housing&quot;</span><span class="p">)</span>
<span class="n">HOUSING_URL</span> <span class="o">=</span> <span class="n">DOWNLOAD_ROOT</span> <span class="o">+</span> <span class="s2">&quot;datasets/housing/housing.tgz&quot;</span>
<span class="n">PROJECT_ROOT_DIR</span> <span class="o">=</span> <span class="s2">&quot;.&quot;</span>
<span class="n">CHAPTER_ID</span> <span class="o">=</span> <span class="s2">&quot;end_to_end_project&quot;</span>
<span class="n">IMAGES_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_ROOT_DIR</span><span class="p">,</span> <span class="s2">&quot;images&quot;</span><span class="p">,</span> <span class="n">CHAPTER_ID</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>.\images\end_to_end_project
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">()</span>
<span class="n">strat_test_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_test_set.csv&quot;</span><span class="p">)</span>
<span class="n">strat_train_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_train_set.csv&quot;</span><span class="p">)</span>
<span class="c1">#print(housing.shape, strat_test_set.shape, strat_train_set.shape)</span>
<span class="c1">#print(strat_test_set.head123(5))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Vertikaler-Cut">Vertikaler Cut<a class="anchor-link" href="#Vertikaler-Cut">&#182;</a></h1><p>Im vorherigen <a href="14112020-10-California-Housing-Data">horizontalen Cut</a> wurden die Trainings und Testdaten erstellt und auf der Festplatte gepseichert. In dem Vertikalen Cut werden nun die Trainings und Testdaten in jeweils beschreibende und zu erklärende Variable aufgeteilt = Supervised Learning.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span> <span class="o">=</span> <span class="n">strat_train_set</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;median_house_value&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># drop labels for training set</span>
<span class="n">housing_labels</span> <span class="o">=</span> <span class="n">strat_train_set</span><span class="p">[</span><span class="s2">&quot;median_house_value&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(16512, 11)
(16512,)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Nan--Values">Nan -Values<a class="anchor-link" href="#Nan--Values">&#182;</a></h1><p>Aus dem <a href="14112020-10-California-Housing-Data">Data-Management-Notebook</a> ist kalr, dass NAN/0/"" Werte in dem Feature "total bedrooms" existieren. Diese Werte werden nun in dieser Rubrik behandelt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># erstelle df aller NAN-Zeilen</span>
<span class="n">sample_incomplete_rows</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[</span><span class="n">housing</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)]</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
<span class="n">sample_incomplete_rows</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>



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
      <th>Unnamed: 0</th>
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>ocean_proximity</th>
      <th>income_cat</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>113</th>
      <td>4629</td>
      <td>-118.30</td>
      <td>34.07</td>
      <td>18.0</td>
      <td>3759.0</td>
      <td>NaN</td>
      <td>3296.0</td>
      <td>1462.0</td>
      <td>2.2708</td>
      <td>&lt;1H OCEAN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>116</th>
      <td>6068</td>
      <td>-117.86</td>
      <td>34.01</td>
      <td>16.0</td>
      <td>4632.0</td>
      <td>NaN</td>
      <td>3038.0</td>
      <td>727.0</td>
      <td>5.1762</td>
      <td>&lt;1H OCEAN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>216</th>
      <td>17923</td>
      <td>-121.97</td>
      <td>37.35</td>
      <td>30.0</td>
      <td>1955.0</td>
      <td>NaN</td>
      <td>999.0</td>
      <td>386.0</td>
      <td>4.6328</td>
      <td>&lt;1H OCEAN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>303</th>
      <td>13656</td>
      <td>-117.30</td>
      <td>34.05</td>
      <td>6.0</td>
      <td>2155.0</td>
      <td>NaN</td>
      <td>1039.0</td>
      <td>391.0</td>
      <td>1.6675</td>
      <td>INLAND</td>
      <td>2</td>
    </tr>
    <tr>
      <th>321</th>
      <td>19252</td>
      <td>-122.79</td>
      <td>38.48</td>
      <td>7.0</td>
      <td>6837.0</td>
      <td>NaN</td>
      <td>3468.0</td>
      <td>1405.0</td>
      <td>3.1662</td>
      <td>&lt;1H OCEAN</td>
      <td>3</td>
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
<h2 id="Drops">Drops<a class="anchor-link" href="#Drops">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># ZeilenDrop</span>
<span class="n">exampleDS</span> <span class="o">=</span> <span class="n">sample_incomplete_rows</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">subset</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;total_bedrooms&quot;</span><span class="p">])</span>    <span class="c1"># option 1</span>
<span class="n">exampleDS</span><span class="o">.</span><span class="n">shape</span> <span class="c1"># =&gt; logisch, da alle gelöscht werden im Sub-DataFrame</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(0, 11)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># SpaltenDrop</span>
<span class="n">exampleDS</span> <span class="o">=</span> <span class="n">sample_incomplete_rows</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;total_bedrooms&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>       <span class="c1"># option 2  </span>
<span class="n">exampleDS</span><span class="o">.</span><span class="n">shape</span> <span class="c1"># hier der Drop der Spalte</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(5, 10)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Imputation">Imputation<a class="anchor-link" href="#Imputation">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Median</span>
<span class="n">median</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[</span><span class="s2">&quot;total_bedrooms&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">median</span><span class="p">()</span>
<span class="n">median</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>433.0</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_incomplete_rows</span><span class="p">[</span><span class="s2">&quot;total_bedrooms&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">median</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="c1"># option 3</span>
<span class="n">sample_incomplete_rows</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[30]:</div>



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
      <th>Unnamed: 0</th>
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>ocean_proximity</th>
      <th>income_cat</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>113</th>
      <td>4629</td>
      <td>-118.30</td>
      <td>34.07</td>
      <td>18.0</td>
      <td>3759.0</td>
      <td>433.0</td>
      <td>3296.0</td>
      <td>1462.0</td>
      <td>2.2708</td>
      <td>&lt;1H OCEAN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>116</th>
      <td>6068</td>
      <td>-117.86</td>
      <td>34.01</td>
      <td>16.0</td>
      <td>4632.0</td>
      <td>433.0</td>
      <td>3038.0</td>
      <td>727.0</td>
      <td>5.1762</td>
      <td>&lt;1H OCEAN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>216</th>
      <td>17923</td>
      <td>-121.97</td>
      <td>37.35</td>
      <td>30.0</td>
      <td>1955.0</td>
      <td>433.0</td>
      <td>999.0</td>
      <td>386.0</td>
      <td>4.6328</td>
      <td>&lt;1H OCEAN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>303</th>
      <td>13656</td>
      <td>-117.30</td>
      <td>34.05</td>
      <td>6.0</td>
      <td>2155.0</td>
      <td>433.0</td>
      <td>1039.0</td>
      <td>391.0</td>
      <td>1.6675</td>
      <td>INLAND</td>
      <td>2</td>
    </tr>
    <tr>
      <th>321</th>
      <td>19252</td>
      <td>-122.79</td>
      <td>38.48</td>
      <td>7.0</td>
      <td>6837.0</td>
      <td>433.0</td>
      <td>3468.0</td>
      <td>1405.0</td>
      <td>3.1662</td>
      <td>&lt;1H OCEAN</td>
      <td>3</td>
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
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span> <span class="c1"># Scikit-Learn 0.20+</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">Imputer</span> <span class="k">as</span> <span class="n">SimpleImputer</span>

<span class="n">imputer</span> <span class="o">=</span> <span class="n">SimpleImputer</span><span class="p">(</span><span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;median&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="c1"># alternatively: housing_num = housing.select_dtypes(include=[np.number])</span>
<span class="c1">#housing_num.shape #10</span>
<span class="c1">#housing.shape #11</span>
<span class="c1">#housing_num.isnull.any()</span>
<span class="n">imputer</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="n">imputer</span><span class="o">.</span><span class="n">statistics_</span>
<span class="n">housing_num</span><span class="o">.</span><span class="n">median</span><span class="p">()</span><span class="o">.</span><span class="n">values</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[53]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 1.0341e+04, -1.1851e+02,  3.4260e+01,  2.9000e+01,  2.1195e+03,
        4.3300e+02,  1.1640e+03,  4.0800e+02,  3.5409e+00,  3.0000e+00])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">housing_tr</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">sample_incomplete_rows</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">values</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[57]:</div>



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
      <th>Unnamed: 0</th>
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>income_cat</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>113</th>
      <td>4629.0</td>
      <td>-118.30</td>
      <td>34.07</td>
      <td>18.0</td>
      <td>3759.0</td>
      <td>433.0</td>
      <td>3296.0</td>
      <td>1462.0</td>
      <td>2.2708</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>6068.0</td>
      <td>-117.86</td>
      <td>34.01</td>
      <td>16.0</td>
      <td>4632.0</td>
      <td>433.0</td>
      <td>3038.0</td>
      <td>727.0</td>
      <td>5.1762</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>216</th>
      <td>17923.0</td>
      <td>-121.97</td>
      <td>37.35</td>
      <td>30.0</td>
      <td>1955.0</td>
      <td>433.0</td>
      <td>999.0</td>
      <td>386.0</td>
      <td>4.6328</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>303</th>
      <td>13656.0</td>
      <td>-117.30</td>
      <td>34.05</td>
      <td>6.0</td>
      <td>2155.0</td>
      <td>433.0</td>
      <td>1039.0</td>
      <td>391.0</td>
      <td>1.6675</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>321</th>
      <td>19252.0</td>
      <td>-122.79</td>
      <td>38.48</td>
      <td>7.0</td>
      <td>6837.0</td>
      <td>433.0</td>
      <td>3468.0</td>
      <td>1405.0</td>
      <td>3.1662</td>
      <td>3.0</td>
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
<div class="prompt input_prompt">In&nbsp;[58]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">imputer</span><span class="o">.</span><span class="n">strategy</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[58]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;median&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[59]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">housing_tr</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[59]:</div>



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
      <th>Unnamed: 0</th>
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>income_cat</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>17606.0</td>
      <td>-121.89</td>
      <td>37.29</td>
      <td>38.0</td>
      <td>1568.0</td>
      <td>351.0</td>
      <td>710.0</td>
      <td>339.0</td>
      <td>2.7042</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18632.0</td>
      <td>-121.93</td>
      <td>37.05</td>
      <td>14.0</td>
      <td>679.0</td>
      <td>108.0</td>
      <td>306.0</td>
      <td>113.0</td>
      <td>6.4214</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14650.0</td>
      <td>-117.20</td>
      <td>32.77</td>
      <td>31.0</td>
      <td>1952.0</td>
      <td>471.0</td>
      <td>936.0</td>
      <td>462.0</td>
      <td>2.8621</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3230.0</td>
      <td>-119.61</td>
      <td>36.31</td>
      <td>25.0</td>
      <td>1847.0</td>
      <td>371.0</td>
      <td>1460.0</td>
      <td>353.0</td>
      <td>1.8839</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3555.0</td>
      <td>-118.59</td>
      <td>34.23</td>
      <td>17.0</td>
      <td>6592.0</td>
      <td>1525.0</td>
      <td>4459.0</td>
      <td>1463.0</td>
      <td>3.0347</td>
      <td>3.0</td>
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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Encoder</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Engineering</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Pipeline</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
 

