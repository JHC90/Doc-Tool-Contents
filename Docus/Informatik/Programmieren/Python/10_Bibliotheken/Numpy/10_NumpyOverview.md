<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div># Numpy
NumPy (oder Numpy) ist eine Lineare Algebra Library für Python. Dass sie so wichtig für Data Science mit Python ist, liegt daran, dass fast alle Libraries im PyData Ökosystem auf NumPy zurückgreifen.
NumPy ist außerdem extrem schnell, da es Anbindung an die C Library hat. Für mehr Informationen darüber, warum man Arrays statt Listen verwenden sollte, könnt ihr diesen tollen StackOverflow Post lesen.
Wir werden nur die Grundlagen von NumPy lernen und es installieren, um damit arbeiten zu können.
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><b>Sources</b><br>
<a href="https://www.udemy.com/course/python-fur-finanzanalysen-und-algorithmisches-trading/learn/lecture/10014224#overview">UdemyKursPythonFürFinanzanalysen</a>. Mit Numpy lassen sich somit auch gut die Kapitel der Mathematik abbilden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install numpy</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Create-DataStructure-from-Array">Create DataStructure from Array<a class="anchor-link" href="#Create-DataStructure-from-Array">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Skalare">Skalare<a class="anchor-link" href="#Skalare">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Skalar = 1dimension = Konstante</span>
<span class="n">ownNpArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">2</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Liste-/-Vektor-/-1d">Liste / Vektor / 1d<a class="anchor-link" href="#Liste-/-Vektor-/-1d">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## hier erstelle ich einen NP-Vektor aus einer Python liste</span>
<span class="n">myOwnList</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span> <span class="c1"># =&gt; Liste</span>
<span class="n">ownNpArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">myOwnList</span><span class="p">)</span> 
<span class="n">ownNpArray</span>
<span class="n">ownNpArray</span><span class="o">.</span><span class="n">dtype</span> <span class="c1"># =&gt; Ausgabe der inkludieten Datentypen</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>dtype(&#39;int32&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Anwendung einer Funktion auf einen Vektor ohne Nnumpy</span>
<span class="kn">from</span> <span class="nn">math</span> <span class="kn">import</span> <span class="o">*</span>
<span class="n">ergebnis</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">ownNpArray</span><span class="p">:</span>
    <span class="n">y</span>  <span class="o">=</span> <span class="p">(</span><span class="n">sin</span><span class="p">(</span><span class="n">x</span><span class="p">))</span> <span class="c1"># sin aus dem Math modul</span>
    <span class="n">ergebnis</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ergebnis</span><span class="p">)</span>

