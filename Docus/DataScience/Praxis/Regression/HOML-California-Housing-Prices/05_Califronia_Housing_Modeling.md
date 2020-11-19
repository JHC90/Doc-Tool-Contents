'''''

{
"title": "Data-Preprocessing-Checklist",
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;OLS&quot;</span><span class="p">,</span> <span class="n">lin_mae</span><span class="p">,</span> <span class="n">lin_mse</span><span class="p">,</span> <span class="n">lin_rmse</span><span class="p">]</span>
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
<div class="prompt input_prompt">In&nbsp;[13]:</div>
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
<div class="prompt input_prompt">In&nbsp;[14]:</div>
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

    <div class="prompt output_prompt">Out[14]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Lasso(alpha=0.01)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
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
<div class="prompt input_prompt">In&nbsp;[16]:</div>
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
<div class="prompt input_prompt">In&nbsp;[17]:</div>
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
<div class="prompt input_prompt">In&nbsp;[18]:</div>
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
<span class="nb">print</span><span class="p">(</span><span class="n">tree_mae</span><span class="p">)</span>
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
75607.39583333333
110805.96464333593
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;RegTree&quot;</span><span class="p">,</span> <span class="n">tree_mae</span><span class="p">,</span> <span class="n">tree_mae</span><span class="p">,</span> <span class="n">tree_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
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
<div class="prompt input_prompt">In&nbsp;[20]:</div>
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
<pre>&lt;ipython-input-20-6bfaa24301ce&gt;:4: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  forest_reg.fit(train_set, train_labels)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>RandomForestRegressor()</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">forest_prediction</span> <span class="o">=</span> <span class="n">forest_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>

<span class="n">RF_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">forest_prediction</span><span class="p">)</span>
<span class="n">RF_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">forest_prediction</span><span class="p">)</span>
<span class="n">RF_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">RF_mse</span><span class="p">)</span>


<span class="nb">print</span><span class="p">(</span><span class="n">RF_mae</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RF_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RF_rmse</span><span class="p">)</span>

<span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;RandForest&quot;</span><span class="p">,</span> <span class="n">RF_mae</span><span class="p">,</span> <span class="n">RF_mse</span><span class="p">,</span> <span class="n">RF_rmse</span><span class="p">]</span>
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
<div class="prompt input_prompt">In&nbsp;[22]:</div>
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
<pre>[[&#39;OLS&#39;, 49483.498062015504, 4462015589.36531, 66798.32025856122], [&#39;Poly-Reg&#39;, 80954.39569223936, 66653273599.85989, 258172.95288209393], [&#39;Lasso-Reg&#39;, 49458.05475606995, 4461389041.578401, 66793.63024704078], [&#39;RegTree&#39;, 75607.39583333333, 75607.39583333333, 110805.96464333593], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655]]
5
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
Lasso-Reg   49458.054756  4.461389e+09   66793.630247
RegTree     75607.395833  7.560740e+04  110805.964643
RandForest  56528.563830  6.167941e+09   78536.239897
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">maeDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;MAE&quot;</span><span class="p">]</span>
<span class="n">mseDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;MSE&quot;</span><span class="p">]</span>
<span class="n">rmseDF</span> <span class="o">=</span> <span class="n">performanceDF</span><span class="p">[</span><span class="s2">&quot;RMSE&quot;</span><span class="p">]</span>
<span class="n">maeDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[24]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x20c46579d90&gt;</pre>
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
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mseDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x20c4664e1c0&gt;</pre>
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
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">rmseDF</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x20c52e9f160&gt;</pre>
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
 

