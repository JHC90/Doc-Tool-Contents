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

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># FeatureImportance</span>
<span class="n">importance</span> <span class="o">=</span> <span class="n">lin_reg</span><span class="o">.</span><span class="n">coef_</span>
<span class="n">featureImportance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">importance</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">feature</span> <span class="o">=</span> <span class="n">train_set</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">specificImportance</span> <span class="o">=</span> <span class="n">importance</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">]</span>
    <span class="n">featureImportance</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">feature</span><span class="p">,</span> <span class="n">specificImportance</span><span class="p">])</span>
    <span class="c1">#print(feature, specificImportance)   </span>
<span class="nb">print</span><span class="p">(</span><span class="n">featureImportance</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[&#39;longitude&#39;, -54351.712905772016], [&#39;latitude&#39;, -55446.55764966471], [&#39;housing_median_age&#39;, 14484.399545536615], [&#39;total_rooms&#39;, -3990.6352368220223], [&#39;total_bedrooms&#39;, 9130.301566577078], [&#39;population&#39;, -44812.96023385288], [&#39;households&#39;, 44533.861471022545], [&#39;median_income&#39;, 63511.40207034306], [&#39;ocean_proximity&#39;, 14202.986271291938], [&#39;income_cat&#39;, 6427.979250867132], [&#39;rooms_per_household&#39;, 975.6353415798012], [&#39;population_per_household&#39;, 10600.000703069374], [&#39;ocean_proximity_&lt;1H OCEAN&#39;, 3.973830549219377e+17], [&#39;ocean_proximity_INLAND&#39;, 3.9738305492190163e+17], [&#39;ocean_proximity_ISLAND&#39;, 3.9738305492207443e+17], [&#39;ocean_proximity_NEAR BAY&#39;, 3.9738305492193325e+17], [&#39;ocean_proximity_NEAR OCEAN&#39;, 3.973830549219421e+17]]
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
<div class="prompt input_prompt">In&nbsp;[8]:</div>
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
<div class="prompt input_prompt">In&nbsp;[9]:</div>
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
<div class="prompt input_prompt">In&nbsp;[10]:</div>
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
<div class="prompt input_prompt">In&nbsp;[11]:</div>
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
<div class="prompt input_prompt">In&nbsp;[12]:</div>
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
<div class="prompt input_prompt">In&nbsp;[13]:</div>
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
<div class="prompt input_prompt">In&nbsp;[14]:</div>
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
<div class="prompt input_prompt">In&nbsp;[15]:</div>
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
<div class="prompt input_prompt">In&nbsp;[16]:</div>
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

    <div class="prompt output_prompt">Out[16]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Lasso(alpha=0.01)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
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
<div class="prompt input_prompt">In&nbsp;[18]:</div>
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
<div class="prompt input_prompt">In&nbsp;[19]:</div>
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
<div class="prompt input_prompt">In&nbsp;[20]:</div>
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
<div class="prompt input_prompt">In&nbsp;[21]:</div>
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
<div class="prompt input_prompt">In&nbsp;[22]:</div>
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
<div class="prompt input_prompt">In&nbsp;[23]:</div>
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
<pre>&lt;ipython-input-23-6bfaa24301ce&gt;:4: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  forest_reg.fit(train_set, train_labels)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>RandomForestRegressor()</pre>
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
<div class="prompt input_prompt">In&nbsp;[34]:</div>
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Suport-Vector-Regressor">Suport Vector Regressor<a class="anchor-link" href="#Suport-Vector-Regressor">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">svm</span>
<span class="n">svm</span> <span class="o">=</span> <span class="n">svm</span><span class="o">.</span><span class="n">SVC</span><span class="p">(</span><span class="n">kernel</span><span class="o">=</span><span class="s1">&#39;linear&#39;</span><span class="p">)</span>
<span class="n">svm</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[47]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>SVC(kernel=&#39;linear&#39;)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">svm_prediction</span> <span class="o">=</span> <span class="n">svm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_set</span><span class="p">)</span>

<span class="n">svm_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">svm_prediction</span><span class="p">)</span>
<span class="n">svm_mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">test_labels</span><span class="p">,</span> <span class="n">svm_prediction</span><span class="p">)</span>
<span class="n">svm_rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">RF_mse</span><span class="p">)</span>


<span class="nb">print</span><span class="p">(</span><span class="n">svm_mae</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">svm_mse</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">svm_rmse</span><span class="p">)</span>

<span class="n">importance</span> <span class="o">=</span> <span class="n">svm</span><span class="o">.</span><span class="n">coef_</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">listEnty</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;SVM&quot;</span><span class="p">,</span> <span class="n">svm_mae</span><span class="p">,</span> <span class="n">svm_mse</span><span class="p">,</span> <span class="n">svm_rmse</span><span class="p">]</span>
<span class="n">resultList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">listEnty</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Print-Results">Print-Results<a class="anchor-link" href="#Print-Results">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
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
<pre>[[&#39;OLS&#39;, 49483.498062015504, 4462015589.36531, 66798.32025856122], [&#39;Poly-Reg&#39;, 49458.03301952227, 4461384770.505101, 66793.59827487289], [&#39;Poly-Reg&#39;, 49458.03301952227, 4461384770.505101, 66793.59827487289], [&#39;Lasso-Reg&#39;, 49458.05475606995, 4461389041.578401, 66793.63024704078], [&#39;RegTree&#39;, 75607.39583333333, 12277961800.540213, 110805.96464333593], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655]]
6
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
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
Poly-Reg    49458.033020  4.461385e+09   66793.598275
Poly-Reg    49458.033020  4.461385e+09   66793.598275
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
<div class="prompt input_prompt">In&nbsp;[28]:</div>
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

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x1f4b273f670&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4gAAAJkCAYAAABTQQ+DAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzde5TfdX3v++drM6mT5oKS5NAD2TCBIwUDJLZho8vSguhCKDeN1gDFILZRKfXKat1HLinqUazUvazUDW09CGqgyKUilRZbLdrd2j1UbjlglsGJHRQNEdIkJHLxff6Y76S//JiQmcxkfpOZ52Ot72K+n8v39/6u9V2L9crne0lVIUmSJEnSf+l0AZIkSZKkicGAKEmSJEkCDIiSJEmSpIYBUZIkSZIEGBAlSZIkSQ0DoiRJkiQJMCBKkiRJkhoGREmSRilJX5Knk8xta783SSXpaWlb2bT9t7ax5yV5Lsnmtu2A8TkLSZIMiJIkjZXvA2cN7iQ5CpjeOiBJgHOBnwLLhzjGP1fVzLbth3uyaEmSWhkQJUkaG9cDb2nZXw5c1zbmOOAA4N3AsiS/ME61SZI0LAZESZLGxr8As5MckWQf4M3A59vGLAduB25s9k8dx/okSdolA6IkSWNncBXxtcDDwKODHUl+EXgT8MWqegb4Es+/zfQVSZ5s2daOU92SJAHQ1ekCJEmaRK4H7gYW8PzbS18PPAv8TbP/BeBrSeZV1fqm7V+q6tfGpVJJkobgCqIkSWOkqtYx8LKaU4Bb2rqXAzOBHyR5DLgJmEbLi20kSeo0VxAlSRpbbwNeUlVbkgz+f/ZA4ETgZOD+lrHvYSA4fmp8S5QkaWgGREmSxlBVDfXc4HHAvVX1d62NST4FvD/JkU3TK5Nsbpt7QlX97z1QqiRJz5Oq6nQNkiRJkqQJwGcQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBU/AzF3Pnzq2enp5OlyFJkiRJHXHPPfc8XlXzhuqbcgGxp6eH3t7eTpchSZIkSR2RZN3O+rzFVJIkSZIEGBAlSZIkSQ0DoiRJkiQJmILPIEqSJEnSM888Q39/P9u2bet0KXtMd3c38+fPZ9q0acOeY0CUJEmSNOX09/cza9Ysenp6SNLpcsZcVbFhwwb6+/tZsGDBsOd5i6kkSZKkKWfbtm3MmTNnUoZDgCTMmTNnxCukriBKkiRpl3o+cEenS5iQ+j72m50uQaMwWcPhoN05P1cQJUmSJKkDknDuuedu33/22WeZN28ep5566g7jzjjjDF75ylfu0LZy5UoOPPBAFi9evH178sknR12TK4iSJEmSpryxXiUfzuryjBkzePDBB9m6dSvTp0/nrrvu4sADD9xhzJNPPsm//du/MXPmTL7//e/v8Dzhe9/7Xi666KIxrdsVREmSJEnqkJNPPpk77hgIp6tWreKss87aof/mm2/mtNNOY9myZdxwww17vB4DoiRJkiR1yGDw27ZtG/fffz/HHnvsDv2DofGss85i1apVO/R98pOf3H576QknnDAm9XiLqSRJkiR1yNFHH01fXx+rVq3ilFNO2aHvxz/+Md/73vf4tV/7NZLQ1dXFgw8+yJFHHgl4i6kkSZIkTTqnn346F1100fNuL73xxht54oknWLBgAT09PfT19e3x20wNiJIkSZLUQeeffz6XXnopRx111A7tq1at4s4776Svr4++vj7uueceA6IkSZIkTWbz58/n3e9+9w5tfX19/OAHP+AVr3jF9rYFCxYwe/Zsvv3tbwM7PoO4ePFi+vr6Rl1LqmrUB9mbLFmypHp7eztdhiRJ0l5lrD8BMFkM51MGmpgeeughjjjiiE6XsccNdZ5J7qmqJUONdwVRkiRJkgQYECVJkiRJDQOiJEmSJAkwIEqSJEmaoib7+1h25/wMiJIkSZKmnO7ubjZs2DBpQ2JVsWHDBrq7u0c0r2sP1SNJkiRJE9b8+fPp7+9n/fr1nS5lj+nu7mb+/PkjmmNAlCRJkjTlTJs2jQULFnS6jAnHW0wlSZIkSYABUZIkSZLUMCBKkiRJkgADoiRJkiSpYUCUJEmSJAEGREmSJElSw4AoSZIkSQIMiJIkSZKkhgFRkiRJkgQYECVJkiRJjTELiEmWJXkoyZYka5Mc17SfmOThJE8l+XqSg1vmJMkVSTY028eTpKW/p5nzVHOM17T95tlJ1jW/eVuS/cbqfCRJkiRpqhmTgJjktcAVwFuBWcCvA48kmQvcAlwC7Af0Aje2TF0BnAksAo4GTgXe3tK/CvgOMAf4IPClJPOa31wIXA2cC+wPPAX82VicjyRJkiRNRWO1gvhHwOVV9S9V9fOqerSqHgXeAKyuqpuqahuwEliU5PBm3nLgyqrqb8ZfCZwHkOQw4FeAy6pqa1XdDDwALG3mngPcXlV3V9VmBkLoG5LMGqNzkiRJkqQpZdQBMck+wBJgXpLvJelP8ukk04GFwH2DY6tqC7C2aae9v/m7te+Rqtr0Av2tx14LPA0cNtpzkiRJkqSpaCxWEPcHpgFvBI4DFgMvBy4GZgIb28ZvZOA2VIbo3wjMbJ5DHOnc9v7tkqxI0pukd/369cM/M0mSJEmaQsYiIG5t/vunVfWjqnoc+BPgFGAzMLtt/GxgcFWwvX82sLmqajfmtvdvV1XXVNWSqloyb968YZ+YJEmSJE0low6IVfUE0A/UEN2rGXgBDQBJZgCHNu3P62/+bu07pO2Zwvb+1mMfArwIWLO75yJJkiRJU9lYvaTm/wV+P8n/keQlwHuArwC3AkcmWZqkG7gUuL+qHm7mXQe8L8mBSQ4A3g9cC1BVa4B7gcuSdCd5PQNvOr25mfsF4LQkxzXB83LglrZnFiVJkiRJw9Q1Rsf5EDCXgdW7bcBfAR+pqm1JlgKfBj4PfBtY1jLvauAQBt5OCvAXTdugZQwExieAHwBvrKr1AFW1Osk7GAiKc4CvMfCZDUmSJEnSbhiTgFhVzwAXNFt739eAw583aaCvgD9otqH6+4DjX+B3vwh8ccQFS5IkSZKeZ6xuMZUkSZIk7eXG6hZTSZIkSaLnA3d0uoQJqe9jv9npEobFFURJkiRJEmBAlCRJkiQ1DIiSJEmSJMCAKEmSJElqGBAlSZIkSYABUZIkSZLUMCBKkiRJkgADoiRJkiSpYUCUJEmSJAEGREmSJElSw4AoSZIkSQIMiJIkSZKkhgFRkiRJkgRAV6cLmMp6PnBHp0uYkPo+9pudLmHC8VoZmtfK0Lxehub18nxeK0PzWpE0lbmCKEmSJEkCDIiSJEmSpIYBUZIkSZIEGBAlSZIkSQ0DoiRJkiQJMCBKkiRJkhoGREmSJEkSYECUJEmSJDUMiJIkSZIkwIAoSZIkSWoYECVJkiRJgAFRkiRJktQwIEqSJEmSAAOiJEmSJKlhQJQkSZIkAWMYEJO8NMm2JJ9vaTsxycNJnkry9SQHt/QlyRVJNjTbx5Okpb+nmfNUc4zXtP3e2UnWJdmS5LYk+43VuUiSJEnSVDSWK4hXAf97cCfJXOAW4BJgP6AXuLFl/ArgTGARcDRwKvD2lv5VwHeAOcAHgS8lmdcceyFwNXAusD/wFPBnY3gukiRJkjTljElATLIMeBL4+5bmNwCrq+qmqtoGrAQWJTm86V8OXFlV/VX1KHAlcF5zvMOAXwEuq6qtVXUz8ACwtJl7DnB7Vd1dVZsZCKFvSDJrLM5HkiRJkqaiUQfEJLOBy4H3t3UtBO4b3KmqLcDapv15/c3frX2PVNWmF+hvPfZa4GngsNGciyRJkiRNZWOxgvgh4C+r6t/b2mcCG9vaNgKzdtK/EZjZPIc40rnt/TtIsiJJb5Le9evX7+J0JEmSJGlqGlVATLIYeA3wySG6NwOz29pmA5t20j8b2FxVtRtz2/t3UFXXVNWSqloyb968nZ+QJEmSJE1ho11BPB7oAX6Q5DHgImBpkn8DVjPwAhoAkswADm3aae9v/m7tO6TtmcL2/tZjHwK8CFgzyvORJEmSpClrtAHxGgZC3+Jm+5/AHcBJwK3AkUmWJukGLgXur6qHm7nXAe9LcmCSAxh4hvFagKpaA9wLXJakO8nrGXjT6c3N3C8ApyU5rgmelwO3tD2zKEmSJEkaga7RTK6qpxj4xAQASTYD26pqfbO/FPg08Hng28CylulXA4cw8HZSgL9o2gYtYyAwPgH8AHjj4HGranWSdzAQFOcAXwPeOppzkSRJkqSpblQBsV1VrWzb/xpw+E7GFvAHzTZUfx8Dt7Du7Le+CHxx9yqVJEmSJLUbk+8gSpIkSZL2fgZESZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCDIiSJEmSpIYBUZIkSZIEGBAlSZIkSQ0DoiRJkiQJMCBKkiRJkhoGREmSJEkSYECUJEmSJDUMiJIkSZIkwIAoSZIkSWoYECVJkiRJgAFRkiRJktQwIEqSJEmSAAOiJEmSJKlhQJQkSZIkAQZESZIkSVLDgChJkiRJAgyIkiRJkqSGAVGSJEmSBIxBQEzyoiR/mWRdkk1JvpPk5Jb+E5M8nOSpJF9PcnBLX5JckWRDs308SVr6e5o5TzXHeE3bb5/d/O6WJLcl2W+05yNJkiRJU9VYrCB2Af8O/AawL3AJ8FdNuJsL3NK07Qf0Aje2zF0BnAksAo4GTgXe3tK/CvgOMAf4IPClJPMAkiwErgbOBfYHngL+bAzOR5IkSZKmpFEHxKraUlUrq6qvqn5eVV8Bvg/8KvAGYHVV3VRV24CVwKIkhzfTlwNXVlV/VT0KXAmcB5DkMOBXgMuqamtV3Qw8ACxt5p4D3F5Vd1fVZgZC6BuSzBrtOUmSJEnSVDTmzyAm2R84DFgNLATuG+yrqi3A2qad9v7m79a+R6pq0wv0tx57LfB089uSJEmSpBEa04CYZBrwBeBzVfUwMBPY2DZsIzC4ytfevxGY2TyHONK57f2tda1I0pukd/369SM7KUmSJEmaIsYsICb5L8D1DKziXdg0bwZmtw2dDWzaSf9sYHNV1W7Mbe/frqquqaolVbVk3rx5wz4nSZIkSZpKxiQgNit+f8nAy2KWVtUzTddqBl5AMzhuBnBo0/68/ubv1r5D2p4pbO9vPfYhwIuANWNwSpIkSZI05YzVCuJngCOA06pqa0v7rcCRSZYm6QYuBe5vbj8FuA54X5IDkxwAvB+4FqCq1gD3Apcl6U7yegbedHpzM/cLwGlJjmuC5+XALW3PLEqSJEmShmksvoN4MAOfplgMPJZkc7OdU1XrGXjr6EeAJ4BjgWUt068Gbmfg7aQPAnc0bYOWAUuauR8D3tgck6paDbyDgaD4EwaePbxgtOcjSZIkSVNV12gPUFXrgLxA/9eAw3fSV8AfNNtQ/X3A8S9w7C8CXxx+tZIkSZKknRnzz1xIkiRJkvZOBkRJkiRJEmBAlCRJkiQ1DIiSJEmSJMCAKEmSJElqGBAlSZIkSYABUZIkSZLUMCBKkiRJkgADoiRJkiSpYUCUJEmSJAEGREmSJElSw4AoSZIkSQIMiJIkSZKkhgFRkiRJkgQYECVJkiRJDQOiJEmSJAkwIEqSJEmSGgZESZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCDIiSJEmSpIYBUZIkSZIE7OUBMcl+SW5NsiXJuiRnd7omSZIkSdpbdXW6gFG6Cnga2B9YDNyR5L6qWt3ZsiRJkiRp77PXriAmmQEsBS6pqs1V9S3gy8C5na1MkiRJkvZOe21ABA4DnquqNS1t9wELO1SPJEmSJO3VUlWdrmG3JDkOuKmqfqml7XeBc6rq+LaxK4AVze4vA98drzr3InOBxztdhPYKXisaCa8XDZfXikbC60XD5bUytIOrat5QHXvzM4ibgdltbbOBTe0Dq+oa4JrxKGpvlaS3qpZ0ug5NfF4rGgmvFw2X14pGwutFw+W1MnJ78y2ma4CuJC9taVsE+IIaSZIkSdoNe21ArKotwC3A5UlmJHkVcAZwfWcrkyRJkqS9014bEBsXANOBnwCrgHf6iYvd5i24Gi6vFY2E14uGy2tFI+H1ouHyWhmhvfYlNZIkSZKksbW3ryBKkiRJksaIAVGSJEmSBBgQJUmSJEkNA6IkSZIkCTAgSpIkSZIaBkRJkiRJEmBAlCRJkiQ1DIiSJEmSJMCAKEmSJElqGBAlSZIkSYABUZIkSZLUMCBKkjRKSfqSPJ1kblv7vUkqSU+S+UluTvJ4ko1JHkhyXjOupxm3uW17c0dOSJI0ZXV1ugBJkiaJ7wNnAX8KkOQoYHpL//XAfcDBwM+Ao4BfajvGi6vq2T1fqiRJQ3MFUZKksXE98JaW/eXAdS37xwDXVtWWqnq2qr5TVV8d1wolSdqFKRkQk1yYpDfJz5JcO1bzkpyY5OEkTyX5epKDx7JuSdKE9i/A7CRHJNkHeDPw+bb+q5IsS3JQRyqUJGkXpmRABH4IfBj47FjNa547uQW4BNgP6AVuHF2ZkqS9zOAq4muBh4FHW/reBHyTgf9PfL95PvGYtvmPJ3myZTtiXKqWJKkxJQNiVd1SVbcBG9r7kpza/E/7yST/K8nRw5kHvAFYXVU3VdU2YCWwKMnhe+g0JEkTz/XA2cB57Hh7KVX1RFV9oKoWAvsD9wK3JUnLsLlV9eKW7aHxKlySJJiiAXFnkvwKA6uDbwfmAFcDX07yomFMX8jAywcAqKotwNqmXZI0BVTVOgZeVnMKA3eV7Gzc48AngAMYuOtEkqQJwYC4o98Frq6qb1fVc1X1OQbeNPeKYcydCWxsa9sIzBrjGiVJE9vbgFc3/1C4XZIrkhyZpCvJLOCdwPeqaqi7UiRJ6ggD4o4OBt7f+vwH8F8Z+BfeXdkMzG5rmw1sGuMaJUkTWFWtrareIbp+EbgVeBJ4hIH/55zeNubJtu8gvm8PlytJ0g78DuKO/h34SFV9ZDfmrmbgleYAJJkBHNq0S5Imsarq2Un7s8DgM4a//wLz+1rGSZLUMVNyBbG5vacb2AfYJ0l3ki7gz4F3JDk2A2Yk+c3mVqAXmgcD/yp8ZJKlzZhLgfur6uHxP0NJkiRJGrkpGRCBi4GtwAeA327+vri5Jeh3gU8DTwDfY+BNdC84D6Cq1gNLgY80c48Flu35U5EkSZKksZGq6nQNkiRJkqQJYKquIEqSJEmS2hgQJUmSJEnAFHyL6dy5c6unp6fTZUiSJElSR9xzzz2PV9W8ofrGPSAmuZCBF78cBayqqvN2Mm458C7gpcB/AF8E/u/mleEk+QYDH7B/tpnyaFX98q5+v6enh97eoT5PJUmSJEmTX5J1O+vrxC2mPwQ+DHx2F+N+EXgPMJeBN4KeCFzUNubCqprZbLsMh5IkSZKknRv3FcSqugUgyRJg/guM+0zL7qNJvgCcsIfLkyRJkqQpa296Sc2vA6vb2j6a5PEk/5Tk+A7UJEmSJEmTxl7xkpokbwWWAL/T0vyHwP8HPM3AB+lvT7K4qtYOMX8FsALgoIMOet7xn3nmGfr7+9m2bdseqL7zuru7mT9/PtOmTet0KZIkSZImsAkfEJOcCXwMeE1VPT7YXlXfbhn2uSRnAacAf9p+jKq6BrgGYMmSJdXe39/fz6xZs+jp6SHJWJ9CR1UVGzZsoL+/nwULFnS6HEmSJEkT2IS+xTTJ64A/B06rqgd2MbyA3Up327ZtY86cOZMuHAIkYc6cOZN2dVSSJEnS2OnEZy66mt/dB9gnSTfw7ODnK1rGvRr4AvD6qvrXtr4XM/Bm039k4DMXb2bgGcX3jKKu3Z064U3mc5MkSeNk5b6drmBiWrmx0xVIY6oTK4gXA1uBDwC/3fx9cZKDkmxOMviQ4CXAvsDfNO2bk3y16ZvGwKcy1gOPA78PnFlV3x3PExlLSTj33HO37z/77LPMmzePU089FYAf//jHnHrqqSxatIiXvexlnHLKKQD09fUxffp0Fi9evH277rrrOnIOkiRJkvZunfjMxUpg5U66Z7aM2+knLapqPXDMmBbWaqz/hWwY/7I0Y8YMHnzwQbZu3cr06dO56667OPDAA7f3X3rppbz2ta/l3e9+NwD333//9r5DDz2Ue++9d2xrliRJkjTlTOhnEKeak08+mTvuuAOAVatWcdZZZ23v+9GPfsT8+f/52cijjz563OuTJEmSNLkZECeQZcuWccMNN7Bt2zbuv/9+jj322O19v/d7v8fb3vY2TjjhBD7ykY/wwx/+cHvf2rVrd7jF9Jvf/GYnypckSZK0l5vwn7mYSo4++mj6+vpYtWrV9mcMB5100kk88sgj3HnnnXz1q1/l5S9/OQ8++CDgLaaSJEmSxoYriBPM6aefzkUXXbTD7aWD9ttvP84++2yuv/56jjnmGO6+++4OVChJkiRpsjIgTjDnn38+l156KUcdddQO7f/wD//AU089BcCmTZtYu3YtBx100FCHkCRJkqTd4i2mE8z8+fO3v6m01T333MOFF15IV1cXP//5z/md3/kdjjnmGPr6+rY/gzjo/PPP513vetd4li1JkiRpEkhVdbqGcbVkyZLq7e3doe2hhx7iiCOO6FBF42MqnKMkSdqDxvozYJPFMD5nJk00Se6pqiVD9XmLqSRJkiQJMCBKkiRJkhoGREmSJEkSYEDcbjI/izmZz02SJEnS2DEgAt3d3WzYsGFSBqmqYsOGDXR3d3e6FEmSJEkTnJ+5YODTEv39/axfv77TpewR3d3dzJ8/v9NlSJIkSZrgDIjAtGnTWLBgQafLkCRJkqSO8hZTSZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZKADgTEJBcm6U3ysyTX7mLse5M8lmRjks8meVFL335Jbk2yJcm6JGfv8eIlSZIkaRLrxAriD4EPA599oUFJTgI+AJwI9ACHAH/UMuQq4Glgf+Ac4DNJFu6BeiVJkiRpShj3gFhVt1TVbcCGXQxdDvxlVa2uqieADwHnASSZASwFLqmqzVX1LeDLwLl7rnJJkiRJmtwm8jOIC4H7WvbvA/ZPMgc4DHiuqta09buCKEmSJEm7aSIHxJnAxpb9wb9nDdE32D9rqAMlWdE899i7fv36MS9UkiRJkiaDiRwQNwOzW/YH/940RN9g/6ahDlRV11TVkqpaMm/evDEvVJIkSZImg4kcEFcDi1r2FwE/rqoNwBqgK8lL2/pXj2N9kiRJkjSpdOIzF11JuoF9gH2SdCfpGmLodcDbkrwsyUuAi4FrAapqC3ALcHmSGUleBZwBXD8uJyFJkiRJk1AnVhAvBrYy8AmL327+vjjJQUk2JzkIoKruBD4OfB1Y12yXtRznAmA68BNgFfDOqnIFUZIkSZJ201Ard3tUVa0EVu6ke2bb2D8B/mQnx/kpcOZY1iZJkiRJU9lEfgZRkiRJkjSODIiSJEmSJMCAKEmSJElqGBAlSZIkSYABUZIkSZLUMCBKkiRJkgADoiRJkiSpYUCUJEmSJAEGREmSJElSw4AoSZIkSQIMiJIkSZKkhgFRkiRJkgQYECVJkiRJDQOiJEmSJAkwIEqSJEmSGgZESZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1Bj3gJhkvyS3JtmSZF2Ss3cy7n8m2dyy/SzJppb+byTZ1tL/3fE7C0mSJEmafLo68JtXAU8D+wOLgTuS3FdVq1sHVdU7gHcM7ie5Fvh527EurKq/2LPlSpIkSdLUMK4riElmAEuBS6pqc1V9C/gycO4w531uz1cpSZIkSVPTeN9iehjwXFWtaWm7D1i4i3lLgfXA3W3tH03yeJJ/SnL82JUpSZIkSVPPeAfEmcDGtraNwKxdzFsOXFdV1dL2h8AhwIHANcDtSQ4danKSFUl6k/SuX79+9yqXJEmSpEluvAPiZmB2W9tsYNMQYwFI8l+B3wCua22vqm9X1aaq+llVfQ74J+CUoY5RVddU1ZKqWjJv3rxRnYAkSZIkTVbjHRDXAF1JXtrStghYvZPxAG8B/ldVPbKLYxeQUdYnSZIkSVPWuAbEqtoC3AJcnmRGklcBZwDXv8C0twDXtjYkeXGSk5J0J+lKcg7w68Df7qHSJUmSJGnSG/fvIAIXANOBnwCrgHdW1eokBzXfMzxocGCSVwLzgZvajjEN+DADL655HPh94Myq8luIkiRJkrSbxv07iFX1U+DMIdp/wMBLbFrb/hmYMcTY9cAxe6pGSZIkSZqKOrGCKEmSJEmagAyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCoKvTBUiSJEmaRFbu2+kKJqaVGztdwbC4gihJkiRJAgyIkiRJkqSGAVGSJEmSBBgQJUmSJEkNA6IkSZIkCTAgSpIkSZIaBkRJkiRJEmBAlCRJkiQ1DIiSJEmSJMCAKEmSJElqjHtATLJfkluTbEmyLsnZOxl3XpLnkmxu2Y4f6XEkSZIkScPT1YHfvAp4GtgfWAzckeS+qlo9xNh/rqpfG4PjSJIkSZJ2YVxXEJPMAJYCl1TV5qr6FvBl4NxOHEeSJEmS9J/G+xbTw4DnqmpNS9t9wMKdjH95kseTrElySZLBFc+RHkeSJEmStAvjfYvpTGBjW9tGYNYQY+8GjgTWMRD8bgSeBT46wuOQZAWwAuCggw7azdIlSZIkaXIb7xXEzcDstrbZwKb2gVX1SFV9v6p+XlUPAJcDbxzpcZpjXVNVS6pqybx580Z1ApIkSZI0WY13QFwDdCV5aUvbImA4L5YpIGNwHEmSJEnSEMY1IFbVFuAW4PIkM5K8CjgDuL59bJKTk+zf/H04cAnw1yM9jiRJkiRpeMb9O4jABcB04CfAKuCdVbU6yUHNtw4HHxI8Ebg/yRbgbxgIhP/Pro4zXichSZIkSdZW7n8AACAASURBVJPNuH8Hsap+Cpw5RPsPGHj5zOD+RcBFIz2OJEmSJGn3dGIFUZIkSZI0AY37CqJarNy30xVMTCvbv2Air5Wd8FoZmtfL0Lxens9rZWheK5KmMFcQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCDIiSJEmSpIYBUZIkSZIEGBAlSZIkSQ0DoiRJkiQJMCBKkiRJkhoGREmSJEkSYECUJEmSJDUMiJIkSZIkwIAoSZIkSWoYECVJkiRJgAFRkiRJktQwIEqSJEmSgA4ExCT7Jbk1yZYk65KcvZNxy5Pck+Q/kvQn+XiSrpb+byTZlmRzs313/M5CkiRJkiafTqwgXgU8DewPnAN8JsnCIcb9IvAeYC5wLHAicFHbmAuramaz/fIerFmSJEmSJr2uXQ8ZO0lmAEuBI6tqM/CtJF8GzgU+0Dq2qj7Tsvtoki8AJ4xbsZIkSZI0xYz3CuJhwHNVtaal7T5gqBXEdr8OrG5r+2iSx5P8U5Ljx6hGSZIkSZqSxjsgzgQ2trVtBGa90KQkbwWWAJ9oaf5D4BDgQOAa4PYkh+5k/ookvUl6169fv7u1S5IkSdKkNt4BcTMwu61tNrBpZxOSnAl8DDi5qh4fbK+qb1fVpqr6WVV9Dvgn4JShjlFV11TVkqpaMm/evFGfhCRJkiRNRuMdENcAXUle2tK2iOffOgpAktcBfw6cVlUP7OLYBWRMqpQkSZKkKWhcA2JVbQFuAS5PMiPJq4AzgOvbxyZ5NfAFYGlV/Wtb34uTnJSkO0lXknMYeEbxb/f8WUiSJEnS5NSJz1xcAEwHfgKsAt5ZVauTHNR8z/CgZtwlwL7A37R86/CrTd804MPAeuBx4PeBM6vKbyFKkiRJ0m4a189cAFTVT4Ezh2j/AQMvsRnc3+knLapqPXDMHilQkiRJkqaoTqwgSpIkSZImIAOiJEmSJAkwIEqSJEmSGgZESZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCDIiSJEmSpIYBUZIkSZIEGBAlSZIkSQ0DoiRJkiQJMCBKkiRJkhoGREmSJEkSYECUJEmSJDXGPSAm2S/JrUm2JFmX5OwXGPveJI8l2Zjks0letDvHkSRJkiTtWidWEK8Cngb2B84BPpNkYfugJCcBHwBOBHqAQ4A/GulxJEmSJEnDM64BMckMYClwSVVtrqpvAV8Gzh1i+HLgL6tqdVU9AXwIOG83jiNJkiRJGobxXkE8DHiuqta0tN0HDLXyt7Dpax23f5I5IzyOJEmSJGkYusb592YCG9vaNgKzhjF28O9ZIzwOSVYAK5rdzUm+O4Kap4q5wOOdLgKAP0qnK9AL81rRSHi9aLi8VjQSXi8aLq+VoR28s47xDoibgdltbbOBTcMYO/j3phEeh6q6BrhmpMVOJUl6q2pJp+vQxOe1opHwetFwea1oJLxeNFxeKyM33reYrgG6kry0pW0RsHqIsaubvtZxP66qDSM8jiRJkiRpGMY1IFbVFuAW4PIkM5K8CjgDuH6I4dcBb0vysiQvAS4Grt2N40iSJEmShqETn7m4AJgO/ARYBbyzqlYnOSjJ5iQHAVTVncDHga8D65rtsl0dZ/xOY9LxFlwNl9eKRsLrRcPltaKR8HrRcHmtjFCqqtM1SJIkSZImgE6sIEqSJEmSJiADoiRJkiQJMCBKkiRJkhoGREmSJEkSYECUJEmSJDUMiJIkSZIkwIAoSZIkSWoYECVJkiRJgAFRkiRJktQwIEqSJEmSAAOiJEmSJKlhQJQkaYSS9CXZmmRzkseSXJtkZtN3bZJKcnrbnP/RtJ/X7P9CkiuT9DfH+X6ST+7kNwa3T4/riUqSphwDoiRJu+e0qpoJLAZeDvz3lr41wPLBnSRdwJuAtS1j/juwBPhvwCzgBOA7Q/1Gy3bh2J+GJEn/qavTBUiStDerqseS/C0DQXHQ7cBvJ3lJVT0BvA64n4EgOOgY4Naq+mGz39dskiR1jCuIkiSNQpL5wMnA91qatwFfBpY1+28Brmub+i/A+5JckOSoJNnjxUqStAsGREmSds9tSTYB/w78BLisrf864C1J9gV+A7itrf+jwBXAOUAv8GiS5W1jbkvyZMv2u2N+FpIktTAgSpK0e86sqlnA8cDhwNzWzqr6FjAPuBj4SlVtbet/rqquqqpXAS8GPgJ8NskRbb/x4pbtz/fg+UiSZECUJGk0quofgWuBTwzR/Xng/Tz/9tL2Y2ytqquAJ4CXjXWNkiQNly+pkSRp9P4H0JdkcVv7p4BvAne3T0jyHuBe4NvAMwzcajqL57/JVJKkcWNAlCRplKpqfZLrgEuATS3tPwX+fifTtgJXAv8XUAx8GmNpVT3SMub2JM+17N9VVa8f0+IlSWqRqup0DZIkSZKkCcBnECVJkiRJgAFRkiRJktQwIEqSJEmSAAOiJEmSJKlhQJQkSZIkAVPwMxdz586tnp6eTpchSZIkSR1xzz33PF5V84bqm3IBsaenh97e3k6XIUmSJEkdkWTdzvq8xVSSJEmSBBgQJUmSJEkNA6IkSZIkCZiCzyBKkiRJmjqeeeYZ+vv72bZtW6dLGXfd3d3Mnz+fadOmDXuOAVGSJEnSpNXf38+sWbPo6ekhSafLGTdVxYYNG+jv72fBggXDnuctppIkSZImrW3btjFnzpwpFQ4BkjBnzpwRr5y6gihJkqRdOupzR3W6hAnpgeUPdLoEDcNUC4eDdue8XUGUJEmSpD1on332YfHixRx55JGcdtppPPnkkwD09fWRhEsuuWT72Mcff5xp06Zx4YUXAvDd736X448/nsWLF3PEEUewYsUKAL7xjW+w7777snjx4u3b1772tVHX6gqiJEmSpCljrFfDh7OKPH36dO69914Ali9fzlVXXcUHP/hBAA455BC+8pWv8KEPfQiAm266iYULF26f+653vYv3vve9nHHGGQO/98B//t5xxx3HV77ylTE7F3AFUZIkSZLGzStf+UoeffTR7fvTp0/niCOOoLe3F4Abb7yR3/qt39re/6Mf/Yj58+dv3z/qqD17u7cBUZIkSZLGwXPPPcff//3fc/rpp+/QvmzZMm644Qb6+/vZZ599OOCAA7b3vfe97+XVr341J598Mp/85Ce3354K8M1vfnOHW0zXrl076hoNiJIkSZK0B23dupXFixczZ84cfvrTn/La1752h/7Xve513HXXXaxatYo3v/nNO/S99a1v5aGHHuJNb3oT3/jGN3jFK17Bz372M2DgFtN77713+3booYeOulYDoiRJkiTtQYPPIK5bt46nn36aq666aof+X/iFX+BXf/VXufLKK1m6dOnz5h9wwAGcf/75/PVf/zVdXV08+OCDe6xWA6IkSZIkjYN9992XT33qU3ziE5/gmWee2aHv/e9/P1dccQVz5szZof3OO+/cPvaxxx5jw4YNHHjggXusRgOiJEmSJI2Tl7/85SxatIgbbrhhh/aFCxeyfPny543/u7/7O4488kgWLVrESSedxB//8R/zS7/0S8Dzn0H80pe+NOr6UlWjPsjeZMmSJTX4hiBJkiQNz1h/GmCyGM4nDtRZDz30EEcccUSny+iYoc4/yT1VtWSo8cNaQUxyYZLeJD9Lcm1b34lJHk7yVJKvJzm4pS9Jrkiyodk+niQt/T3NnKeaY7ym7dhnJ1mXZEuS25Ls19L3oiSfTfIfSR5L8r7hnIskSZIkaWjDvcX0h8CHgc+2NiaZC9wCXALsB/QCN7YMWQGcCSwCjgZOBd7e0r8K+A4wB/gg8KUk85pjLwSuBs4F9geeAv6sZe5K4KXAwcAJwB8ked0wz0eSJEmS1GZYAbGqbqmq24ANbV1vAFZX1U1VtY2B0LYoyeFN/3Lgyqrqr6pHgSuB8wCSHAb8CnBZVW2tqpuBB4DB1/acA9xeVXdX1WYGQugbksxq+t8CfKiqnqiqh4A/Hzy2JEmSJGnkRvuSmoXAfYM7VbUFWNu0P6+/+bu175Gq2vQC/a3HXgs8DRyW5CXAAS9wbEmSJEkCYKq9d2XQ7pz3aAPiTGBjW9tGYNZO+jcCM5vnEEc6t7V/Zsv+UHN3kGRF8wxl7/r161/whCRJkiRNHt3d3WzYsGHKhcSqYsOGDXR3d49oXtcof3czMLutbTawaSf9s4HNVVVJRjq3tX9zy/62IebuoKquAa6BgbeYvvApSZIkSZos5s+fT39/P1Nxoai7u5v58+ePaM5oA+JqBp4zBCDJDODQpn2wfxHwr83+ora+Q5LMarnNdBHwxba5g8c+BHgRsKaqNiX5UdN/1xDHliRJkiSmTZvGggULOl3GXmO4n7noStIN7APsk6Q7SRdwK3BkkqVN/6XA/VX1cDP1OuB9SQ5McgDwfuBagKpaA9wLXNYc7/UMvOn05mbuF4DTkhzXBM/LgVtawuR1wMVJXtK8FOd3B48tSZIkSRq54T6DeDGwFfgA8NvN3xdX1XoG3jr6EeAJ4FhgWcu8q4HbGXg76YPAHU3boGXAkmbux4A3NsekqlYD72AgKP6EgecLL2iZexkDL8RZB/wj8MdVdecwz0eSJEmS1CZT7WHNJUuWVG9vb6fLkCRJ2qsc9bmjOl3ChPTA8gc6XYI0YknuqaolQ/WN9i2mkiRJkqRJwoAoSZIkSQIMiJIkSZKkhgFRkiRJkgQYECVJkiRJDQOiJEmSJAkwIEqSJEmSGgZESZIkSRJgQJQkSZIkNQyIkiRJkiTAgChJkiRJahgQJUmSJEmAAVGSJEmS1DAgSpIkSZIAA6IkSZIkqWFAlCRJkiQBBkRJkiRJUsOAKEmSJEkCxiggJulJ8jdJnkjyWJJPJ+lq+k5M8nCSp5J8PcnBLfOS5IokG5rt40nSdtyvN3MfTvKatt89O8m6JFuS3JZkv7E4H0mSJEmaisZqBfHPgJ8A/yewGPgN4IIkc4FbgEuA/YBe4MaWeSuAM4FFwNHAqcDbW/pXAd8B5gAfBL6UZB5AkoXA1cC5wP7AU00dkiRJkqTdMFYBcQHwV1W1raoeA+4EFgJvAFZX1U1VtQ1YCSxKcngzbzlwZVX1V9WjwJXAefz/7d17mGVVeefx7w9bAbtpuXSLcg8owYBCCIbEhLFnIBeMKNKYEAiCUVGZZMaIIYkJ0qIm6kgm3oigRq6Nys0EMTGSMWKMt0642Yo8cr9qi9B20Y0QfOePvQo2h67qqq7TFNX1/TzPeerUftfae+06q/Y571lr7w0k2R3YFzi5qtZU1UXAtcDiVvco4NKquqKqRuiS0MOSbDGkfZIkSZKkWWVYCeL7gSOSPD3J9sDBPJokXj1aqKruB25oyxmMt+f92I1VtWqceH/dNwAPArsPaZ8kSZIkaVYZVoL4JbqE7cfA7XRTST8DzANWDpRdCYyO8g3GVwLz2nmIk607GH9EkuOSLEuybMWKFZPYLUmSJEmaPaacICbZBPg83bmGc4EFwFbAe4ARYP5AlfnA6KjgYHw+MFJVtR51B+OPqKozqmq/qtpv4cKFE985SZIkSZpF5gxhHVsDOwIfqqqfAD9J8gngncAH6M4zBCDJXGA3YHlbtJzuAjXfaL/vPRDbNckWvWmmewNLB+qOrntXYFPg+iHskyRJkqT18Pyznj/dTXhSuvaYa6e7CRMy5RHEqvohcBPwxiRzkmxJlxReDVwC7JVkcZLNgLcB11TVda362cCbk2yfZDvgBODMtt7rgauAk5NsluQVdFc6vajVPQ84JMkBLfE8Bbh44JxFSZIkSdIEDescxMOA3wRWAN8D/gv4o6paQXfV0XcB9wL7A0f06p0OXEp3ddJvAZe1ZaOOAPZrdd8NHN7WSVUtB95Alyj+gO7cw+OHtD+SJEmSNOsMY4opVXUVsGiM2OXAHmPECjixPdYWv3ms9bb4Uh6dcipJkiRJmoJhjSBKkiRJkmY4E0RJkiRJEmCCKEmSJElqTBAlSZIkSYAJoiRJkiSpMUGUJEmSJAEmiJIkSZKkxgRRkiRJkgSYIEqSJEmSGhNESZIkSRJggihJkiRJakwQJUmSJEkAzJnuBsxmzz/r+dPdhCela4+5drqb8KRjX1k7+8ra2V/Wzv7yePaVtbOvSJrNHEGUJEmSJAEmiJIkSZKkxgRRkiRJkgSYIEqSJEmSmqEliEmOSPKdJPcnuSHJAW35gUmuS7I6yReT7NyrkyTvSXJPe7w3SXrxXVqd1W0dBw1s88gkt7RtfibJ1sPaH0mSJEmabYaSICb5NeA9wKuBLYD/BtyYZAFwMXASsDWwDPhUr+pxwKHA3sALgJcCr+/FzweuBLYB/hy4MMnCts09gdOBo4FtgdXAacPYH0mSJEmajYY1gvh24JSq+lpV/bSq7qiqO4DDgOVVdUFVPQAsAfZOskerdwxwalXd3sqfChwLkGR3YF/g5KpaU1UXAdcCi1vdo4BLq+qKqhqhS0IPS7LFkPZJkiRJkmaVKSeISZ4C7AcsTPK9JLcn+VCSzYE9gatHy1bV/cANbTmD8fa8H7uxqlaNE++v+wbgQWD3qe6TJEmSJM1GwxhB3BZ4KnA4cACwD/DzwF8A84CVA+VX0k1DZS3xlcC8dh7iZOsOxh+R5Lgky5IsW7FixcT3TJIkSZJmkWEkiGvazw9W1V1V9UPgr4GXACPA/IHy84HRUcHB+HxgpKpqPeoOxh9RVWdU1X5Vtd/ChQsnvGOSJEmSNJtMOUGsqnuB24FaS3g53QVoAEgyF9itLX9cvD3vx3YdOKdwMN5f967ApsD167svkiRJkjSbDesiNZ8A/jDJM5NsBbwJ+CxwCbBXksVJNgPeBlxTVde1emcDb06yfZLtgBOAMwGq6nrgKuDkJJsleQXdlU4vanXPAw5JckBLPE8BLh44Z1GSJEmSNEFzhrSedwAL6EbvHgA+Dbyrqh5Ishj4EHAu8HXgiF6904Fd6a5OCvCxtmzUEXQJ473ArcDhVbUCoKqWJ3kDXaK4DXA53W02JEmSJEnrYSgJYlU9BBzfHoOxy4E9HlepixVwYnusLX4zsGic7S4Flk66wZIkSZKkxxnWFFNJkiRJ0gxngihJkiRJAkwQJUmSJEmNCaIkSZIkCTBBlCRJkiQ1JoiSJEmSJMAEUZIkSZLUmCBKkiRJkgATREmSJElSY4IoSZIkSQJMECVJkiRJjQmiJEmSJAkwQZQkSZIkNSaIkiRJkiTABFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKEmSJEkChpggJnlukgeSnNtbdmCS65KsTvLFJDv3YknyniT3tMd7k6QX36XVWd3WcdDA9o5MckuS+5N8JsnWw9oXSZIkSZqNhjmC+GHgm6O/JFkAXAycBGwNLAM+1St/HHAosDfwAuClwOt78fOBK4FtgD8HLkyysK17T+B04GhgW2A1cNoQ90WSJEmSZp2hJIhJjgDuA/6lt/gwYHlVXVBVDwBLgL2T7NHixwCnVtXtVXUHcCpwbFvf7sC+wMlVtaaqLgKuBRa3ukcBl1bVFVU1QpeEHpZki2HsjyRJkiTNRlNOEJPMB04BThgI7QlcPfpLVd0P3NCWPy7envdjN1bVqnHi/XXfADwI7D6VfZEkSZKk2WwYI4jvAD5eVbcNLJ8HrBxYthLYYoz4SmBeOw9xsnUH44+R5Lgky5IsW7FixTp2R5IkSZJmpykliEn2AQ4C/u9awiPA/IFl84FVY8TnAyNVVetRdzD+GFV1RlXtV1X7LVy4cOwdkiRJkqRZbKojiIuAXYBbk9wNvAVYnOQ/geV0F6ABIMlcYLe2nMF4e96P7TpwTuFgvL/uXYFNgeunuD+SJEmSNGtNNUE8gy7p26c9PgJcBvwGcAmwV5LFSTYD3gZcU1XXtbpnA29Osn2S7ejOYTwToKquB64CTk6yWZJX0F3p9KJW9zzgkCQHtMTzFODigXMWJUmSJEmTMGcqlatqNd0tJgBIMgI8UFUr2u+LgQ8B5wJfB47oVT8d2JXu6qQAH2vLRh1BlzDeC9wKHD663qpanuQNdIniNsDlwKunsi+SJEmSNNtNKUEcVFVLBn6/HNhjjLIFnNgea4vfTDeFdaxtLQWWrl9LJUmSJEmDhnIfREmSJEnSzGeCKEmSJEkCTBAlSZIkSY0JoiRJkiQJMEGUJEmSJDUmiJIkSZIkwARRkiRJktSYIEqSJEmSABNESZIkSVJjgihJkiRJAkwQJUmSJEmNCaIkSZIkCTBBlCRJkiQ1JoiSJEmSJMAEUZIkSZLUmCBKkiRJkgATREmSJElSM+UEMcmmST6e5JYkq5JcmeTgXvzAJNclWZ3ki0l27sWS5D1J7mmP9yZJL75Lq7O6reOggW0f2bZ7f5LPJNl6qvsjSZIkSbPVMEYQ5wC3AS8GngGcBHy6JXcLgIvbsq2BZcCnenWPAw4F9gZeALwUeH0vfj5wJbAN8OfAhUkWAiTZEzgdOBrYFlgNnDaE/ZEkSZKkWWnKCWJV3V9VS6rq5qr6aVV9FrgJ+AXgMGB5VV1QVQ8AS4C9k+zRqh8DnFpVt1fVHcCpwLEASXYH9gVOrqo1VXURcC2wuNU9Cri0qq6oqhG6JPSwJFtMdZ8kSZIkaTYa+jmISbYFdgeWA3sCV4/Gqup+4Ia2nMF4e96P3VhVq8aJ99d9A/Bg27YkSZIkaZKGmiAmeSpwHnBWVV0HzANWDhRbCYyO8g3GVwLz2nmIk607GO+367gky5IsW7FixeR2SpIkSZJmiaEliEk2Ac6hG8X7g7Z4BJg/UHQ+sGqM+HxgpKpqPeoOxh9RVWdU1X5Vtd/ChQsnvE+SJEmSNJsMJUFsI34fp7tYzOKqeqiFltNdgGa03Fxgt7b8cfH2vB/bdeCcwsF4f927ApsC1w9hlyRJkiRp1hnWCOLfAs8DDqmqNb3llwB7JVmcZDPgbcA1bfopwNnAm5Nsn2Q74ATgTICquh64Cjg5yWZJXkF3pdOLWt3zgEOSHNASz1OAiwfOWZQkSZIkTdAw7oO4M92tKfYB7k4y0h5HVdUKuquOvgu4F9gfOKJX/XTgUrqrk34LuKwtG3UEsF+r+27g8LZOqmo58Aa6RPEHdOceHj/V/ZEkSZKk2WrOVFdQVbcAGSd+ObDHGLECTmyPtcVvBhaNs+6lwNKJt1aSJEmSNJah3+ZCkiRJkjQzmSBKkiRJkgATREmSJElSY4IoSZIkSQJMECVJkiRJjQmiJEmSJAkwQZQkSZIkNSaIkiRJkiTABFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKEmSJEkCTBAlSZIkSY0JoiRJkiQJMEGUJEmSJDUmiJIkSZIkwARRkiRJktSYIEqSJEmSgBmeICbZOsklSe5PckuSI6e7TZIkSZI0U82Z7gZM0YeBB4FtgX2Ay5JcXVXLp7dZkiRJkjTzzNgRxCRzgcXASVU1UlX/BvwDcPT0tkySJEmSZqYZmyACuwMPV9X1vWVXA3tOU3skSZIkaUZLVU13G9ZLkgOAC6rqWb1lrwOOqqpFA2WPA45rv/4s8N0nqp0zyALgh9PdCM0I9hVNhv1FE2Vf0WTYXzRR9pW127mqFq4tMJPPQRwB5g8smw+sGixYVWcAZzwRjZqpkiyrqv2mux168rOvaDLsL5oo+4omw/6iibKvTN5MnmJ6PTAnyXN7y/YGvECNJEmSJK2HGZsgVtX9wMXAKUnmJvkV4OXAOdPbMkmSJEmamWZsgtgcD2wO/AA4H3ijt7hYb07B1UTZVzQZ9hdNlH1Fk2F/0UTZVyZpxl6kRpIkSZI0XDN9BFGSJEmSNCQmiJJIcnOSg6a7HXrys69Ikp6MkixJcu50t2NjYII4CyQ5Nsm1SVYnuTvJ3ybZssXG/GdK8qtJ/j3JyiQ/SvKVJC98YluvyWof4NckGUny/SSfSDJvA21rUZKftm2tSvLdJK/eENvS8NlXNJYn4xcBSXZJUq0PjbQ2/ul0t0tjGzjG3J3kzKkcY5Ic0Hv97x/oDyNJdhpm+zUcw+4HE9zm4PFiJMnVG3Kba2lDJXnOE7nNYTFB3MglOQF4D/DHwDOAXwJ2Br6Q5Gnj1JsPfBb4ILA1sD3wduAnG7rNGopDqmoesC/wQuAvNuC27mzbmg/8EfDRJD+7Aben4bKvaKbZsvWjw4GTkvzadDdI4xo9xuwD/DzwZ+u7oqr6clXNa+vbsy3ecnRZVd06WjbJTL7X98ZoaP1gkvr9Y+/JVp6t/cgEcSPWkry3A39YVf9UVQ9V1c3Ab9Mlib83TvXdAarq/Kp6uKrWVNU/V9U1G7zhGpqqugP4R2CvJC9LsjzJfUn+NcnzBssneVYbad6mt+wXkqxI8tR1bKuq6nPAj4AXtLqbJPnTJDckuSfJp5Ns3Vv3q5Lc0mInPRlHLWYL+4rWJclWST7bXuN72/MdevFjk9zYRohvSnJUW/6cJF9KNxvlh0k+1avzoiTfbLFvJnnRRNtTVcvo7n28T299v5/kO619n0+ycy/2623kemWS01qbXjvVv4smpqruBj5Pe72S/FK6WUr3Jbk6yaLRskl+JskVrS9dnuTDWcfUwXQzoi5Mcm6SHwPHJnlGko8nuSvJHUnemeQpvTpj9hdtGGvpB6PH/VVJvp3kFaNl2zHl35K8r71GNyU5uBf/mfZ/vCrJF4AFE2lDku2S/EO62XHfS/K6XmxS/Wis41uSK9oqr043evk7U/zTPaFMEDduLwI2o7tf5COqaoTug+B437peDzyc5KwkByfZasM1UxtKkh2BlwCr6G4F8yZgIfA54NIMjCK3A/e/0n2JMOr3gE9W1UPr2NYmSV5Gd4D+Xlv8v4BDgRcD2wH3Ah9u5X8OOA04Cng23Qj39uu5q5oi+4omrbUJygAAC+RJREFUYBPgE3RfMO4ErAE+BJBkLvAB4OCq2oLu/eeqVu8dwD8DWwE70M1MoX0BcFmrtw3w18Bl6X3pMJ4kvwTsRetDSQ4F3gocRtd3v0zXl0myALiQbtRiG+C7rY16grQvEw4Gvpdke7rX/p10s5TeAlyUZGErvhT4Bt1rtQQ4eoKbeTnd67wlcB5wFvBfwHPoRq1+HXhta8+Y/UUbTr8ftEU3AAfQHdffDpyb5Nm9KvvT/b8uAN4LfDxJWmwp8B8t9g7gmAk243zgdrr3msOBv0xyYC8+4X7EGMe3qvpvLb53G7185IuxGaGqfGykD7oPa3ePEXs38AW6A++5Y5R5HnAm3T/RfwH/AGw73fvlY52v+83ACHAfcAvdB+uTgE/3ymwC3AEs6tU5qD3/HeAr7flTgLuBXxxjW4uAn7Zt/QR4GHhTL/4d4MDe788GHgLmAG8Dzu/Fng48ONoOH/YV+8q0941x/750IwD3tudz22u7GNh8oNzZdPch22Fg+dHANwaWfRU4dozt7QJU286a9vx9PHrLrn8EXjPQd1fTJbSvAr7aiwW4DXjtdP+tN+ZH7xizqr1e/0L3oftPgHMGyn6e7gP+TnSfOZ7ei53LwGeVXn+Y035fAlzRi2/bjjWb95b9LvDFdfWX6f67bWyPsfrBGGWvAl7enh8LfK8Xe3qr/6xeP5nbiy8d7ScDx4vRx1uAHenef7bo1fsr4Mz17EdrPb61WAHPme6///o8HEHcuP0QWJC1z59+douPqaq+U1XHVtUOdN/Sbgf8zfCbqQ3g0Krasqp2rqrj6V67W0aDVfVTug9HaxuF+Xvg55LsSjfKvLKqvpFkp/RO9u6Vv7OqtqQ7r+wDwP/oxXYGLmlTiO6jSwIepjvgbtfaMNqm1cA9U991TZJ9RROS5OlJTk831ffHwBXAlkmeUlX3031h8AbgriSXJdmjVT2RLiH7Rrqpy7/flj+mrzW30Ppaxr74yAJgHt2HvUXA6JTmnYH39/rQj9p2t+fxfajovvzUhndodaPKi4A96F6/nYFXjr5W7fX6VbrPJtsBP2r/56NuY2L65Xam6xt39bZxOvDMXnys/qLhW1s/GD194Kre67AXj50qevfok16fmEebadKOPaMGjycAC9p73JZV9T4e7V+rBur1X/fJ9KOxjm8zmgnixu2rdN96HNZf2KYCHUz3Dc6EVNV1dKOJew2xfXri3El3kAOgTc/YkW5k6DGq6gHg03TT+Y4GzmnLb61HT/R+3NXHquondN8KP79N3YHuIHtw7+C8ZVVtVt35bnfRTccYbdPmdNOJNL3sKxrLCcDPAvtX1XxgdApVAKrq81X1a3Qf8q8DPtqW311Vr6uq7YDXA6elu7LfY/pasxOtr/X7UPUuPtJiD1fVqcADwPFt8W3A6wf60OZV9e88vg+l/7s2vKr6Et3niPfRvVbnDLxWc6vq3XSv1dZJnt6rvuNEN9N7fhvdZ6B+gjC/qvbsxcfqL9pA+v0g3TmfHwX+ANimfYH4LdoxZR3uArZqn2lHTeQqtnfS9a8tBur13+Mm3I/GOb7NaCaIG7GqWkk3n/uDSX4zyVOT7AJcQPfN6Tmt6CZJNus9Nk2yR5IT2lzx0fOTfhf42hO/JxqCTwO/leTAdBcQOYHugDfWG+HZdFM7XkY3tWdCqupB4FS6KYEAHwHe1d4ESLIwyctb7ELgkHQXqXgaXV+dyJuCNiz7ikY9tf/eQHeOzRrgvnb+4MmjBZNsm+7iRnPp+ssI3QgwSV6ZRy9mcy/dh6+H6c5v3T3JkUnmpLuIw8/RXUF7ot4NnNja9xHgz5Ls2bb7jCSvbOUuo30h0WbV/E+6aWp6Yv0N3WyDf6P7n/6NJE9pfWxRkh2q6hZgGbAkydOS/DJwyGQ3VFV30Z0bdmqS+enOfd4tyYtbkfH6izas0X6wPd3xYAVAulsfTWggotdP3t76ya8ygX5SVbfRvZ/9Vet3LwBeQ3eu4drKj9uPxjm+AXwf2HUi+/NkY4K4kauq99KdhP0+4MfA1+m+DTmwfYsPXeK3pve4gW6e+P7A15PcT5cYfovuw6JmmKr6Lt05qR+km1p8CN0lpx8co/xX6M4X+8/qrnw7GX8H7JTkEOD9dOeu/nOSVXT9aP+2jeXAHwKfpPsmcBXwA7yVyrSyr6jnczz2vWFLYHO6fvE14J96ZTehe3+4k26q3ot5dGTvhXTvJSN0r/H/rqqbquoe4KWt3j10U7VeWlXjnv4w4DK6D2Wvq6pL6G7r9Mk2BfZbdLNlaOt8Jd1FLu6hS0SXYR96QlXVCrovld5EdyGQt9IlB7fR3Y5r9HPpUcAv071W7wQ+xfq9Vq8CngZ8m66fXEg3ws14/UUbVq8fnED3ReFX6ZKp5wNfmcSqjqR7n/gR3RdWZ0+w3u/SnaN4J3AJcHJVfWGc8mP2I8Y4vrXYEuCsNjX1t5lBRk/slqTHSPL/gKVV9bEnaHvz6E4if27v4KoZwL6imSbJJnQzaY6qqi9Od3s0vnS3Driuqk5eZ2FJU+YIoqTHSfJCuhunb9DLMic5JN2FL+bSjXJfS3e1M80Q9hXNFG0645ZJNqUbuQqeNvGklOSFbRrfJkl+k2608TPT3S5ptjBBlPQYSc4CLqe7BcGqdZWfopfTTfG4E3gucEQ5rWHGsK9ohvllulMoRqdOH1pVa6a3SRrDs+juszpCd8XjN1bVldPaImkWcYqpJEmSJAlwBFGSJEmS1JggSpIkSZIAE0RJkiRJUmOCKElST5JKcvh0t0OSpOlggihJmnWS/HySh5NM5qbMk1n/opZoXpdkzkDs5iRv2RDblSRpqkwQJUmz0euA04C9kjxvA25nZ+A1G3D9kiQNlQmiJGlWSbI5cCTwUeBC1pHAJdk/yX8meSDJlUle0kYHF01gcx8AliSZO876fy/JN5OsSvKDJBck2b4XHx2NPDjJfyRZk+TLSXZI8uIkVycZSfLZJNsMrPvVSb7d2n59kj9K4nu/JGlMvklIkmabw4Fbquoa4BzgVUmeuraCSeYBnwWuA34BOBH4P5PY1geBh4A3j1PmacDJwN7AS4EFwPlrKfd24E3A/sBWwKeAtwHHAYuAPYElvba/DvjLVuZ5wAnAnwDHT6L9kqRZxgRRkjTbvJYuMQT4ErAaeNkYZY8CngK8pqqWV9UXgHdNYlsPACcBf5xk4doKVNXfVdXnqurGqvoG8EbggCQ7DBQ9qaq+3BLbjwAvAv64qr5eVcuAs4D/3i8PnFhVF1bVTVV1KfBuTBAlSeMwQZQkzRpJngP8CrAUoKoKOI8uaVybPYBvVdWa3rKvD6xzeZviOZLkH9eyjnOAm+kStrW1ad8kf5/kliSrgGUttNNA0Wt6z7/ffl47sOyZbZ0LgR2B03ttG6FLEHcbY18lSWLOuotIkrTReC3diOCtSUaXBSDJjlV120D5ALWOdb4EGJ2iumYwWFU/TfKnwGeSvP8xK+/OTfw8cDlwNPADuimmX6abetr3UH+1bd2Dy0a/+B39+Qbg39fRfkmSHmGCKEmaFdrtJo4B/ozuvMK+c4BXA6cMLP8O3TmKm/dGEX+xX6CqblnXtqvqc+2WGoPTU/egSwjfWlU3tXYeNoHdWdf2vp/kDmC3qjp7quuTJM0eJoiSpNnit+iSsY9W1T39QJJPAm9M8s6BOucB7wQ+muQvge2At7bYukYWB50IfI3HjgTeCvwE+IMkH6a7mMw7JrnesSwBPpjkPuBzdKOc+wLbV9VfDWkbkqSNjOcgSpJmi9cAXxxMDpsL6O5ZeFB/YVWNAIfQXSH0SrormC5p4Qcms/Gq+ibdbTU27S1bQTeqeSjwbbqrmY53xdPJbO9jwO/TTV29mm7a6nHATcNYvyRp45Tu/HxJkjQRSV4OXAI8s6p+ON3tkSRpmJxiKknSOJIcA9wI3AbsBfwNcKnJoSRpY2SCKEnS+Lalu0n9s4G7gcvobjgvSdJGxymmkiRJkiTAi9RIkiRJkhoTREmSJEkSYIIoSZIkSWpMECVJkiRJgAmiJEmSJKkxQZQkSZIkAfD/ATNmv77+sI3AAAAAAElFTkSuQmCC
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
<h2 id="Ohrfeige-Funktion">Ohrfeige-Funktion<a class="anchor-link" href="#Ohrfeige-Funktion">&#182;</a></h2><p>Mit der nachfolgenden Funktion werden auf einen Schlag alle Algorithmen ausgeführt und anschließend vergleichend geplottet.</p>
<p>Mit dieser Funktion können "gut" folgende Punkte der <a href="19112020-ShortListModels">Short-List-Models-Checklist</a> abgeabreitet werden:<br></p>
<ul>
<li><a href="07112020200718-DataModelingQuickDirty">Quick&amp; Dirty Modeling</a><br></li>
<li><a href="07112020200718-MeasurePerofrmance">Measuer-Performance</a><br></li>
<li><a href="07112020200718-FeatureImportance">Feature Importance per Model</a><br></li>
<li><a href="07112020200718-AnalyzingError">Error-Analysis per Model</a><br><br></li>
</ul>
<p>somit bestehen "nur noch" für folgende Aufgaben ein Manueller Handlungsbredarf:<br></p>
<ul>
<li><a href="07112020200718-FeatureSelectionAndEngineering">Feature-Selection</a><br></li>
<li><a href="07112020200718-Repetition">Repetition</a><br></li>
<li><a href="07112020200718-SummaryPromissingModels">Summary</a><br></li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">mean_absolute_error</span>
<span class="kn">from</span> <span class="nn">sklearn.tree</span> <span class="kn">import</span> <span class="n">DecisionTreeRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">svm</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">ohrfeige</span><span class="p">(</span><span class="n">trainData</span><span class="p">,</span> <span class="n">trainLabels</span><span class="p">,</span> <span class="n">testData</span><span class="p">,</span> <span class="n">testLabels</span><span class="p">,</span> <span class="n">DataName</span><span class="p">):</span>
    <span class="n">resultlistOhrfeige</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;OLS&quot;</span><span class="p">,</span>
             <span class="s2">&quot;Lasso&quot;</span><span class="p">,</span>
             <span class="s2">&quot;Decision-Tree&quot;</span><span class="p">,</span>
             <span class="s2">&quot;Random-Forest&quot;</span><span class="p">,</span>
             <span class="s2">&quot;SVM-Linear&quot;</span>
            <span class="p">]</span>   <span class="c1"># &quot;Linear SVM&quot;,</span>

    <span class="n">regressors</span> <span class="o">=</span> <span class="p">[</span>
         <span class="n">LinearRegression</span><span class="p">(),</span>
         <span class="n">Lasso</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.01</span><span class="p">,</span> <span class="n">max_iter</span><span class="o">=</span><span class="mi">1000</span><span class="p">),</span>
         <span class="n">DecisionTreeRegressor</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">),</span>
         <span class="n">RandomForestRegressor</span><span class="p">(</span><span class="n">n_estimators</span><span class="o">=</span><span class="mi">100</span><span class="p">),</span>
         <span class="n">svm</span><span class="o">.</span><span class="n">SVC</span><span class="p">(</span><span class="n">kernel</span><span class="o">=</span><span class="s1">&#39;linear&#39;</span><span class="p">)</span>
         <span class="p">]</span>
    
    <span class="sd">&#39;&#39;&#39;importances = [</span>
<span class="sd">         coef_, </span>
<span class="sd">         coef_, </span>
<span class="sd">         feature_importances_,</span>
<span class="sd">         feature_importances_</span>
<span class="sd">         ]</span>
<span class="sd">         &#39;&#39;&#39;</span>
    
    <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">reg</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">names</span><span class="p">,</span> <span class="n">regressors</span><span class="p">):</span>
        <span class="n">reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">trainData</span><span class="p">,</span> <span class="n">trainLabels</span><span class="p">)</span>
        <span class="n">predictions_reg</span> <span class="o">=</span> <span class="n">reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">testData</span><span class="p">)</span>
        <span class="n">mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">testLabels</span><span class="p">,</span> <span class="n">predictions_reg</span><span class="p">)</span>
        <span class="n">mse</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">testLabels</span><span class="p">,</span> <span class="n">predictions_reg</span><span class="p">)</span>
        <span class="n">rmse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">mse</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">importance</span> <span class="o">=</span> <span class="n">reg</span><span class="o">.</span><span class="n">coef_</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="n">importance</span> <span class="o">=</span> <span class="n">reg</span><span class="o">.</span><span class="n">feature_importances_</span>
        <span class="n">resultlistOhrfeige</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">name</span><span class="p">,</span> <span class="n">mae</span><span class="p">,</span> <span class="n">mse</span><span class="p">,</span> <span class="n">rmse</span><span class="p">,</span> <span class="n">importance</span><span class="p">,</span> <span class="n">predictions_reg</span><span class="p">])</span>
        
    
    <span class="n">titles</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Alg-Name&quot;</span><span class="p">,</span> <span class="s2">&quot;MAE&quot;</span><span class="p">,</span> <span class="s2">&quot;MSE&quot;</span><span class="p">,</span> <span class="s2">&quot;RMSE&quot;</span><span class="p">,</span> <span class="s2">&quot;importance&quot;</span><span class="p">,</span> <span class="s2">&quot;predictions&quot;</span><span class="p">]</span>
    <span class="n">ohrfeigePlotList</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">resultlistOhrfeige</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
    
    <span class="n">ohrfeigePlotList</span> <span class="o">=</span> <span class="n">ohrfeigePlotList</span><span class="p">[[</span><span class="s2">&quot;Alg-Name&quot;</span><span class="p">,</span> <span class="s2">&quot;MAE&quot;</span><span class="p">,</span> <span class="s2">&quot;MSE&quot;</span><span class="p">,</span> <span class="s2">&quot;RMSE&quot;</span><span class="p">]]</span>
    <span class="c1">#ohrfeigePlotList = ohrfeigePlotList.drop(&quot;importance&quot;, axis=1) # drop labels for training set</span>
    <span class="n">ohrfeigePlotList</span> <span class="o">=</span> <span class="n">ohrfeigePlotList</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;Alg-Name&#39;</span><span class="p">)</span>
    <span class="n">axes</span> <span class="o">=</span> <span class="n">ohrfeigePlotList</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">rot</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">subplots</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span><span class="mi">10</span><span class="p">),</span> <span class="n">title</span><span class="o">=</span><span class="n">DataName</span><span class="p">)</span>
    <span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
    
    <span class="n">performanceDFOhrfeige</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">resultlistOhrfeige</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
    <span class="k">return</span><span class="p">(</span><span class="n">performanceDFOhrfeige</span><span class="p">)</span>

