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
<div class="prompt input_prompt">In&nbsp;[48]:</div>
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

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>117353.23231589147
27098628985.039486
78536.23989728655
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
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
<div class="prompt input_prompt">In&nbsp;[50]:</div>
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
<pre>[[&#39;OLS&#39;, 49483.498062015504, 4462015589.36531, 66798.32025856122], [&#39;Poly-Reg&#39;, 49458.03301952227, 4461384770.505101, 66793.59827487289], [&#39;Poly-Reg&#39;, 49458.03301952227, 4461384770.505101, 66793.59827487289], [&#39;Lasso-Reg&#39;, 49458.05475606995, 4461389041.578401, 66793.63024704078], [&#39;RegTree&#39;, 75607.39583333333, 12277961800.540213, 110805.96464333593], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655], [&#39;RandForest&#39;, 56528.563829941864, 6167940977.204143, 78536.23989728655], [&#39;SVM&#39;, 117353.23231589147, 27098628985.039486, 78536.23989728655]]
9
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
<pre>                      MAE           MSE           RMSE
Alg-Name                                              
OLS          49483.498062  4.462016e+09   66798.320259
Poly-Reg     49458.033020  4.461385e+09   66793.598275
Poly-Reg     49458.033020  4.461385e+09   66793.598275
Lasso-Reg    49458.054756  4.461389e+09   66793.630247
RegTree      75607.395833  1.227796e+10  110805.964643
RandForest   56528.563830  6.167941e+09   78536.239897
RandForest   56528.563830  6.167941e+09   78536.239897
RandForest   56528.563830  6.167941e+09   78536.239897
SVM         117353.232316  2.709863e+10   78536.239897
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
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

    <div class="prompt output_prompt">Out[52]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x1f4bf80a610&gt;</pre>
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
<div class="prompt input_prompt">In&nbsp;[53]:</div>
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
<div class="prompt input_prompt">In&nbsp;[54]:</div>
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
&lt;ipython-input-54-5b712e516128&gt;:20: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  reg.fit(trainData, trainLabels)
C:\Users\1810837475\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>        Alg-Name            MAE           MSE           RMSE  \
0            OLS   49483.498062  4.462016e+09   66798.320259   
1          Lasso   49458.054756  4.461389e+09   66793.630247   
2  Decision-Tree   75607.395833  1.227796e+10  110805.964643   
3  Random-Forest   56745.107323  6.290655e+09   79313.646527   
4     SVM-Linear  117353.232316  2.709863e+10  164616.612117   

                                          importance  \
0  [[-54351.712905772016, -55446.55764966471, 144...   
1  [-54137.139356899715, -55013.21442234788, 1439...   
2  [0.06593142858806791, 0.05572574053447584, 0.0...   
3  [0.0584072463130713, 0.05506386172811656, 0.04...   
4  [[0.2783439229196297, 0.16175094244728438, -0....   

                                         predictions  
0  [[422400.0], [272448.0], [229056.0], [203968.0...  
1  [422149.5469463768, 272063.34422259615, 228721...  
2  [445400.0, 373700.0, 500001.0, 184200.0, 11630...  
3  [482865.64, 421764.35, 295235.08, 192686.0, 14...  
4  [500001.0, 500001.0, 500001.0, 112500.0, 11250...  
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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SpIkSZIaM+4ppgsXLqyhoaFelyFJkiRJPXH11VffXVWLJuubcQFxaGiI4eHhXpchSZIkST2RZNWm+txiKkmSJEkCDIiSJEmSpIYBUZIkSZIEzMB7ECfz0EMPMTo6yvr163tdypSbPXs2ixcvZscdd+x1KZIkSZJ6zIAIjI6OMm/ePIaGhkjS63KmTFWxevVqRkdHWbJkSa/LkSRJktRjbjEF1q9fz4IFC2ZUOARIwoIFC2bkyqkkSZKkR3MFsTHTwuGEmXrdkiRJggM+c0CvSxgo159wfa9L2GauIEqSJEmSAFcQJ9Xtv6RsyV8SdthhBw444AAefvhhlixZwvLly9l1110ZGRlhyZIlnH766bzvfe8D4O677+bJT34yJ598Mp/4xCf4yU9+wsknn8y9997LAw88wGGHHca5557LlVdeyVFHHbXR/YV/8zf/r707j7erqu8+/vlCkFBCGCM1QVFQhAYKaixqyyMqVlFRBBQKKoOK1gcHpOKEBRVnqC1WW6BSAZmKIAooirYoTmisICBIH4YICBoCxATCUPw9f+x1w8nh5ube5CY3uffzfr3Oi3P22mvttcO6++zfXsM5jt12221Uz0+SJEnS+GAP4mpivfXW48orr+Saa65hk0024fOf//zitK222oqLLrpo8edzzz2XmTNnLv78jne8g8MPP5wrr7yS6667jre//e2L03bZZReuvPLKxS+DQ0mSJElLY4C4Gnruc5/L7bffvvjzeuutx3bbbcfs2bMBOOecc3jta1+7OP2OO+5giy22WPx5hx0cSy5JkiRp5AwQVzOPPPII3/3ud3nlK1+5xPb99tuPs88+m9tuu421116b6dOnL047/PDDeeELX8juu+/OZz/7We69997FaZdffjk77bTT4teNN964ys5FkiRJ0prFAHE1sWjRInbaaSc23XRT7r77bl784hcvkf7Sl76USy+9lLPOOot99913ibSDDz6Y6667jte85jVcdtllPOc5z+HBBx8EHjvEdOutt15l5yRJkiRpzWKAuJoYmIM4Z84cHnrooSXmIAI87nGP41nPehbHH388e++992PyT58+nUMOOYSvfe1rTJo0iWuuuWZVVV2SJEnSOGGAuJrZcMMNOeGEEzjuuON4+OGHl0g74ogj+NSnPsWmm266xPZLLrlk8b533nkn8+bNY8aMGauszpIk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
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
 
