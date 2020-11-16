<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf">http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf</a> // s52-</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Concetpunal">Concetpunal<a class="anchor-link" href="#Concetpunal">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>1) For each of parts (a) through (d), indicate whether we would generally
expect the performance of a flexible statistical learning method to be
better or worse than an inflexible method. Justify your answer.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>(a) The sample size n is extremely large, and the number of predictors p is small.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>(b) The number of predictors p is extremely large, and the number
of observations n is small.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>(c) The relationship between the predictors and response is highly
non-linear</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>(d) The variance of the error terms, i.e. σ2 = Var(), is extremely
high.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Applied">Applied<a class="anchor-link" href="#Applied">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="College-Dataset">College-Dataset<a class="anchor-link" href="#College-Dataset">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">requests</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Starting...&#39;</span><span class="p">)</span>
<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;http://faculty.marshall.usc.edu/gareth-james/ISL/College.csv&#39;</span> <span class="c1"># =&gt; Checken ob die Datei bereits vorliegt oder nicht</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;./data/islrData_college.csv&quot;</span>
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
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">df</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/islrData_college.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
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
<pre>                     Unnamed: 0 Private  Apps  Accept  Enroll  Top10perc  \
0  Abilene Christian University     Yes  1660    1232     721         23   
1            Adelphi University     Yes  2186    1924     512         16   
2                Adrian College     Yes  1428    1097     336         22   
3           Agnes Scott College     Yes   417     349     137         60   
4     Alaska Pacific University     Yes   193     146      55         16   

   Top25perc  F.Undergrad  P.Undergrad  Outstate  Room.Board  Books  Personal  \
0         52         2885          537      7440        3300    450      2200   
1         29         2683         1227     12280        6450    750      1500   
2         50         1036           99     11250        3750    400      1165   
3         89          510           63     12960        5450    450       875   
4         44          249          869      7560        4120    800      1500   

   PhD  Terminal  S.F.Ratio  perc.alumni  Expend  Grad.Rate  
0   70        78       18.1           12    7041         60  
1   29        30       12.2           16   10527         56  
2   53        66       12.9           30    8735         54  
3   92        97        7.7           37   19016         59  
4   76        72       11.9            2   10922         15  
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;Unnamed: 0&#39;</span><span class="p">:</span><span class="s1">&#39;college&#39;</span><span class="p">},</span> 
                 <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> 
<span class="n">df</span><span class="o">.</span><span class="n">columns</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;college&#39;, &#39;Private&#39;, &#39;Apps&#39;, &#39;Accept&#39;, &#39;Enroll&#39;, &#39;Top10perc&#39;,
       &#39;Top25perc&#39;, &#39;F.Undergrad&#39;, &#39;P.Undergrad&#39;, &#39;Outstate&#39;, &#39;Room.Board&#39;,
       &#39;Books&#39;, &#39;Personal&#39;, &#39;PhD&#39;, &#39;Terminal&#39;, &#39;S.F.Ratio&#39;, &#39;perc.alumni&#39;,
       &#39;Expend&#39;, &#39;Grad.Rate&#39;],
      dtype=&#39;object&#39;)</pre>
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
 

