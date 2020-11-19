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
<center><h1>California Housing <br>Data Modeling<br>&<br>Fine Tuning</h1></center><p><img src="imgs/2020-11-14-21-31-19.png" alt=""></p>
<h1 id="Vorgelagerte-Ausarbeitungen">Vorgelagerte Ausarbeitungen<a class="anchor-link" href="#Vorgelagerte-Ausarbeitungen">&#182;</a></h1><ul>
<li><a href="14112020-10-California-Housing-BigPicture">1. Big-Picture</a><br></li>
<li><a href="14112020-10-California-Housing-Data">2. Data-Management</a><br></li>
<li><a href="16112020-10-California-Housing-EDA">3. EDA</a><br></li>
<li><a href="16112020-10-California-Housing-Data-Preprocessing-Checklist">4. Data-Preprocessing</a><br></li>
</ul>
<h1 id="Algorithm-Modeling"><a href="19112020-ShortListModels">Algorithm-Modeling</a><a class="anchor-link" href="#Algorithm-Modeling">&#182;</a></h1><p>In diesem Notebook wird die <a href="19112020-ShortListModels">First-Algorithms-Checkliste</a> im Kontext des California-Housing Problem abgeabreitet. Bei dieser Checkliste geht es darum, erstmalig Algorithmen anzuwenden und deren Performance grunlegend zu prüfen.</p>
<h1 id="Algorithm-Fine-Tuning"><a href="">Algorithm-Fine-Tuning</a><a class="anchor-link" href="#Algorithm-Fine-Tuning">&#182;</a></h1><p>Diese Notebook arbeitet zeitlgeich die <a href="14112020-10-California-Housing-Data">Fine-Tuning-Checkliste</a> ab. Es ist erheblich hantlicher bei der Modelierung in einem Notebook zu bleibe. Es wäre zwar grundsätzlich möglich die trainierten Algorithmen zu speichern un in anderen Notebooks wieder zu öffnen, jedoch ist es komfortabler in einem Notebook hierbei zu arbeiten.</p>
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
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">PolynomialFeatures</span>