<span class="c1">#Anwendung einer Funktion auf einen Vektor MIT Nnumpy</span>
<span class="n">zahlen</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">])</span>
<span class="n">ergebnis</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">zahlen</span><span class="p">)</span> <span class="c1"># sin aus dem numpy Modul</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ergebnis</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.8414709848078965, 0.9092974268256817, 0.1411200080598672]
[0.84147098 0.90929743 0.14112001]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Matrix-/-Tabelle-/-2d">Matrix / Tabelle / 2d<a class="anchor-link" href="#Matrix-/-Tabelle-/-2d">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">meine_matrix</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">],[</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">],[</span><span class="mi">7</span><span class="p">,</span><span class="mi">8</span><span class="p">,</span><span class="mi">9</span><span class="p">]]</span> <span class="c1">#=&gt; mehrdimensionale Liste</span>
<span class="n">meine_matrix</span>
<span class="n">ownNpMatrix</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">meine_matrix</span><span class="p">)</span> 
<span class="n">ownNpMatrix</span><span class="o">.</span><span class="n">dtype</span> <span class="c1"># =&gt; Ausgabe der inkludieten Datentypen</span>
<span class="n">ownNpMatrix</span><span class="o">.</span><span class="n">shape</span> <span class="c1"># =&gt; Ausgabe der inkludieten Datentypen</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(3, 3)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">meine_matrix</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="s1">&#39;Kai&#39;</span><span class="p">,</span><span class="mi">3</span><span class="p">],[</span><span class="mi">4</span><span class="p">,</span><span class="s1">&#39;Eva&#39;</span><span class="p">,</span><span class="mi">6</span><span class="p">],[</span><span class="mi">7</span><span class="p">,</span><span class="s1">&#39;Jochen&#39;</span><span class="p">,</span><span class="mi">9</span><span class="p">]]</span> <span class="c1">#=&gt; mehrdimensionale Liste</span>
<span class="n">meine_matrix</span>
<span class="n">ownNpMatrixWithCategorie</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">meine_matrix</span><span class="p">)</span>
<span class="n">ownNpMatrixWithCategorie</span><span class="p">[:,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">dtype</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>dtype(&#39;&lt;U11&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="create-Array-mit-Numpy-Methoden-/-Sequenz">create Array mit Numpy-Methoden / Sequenz<a class="anchor-link" href="#create-Array-mit-Numpy-Methoden-/-Sequenz">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Spanne über Bereich auf</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span> <span class="c1"># =&gt; array von 0(inkl) bis 10(exkl)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span> <span class="c1"># =&gt; array von 0(inkl) bis 20(exkl) in 2 er schritten</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0 1 2 3 4 5 6 7 8 9]
[ 0  2  4  6  8 10 12 14 16 18]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Zeros-und-Ones">Zeros und Ones<a class="anchor-link" href="#Zeros-und-Ones">&#182;</a></h2><p>Das kann besonders bei der Matritzen Rechnung von Bedeutung werden. Hier erstellen wir arrays mit ledilgich einzelnen werten. Diese Matrizen müssen häufig erstellt werden, daher werden diese hier erzeugt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Vektor mit nur 0</span>
<span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="c1"># Matrix mit nur 0</span>
<span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
<span class="c1"># nur 1er</span>
<span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[9]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Linspace">Linspace<a class="anchor-link" href="#Linspace">&#182;</a></h2><p>Gleichverteilungen in angegebenem Raum</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span> <span class="c1"># Array</span>
<span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">51</span><span class="p">)</span><span class="c1"># Matrix</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ,  1.2,  1.4,  1.6,  1.8,  2. ,
        2.2,  2.4,  2.6,  2.8,  3. ,  3.2,  3.4,  3.6,  3.8,  4. ,  4.2,
        4.4,  4.6,  4.8,  5. ,  5.2,  5.4,  5.6,  5.8,  6. ,  6.2,  6.4,
        6.6,  6.8,  7. ,  7.2,  7.4,  7.6,  7.8,  8. ,  8.2,  8.4,  8.6,
        8.8,  9. ,  9.2,  9.4,  9.6,  9.8, 10. ])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Eye-Fkt-||-Einheitsmatrix">Eye-Fkt || Einheitsmatrix<a class="anchor-link" href="#Eye-Fkt-||-Einheitsmatrix">&#182;</a></h2><p>erstellt eine Einheitsmatrix</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[11]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Symetrische-Matrix-via-Loop">Symetrische Matrix via Loop<a class="anchor-link" href="#Symetrische-Matrix-via-Loop">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr2d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">arr_laenge</span> <span class="o">=</span> <span class="n">arr2d</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="c1">#print(arr2d)</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">arr_laenge</span><span class="p">):</span>
    <span class="n">arr2d</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>
    
<span class="n">arr2d</span>
<span class="c1">#print(arr2d)</span>

