'''''

{
"title": "One Hot Encoding",
"keywords": "Ordinal Encoder, OHE, One-Hot-Encoder",
"categories": "",
"description": "hier werden die Möglihckeiten gelitste wie man ein Train Test split vollziehen kann",
"level": "50",
"pageID": "16112020-OneHotEncodingOrdinalEncoding"
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
<h1 id="NaN-Werte">NaN-Werte<a class="anchor-link" href="#NaN-Werte">&#182;</a></h1><p>Die meisten Algorithmen können nicht mit NAN werten umgehen. Daher gibt es hierbei unterschiedliche Anwendungsoptionen. Die zeilen oder Spalten könnnen entweder weggelassen werden. Alternativ können mit hilfe eines Imputers Ein Wert in das leere Feld gesetzt werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#DatenLaden</span>
<span class="n">HOUSING_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;housing&quot;</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">load_housing_data</span><span class="p">(</span><span class="n">housing_path</span><span class="o">=</span><span class="n">HOUSING_PATH</span><span class="p">):</span>
    <span class="n">csv_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">housing_path</span><span class="p">,</span> <span class="s2">&quot;housing.csv&quot;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">csv_path</span><span class="p">)</span>
<span class="n">housing</span> <span class="o">=</span> <span class="n">load_housing_data</span><span class="p">()</span>
<span class="n">housing</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(20640, 10)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#housing.dtypes</span>
<span class="n">housing</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
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
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object 
dtypes: float64(9), object(1)
memory usage: 1.6+ MB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="One-Hot-Encoding">One Hot Encoding<a class="anchor-link" href="#One-Hot-Encoding">&#182;</a></h1><p>Bei OHE werden kategorische = object Variablen in numerische Werte übertragen. Dazu wird zu jeder mögichen Variable eine Liste angelegt und aus jedem möglichen Wert eine eigene Spate</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_cat</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[[</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">]]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">ocean_proximity</span><span class="o">.</span><span class="n">unique</span><span class="p">())</span> <span class="c1"># Anzeige aller möglichen Ausprägungen</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>  ocean_proximity
0        NEAR BAY
1        NEAR BAY
2        NEAR BAY
3        NEAR BAY
4        NEAR BAY
5        NEAR BAY
6        NEAR BAY
7        NEAR BAY
8        NEAR BAY
9        NEAR BAY
(20640, 1)
[&#39;NEAR BAY&#39; &#39;&lt;1H OCEAN&#39; &#39;INLAND&#39; &#39;NEAR OCEAN&#39; &#39;ISLAND&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Ordinal-Encoder-mit-SK-Learn">Ordinal Encoder mit SK-Learn<a class="anchor-link" href="#Ordinal-Encoder-mit-SK-Learn">&#182;</a></h1><p>Beim Ordinal-Encoder werden lediglich die einzlenen Kategorien mit Hilfe einer Map übertragen. Vor und nach dem Ordinal-Encoding besteht lediglich 1 bezugnehmende Spalte</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OrdinalEncoder</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">future_encoders</span> <span class="kn">import</span> <span class="n">OrdinalEncoder</span> <span class="c1"># Scikit-Learn &lt; 0.20</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ordinal_encoder</span> <span class="o">=</span> <span class="n">OrdinalEncoder</span><span class="p">()</span>
<span class="n">housing_cat_encoded</span> <span class="o">=</span> <span class="n">ordinal_encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat_encoded</span><span class="p">[:</span><span class="mi">10</span><span class="p">])</span>
<span class="n">housing_cat_encoded</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[3.]
 [3.]
 [3.]
 [3.]
 [3.]
 [3.]
 [3.]
 [3.]
 [3.]
 [3.]]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(20640, 1)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Anzeige aktueller Ordinal-Encoder Reihenfolge</span>
<span class="n">ordinal_encoder</span><span class="o">.</span><span class="n">categories_</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[array([&#39;&lt;1H OCEAN&#39;, &#39;INLAND&#39;, &#39;ISLAND&#39;, &#39;NEAR BAY&#39;, &#39;NEAR OCEAN&#39;],
       dtype=object)]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Labelencoder">Labelencoder<a class="anchor-link" href="#Labelencoder">&#182;</a></h1><p>Funktioniert ähnlich wie der Ordinal-encoder, lediglich ensteht hierbie keine mehrdimensionale Liste</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">LabelEncoder</span>
<span class="n">encoder</span> <span class="o">=</span> <span class="n">LabelEncoder</span><span class="p">()</span>
<span class="n">housing_cat_LE</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[</span><span class="s2">&quot;ocean_proximity&quot;</span><span class="p">]</span>
<span class="n">housing_cat_LE_encoded</span> <span class="o">=</span> <span class="n">encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>
<span class="n">housing_cat_LE_encoded</span>
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

    <div class="prompt output_prompt">Out[8]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([3, 3, 3, ..., 1, 1, 1])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">encoder</span><span class="o">.</span><span class="n">classes_</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;&lt;1H OCEAN&#39; &#39;INLAND&#39; &#39;ISLAND&#39; &#39;NEAR BAY&#39; &#39;NEAR OCEAN&#39;]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">transformedSingleValue</span> <span class="o">=</span> <span class="n">encoder</span><span class="o">.</span><span class="n">transform</span><span class="p">([</span><span class="s1">&#39;ISLAND&#39;</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">transformedSingleValue</span><span class="p">)</span>
<span class="n">retransformedSingleValue</span> <span class="o">=</span> <span class="n">encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">transformedSingleValue</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">retransformedSingleValue</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[2]
[&#39;ISLAND&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="One-Hot-Encoding">One Hot Encoding<a class="anchor-link" href="#One-Hot-Encoding">&#182;</a></h1><p>Im gegensatz zum Ordinal-Encoder werden beim OHE aus einer Spalte mit M Unique Values = Ausprägungen M Spalten. Hier zunächst die Basic Funktionen die im Kontext von OHE von Bedeutung sind.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OrdinalEncoder</span> <span class="c1"># just to raise an ImportError if Scikit-Learn &lt; 0.20</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">future_encoders</span> <span class="kn">import</span> <span class="n">OneHotEncoder</span> <span class="c1"># Scikit-Learn &lt; 0.20</span>
<span class="c1"># Vorarbeit fürs verständins</span>
<span class="n">cat_encoder</span> <span class="o">=</span> <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">sparse</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">housing_cat_1hot</span> <span class="o">=</span> <span class="n">cat_encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat_1hot</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[0. 0. 0. 1. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 1. 0.]
 ...
 [0. 1. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 1. 0. 0. 0.]]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">ocean_proximity</span><span class="o">.</span><span class="n">unique</span><span class="p">()))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat_1hot</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">housing_cat_1hot</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">categories_</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>5
(20640, 1)
(20640, 5)
&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
&lt;class &#39;numpy.ndarray&#39;&gt;
[array([&#39;&lt;1H OCEAN&#39;, &#39;INLAND&#39;, &#39;ISLAND&#39;, &#39;NEAR BAY&#39;, &#39;NEAR OCEAN&#39;],
      dtype=object)]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">categories_</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[array([&#39;&lt;1H OCEAN&#39;, &#39;INLAND&#39;, &#39;ISLAND&#39;, &#39;NEAR BAY&#39;, &#39;NEAR OCEAN&#39;],
       dtype=object)]</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_cat_1hot</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(20640, 10)
(20640, 5)
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Inverse Transform</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cat_encoder</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]]))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[&#39;&lt;1H OCEAN&#39;]]
[[&#39;INLAND&#39;]]
[[&#39;ISLAND&#39;]]
[[&#39;NEAR BAY&#39;]]
[[&#39;NEAR OCEAN&#39;]]
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing_cat</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
<span class="n">cat_encoder</span><span class="o">.</span><span class="n">get_feature_names</span><span class="p">([</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Index([&#39;ocean_proximity&#39;], dtype=&#39;object&#39;)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;ocean_proximity_&lt;1H OCEAN&#39;, &#39;ocean_proximity_INLAND&#39;,
       &#39;ocean_proximity_ISLAND&#39;, &#39;ocean_proximity_NEAR BAY&#39;,
       &#39;ocean_proximity_NEAR OCEAN&#39;], dtype=object)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="OHE-auf-das-Dataframe-angewendet">OHE auf das Dataframe angewendet<a class="anchor-link" href="#OHE-auf-das-Dataframe-angewendet">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">housing_cat</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[[</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">]]</span>
<span class="n">housing</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;ocean_proximity&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>  
<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(20640, 10)
(20640, 9)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cat_encoder</span> <span class="o">=</span> <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">sparse</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">housing_ocean_proximity_cat_1hot</span> <span class="o">=</span> <span class="n">cat_encoder</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">housing_cat</span><span class="p">)</span>
<span class="n">titles</span> <span class="o">=</span> <span class="n">cat_encoder</span><span class="o">.</span><span class="n">get_feature_names</span><span class="p">([</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">])</span>
<span class="n">partOHEdf</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">housing_ocean_proximity_cat_1hot</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">titles</span><span class="p">)</span>
<span class="n">housingDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">housing</span><span class="p">,</span><span class="n">partOHEdf</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">housingDF</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">print(housing.shape)</span>
<span class="sd">print(partOHEdf.shape)</span>
<span class="sd">print(partOHEdf)</span>
<span class="sd">print(type(housing_ocean_proximity_cat_1hot))</span>
<span class="sd">print(housing_ocean_proximity_cat_1hot.shape)</span>
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
<pre>(20640, 14)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[18]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\nprint(housing.shape)\nprint(partOHEdf.shape)\nprint(partOHEdf)\nprint(type(housing_ocean_proximity_cat_1hot))\nprint(housing_ocean_proximity_cat_1hot.shape)\n&#39;</pre>
</div>

</div>

</div>
</div>

</div>
 