<span class="c1"># Bug in Numpy</span>
<span class="c1"># https://stackoverflow.com/questions/63761366/numpy-linalg-linalgerror-svd-did-not-converge-in-linear-least-squares-on-first</span>
<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="k">try</span><span class="p">:</span> 
        <span class="n">results</span> <span class="o">=</span> <span class="n">ohrfeige</span><span class="p">(</span><span class="n">train_set</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="n">test_set</span><span class="p">,</span> <span class="n">test_labels</span><span class="p">,</span> <span class="s2">&quot;DataName&quot;</span><span class="p">)</span>
        <span class="k">break</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="k">continue</span>
        
<span class="nb">print</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
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
&lt;ipython-input-32-78f60f658672&gt;:25: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  reg.fit(trainData, trainLabels)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>        Alg-Name           MAE           MSE           RMSE  \
0            OLS  49483.498062  4.462016e+09   66798.320259   
1          Lasso  49458.054756  4.461389e+09   66793.630247   
2  Decision-Tree  75607.395833  1.227796e+10  110805.964643   
3  Random-Forest  56121.506773  6.121134e+09   78237.677169   

                                          importance  \
0  [[-54351.712905772016, -55446.55764966471, 144...   
1  [-54137.139356899715, -55013.21442234788, 1439...   
2  [0.06593142858806791, 0.05572574053447584, 0.0...   
3  [0.058380217517813755, 0.05585420574300106, 0....   

                                         predictions  
0  [[422400.0], [272448.0], [229056.0], [203968.0...  
1  [422149.5469463768, 272063.34422259615, 228721...  
2  [445400.0, 373700.0, 500001.0, 184200.0, 11630...  
3  [490726.68, 440668.37, 299204.12, 206437.0, 14...  
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Fine-Tuning"><a href="">Fine-Tuning</a><a class="anchor-link" href="#Fine-Tuning">&#182;</a></h1>
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
 