<span class="c1"># Subfunctions</span>
<span class="n">arr2d</span><span class="p">[[</span><span class="mi">2</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="mi">8</span><span class="p">]]</span>
<span class="n">arr2d</span><span class="p">[[</span><span class="mi">6</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">8</span><span class="p">,</span><span class="mi">2</span><span class="p">]]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [8., 8., 8., 8., 8., 8., 8., 8., 8., 8.],
       [2., 2., 2., 2., 2., 2., 2., 2., 2., 2.]])</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr2d</span><span class="p">[[</span><span class="mi">2</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="mi">8</span><span class="p">]]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [8., 8., 8., 8., 8., 8., 8., 8., 8., 8.]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Numpy-Basic-Functions">Numpy Basic-Functions<a class="anchor-link" href="#Numpy-Basic-Functions">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Seed">Seed<a class="anchor-link" href="#Seed">&#182;</a></h2><p>Ein Seed sorgt dafür, dass random funktionen beim Wiederholten ausführen, immer die gleichen Results zurückgegben. Das hat den Sinn und Zweck, dass während Entwicklungen immer die gleichen Bedingungen geschaffen werden können.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">101</span><span class="p">)</span> <span class="c1">#&lt;= hier eine Nummer rein, und es kommt immer das gleiche An zahlen raus</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Random">Random<a class="anchor-link" href="#Random">&#182;</a></h2><p>erstellt Random zahlen. Random return eine <a href="https://github.com/JHC90/Basic-DataScience-Skills/wiki/Statistics_Basics_015_Normalverteilung">Normalverteilung</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="c1"># Bereich zwischen 0 &amp; 1 || 1 return value</span>
<span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="c1"># Bereich zwischen 0 &amp; 1 || 3 Return value</span>
<span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span> <span class="c1"># Random Matrix 5x5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[0.68527698, 0.83389686, 0.30696622, 0.89361308, 0.72154386],
       [0.18993895, 0.55422759, 0.35213195, 0.1818924 , 0.78560176],
       [0.96548322, 0.23235366, 0.08356143, 0.60354842, 0.72899276],
       [0.27623883, 0.68530633, 0.51786747, 0.04848454, 0.13786924],
       [0.18696743, 0.9943179 , 0.5206654 , 0.57878954, 0.73481906]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="randn">randn<a class="anchor-link" href="#randn">&#182;</a></h2><p>erstellt Random zahlen. randn return eine <a href="https://github.com/JHC90/Basic-DataScience-Skills/wiki/Statistics_Basics_015_Normalverteilung">StandardNormalverteilung</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">500</span><span class="p">)</span>
<span class="n">randMatrix</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="n">randMatrix</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[-0.38205785, -0.02764404, -1.03098696],
       [ 1.96154884, -0.53106678,  1.31239754],
       [-0.47034729, -0.6553491 , -0.23077137]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="rand">rand<a class="anchor-link" href="#rand">&#182;</a></h2><p>erstellt Random zahlen. rand returnr eine <a href="https://github.com/JHC90/Basic-DataScience-Skills/wiki/Statistics_Basics_013_Gleichverteilung">Gleichverteilung</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="c1">#np.random.rand(3,3)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([0.6511865 , 0.26867605, 0.36891579, 0.56275138, 0.5693618 ])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="randint">randint<a class="anchor-link" href="#randint">&#182;</a></h2><p>Gibt Zufallszahlen von <code>low</code>(inklusive) bis <code>high</code>(exklusive) zurück.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">100</span><span class="p">)</span> <span class="c1"># =&gt; 1 ganzzahlige Zufallszahl zwischen 1 &amp; 100</span>
