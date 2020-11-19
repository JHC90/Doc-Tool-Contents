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
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">train_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;train-prepared-Feature.csv&quot;</span><span class="p">)</span>
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

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\nprint(train_set.head123())\nprint(train_labels.head123())\nprint(test_set.head123())\nprint(test_labels.head123())\n&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>       longitude  latitude  housing_median_age  total_rooms  total_bedrooms  \
index                                                                         
17606  -1.156043  0.771950            0.743331    -0.493234       -0.445438   
18632  -1.176025  0.659695           -1.165317    -0.908967       -1.036928   
14650   1.186849 -1.342183            0.186642    -0.313660       -0.153345   
3230   -0.017068  0.313576           -0.290520    -0.362762       -0.396756   
3555    0.492474 -0.659299           -0.926736     1.856193        2.412211   

       population  households  median_income  ocean_proximity  income_cat  \
index                                                                       
17606   -0.636211   -0.420698      -0.614937        -0.954456   -0.312055   
18632   -0.998331   -1.022227       1.336459         1.890305    0.217683   
14650   -0.433639   -0.093318      -0.532046        -0.954456   -0.465315   
3230     0.036041   -0.383436      -1.045566        -0.954456   -0.079661   
3555     2.724154    2.570975      -0.441437        -0.006202   -0.357834   

       rooms_per_household  population_per_household  \
index                                                  
17606            -0.086499                  0.155318   
18632            -0.033534                 -0.836289   
14650            -0.092405                  0.422200   
3230              0.089736                 -0.196453   
3555             -0.004194                  0.269928   

       ocean_proximity_&lt;1H OCEAN  ocean_proximity_INLAND  \
index                                                      
17606                        1.0                     0.0   
18632                        1.0                     0.0   
14650                        0.0                     0.0   
3230                         0.0                     1.0   
3555                         1.0                     0.0   

       ocean_proximity_ISLAND  ocean_proximity_NEAR BAY  \
index                                                     
17606                     0.0                       0.0   
18632                     0.0                       0.0   
14650                     0.0                       0.0   
3230                      0.0                       0.0   
3555                      0.0                       0.0   

       ocean_proximity_NEAR OCEAN  
index                              
17606                         0.0  
18632                         0.0  
14650                         1.0  
3230                          0.0  
3555                          0.0  
       median_house_value
index                    
17606            286600.0
18632            340600.0
14650            196900.0
3230              46300.0
3555             254500.0
       longitude  latitude  housing_median_age  total_rooms  total_bedrooms  \
index                                                                         
5241    0.574715 -0.696209            0.032860     1.602628        1.026552   
10970   0.838394 -0.860742            0.824710     0.627178        0.236392   
20351   0.246359 -0.653901           -0.125511     0.711592        0.836205   
6568    0.694117 -0.658602            1.854116    -0.384511       -0.536062   
13285   0.927946 -0.719714            0.270415    -0.389200       -0.518355   

       population  households  median_income  ocean_proximity  income_cat  \
index                                                                       
5241     0.614715    1.105510       2.357904         1.889419    0.730902   
10970    0.184453    0.347308       0.404516         0.941264    0.551471   
20351    0.552891    0.899397      -0.446556        -0.006891   -0.224920   
6568    -0.359433   -0.459968       0.160083        -0.006891    0.089414   
13285   -0.318495   -0.509043       0.099254        -0.006891    0.270989   

       rooms_per_household  population_per_household  \
index                                                  
5241             -0.437080                 -0.884208   
10970            -0.254840                 -0.876204   
20351            -0.352712                 -0.024967   
6568              0.122418                 -0.662121   
13285             0.356963                 -0.575998   

       ocean_proximity_&lt;1H OCEAN  ocean_proximity_INLAND  \
index                                                      
5241                         1.0                     0.0   
10970                        1.0                     0.0   
20351                        1.0                     0.0   
6568                         0.0                     1.0   
13285                        0.0                     1.0   

       ocean_proximity_ISLAND  ocean_proximity_NEAR BAY  \
index                                                     
5241                      0.0                       0.0   
10970                     0.0                       0.0   
20351                     0.0                       0.0   
6568                      0.0                       0.0   
13285                     0.0                       0.0   

       ocean_proximity_NEAR OCEAN  
index                              
5241                          0.0  
10970                         0.0  
20351                         0.0  
6568                          0.0  
13285                         0.0  
       median_house_value
index                    
5241             500001.0
10970            240300.0
20351            218200.0
6568             182100.0
13285            121300.0
</pre>
</div>
</div>

</div>
</div>

</div>
 

