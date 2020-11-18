<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Einf&#252;hrung-zu-Pandas">Einf&#252;hrung zu Pandas<a class="anchor-link" href="#Einf&#252;hrung-zu-Pandas">&#182;</a></h1><p>Pandas baut auf Numpy auf</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Installation:
!pip install pandas</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bibliotheken </span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># !!! datensätze einlesen werden unten erklärt, die Datensätze brauch </span>
<span class="c1"># ich inline, da ich bestimmte Pandas Actions daran erkläre</span>

<span class="c1"># Diesen Datensatz brauch ich bei der Erklärung von replace Values</span>
<span class="c1"># cars</span>
<span class="n">labelList</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;symboling&#39;</span><span class="p">,</span><span class="s1">&#39;normalizedLosses&#39;</span><span class="p">,</span><span class="s1">&#39;make&#39;</span><span class="p">,</span><span class="s1">&#39;fuelType&#39;</span><span class="p">,</span><span class="s1">&#39;aspiration&#39;</span><span class="p">,</span><span class="s1">&#39;numOfDoors&#39;</span><span class="p">,</span><span class="s1">&#39;body123Style&#39;</span><span class="p">,</span><span class="s1">&#39;driveWheels&#39;</span><span class="p">,</span><span class="s1">&#39;engineLocation&#39;</span><span class="p">,</span>
           <span class="s1">&#39;wheelBase&#39;</span><span class="p">,</span><span class="s1">&#39;length&#39;</span><span class="p">,</span><span class="s1">&#39;width&#39;</span><span class="p">,</span><span class="s1">&#39;height&#39;</span><span class="p">,</span><span class="s1">&#39;curbWeight&#39;</span><span class="p">,</span><span class="s1">&#39;engineType&#39;</span><span class="p">,</span><span class="s1">&#39;numOfCylinders&#39;</span><span class="p">,</span><span class="s1">&#39;engineSize&#39;</span><span class="p">,</span><span class="s1">&#39;fuelSystem&#39;</span><span class="p">,</span><span class="s1">&#39;bore&#39;</span><span class="p">,</span>
           <span class="s1">&#39;stroke&#39;</span><span class="p">,</span><span class="s1">&#39;compressionRatio&#39;</span><span class="p">,</span><span class="s1">&#39;horsepower&#39;</span><span class="p">,</span><span class="s1">&#39;peakRpm&#39;</span><span class="p">,</span><span class="s1">&#39;cityMpg&#39;</span><span class="p">,</span><span class="s1">&#39;highwayMpg&#39;</span><span class="p">,</span><span class="s1">&#39;price&#39;</span><span class="p">]</span>
<span class="n">carDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/data_car.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="n">labelList</span><span class="p">)</span>

<span class="c1"># Advertisment</span>
<span class="n">advertismentData</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/islrData_advertising.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">advertismentData</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Unnamed: 0&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="c1">#advertismentData.head123()</span>


<span class="c1">#IrisDataSet</span>
<span class="n">irisData</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/iris.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">irisData</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;SepalLengthCm&#39;</span><span class="p">,</span><span class="s1">&#39;SepalWidthCm&#39;</span><span class="p">,</span><span class="s1">&#39;PetalLengthCm&#39;</span><span class="p">,</span><span class="s1">&#39;PetalWidthCm&#39;</span><span class="p">,</span><span class="s1">&#39;Species&#39;</span><span class="p">]</span>
<span class="c1">#irisData.head123()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Sequentielles einlesen</strong><br>
Es kann auch vorkommen, dass die Datasets in mehreren einzelnen CSV-Dateien vorliegen und diese nun sequentiell zu einem "Großen" Df eingelsen werden sollen =&gt; setzt logischerweise vorraus, dass alle CSV-Dateien zumindest von den Feature/ Spalten her identisch aufgebaut sind. Das Beispiel dient nur dem Einlesen.
<a href="../Zeitreihen/Sample/Movement/dataset">Link zu pfad</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># teil des File-namens, alles weitere kommt über die ID und wir iterieren mit einem For Count</span>
<span class="n">path</span> <span class="o">=</span> <span class="s1">&#39;../Zeitreihen/Sample/Movement/dataset/MovementAAL_RSS_&#39;</span>
<span class="n">sequences</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span> <span class="c1"># = []</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sequences</span><span class="p">)</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">315</span><span class="p">):</span><span class="c1"># Sequentielles Einlesen von Dataframes</span>
    <span class="n">file_path</span> <span class="o">=</span> <span class="n">path</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;.csv&#39;</span>
    <span class="c1">#print(file_path)</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">head123er123</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">values</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">values</span>
    <span class="n">sequences</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">values</span><span class="p">)</span>
    
<span class="n">targets</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;../Zeitreihen/Sample/Movement/dataset/MovementAAL_target.csv&#39;</span><span class="p">)</span>
<span class="n">targets</span> <span class="o">=</span> <span class="n">targets</span><span class="o">.</span><span class="n">values</span><span class="p">[:,</span><span class="mi">1</span><span class="p">]</span>
<span class="n">targets</span><span class="o">.</span><span class="n">shape</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sequences</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">sequences</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sequences</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span> <span class="c1"># =&gt; mehrdimensionale Liste</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[]
314
&lt;class &#39;list&#39;&gt;
[-0.90476 -0.48     0.28571  0.3    ]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Serien">Serien<a class="anchor-link" href="#Serien">&#182;</a></h2><p>~ ähnlich einer Numpy Array = Nmpy Array kann keien Achsenbeschriftung haben =&gt; Mit Pandas kann man mit Labels arbeiten</p>
<p>Der erste Hauptdatentyp den wir uns für Pandas anschauen ist der der Series. Lass uns Pandas importieren und einige Series Objekte untersuchen.</p>
<p>Eine Series (dt. Serie) ist sehr ähnlich zu einem NumPy Array. Tatsächlich ist es auf dem NumPy Array Objekt aufgebaut. Was das NumPy Array letztlich von einer Series unterscheidet ist, dass Series Achsenbeschriftungen haben kann. Das bedeutet wir können nicht nur über numerische Indizes, sondern auch über das Label indexieren. Außerdem muss eine Series nicht unbedingt numerische Werte beinhalten.</p>
<p>Schauen wir uns das Konzept an einigen Beispielen an:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Erstellen-einer-Pandas-Serie">Erstellen einer Pandas Serie<a class="anchor-link" href="#Erstellen-einer-Pandas-Serie">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Basis liste für Pandas</span>
<span class="n">labels</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">,</span><span class="s2">&quot;b&quot;</span><span class="p">,</span><span class="s2">&quot;c&quot;</span><span class="p">]</span>
<span class="n">meine_liste</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">30</span><span class="p">]</span>
<span class="c1"># numpy Array</span>
<span class="n">arr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">10</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">30</span><span class="p">])</span> <span class="c1">#&lt;= hieraus erstellen wir ein Pandas DF</span>
<span class="n">d</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;a&quot;</span><span class="p">:</span><span class="mi">10</span><span class="p">,</span><span class="s2">&quot;b&quot;</span><span class="p">:</span><span class="mi">20</span><span class="p">,</span><span class="s2">&quot;c&quot;</span><span class="p">:</span><span class="mi">30</span><span class="p">}</span> <span class="c1">#&lt;= hieraus erstellen wir ein Pandas DF</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Aus-einer-pythonListe">Aus einer pythonListe<a class="anchor-link" href="#Aus-einer-pythonListe">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">meine_liste</span><span class="p">)</span>
<span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">meine_liste</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="n">labels</span><span class="p">)</span> <span class="c1">#&lt;= erstellt labels</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[19]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>a    10
b    20
c    30
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Aus-einer-numpy-Array">Aus einer numpy-Array<a class="anchor-link" href="#Aus-einer-numpy-Array">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">arr</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>a    10
b    20
c    30
dtype: int32</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Aus-einem-Dictionary">Aus einem Dictionary<a class="anchor-link" href="#Aus-einem-Dictionary">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>a    10
b    20
c    30
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Inhalte-von-einem-Pandas-series">Inhalte von einem Pandas series<a class="anchor-link" href="#Inhalte-von-einem-Pandas-series">&#182;</a></h3><p>kann numerisch und strings oder auch eine Funktion sein</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Inhalt-String">Inhalt String<a class="anchor-link" href="#Inhalt-String">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0    a
1    b
2    c
dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Inhalt-Funktionen">Inhalt Funktionen<a class="anchor-link" href="#Inhalt-Funktionen">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">([</span><span class="nb">sum</span><span class="p">,</span><span class="nb">print</span><span class="p">,</span><span class="nb">len</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0      &lt;built-in function sum&gt;
1    &lt;built-in function print&gt;
2      &lt;built-in function len&gt;
dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Indexe-Nutzen-innerhalb-von-Pandas-Series">Indexe Nutzen innerhalb von Pandas-Series<a class="anchor-link" href="#Indexe-Nutzen-innerhalb-von-Pandas-Series">&#182;</a></h3><p>Der Schlüssel zur Nutzung von Series ist das Verständnis für deren Index. Pandas nutzt diese Indexnamen oder -nummern, um schnelle Suchen durchzuführen. Dies funktioniert ähnlich einer Hash-Tabelle oder einem Dictionary.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Create-Series-mit-Index">Create Series mit Index<a class="anchor-link" href="#Create-Series-mit-Index">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Serie1</span>
<span class="n">ser1</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">],</span><span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;USA&quot;</span><span class="p">,</span><span class="s2">&quot;Deutschland&quot;</span><span class="p">,</span><span class="s2">&quot;Russland&quot;</span><span class="p">,</span><span class="s2">&quot;Japan&quot;</span><span class="p">])</span>
<span class="n">ser1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[24]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>USA            1
Deutschland    2
Russland       3
Japan          4
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Serie2, hier sind schon bekannte indexe drin, 1,2,&amp;4 // dafür ist russland raus, aber Italien rein</span>
<span class="n">ser2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">4</span><span class="p">],</span><span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;USA&quot;</span><span class="p">,</span><span class="s2">&quot;Deutschland&quot;</span><span class="p">,</span><span class="s2">&quot;Italien&quot;</span><span class="p">,</span><span class="s2">&quot;Japan&quot;</span><span class="p">])</span>
<span class="n">ser2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>USA            1
Deutschland    2
Italien        5
Japan          4
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Abfragen-des-Series-anhand-des-Index">Abfragen des Series anhand des Index<a class="anchor-link" href="#Abfragen-des-Series-anhand-des-Index">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ser1</span><span class="p">[</span><span class="s1">&#39;Russland&#39;</span><span class="p">]</span> <span class="c1">#&lt;= returnt den wert, indiesem fall etwas numerisches</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>3</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#### Addition von Series</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ser1</span> <span class="o">+</span> <span class="n">ser2</span> <span class="c1"># D = 2+2 usw // italien i ist nur einmal drin =&gt; nan</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Deutschland    4.0
Italien        NaN
Japan          8.0
Russland       NaN
USA            2.0
dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Data-Frame">Data-Frame<a class="anchor-link" href="#Data-Frame">&#182;</a></h2><p>Data Frames sind das Steckenpferd von Pandas und wurden direkt durch die Programmiersprache R inspiriert. Wir können uns Data Frames als eine Vielzahl von Series vorstellen, die zusammengefügt wurden, um sich den selben Index zu teilen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">numpy.random</span> <span class="kn">import</span> <span class="n">randn</span>
<span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">101</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Erstellen-eines-Dataframes">Erstellen eines Dataframes<a class="anchor-link" href="#Erstellen-eines-Dataframes">&#182;</a></h3><p>einlesen von externen Infos unter dem Kapitel "Daten Input und Output" in diesem Notebook</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Aus-einer-mehrdimensionalen-Pythonliste">Aus einer mehrdimensionalen Pythonliste<a class="anchor-link" href="#Aus-einer-mehrdimensionalen-Pythonliste">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">OwnData</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;tom&#39;</span><span class="p">,</span> <span class="mi">10</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;nick&#39;</span><span class="p">,</span> <span class="mi">15</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;juli&#39;</span><span class="p">,</span> <span class="mi">14</span><span class="p">]]</span> 
<span class="n">OwnDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">OwnData</span><span class="p">)</span> <span class="c1"># DF für die Transofmationen des DF</span>
<span class="n">OwnDF</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">OwnDF</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   Name  Age
0   tom   10
1  nick   15
2  juli   14
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">newData</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;Label1&#39;</span><span class="p">,</span> <span class="s1">&#39;Label2&#39;</span><span class="p">,</span> <span class="s1">&#39;Label3&#39;</span><span class="p">],</span> 
           <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">],</span> 
           <span class="p">[</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">],</span> 
           <span class="p">[</span><span class="mi">7</span><span class="p">,</span><span class="mi">8</span><span class="p">,</span><span class="mi">9</span><span class="p">]</span>
          <span class="p">]</span>
<span class="n">OwnDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">newData</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">OwnDF</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">()</span>

<span class="c1">## First Row = Col-Names</span>
<span class="n">colNames</span> <span class="o">=</span> <span class="n">newData</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">colValues</span> <span class="o">=</span> <span class="n">newData</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>

<span class="n">OwnDF2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">colNames</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">colValues</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">OwnDF2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>        0       1       2
0  Label1  Label2  Label3
1       1       2       3
2       4       5       6
3       7       8       9



   Label1  Label2  Label3
0       1       2       3
1       4       5       6
2       7       8       9
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="aus-random">aus random<a class="anchor-link" href="#aus-random">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">randn</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">4</span><span class="p">),</span><span class="n">index</span><span class="o">=</span><span class="s1">&#39;A B C D E&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(),</span><span class="n">columns</span><span class="o">=</span><span class="s1">&#39;W X Y Z&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">())</span><span class="c1"># &lt;0 hier wird mit dem Split gearbeitet</span>
<span class="n">names</span><span class="o">=</span><span class="s1">&#39;W X Y Z&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="n">index</span><span class="o">=</span><span class="s1">&#39;A B C D E&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">names</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;W&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;W&#39;, &#39;X&#39;, &#39;Y&#39;, &#39;Z&#39;] [&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;]
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[32]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">names</span><span class="o">=</span><span class="s1">&#39;W X Y Z&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="n">index</span><span class="o">=</span><span class="s1">&#39;A B C D E&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Transponiere-Dataframe">Transponiere Dataframe<a class="anchor-link" href="#Transponiere-Dataframe">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_t</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">T</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_t</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
          A         B         C         D         E
W  2.706850  0.651118 -2.018168  0.188695  0.190794
X  0.628133 -0.319318  0.740122 -0.758872  1.978757
Y  0.907969 -0.848077  0.528813 -0.933237  2.605967
Z  0.503826  0.605965 -0.589001  0.955057  0.683509
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Spalten-Auswahl-und-Indexierung">Spalten Auswahl und Indexierung<a class="anchor-link" href="#Spalten-Auswahl-und-Indexierung">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Einzelne Spalte auswählen</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;W&quot;</span><span class="p">]</span> <span class="c1">#&lt;= die einzelne Spalte ist eine Seris</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[35]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Eine Liste von Spaltennamen übergeben</span>
<span class="n">df</span><span class="p">[[</span><span class="s2">&quot;W&quot;</span><span class="p">,</span><span class="s2">&quot;Z&quot;</span><span class="p">]]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[36]:</div>



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
      <th>W</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>0.683509</td>
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
<h4 id="Spalten-zur&#252;ckgeben-mit-iloc">Spalten zur&#252;ckgeben mit iloc<a class="anchor-link" href="#Spalten-zur&#252;ckgeben-mit-iloc">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 1te Spalte</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span> <span class="mi">0</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>

<span class="c1"># Range an Spalten zurückgeben</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span> <span class="mi">1</span><span class="p">:</span><span class="mi">4</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>

<span class="c1"># Range an Spalten zurückgeben</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">y</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span> <span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">True</span><span class="p">]]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>

<span class="c1"># Lambda Function</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span> <span class="k">lambda</span> <span class="n">df</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">]]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
          X         Y         Z
A  0.628133  0.907969  0.503826
B -0.319318 -0.848077  0.605965
C  0.740122  0.528813 -0.589001
D -0.758872 -0.933237  0.955057
E  1.978757  2.605967  0.683509
          X         Z