<span class="n">randArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">100</span><span class="p">,</span><span class="mi">10</span><span class="p">)</span><span class="c1"># =&gt; 10 Zufallszahlen zwischen 1&amp;100</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="max,-min,-argmax,-argmin">max, min, argmax, argmin<a class="anchor-link" href="#max,-min,-argmax,-argmin">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">randArray</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[19]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([94, 18, 35, 25, 24, 47, 56, 26, 65, 91])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Max-Value aus dem Randarray</span>
<span class="n">randArray</span><span class="o">.</span><span class="n">max</span><span class="p">()</span>
<span class="c1"># index des Max-Value aus dem Randarray</span>
<span class="n">randArray</span><span class="o">.</span><span class="n">argmax</span><span class="p">()</span>
<span class="c1"># Min-Value aus dem Randarray</span>
<span class="n">randArray</span><span class="o">.</span><span class="n">min</span><span class="p">()</span>
<span class="c1"># index des Min-Value aus dem Randarray</span>
<span class="n">randArray</span><span class="o">.</span><span class="n">argmin</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Alternativen</span>
<span class="n">np</span><span class="o">.</span><span class="n">max</span><span class="p">(</span><span class="n">randArray</span><span class="p">)</span>
<span class="n">np</span><span class="o">.</span><span class="n">min</span><span class="p">(</span><span class="n">randArray</span><span class="p">)</span>
<span class="n">np</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">randArray</span><span class="p">)</span>
<span class="n">np</span><span class="o">.</span><span class="n">argmin</span><span class="p">(</span><span class="n">randArray</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Reshape">Reshape<a class="anchor-link" href="#Reshape">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data for Reshape-Section</span>
<span class="n">arr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">30</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Shape-Function">Shape Function<a class="anchor-link" href="#Shape-Function">&#182;</a></h2><p>mit der Shape function kann die gegenwärtige "Form des Arrays" abgefragt werden. Achtung das ist kein funktionsaufruf =&gt; keine "()" nach Aufruf des shape commands</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">randArray</span><span class="o">.</span><span class="n">shape</span>
<span class="n">randMatrix</span><span class="o">.</span><span class="n">shape</span>
<span class="n">randMatrix</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="c1"># =rows</span>
<span class="n">randMatrix</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="c1"># =Columns</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>




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
<h2 id="Vektor-=&gt;-Matrix">Vektor =&gt; Matrix<a class="anchor-link" href="#Vektor-=&gt;-Matrix">&#182;</a></h2><p>hier wird ein Vektor zu einer Matrix umformuliert. D.h. es ist wichtig dass die Anzahl der elemente in dem Vektor gleich das Produkt aus Zeilen und Spalten aus der Matrix sind. Bsp 30 = 5<em>6 = 3</em>10 = 10*3 ......</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">)</span> <span class="c1"># Tranform in Matrix</span>
<span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">10</span><span class="p">)</span><span class="c1"># Tranform in Matrix</span>
<span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span><span class="c1"># Tranform in Matrix</span>
<span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">30</span><span class="p">,)</span><span class="c1"># Tranform in Vektor = Flatten</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[24]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="o">.</span><span class="n">dtype</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>dtype(&#39;int32&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Good-to-know-bei-Numpy-f&#252;r-Select-&amp;-Update-Data-||-Slect-vs-Copy">Good to know bei Numpy f&#252;r Select &amp; Update Data || Slect vs Copy<a class="anchor-link" href="#Good-to-know-bei-Numpy-f&#252;r-Select-&amp;-Update-Data-||-Slect-vs-Copy">&#182;</a></h1><p>Diesen Mult</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Ist-Situation">Ist-Situation<a class="anchor-link" href="#Ist-Situation">&#182;</a></h2><p>wenn ich aus einem gegebenen ORGINALARRAY ein SUBARRAY auswähle un dieses SUBARRAY ändere, so ändert sich auch der Wertebereich im eigentlichen ORGINALARRAY.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ORGINALARRAY</span> <span class="o">=</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ORGINALARRAY</span><span class="p">)</span>
<span class="n">SUBARRAY</span> <span class="o">=</span> <span class="n">ORGINALARRAY</span><span class="p">[</span><span class="mi">7</span><span class="p">:]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">SUBARRAY</span><span class="p">)</span>
<span class="n">SUBARRAY</span><span class="p">[:]</span> <span class="o">=</span> <span class="mi">100</span> <span class="c1"># =&gt; alle werte in Subarray sind jetzt 100 UND im Orginalbereich hat sich auch der Wertebereich angepasst</span>
<span class="nb">print</span><span class="p">(</span><span class="n">SUBARRAY</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ORGINALARRAY</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[ 0  2  4  6  8 10 12 14 16 18]
[14 16 18]
[100 100 100]
[  0   2   4   6   8  10  12 100 100 100]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Anders ausgedrückt: Beim erstellen eines Subarrays muss man entscheiden ob man ein eigenständiges np.Array benötigt, oder sich immer wieder auf das eigentliche Array bezieht.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="L&#246;sung-mit-Copy">L&#246;sung mit Copy<a class="anchor-link" href="#L&#246;sung-mit-Copy">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ORGINALARRAY</span> <span class="o">=</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">ORGINALARRAY_Copied</span> <span class="o">=</span> <span class="n">ORGINALARRAY</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="n">SUBARRAY</span> <span class="o">=</span> <span class="n">ORGINALARRAY_Copied</span><span class="p">[</span><span class="mi">7</span><span class="p">:]</span>
<span class="n">SUBARRAY</span><span class="p">[:]</span> <span class="o">=</span> <span class="mi">100</span>


<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;##########---Hier nach der Modlifikaiton---##########&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ORGINALARRAY</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ORGINALARRAY_Copied</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">SUBARRAY</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>##########---Hier nach der Modlifikaiton---##########
[ 0  2  4  6  8 10 12 14 16 18]
[  0   2   4   6   8  10  12 100 100 100]
[100 100 100]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Select-Data">Select Data<a class="anchor-link" href="#Select-Data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data for Selection-Demonstration</span>
<span class="n">arr</span> <span class="o">=</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">20</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">arr_2d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(([</span><span class="mi">5</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">15</span><span class="p">],[</span><span class="mi">20</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="mi">30</span><span class="p">],[</span><span class="mi">35</span><span class="p">,</span><span class="mi">40</span><span class="p">,</span><span class="mi">45</span><span class="p">]))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="1D-Vector">1D Vector<a class="anchor-link" href="#1D-Vector">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[29]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Single-Value-from-Vector-mit-Index">Single Value from Vector mit Index<a class="anchor-link" href="#Single-Value-from-Vector-mit-Index">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[30]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>10</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Wertebereich-von-Vector">Wertebereich von Vector<a class="anchor-link" href="#Wertebereich-von-Vector">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span> <span class="c1"># untereGrenze = inkl // obere Grenze = exkl</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[31]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([2, 4, 6, 8])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Auf-Basis-einer-Bedingung-||-Filter-Vector">Auf Basis einer Bedingung || Filter Vector<a class="anchor-link" href="#Auf-Basis-einer-Bedingung-||-Filter-Vector">&#182;</a></h3><p>hierzu arbeitet man mit den ablgelegten Boolean werten</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bsp alle werte &gt; 14</span>
<span class="n">arr</span> <span class="o">&gt;</span> <span class="mi">14</span>
<span class="n">bool_arr</span> <span class="o">=</span> <span class="n">arr</span> <span class="o">&gt;</span> <span class="mi">14</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr</span><span class="p">[</span><span class="n">bool_arr</span><span class="p">])</span>

<span class="c1"># Schneller Filter</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr</span><span class="p">[</span><span class="n">arr</span><span class="o">&gt;</span><span class="mi">17</span><span class="p">])</span> 

<span class="c1"># Filter mit eingehender Variable</span>
<span class="n">x</span><span class="o">=</span><span class="mi">50</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr</span><span class="p">[</span><span class="n">arr</span><span class="o">&gt;</span><span class="n">x</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[ 0  2  4  6  8 10 12 14 16 18]
[16 18]
[18]
[]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="2d-Matrix">2d Matrix<a class="anchor-link" href="#2d-Matrix">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr_2d</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[33]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 5, 10, 15],
       [20, 25, 30],
       [35, 40, 45]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Reihe">Reihe<a class="anchor-link" href="#Reihe">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr_2d</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">arr_2d</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="n">arr_2d</span><span class="p">[</span><span class="mi">2</span><span class="p">,:]</span> <span class="c1"># Andere Schreibweise</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[34]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([35, 40, 45])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Spalte">Spalte<a class="anchor-link" href="#Spalte">&#182;</a></h3><p>vgl Subsets</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr_2d</span><span class="p">[:,</span><span class="mi">0</span><span class="p">]</span>
<span class="n">arr_2d</span><span class="p">[:][</span><span class="mi">1</span><span class="p">]</span> <span class="c1"># Alternative Schreibweise</span>
<span class="c1">#arr_2d[:,2]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[35]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([20, 25, 30])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Wert">Wert<a class="anchor-link" href="#Wert">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr_2d</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[36]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>20</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Subset">Subset<a class="anchor-link" href="#Subset">&#182;</a></h3><p>Das Format ist arr_2d[row][col] oder arr_2d[row,col]</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr_2d</span><span class="p">[:</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">:]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[37]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[10, 15],
       [25, 30]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Update-Data">Update Data<a class="anchor-link" href="#Update-Data">&#182;</a></h1><h2 id="Update-Single-Value">Update Single-Value<a class="anchor-link" href="#Update-Single-Value">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mi">300490</span>
<span class="n">arr</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[38]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([     0,      2,      4, 300490,      8,     10,     12,     14,
           16,     18])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Broadcasting">Broadcasting<a class="anchor-link" href="#Broadcasting">&#182;</a></h2><p>mit dem Broadcasting können mehrere Werte in eienm Array zeitgleich upgedatet werden</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span><span class="o">=</span><span class="mi">100</span>
<span class="n">arr</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[39]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([100, 100, 100, 100, 100,  10,  12,  14,  16,  18])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Arithmetische-Operationen-am-Numpy">Arithmetische Operationen am Numpy<a class="anchor-link" href="#Arithmetische-Operationen-am-Numpy">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Addition-von-Array">Addition von Array<a class="anchor-link" href="#Addition-von-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr2</span> <span class="o">=</span> <span class="n">arr</span> <span class="o">+</span> <span class="n">arr</span>
<span class="n">arr2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([200, 200, 200, 200, 200,  20,  24,  28,  32,  36])</pre>
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
<h2 id="Quadrieren-von-Array">Quadrieren von Array<a class="anchor-link" href="#Quadrieren-von-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr3</span> <span class="o">=</span> <span class="n">arr</span> <span class="o">*</span> <span class="n">arr</span>
<span class="n">arr3</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[41]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([10000, 10000, 10000, 10000, 10000,   100,   144,   196,   256,
         324])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Subtraktion-von-Array">Subtraktion von Array<a class="anchor-link" href="#Subtraktion-von-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr4</span> <span class="o">=</span> <span class="n">arr3</span> <span class="o">-</span><span class="n">arr2</span>
<span class="n">arr4</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[42]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([9800, 9800, 9800, 9800, 9800,   80,  120,  168,  224,  288])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Division-von-Array">Division von Array<a class="anchor-link" href="#Division-von-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr5</span> <span class="o">=</span> <span class="n">arr2</span> <span class="o">/</span> <span class="n">arr</span>
<span class="n">arr5</span> <span class="c1"># 0&gt; wurde zuvor ja mal 2 bzw arr +arr gerechnet =&gt; 2 ist somit logisch</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[43]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([2., 2., 2., 2., 2., 2., 2., 2., 2., 2.])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Potenzieren-von-Array">Potenzieren von Array<a class="anchor-link" href="#Potenzieren-von-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr6</span> <span class="o">=</span> <span class="n">arr</span><span class="o">**</span><span class="mi">2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr6</span><span class="p">)</span>
<span class="n">arr7</span> <span class="o">=</span> <span class="n">arr</span><span class="o">**</span><span class="mi">3</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr7</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[10000 10000 10000 10000 10000   100   144   196   256   324]
[1000000 1000000 1000000 1000000 1000000    1000    1728    2744    4096
    5832]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Wurzel-aus-Array">Wurzel aus Array<a class="anchor-link" href="#Wurzel-aus-Array">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Data for sqrt</span>
<span class="n">ownNpArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">9</span><span class="p">,</span><span class="mi">16</span><span class="p">,</span><span class="mi">25</span><span class="p">])</span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Version1</span>
<span class="n">arr8</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">ownNpArray</span><span class="p">)</span> <span class="c1"># =&gt; </span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr8</span><span class="p">)</span> 
<span class="c1"># Version2</span>
<span class="n">arr9</span> <span class="o">=</span> <span class="n">ownNpArray</span><span class="o">**</span><span class="mf">0.5</span>
<span class="nb">print</span><span class="p">(</span><span class="n">arr9</span><span class="p">)</span> 
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[3. 4. 5.]
[3. 4. 5.]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Calc-Exponenten-e">Calc Exponenten e<a class="anchor-link" href="#Calc-Exponenten-e">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">ownNpArray</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[47]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([8.10308393e+03, 8.88611052e+06, 7.20048993e+10])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Log">Log<a class="anchor-link" href="#Log">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">ownNpArray</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[48]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([2.19722458, 2.77258872, 3.21887582])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Demo-e-und-Log">Demo e und Log<a class="anchor-link" href="#Demo-e-und-Log">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">ownNpArray</span><span class="p">)</span>

<span class="n">expOwnNPArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">ownNpArray</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">expOwnNPArray</span><span class="p">)</span>

<span class="n">logExpOwnNPArray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">expOwnNPArray</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">logExpOwnNPArray</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[ 9 16 25]
[8.10308393e+03 8.88611052e+06 7.20048993e+10]
[ 9. 16. 25.]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Sinus">Sinus<a class="anchor-link" href="#Sinus">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">arr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[50]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([-0.50636564, -0.50636564, -0.50636564, -0.50636564, -0.50636564,
       -0.54402111, -0.53657292,  0.99060736, -0.28790332, -0.75098725])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Cosinus">Cosinus<a class="anchor-link" href="#Cosinus">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">arr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[51]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 0.86231887,  0.86231887,  0.86231887,  0.86231887,  0.86231887,
       -0.83907153,  0.84385396,  0.13673722, -0.95765948,  0.66031671])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Tangens">Tangens<a class="anchor-link" href="#Tangens">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">tan</span><span class="p">(</span><span class="n">arr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[52]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([-0.58721392, -0.58721392, -0.58721392, -0.58721392, -0.58721392,
        0.64836083, -0.63585993,  7.24460662,  0.30063224, -1.13731371])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Matrix">Matrix<a class="anchor-link" href="#Matrix">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">arr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">26</span><span class="p">)</span>
