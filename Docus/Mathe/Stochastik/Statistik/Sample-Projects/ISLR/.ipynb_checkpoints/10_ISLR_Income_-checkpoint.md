<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">requests</span>
</pre></div>

    </div>
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
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Starting...&#39;</span><span class="p">)</span>
<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;http://faculty.marshall.usc.edu/gareth-james/ISL/Income1.csv&#39;</span> <span class="c1"># =&gt; Checken ob die Datei bereits vorliegt oder nicht</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;./data/islrData_Income1.csv&quot;</span>
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
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">df</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/islrData_Income1.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
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
<pre>   Education     Income
0  10.000000  26.658839
1  10.401338  27.306435
2  10.842809  22.132410
3  11.244147  21.169841
4  11.645485  15.192634
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Plotting-Observed">Plotting Observed<a class="anchor-link" href="#Plotting-Observed">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">Education</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">Income</span>
<span class="c1">#plt.plot(x, y, &#39;o&#39;)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x270b088ccf8&gt;]</pre>
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
<h2 id="Modelling">Modelling<a class="anchor-link" href="#Modelling">&#182;</a></h2>
</div>
</div>
</div>
 

