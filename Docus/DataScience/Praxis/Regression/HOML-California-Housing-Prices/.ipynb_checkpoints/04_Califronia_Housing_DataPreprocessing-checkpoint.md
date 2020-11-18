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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
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
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">strat_train_set</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">housing</span> <span class="o">=</span> <span class="n">strat_train_set</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;median_house_value&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># drop labels for training set</span>
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
<pre>(16512, 12)
(16512, 11)
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
<h1 id="1.-Data-Cleaning---NAN-Values"><a href="07112020200718-DataCleaning">1. Data-Cleaning - NAN-Values</a><a class="anchor-link" href="#1.-Data-Cleaning---NAN-Values">&#182;</a></h1><p>Aus dem <a href="14112020-10-California-Housing-Data">Data-Management-Notebook</a> ist klar, dass NAN/0/"" Werte in dem Feature "total bedrooms" existieren. Diese Werte werden nun in dieser Rubrik behandelt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">missingno</span> <span class="k">as</span> <span class="nn">msno</span>
<span class="n">msno</span><span class="o">.</span><span class="n">matrix</span><span class="p">(</span><span class="n">housing</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Imputation">Imputation<a class="anchor-link" href="#Imputation">&#182;</a></h2><p>In dieser Lösung entscheide ich mich dazu eine Imputaion durchzuführen. Ander Lösungen finden sich in diesem <a href="16112020-NAWerte">Notebook</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span> <span class="c1"># Scikit-Learn 0.20+</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">Imputer</span> <span class="k">as</span> <span class="n">SimpleImputer</span>
<span class="n">imputer</span> <span class="o">=</span> <span class="n">SimpleImputer</span><span class="p">(</span><span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;median&quot;</span><span class="p">)</span>
<span class="c1"># erstellen eines Sub-DF welches nur die numerischen Werte beinhaltet</span>
<span class="n">housing_num</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">imputer</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="c1"># imputer.statistics_</span>
<span class="c1"># housing_num.median().values</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing_tr</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#print(housing_tr.isnull().any())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#print(housing.isnull().any())</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="2.-Feature-Selection"><a href="07112020200718-FeatureSelection">2. Feature-Selection</a><a class="anchor-link" href="#2.-Feature-Selection">&#182;</a></h1><p>Im konkreten Beispiel verwende ich alle gegebenen Feature des Datensatzes</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="3.-Feature-Engineering"><a href="07112020200718-FeatureEngineering">3. Feature-Engineering</a><a class="anchor-link" href="#3.-Feature-Engineering">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="One-Hot-Encoding">One Hot Encoding<a class="anchor-link" href="#One-Hot-Encoding">&#182;</a></h2><p>für die kategorischen Variablen check out das <a href="16112020-OneHotEncodingOrdinalEncoding">OHE-Notebook</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OrdinalEncoder</span> <span class="c1"># just to raise an ImportError if Scikit-Learn &lt; 0.20</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">future_encoders</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span> <span class="c1"># Scikit-Learn &lt; 0.20</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_cat</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[[</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">]]</span>
<span class="n">housing_cat</span><span class="o">.</span><span class="n">shape</span>
<span class="n">cat_encoder</span> <span class="o">=</span> <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">sparse</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">housing_ocean_proximity_cat_1hot</span> <span class="o">=</span> <span class="n">cat_encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>
<span class="n">titles</span> <span class="o">=</span> <span class="n">cat_encoder</span><span class="o">.</span><span class="n">get_feature_names</span><span class="p">([</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">])</span>
<span class="n">partOHEdf</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">housing_ocean_proximity_cat_1hot</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">partOHEdf</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Zusammenf&#252;gen-des-OHE-&amp;-Imputer-DF">Zusammenf&#252;gen des OHE &amp; Imputer DF<a class="anchor-link" href="#Zusammenf&#252;gen-des-OHE-&amp;-Imputer-DF">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housingDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">housing_tr</span><span class="p">,</span><span class="n">partOHEdf</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housingDF</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housingDF</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Creation</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.base</span> <span class="kn">import</span> <span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span>
<span class="c1"># get the right column indices: safer than hard-coding indices 3, 4, 5, 6</span>
<span class="n">rooms_ix</span><span class="p">,</span> <span class="n">bedrooms_ix</span><span class="p">,</span> <span class="n">population_ix</span><span class="p">,</span> <span class="n">household_ix</span> <span class="o">=</span> <span class="p">[</span>
    <span class="nb">list</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">col</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="p">(</span><span class="s2">&quot;total_rooms&quot;</span><span class="p">,</span> <span class="s2">&quot;total_bedrooms&quot;</span><span class="p">,</span> <span class="s2">&quot;population&quot;</span><span class="p">,</span> <span class="s2">&quot;households&quot;</span><span class="p">)]</span>

<span class="k">class</span> <span class="nc">CombinedAttributesAdder</span><span class="p">(</span><span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">add_bedrooms_per_room</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span> <span class="c1"># no *args or **kwargs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_bedrooms_per_room</span> <span class="o">=</span> <span class="n">add_bedrooms_per_room</span>
    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>  <span class="c1"># nothing else to do</span>
    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="n">rooms_per_household</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">rooms_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">household_ix</span><span class="p">]</span>
        <span class="n">population_per_household</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">population_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">household_ix</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_bedrooms_per_room</span><span class="p">:</span>
            <span class="n">bedrooms_per_room</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">bedrooms_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">rooms_ix</span><span class="p">]</span>
            <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">X</span><span class="p">,</span> <span class="n">rooms_per_household</span><span class="p">,</span> <span class="n">population_per_household</span><span class="p">,</span>
                         <span class="n">bedrooms_per_room</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">X</span><span class="p">,</span> <span class="n">rooms_per_household</span><span class="p">,</span> <span class="n">population_per_household</span><span class="p">]</span>

<span class="n">attr_adder</span> <span class="o">=</span> <span class="n">CombinedAttributesAdder</span><span class="p">(</span><span class="n">add_bedrooms_per_room</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">housing_extra_attribs</span> <span class="o">=</span> <span class="n">attr_adder</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing_extra_attribs</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="4.-Feature-Scaling"><a href="07112020200718-FeatureScaling">4. Feature Scaling</a><a class="anchor-link" href="#4.-Feature-Scaling">&#182;</a></h1><p>wichtig ist, dass die Skalierungen später(nach den Predictions) wieder zurück skaliert werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housingDF</span><span class="o">.</span><span class="n">dtypes</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">MinMaxScaler</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">MinMaxScaler</span><span class="p">()</span>
<span class="c1">#print(housing_tr)</span>
<span class="n">scaler</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">housingDF</span><span class="p">)</span>
<span class="n">housing_tr_scaled</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housingDF</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing_tr_scaled</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#print(houhousingDF.colsing_tr_scaled)</span>
<span class="n">titles</span> <span class="o">=</span> <span class="n">housingDF</span><span class="o">.</span><span class="n">columns</span>
<span class="n">finalPreporcessedDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">housing_tr_scaled</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">finalPreporcessedDF</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">finalPreporcessedDF</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="5.-SK-Learn-Pipeline"><a href="07112020200718-FeatureScaling">5. SK-Learn Pipeline</a><a class="anchor-link" href="#5.-SK-Learn-Pipeline">&#182;</a></h1><p>Die oberen Schritte waren bisher primär für die Entwicklung. Für einen vernünftigen Einsatz werden nun <a href="">SK-Learn Pipelines</a> verwendet.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">()</span>
<span class="n">strat_test_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_test_set.csv&quot;</span><span class="p">)</span>
<span class="n">strat_train_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_train_set.csv&quot;</span><span class="p">)</span>
<span class="n">housing_num</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">housing_cat</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ocean_proximity&quot;</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">FunctionTransformer</span>

<span class="k">def</span> <span class="nf">add_extra_features</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">add_bedrooms_per_room</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
    <span class="n">rooms_per_household</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">rooms_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">household_ix</span><span class="p">]</span>
    <span class="n">population_per_household</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">population_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">household_ix</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">add_bedrooms_per_room</span><span class="p">:</span>
        <span class="n">bedrooms_per_room</span> <span class="o">=</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">bedrooms_ix</span><span class="p">]</span> <span class="o">/</span> <span class="n">X</span><span class="p">[:,</span> <span class="n">rooms_ix</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">X</span><span class="p">,</span> <span class="n">rooms_per_household</span><span class="p">,</span> <span class="n">population_per_household</span><span class="p">,</span>
                     <span class="n">bedrooms_per_room</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">X</span><span class="p">,</span> <span class="n">rooms_per_household</span><span class="p">,</span> <span class="n">population_per_household</span><span class="p">]</span>

<span class="n">attr_adder</span> <span class="o">=</span> <span class="n">FunctionTransformer</span><span class="p">(</span><span class="n">add_extra_features</span><span class="p">,</span> <span class="n">validate</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                                 <span class="n">kw_args</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;add_bedrooms_per_room&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">})</span>
<span class="n">housing_extra_attribs</span> <span class="o">=</span> <span class="n">attr_adder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_extra_attribs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span>
    <span class="n">housing_extra_attribs</span><span class="p">,</span>
    <span class="n">columns</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span><span class="o">+</span><span class="p">[</span><span class="s2">&quot;rooms_per_household&quot;</span><span class="p">,</span> <span class="s2">&quot;population_per_household&quot;</span><span class="p">],</span>
    <span class="n">index</span><span class="o">=</span><span class="n">housing</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">housing_extra_attribs</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="kn">import</span> <span class="n">Pipeline</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>

<span class="n">num_pipeline</span> <span class="o">=</span> <span class="n">Pipeline</span><span class="p">([</span>
        <span class="p">(</span><span class="s1">&#39;imputer&#39;</span><span class="p">,</span> <span class="n">SimpleImputer</span><span class="p">(</span><span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;median&quot;</span><span class="p">)),</span>
        <span class="p">(</span><span class="s1">&#39;attribs_adder&#39;</span><span class="p">,</span> <span class="n">FunctionTransformer</span><span class="p">(</span><span class="n">add_extra_features</span><span class="p">,</span> <span class="n">validate</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
        <span class="p">(</span><span class="s1">&#39;std_scaler&#39;</span><span class="p">,</span> <span class="n">StandardScaler</span><span class="p">()),</span>
    <span class="p">])</span>

<span class="n">cat_pipeline</span> <span class="o">=</span> <span class="n">Pipeline</span><span class="p">([</span>
        <span class="p">(</span><span class="s1">&#39;OHE&#39;</span><span class="p">,</span> <span class="n">OneHotEncoder</span><span class="p">())</span>
    <span class="p">])</span>

<span class="n">housing_num_tr</span> <span class="o">=</span> <span class="n">num_pipeline</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="n">housing_num_tr</span>
<span class="kn">from</span> <span class="nn">pipe_tools.pipe_visualizer</span> <span class="kn">import</span> <span class="n">plot_pipeline</span>
<span class="n">plot_pipeline</span><span class="p">(</span><span class="n">num_pipeline</span><span class="p">,</span> <span class="s2">&quot;pipeline_plot.png&quot;</span><span class="p">)</span>
<span class="n">plot_pipeline</span><span class="p">(</span><span class="n">cat_pipeline</span><span class="p">,</span> <span class="s2">&quot;pipeline_plot.png&quot;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.compose</span> <span class="kn">import</span> <span class="n">ColumnTransformer</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;SK-Learn Version passt&quot;</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">future_encoders</span> <span class="kn">import</span> <span class="n">ColumnTransformer</span> <span class="c1"># Scikit-Learn &lt; 0.20</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Alte Version&quot;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">num_attribs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="n">cat_attribs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>


<span class="n">full_pipeline</span> <span class="o">=</span> <span class="n">ColumnTransformer</span><span class="p">([</span>
        <span class="p">(</span><span class="s2">&quot;num&quot;</span><span class="p">,</span> <span class="n">num_pipeline</span><span class="p">,</span> <span class="n">num_attribs</span><span class="p">),</span>
        <span class="p">(</span><span class="s2">&quot;cat&quot;</span><span class="p">,</span> <span class="n">OneHotEncoder</span><span class="p">(),</span> <span class="n">cat_attribs</span><span class="p">),</span>
    <span class="p">])</span>

<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">housing_prepared</span> <span class="o">=</span> <span class="n">full_pipeline</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_prepared</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
 

