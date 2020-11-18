'''''

{
"title": "Python Lösungen - SK-Learn Pipelines,
"keywords": "python, SK-Learn, Pipeline ",
"categories": "",
"description": "Hier werden unterschiedliche Methoden aufgezeigt wie Remote Datensätze lokal verfügbar gemacht werden können",
"level": "20",
"pageID": "15112020-SK-Learn-Pipelines-Extended"
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
<h1 id="SK-Learn-Pipelines">SK-Learn Pipelines<a class="anchor-link" href="#SK-Learn-Pipelines">&#182;</a></h1><p>Hier der zweite Teil der SK-Learn notebooks. Nun werden die Feature einerseits mit Namen und anderseits auch per Datentyp angesprochen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Bibliotheken</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Data-Loading">Data-Loading<a class="anchor-link" href="#Data-Loading">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">labelList</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;symboling&#39;</span><span class="p">,</span><span class="s1">&#39;normalizedLosses&#39;</span><span class="p">,</span><span class="s1">&#39;make&#39;</span><span class="p">,</span><span class="s1">&#39;fuelType&#39;</span><span class="p">,</span><span class="s1">&#39;aspiration&#39;</span><span class="p">,</span><span class="s1">&#39;numOfDoors&#39;</span><span class="p">,</span><span class="s1">&#39;body123Style&#39;</span><span class="p">,</span><span class="s1">&#39;driveWheels&#39;</span><span class="p">,</span><span class="s1">&#39;engineLocation&#39;</span><span class="p">,</span>
           <span class="s1">&#39;wheelBase&#39;</span><span class="p">,</span><span class="s1">&#39;length&#39;</span><span class="p">,</span><span class="s1">&#39;width&#39;</span><span class="p">,</span><span class="s1">&#39;height&#39;</span><span class="p">,</span><span class="s1">&#39;curbWeight&#39;</span><span class="p">,</span><span class="s1">&#39;engineType&#39;</span><span class="p">,</span><span class="s1">&#39;numOfCylinders&#39;</span><span class="p">,</span><span class="s1">&#39;engineSize&#39;</span><span class="p">,</span><span class="s1">&#39;fuelSystem&#39;</span><span class="p">,</span><span class="s1">&#39;bore&#39;</span><span class="p">,</span>
           <span class="s1">&#39;stroke&#39;</span><span class="p">,</span><span class="s1">&#39;compressionRatio&#39;</span><span class="p">,</span><span class="s1">&#39;horsepower&#39;</span><span class="p">,</span><span class="s1">&#39;peakRpm&#39;</span><span class="p">,</span><span class="s1">&#39;cityMpg&#39;</span><span class="p">,</span><span class="s1">&#39;highwayMpg&#39;</span><span class="p">,</span><span class="s1">&#39;price&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data_car.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="n">labelList</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;?&quot;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>
<span class="n">df</span><span class="p">[[</span><span class="s1">&#39;price&#39;</span><span class="p">]]</span><span class="o">=</span><span class="n">df</span><span class="p">[[</span><span class="s1">&#39;price&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;float64&#39;</span><span class="p">)</span>
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
RangeIndex: 205 entries, 0 to 204
Data columns (total 26 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   symboling         205 non-null    int64  
 1   normalizedLosses  164 non-null    object 
 2   make              205 non-null    object 
 3   fuelType          205 non-null    object 
 4   aspiration        205 non-null    object 
 5   numOfDoors        203 non-null    object 
 6   body123Style         205 non-null    object 
 7   driveWheels       205 non-null    object 
 8   engineLocation    205 non-null    object 
 9   wheelBase         205 non-null    float64
 10  length            205 non-null    float64
 11  width             205 non-null    float64
 12  height            205 non-null    float64
 13  curbWeight        205 non-null    int64  
 14  engineType        205 non-null    object 
 15  numOfCylinders    205 non-null    object 
 16  engineSize        205 non-null    int64  
 17  fuelSystem        205 non-null    object 
 18  bore              201 non-null    object 
 19  stroke            201 non-null    object 
 20  compressionRatio  205 non-null    float64
 21  horsepower        203 non-null    object 
 22  peakRpm           203 non-null    object 
 23  cityMpg           205 non-null    int64  
 24  highwayMpg        205 non-null    int64  
 25  price             201 non-null    float64
dtypes: float64(6), int64(5), object(15)
memory usage: 41.8+ KB
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">output_features</span> <span class="o">=</span> <span class="p">[</span>
    <span class="s2">&quot;symboling&quot;</span>
<span class="p">]</span>

<span class="n">input_features</span> <span class="o">=</span> <span class="p">[</span>
    <span class="s1">&#39;normalizedLosses&#39;</span><span class="p">,</span>
    <span class="s1">&#39;make&#39;</span><span class="p">,</span>
    <span class="s1">&#39;fuelType&#39;</span><span class="p">,</span>
    <span class="s1">&#39;aspiration&#39;</span><span class="p">,</span>
    <span class="s1">&#39;numOfDoors&#39;</span><span class="p">,</span>
    <span class="s1">&#39;body123Style&#39;</span><span class="p">,</span>
    <span class="s1">&#39;driveWheels&#39;</span><span class="p">,</span>
    <span class="s1">&#39;engineLocation&#39;</span><span class="p">,</span>
    <span class="s1">&#39;wheelBase&#39;</span><span class="p">,</span>
    <span class="s1">&#39;length&#39;</span><span class="p">,</span>
    <span class="s1">&#39;width&#39;</span><span class="p">,</span>
    <span class="s1">&#39;height&#39;</span><span class="p">,</span>
    <span class="s1">&#39;curbWeight&#39;</span><span class="p">,</span>
    <span class="s1">&#39;engineType&#39;</span><span class="p">,</span>
    <span class="s1">&#39;numOfCylinders&#39;</span><span class="p">,</span>
    <span class="s1">&#39;engineSize&#39;</span><span class="p">,</span>
    <span class="s1">&#39;fuelSystem&#39;</span><span class="p">,</span>
    <span class="s1">&#39;bore&#39;</span><span class="p">,</span>
    <span class="s1">&#39;stroke&#39;</span><span class="p">,</span>
    <span class="s1">&#39;compressionRatio&#39;</span><span class="p">,</span>
    <span class="s1">&#39;horsepower&#39;</span><span class="p">,</span>
    <span class="s1">&#39;peakRpm&#39;</span><span class="p">,</span>
    <span class="s1">&#39;cityMpg&#39;</span><span class="p">,</span>
    <span class="s1">&#39;highwayMpg&#39;</span><span class="p">,</span>
    <span class="s1">&#39;price&#39;</span>
<span class="p">]</span>

<span class="n">train_X</span><span class="p">,</span> <span class="n">test_X</span><span class="p">,</span> <span class="n">train_y</span><span class="p">,</span> <span class="n">test_y</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span>
    <span class="n">df</span><span class="p">[</span><span class="n">input_features</span><span class="p">],</span> 
    <span class="n">df</span><span class="p">[</span><span class="n">output_features</span><span class="p">],</span>
    <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span>
<span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train_X</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="n">test_X</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="n">train_y</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="n">test_y</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>((164, 25), (41, 25), (164, 1), (41, 1))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">debug_print</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">debug</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;This method prints some debug information based on a debug parameter.&quot;&quot;&quot;</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">debug</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">&quot;input&quot;</span><span class="p">,</span> <span class="s2">&quot;shape&quot;</span><span class="p">,</span> <span class="s2">&quot;columns&quot;</span><span class="p">,</span> <span class="kc">False</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Debug parameter value is not valied.&quot;</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">debug</span><span class="o">==</span><span class="s2">&quot;input&quot;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">X</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>
    <span class="k">elif</span> <span class="n">debug</span><span class="o">==</span><span class="s2">&quot;shape&quot;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">X</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">debug</span><span class="o">==</span><span class="s2">&quot;columns&quot;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">X</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">debug</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
        <span class="k">pass</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">PriceImputer</span><span class="p">():</span>
    <span class="sd">&quot;&quot;&quot;Imputs Price with median price of car-Brand.&quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">=</span> <span class="n">debug</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> <span class="o">=</span> <span class="kc">None</span>
    
    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>
    
    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">):</span>
        <span class="n">debug_print</span><span class="p">(</span><span class="n">X</span><span class="o">=</span><span class="n">X</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">d</span><span class="p">)</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">X</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="c1"># Es wird der durschnittliche Preis der jeweiligen Marke imputet</span>
        <span class="n">df</span><span class="o">.</span><span class="n">price</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;make&#39;</span><span class="p">])[</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">median</span><span class="p">()))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">df</span>
    
    <span class="k">def</span> <span class="nf">get_feature_names</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">OHE</span><span class="p">():</span>
    <span class="sd">&quot;&quot;&quot;OHE on the Object-Variables&quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">=</span> <span class="n">debug</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> <span class="o">=</span> <span class="kc">None</span>
    
    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>
    
    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">):</span>
        <span class="n">interimLabelListdf</span> <span class="o">=</span> <span class="n">X</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="s1">&#39;object&#39;</span><span class="p">)</span>
        <span class="n">interimLabelList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">interimLabelListdf</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
        <span class="n">ohe</span> <span class="o">=</span> <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">sparse</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="n">npArray</span> <span class="o">=</span> <span class="n">ohe</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X</span><span class="p">[</span><span class="n">interimLabelList</span><span class="p">])</span>
        <span class="n">titles</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">singleList</span> <span class="ow">in</span> <span class="n">ohe</span><span class="o">.</span><span class="n">categories_</span><span class="p">:</span>
            <span class="n">titles</span> <span class="o">=</span> <span class="n">titles</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">singleList</span><span class="p">)</span>
        <span class="n">interimDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">npArray</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">X</span><span class="p">,</span> <span class="n">interimDF</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">sort</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">interimLabelList</span><span class="p">),</span><span class="mi">1</span><span class="p">):</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="n">interimLabelList</span><span class="p">[</span><span class="n">i</span><span class="p">]],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
            <span class="c1">#train_X = train_X.drop([&#39;normalizedLosses&#39;], axis=1)</span>
        <span class="k">return</span> <span class="n">df</span>
    
    
    <span class="k">def</span> <span class="nf">get_feature_names</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="kn">import</span> <span class="n">Pipeline</span>

<span class="k">class</span> <span class="nc">FeaturePipeline</span><span class="p">(</span><span class="n">Pipeline</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">get_feature_names</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">get_feature_names</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Selectoren</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">FeatureSelector</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;This transformer lets you pick columns from a pandas dataset based on name&quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">features</span> <span class="o">=</span> <span class="p">[],</span> <span class="n">debug</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">=</span> <span class="n">debug</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">features</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">list</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Input features must be of type List.&quot;</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">features</span><span class="p">)</span> <span class="o">==</span> <span class="nb">list</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="n">features</span>

    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">):</span>
        <span class="n">debug_print</span><span class="p">(</span><span class="n">X</span><span class="o">=</span><span class="n">X</span><span class="p">,</span> <span class="n">debug</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">d</span><span class="p">)</span>
        <span class="n">X</span> <span class="o">=</span> <span class="n">X</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">columns</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span> <span class="o">=</span> <span class="n">X</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">X</span>
    
    <span class="k">def</span> <span class="nf">get_feature_names</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">colnames</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># DataType</span>
<span class="kn">from</span> <span class="nn">sklearn.base</span> <span class="kn">import</span> <span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span>
<span class="k">class</span> <span class="nc">TypeSelector</span><span class="p">(</span><span class="n">BaseEstimator</span><span class="p">,</span> <span class="n">TransformerMixin</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;This transformer lets you pick columns from a pandas dataset based on Datatype&quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dtype</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dtype</span> <span class="o">=</span> <span class="n">dtype</span>

    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">X</span><span class="p">):</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">X</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">dtype</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="kn">import</span> <span class="n">Pipeline</span><span class="p">,</span> <span class="n">FeatureUnion</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">RobustScaler</span><span class="p">,</span> <span class="n">OneHotEncoder</span>
<span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span>
<span class="n">debug_state</span> <span class="o">=</span> <span class="kc">False</span>
<span class="c1"># Definition Pipeline</span>
<span class="n">pipe</span> <span class="o">=</span> <span class="n">FeaturePipeline</span><span class="p">(</span>
    <span class="p">[</span>

        <span class="p">(</span><span class="s2">&quot;price_imputationName&quot;</span><span class="p">,</span> <span class="n">PriceImputer</span><span class="p">(</span><span class="n">debug</span><span class="o">=</span><span class="kc">False</span><span class="p">)),</span>
        <span class="c1">#(&quot;OHE&quot;, OHE(debug=False)),</span>
    <span class="p">]</span>
<span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">pipe_tools.pipe_visualizer</span> <span class="kn">import</span> <span class="n">plot_pipeline</span>
<span class="n">plot_pipeline</span><span class="p">(</span><span class="n">pipe</span><span class="p">,</span> <span class="s2">&quot;pipeline_plot.png&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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VuSv//qvd9tnYGAgb3rTm3LkkUfmqaeeyjPPPJMLL7wwyY4QcfXVV+fv//7vs3bt2pxxxhl55zvfOeK5brrppnz2s5/NunXrMm3atJx++uk5/vjjc8899+QNb3jDHreb3Hrrrbn++utz++23Z8WKFbn++usPeI5ly5blnHPOyfvf//488MAD+cu//MskycKFC/Ptb3879913Xz70oQ/l4x//eNauXZtFixblyiuvzCte8Yo88MADuffee/c45k9+8pN85StfyZe+9KX80z/9U+bPnz/0u9nplltuyU9/+tP8/Oc/z0033ZQ777xzt/evuuqqXHvttdmwYcMex29tbc21116bdevW5b777stdd92Vr371q7ttc8cdd+RnP/tZ7r///nzhC1/IBz/4wXznO9/J008/nV/84hf57ne/myT5t3/7t/zBH/xBrr/++qxfvz4XX3xxzjvvvLpdywUAAIDmUFdh5LLLLsvChQsza9asXHHFFUN/NLe0tOTTn/50pk2blo6Ojt32eeCBB7J69ep88YtfzPTp09Pe3p7f/d3fTZJcf/31+fjHP54TTjghbW1tufzyy/Pwww8P66qRXZ1//vl55Stfmfb29px//vlpb2/Peeedl9bW1px99tl59NFHd9v+ne98Zw477LAccsghueiii3L77beP+ndy1lln5dBDD01LS0vOPvvsHHHEEfn3f//3Ye1766235vzzz8+JJ56YqVOn5iMf+Ujuu+++PPXUU0PbfOxjH0tnZ2eOOOKIvO51r8vDDz+82zFOOumkvPGNb8w111yzx/Ff+cpX5rTTTktbW1uOOuqoXHzxxfnnf/7n3bb56Ec/mpkzZ+Z3fud38rKXvSxvfOMbs2jRohxyyCFZunRpHnrooSTJ17/+9Vx88cU59dRT09ramve+972ZNm1a7r///hH+xgAAAGD46iqMLFy4cOj7I488cui2j7lz56a9vX2v+zz99NM58sgj09bWtsd7K1asyB/90R+ls7MznZ2dmTVrVqrVap555pkRzTVv3ryh7zs6OjJv3ryhW07a29uzdevW3bY/7LDDhr4//PDDs3bt2hGdb1f/+I//mLe97W1ZsmRJlixZkuXLl+c3v/nNsPZds2ZN5s+fP/Tz9OnTM3v27N0+/66zHnTQQdmyZcsex/nMZz6Tr33ta3nuued2e/2xxx7Lm970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KJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWMIIAAAAUCxhBAAAACiWMAIAAAAUSxgBAAAAiiWMAAAAAMUSRgAAAIBiCSMAAABAsYQRAAAAoFjCCAAAAFAsYQQAAAAoljACAAAAFEsYAQAAAIoljAAAAADFEkYAAACAYgkjAAAAQLGEEQAAAKBYwggAAABQLGEEAAAAKJYwAgAAABRLGAEAAACKJYwAAAAAxRJGAAAAgGIJIwAAAECxhBEAAACgWJVqtVqt9RAkt9xyS7761a/ml7/8ZWbMmJGjjz46f/Znf5ZXvOIVtR4NAAAAmpYrRurE9u3b86Mf/SgrV67Mr371q9x+++2ZOnVqrccCAACApiaM1Im3vvWtOeqoo5IklUolb3rTm3LCCSfUdigAAABocsJInahUKvnCF76Qtra2tLW15fOf/3ytRwIAAICmZ42ROlKtVtPV1ZUjjjgijzzySK3HAQAAgKYnjNTa9i3JxoeSjQ8nfRvyzIrHctD0GemasyBpPzSZ9V+Tzpcnre21nhQAAACajjAy2aqDybM/Sp74erLu/mTbmqStIxnoSwa37bJhJWntSCptyUBPMn1hMvf/ShZ/KJlzSs3GBwAAgGYijEyW3g3JE99IHv1y0r9lx7+RqrQkLe3JQQuTEz+aHPmOpO2g8Z8VAAAACiGMTLTBgeQ/vpD84qoklWRg6/gct23GjuO9+rrkqHcmlcr4HBcAAAAKIoxMpE2PJv/vsmTLr5OB7ok5R+v0ZO5rktO/nXQcNjHnAAAAgCYljEyEanXHLTOPXJkM9CYZnNjzVabsWJz1tBuTIy6Y2HMBAABAExFGxlu1mvzsw8kT3xy/22aGq7Uj+a9fThZfMrnnBQAAgAbVVusBmkq1mvz0kuTX35n8KJLseHrNv30kGexPjrts8s8PAAAADaal1gM0lZ9f/tsoMkHriQzHQE/y8P/aMQcAAACwX26lGS/P/Tj557fU5kqRvWk9KDnnkeTgY2o9CQAAAPx/7d1pjF1lHcfx3713ptOZrnSmiCkMiBJDIRJCgVaJaEBTEuIC0hJQMZEmBgSNCsRKUjQ1GmINiwRJBAFBAgaCivuLNlIaF1RAiLSUgCEsXSh1CnSZ5friEkppaCf3Tntu53w+SZPpac85/8zLb57nOW3LipGxMLgleei89okiSTKyLVm5MKnv44NfAQAA4AAmjIyFhy9JhrYUPcWu6iPJwJPJ6muLngQAAADalq00rVr/YLJ8fnutFnmrWk9y5pPJpMOKngQAAADajhUjrfr3d9o3iiRJfShZc33RUwAAAEBbEkZa8dpzyYYHi55iz0Z2JGtvSoa3Fz0JAAAAtB1hpBVrbih6gtGpjyTP3Vf0FAAAANB2nDHSrJHh5N7eZPB/RU8yOgcdn5zxz6KnAAAAgLZixUiztqxJ6sNFTzF6mx9PhncUPQUAAAC0lY6iBzhgbXo4t64YzLJfJ0+vT6Z2J5+ek3xvYTJ9UvKFHyeHzkiWLth5y7Mbkvd8NRm8PZm+aOf113ckXR1J7Y1MddMXk6deSr77y8b1jloye1ay7Pxk3lHJVfcma9cld1y060iV85OnliWf/GHy342Na1t3JJ0dSUd1MFk0PYsXX5nFixfv298NAAAAHCCEkSYtu/bGXH3n9tz2peS0Y5LnX0ku+mnyse8nDy3Z+/2v3rLz5yO+kvxkUXL6sTuvXXVvsnBuI34MDiXfuic565rkhR/t/dlPXL3z548sTT77oeTC03uSE65J3rfonW8EAACAkrGVpgkDAwNZctNfc/0FyfzjGisyjpiZ3HNpY6XGHSvH9n2dHckFH05e2py8/GqTDxl+PdkwxoMBAADAAU4YacKqVauybcdIzjpx1+uTJyZnHJf86fGxfd/2weTWPze25vRNaeFBA6vHbCYAAAAYD2ylacLGjRvTN6WSjtruH/R59/TkH88ksw5q/T33/CV54F/JhI7k2EOT+7/W4gOHt7Y+FAAAAIwjwkgT+vr6snFLPUPDjYNR3+rFzY1VHR21ZPBtH60ZHE6qlcaf0Vgwd/cDVpOko9o4d2SXZ7/x987a7v//TSNDe/hHAAAAKB9baZowb968dHUm9/191+uvbUt+92jjMNb+3sZXaN7qmfXJYb1JtcXfen9f8uzGtz17Q+OrNrNm7OHGWldrLwYAAIBxRhhpwrRp07JkweRcclvy+0cbqzWe3ZCcc13jHJDPnZKcfVLym0eSPz6WDI8kL7ySLL0/OXde6++f/4Fk9YvJzx5svHvTq8niu5PPnLT7CpZddLZyQAkAAACMP7bSNOnyz89J78QV+cbPk6fXJVO7k0/NSe68OOnqTI45NLnry8k3707WXpdM72lsjVlyVuvvPnha8tvLksvvSi69Peme0Dj09Qfn7+muStJ7cusvBwAAgHGkUq/Xdz9BlL177NvJE0uT+gFybkfH1GTuLUn/2UVPAgAAAG3DVppm9Z6YdEwqeorRqw8lvXOKngIAAADaijDSrBknJMPbip5i9CqVpKe/6CkAAACgrQgjzep+VzLlqKKnGJ1KNZn1iUYcAQAAAN4kjLRi9uVJx+Sip9i76sTk6K8XPQUAAAC0HWGkFf3nFD3B6Ew6vLH1BwAAANiFMNKK2sTkvRcm1QlFT/LOOiYls68oegoAAABoS8JIq2ZfkVS7ip7inXXNTA4/t+gpAAAAoC0JI63qPiQ58cak1oaf7q11J6f8Iqm1cbgBAACAAgkjY+GI85KZH0wqnUVPslOtJznq4qR3TtGTAAAAQNuq1Ov1etFDjAtbX0oeeH8yOFD0JEmllvT0J2f+x2oRAAAA2AMrRsZK9yHJR//QBltqKsmE6cnpy0URAAAA2AthZCz1zU1O/VVjG0shqm9EkZWNT/QCAAAAe2Qrzb6wYVWyfH4y/FpSH9k/76xOSCbMSD7+UDL5yP3zTgAAADjACSP7ypa1ycqFycDqRiDZl2o9ySGnJSffkkzs27fvAgAAgHFEGNmX6iPJk9ckj12ZjGwf+9Uj1QmNT/KefHPSf/bYPhsAAABKQBjZH7asTR6+NFm3PEm9EUlaUetJMpL0L0iOX2aVCAAAADRJGNmfXn8+eerGZM0NjdUjw1uT+uDo7q12NVaIdE5Njr4sOfKCxkGrAAAAQNOEkSKMDCbrViQv/y1ZvyLZ9EgyNJBUO7PzQ0EjyfCOZOLMZMac5OBTG1+96ZuXVCrFzQ4AAADjiDDSLrZvSgY3J0Nbk0o1qU1MuvqSzilFTwYAAADjljACAAAAlFZ17/8FAAAAYHwSRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0hJGAAAAgNISRgAAAIDSEkYAAACA0vo/cFLkMeqkacUAAAAASUVORK5CYII=
"
>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">train_X</span><span class="o">.</span><span class="n">price</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">train_X</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">train_X_prepared</span> <span class="o">=</span> <span class="n">pipe</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">train_X</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">train_X_prepared</span><span class="o">.</span><span class="n">price</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">train_X_prepared</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>True
(164, 25)
False
(164, 25)
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
 

