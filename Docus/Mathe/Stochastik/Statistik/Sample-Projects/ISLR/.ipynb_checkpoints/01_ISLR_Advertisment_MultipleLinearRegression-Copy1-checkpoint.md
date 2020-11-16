<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Basics-Lineare-Regression">Basics Lineare Regression<a class="anchor-link" href="#Basics-Lineare-Regression">&#182;</a></h1><p>das hier ist aus Kapitel 2
<a href="http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf">http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf</a></p>
<p>Basic-Understanding:</p>
<ul>
<li><a href="https://towardsdatascience.com/linear-regression-understanding-the-theory-7e53ac2831b5">https://towardsdatascience.com/linear-regression-understanding-the-theory-7e53ac2831b5</a></li>
</ul>
<p>Ziel der MultiplenLinearenRegression ist einen Zusammenhang zwischen mehr als zwei Variablen aufzudecken. Wir starten mit zwei Variabeln</p>
<p>Als Datensatz wird hier der Advertisment von ISLR verwendet. Der datensatz zeigt die Ausgaben von Tv, Radio und newspaper und wie diese sich auf sales auswirken. in diesem Notebook betrachte ich nur ein feature(tv), alle Feature zusammen werden in dem Notebook Multiple Regression betrachtet.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Daten-downloaden">Daten downloaden<a class="anchor-link" href="#Daten-downloaden">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">requests</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Starting...&#39;</span><span class="p">)</span>
<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;http://faculty.marshall.usc.edu/gareth-james/ISL/Advertising.csv&#39;</span> <span class="c1"># =&gt; Checken ob die Datei bereits vorliegt oder nicht</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;./data/islrData_advertising.csv&quot;</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span><span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">output_file</span><span class="p">:</span>
    <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Completed!!!&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Download Starting...
Download Completed!!!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">df</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/islrData_advertising.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Unnamed: 0&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>      TV  radio  newspaper  sales
0  230.1   37.8       69.2   22.1
1   44.5   39.3       45.1   10.4
2   17.2   45.9       69.3    9.3
3  151.5   41.3       58.5   18.5
4  180.8   10.8       58.4   12.9
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Modelling">Modelling<a class="anchor-link" href="#Modelling">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Xs</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;sales&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;TV&#39;</span><span class="p">,</span><span class="s1">&#39;radio&#39;</span><span class="p">,</span><span class="s1">&#39;newspaper&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">r2_score</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">reg</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">Xs</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[33]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Ausgabe des Multiplen Modelles</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;The linear model is: Y = </span><span class="si">{:.5}</span><span class="s2"> + </span><span class="si">{:.5}</span><span class="s2">*TV + </span><span class="si">{:.5}</span><span class="s2">*radio + </span><span class="si">{:.5}</span><span class="s2">*newspaper&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">reg</span><span class="o">.</span><span class="n">intercept_</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">reg</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">reg</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span> <span class="n">reg</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">2</span><span class="p">]))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>The linear model is: Y = 2.9389 + 0.045765*TV + 0.18853*radio + -0.0010375*newspaper
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Dieses Modell kann nicht visualisiert werden, da hier zu viele Dimensionen(&gt;2Feature + 1 Target) dabei sind</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Assessing-Multiple-Linear-Regression-via-the-Relevance">Assessing Multiple Linear Regression via the Relevance<a class="anchor-link" href="#Assessing-Multiple-Linear-Regression-via-the-Relevance">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">statsmodels.api</span> <span class="k">as</span> <span class="nn">sm</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install statsmodel</span>
<span class="kn">import</span> <span class="nn">statsmodels.api</span> <span class="k">as</span> <span class="nn">sm</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">column_stack</span><span class="p">((</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;TV&#39;</span><span class="p">],</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;radio&#39;</span><span class="p">],</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;newspaper&#39;</span><span class="p">]))</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;sales&#39;</span><span class="p">]</span>
<span class="n">X2</span> <span class="o">=</span> <span class="n">sm</span><span class="o">.</span><span class="n">add_constant</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>
<span class="n">est</span> <span class="o">=</span> <span class="n">sm</span><span class="o">.</span><span class="n">OLS</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">X2</span><span class="p">)</span>
<span class="n">est2</span> <span class="o">=</span> <span class="n">est</span><span class="o">.</span><span class="n">fit</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">est2</span><span class="o">.</span><span class="n">summary</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  sales   R-squared:                       0.897
Model:                            OLS   Adj. R-squared:                  0.896
Method:                 Least Squares   F-statistic:                     570.3
Date:                Wed, 18 Mar 2020   Prob (F-statistic):           1.58e-96
Time:                        20:44:51   Log-Likelihood:                -386.18
No. Observations:                 200   AIC:                             780.4
Df Residuals:                     196   BIC:                             793.6
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P&gt;|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.9389      0.312      9.422      0.000       2.324       3.554
x1             0.0458      0.001     32.809      0.000       0.043       0.049
x2             0.1885      0.009     21.893      0.000       0.172       0.206
x3            -0.0010      0.006     -0.177      0.860      -0.013       0.011
==============================================================================
Omnibus:                       60.414   Durbin-Watson:                   2.084
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              151.241
Skew:                          -1.327   Prob(JB):                     1.44e-33
Kurtosis:                       6.332   Cond. No.                         454.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="p-Value">p-Value<a class="anchor-link" href="#p-Value">&#182;</a></h2><p>Der P-Value gibt aufschluss wie sehr die Daten stark miteinander korrelieren. Der P-Wert soll so niedrig wie möglich sein. Je niedriger ein p-Wert desto eher erklärt dieses Feature das Target. Daumenregel: P-Wert eines feature soll kleiner als 0.05 sein. In diesem Beispiel sind TV &amp; Radio siginifikant, newspaper hingegen nicht. Nehmen wir newspaper aus dem Modell werden wir einen etwas schlechterne r² erhalten, dafür besser predicten.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="R&#178;--Value">R&#178; -Value<a class="anchor-link" href="#R&#178;--Value">&#182;</a></h2><p>Der R²(R-squared) ist bei  0.897, das bedeutet das ~90% der Variablität der von Sales somit erklärt wird. Das Modell ist somit um einiges besser als das Modell mit der Linearen Regression. Mehr Fearue ins Modell klopfen sorgt unweigerlich dafür dass ein besserer R² herauskommt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="F-Value">F-Value<a class="anchor-link" href="#F-Value">&#182;</a></h2><p>Wenn ein hoher Zusammenhang besteht, dann ist der F-Wert höher als 1. der F-Wert hier ist 570.3, das besagt dass ein starker Zusammenhang zwischen den Ausgaben und den Sales ist.</p>
<p>Kommen in anderen Modellen mehr Input Feature zusammen kann es vorkommen dass gewisse feature laut p-Value ins modell gehören, jedoch eigentlich gar nicht signifikant sind. Das verhindert dann der F-Value</p>

</div>
</div>
</div>
 