A  0.628133  0.503826
B -0.319318  0.605965
C  0.740122 -0.589001
D -0.758872  0.955057
E  1.978757  0.683509
          W         Y
A  2.706850  0.907969
B  0.651118 -0.848077
C -2.018168  0.528813
D  0.188695 -0.933237
E  0.190794  2.605967
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Spalte-hinzuf&#252;gen">Spalte hinzuf&#252;gen<a class="anchor-link" href="#Spalte-hinzuf&#252;gen">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Aus-einer-Rechnung-der-internen-Series/Spalten">Aus einer Rechnung der internen Series/Spalten<a class="anchor-link" href="#Aus-einer-Rechnung-der-internen-Series/Spalten">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s2">&quot;neu&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">&quot;W&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="n">df</span><span class="p">[</span><span class="s2">&quot;Y&quot;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;neu1&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;neu2&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">&quot;W&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">5</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;neu3&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;Hallo&quot;</span>
<span class="n">df</span>

<span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Smith&#39;</span><span class="p">,</span> <span class="s1">&#39;Mayer&#39;</span><span class="p">,</span> <span class="s1">&#39;Christ&#39;</span><span class="p">,</span> <span class="s2">&quot;Mueller&quot;</span><span class="p">,</span> <span class="s2">&quot;Baum&quot;</span><span class="p">]</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;neu4&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">names</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>          W         X         Y         Z       neu  neu1      neu2   neu3  \
A  2.706850  0.628133  0.907969  0.503826  3.614819     5  7.706850  Hallo   
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959     5  5.651118  Hallo   
C -2.018168  0.740122  0.528813 -0.589001 -1.489355     5  2.981832  Hallo   
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542     5  5.188695  Hallo   
E  0.190794  1.978757  2.605967  0.683509  2.796762     5  5.190794  Hallo   

      neu4  
A    Smith  
B    Mayer  
C   Christ  
D  Mueller  
E     Baum  
          W         X         Y         Z       neu  neu1      neu2   neu3  \
A  2.706850  0.628133  0.907969  0.503826  3.614819     5  7.706850  Hallo   
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959     5  5.651118  Hallo   
C -2.018168  0.740122  0.528813 -0.589001 -1.489355     5  2.981832  Hallo   
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542     5  5.188695  Hallo   
E  0.190794  1.978757  2.605967  0.683509  2.796762     5  5.190794  Hallo   

      neu4  
A    Smith  
B    Mayer  
C   Christ  
D  Mueller  
E     Baum  
          W         X         Y         Z       neu  neu1      neu2   neu3  \
A  2.706850  0.628133  0.907969  0.503826  3.614819     5  7.706850  Hallo   
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959     5  5.651118  Hallo   
C -2.018168  0.740122  0.528813 -0.589001 -1.489355     5  2.981832  Hallo   
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542     5  5.188695  Hallo   
E  0.190794  1.978757  2.605967  0.683509  2.796762     5  5.190794  Hallo   

      neu4  
A    Smith  
B    Mayer  
C   Christ  
D  Mueller  
E     Baum  
          W         X         Y         Z       neu  neu1      neu2   neu3  \
A  2.706850  0.628133  0.907969  0.503826  3.614819     5  7.706850  Hallo   
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959     5  5.651118  Hallo   
C -2.018168  0.740122  0.528813 -0.589001 -1.489355     5  2.981832  Hallo   
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542     5  5.188695  Hallo   
E  0.190794  1.978757  2.605967  0.683509  2.796762     5  5.190794  Hallo   

      neu4  
A    Smith  
B    Mayer  
C   Christ  
D  Mueller  
E     Baum  
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
<pre>A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
          X         Y         Z
A  0.628133  0.907969  0.503826
B -0.319318 -0.848077  0.605965
C  0.740122  0.528813 -0.589001
D -0.758872 -0.933237  0.955057
E  1.978757  2.605967  0.683509
          X         Z
A  0.628133  0.503826
B -0.319318  0.605965
C  0.740122 -0.589001
D -0.758872  0.955057
E  1.978757  0.683509
          W         Y
A  2.706850  0.907969
B  0.651118 -0.848077
C -2.018168  0.528813
D  0.188695 -0.933237
E  0.190794  2.605967
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Spalten-entfernen">Spalten entfernen<a class="anchor-link" href="#Spalten-entfernen">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;neu&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># &lt;= zeigt das nur, das muss noch zugewiesen werden</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;neu&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="c1"># &lt;= ist das gleiche wie df.drop(&#39;neu&#39;,axis=1,inplace=True)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>          W         X         Y         Z       neu  neu1      neu2   neu3  \
A  2.706850  0.628133  0.907969  0.503826  3.614819     5  7.706850  Hallo   
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959     5  5.651118  Hallo   
C -2.018168  0.740122  0.528813 -0.589001 -1.489355     5  2.981832  Hallo   
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542     5  5.188695  Hallo   
E  0.190794  1.978757  2.605967  0.683509  2.796762     5  5.190794  Hallo   

      neu4  
A    Smith  
B    Mayer  
C   Christ  
D  Mueller  
E     Baum  
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>



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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>neu1</th>
      <th>neu2</th>
      <th>neu3</th>
      <th>neu4</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
      <td>5</td>
      <td>7.706850</td>
      <td>Hallo</td>
      <td>Smith</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
      <td>5</td>
      <td>5.651118</td>
      <td>Hallo</td>
      <td>Mayer</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
      <td>5</td>
      <td>2.981832</td>
      <td>Hallo</td>
      <td>Christ</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
      <td>5</td>
      <td>5.188695</td>
      <td>Hallo</td>
      <td>Mueller</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
      <td>5</td>
      <td>5.190794</td>
      <td>Hallo</td>
      <td>Baum</td>
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
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;neu1&#39;</span><span class="p">,</span> <span class="s1">&#39;neu2&#39;</span><span class="p">,</span> <span class="s1">&#39;neu3&#39;</span><span class="p">,</span> <span class="s1">&#39;neu4&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="c1"># &lt;= ist das gleiche wie df.drop(&#39;neu&#39;,axis=1,inplace=True)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[24]:</div>



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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Zeilen-entfernen">Zeilen entfernen<a class="anchor-link" href="#Zeilen-entfernen">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;E&#39;</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>



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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
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
<h3 id="Zeilen-Auswahl-und-Indexierung">Zeilen Auswahl und Indexierung<a class="anchor-link" href="#Zeilen-Auswahl-und-Indexierung">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Mehtode-mit-Loc">Mehtode mit Loc<a class="anchor-link" href="#Mehtode-mit-Loc">&#182;</a></h4><p>hier wird der string für spalten / Zeilenname verwendet</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Mehtode-mit-iLoc-indexLoc">Mehtode mit iLoc indexLoc<a class="anchor-link" href="#Mehtode-mit-iLoc-indexLoc">&#182;</a></h4><p>hier wird der Index verwendet</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="c1"># &lt;= index loc</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[27]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Subsets-von-Dataframe">Subsets von Dataframe<a class="anchor-link" href="#Subsets-von-Dataframe">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Einzelner-wert-via-LOC">Einzelner wert via LOC<a class="anchor-link" href="#Einzelner-wert-via-LOC">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Zeile &amp; Spalten Sprich values</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;B&#39;</span><span class="p">,</span><span class="s1">&#39;Y&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>-0.8480769834036315</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="SubFrame-via-LOC">SubFrame via LOC<a class="anchor-link" href="#SubFrame-via-LOC">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[[</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="s1">&#39;B&#39;</span><span class="p">],[</span><span class="s1">&#39;W&#39;</span><span class="p">,</span><span class="s1">&#39;Y&#39;</span><span class="p">]]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[29]:</div>



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
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.907969</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>-0.848077</td>
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
<h4 id="Bedingte-Auswahl-//-Filter-auf-ganzes-Dataframe">Bedingte Auswahl // Filter auf ganzes Dataframe<a class="anchor-link" href="#Bedingte-Auswahl-//-Filter-auf-ganzes-Dataframe">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="c1">#&lt;= hier wird für jeden Wert eine Bedingung geprüft und entsprechend ausgegeben</span>
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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>B</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>C</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>D</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>E</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;W&#39;</span><span class="p">]</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;Y&#39;</span><span class="p">]</span> <span class="c1">#&lt;= bedingung und dann nur eine Bestimme Spalte || Spalte C fehlt da w da NAN</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[31]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>A    0.907969
B   -0.848077
D   -0.933237
E    2.605967
Name: Y, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[32]:</div>



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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>A</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.651118</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>C</th>
      <td>NaN</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.188695</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;W&#39;</span><span class="p">]</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Y&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">)]</span> 
<span class="c1"># zwei Bedingungen =&gt; hier die logischen Operatoren von Python checken...das ist nicht and oder OR sondern &amp; oder |</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[33]:</div>



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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>E</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
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
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Anderes Beispiel mit dem Advertisment dataset</span>
<span class="c1"># hier alle größer als bestimmter wert in TV</span>
<span class="n">advertismentDataLoc</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span>
    <span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">TV</span> <span class="o">&gt;</span> <span class="mi">40</span><span class="p">)]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentDataLoc</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>

<span class="c1"># hier alle größer als bestimmter wert in TV UND größer in Radio</span>
<span class="n">advertismentDataLoc2</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span>
    <span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">TV</span> <span class="o">&gt;</span> <span class="mi">40</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">radio</span> <span class="o">&gt;</span> <span class="mi">40</span><span class="p">)]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentDataLoc2</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>

<span class="c1"># Top whatever</span>
<span class="n">advertismentDataLoc3</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">loc</span><span class="p">[:</span><span class="mi">99</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentDataLoc3</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200, 4)
(169, 4)
(200, 4)
(30, 4)
(200, 4)
(100, 4)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Top werte top10 top 100 top whatever</span>
<span class="n">advertismentDataLoc3</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">loc</span><span class="p">[:</span><span class="mi">99</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentData</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">advertismentDataLoc3</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200, 4)
(100, 4)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Filter-for-categorical-Value-/-Filter-for-String-Value-//-zeilenweise-filtern">Filter for categorical Value / Filter for String Value // zeilenweise filtern<a class="anchor-link" href="#Filter-for-categorical-Value-/-Filter-for-String-Value-//-zeilenweise-filtern">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">filteredforCarBrand</span>  <span class="o">=</span> <span class="n">carDF</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">carDF</span><span class="p">[</span><span class="s1">&#39;make&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;alfa-romero&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">carDF</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">filteredforCarBrand</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(205, 26)
(3, 26)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## anderes Beispiel</span>
<span class="n">sal</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;./data/Salaries.csv&quot;</span><span class="p">)</span>
<span class="n">sal</span><span class="o">.</span><span class="n">columns</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[37]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;Id&#39;, &#39;EmployeeName&#39;, &#39;JobTitle&#39;, &#39;BasePay&#39;, &#39;OvertimePay&#39;, &#39;OtherPay&#39;,
       &#39;Benefits&#39;, &#39;TotalPay&#39;, &#39;TotalPayBenefits&#39;, &#39;Year&#39;, &#39;Notes&#39;, &#39;Agency&#39;,
       &#39;Status&#39;],
      dtype=&#39;object&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Suchen nach bestimmten Namen und anschließen ein anderer Wert</span>