<span class="n">matrix</span> <span class="o">=</span> <span class="n">arr</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
<span class="n">matrix</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[53]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Spaltensumme">Spaltensumme<a class="anchor-link" href="#Spaltensumme">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">matrix</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[55 60 65 70 75]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Matrixsumme">Matrixsumme<a class="anchor-link" href="#Matrixsumme">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">matrix</span><span class="p">)))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>325
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Standardabweichung-Matrix">Standardabweichung Matrix<a class="anchor-link" href="#Standardabweichung-Matrix">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[56]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">std</span><span class="p">(</span><span class="n">matrix</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[56]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>7.211102550927978</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Varianz-Matrix">Varianz Matrix<a class="anchor-link" href="#Varianz-Matrix">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">var</span><span class="p">(</span><span class="n">matrix</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[57]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>52.0</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Conversion-with-other-Libraries">Conversion with other Libraries<a class="anchor-link" href="#Conversion-with-other-Libraries">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[58]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Pandas</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Numpy-to-Pandas">Numpy to Pandas<a class="anchor-link" href="#Numpy-to-Pandas">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[59]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ToPandas</span> <span class="o">=</span>  <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">matrix</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">ToPandas</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ToPandas</span><span class="p">)</span>
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
    0   1   2   3   4
0   1   2   3   4   5
1   6   7   8   9  10
2  11  12  13  14  15
3  16  17  18  19  20
4  21  22  23  24  25
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Pandas-to-Numpy">Pandas to Numpy<a class="anchor-link" href="#Pandas-to-Numpy">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">BackToNumpy</span> <span class="o">=</span> <span class="n">ToPandas</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">BackToNumpy</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">BackToNumpy</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;numpy.ndarray&#39;&gt;
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
</pre>
</div>
</div>

</div>
</div>

</div>
 

