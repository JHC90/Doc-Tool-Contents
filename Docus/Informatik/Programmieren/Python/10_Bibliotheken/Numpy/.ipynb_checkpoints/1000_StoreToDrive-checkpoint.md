'''''

{
"title": "Numpy - Read /Write to file",
"keywords": "Numpy, ",
"categories": "",
"description": "Hier geht es um die individuelle Abarbeitung der <em>EDA</em>-Checkliste im Kontext der California-Housing Problematik",
"level": "30",
"pageID": "19112020-NumpyReadWrite"
}
'''''
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Einlesen des Numpy Arrays von einer csv</span>
<span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">genfromtxt</span>
<span class="n">my_data</span> <span class="o">=</span> <span class="n">genfromtxt</span><span class="p">(</span><span class="s1">&#39;./Data/housing.csv&#39;</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;;&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_data</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">my_data</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_data</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(20640, 9)
&lt;class &#39;numpy.ndarray&#39;&gt;
[[-1.2223e+02  3.7880e+01  4.1000e+01 ...  1.2600e+02  8.3252e+01
   4.5260e+05]
 [-1.2222e+02  3.7860e+01  2.1000e+01 ...  1.1380e+03  8.3014e+01
   3.5850e+05]
 [-1.2224e+02  3.7850e+01  5.2000e+01 ...  1.7700e+02  7.2574e+01
   3.5210e+05]
 ...
 [-1.2122e+02  3.9430e+01  1.7000e+01 ...  4.3300e+02         nan
   9.2300e+04]
 [-1.2132e+02  3.9430e+01  1.8000e+01 ...  3.4900e+02  1.8672e+01
   8.4700e+04]
 [-1.2124e+02  3.9370e+01  1.6000e+01 ...  5.3000e+02  2.3886e+01
   8.9400e+04]]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">np</span><span class="o">.</span><span class="n">savetxt</span><span class="p">(</span><span class="s2">&quot;./Data/SavedFileFromNumpy.csv&quot;</span><span class="p">,</span> <span class="n">my_data</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s2">&quot;;&quot;</span><span class="p">)</span>
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
 