<span class="n">polynomial_feature_extractor</span> <span class="o">=</span> <span class="n">PolynomialFeatures</span><span class="p">(</span><span class="n">degree</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
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
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">importance</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>18
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
<div class="prompt input_prompt">In&nbsp;[15]:</div>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\Anaconda3\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:529: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 6340902440107.633, tolerance: 22103585513.765118
  model = cd_fast.enet_coordinate_descent(
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Lasso(alpha=0.01)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
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
<div class="prompt input_prompt">In&nbsp;[17]:</div>
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
<div class="prompt input_prompt">In&nbsp;[18]:</div>
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
<div class="prompt input_prompt">In&nbsp;[19]:</div>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>49458.05475606995
4461389041.578401
66793.63024704078
</pre>
</div>
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
<div class="prompt input_prompt">In&nbsp;[20]:</div>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>75607.39583333333
12277961800.540213
110805.96464333593
</pre>
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
<div class="prompt input_prompt">In&nbsp;[21]:</div>
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
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">RandomForestRegressor</span>

<span class="n">forest_reg</span> <span class="o">=</span> <span class="n">RandomForestRegressor</span><span class="p">(</span><span class="n">n_estimators</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
<span class="n">forest_reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>&lt;ipython-input-22-6bfaa24301ce&gt;:4: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  forest_reg.fit(train_set, train_labels)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>RandomForestRegressor()</pre>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>56528.563829941864
6167940977.204143
78536.23989728655
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
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
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">resultList</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">resultList</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[&#39;OLS&#39;, 49483.498062015504, 4462015589.36531, 66798.32025856122], [&#39;Poly-Reg&#39;, 80954.39569223936, 66653273599.85989, 258172.95288209393], [&#39;Poly-Reg&#39;, 80954.39569223936, 66653273599.85989, 258172.95288209393], [&#39;Lasso-Reg&#39;, 49458.05475606995, 4461389041.578401, 66793.63024704078], [&#39;RegTree&#39;, 75607.39583333333, 12277961800.540213, 110805.96464333593], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655]]
6
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>                     MAE           MSE           RMSE
Alg-Name                                             
OLS         49483.498062  4.462016e+09   66798.320259
Poly-Reg    80954.395692  6.665327e+10  258172.952882
Poly-Reg    80954.395692  6.665327e+10  258172.952882
Lasso-Reg   49458.054756  4.461389e+09   66793.630247
RegTree     75607.395833  1.227796e+10  110805.964643
RandForest  56528.563830  6.167941e+09   78536.239897
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">axes</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">rot</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">subplots</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[44]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x1bd8b639af0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4gAAAJkCAYAAABTQQ+DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdf5SedXnn8fcliUyaX0Iyi0tmZRLWFAyQqGHR07KGKlUooBKsAYpB1KiUqvzQdReBFMqpqCm7VlToUhGEgPxsgZUWrBR7dnU7SAjJAXMITHAQdBhDNpNkIOC1fzzfmT55MgkzmSd55sm8X+fcx7m/1/29n+v23OfkfLh/RWYiSZIkSdLrGt2AJEmSJGl0MCBKkiRJkgADoiRJkiSpMCBKkiRJkgADoiRJkiSpMCBKkiRJkgADoiRJkiSpMCBKkjRCEdEZES9HxPSa8RURkRHRXjW2tIz9p5ptz4yIVyOit2Y5cM8chSRJBkRJkurlaeDU/pWIOByYUL1BRARwBvAbYPEg+/g/mTmpZvnl7mxakqRqBkRJkurjBuAjVeuLgetrtjkaOBD4LLAoIl6/h3qTJGlIDIiSJNXHT4ApEXFoROwDfBj4Xs02i4G7gVvK+gl7sD9Jkl6TAVGSpPrpv4p4LPAE8Gx/ISJ+B/gQcFNmbgVuY/vbTN8RES9WLWv3UN+SJAEwrtENSJK0F7kBeAiYyfa3l34QeAX4X2X9RuCBiGjNzO4y9pPM/P090qkkSYPwCqIkSXWSmeuovKzmeOCOmvJiYBLwTEQ8D9wKjKfqxTaSJDWaVxAlSaqvjwH7ZeamiOj/d3YG8G7gOGBl1bafoxIcv75nW5QkaXAGREmS6igzB3tu8GhgRWb+Y/VgRHwdOD8iDitD74yI3pq5x2Tmv+6GViVJ2k5kZqN7kCRJkiSNAj6DKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCxuBnLqZPn57t7e2NbkOSJEmSGuLhhx9+ITNbB6uNuYDY3t5OR0dHo9uQJEmSpIaIiHU7qnmLqSRJkiQJMCBKkiRJkgoDoiRJkiQJGIPPIEqSJEnS1q1b6erqoq+vr9Gt7DYtLS20tbUxfvz4Ic+pS0CMiHbgm8A7gZeA24DPZeYrEfFu4CrgTcBPgTMzc12ZF8CXgY+XXV0L/JfMzKr9fgc4CngGOCczH6j63dOAvwSmA/cDZ2Xmb+pxTJIkSZL2Xl1dXUyePJn29nYqsWTvkpn09PTQ1dXFzJkzhzyvXreYfhP4NfDvgXnAu4CzI2I6cAdwEbA/0AHcUjVvCfABYC5wBHAC8Mmq+nLgEWAacCFwW0S0AkTEHOBq4AzgAGBz6UOSJEmSdqqvr49p06btleEQICKYNm3asK+Q1usW05nANzKzD3g+Iu4D5gAnA6sz89bS5FLghYg4JDOfABYDyzKzq9SXAZ8Avh0Rs4G3AX+YmVuA2yPic8BC4NvA6cDdmflQmXsR8HhETM7MjXU6LmlUaP/ivY1uYVTq/PIfNbqFUcnzZXCeL5KkWntrOOy3K8dXryuI/wNYFBG/ExEzgOOA/pD4aP9GmbkJWFvGqa2Xv6trT9WEvdp69b7XAi8Ds+t0TJIkSZK020QEZ5xxxsD6K6+8QmtrKyeccMI2273//e/nne985zZjS5cuZcaMGcybN29gefHFF0fcU72uIP4zlSt//w/YB/gucBeVW0a7a7bdAEwuf08q69W1SeXZxNpaf33GDubW7ntARCyhcjsrb3rTm4Z6TJIkSZLGiHrfgTOUO1cmTpzIqlWr2LJlCxMmTOD+++9nxowZ22zz4osv8rOf/YxJkybx9NNPb/M84bnnnssFF1xQ175HfAUxIl4H/AOVZw0nUnlhzH7AFUAvMKVmyhSg/6pgbX0K0FteUjPcubX1AZl5TWbOz8z5ra2tQz84SZIkSdqNjjvuOO69txJOly9fzqmnnrpN/fbbb+fEE09k0aJF3Hzzzbu9n3rcYro/8B+oPIP4Umb2UHnz6PHAaiovoAEgIiYCB5dxauvl7+rarIiYvJN69b5nAfsCa+pwTJIkSZK02/UHv76+PlauXMlRRx21Tb0/NJ566qksX758m9qVV145cHvpMcccU5d+RhwQM/MF4Gng0xExLiLeQOXlM48CdwKHRcTCiGgBLgZWlhfUAFwPnBcRMyLiQOB84Lqy3zXACuCSiGiJiA9SedPp7WXujcCJEXF0CZ6XAnf4ghpJkiRJzeKII46gs7OT5cuXc/zxx29T+9WvfsWTTz7J7//+7zN79mzGjRvHqlWrBurnnnsuK1asYMWKFfzoRz+qSz/1eknNycD7qDxv+CTwCnBuZnZTeevo5cB6Kt8zXFQ172rgbuAxYBVwbxnrtwiYX+Z+GTil7JPMXA18ikpQ/DWVZw/PrtPxSJIkSdIecdJJJ3HBBRdsd3vpLbfcwvr165k5cybt7e10dnbu9ttM6/KSmsxcASzYQe0B4JAd1BL4QlkGq3fuaL+lfhNw07CalSRJkqRR5KyzzmLq1KkcfvjhPPjggwPjy5cv57777ht4g+nTTz/Nsccey1/8xV/stl7qdQVRkiRJkrQL2tra+OxnP7vNWGdnJ8888wzveMc7BsZmzpzJlClT+OlPfwps+wzivHnz6OzsHHEv9frMhSRJkiQ1raF8lqLeent7txtbsGABCxYsAODZZ5/drv6zn/0MgKOOOoqlS5fWvScDoiRJkl5Tvb8Rt7doRKiQdidvMZUkSZIkAQZESZIkSVJhQJQkSZI0JlU+qrD32pXjMyBKkiRJGnNaWlro6enZa0NiZtLT00NLS8uw5vmSGkmSJEljTltbG11dXXR3dze6ld2mpaWFtra2Yc0xIEqSJEkac8aPH8/MmTMb3cao4y2mkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKuoWECNiUUQ8HhGbImJtRBxdxt8dEU9ExOaI+FFEHFQ1JyLiiojoKctXIiKq6u1lzuayj/fU/OZpEbGu/OZdEbF/vY5HkiRJksaaugTEiDgWuAL4KDAZ+M/AUxExHbgDuAjYH+gAbqmaugT4ADAXOAI4AfhkVX058AgwDbgQuC0iWstvzgGuBs4ADgA2A9+sx/FIkiRJ0lhUryuIfw5cmpk/yczfZuazmfkscDKwOjNvzcw+YCkwNyIOKfMWA8sys6tsvww4EyAiZgNvAy7JzC2ZeTvwGLCwzD0duDszH8rMXioh9OSImFynY5IkSZKkMWXEATEi9gHmA60R8WREdEXENyJiAjAHeLR/28zcBKwt49TWy9/Vtacyc+NO6tX7Xgu8DMwe6TFJkiRJ0lhUjyuIBwDjgVOAo4F5wFuBLwGTgA0122+gchsqg9Q3AJPKc4jDnVtbHxARSyKiIyI6uru7h35kkiRJkjSG1CMgbin/+9eZ+VxmvgD8FXA80AtMqdl+CtB/VbC2PgXozczchbm19QGZeU1mzs/M+a2trUM+MEmSJEkaS0YcEDNzPdAF5CDl1VReQANAREwEDi7j29XL39W1WTXPFNbWq/c9C9gXWLOrxyJJkiRJY1m9XlLzHeDPIuLfRcR+wOeAe4A7gcMiYmFEtAAXAysz84ky73rgvIiYEREHAucD1wFk5hpgBXBJRLRExAepvOn09jL3RuDEiDi6BM9LgTtqnlmUJEmSJA3RuDrt5zJgOpWrd33A94HLM7MvIhYC3wC+B/wUWFQ172pgFpW3kwL8zzLWbxGVwLgeeAY4JTO7ATJzdUR8ikpQnAY8QOUzG5IkSZKkXVCXgJiZW4Gzy1JbewA4ZLtJlVoCXyjLYPVOYMFOfvcm4KZhNyxJkiRJ2k69bjGVJEmSJDW5et1iKkmSJEm0f/HeRrcwKnV++Y8a3cKQeAVRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJxbhGNzCWtX/x3ka3MCp1fvmPGt2CJI0J/js0OP8dkjSWeQVRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgTUMSBGxJsjoi8ivlc19u6IeCIiNkfEjyLioKpaRMQVEdFTlq9ERFTV28uczWUf76n5vdMiYl1EbIqIuyJi/3odiyRJkiSNRfW8gngV8K/9KxExHbgDuAjYH+gAbqnafgnwAWAucARwAvDJqvpy4BFgGnAhcFtEtJZ9zwGuBs4ADgA2A9+s47FIkiRJ0phTl4AYEYuAF4EfVg2fDKzOzFszsw9YCsyNiENKfTGwLDO7MvNZYBlwZtnfbOBtwCWZuSUzbwceAxaWuacDd2fmQ5nZSyWEnhwRk+txPJIkSZI0Fo04IEbEFOBS4Pya0hzg0f6VzNwErC3j29XL39W1pzJz407q1fteC7wMzB7JsUiSJEnSWFaPK4iXAddm5i9qxicBG2rGNgCTd1DfAEwqzyEOd25tfRsRsSQiOiKio7u7+zUOR5IkSZLGphEFxIiYB7wHuHKQci8wpWZsCrBxB/UpQG9m5i7Mra1vIzOvycz5mTm/tbV1xwckSZIkSWPYSK8gLgDagWci4nngAmBhRPwMWE3lBTQARMRE4OAyTm29/F1dm1XzTGFtvXrfs4B9gTUjPB5JkiRJGrNGGhCvoRL65pXl28C9wHuBO4HDImJhRLQAFwMrM/OJMvd64LyImBERB1J5hvE6gMxcA6wALomIloj4IJU3nd5e5t4InBgRR5fgeSlwR80zi5IkSZKkYRg3ksmZuZnKJyYAiIheoC8zu8v6QuAbwPeAnwKLqqZfDcyi8nZSgP9ZxvotohIY1wPPAKf07zczV0fEp6gExWnAA8BHR3IskiRJkjTWjSgg1srMpTXrDwCH7GDbBL5QlsHqnVRuYd3Rb90E3LRrnUqSJEmSatXlO4iSJEmSpOZnQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVJhQJQkSZIkAQZESZIkSVIx4oAYEftGxLURsS4iNkbEIxFxXFX93RHxRERsjogfRcRBVbWIiCsioqcsX4mIqKq3lzmbyz7eU/Pbp5Xf3RQRd0XE/iM9HkmSJEkaq+pxBXEc8AvgXcBU4CLg+yXcTQfuKGP7Ax3ALVVzlwAfAOYCRwAnAJ+sqi8HHgGmARcCt0VEK0BEzAGuBs4ADgA2A9+sw/FIkiRJ0pg04oCYmZsyc2lmdmbmbzPzHuBp4O3AycDqzLw1M/uApcDciDikTF8MLMvMrsx8FlgGnAkQEbOBtwGXZOaWzLwdeAxYWOaeDtydmQ9lZi+VEHpyREwe6TFJkiRJ0lhU92cQI+IAYDawGpgDPNpfy8xNwNoyTm29/F1deyozN+6kXr3vtcDL5bclSZIkScNU14AYEeOBG4HvZuYTwCRgQ81mG4D+q3y19Q3ApPIc4nDn1tar+1oSER0R0dHd3T28g5IkSZKkMaJuATEiXgfcQOUq3jlluBeYUrPpFGDjDupTgN7MzF2YW1sfkJnXZOb8zJzf2to65GOSJEmSpLGkLgGxXPG7lsrLYhZm5tZSWk3lBTT9200EDi7j29XL39W1WTXPFNbWq/c9C9gXWFOHQ5IkSZKkMadeVxC/BRwKnJiZW6rG7wQOi4iFEdECXAysLLefAlwPnBcRMyLiQOB84DqAzFwDrAAuiYiWiPgglTed3l7m3gicGBFHl+B5KXBHzTOLkiRJkqQhqsd3EA+i8mmKecDzEdFbltMzs5vKW0cvB9YDRwGLqqZfDdxN5e2kq4B7y1i/RcD8MvfLwClln2TmauBTVILir6k8e3j2SI9HkiRJksaqcSPdQWauA2In9QeAQ3ZQS+ALZRms3gks2Mm+bwJuGnq3kiRJkqQdqftnLiRJkiRJzcmAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCDIiSJEmSpMKAKEmSJEkCmjwgRsT+EXFnRGyKiHURcVqje5IkSZKkZjWu0Q2M0FXAy8ABwDzg3oh4NDNXN7YtSZIkSWo+TXsFMSImAguBizKzNzP/Bfh74IzGdiZJkiRJzalpAyIwG3g1M9dUjT0KzGlQP5IkSZLU1CIzG93DLomIo4FbM/ONVWOfAE7PzAU12y4BlpTV3wV+vqf6bCLTgRca3YSagueKhsPzRUPluaLh8HzRUHmuDO6gzGwdrNDMzyD2AlNqxqYAG2s3zMxrgGv2RFPNKiI6MnN+o/vQ6Oe5ouHwfNFQea5oODxfNFSeK8PXzLeYrgHGRcSbq8bmAr6gRpIkSZJ2QdMGxMzcBNwBXBoREyPi94D3Azc0tjNJkiRJak5NGxCLs4EJwK+B5cCn/cTFLvMWXA2V54qGw/NFQ+W5ouHwfNFQea4MU9O+pEaSJEmSVF/NfgVRkiRJklQnBkRJkiRJEmBAlCRJkiQVBkRJkiRJEmBAlCRJkiQVBkRJkiRJEmBAlCRJkiQVBkRJkiRJEmBAlCRJkiQVBkRJkiRJEmBAlCRJkiQVBkRJkkYoIjoj4uWImF4zviIiMiLaI6ItIm6PiBciYkNEPBYRZ5bt2st2vTXLhxtyQJKkMWtcoxuQJGkv8TRwKvDXABFxODChqn4D8ChwEPAScDjwxpp9vCEzX9n9rUqSNDivIEqSVB83AB+pWl8MXF+1fiRwXWZuysxXMvORzPzBHu1QkqTXMCYDYkScExEdEfFSRFxXr3kR8e6IeCIiNkfEjyLioHr2LUka1X4CTImIQyNiH+DDwPdq6ldFxKKIeFNDOpQk6TWMyYAI/BL4C+Bv6zWvPHdyB3ARsD/QAdwysjYlSU2m/yriscATwLNVtQ8BP6by78TT5fnEI2vmvxARL1Yth+6RriVJKsZkQMzMOzLzLqCnthYRJ5R/tF+MiP8dEUcMZR5wMrA6M2/NzD5gKTA3Ig7ZTYchSRp9bgBOA85k29tLycz1mfnFzJwDHACsAO6KiKjabHpmvqFqeXxPNS5JEozRgLgjEfE2KlcHPwlMA64G/j4i9h3C9DlUXj4AQGZuAtaWcUnSGJCZ66i8rOZ4KneV7Gi7F4CvAQdSuetEkqRRwYC4rU8AV2fmTzPz1cz8LpU3zb1jCHMnARtqxjYAk+vcoyRpdPsY8AflPxQOiIgrIuKwiBgXEZOBTwNPZuZgd6VIktQQBsRtHQScX/38B/AfqPwX3tfSC0ypGZsCbKxzj5KkUSwz12ZmxyCl3wHuBF4EnqLyb85JNdu8WPMdxPN2c7uSJG3D7yBu6xfA5Zl5+S7MXU3lleYARMRE4OAyLknai2Vm+w7GXwH6nzH8s53M76zaTpKkhhmTVxDL7T0twD7APhHREhHjgL8BPhURR0XFxIj4o3Ir0M7mQeW/Ch8WEQvLNhcDKzPziT1/hJIkSZI0fGMyIAJfArYAXwT+pPz9pXJL0CeAbwDrgSepvIlup/MAMrMbWAhcXuYeBSza/YciSZIkSfURmdnoHiRJkiRJo8BYvYIoSZIkSaphQJQkSZIkAWPwLabTp0/P9vb2RrchSZIkSQ3x8MMPv5CZrYPVxlxAbG9vp6NjsM9TSZIkSdLeLyLW7ajmLaaSJEmSJMCAKEmSJEkqDIiSJEmSJGAMPoM4mK1bt9LV1UVfX1+jW9ktWlpaaGtrY/z48Y1uRZIkSdIoZkAEurq6mDx5Mu3t7UREo9upq8ykp6eHrq4uZs6c2eh2JEmSJI1i3mIK9PX1MW3atL0uHAJEBNOmTdtrr45KkiRJqh+vIBZ7Yzjstzcf25ixdGqjOxidlm5odAejk+fL4DxfJEl6TV5BHCUigjPOOGNg/ZVXXqG1tZUTTjgBgF/96leccMIJzJ07l7e85S0cf/zxAHR2djJhwgTmzZs3sFx//fUNOQZJkiRJzc0riIOp9399H8J/tZ44cSKrVq1iy5YtTJgwgfvvv58ZM2YM1C+++GKOPfZYPvvZzwKwcuXKgdrBBx/MihUr6tuzJEmSpDHHK4ijyHHHHce9994LwPLlyzn11FMHas899xxtbW0D60ccccQe70+SJEnS3s2AOIosWrSIm2++mb6+PlauXMlRRx01UPvTP/1TPvaxj3HMMcdw+eWX88tf/nKgtnbt2m1uMf3xj3/ciPYlSZIkNTlvMR1FjjjiCDo7O1m+fPnAM4b93vve9/LUU09x33338YMf/IC3vvWtrFq1CvAWU0mSJEn14RXEUeakk07iggsu2Ob20n77778/p512GjfccANHHnkkDz30UAM6lCRJkrS3MiCOMmeddRYXX3wxhx9++Dbj//RP/8TmzZsB2LhxI2vXruVNb3pTI1qUJEmStJfyFtNRpq2tbeBNpdUefvhhzjnnHMaNG8dvf/tbPv7xj3PkkUfS2dk58Axiv7POOovPfOYze7JtSZIkSXsBA+JgGvAx5d7e3u3GFixYwIIFCwD4/Oc/z+c///nttmlvb2fLli27uz1JkiRJY4C3mEqSJEmSgL0gIEbEooh4PCI2RcTaiDi60T1JkiRJUjNq6ltMI+JY4Argw8D/Bf59YzuSJEmSpObV1AER+HPg0sz8SVl/dld3lJlERH26GmUys9EtSJIkSWoCTXuLaUTsA8wHWiPiyYjoiohvRMSE4e6rpaWFnp6evTJIZSY9PT20tLQ0uhVJkiRJo1wzX0E8ABgPnAIcDWwF/g74EnBh9YYRsQRYAgz67cC2tja6urro7u7ezS03RktLC21tbY1uQ5IkSdIo18wBsf/bDn+dmc8BRMRfMUhAzMxrgGsA5s+fv91lwvHjxzNz5szd260kSZIkjXJNe4tpZq4HuoC9775QSZIkSWqApg2IxXeAP4uIfxcR+wGfA+5pcE+SJEmS1JSa+RZTgMuA6cAaoA/4PnB5QzuSJEmSpCbV1AExM7cCZ5dFkiRJkjQCzX6LqSRJkiSpTgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiTAgChJkiRJKgyIkiRJkiRgLwmIEfHmiOiLiO81uhdJkiRJalZ7RUAErgL+tdFNSJIkSVIza/qAGBGLgBeBHza6F0mSJElqZk0dECNiCnApcH6je5EkSZKkZtfUARG4DLg2M3+xs40iYklEdERER3d39x5qTZIkSZKaS9MGxIiYB7wHuPK1ts3MazJzfmbOb21t3f3NSZIkSVITGtfoBkZgAdAOPBMRAJOAfSLiLZn5tgb2JUmSJElNqZkD4jXAzVXrF1AJjJ9uSDeSJEmS1OSaNiBm5mZgc/96RPQCfZnpQ4aSJEmStAuaNiDWysylje5BkiRJkppZ076kRpIkSZJUXwZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFU0bECNi34i4NiLWRcTGiHgkIo5rdF+SJEmS1KyaNiAC44BfAO8CpgIXAd+PiPYG9iRJkiRJTWtcoxvYVZm5CVhaNXRPRDwNvB3obERPkiRJktTMmvkK4jYi4gBgNrC60b1IkiRJUjPaKwJiRIwHbgS+m5lPDFJfEhEdEdHR3d295xuUJEmSpCbQ9AExIl4H3AC8DJwz2DaZeU1mzs/M+a2trXu0P0mSJElqFk37DCJARARwLXAAcHxmbm1wS5IkSZLUtJo6IALfAg4F3pOZWxrdjCRJkiQ1s6a9xTQiDgI+CcwDno+I3rKc3uDWJEmSJKkpNe0VxMxcB0Sj+5AkSZKkvUXTXkGUJEmSJNWXAVGSJEmSBBgQJUmSJEmFAVGSJEmSBBgQJUmSJEmFAVGSJEmSBBgQJUmSJEmFAVGSJEmSBBgQJUmSJEmFAVGSJEmSBBgQJUmSJEmFAVGSJEmSBMC4RjcgSZKkJrB0aqM7GN4rIM0AACAASURBVJ2Wbmh0B1JdeQVRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgQYECVJkiRJhQFRkiRJkgTAuEY3IEmSJGkvsnRqozsYnZZuaHQHQ+IVREmSJEkSYECUJEmSJBUGREmSJEkS4DOIjeX92YNrkvuzJanp+e/Q4Px3SNIY5hVESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRLQ5AExIvaPiDsjYlNErIuI0xrdkyRJkiQ1q2b/zMVVwMvAAcA84N6IeDQzVze2LUmSJElqPk17BTEiJgILgYsyszcz/wX4e+CMxnYmSZIkSc2paQMiMBt4NTPXVI09CsxpUD+SJEmS1NQiMxvdwy6JiKOBWzPzjVVjnwBOz8wFNdsuAZaU1d8Ffr6n+mwi04EXGt2EmoLniobD80VD5bmi4fB80VB5rgzuoMxsHazQzM8g9gJTasamABtrN8zMa4Br9kRTzSoiOjJzfqP70OjnuaLh8HzRUHmuaDg8XzRUnivD18y3mK4BxkXEm6vG5gK+oEaSJEmSdkHTBsTM3ATcAVwaERMj4veA9wM3NLYzSZIkSWpOTRsQi7OBCcCvgeXAp/3ExS7zFlwNleeKhsPzRUPluaLh8HzRUHmuDFPTvqRGkiRJklRfzX4FUZIkSZJUJwZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZIkSRJgQJQkSZIkFQZESZKGKSI6I2JLRPRGxPMRcV1ETCq16yIiI+Kkmjn/vYyfWdZfHxHLIqKr7OfpiLhyB7/Rv3xjjx6oJGnMMSBKkrRrTszMScA84K3Af62qrQEW969ExDjgQ8Daqm3+KzAf+E/AZOAY4JHBfqNqOaf+hyFJ0r8Z1+gGJElqZpn5fET8A5Wg2O9u4E8iYr/MXA+8D1hJJQj2OxK4MzN/WdY7yyJJUsN4BVGSpBGIiDbgOODJquE+4O+BRWX9I8D1NVN/ApwXEWdHxOEREbu9WUmSXoMBUZKkXXNXRGwEfgH8Grikpn498JGImAq8C7irpv6XwBXA6UAH8GxELK7Z5q6IeLFq+UTdj0KSpCoGREmSds0HMnMysAA4BJheXczMfwFagS8B92Tmlpr6q5l5VWb+HvAG4HLgbyPi0JrfeEPV8je78XgkSTIgSpI0Epn5z8B1wNcGKX8POJ/tby+t3ceWzLwKWA+8pd49SpI0VL6kRpKkkfvvQGdEzKsZ/zrwY+Ch2gkR8TlgBfBTYCuVW00ns/2bTCVJ2mMMiJIkjVBmdkfE9cBFwMaq8d8AP9zBtC3AMuA/Aknl0xgLM/Opqm3ujohXq9bvz8wP1rV5SZKqRGY2ugdJkiRJ0ijgM4iSJEmSJMCAKEmSJEkqDIiSJEmSJMCAKEmSJEkqDIiSJEmSJGAMfuZi+vTp2d7e3ug2JEmSJKkhHn744Rcys3Ww2pgLiO3t7XR0dDS6DUmSJElqiIhYt6Oat5hKkiRJkgADoiRJkiSpMCBKkiRJkoAx+AyiJEmSpLFj69atdHV10dfX1+hW9riWlhba2toYP378kOcYECVJkiTttbq6upg8eTLt7e1ERKPb2WMyk56eHrq6upg5c+aQ53mLqSRJkqS9Vl9fH9OmTRtT4RAgIpg2bdqwr5y+5hXEiNgX+CbwHmB/4Engv2XmDyKiHXga2FQ15YrMvKzMDeDLwMdL7Vrgv2Rmlno78B3gKOAZ4JzMfKDqt08D/hKYDtwPnJWZv6nq61vAKcBm4CuZ+VfDOnqpSRz+3cMb3cKo9Njixxrdwqjk+TI4zxdJGrvGWjjstyvHPZQriOOAXwDvAqYCFwHfL+Gu3xsyc1JZLqsaXwJ8AJgLHAGcAHyyqr4ceASYBlwI3BYRreVg5gBXA2cAB1AJgd+smrsUeDNwEHAM8IWIeN8QjkeSJEmS9ph99tmHefPmcdhhh3HiiSfy4osvAtDZ2UlEcNFFFw1s+8ILLzB+/HjOOeccAH7+85+zYMEC5s2bx6GHHsqSJUsAePDBB5k6dSrz5s0bWB544IHtf3yYXvMKYmZuohLG+t0TEU8Dbwcefo3pi4FlmdkFEBHLgE8A346I2cDbgD/MzC3A7RHxOWAh8G3gdODuzHyozL0IeDwiJmfmRuAjwEczcz2wPiL+BjgTuG9IRy5JkiRpzKn3nTZDuUNlwoQJrFixAoDFixdz1VVXceGFFwIwa9Ys7rnnHi67rHKd7dZbb2XOnDkDcz/zmc9w7rnn8v73v7/ye4/92+8dffTR3HPPPXU7FtiFZxAj4gBgNrC6anhdRHRFxHciYnrV+Bzg0ar1R8tYf+2pEvZ2VB+Ym5lrgZeB2RGxH3DgTvYtSZIkSaPOO9/5Tp599tmB9QkTJnDooYfS0dEBwC233MIf//EfD9Sfe+452traBtYPP3z3PkoyrIAYEeOBG4HvZuYTwAvAkVRu83w7MLnU+00CNlStbwAmlWcTa2v99ck7mFtdn1S1Ptjc2r6XRERHRHR0d3e/1mFKkiRJUt29+uqr/PCHP+Skk07aZnzRokXcfPPNdHV1sc8++3DggQcO1M4991z+4A/+gOOOO44rr7xy4PZUgB//+Mfb3GK6du3aEfc45IAYEa8DbqByFe8cgMzszcyOzHwlM39Vxv8wIqaUab3AlKrdTAF6y0tqamv99Y07mFtd761aH2zuNjLzmsycn5nzW1tbh3S8kiRJklQPW7ZsYd68eUybNo3f/OY3HHvssdvU3/e+93H//fezfPlyPvzhD29T++hHP8rjjz/Ohz70IR588EHe8Y538NJLLwGVW0xXrFgxsBx88MEj7nVIAbFc8buWystiFmbm1h1smv1Tyv+upvKCmn5z+bdbU1cDsyJi8k7qA3MjYhawL7CmPHf43E72LUmSJEmjQv8ziOvWrePll1/mqquu2qb++te/nre//e0sW7aMhQsXbjf/wAMP5KyzzuLv/u7vGDduHKtWrdptvQ71CuK3gEOBE8sLZQCIiKMi4ncj4nURMQ34OvBgZvbf+nk9cF5EzIiIA4HzgesAMnMNsAK4JCJaIuKDVN50enuZeyNwYkQcHRETgUuBO6qeWbwe+FJE7BcRh1B5+c11u/D/gSRJkiTtdlOnTuXrX/86X/va19i6ddtrbueffz5XXHEF06ZN22b8vvvuG9j2+eefp6enhxkzZuy2Hl8zIEbEQVQ+TTEPeD4iestyOjCLyltDNwKrgJeAU6umXw3cDTxW6veWsX6LgPnAeirfSzwlM7sBMnM18CkqQfHXVJ4vPLtq7iXAWmAd8M/AVzPTN5hKkiRJGrXe+ta3MnfuXG6++eZtxufMmcPixYu32/4f//EfOeyww5g7dy7vfe97+epXv8ob3/hGYPtnEG+77bYR9xflm/Vjxvz587P/DUFSs/DD54Pzw+eD83wZnOeLJI1Njz/+OIceemij22iYwY4/Ih7OzPmDbT/sz1xIkiRJkvZOBkRJkiRJEmBAlCRJkiQVBkRJkiRJe7Wx9t6Vfrty3AZESZIkSXutlpYWenp6xlxIzEx6enpoaWkZ1rxxu6kfSZIkSWq4trY2urq66O7ubnQre1xLSwttbW3DmmNAlCRJkrTXGj9+PDNnzmx0G03DW0wlSZIkSYABUZIkSZJUGBAlSZIkSYABUZIkSZJUGBAlSZIkSYABUZIkSZJUGBAlSZIkSYABUZIkSZJUGBAlSZIkSYABUZIkSZJUGBAlSZIkSYABUZIkSZJUGBAlSZIkScAQAmJE7BsR10bEuojYGBGPRMRxVfV3R8QTEbE5In4UEQdV1SIiroiInrJ8JSKiqt5e5mwu+3hPzW+fVn53U0TcFRH71/T1txHx/yLi+Yg4b+T/d0iSJEnS2DWUK4jjgF8A7wKmAhcB3y/hbjpwRxnbH+gAbqmauwT4ADAXOAI4AfhkVX058AgwDbgQuC0iWgEiYg5wNXAGcACwGfhm1dylwJuBg4BjgC9ExPuGeNySJEmSpBqvGRAzc1NmLs3Mzsz8bWbeAzwNvB04GVidmbdmZh+V0DY3Ig4p0xcDyzKzKzOfBZYBZwJExGzgbcAlmbklM28HHgMWlrmnA3dn5kOZ2UslhJ4cEZNL/SPAZZm5PjMfB/6mf9+SJEmSpOEb9jOIEXEAMBtYDcwBHu2vZeYmYG0Zp7Ze/q6uPZWZG3dSr973WuBlYHZE7AccuJN9S5IkSZKGaVgBMSLGAzcC383MJ4BJwIaazTYA/Vf5ausbgEnlOcThzq2uT6paH2xubd9LIqIjIjq6u7t3fICSJEmSNIYNOSBGxOuAG6hcxTunDPcCU2o2nQJs3EF9CtCbmbkLc6vrvVXrg83dRmZek5nzM3N+a2vroMcnSZIkSWPdkAJiueJ3LZWXxSzMzK2ltJrKC2j6t5sIHFzGt6uXv6trs6qeKRysXr3vWcC+wJrMXA88t5N9S5IkSZKGaahXEL8FHAqcmJlbqsbvBA6LiIUR0QJcDKwst58CXA+cFxEzIuJA4HzgOoDMXAOsAC6JiJaI+CCVN53eXubeCJwYEUeX4HkpcEfVM4vXA1+KiP3KS3E+0b9vSZIkSdLwDeU7iAdR+TTFPOD5iOgty+mZ2U3lraOXA+uBo4BFVdOvBu6m8nbSVcC9ZazfImB+mftl4JSyTzJzNfApKkHx11SeLzy7au4lVF6Isw74Z+CrmXnfsI5ekiRJkjRg3GttkJnrgNhJ/QHgkB3UEvhCWQardwILdrLvm4CbdlB7CTirLJIkSZKkERr2Zy4kSZIkSXsnA6IkSZIkCTAgSpIkSZIKA6IkSZIkCTAgSpIkSZIKA6IkSZIkCTAgSpIkSZIKA6IkSZIkCTAgSpIkSZIKA6IkSZIkCTAgSpIkSZIKA6IkSZIkCTAgSpIkSZIKA6IkSZL0/9u79zDJqvLe498fjAIyjMNlggIyBhUxoBiFoEbiGEwiRgQBEwURvICXY84xongJyKioaOQ8iUZOkIRwEfDCLSJeoueoGONtEkUYRR5RRuSiIyJOwwAG3/PHXqWborunmumm6env53nqmar97rX3qq41u+rda629JQEmiJIkSZKkxgRRkiRJkgSYIEqSJEmSGhNESZIkSRJggihJkiRJakZKEJO8OsmKJHckOb23/OFJKslY73FcL54k705yU3u8J0mGyn8+yW1JrkzyjKH9HpJkVZJbk1yUZKtebJMkpyX5ZZIbk7x2vf4SkiRJkjTPjdqDeD1wAnDaBPHFVbWwPd7eW34UcACwO/A44NnAy3vxc4FvAlsDfwOcl2QJQJJdgVOAw4BtgduAk3tllwOPApYCTweOSfLMEd+PJEmSJGnISAliVV1QVRcBN01x+4cDJ1XVj6vqOuAk4AiAJDsDTwCOr6q1VXU+cDlwUCt7KHBxVV1aVWPAccCBSbZo8RcBb6+qm6vqu8Cpg21LkiRJkqZuuuYgrkry4yT/kmSb3vJdgct6ry9rywaxH1TVmknivylbVVcDdwI7J9kS2G6SbUuSJEmSpmh9E8SfAXvSDfN8IrAFcHYvvhC4pff6FmBhm4c4HBvEt5igbD++sPd6vLJ3k+SoNodyxerVq0d4W5IkSZI0/6xXglhVY1W1oqr+u6p+Arwa+NMki9oqY8CiXpFFwFhV1TixQXzNBGX78bHe6/HKDtfzg1W1R1XtsWTJktHfoCRJkiTNI9N9m4tq/w6uVLqS7gI1A7u3ZYPYTr05hePFf1M2yU7AJsBVVXUzcMMk25YkSZIkTdGot7lYkGRTYGNg4ySbtmV7JXl0ko2SbA28D/hCVQ2Gfp4JvDbJ9km2A44GTgeoqquAbwHHt+09l+5Kp+e3smcD+yXZO8nmwNuAC3pzFs8Ejk2yZZJdgCMH25YkSZIkTd2oPYjHAmuBNwIvbM+PBXYCPk03tPMK4A7gBb1ypwAX012d9ArgkrZs4PnAHsDNwInAwVW1GqCqVgKvoEsUf0o3v/BVvbLHA1cDq4AvAn9bVZ8e8f1IkiRJkoYsGGWlqlpOd9/B8Zw7SbkCjmmP8eLXAMsmKX8OcM4EsTuAl7SHJEmSJGk9TfccREmSJEnSHGWCKEmSJEkCTBAlSZIkSY0JoiRJkiQJMEGUJEmSJDUmiJIkSZIkwARRkiRJktSYIEqSJEmSABNESZIkSVJjgihJkiRJAkwQJUmSJEmNCaIkSZIkCTBBlCRJkiQ1JoiSJEmSJMAEUZIkSZLUmCBKkiRJkgATREmSJElSs2C2KyBJkqT7v8ee8djZrsL90uWHXz7bVZCmlT2IkiRJkiTABFGSJEmS1IyUICZ5dZIVSe5IcvpQbJ8kVya5LcnnkyztxZLk3Uluao/3JEkv/vBW5ra2jWcMbfuQJKuS3JrkoiRb9WKbJDktyS+T3Jjktff6ryBJkiRJGrkH8XrgBOC0/sIk2wAXAMcBWwErgI/0VjkKOADYHXgc8Gzg5b34ucA3ga2BvwHOS7KkbXtX4BTgMGBb4Dbg5F7Z5cCjgKXA04FjkjxzxPcjSZIkSRoyUoJYVRdU1UXATUOhA4GVVfWxqrqdLmnbPckuLX44cFJV/biqrgNOAo4ASLIz8ATg+KpaW1XnA5cDB7WyhwIXV9WlVTVGl4QemGSLFn8R8PaqurmqvgucOti2JEmSJGnq1ncO4q7AZYMXVXUrcHVbfo94e96P/aCq1kwS72/7auBOYOckWwLbTbJtSZIkSdIUrW+CuBC4ZWjZLcAWE8RvARa2eYhTLduPL+y9Hq/s3SQ5qs2hXLF69epJ35AkSZIkzVfrmyCOAYuGli0C1kwQXwSMVVXdi7L9+Fjv9Xhl76aqPlhVe1TVHkuWLJn0DUmSJEnSfLW+CeJKugvQAJBkc+ARbfk94u15P7ZTb07hePH+tncCNgGuqqqbgRsm2bYkSZIkaYpGvc3FgiSbAhsDGyfZNMkC4EJgtyQHtfhbgG9X1ZWt6JnAa5Nsn2Q74GjgdICqugr4FnB8295z6a50en4rezawX5K9W+L5NuCC3pzFM4Fjk2zZLopz5GDbkiRJkqSpG7UH8VhgLfBG4IXt+bFVtZruqqPvAG4G9gKe3yt3CnAx3dVJrwAuacsGng/s0cqeCBzctklVrQReQZco/pRufuGremWPp7sgzirgi8DfVtWnR3w/kiRJkqQhC0ZZqaqW093CYrzY54BdJogVcEx7jBe/Blg2yX7PAc6ZIHYH8JL2kCRJkiStp/WdgyhJkiRJ2kCYIEqSJEmSABNESZIkSVJjgihJkiRJAkwQJUmSJEmNCaIkSZIkCRjxNheSJEmSNIrHnvHY2a7C/dLlh18+21UYiT2IkiRJkiTABFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKEmSJEkCTBAlSZIkSY23uZhFXgJ4fHPlEsCSNNf5PTQ+v4ckzWf2IEqSJEmSABNESZIkSVJjgihJkiRJAkwQJUmSJEmNCaIkSZIkCZimBDHJF5LcnmSsPb7Xi+2T5MoktyX5fJKlvViSvDvJTe3xniTpxR/eytzWtvGMof0ekmRVkluTXJRkq+l4P5IkSZI0H01nD+Krq2phezwaIMk2wAXAccBWwArgI70yRwEHALsDjwOeDby8Fz8X+CawNfA3wHlJlrRt7wqcAhwGbAvcBpw8je9HkiRJkuaVmR5ieiCwsqo+VlW3A8uB3ZPs0uKHAydV1Y+r6jrgJOAIgCQ7A08Ajq+qtVV1PnA5cFAreyhwcVVdWlVjdEnogUm2mOH3JEmSJEkbpOlMEN+V5GdJvpxkWVu2K3DZYIWquhW4ui2/R7w978d+UFVrJon3t301cCew87S8G0mSJEmaZ6YrQXwDsBOwPfBB4OIkjwAWArcMrXsLMOjlG47fAixs8xCnWnY4/htJjkqyIsmK1atXT+V9SZIkSdK8MS0JYlV9rarWVNUdVXUG8GXgWcAYsGho9UXAoFdwOL4IGKuquhdlh+P9+n2wqvaoqj2WLFkytTcnSZIkSfPETM1BLCDASroL0ACQZHPgEW05w/H2vB/baWhO4XC8v+2dgE2Aq6btXUiSJEnSPLLeCWKSxUn+LMmmSRYkORT4I+AzwIXAbkkOSrIp8Bbg21V1ZSt+JvDaJNsn2Q44GjgdoKquAr4FHN+2/Vy6K52e38qeDeyXZO+WeL4NuGBozqIkSZIkaUQLpmEbDwBOAHYB7gKuBA6oqu8BJDkI+AfgQ8DXgOf3yp5CN3fx8vb6n9qygefTJYw3Az8CDq6q1QBVtTLJK+gSxa2BzwEvnob3I0mSJEnz0noniC1h23OS+OfoksfxYgUc0x7jxa8Blk2y7XOAc0avrSRJkiRpIjN9H0RJkiRJ0hxhgihJkiRJAkwQJUmSJEmNCaIkSZIkCTBBlCRJkiQ1JoiSJEmSJMAEUZIkSZLUmCBKkiRJkgATREmSJElSY4IoSZIkSQJMECVJkiRJjQmiJEmSJAkwQZQkSZIkNSaIkiRJkiTABFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKEmSJEkCTBAlSZIkSY0JoiRJkiQJmOMJYpKtklyY5NYkq5IcMtt1kiRJkqS5asFsV2A9fQC4E9gWeDxwSZLLqmrl7FZLkiRJkuaeOduDmGRz4CDguKoaq6p/Bz4OHDa7NZMkSZKkuWnOJojAzsBdVXVVb9llwK6zVB9JkiRJmtNSVbNdh3slyd7Ax6rqIb1lRwKHVtWyoXWPAo5qLx8NfO++quccsg3ws9muhOYE24qmwvaiUdlWNBW2F43KtjK+pVW1ZLzAXJ6DOAYsGlq2CFgzvGJVfRD44H1RqbkqyYqq2mO266H7P9uKpsL2olHZVjQVtheNyrYydXN5iOlVwIIkj+ot2x3wAjWSJEmSdC/M2QSxqm4FLgDelmTzJH8I7A+cNbs1kyRJkqS5ac4miM2rgM2AnwLnAq/0Fhf3mkNwNSrbiqbC9qJR2VY0FbYXjcq2MkVz9iI1kiRJkqTpNdd7ECVJkiRJ08QEURJJrknyjNmuh+7/bCuSpPujJMuTfGi267EhMEGcB5IckeTyJLcluTHJ/0myuMUm/M+U5KlJ/iPJLUl+nuTLSfa8b2uvqWo/4NcmGUvykyT/kmThDO1rWZJft32tSfK9JC+eiX1p+tlWNJH744mAJA9PUq0NjbU6vnG266WJDR1jbkxy+vocY5Ls3fv8bx1qD2NJdpzO+mt6THc7GHGfw8eLsSSXzeQ+x6lDJXnkfbnP6WKCuIFLcjTwbuD1wIOBJwFLgc8meeAk5RYBnwDeD2wFbA+8FbhjpuusabFfVS0EngDsCRw7g/u6vu1rEfDXwKlJHj2D+9P0sq1orlnc2tHBwHFJ/mS2K6RJDY4xjwd+H3jTvd1QVX2pqha27e3aFi8eLKuqHw3WTTKX7/W9IZq2djBF/fax+1QLz9d2ZIK4AWtJ3luBv6qqT1fVr6rqGuAv6JLEF05SfGeAqjq3qu6qqrVV9W9V9e0Zr7imTVVdB3wK2C3Jc5KsTPKLJF9I8pjh9ZM8pPU0b91b9sQkq5M8YB37qqr6JPBz4HGt7EZJ3pjk6iQ3Jflokq16235RklUtdtz9sddivrCtaF2SbJnkE+0zvrk936EXPyLJD1oP8Q+THNqWPzLJF9ONRvlZko/0yjwlyTda7BtJnjJqfapqBd29jx/f295Lkny31e8zSZb2Yn/aeq5vSXJyq9PL1vfvotFU1Y3AZ2ifV5InpRul9IsklyVZNlg3ye8mubS1pc8l+UDWMXQw3Yio85J8KMkvgSOSPDjJPye5Icl1SU5IsnGvzITtRTNjnHYwOO6vSfKdJM8drNuOKf+e5L3tM/phkn178d9t/4/XJPkssM0odUiyXZKPpxsd9/0kR/ZiU2pHEx3fklzaNnlZut7Lv1zPP919ygRxw/YUYFO6+0X+RlWN0f0QnOys61XAXUnOSLJvki1nrpqaKUkeBjwLWEN3K5jXAEuATwIXZ6gXuR24v0B3EmHghcCHq+pX69jXRkmeQ3eA/n5b/D+BA4CnAdsBNwMfaOv/HnAycCjwULoe7u3v5VvVerKtaAQbAf9Cd4JxR2At8A8ASTYH3gfsW1Vb0H3/fKuVezvwb8CWwA50I1NoJwAuaeW2Bv43cEl6Jx0mk+RJwG60NpTkAODNwIF0bfdLdG2ZJNsA59H1WmwNfK/VUfeRdjJhX+D7Sban++xPoBul9Drg/CRL2urnAF+n+6yWA4eNuJv96T7nxcDZwBnAfwOPpOu1+lPgZa0+E7YXzZx+O2iLrgb2pjuuvxX4UJKH9orsRff/dRvgPcA/J0mLnQP8Z4u9HTh8xGqcC/yY7rvmYOCdSfbpxUduR0xwfKuqP2rx3Vvv5W9OjM0JVeVjA33Q/Vi7cYLYicBn6Q68H5pgnccAp9P9J/pv4OPAtrP9vnys83O/BhgDfgGsovthfRzw0d46GwHXAct6ZZ7Rnv8l8OX2fGPgRuAPJtjXMuDXbV93AHcBr+nFvwvs03v9UOBXwALgLcC5vdiDgDsH9fBhW7GtzHrbmPTvS9cDcHN7vnn7bA8CNhta70y6+5DtMLT8MODrQ8u+Ahwxwf4eDlTbz9r2/L389pZdnwJeOtR2b6NLaF8EfKUXC3At8LLZ/ltvyI/eMWZN+7z+L92P7jcAZw2t+xm6H/g70v3meFAv9iGGfqv02sOC9no5cGkvvm071mzWW/YC4PPrai+z/Xfb0B4TtYMJ1v0WsH97fgTw/V7sQa38Q3rtZPNe/JxBOxk6XgwerwMeRvf9s0Wv3LuA0+9lOxr3+NZiBTxytv/+9+ZhD+KG7WfANhl//PRDW3xCVfXdqjqi/ACOCgAACZpJREFUqnagO0u7HfB3019NzYADqmpxVS2tqlfRfXarBsGq+jXdj6PxemH+Ffi9JDvR9TLfUlVfT7JjepO9e+tfX1WL6eaVvQ/4415sKXBhG0L0C7ok4C66A+52rQ6DOt0G3LT+b11TZFvRSJI8KMkp6Yb6/hK4FFicZOOqupXuhMErgBuSXJJkl1b0GLqE7Ovphi6/pC2/W1trVtHaWia++Mg2wEK6H3vLgMGQ5qXA3/fa0M/bfrfnnm2o6E5+auYdUF2v8jJgF7rPbynwvMFn1T6vp9L9NtkO+Hn7fz5wLaPpr7eUrm3c0NvHKcDv9OITtRdNv/HawWD6wLd6n8Nu3H2o6I2DJ702sZA20qQdewaGjycA27TvuMVV9V5+277WDJXrf+5TaUcTHd/mNBPEDdtX6M56HNhf2IYC7Ut3BmckVXUlXW/ibtNYP913rqc7yAHQhmc8jK5n6G6q6nbgo3TD+Q4DzmrLf1S/neh9j6uPVdUddGeFH9uG7kB3kN23d3BeXFWbVjff7Qa64RiDOm1GN5xIs8u2ookcDTwa2KuqFgGDIVQBqKrPVNWf0P3IvxI4tS2/saqOrKrtgJcDJ6e7st/d2lqzI62t9dtQ9S4+0mJ3VdVJwO3Aq9ria4GXD7WhzarqP7hnG0r/tWZeVX2R7nfEe+k+q7OGPqvNq+pEus9qqyQP6hV/2Ki76T2/lu43UD9BWFRVu/biE7UXzZB+O0g35/NU4NXA1u0E4hW0Y8o63ABs2X7TDoxyFdvr6drXFkPl+t9xI7ejSY5vc5oJ4gasqm6hG8/9/iTPTPKAJA8HPkZ35vSstupGSTbtPTZJskuSo9tY8cH8pBcAX73v34mmwUeBP0+yT7oLiBxNd8Cb6IvwTLqhHc+hG9ozkqq6EziJbkggwD8C72hfAiRZkmT/FjsP2C/dRSoeSNdWR/lS0MyyrWjgAf3vBro5NmuBX7T5g8cPVkyybbqLG21O117G6HqASfK8/PZiNjfT/fi6i25+685JDkmyIN1FHH6P7graozoROKbV7x+BNyXZte33wUme19a7hHZCoo2q+R90w9R03/o7utEG/073f/rPkmzc2tiyJDtU1SpgBbA8yQOTPBnYb6o7qqob6OaGnZRkUbq5z49I8rS2ymTtRTNr0A62pzserAZId+ujkToieu3kra2dPJUR2klVXUv3ffau1u4eB7yUbq7heOtP2o4mOb4B/ATYaZT3c39jgriBq6r30E3Cfi/wS+BrdGdD9mln8aFL/Nb2HlfTjRPfC/haklvpEsMr6H4sao6pqu/RzUl9P93Q4v3oLjl95wTrf5luvth/VXfl26k4DdgxyX7A39PNXf23JGvo2tFebR8rgb8CPkx3JnAN8FO8lcqssq2o55Pc/bthMbAZXbv4KvDp3rob0X0/XE83VO9p/LZnb0+675Ixus/4f1XVD6vqJuDZrdxNdEO1nl1Vk05/GHIJ3Y+yI6vqQrrbOn24DYG9gm60DG2bz6O7yMVNdInoCmxD96mqWk13Uuk1dBcCeTNdcnAt3e24Br9LDwWeTPdZnQB8hHv3Wb0IeCDwHbp2ch5dDzeTtRfNrF47OJruROFX6JKpxwJfnsKmDqH7nvg53QmrM0cs9wK6OYrXAxcCx1fVZydZf8J2xATHtxZbDpzRhqb+BXPIYGK3JN1Nkv8HnFNV/3Qf7W8h3STyR/UOrpoDbCuaa5JsRDeS5tCq+vxs10eTS3frgCur6vh1rixpvdmDKOkekuxJd+P0Gb0sc5L90l34YnO6Xu7L6a52pjnCtqK5og1nXJxkE7qeq+C0ifulJHu2YXwbJXkmXW/jRbNdL2m+MEGUdDdJzgA+R3cLgjXrWn897U83xON64FHA88thDXOGbUVzzJPpplAMhk4fUFVrZ7dKmsBD6O6zOkZ3xeNXVtU3Z7VG0jziEFNJkiRJEmAPoiRJkiSpMUGUJEmSJAEmiJIkSZKkxgRRkqSeJJXk4NmuhyRJs8EEUZI07yT5/SR3JZnKTZmnsv1lLdG8MsmCodg1SV43E/uVJGl9mSBKkuajI4GTgd2SPGYG97MUeOkMbl+SpGllgihJmleSbAYcApwKnMc6ErgkeyX5ryS3J/lmkme13sFlI+zufcDyJJtPsv0XJvlGkjVJfprkY0m278UHvZH7JvnPJGuTfCnJDkmeluSyJGNJPpFk66FtvzjJd1rdr0ry10n87pckTcgvCUnSfHMwsKqqvg2cBbwoyQPGWzHJQuATwJXAE4FjgL+dwr7eD/wKeO0k6zwQOB7YHXg2sA1w7jjrvRV4DbAXsCXwEeAtwFHAMmBXYHmv7kcC72zrPAY4GngD8Kop1F+SNM+YIEqS5puX0SWGAF8EbgOeM8G6hwIbAy+tqpVV9VngHVPY1+3AccDrkywZb4WqOq2qPllVP6iqrwOvBPZOssPQqsdV1ZdaYvuPwFOA11fV16pqBXAG8PT++sAxVXVeVf2wqi4GTsQEUZI0CRNESdK8keSRwB8C5wBUVQFn0yWN49kFuKKq1vaWfW1omyvbEM+xJJ8aZxtnAdfQJWzj1ekJSf41yaoka4AVLbTj0Krf7j3/Sfv38qFlv9O2uQR4GHBKr25jdAniIyZ4r5IksWDdq0iStMF4GV2P4I+SDJYFIMnDquraofUD1Dq2+SxgMER17XCwqn6d5I3ARUn+/m4b7+Ymfgb4HHAY8FO6IaZfoht62ver/mbbtoeXDU78Dv59BfAf66i/JEm/YYIoSZoX2u0mDgfeRDevsO8s4MXA24aWf5dujuJmvV7EP+ivUFWr1rXvqvpku6XG8PDUXegSwjdX1Q9bPQ8c4e2sa38/SXId8IiqOnN9tydJmj9MECVJ88Wf0yVjp1bVTf1Akg8Dr0xywlCZs4ETgFOTvBPYDnhzi62rZ3HYMcBXuXtP4I+AO4BXJ/kA3cVk3j7F7U5kOfD+JL8APknXy/kEYPuqetc07UOStIFxDqIkab54KfD54eSw+RjdPQuf0V9YVWPAfnRXCP0m3RVMl7fw7VPZeVV9g+62Gpv0lq2m69U8APgO3dVMJ7vi6VT290/AS+iGrl5GN2z1KOCH07F9SdKGKd38fEmSNIok+wMXAr9TVT+b7fpIkjSdHGIqSdIkkhwO/AC4FtgN+DvgYpNDSdKGyARRkqTJbUt3k/qHAjcCl9DdcF6SpA2OQ0wlSZIkSYAXqZEkSZIkNSaIkiRJkiTABFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKEmSJEkC4P8DcbmveqwnzWcAAAAASUVORK5CYII=
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
<h2 id="Ohrfeige-Funktion">Ohrfeige-Funktion<a class="anchor-link" href="#Ohrfeige-Funktion">&#182;</a></h2><p>Mit der nachfolgenden Funktion versuchen wir</p>

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
<h1 id="Fine-Tuning"><a href="">Fine-Tuning</a><a class="anchor-link" href="#Fine-Tuning">&#182;</a></h1>
</div>
</div>
</div>
 

