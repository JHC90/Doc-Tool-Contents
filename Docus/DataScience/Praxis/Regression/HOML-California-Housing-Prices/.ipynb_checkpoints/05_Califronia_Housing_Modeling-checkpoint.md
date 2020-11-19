'''''

{
"title": "Data-Modelling-Checklist",
"keywords": "DataPreprocessing, ",
"categories": "",
"description": "Hier geht es um die individuelle Abarbeitung der <em>EDA</em>-Checkliste im Kontext der California-Housing Problematik",
"level": "50",
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
<center><h1>California Housing <br> Data Modeling</h1></center><p><img src="imgs/2020-11-14-21-31-19.png" alt=""></p>
<h1 id="Vorgelagerte-Ausarbeitungen">Vorgelagerte Ausarbeitungen<a class="anchor-link" href="#Vorgelagerte-Ausarbeitungen">&#182;</a></h1><ul>
<li><a href="14112020-10-California-Housing-BigPicture">1. Big-Picture</a><br></li>
<li><a href="14112020-10-California-Housing-Data">2. Data-Management</a><br></li>
<li><a href="16112020-10-California-Housing-EDA">3. EDA</a><br></li>
<li><a href="16112020-10-California-Housing-Data-Preprocessing-Checklist">4. Data-Preprocessing</a><br></li>
</ul>
<h1 id="Algorithm-Modeling"><a href="">Algorithm-Modeling</a><a class="anchor-link" href="#Algorithm-Modeling">&#182;</a></h1><p>In diesem Notebook wird die <a href="19112020-ShortListModels">First-Algorithms-Checkliste</a> im Kontext des California-Housing Problem abgeabreitet. Bei dieser Checkliste geht es darum, erstmalig Algorithmen anzuwenden und deren Performance grunlegend zu prüfen.</p>
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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Laden der Daten und adaptieren des Indexes</span>
<span class="n">train_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;train-prepared-Feature.csv&quot;</span><span class="p">)</span>
<span class="n">train_set</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;index&#39;</span><span class="p">)</span>

<span class="n">train_labels</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;train-prepared-Labels.csv&quot;</span><span class="p">)</span>
<span class="n">train_labels</span> <span class="o">=</span> <span class="n">train_labels</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;index&#39;</span><span class="p">)</span>

<span class="n">test_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;test-prepared-Feature.csv&quot;</span><span class="p">)</span>
<span class="n">test_set</span> <span class="o">=</span> <span class="n">test_set</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;index&#39;</span><span class="p">)</span>

<span class="n">test_labels</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;test-prepared-Labels.csv&quot;</span><span class="p">)</span>
<span class="n">test_labels</span> <span class="o">=</span> <span class="n">test_labels</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;index&#39;</span><span class="p">)</span>


<span class="nb">print</span><span class="p">(</span><span class="n">train_set</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">train_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">test_set</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">test_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">print(train_set.head123())</span>
<span class="sd">print(train_labels.head123())</span>
<span class="sd">print(test_set.head123())</span>
<span class="sd">print(test_labels.head123())</span>
<span class="sd">&#39;&#39;&#39;</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(16512, 17)
(16512, 1)
(4128, 17)
(4128, 1)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\nprint(train_set.head123())\nprint(train_labels.head123())\nprint(test_set.head123())\nprint(test_labels.head123())\n&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">mean_squared_error</span><span class="p">,</span> <span class="n">r2_score</span><span class="p">,</span> <span class="n">accuracy_score</span><span class="p">,</span> <span class="n">median_absolute_error</span>

<span class="k">def</span> <span class="nf">calculate_performance</span><span class="p">(</span><span class="n">prediction</span><span class="p">,</span> <span class="n">actual</span><span class="p">,</span> <span class="n">scaler</span><span class="p">):</span>
    <span class="n">p</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">prediction</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span>
    <span class="n">a</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">actual</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span>
    <span class="n">mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">a</span><span class="p">)</span>
    <span class="n">err</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">mse</span><span class="p">)</span>
    <span class="n">r2</span> <span class="o">=</span> <span class="n">r2_score</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">p</span><span class="p">)</span>
    <span class="n">mae</span> <span class="o">=</span> <span class="n">median_absolute_error</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">a</span><span class="p">)</span>
    
    <span class="k">return</span> <span class="p">(</span><span class="n">mse</span><span class="p">,</span> <span class="n">err</span><span class="p">,</span> <span class="n">r2</span><span class="p">,</span> <span class="n">mae</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">print_performance</span><span class="p">(</span><span class="n">measure_tuple</span><span class="p">):</span>
    
    <span class="n">mse</span> <span class="o">=</span> <span class="n">measure_tuple</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">err</span> <span class="o">=</span> <span class="n">measure_tuple</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="n">r2</span> <span class="o">=</span> <span class="n">measure_tuple</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
    <span class="n">mae</span> <span class="o">=</span> <span class="n">measure_tuple</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
    
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Mean squared error is </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">mse</span><span class="p">)))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Positive mean error is </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">)))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Overall R² is </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">r2</span><span class="p">)))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Median absolute error is </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">mae</span><span class="p">)))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Train-Model">Train Model<a class="anchor-link" href="#Train-Model">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Liste der Performance-Vergleiche</span>
<span class="n">resultList</span> <span class="o">=</span> <span class="p">[]</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">resultList</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;list&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Lineare-Regression">Lineare Regression<a class="anchor-link" href="#Lineare-Regression">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Die folgenden 3 Zeilen genügen um ein Model zu erstellen und zu trainieren</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>
<span class="n">lin_reg</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">lin_reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
<span class="n">lin_reg</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">test_set</span><span class="p">,</span> <span class="n">test_labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0.6576014402233354</pre>
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

</div># FeatureImportance
importance = lin_reg.coef_
featureImportance = []
for i in range(0, len(importance[0]),1):
    feature = train_set.columns[i]
    specificImportance = importance[0][i]
    featureImportance.append([feature, specificImportance])
    #print(feature, specificImportance)   
print(featureImportance)
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># test einer möglichen Prediction, das dient nur der Veranschaulichung</span>
<span class="n">some_data</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="mi">5</span><span class="p">]</span>
<span class="n">some_true_labels</span> <span class="o">=</span> <span class="n">train_labels</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="mi">5</span><span class="p">]</span>
<span class="n">some_predictions</span> <span class="o">=</span> <span class="n">lin_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">some_data</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Predictions:&quot;</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">some_predictions</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Wahre Werte:&quot;</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">some_true_labels</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Predictions: [array([203840.]), array([326528.]), array([204544.]), array([58304.]), array([194240.])]
Wahre Werte: [&#39;median_house_value&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Performance Measure OLS</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_predictions_ols</span> <span class="o">=</span> <span class="n">lin_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">mean_absolute_error</span>
<span class="n">lin_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">housing_predictions_ols</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lin_mae</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>49483.498062015504
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## MSE</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">mean_squared_error</span>
<span class="n">lin_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">housing_predictions_ols</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lin_mse</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>4462015589.36531
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## RMSE</span>
<span class="n">lin_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">lin_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lin_rmse</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>66798.32025856122
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#listEnty = [&quot;OLS&quot;, lin_mae, lin_mse, lin_rmse, featureImportance]</span>
<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;OLS&quot;</span><span class="p">,</span> <span class="n">lin_mae</span><span class="p">,</span> <span class="n">lin_mse</span><span class="p">,</span> <span class="n">lin_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
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
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-12-b5c2d61aaca0&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold">#listEnty = [&#34;OLS&#34;, lin_mae, lin_mse, lin_rmse, importance, featureImportance]</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 2</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>listEnty <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-blue-intense-fg ansi-bold">&#34;OLS&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> lin_mae<span class="ansi-yellow-intense-fg ansi-bold">,</span> lin_mse<span class="ansi-yellow-intense-fg ansi-bold">,</span> lin_rmse<span class="ansi-yellow-intense-fg ansi-bold">,</span> importance<span class="ansi-yellow-intense-fg ansi-bold">]</span>
<span class="ansi-green-fg">      3</span> resultList<span class="ansi-yellow-intense-fg ansi-bold">.</span>append<span class="ansi-yellow-intense-fg ansi-bold">(</span>listEnty<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-red-intense-fg ansi-bold">NameError</span>: name &#39;importance&#39; is not defined</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Polynomiale-Regression">Polynomiale Regression<a class="anchor-link" href="#Polynomiale-Regression">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">PolynomialFeatures</span>

<span class="n">polynomial_feature_extractor</span> <span class="o">=</span> <span class="n">PolynomialFeatures</span><span class="p">(</span><span class="n">degree</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">polynomial_feature_extractor</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>

<span class="n">poly_train_data_X</span> <span class="o">=</span> <span class="n">polynomial_feature_extractor</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">train_set</span><span class="p">)</span>
<span class="n">poly_test_data_X</span> <span class="o">=</span> <span class="n">polynomial_feature_extractor</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>

<span class="n">poly_regressor</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">poly_regressor</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">poly_train_data_X</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>

<span class="n">poly_predicted_y</span> <span class="o">=</span> <span class="n">poly_regressor</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">poly_test_data_X</span><span class="p">)</span>

<span class="n">poly_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">poly_predicted_y</span><span class="p">)</span>
<span class="n">poly_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">poly_predicted_y</span><span class="p">)</span>
<span class="n">poly_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">poly_mse</span><span class="p">)</span>

<span class="c1">#print(poly_mae)</span>
<span class="c1">#print(poly_mse)</span>
<span class="c1">#print(poly_rmse)</span>

<span class="n">importance</span> <span class="o">=</span> <span class="n">poly_regressor</span><span class="o">.</span><span class="n">coef_</span>
<span class="c1"># importance</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39;featureImportance = []</span>
<span class="sd">for i in range(0, len(importance[0]),1):</span>
<span class="sd">    feature = train_set.columns[i]</span>
<span class="sd">    specificImportance = importance[0][i]</span>
<span class="sd">    featureImportance.append([feature, specificImportance])</span>
<span class="sd">    #print(feature, specificImportance)   </span>
<span class="sd">print(featureImportance)</span>
<span class="sd">&#39;&#39;&#39;</span>

<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Poly-Reg&quot;</span><span class="p">,</span> <span class="n">poly_mae</span><span class="p">,</span> <span class="n">poly_mse</span><span class="p">,</span> <span class="n">poly_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Lasso-Regression">Lasso Regression<a class="anchor-link" href="#Lasso-Regression">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">Lasso</span>

<span class="c1"># small alpha --&gt; little restriction on coefficients</span>
<span class="n">lasso_regressor</span> <span class="o">=</span> <span class="n">Lasso</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.01</span><span class="p">,</span> <span class="n">max_iter</span><span class="o">=</span><span class="mi">1000</span><span class="p">)</span>
<span class="n">lasso_regressor</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">lasso_predicted_y</span> <span class="o">=</span> <span class="n">lasso_regressor</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">lasso_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">lasso_predicted_y</span><span class="p">)</span>
<span class="n">lasso_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">lasso_predicted_y</span><span class="p">)</span>
<span class="n">lasso_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">lasso_mse</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Importance</span>
<span class="n">featureImportance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">importance</span> <span class="o">=</span> <span class="n">lasso_regressor</span><span class="o">.</span><span class="n">coef_</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">importance</span><span class="p">),</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">feature</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">specificImportance</span> <span class="o">=</span> <span class="n">importance</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">featureImportance</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">feature</span><span class="p">,</span> <span class="n">specificImportance</span><span class="p">])</span>
    <span class="c1">#print(feature, specificImportance)   </span>

<span class="c1">#listEnty = [&quot;Poly-Reg&quot;, poly_mae, poly_mse, poly_rmse, featureImportance]</span>
<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Poly-Reg&quot;</span><span class="p">,</span> <span class="n">poly_mae</span><span class="p">,</span> <span class="n">poly_mse</span><span class="p">,</span> <span class="n">poly_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">lasso_mae</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lasso_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lasso_rmse</span><span class="p">)</span>

<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Lasso-Reg&quot;</span><span class="p">,</span> <span class="n">lasso_mae</span><span class="p">,</span> <span class="n">lasso_mse</span><span class="p">,</span> <span class="n">lasso_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Regression-Decision-Tree">Regression-Decision-Tree<a class="anchor-link" href="#Regression-Decision-Tree">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.tree</span> <span class="kn">import</span> <span class="n">DecisionTreeRegressor</span>

<span class="n">tree_reg</span> <span class="o">=</span> <span class="n">DecisionTreeRegressor</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
<span class="n">tree_reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>

<span class="n">housing_predictions_dtr</span> <span class="o">=</span> <span class="n">tree_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>
<span class="c1">#print(housing_predictions_dtr)</span>
<span class="c1">#print(test_labels)</span>

<span class="n">tree_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">housing_predictions_dtr</span><span class="p">)</span>
<span class="n">tree_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">housing_predictions_dtr</span><span class="p">)</span>
<span class="n">tree_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">tree_mse</span><span class="p">)</span>


<span class="nb">print</span><span class="p">(</span><span class="n">tree_mae</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">tree_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">tree_rmse</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Importance</span>
<span class="n">featureImportance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">importance</span> <span class="o">=</span> <span class="n">tree_reg</span><span class="o">.</span><span class="n">feature_importances_</span>
<span class="c1">#print(importance)</span>
<span class="c1">#print(len(importance))</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">importance</span><span class="p">),</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">feature</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">specificImportance</span> <span class="o">=</span> <span class="n">importance</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">featureImportance</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">feature</span><span class="p">,</span> <span class="n">specificImportance</span><span class="p">])</span>
<span class="c1">#listEnty = [&quot;RegTree&quot;, tree_mae, tree_mse, tree_rmse, featureImportance]</span>
<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;RegTree&quot;</span><span class="p">,</span> <span class="n">tree_mae</span><span class="p">,</span> <span class="n">tree_mse</span><span class="p">,</span> <span class="n">tree_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Random-Forest">Random Forest<a class="anchor-link" href="#Random-Forest">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">RandomForestRegressor</span>

<span class="n">forest_reg</span> <span class="o">=</span> <span class="n">RandomForestRegressor</span><span class="p">(</span><span class="n">n_estimators</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
<span class="n">forest_reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">forest_prediction</span> <span class="o">=</span> <span class="n">forest_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>

<span class="n">RF_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">forest_prediction</span><span class="p">)</span>
<span class="n">RF_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">forest_prediction</span><span class="p">)</span>
<span class="n">RF_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">RF_mse</span><span class="p">)</span>


<span class="nb">print</span><span class="p">(</span><span class="n">RF_mae</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RF_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RF_rmse</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Importance</span>
<span class="n">featureImportance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">importance</span> <span class="o">=</span> <span class="n">forest_reg</span><span class="o">.</span><span class="n">feature_importances_</span>
<span class="c1">#print(importance)</span>
<span class="c1">#print(len(importance))</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">importance</span><span class="p">),</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">feature</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">specificImportance</span> <span class="o">=</span> <span class="n">importance</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">featureImportance</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">feature</span><span class="p">,</span> <span class="n">specificImportance</span><span class="p">])</span>
<span class="c1">#listEnty = [&quot;RegTree&quot;, tree_mae, tree_mse, tree_rmse, featureImportance]</span>
<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;RandForest&quot;</span><span class="p">,</span> <span class="n">RF_mae</span><span class="p">,</span> <span class="n">RF_mse</span><span class="p">,</span> <span class="n">RF_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">resultList</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">resultList</span><span class="p">))</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">titles</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Alg-Name&quot;</span><span class="p">,</span> <span class="s2">&quot;MAE&quot;</span><span class="p">,</span> <span class="s2">&quot;MSE&quot;</span><span class="p">,</span> <span class="s2">&quot;RMSE&quot;</span><span class="p">]</span>
<span class="n">performanceDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">resultList</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
<span class="n">performanceDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;Alg-Name&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">performanceDF</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">maeDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;MAE&quot;</span><span class="p">]</span>
<span class="n">mseDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;MSE&quot;</span><span class="p">]</span>
<span class="n">rmseDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;RMSE&quot;</span><span class="p">]</span>
<span class="n">maeDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mseDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">rmseDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
 