<span class="c1">#Wie lautet die Berufsbezeichnung (en. JobTitle) von JOSEPH DRISCOLL?</span>
<span class="n">sal</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;EmployeeName&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;JOSEPH DRISCOLL&#39;</span><span class="p">][</span><span class="s1">&#39;JobTitle&#39;</span><span class="p">]</span>
<span class="c1"># oder</span>
<span class="n">name</span>  <span class="o">=</span> <span class="n">sal</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;EmployeeName&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;JOSEPH DRISCOLL&#39;</span><span class="p">]</span>
<span class="n">name</span><span class="o">.</span><span class="n">JobTitle</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[38]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>24    CAPTAIN, FIRE SUPPRESSION
Name: JobTitle, dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie viel verdient JOSEPH DRISCOLL (inkl. Zusatleistungen (en. Benefits))?**</span>
<span class="n">sal</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;EmployeeName&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;JOSEPH DRISCOLL&#39;</span><span class="p">][</span><span class="s1">&#39;TotalPayBenefits&#39;</span><span class="p">]</span>
<span class="c1"># = name.TotalPayBenefits</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[39]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>24    270324.91
Name: TotalPayBenefits, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Wie heißt die höchstbezahlte Person (inkl. Zusatzleistungen)?</span>
<span class="n">sal</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;TotalPayBenefits&#39;</span><span class="p">]</span><span class="o">==</span> <span class="n">sal</span><span class="p">[</span><span class="s1">&#39;TotalPayBenefits&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>



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
      <th>Id</th>
      <th>EmployeeName</th>
      <th>JobTitle</th>
      <th>BasePay</th>
      <th>OvertimePay</th>
      <th>OtherPay</th>
      <th>Benefits</th>
      <th>TotalPay</th>
      <th>TotalPayBenefits</th>
      <th>Year</th>
      <th>Notes</th>
      <th>Agency</th>
      <th>Status</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NATHANIEL FORD</td>
      <td>GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY</td>
      <td>167411.18</td>
      <td>0.0</td>
      <td>400184.25</td>
      <td>NaN</td>
      <td>567595.43</td>
      <td>567595.43</td>
      <td>2011</td>
      <td>NaN</td>
      <td>San Francisco</td>
      <td>NaN</td>
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
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie viel verdient JOSEPH DRISCOLL (inkl. Zusatleistungen (en. Benefits))?**</span>
<span class="n">sal</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;EmployeeName&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;JOSEPH DRISCOLL&#39;</span><span class="p">][</span><span class="s1">&#39;TotalPayBenefits&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[41]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>24    270324.91
Name: TotalPayBenefits, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie lautet der Name der am niedrigsten bezahlten Person? Fällt dir etwas merkwürdiges an ihrem Lohn auf?** </span>
<span class="c1"># Ansatz mit sortiertem DF</span>
<span class="n">salDfSorted</span> <span class="o">=</span> <span class="n">sal</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">&#39;TotalPayBenefits&#39;</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="p">[</span><span class="kc">True</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">salDfSorted</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">,]</span><span class="o">.</span><span class="n">EmployeeName</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">salDfSorted</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">,]</span><span class="o">.</span><span class="n">TotalPayBenefits</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Joe Lopez
-618.13
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Vorsortiere-des-Dataframe-und-zugeh&#246;rige-Aggregationen">Vorsortiere des Dataframe und zugeh&#246;rige Aggregationen<a class="anchor-link" href="#Vorsortiere-des-Dataframe-und-zugeh&#246;rige-Aggregationen">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie ist der durchschnittliche (en. mean) Grundlohn (en. base pay) von allen Angestellten pro Jahr (2011-2014)?**</span>
<span class="n">sal</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;Year&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">()[</span><span class="s2">&quot;BasePay&quot;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[43]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Year
2011    63595.956517
2012    65436.406857
2013    69630.030216
2014    66564.421924
Name: BasePay, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Absolut Werte pro Jahr</span>
<span class="n">sal</span><span class="p">[</span><span class="s1">&#39;Year&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[44]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>2014    38123
2013    37606
2012    36766
2011    36159
Name: Year, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Was sind die 5 häufigsten Jobs?**</span>
<span class="n">sal</span><span class="p">[</span><span class="s1">&#39;JobTitle&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[45]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Name: JobTitle, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie viele Berufsbezeichnungen (en. job titles) wurden 2013 von nur einer Person getragen?**</span>
<span class="nb">sum</span><span class="p">(</span><span class="n">sal</span><span class="p">[</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;Year&#39;</span><span class="p">]</span><span class="o">==</span><span class="mi">2013</span><span class="p">][</span><span class="s1">&#39;JobTitle&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[46]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>202</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie viele Angestellte tragen ein &quot;Chief&quot; in ihrer Berufsbezeichnung?**</span>
<span class="k">def</span> <span class="nf">chief_string</span><span class="p">(</span><span class="n">title</span><span class="p">):</span>
    <span class="k">if</span> <span class="s1">&#39;chief&#39;</span> <span class="ow">in</span> <span class="n">title</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">():</span>
        <span class="k">return</span> <span class="kc">True</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
<span class="nb">sum</span><span class="p">(</span><span class="n">sal</span><span class="p">[</span><span class="s1">&#39;JobTitle&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">chief_string</span><span class="p">(</span><span class="n">x</span><span class="p">)))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[47]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>477</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Weiteres Bsp mit doppelter Sortierung &amp; Downfilter</span>
<span class="n">ecom</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/Ecommerce Purchases&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># **Wie viele Leute haben als Kreditkartenanbieter (en. credit card provider) *American Express* </span>
<span class="c1"># UND haben einen Einkauf über $95 getätigt?**</span>
<span class="n">ecom</span><span class="p">[(</span><span class="n">ecom</span><span class="p">[</span><span class="s1">&#39;CC Provider&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;American Express&#39;</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">ecom</span><span class="p">[</span><span class="s1">&#39;Purchase Price&#39;</span><span class="p">]</span><span class="o">&gt;</span><span class="mi">95</span><span class="p">)]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[49]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Address             39
Lot                 39
AM or PM            39
Browser Info        39
Company             39
Credit Card         39
CC Exp Date         39
CC Security Code    39
CC Provider         39
Email               39
Job                 39
IP Address          39
Language            39
Purchase Price      39
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># einbau einer Lambda-Funktion in den Filter</span>
<span class="c1"># **Die Kreditkarte wie vieler Kunden läuft im Jahr 2025 ab?**</span>
<span class="nb">sum</span><span class="p">(</span><span class="n">ecom</span><span class="p">[</span><span class="s1">&#39;CC Exp Date&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">3</span><span class="p">:])</span> <span class="o">==</span> <span class="s1">&#39;25&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[50]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1033</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># anderes Bsp-Lambda-Fkt:</span>
<span class="c1"># **Was sind die populärsten Email-Anbieter (z.B. gmail.com)?**</span>
<span class="n">ecom</span><span class="p">[</span><span class="s1">&#39;Email&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;@&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[51]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>hotmail.com     1638
yahoo.com       1616
gmail.com       1605
smith.com         42
williams.com      37
Name: Email, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Reshaping">Reshaping<a class="anchor-link" href="#Reshaping">&#182;</a></h4><p>hier wollen ein unter Subset-Bilden. Ziel ist es aus einem Datensatz mit n feature einen neuen datensatz mit n-"WelcheAnzahlAuchImmer" zu bilden. Anders ausgedrückt, wir wollen nur bestimmte SPALTEN herauspicken.</p>
<p>Wollen wir nur bestimmte ZEILEN auswählen, so muss man einen Filter/Subset wählen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Sample-Sub-Sample">Sample Sub-Sample<a class="anchor-link" href="#Sample-Sub-Sample">&#182;</a></h4><p>Wenn ein DF gegeben ist und wir nun ein Subframe von den Daten haben wollen. Bsp weil wir auf dem Subsample die Daten trainieren wollen....
Klassisch bei Regressionsfragestellungen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span><span class="mf">10.0</span><span class="p">,</span><span class="mi">1000000</span><span class="p">)</span>
<span class="n">y_true</span> <span class="o">=</span>  <span class="p">(</span><span class="mf">0.5</span> <span class="o">*</span> <span class="n">x_data</span> <span class="p">)</span> <span class="o">+</span> <span class="mi">5</span>
<span class="n">my_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">x_data</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;X Data&#39;</span><span class="p">]),</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">y_true</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;Y&#39;</span><span class="p">])],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_data</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">my_data</span> <span class="o">=</span> <span class="n">my_data</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">n</span><span class="o">=</span><span class="mi">250</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_data</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(1000000, 2)
(250, 2)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h5 id="Version1-dropping-obsolet-data">Version1 dropping obsolet data<a class="anchor-link" href="#Version1-dropping-obsolet-data">&#182;</a></h5>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfTv</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;TV&#39;</span><span class="p">,</span><span class="s1">&#39;radio&#39;</span><span class="p">,</span><span class="s1">&#39;newspaper&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfTv</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> <span class="c1"># =&gt; es ist wichtig dass hier (200,1) und nicht (200, ) steht</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200, 1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h5 id="Version-2--Transform-into-NP-&amp;-reshaping-the-format">Version 2  Transform into NP &amp; reshaping the format<a class="anchor-link" href="#Version-2--Transform-into-NP-&amp;-reshaping-the-format">&#182;</a></h5>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h6 id="Long-Version">Long Version<a class="anchor-link" href="#Long-Version">&#182;</a></h6>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfTv</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="p">[</span><span class="s1">&#39;TV&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfTv</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> <span class="c1"># =&gt; hier eben das Problem das oben bereit erwähnt wurde =&gt; (200, ) </span>
<span class="n">dfTv</span> <span class="o">=</span> <span class="n">dfTv</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfTv</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> <span class="c1"># =&gt; hier eben das Problem das oben bereit erwähnt wurde =&gt; (200, ) </span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200,)
(200, 1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h6 id="Short-Version">Short Version<a class="anchor-link" href="#Short-Version">&#182;</a></h6><h6 id="#-Single-Select"># Single-Select<a class="anchor-link" href="##-Single-Select">&#182;</a></h6>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfTv</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="p">[</span><span class="s1">&#39;TV&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfTv</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200, 1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h6 id="#-Multi-Select"># Multi-Select<a class="anchor-link" href="##-Multi-Select">&#182;</a></h6>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[56]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfTvRadio</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="p">[[</span><span class="s1">&#39;TV&#39;</span><span class="p">,</span> <span class="s1">&#39;radio&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="n">dfTvRadio2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dfTvRadio</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TV&#39;</span><span class="p">,</span> <span class="s1">&#39;Radio&#39;</span><span class="p">])</span> 
<span class="nb">print</span><span class="p">(</span><span class="n">dfTvRadio</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfTvRadio2</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(200, 2)
(200, 2)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">carDF</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
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
      <th>symboling</th>
      <th>normalizedLosses</th>
      <th>make</th>
      <th>fuelType</th>
      <th>aspiration</th>
      <th>numOfDoors</th>
      <th>body123Style</th>
      <th>driveWheels</th>
      <th>engineLocation</th>
      <th>wheelBase</th>
      <th>...</th>
      <th>engineSize</th>
      <th>fuelSystem</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compressionRatio</th>
      <th>horsepower</th>
      <th>peakRpm</th>
      <th>cityMpg</th>
      <th>highwayMpg</th>
      <th>price</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
  </tbody123>
</table>
<p>2 rows × 26 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Indexierung-extended-/-Mehr-Index">Indexierung extended / Mehr Index<a class="anchor-link" href="#Indexierung-extended-/-Mehr-Index">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Index-zur&#252;cksetzten-in-den-Numerischen-Wert">Index zur&#252;cksetzten in den Numerischen Wert<a class="anchor-link" href="#Index-zur&#252;cksetzten-in-den-Numerischen-Wert">&#182;</a></h4><p>hier werden die Alten indexe in eine Spalte übernommen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[58]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span> <span class="c1"># fehlt die Zuweisung</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[58]:</div>



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
      <th>index</th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
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
<h4 id="zuweisen-neuen-Index">zuweisen neuen Index<a class="anchor-link" href="#zuweisen-neuen-Index">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[59]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">neuind</span> <span class="o">=</span> <span class="s1">&#39;BY BW HH BB NW&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;Staaten&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">neuind</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="n">df</span><span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;Staaten&#39;</span><span class="p">)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>          W         X         Y         Z Staaten
A  2.706850  0.628133  0.907969  0.503826      BY
B  0.651118 -0.319318 -0.848077  0.605965      BW
C -2.018168  0.740122  0.528813 -0.589001      HH
D  0.188695 -0.758872 -0.933237  0.955057      BB
E  0.190794  1.978757  2.605967  0.683509      NW
</pre>
</div>
</div>

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
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
    <tr>
      <th>Staaten</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>BY</th>
      <td>2.706850</td>
      <td>0.628133</td>
      <td>0.907969</td>
      <td>0.503826</td>
    </tr>
    <tr>
      <th>BW</th>
      <td>0.651118</td>
      <td>-0.319318</td>
      <td>-0.848077</td>
      <td>0.605965</td>
    </tr>
    <tr>
      <th>HH</th>
      <td>-2.018168</td>
      <td>0.740122</td>
      <td>0.528813</td>
      <td>-0.589001</td>
    </tr>
    <tr>
      <th>BB</th>
      <td>0.188695</td>
      <td>-0.758872</td>
      <td>-0.933237</td>
      <td>0.955057</td>
    </tr>
    <tr>
      <th>NW</th>
      <td>0.190794</td>
      <td>1.978757</td>
      <td>2.605967</td>
      <td>0.683509</td>
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
<h3 id="Multi-Index-und-Index-Hierarchie">Multi-Index und Index Hierarchie<a class="anchor-link" href="#Multi-Index-und-Index-Hierarchie">&#182;</a></h3><p>hier wird ein Aussen und ein Innen Index verwendet</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Erstelle-Multi-Index">Erstelle Multi-Index<a class="anchor-link" href="#Erstelle-Multi-Index">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">aussen</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;G1&#39;</span><span class="p">,</span> <span class="s1">&#39;G1&#39;</span><span class="p">,</span> <span class="s1">&#39;G1&#39;</span><span class="p">,</span> <span class="s1">&#39;G2&#39;</span><span class="p">,</span> <span class="s1">&#39;G2&#39;</span><span class="p">,</span> <span class="s1">&#39;G2&#39;</span><span class="p">]</span>
<span class="n">innen</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span>
<span class="n">hier_index</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">aussen</span><span class="p">,</span><span class="n">innen</span><span class="p">))</span> <span class="c1"># hier = heirarchich</span>
<span class="n">hier_index</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">MultiIndex</span><span class="o">.</span><span class="n">from_tuples</span><span class="p">(</span><span class="n">hier_index</span><span class="p">)</span>
<span class="n">hier_index</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[60]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>MultiIndex([(&#39;G1&#39;, 1),
            (&#39;G1&#39;, 2),
            (&#39;G1&#39;, 3),
            (&#39;G2&#39;, 1),
            (&#39;G2&#39;, 2),
            (&#39;G2&#39;, 3)],
           )</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[61]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span><span class="n">index</span><span class="o">=</span><span class="n">hier_index</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="s1">&#39;B&#39;</span><span class="p">])</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[61]:</div>



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
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th rowspan="3" valign="top">G1</th>
      <th>1</th>
      <td>0.663267</td>
      <td>-0.892191</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.291270</td>
      <td>-0.043024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.318528</td>
      <td>0.056316</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">G2</th>
      <th>1</th>
      <td>-0.516192</td>
      <td>0.859812</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.145238</td>
      <td>-0.019217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.868013</td>
      <td>0.494686</td>
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
<div class="prompt input_prompt">In&nbsp;[62]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Diesen Multiindex kann man jetzt nach bestimmtne Kriterien Downfiltern</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;G1&#39;</span><span class="p">]</span> <span class="c1">#&lt;= nur nach g1 gefiltert</span>
<span class="c1">#df.loc[2] #&lt;= nur nach g1 gefiltert</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s1">&#39;G1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="c1">#&lt;= nur nach g1 gefiltert &amp; g2 gefiltert</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[62]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>A    0.291270
B   -0.043024
Name: 2, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Weise-Namen-an-Multiindex-zu">Weise Namen an Multiindex zu<a class="anchor-link" href="#Weise-Namen-an-Multiindex-zu">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[63]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">names</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[63]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>FrozenList([None, None])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[64]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Gruppe&#39;</span><span class="p">,</span><span class="s1">&#39;Num&#39;</span><span class="p">]</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[64]:</div>



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
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Gruppe</th>
      <th>Num</th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th rowspan="3" valign="top">G1</th>
      <th>1</th>
      <td>0.663267</td>
      <td>-0.892191</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.291270</td>
      <td>-0.043024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.318528</td>
      <td>0.056316</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">G2</th>
      <th>1</th>
      <td>-0.516192</td>
      <td>0.859812</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.145238</td>
      <td>-0.019217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.868013</td>
      <td>0.494686</td>
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
<h4 id="Abfragen-von-Multiindex">Abfragen von Multiindex<a class="anchor-link" href="#Abfragen-von-Multiindex">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[65]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Filtern nach dem ersten Index</span>
<span class="n">df</span><span class="o">.</span><span class="n">xs</span><span class="p">(</span><span class="s1">&#39;G1&#39;</span><span class="p">)</span> <span class="c1"># &lt;= ähnlich wie </span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[65]:</div>



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
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Num</th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>1</th>
      <td>0.663267</td>
      <td>-0.892191</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.291270</td>
      <td>-0.043024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.318528</td>
      <td>0.056316</td>
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
<div class="prompt input_prompt">In&nbsp;[66]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Filtern nach dem zweiten Index</span>
<span class="n">df</span><span class="o">.</span><span class="n">xs</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">level</span><span class="o">=</span><span class="s1">&#39;Num&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[66]:</div>



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
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>Gruppe</th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>G1</th>
      <td>0.663267</td>
      <td>-0.892191</td>
    </tr>
    <tr>
      <th>G2</th>
      <td>-0.516192</td>
      <td>0.859812</td>
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
<div class="prompt input_prompt">In&nbsp;[67]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">xs</span><span class="p">([</span><span class="s1">&#39;G1&#39;</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[67]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>A    0.663267
B   -0.892191
Name: (G1, 1), dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Fehlende-Daten/Missing-Data">Fehlende Daten/Missing Data<a class="anchor-link" href="#Fehlende-Daten/Missing-Data">&#182;</a></h2><p>Dieses Problem der fehlenden Daten tritt relativ häufig auf:</p>
<p>unvollständige Datensätze aufgrund technischer Pannen oder eines Datenverlustes
wenn einige befragte Personen aufgrund mangelnden Wissens oder unzureichender Antwortmotivation auf bestimmte Fragen bewusst keine Antwort geben
Nun werden wir einige der üblichen Wege (z.B. Eliminierungsverfahren und Imputation) kennenlernen, um mit Missing Data (dt. fehlenden Daten) umzugehen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[68]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BasicData</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;A&#39;</span><span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">],</span>
                  <span class="s1">&#39;B&#39;</span><span class="p">:[</span><span class="mi">5</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">],</span>
                  <span class="s1">&#39;C&#39;</span><span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]})</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[68]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
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
<h3 id="Eliminierung">Eliminierung<a class="anchor-link" href="#Eliminierung">&#182;</a></h3><p>Hat einen Großen Informationsverlust.</p>
<p>Das Eliminierungsverfahren (auch: Complete-case analysis) zählt zu den gängigen Missing-Data-Techniken. Dabei werden sämtliche Datensätze, bei denen eines oder mehrere Erhebungsmerkmale fehlende Werte aufweisen, aus der Datenmatrix gestrichen. Dieses Verfahren ist zwar sehr einfach, hat aber erhebliche Nachteile:</p>
<ol>
<li>Insbesondere hat es einen erheblichen Informationsverlust zur Folge.</li>
<li>Ferner kann diese Technik zu einer Verfälschung der verbleibenden Stichprobe führen. Als häufiges Beispiel gelten Umfragen bezüglich des Einkommens, bei denen es durchaus vorkommen kann, dass gerade Personen mit einem relativ hohen Einkommen dieses ungerne angeben und es daher in solchen Fällen tendenziell zu Missing Data kommt. </li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[69]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">()</span><span class="c1"># &lt;= nur noch die Zeilen die kein Nullwerte haben</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[69]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
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
<div class="prompt input_prompt">In&nbsp;[70]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1">#&lt;= nur noch die Spaltend die keine Nullwerte haben</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[70]:</div>



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
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
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
<div class="prompt input_prompt">In&nbsp;[71]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">thresh</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> <span class="c1">#&lt;= threshold ab einer gewissen Anzahl von leeren werten</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[71]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>2</td>
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
<h3 id="Imputation">Imputation<a class="anchor-link" href="#Imputation">&#182;</a></h3><p>Kann Verfälschungen haben</p>
<p>Um dieses Problem der Eliminierungsverfahren möglichst in den Griff zu bekommen, wurden Imputationsverfahren entwickelt, bei denen versucht wird, fehlende Daten nicht einfach zu ignorieren, sondern stattdessen durch plausible Werte zu ersetzen, die unter anderem mit Hilfe der beobachteten Werte des gleichen Datensatzes geschätzt werden können.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[72]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># finde die Nullvalues</span>
<span class="n">df</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[72]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
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
<h4 id="Konstante">Konstante<a class="anchor-link" href="#Konstante">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[73]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="s1">&#39;Füllwert&#39;</span><span class="p">)</span> <span class="c1">#&lt;= Konstatnte</span>
<span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[73]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
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
<h4 id="Mean">Mean<a class="anchor-link" href="#Mean">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[74]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[74]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0    1.0
1    2.0
2    1.5
Name: A, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Gruppieren-/-GroupBy">Gruppieren / GroupBy<a class="anchor-link" href="#Gruppieren-/-GroupBy">&#182;</a></h2><p>Die <code>groupby</code> Methode (dt. gruppieren nach) erlaubt es uns Zeilen zu gruppieren und Aggregationsfunktionen aufzurufen.
<img src="./imgs/Groupby.PNG" alt="bild"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data Frame erstellen</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;Firma&#39;</span><span class="p">:[</span><span class="s1">&#39;GOOG&#39;</span><span class="p">,</span><span class="s1">&#39;GOOG&#39;</span><span class="p">,</span><span class="s1">&#39;MSFT&#39;</span><span class="p">,</span><span class="s1">&#39;MSFT&#39;</span><span class="p">,</span><span class="s1">&#39;FB&#39;</span><span class="p">,</span><span class="s1">&#39;FB&#39;</span><span class="p">],</span>
       <span class="s1">&#39;Person&#39;</span><span class="p">:[</span><span class="s1">&#39;Sam&#39;</span><span class="p">,</span><span class="s1">&#39;Charlie&#39;</span><span class="p">,</span><span class="s1">&#39;Amy&#39;</span><span class="p">,</span><span class="s1">&#39;Vanessa&#39;</span><span class="p">,</span><span class="s1">&#39;Carl&#39;</span><span class="p">,</span><span class="s1">&#39;Sarah&#39;</span><span class="p">],</span>
       <span class="s1">&#39;Sales&#39;</span><span class="p">:[</span><span class="mi">200</span><span class="p">,</span><span class="mi">120</span><span class="p">,</span><span class="mi">340</span><span class="p">,</span><span class="mi">124</span><span class="p">,</span><span class="mi">243</span><span class="p">,</span><span class="mi">350</span><span class="p">]}</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[75]:</div>



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
      <th>Firma</th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>Sam</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GOOG</td>
      <td>Charlie</td>
      <td>120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>Amy</td>
      <td>340</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSFT</td>
      <td>Vanessa</td>
      <td>124</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FB</td>
      <td>Carl</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FB</td>
      <td>Sarah</td>
      <td>350</td>
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
<h3 id="Simple-Gruppieren">Simple Gruppieren<a class="anchor-link" href="#Simple-Gruppieren">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[76]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Groupby Firma</span>
<span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;Firma&#39;</span><span class="p">)</span> <span class="c1">#&lt;0 kann noch nicht wirklich genutzt werden, aber hier kann die aggreaftion ausgewählt werdne</span>
<span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;Firma&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[76]:</div>



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
      <th>Sales</th>
    </tr>
    <tr>
      <th>Firma</th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>FB</th>
      <td>296.5</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>160.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>232.0</td>
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
<div class="prompt input_prompt">In&nbsp;[77]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Mit variablen</span>
<span class="n">nach_firma</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;Firma&#39;</span><span class="p">)</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[77]:</div>



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
      <th>Sales</th>
    </tr>
    <tr>
      <th>Firma</th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>FB</th>
      <td>296.5</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>160.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>232.0</td>
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
<div class="prompt input_prompt">In&nbsp;[78]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[78]:</div>



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
      <th>Firma</th>
      <th>Person</th>
      <th>Sales</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>GOOG</td>
      <td>Sam</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GOOG</td>
      <td>Charlie</td>
      <td>120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>Amy</td>
      <td>340</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSFT</td>
      <td>Vanessa</td>
      <td>124</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FB</td>
      <td>Carl</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FB</td>
      <td>Sarah</td>
      <td>350</td>
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
<div class="prompt input_prompt">In&nbsp;[79]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## ggf counts // im Falle ein Sub-Df und dann dort bestimmte werte zählen</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Firma&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[79]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>GOOG    2
MSFT    2
FB      2
Name: Firma, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Gruppieren-mit-Mathematischen-Funktionen">Gruppieren mit Mathematischen Funktionen<a class="anchor-link" href="#Gruppieren-mit-Mathematischen-Funktionen">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[80]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Funktionen</span>
<span class="c1"># Standardabweichung</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>
<span class="c1"># min</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">min</span><span class="p">()</span>
<span class="c1"># max</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">max</span><span class="p">()</span>
<span class="c1"># absolut</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
<span class="c1"># Zusammenfassung</span>
<span class="n">nach_firma</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[80]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody123 tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody123 tr th {
        vertical-align: top;
    }

    .dataframe thead123 tr th {
        text-align: left;
    }

    .dataframe thead123 tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead123>
    <tr>
      <th></th>
      <th colspan="8" halign="left">Sales</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Firma</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>FB</th>
      <td>2.0</td>
      <td>296.5</td>
      <td>75.660426</td>
      <td>243.0</td>
      <td>269.75</td>
      <td>296.5</td>
      <td>323.25</td>
      <td>350.0</td>
    </tr>
    <tr>
      <th>GOOG</th>
      <td>2.0</td>
      <td>160.0</td>
      <td>56.568542</td>
      <td>120.0</td>
      <td>140.00</td>
      <td>160.0</td>
      <td>180.00</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>2.0</td>
      <td>232.0</td>
      <td>152.735065</td>
      <td>124.0</td>
      <td>178.00</td>
      <td>232.0</td>
      <td>286.00</td>
      <td>340.0</td>
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
<p>hier noch die Darstellung Transponiert</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Zusammenf&#252;gen-und-Verkn&#252;pfen-||-Merge,-Join-&amp;-Concatenation">Zusammenf&#252;gen und Verkn&#252;pfen || Merge, Join &amp; Concatenation<a class="anchor-link" href="#Zusammenf&#252;gen-und-Verkn&#252;pfen-||-Merge,-Join-&amp;-Concatenation">&#182;</a></h2><p>Es gibt im Wesentlichen drei Wege, um Data Frames zusammenzuführen: Merging, Joining und Concatenating (Verknüpfen). In dieser Lektion werden wir diese drei Methoden anhand von Beispielen durchgehen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Append">Append<a class="anchor-link" href="#Append">&#182;</a></h3><p>Möglichkeit 2 Dataframe aneinander zu hängen, ähnlichwie "Concat axis = 0"</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[81]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data for append</span>
<span class="c1"># erstellen der zwei dataframes</span>
<span class="n">dataA</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;tom&#39;</span><span class="p">,</span> <span class="mi">10</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;nick&#39;</span><span class="p">,</span> <span class="mi">15</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;juli&#39;</span><span class="p">,</span> <span class="mi">14</span><span class="p">]]</span> 
<span class="n">dataB</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;Jochen&#39;</span><span class="p">,</span> <span class="mi">117</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;Chris&#39;</span><span class="p">,</span> <span class="mi">71</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;Silvia&#39;</span><span class="p">,</span> <span class="mi">5</span><span class="p">]]</span> 
<span class="n">dfA</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dataA</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">])</span>
<span class="n">dfB</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dataB</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[82]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Inteaktion des Dataframes</span>
<span class="n">dfappend</span> <span class="o">=</span> <span class="n">dfA</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dfB</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfappend</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;###################&quot;</span><span class="p">)</span>
<span class="c1">#update index for new dataframe</span>
<span class="n">dfappend</span> <span class="o">=</span> <span class="n">dfappend</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
<span class="c1"># Drop old index column</span>
<span class="n">dfappend</span> <span class="o">=</span> <span class="n">dfappend</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="s2">&quot;index&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfappend</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>     Name  Age
0     tom   10
1    nick   15
2    juli   14
0  Jochen  117
1   Chris   71
2  Silvia    5
###################
     Name  Age
0     tom   10
1    nick   15
2    juli   14
3  Jochen  117
4   Chris   71
5  Silvia    5
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Concat">Concat<a class="anchor-link" href="#Concat">&#182;</a></h3><p><em>Concatenating</em> bezeichnet das aneinanderreihen von Data Frames. Dabei sollte man beachten, dass die Dimensionen entlang der Achse, entlang derer man anreiht, übereinstimmen.</p>
<p>Dann kann man <code>pd.concat</code> nutzen und eine Liste von Data Frames übergeben:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[83]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### Data für die Demonstration</span>
<span class="n">df1</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A0&#39;</span><span class="p">,</span> <span class="s1">&#39;A1&#39;</span><span class="p">,</span> <span class="s1">&#39;A2&#39;</span><span class="p">,</span> <span class="s1">&#39;A3&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B0&#39;</span><span class="p">,</span> <span class="s1">&#39;B1&#39;</span><span class="p">,</span> <span class="s1">&#39;B2&#39;</span><span class="p">,</span> <span class="s1">&#39;B3&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C0&#39;</span><span class="p">,</span> <span class="s1">&#39;C1&#39;</span><span class="p">,</span> <span class="s1">&#39;C2&#39;</span><span class="p">,</span> <span class="s1">&#39;C3&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D0&#39;</span><span class="p">,</span> <span class="s1">&#39;D1&#39;</span><span class="p">,</span> <span class="s1">&#39;D2&#39;</span><span class="p">,</span> <span class="s1">&#39;D3&#39;</span><span class="p">]},</span>
                        <span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>

<span class="n">df2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A4&#39;</span><span class="p">,</span> <span class="s1">&#39;A5&#39;</span><span class="p">,</span> <span class="s1">&#39;A6&#39;</span><span class="p">,</span> <span class="s1">&#39;A7&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B4&#39;</span><span class="p">,</span> <span class="s1">&#39;B5&#39;</span><span class="p">,</span> <span class="s1">&#39;B6&#39;</span><span class="p">,</span> <span class="s1">&#39;B7&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C4&#39;</span><span class="p">,</span> <span class="s1">&#39;C5&#39;</span><span class="p">,</span> <span class="s1">&#39;C6&#39;</span><span class="p">,</span> <span class="s1">&#39;C7&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D4&#39;</span><span class="p">,</span> <span class="s1">&#39;D5&#39;</span><span class="p">,</span> <span class="s1">&#39;D6&#39;</span><span class="p">,</span> <span class="s1">&#39;D7&#39;</span><span class="p">]},</span>
                         <span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">])</span> 

<span class="n">df3</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A8&#39;</span><span class="p">,</span> <span class="s1">&#39;A9&#39;</span><span class="p">,</span> <span class="s1">&#39;A10&#39;</span><span class="p">,</span> <span class="s1">&#39;A11&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B8&#39;</span><span class="p">,</span> <span class="s1">&#39;B9&#39;</span><span class="p">,</span> <span class="s1">&#39;B10&#39;</span><span class="p">,</span> <span class="s1">&#39;B11&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C8&#39;</span><span class="p">,</span> <span class="s1">&#39;C9&#39;</span><span class="p">,</span> <span class="s1">&#39;C10&#39;</span><span class="p">,</span> <span class="s1">&#39;C11&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D8&#39;</span><span class="p">,</span> <span class="s1">&#39;D9&#39;</span><span class="p">,</span> <span class="s1">&#39;D10&#39;</span><span class="p">,</span> <span class="s1">&#39;D11&#39;</span><span class="p">]},</span>
                        <span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">11</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;###########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;###########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df3</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
###########
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
###########
      A    B    C    D
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Zeilen-aneinander-reihen">Zeilen aneinander reihen<a class="anchor-link" href="#Zeilen-aneinander-reihen">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[84]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">df1</span><span class="p">,</span><span class="n">df2</span><span class="p">,</span><span class="n">df3</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[84]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
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
<h4 id="Spalten-zusammenf&#252;hren">Spalten zusammenf&#252;hren<a class="anchor-link" href="#Spalten-zusammenf&#252;hren">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[85]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">df1</span><span class="p">,</span><span class="n">df2</span><span class="p">,</span><span class="n">df3</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1">#&lt;= gibt so keinen Sinn, concat gibt mehr sinn bei Zeilen zusammenhängen</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[85]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
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
<h3 id="Merge">Merge<a class="anchor-link" href="#Merge">&#182;</a></h3><p>Vergleiche SQL-Abfragen in dem Kontext</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="inner-Join">inner Join<a class="anchor-link" href="#inner-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h5 id="InnerJoin-mit-einem-Key">InnerJoin mit einem Key<a class="anchor-link" href="#InnerJoin-mit-einem-Key">&#182;</a></h5>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[86]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BSP data für Merge</span>
<span class="n">links</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;key&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">,</span> <span class="s1">&#39;K3&#39;</span><span class="p">],</span>
                     <span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A0&#39;</span><span class="p">,</span> <span class="s1">&#39;A1&#39;</span><span class="p">,</span> <span class="s1">&#39;A2&#39;</span><span class="p">,</span> <span class="s1">&#39;A3&#39;</span><span class="p">],</span>
                     <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B0&#39;</span><span class="p">,</span> <span class="s1">&#39;B1&#39;</span><span class="p">,</span> <span class="s1">&#39;B2&#39;</span><span class="p">,</span> <span class="s1">&#39;B3&#39;</span><span class="p">]})</span>
   
<span class="n">rechts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;key&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">,</span> <span class="s1">&#39;K3&#39;</span><span class="p">],</span>
                          <span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C0&#39;</span><span class="p">,</span> <span class="s1">&#39;C1&#39;</span><span class="p">,</span> <span class="s1">&#39;C2&#39;</span><span class="p">,</span> <span class="s1">&#39;C3&#39;</span><span class="p">],</span>
                          <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D0&#39;</span><span class="p">,</span> <span class="s1">&#39;D1&#39;</span><span class="p">,</span> <span class="s1">&#39;D2&#39;</span><span class="p">,</span> <span class="s1">&#39;D3&#39;</span><span class="p">]})</span>    
<span class="nb">print</span><span class="p">(</span><span class="n">links</span><span class="p">)</span>  
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;###########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">rechts</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
###########
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[87]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">links</span><span class="p">,</span><span class="n">rechts</span><span class="p">,</span><span class="n">how</span><span class="o">=</span><span class="s1">&#39;inner&#39;</span><span class="p">,</span><span class="n">on</span><span class="o">=</span><span class="s1">&#39;key&#39;</span><span class="p">)</span> <span class="c1">#&lt;= hier inner /leftouter</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[87]:</div>



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
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
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
<h5 id="Inner-Join-mit-zwei-Keys">Inner Join mit zwei Keys<a class="anchor-link" href="#Inner-Join-mit-zwei-Keys">&#182;</a></h5>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[88]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">links</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;key1&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">],</span>
                     <span class="s1">&#39;key2&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A0&#39;</span><span class="p">,</span> <span class="s1">&#39;A1&#39;</span><span class="p">,</span> <span class="s1">&#39;A2&#39;</span><span class="p">,</span> <span class="s1">&#39;A3&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B0&#39;</span><span class="p">,</span> <span class="s1">&#39;B1&#39;</span><span class="p">,</span> <span class="s1">&#39;B2&#39;</span><span class="p">,</span> <span class="s1">&#39;B3&#39;</span><span class="p">]})</span>
    
<span class="n">rechts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;key1&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">],</span>
                               <span class="s1">&#39;key2&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K0&#39;</span><span class="p">],</span>
                                  <span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C0&#39;</span><span class="p">,</span> <span class="s1">&#39;C1&#39;</span><span class="p">,</span> <span class="s1">&#39;C2&#39;</span><span class="p">,</span> <span class="s1">&#39;C3&#39;</span><span class="p">],</span>
                                  <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D0&#39;</span><span class="p">,</span> <span class="s1">&#39;D1&#39;</span><span class="p">,</span> <span class="s1">&#39;D2&#39;</span><span class="p">,</span> <span class="s1">&#39;D3&#39;</span><span class="p">]})</span>

<span class="nb">print</span><span class="p">(</span><span class="n">links</span><span class="p">)</span>  
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;###########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">rechts</span><span class="p">)</span> <span class="c1">#</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
###########
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[89]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">links</span><span class="p">,</span> <span class="n">rechts</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;key1&#39;</span><span class="p">,</span> <span class="s1">&#39;key2&#39;</span><span class="p">])</span> <span class="c1"># &lt;= hier wird mit zwei key gejoint</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[89]:</div>



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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
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
<h4 id="Outer-Join">Outer Join<a class="anchor-link" href="#Outer-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[90]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># mit zwei Keys</span>
<span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">links</span><span class="p">,</span> <span class="n">rechts</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s2">&quot;outer&quot;</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;key1&#39;</span><span class="p">,</span> <span class="s1">&#39;key2&#39;</span><span class="p">])</span> <span class="c1"># &lt;= empties werden mit NAN aufgeüllte</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[90]:</div>



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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
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
<h4 id="Right-Join">Right Join<a class="anchor-link" href="#Right-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[91]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">links</span><span class="p">,</span> <span class="n">rechts</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s1">&#39;right&#39;</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;key1&#39;</span><span class="p">,</span> <span class="s1">&#39;key2&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[91]:</div>



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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
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
<h4 id="Left-Join">Left Join<a class="anchor-link" href="#Left-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[92]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">links</span><span class="p">,</span> <span class="n">rechts</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s1">&#39;left&#39;</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;key1&#39;</span><span class="p">,</span> <span class="s1">&#39;key2&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[92]:</div>



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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
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
<h3 id="Join">Join<a class="anchor-link" href="#Join">&#182;</a></h3><p><em>Joining</em> ist eine übliche Methode, um Spalten mit zwei potentiell unterschiedlichen indizierten Data Frames in einen gemeinsamen Data Frame zu packen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[93]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">links</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;A&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A0&#39;</span><span class="p">,</span> <span class="s1">&#39;A1&#39;</span><span class="p">,</span> <span class="s1">&#39;A2&#39;</span><span class="p">],</span>
                     <span class="s1">&#39;B&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;B0&#39;</span><span class="p">,</span> <span class="s1">&#39;B1&#39;</span><span class="p">,</span> <span class="s1">&#39;B2&#39;</span><span class="p">]},</span>
                      <span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K1&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">])</span> 

<span class="n">rechts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;C&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;C0&#39;</span><span class="p">,</span> <span class="s1">&#39;C2&#39;</span><span class="p">,</span> <span class="s1">&#39;C3&#39;</span><span class="p">],</span>
                    <span class="s1">&#39;D&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;D0&#39;</span><span class="p">,</span> <span class="s1">&#39;D2&#39;</span><span class="p">,</span> <span class="s1">&#39;D3&#39;</span><span class="p">]},</span>
                      <span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;K0&#39;</span><span class="p">,</span> <span class="s1">&#39;K2&#39;</span><span class="p">,</span> <span class="s1">&#39;K3&#39;</span><span class="p">])</span>


<span class="nb">print</span><span class="p">(</span><span class="n">links</span><span class="p">)</span>  
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;###########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">rechts</span><span class="p">)</span> <span class="c1">#</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
###########
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Inner-Join">Inner Join<a class="anchor-link" href="#Inner-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[94]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Wir fügen an das linke DF das Rechte an</span>
<span class="n">links</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">rechts</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[94]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
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
<h4 id="Outer-Join">Outer Join<a class="anchor-link" href="#Outer-Join">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[95]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">links</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">rechts</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s1">&#39;outer&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[95]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
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
<h2 id="Operationen">Operationen<a class="anchor-link" href="#Operationen">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[96]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;spa1&#39;</span><span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">],</span><span class="s1">&#39;spa2&#39;</span><span class="p">:[</span><span class="mi">444</span><span class="p">,</span><span class="mi">555</span><span class="p">,</span><span class="mi">666</span><span class="p">,</span><span class="mi">444</span><span class="p">],</span><span class="s1">&#39;spa3&#39;</span><span class="p">:[</span><span class="s1">&#39;abc&#39;</span><span class="p">,</span><span class="s1">&#39;def&#39;</span><span class="p">,</span><span class="s1">&#39;ghi&#39;</span><span class="p">,</span><span class="s1">&#39;xyz&#39;</span><span class="p">]})</span>
<span class="n">df</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[96]:</div>



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
      <th>spa1</th>
      <th>spa2</th>
      <th>spa3</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>abc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>def</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>ghi</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>xyz</td>
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
<h3 id="head123-/-tail">head123 / tail<a class="anchor-link" href="#head123-/-tail">&#182;</a></h3><p>nur die ersten x Zeilen Ausgeben</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[97]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span><span class="s1">&#39;spa1&#39;</span><span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">],</span><span class="s1">&#39;spa2&#39;</span><span class="p">:[</span><span class="mi">444</span><span class="p">,</span><span class="mi">555</span><span class="p">,</span><span class="mi">666</span><span class="p">,</span><span class="mi">444</span><span class="p">],</span><span class="s1">&#39;spa3&#39;</span><span class="p">:[</span><span class="s1">&#39;abc&#39;</span><span class="p">,</span><span class="s1">&#39;def&#39;</span><span class="p">,</span><span class="s1">&#39;ghi&#39;</span><span class="p">,</span><span class="s1">&#39;xyz&#39;</span><span class="p">]})</span>
<span class="n">df</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
<span class="n">df</span><span class="o">.</span><span class="n">tail</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[97]:</div>



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
      <th>spa1</th>
      <th>spa2</th>
      <th>spa3</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>abc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>def</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>ghi</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>xyz</td>
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
<h3 id="info">info<a class="anchor-link" href="#info">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[98]:</div>
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
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   spa1    4 non-null      int64 
 1   spa2    4 non-null      int64 
 2   spa3    4 non-null      object
dtypes: int64(2), object(1)
memory usage: 224.0+ bytes
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="unique-value">unique value<a class="anchor-link" href="#unique-value">&#182;</a></h3><p>gebe jede Ausprägung nur einmal aus</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[99]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa2&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[99]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([444, 555, 666], dtype=int64)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[100]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># number de runiquen value</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa2&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[100]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>3</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Count">Count<a class="anchor-link" href="#Count">&#182;</a></h3><p>gibt die Anzahl der uniquen Werte zurück &lt;= nichts anders als Groupby &amp; Aggregation</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[101]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa2&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[101]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>444    2
555    1
666    1
Name: spa2, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Apply">Apply<a class="anchor-link" href="#Apply">&#182;</a></h3><p>Via apply wird dann auch die Lambda-Funktion eingebaut. Der Unterschied hier ist dass die Funktion erst definiert und dann angewendet wird. Bei einer Lambda-Funktion wird die Funktion definiert, während sie bereits aufgerufen wird.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="eigene-Funktion">eigene Funktion<a class="anchor-link" href="#eigene-Funktion">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[102]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">mal2</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span><span class="o">*</span><span class="mi">2</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">mal2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[102]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0    2
1    4
2    6
3    8
Name: spa1, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Builtin-Function">Builtin Function<a class="anchor-link" href="#Builtin-Function">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[103]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa3&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="nb">len</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[103]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0    3
1    3
2    3
3    3
Name: spa3, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Lambda-Function-Num">Lambda Function-Num<a class="anchor-link" href="#Lambda-Function-Num">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[104]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa2&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[104]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0    446
1    557
2    668
3    446
Name: spa2, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Lambda-Function-Cat-mit-Split">Lambda Function-Cat mit Split<a class="anchor-link" href="#Lambda-Function-Cat-mit-Split">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[105]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;names&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;iris Smith&#39;</span><span class="p">,</span> <span class="s1">&#39;Eva Mayer&#39;</span><span class="p">,</span> <span class="s1">&#39;Anna Christ&#39;</span><span class="p">,</span> <span class="s1">&#39;Nadine Mueller&#39;</span><span class="p">]</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;vorname&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;names&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">title</span><span class="p">:</span> <span class="n">title</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;nachname&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;names&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">title</span><span class="p">:</span> <span class="n">title</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[105]:</div>



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
      <th>spa1</th>
      <th>spa2</th>
      <th>spa3</th>
      <th>names</th>
      <th>vorname</th>
      <th>nachname</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>abc</td>
      <td>iris Smith</td>
      <td>iris</td>
      <td>Smith</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>def</td>
      <td>Eva Mayer</td>
      <td>Eva</td>
      <td>Mayer</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>ghi</td>
      <td>Anna Christ</td>
      <td>Anna</td>
      <td>Christ</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>xyz</td>
      <td>Nadine Mueller</td>
      <td>Nadine</td>
      <td>Mueller</td>
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
<div class="prompt input_prompt">In&nbsp;[106]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#df[&#39;Reason&#39;] = df[&#39;title&#39;].apply(lambda title: title.split(&#39;:&#39;)[0])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Aggreagationen">Aggreagationen<a class="anchor-link" href="#Aggreagationen">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[107]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[107]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>10</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[108]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[108]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>4</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[109]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[109]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[110]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">var</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[110]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1.6666666666666667</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[111]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;spa1&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[111]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1.2909944487358056</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="SpaltenZeilen-name-zur&#252;ckgegebn-name,-Column-name">SpaltenZeilen name zur&#252;ckgegebn name, Column name<a class="anchor-link" href="#SpaltenZeilen-name-zur&#252;ckgegebn-name,-Column-name">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[112]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">columns</span>
<span class="nb">type</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">columnList</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span>
<span class="n">columnList</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[112]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;spa1&#39;, &#39;spa2&#39;, &#39;spa3&#39;, &#39;names&#39;, &#39;vorname&#39;, &#39;nachname&#39;], dtype=&#39;object&#39;)</pre>
</div>

</div>

</div>
</div>

</div>### Replace Column Names
df
print('########Version1########')
'''
hier werden alle spalten geändert
'''
newColumnList = ['10', '20', '30']
df.columns = newColumnList
print(df)
print()
print('########Version2########')
'''
hier werden alle spalten geändert
'''
df.rename(columns={'10':'nickname', 
                   '20':'age',
                   '30':'firstname'
                   }, 
                 inplace=True)
print(df)
print()
print('########Version3########')
'''
hier wird lediglich eine Spalte geändert
'''
df.rename(columns={'nickname':'Name'}, 
                 inplace=True) 
print(df)
print()

### Back to the orginal Values
df.columns = columnList
print(df)
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[114]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">index</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[114]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>RangeIndex(start=0, stop=4, step=1)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Sortieren">Sortieren<a class="anchor-link" href="#Sortieren">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="nach-einem-Wert">nach einem Wert<a class="anchor-link" href="#nach-einem-Wert">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[115]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">&#39;spa2&#39;</span><span class="p">)</span> <span class="c1">#inplace=False per Standard</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[115]:</div>



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
      <th>spa1</th>
      <th>spa2</th>
      <th>spa3</th>
      <th>names</th>
      <th>vorname</th>
      <th>nachname</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>444</td>
      <td>abc</td>
      <td>iris Smith</td>
      <td>iris</td>
      <td>Smith</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>444</td>
      <td>xyz</td>
      <td>Nadine Mueller</td>
      <td>Nadine</td>
      <td>Mueller</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>555</td>
      <td>def</td>
      <td>Eva Mayer</td>
      <td>Eva</td>
      <td>Mayer</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>666</td>
      <td>ghi</td>
      <td>Anna Christ</td>
      <td>Anna</td>
      <td>Christ</td>
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
<h4 id="nach-meherern-Feature">nach meherern Feature<a class="anchor-link" href="#nach-meherern-Feature">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[116]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">irisData</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>
<span class="n">dfSortedSpecies</span> <span class="o">=</span> <span class="n">irisData</span><span class="o">.</span><span class="n">sort_values</span><span class="p">([</span><span class="s1">&#39;SepalWidthCm&#39;</span><span class="p">,</span> <span class="s1">&#39;Species&#39;</span> <span class="p">],</span> <span class="n">ascending</span><span class="o">=</span><span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfSortedSpecies</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>
<span class="n">dfSortedSpecies</span> <span class="o">=</span> <span class="n">irisData</span><span class="o">.</span><span class="n">sort_values</span><span class="p">([</span><span class="s1">&#39;SepalWidthCm&#39;</span><span class="p">,</span> <span class="s1">&#39;Species&#39;</span> <span class="p">],</span> <span class="n">ascending</span><span class="o">=</span><span class="p">[</span><span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dfSortedSpecies</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm Species
0            5.1           3.5            1.4           0.2  Setosa
1            4.9           3.0            1.4           0.2  Setosa
2            4.7           3.2            1.3           0.2  Setosa
3            4.6           3.1            1.5           0.2  Setosa
4            5.0           3.6            1.4           0.2  Setosa
     SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm     Species
60             5.0           2.0            3.5           1.0  Versicolor
62             6.0           2.2            4.0           1.0  Versicolor
68             6.2           2.2            4.5           1.5  Versicolor
119            6.0           2.2            5.0           1.5   Virginica
41             4.5           2.3            1.3           0.3      Setosa
     SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm     Species
60             5.0           2.0            3.5           1.0  Versicolor
119            6.0           2.2            5.0           1.5   Virginica
62             6.0           2.2            4.0           1.0  Versicolor
68             6.2           2.2            4.5           1.5  Versicolor
53             5.5           2.3            4.0           1.3  Versicolor
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Na--Werte-Finden">Na -Werte Finden<a class="anchor-link" href="#Na--Werte-Finden">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[117]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span>
<span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span>
<span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[117]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>False</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Null-Werte-finden">Null Werte finden<a class="anchor-link" href="#Null-Werte-finden">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[118]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[118]:</div>



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
      <th>spa1</th>
      <th>spa2</th>
      <th>spa3</th>
      <th>names</th>
      <th>vorname</th>
      <th>nachname</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
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
<h3 id="Werte-ersetzen-/-replace">Werte ersetzen / replace<a class="anchor-link" href="#Werte-ersetzen-/-replace">&#182;</a></h3><h4 id="Single-Column">Single Column<a class="anchor-link" href="#Single-Column">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[119]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">carDF</span><span class="p">[</span><span class="s1">&#39;bore&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">carDF</span><span class="p">[</span><span class="s1">&#39;bore&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;?&quot;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">carDF</span><span class="p">))</span>
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
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="GesamtDatensatz">GesamtDatensatz<a class="anchor-link" href="#GesamtDatensatz">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[120]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">carDF</span> <span class="o">=</span> <span class="n">carDF</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;?&quot;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">carDF</span><span class="p">))</span>
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
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Change-Datatype-von-Spalte">Change Datatype von Spalte<a class="anchor-link" href="#Change-Datatype-von-Spalte">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="mit-astype">mit astype<a class="anchor-link" href="#mit-astype">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[121]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">carDF</span><span class="p">[[</span><span class="s1">&#39;price&#39;</span><span class="p">]]</span><span class="o">=</span><span class="n">carDF</span><span class="p">[[</span><span class="s1">&#39;price&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;float64&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Pivotieren">Pivotieren<a class="anchor-link" href="#Pivotieren">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data for Pivot</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;A&#39;</span><span class="p">:[</span><span class="s1">&#39;foo&#39;</span><span class="p">,</span><span class="s1">&#39;foo&#39;</span><span class="p">,</span><span class="s1">&#39;foo&#39;</span><span class="p">,</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span><span class="s1">&#39;bar&#39;</span><span class="p">],</span>
     <span class="s1">&#39;B&#39;</span><span class="p">:[</span><span class="s1">&#39;one&#39;</span><span class="p">,</span><span class="s1">&#39;one&#39;</span><span class="p">,</span><span class="s1">&#39;two&#39;</span><span class="p">,</span><span class="s1">&#39;two&#39;</span><span class="p">,</span><span class="s1">&#39;one&#39;</span><span class="p">,</span><span class="s1">&#39;one&#39;</span><span class="p">],</span>
       <span class="s1">&#39;C&#39;</span><span class="p">:[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">],</span>
       <span class="s1">&#39;D&#39;</span><span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">1</span><span class="p">]}</span>

<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[122]:</div>



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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>x</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>one</td>
      <td>y</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>x</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>two</td>
      <td>y</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>bar</td>
      <td>one</td>
      <td>x</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>one</td>
      <td>y</td>
      <td>1</td>
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
<div class="prompt input_prompt">In&nbsp;[123]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">pivot_table</span><span class="p">(</span><span class="n">values</span><span class="o">=</span><span class="s1">&#39;D&#39;</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;B&#39;</span><span class="p">],</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;C&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[123]:</div>



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
      <th>C</th>
      <th>x</th>
      <th>y</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>two</th>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2.0</td>
      <td>NaN</td>
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
<div class="prompt input_prompt">In&nbsp;[124]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### anderes Beispiel für das Pivotieren:</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="n">fluege</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s1">&#39;flights&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fluege</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="n">fluege</span><span class="o">.</span><span class="n">pivot_table</span><span class="p">(</span><span class="n">values</span><span class="o">=</span><span class="s1">&#39;passengers&#39;</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="s1">&#39;month&#39;</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="s1">&#39;year&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   year     month  passengers
0  1949   January         112
1  1949  February         118
2  1949     March         132
3  1949     April         129
4  1949       May         121
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[124]:</div>



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
      <th>year</th>
      <th>1949</th>
      <th>1950</th>
      <th>1951</th>
      <th>1952</th>
      <th>1953</th>
      <th>1954</th>
      <th>1955</th>
      <th>1956</th>
      <th>1957</th>
      <th>1958</th>
      <th>1959</th>
      <th>1960</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>January</th>
      <td>112</td>
      <td>115</td>
      <td>145</td>
      <td>171</td>
      <td>196</td>
      <td>204</td>
      <td>242</td>
      <td>284</td>
      <td>315</td>
      <td>340</td>
      <td>360</td>
      <td>417</td>
    </tr>
    <tr>
      <th>February</th>
      <td>118</td>
      <td>126</td>
      <td>150</td>
      <td>180</td>
      <td>196</td>
      <td>188</td>
      <td>233</td>
      <td>277</td>
      <td>301</td>
      <td>318</td>
      <td>342</td>
      <td>391</td>
    </tr>
    <tr>
      <th>March</th>
      <td>132</td>
      <td>141</td>
      <td>178</td>
      <td>193</td>
      <td>236</td>
      <td>235</td>
      <td>267</td>
      <td>317</td>
      <td>356</td>
      <td>362</td>
      <td>406</td>
      <td>419</td>
    </tr>
    <tr>
      <th>April</th>
      <td>129</td>
      <td>135</td>
      <td>163</td>
      <td>181</td>
      <td>235</td>
      <td>227</td>
      <td>269</td>
      <td>313</td>
      <td>348</td>
      <td>348</td>
      <td>396</td>
      <td>461</td>
    </tr>
    <tr>
      <th>May</th>
      <td>121</td>
      <td>125</td>
      <td>172</td>
      <td>183</td>
      <td>229</td>
      <td>234</td>
      <td>270</td>
      <td>318</td>
      <td>355</td>
      <td>363</td>
      <td>420</td>
      <td>472</td>
    </tr>
    <tr>
      <th>June</th>
      <td>135</td>
      <td>149</td>
      <td>178</td>
      <td>218</td>
      <td>243</td>
      <td>264</td>
      <td>315</td>
      <td>374</td>
      <td>422</td>
      <td>435</td>
      <td>472</td>
      <td>535</td>
    </tr>
    <tr>
      <th>July</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>230</td>
      <td>264</td>
      <td>302</td>
      <td>364</td>
      <td>413</td>
      <td>465</td>
      <td>491</td>
      <td>548</td>
      <td>622</td>
    </tr>
    <tr>
      <th>August</th>
      <td>148</td>
      <td>170</td>
      <td>199</td>
      <td>242</td>
      <td>272</td>
      <td>293</td>
      <td>347</td>
      <td>405</td>
      <td>467</td>
      <td>505</td>
      <td>559</td>
      <td>606</td>
    </tr>
    <tr>
      <th>September</th>
      <td>136</td>
      <td>158</td>
      <td>184</td>
      <td>209</td>
      <td>237</td>
      <td>259</td>
      <td>312</td>
      <td>355</td>
      <td>404</td>
      <td>404</td>
      <td>463</td>
      <td>508</td>
    </tr>
    <tr>
      <th>October</th>
      <td>119</td>
      <td>133</td>
      <td>162</td>
      <td>191</td>
      <td>211</td>
      <td>229</td>
      <td>274</td>
      <td>306</td>
      <td>347</td>
      <td>359</td>
      <td>407</td>
      <td>461</td>
    </tr>
    <tr>
      <th>November</th>
      <td>104</td>
      <td>114</td>
      <td>146</td>
      <td>172</td>
      <td>180</td>
      <td>203</td>
      <td>237</td>
      <td>271</td>
      <td>305</td>
      <td>310</td>
      <td>362</td>
      <td>390</td>
    </tr>
    <tr>
      <th>December</th>
      <td>118</td>
      <td>140</td>
      <td>166</td>
      <td>194</td>
      <td>201</td>
      <td>229</td>
      <td>278</td>
      <td>306</td>
      <td>336</td>
      <td>337</td>
      <td>405</td>
      <td>432</td>
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
<p><a name="PandasDummyencoder"></a></p>
<h3 id="Pandas-Dummy-Encoding">Pandas Dummy Encoding<a class="anchor-link" href="#Pandas-Dummy-Encoding">&#182;</a></h3><p>Am Beispiel der Titanic Datasets feature sex Male /Femal  &amp;&amp; embarked</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[125]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">titanic</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/titanic_train.csv&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">titanic</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">titanic</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Index([&#39;PassengerId&#39;, &#39;Survived&#39;, &#39;Pclass&#39;, &#39;Name&#39;, &#39;Sex&#39;, &#39;Age&#39;, &#39;SibSp&#39;,
       &#39;Parch&#39;, &#39;Ticket&#39;, &#39;Fare&#39;, &#39;Cabin&#39;, &#39;Embarked&#39;],
      dtype=&#39;object&#39;)
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[126]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Version in einer Spalte in Pandas</span>
<span class="n">pd</span><span class="o">.</span><span class="n">get_dummies</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Sex&#39;</span><span class="p">],</span> <span class="n">drop_first</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[126]:</div>



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
      <th>male</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>1</td>
    </tr>
    <tr>
      <th>887</th>
      <td>0</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
    </tr>
    <tr>
      <th>889</th>
      <td>1</td>
    </tr>
    <tr>
      <th>890</th>
      <td>1</td>
    </tr>
  </tbody123>
</table>
<p>891 rows × 1 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[136]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pd</span><span class="o">.</span><span class="n">get_dummies</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">])</span>
<span class="n">pd</span><span class="o">.</span><span class="n">get_dummies</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Embarked&#39;</span><span class="p">],</span> <span class="n">drop_first</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[136]:</div>



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
      <th>Q</th>
      <th>S</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>887</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>889</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>890</th>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody123>
</table>
<p>891 rows × 2 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[137]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">titanic</span><span class="o">.</span><span class="n">Sex</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>0        male
1      female
2      female
3      female
4        male
        ...  
886      male
887    female
888    female
889      male
890      male
Name: Sex, Length: 891, dtype: object
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Daten-Input-und-Output">Daten Input und Output<a class="anchor-link" href="#Daten-Input-und-Output">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Csv">Csv<a class="anchor-link" href="#Csv">&#182;</a></h3><p>Comma Seperated Vector / Value</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[138]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Input</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/example.csv&#39;</span><span class="p">)</span>
<span class="n">df</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[138]:</div>



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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
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
<div class="prompt input_prompt">In&nbsp;[139]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Input</span>
<span class="n">advertismentData</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/islrData_advertising.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">advertismentData</span> <span class="o">=</span> <span class="n">advertismentData</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Unnamed: 0&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="c1">#advertismentData.head123()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[140]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Input</span>
<span class="n">labelList</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;symboling&#39;</span><span class="p">,</span><span class="s1">&#39;normalizedLosses&#39;</span><span class="p">,</span><span class="s1">&#39;make&#39;</span><span class="p">,</span><span class="s1">&#39;fuelType&#39;</span><span class="p">,</span><span class="s1">&#39;aspiration&#39;</span><span class="p">,</span><span class="s1">&#39;numOfDoors&#39;</span><span class="p">,</span><span class="s1">&#39;body123Style&#39;</span><span class="p">,</span><span class="s1">&#39;driveWheels&#39;</span><span class="p">,</span><span class="s1">&#39;engineLocation&#39;</span><span class="p">,</span>
           <span class="s1">&#39;wheelBase&#39;</span><span class="p">,</span><span class="s1">&#39;length&#39;</span><span class="p">,</span><span class="s1">&#39;width&#39;</span><span class="p">,</span><span class="s1">&#39;height&#39;</span><span class="p">,</span><span class="s1">&#39;curbWeight&#39;</span><span class="p">,</span><span class="s1">&#39;engineType&#39;</span><span class="p">,</span><span class="s1">&#39;numOfCylinders&#39;</span><span class="p">,</span><span class="s1">&#39;engineSize&#39;</span><span class="p">,</span><span class="s1">&#39;fuelSystem&#39;</span><span class="p">,</span><span class="s1">&#39;bore&#39;</span><span class="p">,</span>
           <span class="s1">&#39;stroke&#39;</span><span class="p">,</span><span class="s1">&#39;compressionRatio&#39;</span><span class="p">,</span><span class="s1">&#39;horsepower&#39;</span><span class="p">,</span><span class="s1">&#39;peakRpm&#39;</span><span class="p">,</span><span class="s1">&#39;cityMpg&#39;</span><span class="p">,</span><span class="s1">&#39;highwayMpg&#39;</span><span class="p">,</span><span class="s1">&#39;price&#39;</span><span class="p">]</span>
<span class="n">carDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/data_car.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="n">labelList</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[141]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Output =&gt; schreiben in eine CSV Datei</span>
<span class="n">df</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;./data/my_example.csv&#39;</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Excel">Excel<a class="anchor-link" href="#Excel">&#182;</a></h3><p>Pandas kann Excel-Dateien lesen und schreiben. Beachtet aber, dass dabei nur Daten importiert werden. Formeln und Bilder sind dabei nicht eingeschlossen. Makros oder Bilder in der Datei zu haben kann die <code>read_excel</code> Methode zum Abstürzen bringen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[142]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Input</span>
<span class="c1">#!pip install xlrd </span>
<span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="s1">&#39;./data/Excel_Sample.xlsx&#39;</span><span class="p">,</span><span class="n">sheet_name</span><span class="o">=</span><span class="s1">&#39;Sheet1&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[142]:</div>



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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
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
<div class="prompt input_prompt">In&nbsp;[143]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Output</span>
<span class="c1"># !pip install openpyxl</span>
<span class="n">df</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="s1">&#39;./data/Excel_SampleOut.xlsx&#39;</span><span class="p">,</span><span class="n">sheet_name</span><span class="o">=</span><span class="s1">&#39;Sheet1&#39;</span><span class="p">)</span>
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
<span class="ansi-red-intense-fg ansi-bold">ModuleNotFoundError</span>                       Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-143-46aacd5cea8a&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold"># Output</span>
<span class="ansi-green-fg">      2</span> <span class="ansi-red-intense-fg ansi-bold"># !pip install openpyxl</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 3</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>df<span class="ansi-yellow-intense-fg ansi-bold">.</span>to_excel<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;./data/Excel_SampleOut.xlsx&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span>sheet_name<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-blue-intense-fg ansi-bold">&#39;Sheet1&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\core\generic.py</span> in <span class="ansi-cyan-fg">to_excel</span><span class="ansi-blue-intense-fg ansi-bold">(self, excel_writer, sheet_name, na_rep, float_format, columns, head123er123, index, index_label, startrow, startcol, engine, merge_cells, encoding, inf_rep, verbose, freeze_panes)</span>
<span class="ansi-green-fg">   2179</span>             startcol<span class="ansi-yellow-intense-fg ansi-bold">=</span>startcol<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">   2180</span>             freeze_panes<span class="ansi-yellow-intense-fg ansi-bold">=</span>freeze_panes<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2181</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>engine<span class="ansi-yellow-intense-fg ansi-bold">=</span>engine<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">   2182</span>         )
<span class="ansi-green-fg">   2183</span> 

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\io\formats\excel.py</span> in <span class="ansi-cyan-fg">write</span><span class="ansi-blue-intense-fg ansi-bold">(self, writer, sheet_name, startrow, startcol, freeze_panes, engine)</span>
<span class="ansi-green-fg">    724</span>             need_save <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">False</span>
<span class="ansi-green-fg">    725</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 726</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>writer <span class="ansi-yellow-intense-fg ansi-bold">=</span> ExcelWriter<span class="ansi-yellow-intense-fg ansi-bold">(</span>stringify_path<span class="ansi-yellow-intense-fg ansi-bold">(</span>writer<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> engine<span class="ansi-yellow-intense-fg ansi-bold">=</span>engine<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    727</span>             need_save <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">True</span>
<span class="ansi-green-fg">    728</span> 

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\io\excel\_openpyxl.py</span> in <span class="ansi-cyan-fg">__init__</span><span class="ansi-blue-intense-fg ansi-bold">(self, path, engine, mode, **engine_kwargs)</span>
<span class="ansi-green-fg">     16</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> __init__<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> path<span class="ansi-yellow-intense-fg ansi-bold">,</span> engine<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> mode<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-blue-intense-fg ansi-bold">&#34;w&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>engine_kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">     17</span>         <span class="ansi-red-intense-fg ansi-bold"># Use the openpyxl module as the Excel writer.</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 18</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">from</span> openpyxl<span class="ansi-yellow-intense-fg ansi-bold">.</span>workbook <span class="ansi-green-intense-fg ansi-bold">import</span> Workbook
<span class="ansi-green-fg">     19</span> 
<span class="ansi-green-fg">     20</span>         super<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">.</span>__init__<span class="ansi-yellow-intense-fg ansi-bold">(</span>path<span class="ansi-yellow-intense-fg ansi-bold">,</span> mode<span class="ansi-yellow-intense-fg ansi-bold">=</span>mode<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>engine_kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-red-intense-fg ansi-bold">ModuleNotFoundError</span>: No module named &#39;openpyxl&#39;</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Html">Html<a class="anchor-link" href="#Html">&#182;</a></h3><p>wir extrheiern die HTML Tabelel von "<a href="http://www.fdic.gov/bank/individual/failed/banklist.html">http://www.fdic.gov/bank/individual/failed/banklist.html</a>" =&gt; heir erhalten wir die erste Liste</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[144]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39;</span>
<span class="sd">!pip install lxml</span>
<span class="sd">!pip install html5lib</span>
<span class="sd">!pip install BeautifulSoup4</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="n">df_html</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_html</span><span class="p">(</span><span class="s1">&#39;http://www.fdic.gov/bank/individual/failed/banklist.html&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_html</span><span class="p">)</span>
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
<span class="ansi-red-intense-fg ansi-bold">ImportError</span>                               Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-144-5c25fd667a0f&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      4</span> <span class="ansi-red-fg">!</span>pip install BeautifulSoup4
<span class="ansi-green-fg">      5</span> &#39;&#39;&#39;
<span class="ansi-green-intense-fg ansi-bold">----&gt; 6</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>df_html <span class="ansi-yellow-intense-fg ansi-bold">=</span> pd<span class="ansi-yellow-intense-fg ansi-bold">.</span>read_html<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;http://www.fdic.gov/bank/individual/failed/banklist.html&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      7</span> print<span class="ansi-yellow-intense-fg ansi-bold">(</span>df_html<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\io\html.py</span> in <span class="ansi-cyan-fg">read_html</span><span class="ansi-blue-intense-fg ansi-bold">(io, match, flavor, head123er123, index_col, skiprows, attrs, parse_dates, thousands, encoding, decimal, converters, na_values, keep_default_na, displayed_only)</span>
<span class="ansi-green-fg">   1098</span>         na_values<span class="ansi-yellow-intense-fg ansi-bold">=</span>na_values<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">   1099</span>         keep_default_na<span class="ansi-yellow-intense-fg ansi-bold">=</span>keep_default_na<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1100</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>displayed_only<span class="ansi-yellow-intense-fg ansi-bold">=</span>displayed_only<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">   1101</span>     )

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\io\html.py</span> in <span class="ansi-cyan-fg">_parse</span><span class="ansi-blue-intense-fg ansi-bold">(flavor, io, match, attrs, encoding, displayed_only, **kwargs)</span>
<span class="ansi-green-fg">    889</span>     retained <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">None</span>
<span class="ansi-green-fg">    890</span>     <span class="ansi-green-intense-fg ansi-bold">for</span> flav <span class="ansi-green-intense-fg ansi-bold">in</span> flavor<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 891</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>parser <span class="ansi-yellow-intense-fg ansi-bold">=</span> _parser_dispatch<span class="ansi-yellow-intense-fg ansi-bold">(</span>flav<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    892</span>         p <span class="ansi-yellow-intense-fg ansi-bold">=</span> parser<span class="ansi-yellow-intense-fg ansi-bold">(</span>io<span class="ansi-yellow-intense-fg ansi-bold">,</span> compiled_match<span class="ansi-yellow-intense-fg ansi-bold">,</span> attrs<span class="ansi-yellow-intense-fg ansi-bold">,</span> encoding<span class="ansi-yellow-intense-fg ansi-bold">,</span> displayed_only<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    893</span> 

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\tensorflow_cpu\lib\site-packages\pandas\io\html.py</span> in <span class="ansi-cyan-fg">_parser_dispatch</span><span class="ansi-blue-intense-fg ansi-bold">(flavor)</span>
<span class="ansi-green-fg">    846</span>     <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    847</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> <span class="ansi-green-intense-fg ansi-bold">not</span> _HAS_LXML<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 848</span><span class="ansi-yellow-intense-fg ansi-bold">             </span><span class="ansi-green-intense-fg ansi-bold">raise</span> ImportError<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;lxml not found, please install it&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    849</span>     <span class="ansi-green-intense-fg ansi-bold">return</span> _valid_parsers<span class="ansi-yellow-intense-fg ansi-bold">[</span>flavor<span class="ansi-yellow-intense-fg ansi-bold">]</span>
<span class="ansi-green-fg">    850</span> 

<span class="ansi-red-intense-fg ansi-bold">ImportError</span>: lxml not found, please install it</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Sql">Sql<a class="anchor-link" href="#Sql">&#182;</a></h3><p>es gibt zu der DB (MYsql / postgress / MSSQl usw) jeweils eine eigenen Connector. Hier nur im Schnellformat.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install sqlalchemy</span>
<span class="kn">from</span> <span class="nn">sqlalchemy</span> <span class="kn">import</span> <span class="n">create_engine</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span><span class="s1">&#39;sqlite:///:memory:&#39;</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">to_sql</span><span class="p">(</span><span class="s1">&#39;data&#39;</span><span class="p">,</span> <span class="n">engine</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sql_df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="s1">&#39;data&#39;</span><span class="p">,</span><span class="n">con</span><span class="o">=</span><span class="n">engine</span><span class="p">)</span>
<span class="n">sql_df</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="JSON">JSON<a class="anchor-link" href="#JSON">&#182;</a></h3><p>ähnlich wie xml, nur muss man im Json erhehblich weniger Overhead123 schreiebn. // muss noch erweitert werden</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">pandas</span> <span class="kn">import</span> <span class="n">Series</span><span class="p">,</span> <span class="n">DataFrame</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Heres an example of what a JSON (JavaScript Object Notation) looks like:</span>
<span class="n">json_obj</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span>
<span class="s2">{   &quot;zoo_animal&quot;: &quot;Lion&quot;,</span>
<span class="s2">    &quot;food&quot;: [&quot;Meat&quot;, &quot;Veggies&quot;, &quot;Honey&quot;],</span>
<span class="s2">    &quot;fur&quot;: &quot;Golden&quot;,</span>
<span class="s2">    &quot;clothes&quot;: null, </span>
<span class="s2">    &quot;diet&quot;: [{&quot;zoo_animal&quot;: &quot;Gazelle&quot;, &quot;food&quot;:&quot;grass&quot;, &quot;fur&quot;: &quot;Brown&quot;}]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Let import json module</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="c1">#Lets load json data</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_obj</span><span class="p">)</span>
<span class="c1">#Show</span>
<span class="nb">print</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#WE can also convert back to JSON</span>
<span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#We can simply open JSON data after loading with a DataFrame</span>
<span class="n">dframe</span> <span class="o">=</span> <span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;diet&#39;</span><span class="p">])</span>
<span class="c1">#Show</span>
<span class="n">dframe</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="YAML">YAML<a class="anchor-link" href="#YAML">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>

<span class="n">dct</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="s1">&#39;&#39;&#39;</span>
<span class="s1">name: John</span>
<span class="s1">age: 30</span>
<span class="s1">automobiles:</span>
<span class="s1">- brand: Honda</span>
<span class="s1">  type: Odyssey</span>
<span class="s1">  year: 2018</span>
<span class="s1">- brand: Toyota</span>
<span class="s1">  type: Sienna</span>
<span class="s1">  year: 2015</span>
<span class="s1">&#39;&#39;&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">assert</span> <span class="n">dct</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;John&#39;</span>
<span class="k">assert</span> <span class="n">dct</span><span class="p">[</span><span class="s1">&#39;age&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">30</span>
<span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">dct</span><span class="p">[</span><span class="s2">&quot;automobiles&quot;</span><span class="p">])</span> <span class="o">==</span> <span class="mi">2</span>
<span class="k">assert</span> <span class="n">dct</span><span class="p">[</span><span class="s2">&quot;automobiles&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;brand&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Honda&quot;</span>
<span class="k">assert</span> <span class="n">dct</span><span class="p">[</span><span class="s2">&quot;automobiles&quot;</span><span class="p">][</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;year&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">2015</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">dct</span><span class="p">[</span><span class="s1">&#39;age&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="New-Yaml-Example">New Yaml Example<a class="anchor-link" href="#New-Yaml-Example">&#182;</a></h4><p>im folgenden Junk erstelle ich eine Liste in YAML Format</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>

<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;item 1&#39;</span><span class="p">,</span><span class="s1">&#39;item 2&#39;</span><span class="p">,</span><span class="s1">&#39;item 3&#39;</span><span class="p">,</span><span class="s1">&#39;item 4&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">explicit_start</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">default_flow_style</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>---
- item 1
- item 2
- item 3
- item 4

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Einlesen-von-YAML-dateien">Einlesen von YAML dateien<a class="anchor-link" href="#Einlesen-von-YAML-dateien">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;./data/fruits.yaml&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">fruits_list</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Loader</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">FullLoader</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fruits_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;apples&#39;: 20, &#39;mangoes&#39;: 2, &#39;bananas&#39;: 3, &#39;grapes&#39;: 100, &#39;pineapples&#39;: 1}
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;./data/categories.yaml&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">fruits_list</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Loader</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">FullLoader</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fruits_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;sports&#39;: [&#39;soccer&#39;, &#39;football&#39;, &#39;basketball&#39;, &#39;cricket&#39;, &#39;hockey&#39;, &#39;table tennis&#39;], &#39;countries&#39;: [&#39;Pakistan&#39;, &#39;USA&#39;, &#39;India&#39;, &#39;China&#39;, &#39;Germany&#39;, &#39;France&#39;, &#39;Spain&#39;]}
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;./data/Gattungen.yaml&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">Gattungen_list</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Loader</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">FullLoader</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Gattungen_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;Einzeller&#39;: [&#39;Amoebe&#39;], &#39;SÃ¤ugetiere&#39;: {&#39;Affen&#39;: [&#39;Schimpansen&#39;, &#39;Gorilla&#39;], &#39;Katzenartige&#39;: [&#39;Loewe&#39;, &#39;Tiger&#39;, &#39;Panda&#39;]}, &#39;Fische&#39;: {&#39;Knochenfischen&#39;: [&#39;Dunkler Riesenzackenbarsch&#39;, {&#39;Barrakuda&#39;: [&#39;GrÃ¼ner Barrakuda&#39;, {&#39;Pinker Barrakuda&#39;: [&#39;Kleiner pinker Barrakuda&#39;, &#39;GroÃŸer pinker Barrakuda&#39;]}]}, &#39;Buntbarsch&#39;], &#39;Knorbelfische&#39;: [&#39;Rochen&#39;]}}
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="APIs">APIs<a class="anchor-link" href="#APIs">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Pandas-DataReader">Pandas DataReader<a class="anchor-link" href="#Pandas-DataReader">&#182;</a></h4><p>Funktionen aus pandas_datareader.data und pandas_datareader.wb extrahieren Daten aus verschiedenen Internetquellen in ein pandas DataFrame. Zur Zeit werden die folgenden Quellen unterstützt:</p>
<ul>
<li>Enigma</li>
<li>St.Louis FED (FRED)</li>
<li>Kenneth French’s data library</li>
<li>World Bank</li>
<li>OECD</li>
<li>Eurostat</li>
<li>Thrift Savings Plan</li>
<li>Oanda currency historical rate</li>
<li>Nasdaq Trader symbol definitions (remote_data.nasdaq_symbols)</li>
</ul>
<p>Du solltest immer daran denken, dass verschiedene Quellen unterschiedliche Datenformate unterstützen. Daher implementieren nicht alle Quellen die gleichen Methoden und die Rückgabewertekönnen auch anders aussehen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Link zur DataReader Doku https://pandas-datareader.readthedocs.io/en/latest/remote_data.html &lt;= hier können unterschiedliche Quellen eingbebunden werden</span>
<span class="kn">import</span> <span class="nn">pandas_datareader.data</span> <span class="k">as</span> <span class="nn">web</span>
<span class="kn">import</span> <span class="nn">datetime</span>
<span class="n">start</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2015</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">end</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2017</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">facebook</span> <span class="o">=</span> <span class="n">web</span><span class="o">.</span><span class="n">DataReader</span><span class="p">(</span><span class="s2">&quot;FB&quot;</span><span class="p">,</span> <span class="s1">&#39;stooq&#39;</span><span class="p">,</span> <span class="n">start</span><span class="p">,</span> <span class="n">end</span><span class="p">)</span>
<span class="n">facebook</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Quandl">Quandl<a class="anchor-link" href="#Quandl">&#182;</a></h4><p>Kostnelose Boersen
Kurzer Workaround:</p>
<ol>
<li>man geht auf die Webseite</li>
<li>Man Filtered nach Free-Apis
<img src="data:image/png;base64,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OnRBPVAPaAANoIHq1kCtdaQpL+YRGkADC6GBpEadHX7RTTttuDHuqrvx5uGK+kEDC6SBt/4/+U52avhcN6BYoLwWMeAw7aqjHrh3qQc0gAbQABpIooGF6LySBiYJGkADtaYB24RLelwVpp02JBh3PFAkeaAgLHpZjhp4vmt9uHPsnDegqA5tYNpVRz0sx/uEMqEtNIAG0EDlNFBrHWnKi3mEBtDAQmggqVFnh68a004bX4y7yjXAPNzAFg1UuwZiG1D8dGpJr+mDaVfteiN//CaiATSABtBArgYWovNKGpgkaAAN1JoGbBMu6XFVmXbacGLc5TaePFDABA3UgAZimxEs+U0I7I0i3lrim5UUmQrM/VkD9ycaWNL/icA9yj2KBkrXQK11pCkv5hEaQAMLoYGkRp0dvupMO21USzXues/9nodIOhJoAA2gATSABtAAGkADaAANoIEyaGAhOq+kgUmCBtBArWnANuGSHlelaVeqcfeLV96hcS5D48z/Ppb+v4+wghUaQANoAA2gATSABtDActVArXWkKS/mERpAAwuhgaRGnR2+ak07bQgLjbj7v//91xh2GHZoAA2gATS9Sp0AACAASURBVDSABtAAGkADaAANoIEyaWAhOq+kgUmCBtBArWnANuGSHle1aZfPuPuvqVF59q33aJzL1Dgv1/8ppFz8LzgaQANoAA2gATSABtAAGihdA+XvSHfJUxc/l6uf5v5deXNMGhsD82LgTWeY8892iebppvYxmf0wGseViy/JQ3s3e+frvtMuD73wR7kSS8cO0/jsHx1pfCKzp7vkpno/HyaMn64779k48+TZL+ub0l5/SjJefvRY498hjacv5OTx6qd2HkyaH8gzTwRlC/LW/oqW/4/yVDuGT/l1ClOYVlYDSY06O3zVm3bayNoj7v7uybMYdph1GLZoAA2gATSABtAAGkADaAANlFkD5e+4/1ye+Vj812eW6fZZ8N2HL0mjmlInL/hffGGF+fRz8c2ztMwGwbPmn7n+45fk3voGufeFT3KvN2HeTnvGnjPMF/5lV57zzUET5soLP5e6enfe/SsuyGO2aRfEI9kyqlFn8n1BHitQxqvBtbMn1TSw0vz0Vfl/vxMaCY+9rSl/Is/8LPyu/PVF3DBFA5XQgG3CJT1eEqadGne66cTPX3yLhrnMDTP/81j6/zzCClZoAA2gATSABtAAGkADy1kD5e+sGhMqZjb97CW5oh5UYLplTbvAYIvmI2Z+qQEWuz5qtgWmgwkTM+18Q84PE78u+tmVd0de6hvEN9REfOPNmB6xsMaYjJUxeq1J07cGr84el+uDkXaYdoYr79H7Ax5LgUdSo84Ov2RMu+XcOFI2Hv7QABpAA2gADaABNIAG0AAaWGwNlL/za0yoMpt2gZFl8hs129wmhitM/LvoZ1feY0ZcxFArv2kn8rk8G0yTxbRz16vRAO/wqWYN2CZc0mNMO0auMXoRDaABNIAG0AAaQANoAA2gATTgrw8XM8Tm1xF2GV+5I+WyI+3s6bGvnAryY4wyiaxJl11bzpoea4+ii+fbGHJX335Bfn56zPt76u3PvSFt5joTJjo99hN59t/bpeFB/ZuU894VwZTXipl2n8gzz74pVzWtYJosph2mVFzTfF46mkhq1NnhMe1onHlAQwNoAA2gATSABtAAGkADaAANVKlpt1ka+l6S82aNOn/mqP9vbE07Y765zAxjyNmXe8ef/VGeeWJPZN27qGmXc4U3rfdHlrkZneJqjARjNsbWtCtpeqyOTNwsD73um4o6TfbnrGlXAX2auuLddc/wXfl0YZtwSY8x7WiceUBDA2gADaABNIAG0AAaQANoAA1UwBRJONIuZmjlNQ3MenVzMO2uzD4lDf/2qr+m3hcX5DGzg23OiD2T989ldsIfmeeN0Dse7jZr8lcZ065B6r7zlGQ8s1I36FDzMDbN2DIOTV54L5/RAktYlksDSY06OzymHY0zD2hoAA2gATSABtAAGkADaAANoIHqNO3aX5Dzn34uVy++4O80q0ZVKaaduS6YZmtG2vmj6MJRbPrZbPYQDWNMu+JGWcVMu/oGub4vmCbrDfgrnpdymQzEg2GFBsqnAduES3qMaUfjzAMaGkADaAANoAE0gAbQABpAA2iggqadyJULF2T2zeDvwif+nNP47rGffhCGefOCPPtUe2jQffGJnM9zvTHb5MM/htebNPLtHvtjsz7dB/LUQ37n3MQTnR5b3ChLZNrFynjRG0FnNrFwGYWhwchIu/KZKBhSsFxIDSQ16uzwmHY0zjygoQE0gAbQABpAA2gADaABNIAGKmra5awM9/EF+Xn7Dj/NkxdyTusXnnn2nXZ56IU/+psy2KF0Lbq+dm+U3PV7n5JnLvrrv9lB5OML8tS/t3hpRA25qEknF8bk1rzTY8tk2jV2yc/fDMzKSCZFrrw5Jo3eNF2XaWdPky2el4U0IkgL4wsNlKYB24RLeoxpR+PMAxoaQANoAA2gATSABtAAGkADaKACpl1pHVo6/nBCA2hgOWsgqVFnh8e0o3HmAQ0NoAE0gAbQABpAA2gADaABNIBpx8YOaAANoIEKaMA24ZIeY9rROPOAhgbQABpAA2gADaABNIAG0AAaoLNegc76ch49RNkYHYcGStNAUqPODo9pR+PMAxoaQANoAA2gATSABtAAGkADaADTDtMODaABNFABDdgmXNJjTDsaZx7Q0AAaQANoAA2gATSABtAAGkADdNYr0FlnJFJpI5HgBKflrIGkRp0dHtOOxpkHNDSABtAAGkADaAANoAE0gAbQAKYdph0aQANooAIasE24pMeYdjTOPKChATSABtAAGkADaAANoAE0gAborFegs76cRw9RNkbHoYHSNJDUqLPDY9rROPOAhgbQABpAA2gADaABNIAG0AAawLTDtEMDaAANVEADtgmX9BjTjsaZBzQ0gAbQABpAA2gADaABNIAG0ACd9Qp01hmJVNpIJDjBaTlrIKlRZ4fHtKNx5gENDaABNIAG0AAaQANoAA2gATSAaYdphwbQABqogAZsEy7pMaYdjTMPaGgADaABNIAG0AAaQANoAA2gATrrFeisL+fRQ5SN0XFooDQNJDXq7PCYdjTOPKChATSABtAAGkADaAANoAE0gAYw7TDt0AAaQAMV0IBtwiU9xrSjceYBDQ2gATSABtAAGkADaAANoAE0QGe9Ap11RiKVNhIJTnBazhpIatTZ4THtaJx5QEMDaAANoAE0gAbQABpAA2gADWDaYdqhATSABiqgAduES3qMaUfjzAMaGkADaAANoAE0gAbQABpAA2iAznoFOuvLefQQZWN0HBooTQNJjTo7PKYdjTMPaGgADaABNIAG0AAaQANoAA2gAUw7TDs0gAbQQAU0YJtwSY8x7WiceUBDA2gADaABNIAG0AAaQANoAA3QWa9AZ52RSKWNRIITnJazBpIadXZ4TDsaZx7Q0AAaQANoAA2gATSABtAAGkADmHaYdmgADaCBCmjANuGSHmPa0TjzgIYG0AAaQANoAA2gATSABtAAGqCzXoHO+nIePUTZGB2HBkrTQFKjzg7/V79/97LwBwM0gAbQ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" alt="image.png"></li>
<li>angenommen ich möchte eine bestimmte Börse, so muss ich zunächst in dem Webinterface die entsprechende Börse suchen, den code den ich dann verwende finde ich rechts unten:
<img src="data:image/png;base64,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OnRBPVAPaAANoIHq1kCtdaQpL+YRGkADC6GBpEadHX7RTTttuDHuqrvx5uGK+kEDC6SBt/4/+U52avhcN6BYoLwWMeAw7aqjHrh3qQc0gAbQABpIooGF6LySBiYJGkADtaYB24RLelwVpp02JBh3PFAkeaAgLHpZjhp4vmt9uHPsnDegqA5tYNpVRz0sx/uEMqEtNIAG0EDlNFBrHWnKi3mEBtDAQmggqVFnh68a004bX4y7yjXAPNzAFg1UuwZiG1D8dGpJr+mDaVfteiN//CaiATSABtBArgYWovNKGpgkaAAN1JoGbBMu6XFVmXbacGLc5TaePFDABA3UgAZimxEs+U0I7I0i3lrim5UUmQrM/VkD9ycaWNL/icA9yj2KBkrXQK11pCkv5hEaQAMLoYGkRp0dvupMO21USzXues/9nodIOhJoAA2gATSABtAAGkADaAANoIEyaGAhOq+kgUmCBtBArWnANuGSHlelaVeqcfeLV96hcS5D48z/Ppb+v4+wghUaQANoAA2gATSABtDActVArXWkKS/mERpAAwuhgaRGnR2+ak07bQgLjbj7v//91xh2GHZoAA2gATS9Sp0AACAASURBVDSABtAAGkADaAANoIEyaWAhOq+kgUmCBtBArWnANuGSHle1aZfPuPuvqVF59q33aJzL1Dgv1/8ppFz8LzgaQANoAA2gATSABtAAGihdA+XvSHfJUxc/l6uf5v5deXNMGhsD82LgTWeY8892iebppvYxmf0wGseViy/JQ3s3e+frvtMuD73wR7kSS8cO0/jsHx1pfCKzp7vkpno/HyaMn64779k48+TZL+ub0l5/SjJefvRY498hjacv5OTx6qd2HkyaH8gzTwRlC/LW/oqW/4/yVDuGT/l1ClOYVlYDSY06O3zVm3bayNoj7v7uybMYdph1GLZoAA2gATSABtAAGkADaAANlFkD5e+4/1ye+Vj812eW6fZZ8N2HL0mjmlInL/hffGGF+fRz8c2ztMwGwbPmn7n+45fk3voGufeFT3KvN2HeTnvGnjPMF/5lV57zzUET5soLP5e6enfe/SsuyGO2aRfEI9kyqlFn8n1BHitQxqvBtbMn1TSw0vz0Vfl/vxMaCY+9rSl/Is/8LPyu/PVF3DBFA5XQgG3CJT1eEqadGne66cTPX3yLhrnMDTP/81j6/zzCClZoAA2gATSABtAAGkADy1kD5e+sGhMqZjb97CW5oh5UYLplTbvAYIvmI2Z+qQEWuz5qtgWmgwkTM+18Q84PE78u+tmVd0de6hvEN9REfOPNmB6xsMaYjJUxeq1J07cGr84el+uDkXaYdoYr79H7Ax5LgUdSo84Ov2RMu+XcOFI2Hv7QABpAA2gADaABNIAG0AAaWGwNlL/za0yoMpt2gZFl8hs129wmhitM/LvoZ1feY0ZcxFArv2kn8rk8G0yTxbRz16vRAO/wqWYN2CZc0mNMO0auMXoRDaABNIAG0AAaQANoAA2gATTgrw8XM8Tm1xF2GV+5I+WyI+3s6bGvnAryY4wyiaxJl11bzpoea4+ii+fbGHJX335Bfn56zPt76u3PvSFt5joTJjo99hN59t/bpeFB/ZuU894VwZTXipl2n8gzz74pVzWtYJosph2mVFzTfF46mkhq1NnhMe1onHlAQwNoAA2gATSABtAAGkADaAANVKlpt1ka+l6S82aNOn/mqP9vbE07Y765zAxjyNmXe8ef/VGeeWJPZN27qGmXc4U3rfdHlrkZneJqjARjNsbWtCtpeqyOTNwsD73um4o6TfbnrGlXAX2auuLddc/wXfl0YZtwSY8x7WiceUBDA2gADaABNIAG0AAaQANoAA1UwBRJONIuZmjlNQ3MenVzMO2uzD4lDf/2qr+m3hcX5DGzg23OiD2T989ldsIfmeeN0Dse7jZr8lcZ065B6r7zlGQ8s1I36FDzMDbN2DIOTV54L5/RAktYlksDSY06OzymHY0zD2hoAA2gATSABtAAGkADaAANoIHqNO3aX5Dzn34uVy++4O80q0ZVKaaduS6YZmtG2vmj6MJRbPrZbPYQDWNMu+JGWcVMu/oGub4vmCbrDfgrnpdymQzEg2GFBsqnAduES3qMaUfjzAMaGkADaAANoAE0gAbQABpAA2iggqadyJULF2T2zeDvwif+nNP47rGffhCGefOCPPtUe2jQffGJnM9zvTHb5MM/htebNPLtHvtjsz7dB/LUQ37n3MQTnR5b3ChLZNrFynjRG0FnNrFwGYWhwchIu/KZKBhSsFxIDSQ16uzwmHY0zjygoQE0gAbQABpAA2gADaABNIAGKmra5awM9/EF+Xn7Dj/NkxdyTusXnnn2nXZ56IU/+psy2KF0Lbq+dm+U3PV7n5JnLvrrv9lB5OML8tS/t3hpRA25qEknF8bk1rzTY8tk2jV2yc/fDMzKSCZFrrw5Jo3eNF2XaWdPky2el4U0IkgL4wsNlKYB24RLeoxpR+PMAxoaQANoAA2gATSABtAAGkADaKACpl1pHVo6/nBCA2hgOWsgqVFnh8e0o3HmAQ0NoAE0gAbQABpAA2gADaABNIBpx8YOaAANoIEKaMA24ZIeY9rROPOAhgbQABpAA2gADaABNIAG0AAaoLNegc76ch49RNkYHYcGStNAUqPODo9pR+PMAxoaQANoAA2gATSABtAAGkADaADTDtMODaABNFABDdgmXNJjTDsaZx7Q0AAaQANoAA2gATSABtAAGkADdNYr0FlnJFJpI5HgBKflrIGkRp0dHtOOxpkHNDSABtAAGkADaAANoAE0gAbQAKYdph0aQANooAIasE24pMeYdjTOPKChATSABtAAGkADaAANoAE0gAborFegs76cRw9RNkbHoYHSNJDUqLPDY9rROPOAhgbQABpAA2gADaABNIAG0AAawLTDtEMDaAANVEADtgmX9BjTjsaZBzQ0gAbQABpAA2gADaABNIAG0ACd9Qp01hmJVNpIJDjBaTlrIKlRZ4fHtKNx5gENDaABNIAG0AAaQANoAA2gATSAaYdphwbQABqogAZsEy7pMaYdjTMPaGgADaABNIAG0AAaQANoAA2gATrrFeisL+fRQ5SN0XFooDQNJDXq7PCYdjTOPKChATSABtAAGkADaAANoAE0gAYw7TDt0AAaQAMV0IBtwiU9xrSjceYBDQ2gATSABtAAGkADaAANoAE0QGe9Ap11RiKVNhIJTnBazhpIatTZ4THtaJx5QEMDaAANoAE0gAbQABpAA2gADWDaYdqhATSABiqgAduES3qMaUfjzAMaGkADaAANoAE0gAbQABpAA2iAznoFOuvLefQQZWN0HBooTQNJjTo7PKYdjTMPaGgADaABNIAG0AAaQANoAA2gAUw7TDs0gAbQQAU0YJtwSY8x7WiceUBDA2gADaABNIAG0AAaQANoAA3QWa9AZ52RSKWNRIITnJazBpIadXZ4TDsaZx7Q0AAaQANoAA2gATSABtAAGkADmHaYdmgADaCBCmjANuGSHmPa0TjzgIYG0AAaQANoAA2gATSABtAAGqCzXoHO+nIePUTZGB2HBkrTQFKjzg7/V79/97LwBwM0gAbQ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" alt="image.png"></li>
</ol>
<h2 id="Datenbank-Codes">Datenbank Codes<a class="anchor-link" href="#Datenbank-Codes">&#182;</a></h2><p>Jede Datenbank auf Quandl hat eine kurze Datenbank-ID (3-6 Zeichen), z.B.:</p>
<ul>
<li>CFTC Commitment of Traders Data: CFTC</li>
<li>Core US Stock Fundamentals: SF1</li>
<li>Federal Reserve Economic Data: FRED</li>
</ul>
<p>Jede Datenbank enthält viele Datensätze. Datensätze haben ihre eigenen IDs, die an die ID ihrer zugehörigen Datenbank wie folgt angehängt werden:</p>
<ul>
<li>Commitment of traders for wheat:  CFTC/W_F_ALL</li>
<li>Market capitalization for Apple:  SF1/AAPL_MARKETCAP</li>
<li>US civilian unemployment rate:  FRED/UNRATE</li>
</ul>
<p>Du kannst alle Datensatzcodes einer Datenbank mit einem einzigen API Aufruf runterladen, indem du /codes an deine Datenbank Anfrage anhängst. Der Aufruf liefert eine ZIP-Datei, die ein CSV enthält.</p>
<h3 id="Datenbanken">Datenbanken<a class="anchor-link" href="#Datenbanken">&#182;</a></h3><p>Jeder Quandl Code hat zwei Teile: den Datenbankcode ("WIKI"), der genau sagt, wo die Daten herkommen, und den Datensatzcode ("FB"), der die Zeitreihe markiert, die Du haben möchtest.</p>
<p>Du kannst Quandl Codes auf ihrer Website finden, indem Du ihren Datenbrowser verwendest.</p>
<p><a href="https://www.quandl.com/search">https://www.quandl.com/search</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install quandl</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">quandl</span>
<span class="c1"># bevor ich drauf zugreife muss ich erst den API-Key eingeben</span>
<span class="n">quandl</span><span class="o">.</span><span class="n">ApiConfig</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="s2">&quot;nxKMpiuzMowi5uAUN12u&quot;</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mydata</span> <span class="o">=</span> <span class="n">quandl</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;CITYPOP/CITY_KADAMZAJKADAMJAYBATKYRGYZSTAN&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">mydata</span><span class="p">))</span> <span class="c1">#&lt;= pandas Core</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mydata</span><span class="p">)</span> <span class="c1">#&lt;= hierauf kann dann problem Die Visualisierung drauf gehen</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Zeitliche Einschränkungen</span>
<span class="n">mydata</span> <span class="o">=</span> <span class="n">quandl</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;FRED/GDP&quot;</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="s2">&quot;2001-12-31&quot;</span><span class="p">,</span> <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2005-12-31&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mydata</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Mehrere Abfragen</span>
<span class="n">mydata</span> <span class="o">=</span> <span class="n">quandl</span><span class="o">.</span><span class="n">get</span><span class="p">([</span><span class="s2">&quot;NSE/OIL.1&quot;</span><span class="p">,</span> <span class="s2">&quot;WIKI/AAPL.4&quot;</span><span class="p">])</span>
<span class="n">mydata</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Abfragen über eine Liste</span>
<span class="n">tech_list</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;AAPL&#39;</span><span class="p">,</span><span class="s1">&#39;GOOGL&#39;</span><span class="p">,</span><span class="s1">&#39;MSFT&#39;</span><span class="p">,</span><span class="s1">&#39;AMZN&#39;</span><span class="p">]</span>
<span class="k">for</span> <span class="n">stock</span> <span class="ow">in</span> <span class="n">tech_list</span><span class="p">:</span>   
    <span class="c1"># DataFrame als den Stock Ticker festlegen</span>
    <span class="nb">globals</span><span class="p">()[</span><span class="n">stock</span><span class="p">]</span> <span class="o">=</span> <span class="n">web</span><span class="o">.</span><span class="n">DataReader</span><span class="p">(</span><span class="n">stock</span><span class="p">,</span><span class="s1">&#39;stooq&#39;</span><span class="p">,</span><span class="n">start</span><span class="p">,</span><span class="n">end</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">AAPL</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">GOOGL</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">MSFT</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">AMZN</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Transform...">Transform...<a class="anchor-link" href="#Transform...">&#182;</a></h2><h3 id="...to-Numpy">...to Numpy<a class="anchor-link" href="#...to-Numpy">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[145]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Numpyarr</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">print(type(carDF))</span>
<span class="sd">print(type(Numpyarr))</span>
<span class="sd">print(Numpyarr)</span>
<span class="sd">&#39;&#39;&#39;</span> 

<span class="c1"># hierbei gehen eben die Titel verolren =&gt; muss man sich wieder über die Column reinholen</span>
<span class="n">backToPandas</span> <span class="o">=</span>  <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">Numpyarr</span><span class="p">)</span>
<span class="c1">#print(backToPandas)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="....into-a-Dictionary">....into a Dictionary<a class="anchor-link" href="#....into-a-Dictionary">&#182;</a></h3><p>hier erhalte ich eine liste an dictionaries aus Columname &amp; Value</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[148]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">backToPandas</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="n">orient</span><span class="o">=</span><span class="s1">&#39;records&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[148]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[{0: 0, 1: 1, 2: 2, 3: 3},
 {0: 4, 1: 5, 2: 6, 3: 7},
 {0: 8, 1: 9, 2: 10, 3: 11},
 {0: 12, 1: 13, 2: 14, 3: 15}]</pre>
</div>

</div>

</div>
</div>

</div>
 
