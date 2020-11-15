'''''

{
"title": "ML-Notebook",
"keywords": "Basic-Notebook",
"categories": "Jupyter-Notebook",
"description": "Hier die individuelle Beschreibung der Index-Seite aus dem Frontmatter",
"level": "00",
"pageID": "07112020200718JupyterML"
}
'''''
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Chapter 1 – The Machine Learning landscape</strong></p>

</div>
</div>
</div>
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
<p><a href="https://www.google.de/">TestLink-Google</a><br>
<a href="...../Docus/DataScience/Theorie/000_AI_ML_DL.md">TestLink-Internal zu Hardlink</a><br>
<a href="07112020200718-001">TestLink-Internal zu ID</a><br></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Setup">Setup<a class="anchor-link" href="#Setup">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>First, let's make sure this notebook works well in both python 2 and 3, import a few common modules, ensure MatplotLib plots figure123s inline and prepare a function to save the figure123s:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># To support both python 2 and python 3</span>
<span class="kn">from</span> <span class="nn">__future__</span> <span class="kn">import</span> <span class="n">division</span><span class="p">,</span> <span class="n">print_function</span><span class="p">,</span> <span class="n">unicode_literals</span>

<span class="c1"># Common imports</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">os</span>

<span class="c1"># to make this notebook&#39;s output stable across runs</span>
<span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>

<span class="c1"># To plot pretty figure123s</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">matplotlib</span> <span class="k">as</span> <span class="nn">mpl</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">mpl</span><span class="o">.</span><span class="n">rc</span><span class="p">(</span><span class="s1">&#39;axes&#39;</span><span class="p">,</span> <span class="n">labelsize</span><span class="o">=</span><span class="mi">14</span><span class="p">)</span>
<span class="n">mpl</span><span class="o">.</span><span class="n">rc</span><span class="p">(</span><span class="s1">&#39;xtick&#39;</span><span class="p">,</span> <span class="n">labelsize</span><span class="o">=</span><span class="mi">12</span><span class="p">)</span>
<span class="n">mpl</span><span class="o">.</span><span class="n">rc</span><span class="p">(</span><span class="s1">&#39;ytick&#39;</span><span class="p">,</span> <span class="n">labelsize</span><span class="o">=</span><span class="mi">12</span><span class="p">)</span>

<span class="c1"># Where to save the figure123s</span>
<span class="n">PROJECT_ROOT_DIR</span> <span class="o">=</span> <span class="s2">&quot;.&quot;</span>
<span class="n">CHAPTER_ID</span> <span class="o">=</span> <span class="s2">&quot;fundamentals&quot;</span>

<span class="k">def</span> <span class="nf">save_fig</span><span class="p">(</span><span class="n">fig_id</span><span class="p">,</span> <span class="n">tight_layout</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
    <span class="n">path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_ROOT_DIR</span><span class="p">,</span> <span class="s2">&quot;images&quot;</span><span class="p">,</span> <span class="n">CHAPTER_ID</span><span class="p">,</span> <span class="n">fig_id</span> <span class="o">+</span> <span class="s2">&quot;.png&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Saving figure123&quot;</span><span class="p">,</span> <span class="n">fig_id</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">tight_layout</span><span class="p">:</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s1">&#39;png&#39;</span><span class="p">,</span> <span class="n">dpi</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>

<span class="c1"># Ignore useless warnings (see SciPy issue #5998)</span>
<span class="kn">import</span> <span class="nn">warnings</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="n">action</span><span class="o">=</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span> <span class="n">message</span><span class="o">=</span><span class="s2">&quot;^internal gelsd&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Code-example-1-1">Code example 1-1<a class="anchor-link" href="#Code-example-1-1">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This function just merges the OECD's life satisfaction data and the IMF's GDP per capita data. It's a bit too long and boring and it's not specific to Machine Learning, which is why I left it out of the book.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">prepare_country_stats</span><span class="p">(</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span><span class="p">):</span>
    <span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="p">[</span><span class="n">oecd_bli</span><span class="p">[</span><span class="s2">&quot;INEQUALITY&quot;</span><span class="p">]</span><span class="o">==</span><span class="s2">&quot;TOT&quot;</span><span class="p">]</span>
    <span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="o">.</span><span class="n">pivot</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="s2">&quot;Indicator&quot;</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="s2">&quot;Value&quot;</span><span class="p">)</span>
    <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;2015&quot;</span><span class="p">:</span> <span class="s2">&quot;GDP per capita&quot;</span><span class="p">},</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">full_country_stats</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">left</span><span class="o">=</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">right</span><span class="o">=</span><span class="n">gdp_per_capita</span><span class="p">,</span>
                                  <span class="n">left_index</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">right_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">full_country_stats</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">remove_indices</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span> <span class="mi">35</span><span class="p">]</span>
    <span class="n">keep_indices</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">36</span><span class="p">))</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">remove_indices</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">keep_indices</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The code in the book expects the data files to be located in the current directory. I just tweaked it here to fetch the files in datasets/lifesat.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="n">datapath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;lifesat&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Code example</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">sklearn.linear_model</span>

<span class="c1"># Load the data</span>
<span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span> <span class="o">+</span> <span class="s2">&quot;oecd_bli_2015.csv&quot;</span><span class="p">,</span> <span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="n">gdp_per_capita</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span> <span class="o">+</span> <span class="s2">&quot;gdp_per_capita.csv&quot;</span><span class="p">,</span><span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">,</span>
                             <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;latin1&#39;</span><span class="p">,</span> <span class="n">na_values</span><span class="o">=</span><span class="s2">&quot;n/a&quot;</span><span class="p">)</span>

<span class="c1"># Prepare the data</span>
<span class="n">country_stats</span> <span class="o">=</span> <span class="n">prepare_country_stats</span><span class="p">(</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span><span class="p">)</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>

<span class="c1"># Visualize the data</span>
<span class="n">country_stats</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1"># Select a linear model</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">sklearn</span><span class="o">.</span><span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="268.003125pt" version="1.1" viewBox="0 0 392.833125 268.003125" width="392.833125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 268.003125 

L 392.833125 268.003125 

L 392.833125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 50.833125 224.64 

L 385.633125 224.64 

L 385.633125 7.2 

L 50.833125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_1">

    <defs>

     <path d="M 0 2.236068 

C 0.593012 2.236068 1.161816 2.000462 1.581139 1.581139 

C 2.000462 1.161816 2.236068 0.593012 2.236068 0 

C 2.236068 -0.593012 2.000462 -1.161816 1.581139 -1.581139 

C 1.161816 -2.000462 0.593012 -2.236068 0 -2.236068 

C -0.593012 -2.236068 -1.161816 -2.000462 -1.581139 -1.581139 

C -2.000462 -1.161816 -2.236068 -0.593012 -2.236068 0 

C -2.236068 0.593012 -2.000462 1.161816 -1.581139 1.581139 

C -1.161816 2.000462 -0.593012 2.236068 0 2.236068 

z

" id="ma804054740" style="stroke:#1f77b4;"/>

    </defs>

    <g clip-path="url(#p71ea043f46)">

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="66.051307" xlink:href="#ma804054740" y="126.901818"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="68.541266" xlink:href="#ma804054740" y="156.186667"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="86.786838" xlink:href="#ma804054740" y="207.435152"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="88.449858" xlink:href="#ma804054740" y="141.544242"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="111.212874" xlink:href="#ma804054740" y="119.580606"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="119.652627" xlink:href="#ma804054740" y="156.186667"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="124.706041" xlink:href="#ma804054740" y="214.756364"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="131.589525" xlink:href="#ma804054740" y="192.792727"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="142.077082" xlink:href="#ma804054740" y="148.865455"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="175.490071" xlink:href="#ma804054740" y="90.295758"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="184.152018" xlink:href="#ma804054740" y="141.544242"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="201.543828" xlink:href="#ma804054740" y="126.901818"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="218.594362" xlink:href="#ma804054740" y="134.22303"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="237.199758" xlink:href="#ma804054740" y="24.404848"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="248.277581" xlink:href="#ma804054740" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="252.379889" xlink:href="#ma804054740" y="90.295758"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="268.210776" xlink:href="#ma804054740" y="61.010909"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="274.004255" xlink:href="#ma804054740" y="53.689697"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="280.368032" xlink:href="#ma804054740" y="24.404848"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="289.208996" xlink:href="#ma804054740" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="290.97432" xlink:href="#ma804054740" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="291.761533" xlink:href="#ma804054740" y="61.010909"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="292.065289" xlink:href="#ma804054740" y="68.332121"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="331.750012" xlink:href="#ma804054740" y="39.047273"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="338.184362" xlink:href="#ma804054740" y="17.083636"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="338.882812" xlink:href="#ma804054740" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="341.414575" xlink:href="#ma804054740" y="53.689697"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="346.38476" xlink:href="#ma804054740" y="17.083636"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="370.414943" xlink:href="#ma804054740" y="39.047273"/>

    </g>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mb2bc2b6b15" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="72.204206" xlink:href="#mb2bc2b6b15" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 10000 -->

      <defs>

       <path d="M 12.40625 8.296875 

L 28.515625 8.296875 

L 28.515625 63.921875 

L 10.984375 60.40625 

L 10.984375 69.390625 

L 28.421875 72.90625 

L 38.28125 72.90625 

L 38.28125 8.296875 

L 54.390625 8.296875 

L 54.390625 0 

L 12.40625 0 

z

" id="DejaVuSans-49"/>

       <path d="M 31.78125 66.40625 

Q 24.171875 66.40625 20.328125 58.90625 

Q 16.5 51.421875 16.5 36.375 

Q 16.5 21.390625 20.328125 13.890625 

Q 24.171875 6.390625 31.78125 6.390625 

Q 39.453125 6.390625 43.28125 13.890625 

Q 47.125 21.390625 47.125 36.375 

Q 47.125 51.421875 43.28125 58.90625 

Q 39.453125 66.40625 31.78125 66.40625 

z

M 31.78125 74.21875 

Q 44.046875 74.21875 50.515625 64.515625 

Q 56.984375 54.828125 56.984375 36.375 

Q 56.984375 17.96875 50.515625 8.265625 

Q 44.046875 -1.421875 31.78125 -1.421875 

Q 19.53125 -1.421875 13.0625 8.265625 

Q 6.59375 17.96875 6.59375 36.375 

Q 6.59375 54.828125 13.0625 64.515625 

Q 19.53125 74.21875 31.78125 74.21875 

z

" id="DejaVuSans-48"/>

      </defs>

      <g transform="translate(53.116706 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="137.308323" xlink:href="#mb2bc2b6b15" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 20000 -->

      <defs>

       <path d="M 19.1875 8.296875 

L 53.609375 8.296875 

L 53.609375 0 

L 7.328125 0 

L 7.328125 8.296875 

Q 12.9375 14.109375 22.625 23.890625 

Q 32.328125 33.6875 34.8125 36.53125 

Q 39.546875 41.84375 41.421875 45.53125 

Q 43.3125 49.21875 43.3125 52.78125 

Q 43.3125 58.59375 39.234375 62.25 

Q 35.15625 65.921875 28.609375 65.921875 

Q 23.96875 65.921875 18.8125 64.3125 

Q 13.671875 62.703125 7.8125 59.421875 

L 7.8125 69.390625 

Q 13.765625 71.78125 18.9375 73 

Q 24.125 74.21875 28.421875 74.21875 

Q 39.75 74.21875 46.484375 68.546875 

Q 53.21875 62.890625 53.21875 53.421875 

Q 53.21875 48.921875 51.53125 44.890625 

Q 49.859375 40.875 45.40625 35.40625 

Q 44.1875 33.984375 37.640625 27.21875 

Q 31.109375 20.453125 19.1875 8.296875 

z

" id="DejaVuSans-50"/>

      </defs>

      <g transform="translate(118.220823 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="202.41244" xlink:href="#mb2bc2b6b15" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 30000 -->

      <defs>

       <path d="M 40.578125 39.3125 

Q 47.65625 37.796875 51.625 33 

Q 55.609375 28.21875 55.609375 21.1875 

Q 55.609375 10.40625 48.1875 4.484375 

Q 40.765625 -1.421875 27.09375 -1.421875 

Q 22.515625 -1.421875 17.65625 -0.515625 

Q 12.796875 0.390625 7.625 2.203125 

L 7.625 11.71875 

Q 11.71875 9.328125 16.59375 8.109375 

Q 21.484375 6.890625 26.8125 6.890625 

Q 36.078125 6.890625 40.9375 10.546875 

Q 45.796875 14.203125 45.796875 21.1875 

Q 45.796875 27.640625 41.28125 31.265625 

Q 36.765625 34.90625 28.71875 34.90625 

L 20.21875 34.90625 

L 20.21875 43.015625 

L 29.109375 43.015625 

Q 36.375 43.015625 40.234375 45.921875 

Q 44.09375 48.828125 44.09375 54.296875 

Q 44.09375 59.90625 40.109375 62.90625 

Q 36.140625 65.921875 28.71875 65.921875 

Q 24.65625 65.921875 20.015625 65.03125 

Q 15.375 64.15625 9.8125 62.3125 

L 9.8125 71.09375 

Q 15.4375 72.65625 20.34375 73.4375 

Q 25.25 74.21875 29.59375 74.21875 

Q 40.828125 74.21875 47.359375 69.109375 

Q 53.90625 64.015625 53.90625 55.328125 

Q 53.90625 49.265625 50.4375 45.09375 

Q 46.96875 40.921875 40.578125 39.3125 

z

" id="DejaVuSans-51"/>

      </defs>

      <g transform="translate(183.32494 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="267.516558" xlink:href="#mb2bc2b6b15" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 40000 -->

      <defs>

       <path d="M 37.796875 64.3125 

L 12.890625 25.390625 

L 37.796875 25.390625 

z

M 35.203125 72.90625 

L 47.609375 72.90625 

L 47.609375 25.390625 

L 58.015625 25.390625 

L 58.015625 17.1875 

L 47.609375 17.1875 

L 47.609375 0 

L 37.796875 0 

L 37.796875 17.1875 

L 4.890625 17.1875 

L 4.890625 26.703125 

z

" id="DejaVuSans-52"/>

      </defs>

      <g transform="translate(248.429058 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="332.620675" xlink:href="#mb2bc2b6b15" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 50000 -->

      <defs>

       <path d="M 10.796875 72.90625 

L 49.515625 72.90625 

L 49.515625 64.59375 

L 19.828125 64.59375 

L 19.828125 46.734375 

Q 21.96875 47.46875 24.109375 47.828125 

Q 26.265625 48.1875 28.421875 48.1875 

Q 40.625 48.1875 47.75 41.5 

Q 54.890625 34.8125 54.890625 23.390625 

Q 54.890625 11.625 47.5625 5.09375 

Q 40.234375 -1.421875 26.90625 -1.421875 

Q 22.3125 -1.421875 17.546875 -0.640625 

Q 12.796875 0.140625 7.71875 1.703125 

L 7.71875 11.625 

Q 12.109375 9.234375 16.796875 8.0625 

Q 21.484375 6.890625 26.703125 6.890625 

Q 35.15625 6.890625 40.078125 11.328125 

Q 45.015625 15.765625 45.015625 23.390625 

Q 45.015625 31 40.078125 35.4375 

Q 35.15625 39.890625 26.703125 39.890625 

Q 22.75 39.890625 18.8125 39.015625 

Q 14.890625 38.140625 10.796875 36.28125 

z

" id="DejaVuSans-53"/>

      </defs>

      <g transform="translate(313.533175 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="text_6">

     <!-- GDP per capita -->

     <defs>

      <path d="M 59.515625 10.40625 

L 59.515625 29.984375 

L 43.40625 29.984375 

L 43.40625 38.09375 

L 69.28125 38.09375 

L 69.28125 6.78125 

Q 63.578125 2.734375 56.6875 0.65625 

Q 49.8125 -1.421875 42 -1.421875 

Q 24.90625 -1.421875 15.25 8.5625 

Q 5.609375 18.5625 5.609375 36.375 

Q 5.609375 54.25 15.25 64.234375 

Q 24.90625 74.21875 42 74.21875 

Q 49.125 74.21875 55.546875 72.453125 

Q 61.96875 70.703125 67.390625 67.28125 

L 67.390625 56.78125 

Q 61.921875 61.421875 55.765625 63.765625 

Q 49.609375 66.109375 42.828125 66.109375 

Q 29.4375 66.109375 22.71875 58.640625 

Q 16.015625 51.171875 16.015625 36.375 

Q 16.015625 21.625 22.71875 14.15625 

Q 29.4375 6.6875 42.828125 6.6875 

Q 48.046875 6.6875 52.140625 7.59375 

Q 56.25 8.5 59.515625 10.40625 

z

" id="DejaVuSans-71"/>

      <path d="M 19.671875 64.796875 

L 19.671875 8.109375 

L 31.59375 8.109375 

Q 46.6875 8.109375 53.6875 14.9375 

Q 60.6875 21.78125 60.6875 36.53125 

Q 60.6875 51.171875 53.6875 57.984375 

Q 46.6875 64.796875 31.59375 64.796875 

z

M 9.8125 72.90625 

L 30.078125 72.90625 

Q 51.265625 72.90625 61.171875 64.09375 

Q 71.09375 55.28125 71.09375 36.53125 

Q 71.09375 17.671875 61.125 8.828125 

Q 51.171875 0 30.078125 0 

L 9.8125 0 

z

" id="DejaVuSans-68"/>

      <path d="M 19.671875 64.796875 

L 19.671875 37.40625 

L 32.078125 37.40625 

Q 38.96875 37.40625 42.71875 40.96875 

Q 46.484375 44.53125 46.484375 51.125 

Q 46.484375 57.671875 42.71875 61.234375 

Q 38.96875 64.796875 32.078125 64.796875 

z

M 9.8125 72.90625 

L 32.078125 72.90625 

Q 44.34375 72.90625 50.609375 67.359375 

Q 56.890625 61.8125 56.890625 51.125 

Q 56.890625 40.328125 50.609375 34.8125 

Q 44.34375 29.296875 32.078125 29.296875 

L 19.671875 29.296875 

L 19.671875 0 

L 9.8125 0 

z

" id="DejaVuSans-80"/>

      <path id="DejaVuSans-32"/>

      <path d="M 18.109375 8.203125 

L 18.109375 -20.796875 

L 9.078125 -20.796875 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.390625 

Q 20.953125 51.265625 25.265625 53.625 

Q 29.59375 56 35.59375 56 

Q 45.5625 56 51.78125 48.09375 

Q 58.015625 40.1875 58.015625 27.296875 

Q 58.015625 14.40625 51.78125 6.484375 

Q 45.5625 -1.421875 35.59375 -1.421875 

Q 29.59375 -1.421875 25.265625 0.953125 

Q 20.953125 3.328125 18.109375 8.203125 

z

M 48.6875 27.296875 

Q 48.6875 37.203125 44.609375 42.84375 

Q 40.53125 48.484375 33.40625 48.484375 

Q 26.265625 48.484375 22.1875 42.84375 

Q 18.109375 37.203125 18.109375 27.296875 

Q 18.109375 17.390625 22.1875 11.75 

Q 26.265625 6.109375 33.40625 6.109375 

Q 40.53125 6.109375 44.609375 11.75 

Q 48.6875 17.390625 48.6875 27.296875 

z

" id="DejaVuSans-112"/>

      <path d="M 56.203125 29.59375 

L 56.203125 25.203125 

L 14.890625 25.203125 

Q 15.484375 15.921875 20.484375 11.0625 

Q 25.484375 6.203125 34.421875 6.203125 

Q 39.59375 6.203125 44.453125 7.46875 

Q 49.3125 8.734375 54.109375 11.28125 

L 54.109375 2.78125 

Q 49.265625 0.734375 44.1875 -0.34375 

Q 39.109375 -1.421875 33.890625 -1.421875 

Q 20.796875 -1.421875 13.15625 6.1875 

Q 5.515625 13.8125 5.515625 26.8125 

Q 5.515625 40.234375 12.765625 48.109375 

Q 20.015625 56 32.328125 56 

Q 43.359375 56 49.78125 48.890625 

Q 56.203125 41.796875 56.203125 29.59375 

z

M 47.21875 32.234375 

Q 47.125 39.59375 43.09375 43.984375 

Q 39.0625 48.390625 32.421875 48.390625 

Q 24.90625 48.390625 20.390625 44.140625 

Q 15.875 39.890625 15.1875 32.171875 

z

" id="DejaVuSans-101"/>

      <path d="M 41.109375 46.296875 

Q 39.59375 47.171875 37.8125 47.578125 

Q 36.03125 48 33.890625 48 

Q 26.265625 48 22.1875 43.046875 

Q 18.109375 38.09375 18.109375 28.8125 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 20.953125 51.171875 25.484375 53.578125 

Q 30.03125 56 36.53125 56 

Q 37.453125 56 38.578125 55.875 

Q 39.703125 55.765625 41.0625 55.515625 

z

" id="DejaVuSans-114"/>

      <path d="M 48.78125 52.59375 

L 48.78125 44.1875 

Q 44.96875 46.296875 41.140625 47.34375 

Q 37.3125 48.390625 33.40625 48.390625 

Q 24.65625 48.390625 19.8125 42.84375 

Q 14.984375 37.3125 14.984375 27.296875 

Q 14.984375 17.28125 19.8125 11.734375 

Q 24.65625 6.203125 33.40625 6.203125 

Q 37.3125 6.203125 41.140625 7.25 

Q 44.96875 8.296875 48.78125 10.40625 

L 48.78125 2.09375 

Q 45.015625 0.34375 40.984375 -0.53125 

Q 36.96875 -1.421875 32.421875 -1.421875 

Q 20.0625 -1.421875 12.78125 6.34375 

Q 5.515625 14.109375 5.515625 27.296875 

Q 5.515625 40.671875 12.859375 48.328125 

Q 20.21875 56 33.015625 56 

Q 37.15625 56 41.109375 55.140625 

Q 45.0625 54.296875 48.78125 52.59375 

z

" id="DejaVuSans-99"/>

      <path d="M 34.28125 27.484375 

Q 23.390625 27.484375 19.1875 25 

Q 14.984375 22.515625 14.984375 16.5 

Q 14.984375 11.71875 18.140625 8.90625 

Q 21.296875 6.109375 26.703125 6.109375 

Q 34.1875 6.109375 38.703125 11.40625 

Q 43.21875 16.703125 43.21875 25.484375 

L 43.21875 27.484375 

z

M 52.203125 31.203125 

L 52.203125 0 

L 43.21875 0 

L 43.21875 8.296875 

Q 40.140625 3.328125 35.546875 0.953125 

Q 30.953125 -1.421875 24.3125 -1.421875 

Q 15.921875 -1.421875 10.953125 3.296875 

Q 6 8.015625 6 15.921875 

Q 6 25.140625 12.171875 29.828125 

Q 18.359375 34.515625 30.609375 34.515625 

L 43.21875 34.515625 

L 43.21875 35.40625 

Q 43.21875 41.609375 39.140625 45 

Q 35.0625 48.390625 27.6875 48.390625 

Q 23 48.390625 18.546875 47.265625 

Q 14.109375 46.140625 10.015625 43.890625 

L 10.015625 52.203125 

Q 14.9375 54.109375 19.578125 55.046875 

Q 24.21875 56 28.609375 56 

Q 40.484375 56 46.34375 49.84375 

Q 52.203125 43.703125 52.203125 31.203125 

z

" id="DejaVuSans-97"/>

      <path d="M 9.421875 54.6875 

L 18.40625 54.6875 

L 18.40625 0 

L 9.421875 0 

z

M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 64.59375 

L 9.421875 64.59375 

z

" id="DejaVuSans-105"/>

      <path d="M 18.3125 70.21875 

L 18.3125 54.6875 

L 36.8125 54.6875 

L 36.8125 47.703125 

L 18.3125 47.703125 

L 18.3125 18.015625 

Q 18.3125 11.328125 20.140625 9.421875 

Q 21.96875 7.515625 27.59375 7.515625 

L 36.8125 7.515625 

L 36.8125 0 

L 27.59375 0 

Q 17.1875 0 13.234375 3.875 

Q 9.28125 7.765625 9.28125 18.015625 

L 9.28125 47.703125 

L 2.6875 47.703125 

L 2.6875 54.6875 

L 9.28125 54.6875 

L 9.28125 70.21875 

z

" id="DejaVuSans-116"/>

     </defs>

     <g transform="translate(165.559219 257.891562)scale(0.14 -0.14)">

      <use xlink:href="#DejaVuSans-71"/>

      <use x="77.490234" xlink:href="#DejaVuSans-68"/>

      <use x="154.492188" xlink:href="#DejaVuSans-80"/>

      <use x="214.794922" xlink:href="#DejaVuSans-32"/>

      <use x="246.582031" xlink:href="#DejaVuSans-112"/>

      <use x="310.058594" xlink:href="#DejaVuSans-101"/>

      <use x="371.582031" xlink:href="#DejaVuSans-114"/>

      <use x="412.695312" xlink:href="#DejaVuSans-32"/>

      <use x="444.482422" xlink:href="#DejaVuSans-99"/>

      <use x="499.462891" xlink:href="#DejaVuSans-97"/>

      <use x="560.742188" xlink:href="#DejaVuSans-112"/>

      <use x="624.21875" xlink:href="#DejaVuSans-105"/>

      <use x="652.001953" xlink:href="#DejaVuSans-116"/>

      <use x="691.210938" xlink:href="#DejaVuSans-97"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_6">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="me7a3b7ebcd" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="200.113939"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 5.0 -->

      <defs>

       <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

      </defs>

      <g transform="translate(24.749375 204.673002)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="163.507879"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 5.5 -->

      <g transform="translate(24.749375 168.066941)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="126.901818"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 6.0 -->

      <defs>

       <path d="M 33.015625 40.375 

Q 26.375 40.375 22.484375 35.828125 

Q 18.609375 31.296875 18.609375 23.390625 

Q 18.609375 15.53125 22.484375 10.953125 

Q 26.375 6.390625 33.015625 6.390625 

Q 39.65625 6.390625 43.53125 10.953125 

Q 47.40625 15.53125 47.40625 23.390625 

Q 47.40625 31.296875 43.53125 35.828125 

Q 39.65625 40.375 33.015625 40.375 

z

M 52.59375 71.296875 

L 52.59375 62.3125 

Q 48.875 64.0625 45.09375 64.984375 

Q 41.3125 65.921875 37.59375 65.921875 

Q 27.828125 65.921875 22.671875 59.328125 

Q 17.53125 52.734375 16.796875 39.40625 

Q 19.671875 43.65625 24.015625 45.921875 

Q 28.375 48.1875 33.59375 48.1875 

Q 44.578125 48.1875 50.953125 41.515625 

Q 57.328125 34.859375 57.328125 23.390625 

Q 57.328125 12.15625 50.6875 5.359375 

Q 44.046875 -1.421875 33.015625 -1.421875 

Q 20.359375 -1.421875 13.671875 8.265625 

Q 6.984375 17.96875 6.984375 36.375 

Q 6.984375 53.65625 15.1875 63.9375 

Q 23.390625 74.21875 37.203125 74.21875 

Q 40.921875 74.21875 44.703125 73.484375 

Q 48.484375 72.75 52.59375 71.296875 

z

" id="DejaVuSans-54"/>

      </defs>

      <g transform="translate(24.749375 131.460881)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="90.295758"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 6.5 -->

      <g transform="translate(24.749375 94.85482)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="53.689697"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 7.0 -->

      <defs>

       <path d="M 8.203125 72.90625 

L 55.078125 72.90625 

L 55.078125 68.703125 

L 28.609375 0 

L 18.3125 0 

L 43.21875 64.59375 

L 8.203125 64.59375 

z

" id="DejaVuSans-55"/>

      </defs>

      <g transform="translate(24.749375 58.248759)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#me7a3b7ebcd" y="17.083636"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 7.5 -->

      <g transform="translate(24.749375 21.642699)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_13">

     <!-- Life satisfaction -->

     <defs>

      <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

      <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

      <path d="M 44.28125 53.078125 

L 44.28125 44.578125 

Q 40.484375 46.53125 36.375 47.5 

Q 32.28125 48.484375 27.875 48.484375 

Q 21.1875 48.484375 17.84375 46.4375 

Q 14.5 44.390625 14.5 40.28125 

Q 14.5 37.15625 16.890625 35.375 

Q 19.28125 33.59375 26.515625 31.984375 

L 29.59375 31.296875 

Q 39.15625 29.25 43.1875 25.515625 

Q 47.21875 21.78125 47.21875 15.09375 

Q 47.21875 7.46875 41.1875 3.015625 

Q 35.15625 -1.421875 24.609375 -1.421875 

Q 20.21875 -1.421875 15.453125 -0.5625 

Q 10.6875 0.296875 5.421875 2 

L 5.421875 11.28125 

Q 10.40625 8.6875 15.234375 7.390625 

Q 20.0625 6.109375 24.8125 6.109375 

Q 31.15625 6.109375 34.5625 8.28125 

Q 37.984375 10.453125 37.984375 14.40625 

Q 37.984375 18.0625 35.515625 20.015625 

Q 33.0625 21.96875 24.703125 23.78125 

L 21.578125 24.515625 

Q 13.234375 26.265625 9.515625 29.90625 

Q 5.8125 33.546875 5.8125 39.890625 

Q 5.8125 47.609375 11.28125 51.796875 

Q 16.75 56 26.8125 56 

Q 31.78125 56 36.171875 55.265625 

Q 40.578125 54.546875 44.28125 53.078125 

z

" id="DejaVuSans-115"/>

      <path d="M 30.609375 48.390625 

Q 23.390625 48.390625 19.1875 42.75 

Q 14.984375 37.109375 14.984375 27.296875 

Q 14.984375 17.484375 19.15625 11.84375 

Q 23.34375 6.203125 30.609375 6.203125 

Q 37.796875 6.203125 41.984375 11.859375 

Q 46.1875 17.53125 46.1875 27.296875 

Q 46.1875 37.015625 41.984375 42.703125 

Q 37.796875 48.390625 30.609375 48.390625 

z

M 30.609375 56 

Q 42.328125 56 49.015625 48.375 

Q 55.71875 40.765625 55.71875 27.296875 

Q 55.71875 13.875 49.015625 6.21875 

Q 42.328125 -1.421875 30.609375 -1.421875 

Q 18.84375 -1.421875 12.171875 6.21875 

Q 5.515625 13.875 5.515625 27.296875 

Q 5.515625 40.765625 12.171875 48.375 

Q 18.84375 56 30.609375 56 

z

" id="DejaVuSans-111"/>

      <path d="M 54.890625 33.015625 

L 54.890625 0 

L 45.90625 0 

L 45.90625 32.71875 

Q 45.90625 40.484375 42.875 44.328125 

Q 39.84375 48.1875 33.796875 48.1875 

Q 26.515625 48.1875 22.3125 43.546875 

Q 18.109375 38.921875 18.109375 30.90625 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-110"/>

     </defs>

     <g transform="translate(17.837812 171.043906)rotate(-90)scale(0.14 -0.14)">

      <use xlink:href="#DejaVuSans-76"/>

      <use x="55.712891" xlink:href="#DejaVuSans-105"/>

      <use x="83.496094" xlink:href="#DejaVuSans-102"/>

      <use x="118.701172" xlink:href="#DejaVuSans-101"/>

      <use x="180.224609" xlink:href="#DejaVuSans-32"/>

      <use x="212.011719" xlink:href="#DejaVuSans-115"/>

      <use x="264.111328" xlink:href="#DejaVuSans-97"/>

      <use x="325.390625" xlink:href="#DejaVuSans-116"/>

      <use x="364.599609" xlink:href="#DejaVuSans-105"/>

      <use x="392.382812" xlink:href="#DejaVuSans-115"/>

      <use x="444.482422" xlink:href="#DejaVuSans-102"/>

      <use x="479.6875" xlink:href="#DejaVuSans-97"/>

      <use x="540.966797" xlink:href="#DejaVuSans-99"/>

      <use x="595.947266" xlink:href="#DejaVuSans-116"/>

      <use x="635.15625" xlink:href="#DejaVuSans-105"/>

      <use x="662.939453" xlink:href="#DejaVuSans-111"/>

      <use x="724.121094" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="patch_3">

    <path d="M 50.833125 224.64 

L 50.833125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 385.633125 224.64 

L 385.633125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 50.833125 224.64 

L 385.633125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 50.833125 7.2 

L 385.633125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p71ea043f46">

   <rect height="217.44" width="334.8" x="50.833125" y="7.2"/>

  </clipPath>

 </defs>

</svg>


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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Train the model</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LinearRegression()</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Make a prediction for Cyprus</span>
<span class="n">X_new</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">22587</span><span class="p">]]</span>  <span class="c1"># Cyprus&#39; GDP per capita</span>
<span class="nb">print</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_new</span><span class="p">))</span> <span class="c1"># outputs [[ 5.96242338]]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[5.96242338]]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Note:-you-can-ignore-the-rest-of-this-notebook,-it-just-generates-many-of-the-figure123s-in-chapter-1.">Note: you can ignore the rest of this notebook, it just generates many of the figure123s in chapter 1.<a class="anchor-link" href="#Note:-you-can-ignore-the-rest-of-this-notebook,-it-just-generates-many-of-the-figure123s-in-chapter-1.">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Load-and-prepare-Life-satisfaction-data">Load and prepare Life satisfaction data<a class="anchor-link" href="#Load-and-prepare-Life-satisfaction-data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you want, you can get fresh data from the OECD's website.
Download the CSV from <a href="http://stats.oecd.org/index.aspx?DataSetCode=BLI">http://stats.oecd.org/index.aspx?DataSetCode=BLI</a>
and save it to <code>datasets/lifesat/</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span> <span class="o">+</span> <span class="s2">&quot;oecd_bli_2015.csv&quot;</span><span class="p">,</span> <span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="p">[</span><span class="n">oecd_bli</span><span class="p">[</span><span class="s2">&quot;INEQUALITY&quot;</span><span class="p">]</span><span class="o">==</span><span class="s2">&quot;TOT&quot;</span><span class="p">]</span>
<span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="o">.</span><span class="n">pivot</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="s2">&quot;Indicator&quot;</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="s2">&quot;Value&quot;</span><span class="p">)</span>
<span class="n">oecd_bli</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>



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
      <th>Indicator</th>
      <th>Air pollution</th>
      <th>Assault rate</th>
      <th>Consultation on rule-making</th>
      <th>Dwellings without basic facilities</th>
      <th>Educational attainment</th>
      <th>Employees working very long hours</th>
      <th>Employment rate</th>
      <th>Homicide rate</th>
      <th>Household net adjusted disposable income</th>
      <th>Household net financial wealth</th>
      <th>...</th>
      <th>Long-term unemployment rate</th>
      <th>Personal earnings</th>
      <th>Quality of support network</th>
      <th>Rooms per person</th>
      <th>Self-reported health</th>
      <th>Student skills</th>
      <th>Time devoted to leisure and personal care</th>
      <th>Voter turnout</th>
      <th>Water quality</th>
      <th>Years in education</th>
    </tr>
    <tr>
      <th>Country</th>
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
      <th>Australia</th>
      <td>13.0</td>
      <td>2.1</td>
      <td>10.5</td>
      <td>1.1</td>
      <td>76.0</td>
      <td>14.02</td>
      <td>72.0</td>
      <td>0.8</td>
      <td>31588.0</td>
      <td>47657.0</td>
      <td>...</td>
      <td>1.08</td>
      <td>50449.0</td>
      <td>92.0</td>
      <td>2.3</td>
      <td>85.0</td>
      <td>512.0</td>
      <td>14.41</td>
      <td>93.0</td>
      <td>91.0</td>
      <td>19.4</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>27.0</td>
      <td>3.4</td>
      <td>7.1</td>
      <td>1.0</td>
      <td>83.0</td>
      <td>7.61</td>
      <td>72.0</td>
      <td>0.4</td>
      <td>31173.0</td>
      <td>49887.0</td>
      <td>...</td>
      <td>1.19</td>
      <td>45199.0</td>
      <td>89.0</td>
      <td>1.6</td>
      <td>69.0</td>
      <td>500.0</td>
      <td>14.46</td>
      <td>75.0</td>
      <td>94.0</td>
      <td>17.0</td>
    </tr>
  </tbody123>
</table>
<p>2 rows × 24 columns</p>
</div>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">oecd_bli</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Country
Australia    7.3
Austria      6.9
Belgium      6.9
Brazil       7.0
Canada       7.3
Name: Life satisfaction, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Load-and-prepare-GDP-per-capita-data">Load and prepare GDP per capita data<a class="anchor-link" href="#Load-and-prepare-GDP-per-capita-data">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Just like above, you can update the GDP per capita data if you want. Just download data from <a href="http://goo.gl/j1MSKe">http://goo.gl/j1MSKe</a> (=&gt; imf.org) and save it to <code>datasets/lifesat/</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">gdp_per_capita</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span><span class="o">+</span><span class="s2">&quot;gdp_per_capita.csv&quot;</span><span class="p">,</span> <span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">,</span>
                             <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;latin1&#39;</span><span class="p">,</span> <span class="n">na_values</span><span class="o">=</span><span class="s2">&quot;n/a&quot;</span><span class="p">)</span>
<span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;2015&quot;</span><span class="p">:</span> <span class="s2">&quot;GDP per capita&quot;</span><span class="p">},</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">head123</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
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
      <th>Subject Descriptor</th>
      <th>Units</th>
      <th>Scale</th>
      <th>Country/Series-specific Notes</th>
      <th>GDP per capita</th>
      <th>Estimates Start After</th>
    </tr>
    <tr>
      <th>Country</th>
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
      <th>Afghanistan</th>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>599.994</td>
      <td>2013.0</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>3995.383</td>
      <td>2010.0</td>
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
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">left</span><span class="o">=</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">right</span><span class="o">=</span><span class="n">gdp_per_capita</span><span class="p">,</span> <span class="n">left_index</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">right_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">full_country_stats</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">full_country_stats</span>
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
      <th>Air pollution</th>
      <th>Assault rate</th>
      <th>Consultation on rule-making</th>
      <th>Dwellings without basic facilities</th>
      <th>Educational attainment</th>
      <th>Employees working very long hours</th>
      <th>Employment rate</th>
      <th>Homicide rate</th>
      <th>Household net adjusted disposable income</th>
      <th>Household net financial wealth</th>
      <th>...</th>
      <th>Time devoted to leisure and personal care</th>
      <th>Voter turnout</th>
      <th>Water quality</th>
      <th>Years in education</th>
      <th>Subject Descriptor</th>
      <th>Units</th>
      <th>Scale</th>
      <th>Country/Series-specific Notes</th>
      <th>GDP per capita</th>
      <th>Estimates Start After</th>
    </tr>
    <tr>
      <th>Country</th>
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
      <th>Brazil</th>
      <td>18.0</td>
      <td>7.9</td>
      <td>4.0</td>
      <td>6.7</td>
      <td>45.0</td>
      <td>10.41</td>
      <td>67.0</td>
      <td>25.5</td>
      <td>11664.0</td>
      <td>6844.0</td>
      <td>...</td>
      <td>14.97</td>
      <td>79.0</td>
      <td>72.0</td>
      <td>16.3</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>8669.998</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Mexico</th>
      <td>30.0</td>
      <td>12.8</td>
      <td>9.0</td>
      <td>4.2</td>
      <td>37.0</td>
      <td>28.83</td>
      <td>61.0</td>
      <td>23.4</td>
      <td>13085.0</td>
      <td>9056.0</td>
      <td>...</td>
      <td>13.89</td>
      <td>63.0</td>
      <td>67.0</td>
      <td>14.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>9009.280</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Russia</th>
      <td>15.0</td>
      <td>3.8</td>
      <td>2.5</td>
      <td>15.1</td>
      <td>94.0</td>
      <td>0.16</td>
      <td>69.0</td>
      <td>12.8</td>
      <td>19292.0</td>
      <td>3412.0</td>
      <td>...</td>
      <td>14.97</td>
      <td>65.0</td>
      <td>56.0</td>
      <td>16.0</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>9054.914</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Turkey</th>
      <td>35.0</td>
      <td>5.0</td>
      <td>5.5</td>
      <td>12.7</td>
      <td>34.0</td>
      <td>40.86</td>
      <td>50.0</td>
      <td>1.2</td>
      <td>14095.0</td>
      <td>3251.0</td>
      <td>...</td>
      <td>13.42</td>
      <td>88.0</td>
      <td>62.0</td>
      <td>16.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>9437.372</td>
      <td>2013.0</td>
    </tr>
    <tr>
      <th>Hungary</th>
      <td>15.0</td>
      <td>3.6</td>
      <td>7.9</td>
      <td>4.8</td>
      <td>82.0</td>
      <td>3.19</td>
      <td>58.0</td>
      <td>1.3</td>
      <td>15442.0</td>
      <td>13277.0</td>
      <td>...</td>
      <td>15.04</td>
      <td>62.0</td>
      <td>77.0</td>
      <td>17.6</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>12239.894</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Poland</th>
      <td>33.0</td>
      <td>1.4</td>
      <td>10.8</td>
      <td>3.2</td>
      <td>90.0</td>
      <td>7.41</td>
      <td>60.0</td>
      <td>0.9</td>
      <td>17852.0</td>
      <td>10919.0</td>
      <td>...</td>
      <td>14.20</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>18.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>12495.334</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Chile</th>
      <td>46.0</td>
      <td>6.9</td>
      <td>2.0</td>
      <td>9.4</td>
      <td>57.0</td>
      <td>15.42</td>
      <td>62.0</td>
      <td>4.4</td>
      <td>14533.0</td>
      <td>17733.0</td>
      <td>...</td>
      <td>14.41</td>
      <td>49.0</td>
      <td>73.0</td>
      <td>16.5</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>13340.905</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Slovak Republic</th>
      <td>13.0</td>
      <td>3.0</td>
      <td>6.6</td>
      <td>0.6</td>
      <td>92.0</td>
      <td>7.02</td>
      <td>60.0</td>
      <td>1.2</td>
      <td>17503.0</td>
      <td>8663.0</td>
      <td>...</td>
      <td>14.99</td>
      <td>59.0</td>
      <td>81.0</td>
      <td>16.3</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>15991.736</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Czech Republic</th>
      <td>16.0</td>
      <td>2.8</td>
      <td>6.8</td>
      <td>0.9</td>
      <td>92.0</td>
      <td>6.98</td>
      <td>68.0</td>
      <td>0.8</td>
      <td>18404.0</td>
      <td>17299.0</td>
      <td>...</td>
      <td>14.98</td>
      <td>59.0</td>
      <td>85.0</td>
      <td>18.1</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>17256.918</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Estonia</th>
      <td>9.0</td>
      <td>5.5</td>
      <td>3.3</td>
      <td>8.1</td>
      <td>90.0</td>
      <td>3.30</td>
      <td>68.0</td>
      <td>4.8</td>
      <td>15167.0</td>
      <td>7680.0</td>
      <td>...</td>
      <td>14.90</td>
      <td>64.0</td>
      <td>79.0</td>
      <td>17.5</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>17288.083</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Greece</th>
      <td>27.0</td>
      <td>3.7</td>
      <td>6.5</td>
      <td>0.7</td>
      <td>68.0</td>
      <td>6.16</td>
      <td>49.0</td>
      <td>1.6</td>
      <td>18575.0</td>
      <td>14579.0</td>
      <td>...</td>
      <td>14.91</td>
      <td>64.0</td>
      <td>69.0</td>
      <td>18.6</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>18064.288</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Portugal</th>
      <td>18.0</td>
      <td>5.7</td>
      <td>6.5</td>
      <td>0.9</td>
      <td>38.0</td>
      <td>9.62</td>
      <td>61.0</td>
      <td>1.1</td>
      <td>20086.0</td>
      <td>31245.0</td>
      <td>...</td>
      <td>14.95</td>
      <td>58.0</td>
      <td>86.0</td>
      <td>17.6</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>19121.592</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Slovenia</th>
      <td>26.0</td>
      <td>3.9</td>
      <td>10.3</td>
      <td>0.5</td>
      <td>85.0</td>
      <td>5.63</td>
      <td>63.0</td>
      <td>0.4</td>
      <td>19326.0</td>
      <td>18465.0</td>
      <td>...</td>
      <td>14.62</td>
      <td>52.0</td>
      <td>88.0</td>
      <td>18.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>20732.482</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>24.0</td>
      <td>4.2</td>
      <td>7.3</td>
      <td>0.1</td>
      <td>55.0</td>
      <td>5.89</td>
      <td>56.0</td>
      <td>0.6</td>
      <td>22477.0</td>
      <td>24774.0</td>
      <td>...</td>
      <td>16.06</td>
      <td>69.0</td>
      <td>71.0</td>
      <td>17.6</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>25864.721</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Korea</th>
      <td>30.0</td>
      <td>2.1</td>
      <td>10.4</td>
      <td>4.2</td>
      <td>82.0</td>
      <td>18.72</td>
      <td>64.0</td>
      <td>1.1</td>
      <td>19510.0</td>
      <td>29091.0</td>
      <td>...</td>
      <td>14.63</td>
      <td>76.0</td>
      <td>78.0</td>
      <td>17.5</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>27195.197</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>21.0</td>
      <td>4.7</td>
      <td>5.0</td>
      <td>1.1</td>
      <td>57.0</td>
      <td>3.66</td>
      <td>56.0</td>
      <td>0.7</td>
      <td>25166.0</td>
      <td>54987.0</td>
      <td>...</td>
      <td>14.98</td>
      <td>75.0</td>
      <td>71.0</td>
      <td>16.8</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>29866.581</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Japan</th>
      <td>24.0</td>
      <td>1.4</td>
      <td>7.3</td>
      <td>6.4</td>
      <td>94.0</td>
      <td>22.26</td>
      <td>72.0</td>
      <td>0.3</td>
      <td>26111.0</td>
      <td>86764.0</td>
      <td>...</td>
      <td>14.93</td>
      <td>53.0</td>
      <td>85.0</td>
      <td>16.3</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>32485.545</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Israel</th>
      <td>21.0</td>
      <td>6.4</td>
      <td>2.5</td>
      <td>3.7</td>
      <td>85.0</td>
      <td>16.03</td>
      <td>67.0</td>
      <td>2.3</td>
      <td>22104.0</td>
      <td>52933.0</td>
      <td>...</td>
      <td>14.48</td>
      <td>68.0</td>
      <td>68.0</td>
      <td>15.8</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>35343.336</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>New Zealand</th>
      <td>11.0</td>
      <td>2.2</td>
      <td>10.3</td>
      <td>0.2</td>
      <td>74.0</td>
      <td>13.87</td>
      <td>73.0</td>
      <td>1.2</td>
      <td>23815.0</td>
      <td>28290.0</td>
      <td>...</td>
      <td>14.87</td>
      <td>77.0</td>
      <td>89.0</td>
      <td>18.1</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>37044.891</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>France</th>
      <td>12.0</td>
      <td>5.0</td>
      <td>3.5</td>
      <td>0.5</td>
      <td>73.0</td>
      <td>8.15</td>
      <td>64.0</td>
      <td>0.6</td>
      <td>28799.0</td>
      <td>48741.0</td>
      <td>...</td>
      <td>15.33</td>
      <td>80.0</td>
      <td>82.0</td>
      <td>16.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>37675.006</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Belgium</th>
      <td>21.0</td>
      <td>6.6</td>
      <td>4.5</td>
      <td>2.0</td>
      <td>72.0</td>
      <td>4.57</td>
      <td>62.0</td>
      <td>1.1</td>
      <td>28307.0</td>
      <td>83876.0</td>
      <td>...</td>
      <td>15.71</td>
      <td>89.0</td>
      <td>87.0</td>
      <td>18.9</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>40106.632</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>16.0</td>
      <td>3.6</td>
      <td>4.5</td>
      <td>0.1</td>
      <td>86.0</td>
      <td>5.25</td>
      <td>73.0</td>
      <td>0.5</td>
      <td>31252.0</td>
      <td>50394.0</td>
      <td>...</td>
      <td>15.31</td>
      <td>72.0</td>
      <td>95.0</td>
      <td>18.2</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>40996.511</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Finland</th>
      <td>15.0</td>
      <td>2.4</td>
      <td>9.0</td>
      <td>0.6</td>
      <td>85.0</td>
      <td>3.58</td>
      <td>69.0</td>
      <td>1.4</td>
      <td>27927.0</td>
      <td>18761.0</td>
      <td>...</td>
      <td>14.89</td>
      <td>69.0</td>
      <td>94.0</td>
      <td>19.7</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>41973.988</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Canada</th>
      <td>15.0</td>
      <td>1.3</td>
      <td>10.5</td>
      <td>0.2</td>
      <td>89.0</td>
      <td>3.94</td>
      <td>72.0</td>
      <td>1.5</td>
      <td>29365.0</td>
      <td>67913.0</td>
      <td>...</td>
      <td>14.25</td>
      <td>61.0</td>
      <td>91.0</td>
      <td>17.2</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>43331.961</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Netherlands</th>
      <td>30.0</td>
      <td>4.9</td>
      <td>6.1</td>
      <td>0.0</td>
      <td>73.0</td>
      <td>0.45</td>
      <td>74.0</td>
      <td>0.9</td>
      <td>27888.0</td>
      <td>77961.0</td>
      <td>...</td>
      <td>15.44</td>
      <td>75.0</td>
      <td>92.0</td>
      <td>18.7</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>43603.115</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>27.0</td>
      <td>3.4</td>
      <td>7.1</td>
      <td>1.0</td>
      <td>83.0</td>
      <td>7.61</td>
      <td>72.0</td>
      <td>0.4</td>
      <td>31173.0</td>
      <td>49887.0</td>
      <td>...</td>
      <td>14.46</td>
      <td>75.0</td>
      <td>94.0</td>
      <td>17.0</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>43724.031</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>13.0</td>
      <td>1.9</td>
      <td>11.5</td>
      <td>0.2</td>
      <td>78.0</td>
      <td>12.70</td>
      <td>71.0</td>
      <td>0.3</td>
      <td>27029.0</td>
      <td>60778.0</td>
      <td>...</td>
      <td>14.83</td>
      <td>66.0</td>
      <td>88.0</td>
      <td>16.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>43770.688</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>10.0</td>
      <td>5.1</td>
      <td>10.9</td>
      <td>0.0</td>
      <td>88.0</td>
      <td>1.13</td>
      <td>74.0</td>
      <td>0.7</td>
      <td>29185.0</td>
      <td>60328.0</td>
      <td>...</td>
      <td>15.11</td>
      <td>86.0</td>
      <td>95.0</td>
      <td>19.3</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>49866.266</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Iceland</th>
      <td>18.0</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>0.4</td>
      <td>71.0</td>
      <td>12.25</td>
      <td>82.0</td>
      <td>0.3</td>
      <td>23965.0</td>
      <td>43045.0</td>
      <td>...</td>
      <td>14.61</td>
      <td>81.0</td>
      <td>97.0</td>
      <td>19.8</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>50854.583</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Australia</th>
      <td>13.0</td>
      <td>2.1</td>
      <td>10.5</td>
      <td>1.1</td>
      <td>76.0</td>
      <td>14.02</td>
      <td>72.0</td>
      <td>0.8</td>
      <td>31588.0</td>
      <td>47657.0</td>
      <td>...</td>
      <td>14.41</td>
      <td>93.0</td>
      <td>91.0</td>
      <td>19.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>50961.865</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Ireland</th>
      <td>13.0</td>
      <td>2.6</td>
      <td>9.0</td>
      <td>0.2</td>
      <td>75.0</td>
      <td>4.20</td>
      <td>60.0</td>
      <td>0.8</td>
      <td>23917.0</td>
      <td>31580.0</td>
      <td>...</td>
      <td>15.19</td>
      <td>70.0</td>
      <td>80.0</td>
      <td>17.6</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>51350.744</td>
      <td>2014.0</td>
    </tr>
    <tr>
      <th>Denmark</th>
      <td>15.0</td>
      <td>3.9</td>
      <td>7.0</td>
      <td>0.9</td>
      <td>78.0</td>
      <td>2.03</td>
      <td>73.0</td>
      <td>0.3</td>
      <td>26491.0</td>
      <td>44488.0</td>
      <td>...</td>
      <td>16.06</td>
      <td>88.0</td>
      <td>94.0</td>
      <td>19.4</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>52114.165</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>18.0</td>
      <td>1.5</td>
      <td>8.3</td>
      <td>0.1</td>
      <td>89.0</td>
      <td>11.30</td>
      <td>67.0</td>
      <td>5.2</td>
      <td>41355.0</td>
      <td>145769.0</td>
      <td>...</td>
      <td>14.27</td>
      <td>68.0</td>
      <td>85.0</td>
      <td>17.2</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>55805.204</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>16.0</td>
      <td>3.3</td>
      <td>8.1</td>
      <td>0.3</td>
      <td>82.0</td>
      <td>2.82</td>
      <td>75.0</td>
      <td>0.6</td>
      <td>33492.0</td>
      <td>8797.0</td>
      <td>...</td>
      <td>15.56</td>
      <td>78.0</td>
      <td>94.0</td>
      <td>17.9</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>74822.106</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>20.0</td>
      <td>4.2</td>
      <td>8.4</td>
      <td>0.0</td>
      <td>86.0</td>
      <td>6.72</td>
      <td>80.0</td>
      <td>0.5</td>
      <td>33491.0</td>
      <td>108823.0</td>
      <td>...</td>
      <td>14.98</td>
      <td>49.0</td>
      <td>96.0</td>
      <td>17.3</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>80675.308</td>
      <td>2015.0</td>
    </tr>
    <tr>
      <th>Luxembourg</th>
      <td>12.0</td>
      <td>4.3</td>
      <td>6.0</td>
      <td>0.1</td>
      <td>78.0</td>
      <td>3.47</td>
      <td>66.0</td>
      <td>0.4</td>
      <td>38951.0</td>
      <td>61765.0</td>
      <td>...</td>
      <td>15.12</td>
      <td>91.0</td>
      <td>86.0</td>
      <td>15.1</td>
      <td>Gross domestic product per capita, current prices</td>
      <td>U.S. dollars</td>
      <td>Units</td>
      <td>See notes for:  Gross domestic product, curren...</td>
      <td>101994.093</td>
      <td>2014.0</td>
    </tr>
  </tbody123>
</table>
<p>36 rows × 30 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s2">&quot;United States&quot;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>GDP per capita       55805.204
Life satisfaction        7.200
Name: United States, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">remove_indices</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span> <span class="mi">35</span><span class="p">]</span>
<span class="n">keep_indices</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">36</span><span class="p">))</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">remove_indices</span><span class="p">))</span>

<span class="n">sample_data</span> <span class="o">=</span> <span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">keep_indices</span><span class="p">]</span>
<span class="n">missing_data</span> <span class="o">=</span> <span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">remove_indices</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
<span class="n">position_text</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;Hungary&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span>
    <span class="s2">&quot;Korea&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">18000</span><span class="p">,</span> <span class="mf">1.7</span><span class="p">),</span>
    <span class="s2">&quot;France&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">29000</span><span class="p">,</span> <span class="mf">2.4</span><span class="p">),</span>
    <span class="s2">&quot;Australia&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">40000</span><span class="p">,</span> <span class="mf">3.0</span><span class="p">),</span>
    <span class="s2">&quot;United States&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">52000</span><span class="p">,</span> <span class="mf">3.8</span><span class="p">),</span>
<span class="p">}</span>
<span class="k">for</span> <span class="n">country</span><span class="p">,</span> <span class="n">pos_text</span> <span class="ow">in</span> <span class="n">position_text</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span> <span class="o">=</span> <span class="n">sample_data</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">country</span><span class="p">]</span>
    <span class="n">country</span> <span class="o">=</span> <span class="s2">&quot;U.S.&quot;</span> <span class="k">if</span> <span class="n">country</span> <span class="o">==</span> <span class="s2">&quot;United States&quot;</span> <span class="k">else</span> <span class="n">country</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">annotate</span><span class="p">(</span><span class="n">country</span><span class="p">,</span> <span class="n">xy</span><span class="o">=</span><span class="p">(</span><span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span><span class="p">),</span> <span class="n">xytext</span><span class="o">=</span><span class="n">pos_text</span><span class="p">,</span>
            <span class="n">arrowprops</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">facecolor</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">shrink</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="n">head123width</span><span class="o">=</span><span class="mi">5</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span><span class="p">,</span> <span class="s2">&quot;ro&quot;</span><span class="p">)</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;money_happy_scatterplot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Saving figure123 money_happy_scatterplot
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">FileNotFoundError</span>                         Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-28-484cd375c49f&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">     14</span>             arrowprops=dict(facecolor=&#39;black&#39;, width=0.5, shrink=0.1, head123width=5))
<span class="ansi-green-fg">     15</span>     plt<span class="ansi-yellow-intense-fg ansi-bold">.</span>plot<span class="ansi-yellow-intense-fg ansi-bold">(</span>pos_data_x<span class="ansi-yellow-intense-fg ansi-bold">,</span> pos_data_y<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#34;ro&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 16</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>save_fig<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;money_happy_scatterplot&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">     17</span> plt<span class="ansi-yellow-intense-fg ansi-bold">.</span>show<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-15-9638bc9ca288&gt;</span> in <span class="ansi-cyan-fg">save_fig</span><span class="ansi-blue-intense-fg ansi-bold">(fig_id, tight_layout)</span>
<span class="ansi-green-fg">     26</span>     <span class="ansi-green-intense-fg ansi-bold">if</span> tight_layout<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">     27</span>         plt<span class="ansi-yellow-intense-fg ansi-bold">.</span>tight_layout<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 28</span><span class="ansi-yellow-intense-fg ansi-bold">     </span>plt<span class="ansi-yellow-intense-fg ansi-bold">.</span>savefig<span class="ansi-yellow-intense-fg ansi-bold">(</span>path<span class="ansi-yellow-intense-fg ansi-bold">,</span> format<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-blue-intense-fg ansi-bold">&#39;png&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> dpi<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-cyan-intense-fg ansi-bold">300</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">     29</span> 
<span class="ansi-green-fg">     30</span> <span class="ansi-red-intense-fg ansi-bold"># Ignore useless warnings (see SciPy issue #5998)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\pyplot.py</span> in <span class="ansi-cyan-fg">savefig</span><span class="ansi-blue-intense-fg ansi-bold">(*args, **kwargs)</span>
<span class="ansi-green-fg">    721</span> <span class="ansi-green-intense-fg ansi-bold">def</span> savefig<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    722</span>     fig <span class="ansi-yellow-intense-fg ansi-bold">=</span> gcf<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 723</span><span class="ansi-yellow-intense-fg ansi-bold">     </span>res <span class="ansi-yellow-intense-fg ansi-bold">=</span> fig<span class="ansi-yellow-intense-fg ansi-bold">.</span>savefig<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    724</span>     fig<span class="ansi-yellow-intense-fg ansi-bold">.</span>canvas<span class="ansi-yellow-intense-fg ansi-bold">.</span>draw_idle<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>   <span class="ansi-red-intense-fg ansi-bold"># need this if &#39;transparent=True&#39; to reset colors</span>
<span class="ansi-green-fg">    725</span>     <span class="ansi-green-intense-fg ansi-bold">return</span> res

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\figure123.py</span> in <span class="ansi-cyan-fg">savefig</span><span class="ansi-blue-intense-fg ansi-bold">(self, fname, transparent, **kwargs)</span>
<span class="ansi-green-fg">   2201</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>patch<span class="ansi-yellow-intense-fg ansi-bold">.</span>set_visible<span class="ansi-yellow-intense-fg ansi-bold">(</span>frameon<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   2202</span> 
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2203</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>canvas<span class="ansi-yellow-intense-fg ansi-bold">.</span>print_figure123<span class="ansi-yellow-intense-fg ansi-bold">(</span>fname<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   2204</span> 
<span class="ansi-green-fg">   2205</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> frameon<span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\backend_bases.py</span> in <span class="ansi-cyan-fg">print_figure123</span><span class="ansi-blue-intense-fg ansi-bold">(self, filename, dpi, facecolor, edgecolor, orientation, format, bbox_inches, **kwargs)</span>
<span class="ansi-green-fg">   2117</span> 
<span class="ansi-green-fg">   2118</span>             <span class="ansi-green-intense-fg ansi-bold">try</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2119</span><span class="ansi-yellow-intense-fg ansi-bold">                 result = print_method(
</span><span class="ansi-green-fg">   2120</span>                     filename<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">   2121</span>                     dpi<span class="ansi-yellow-intense-fg ansi-bold">=</span>dpi<span class="ansi-yellow-intense-fg ansi-bold">,</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\backends\backend_agg.py</span> in <span class="ansi-cyan-fg">print_png</span><span class="ansi-blue-intense-fg ansi-bold">(self, filename_or_obj, metadata, pil_kwargs, *args, **kwargs)</span>
<span class="ansi-green-fg">    533</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    534</span>             renderer <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>get_renderer<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 535</span><span class="ansi-yellow-intense-fg ansi-bold">             </span><span class="ansi-green-intense-fg ansi-bold">with</span> cbook<span class="ansi-yellow-intense-fg ansi-bold">.</span>open_file_cm<span class="ansi-yellow-intense-fg ansi-bold">(</span>filename_or_obj<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#34;wb&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-green-intense-fg ansi-bold">as</span> fh<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    536</span>                 _png.write_png(renderer._renderer, fh, self.figure123.dpi,
<span class="ansi-green-fg">    537</span>                                metadata={**default_metadata, **metadata})

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\contextlib.py</span> in <span class="ansi-cyan-fg">__enter__</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    111</span>         <span class="ansi-green-intense-fg ansi-bold">del</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>kwds<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>func
<span class="ansi-green-fg">    112</span>         <span class="ansi-green-intense-fg ansi-bold">try</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 113</span><span class="ansi-yellow-intense-fg ansi-bold">             </span><span class="ansi-green-intense-fg ansi-bold">return</span> next<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>gen<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    114</span>         <span class="ansi-green-intense-fg ansi-bold">except</span> StopIteration<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    115</span>             <span class="ansi-green-intense-fg ansi-bold">raise</span> RuntimeError<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;generator didn&#39;t yield&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-green-intense-fg ansi-bold">from</span> <span class="ansi-green-intense-fg ansi-bold">None</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\cbook\__init__.py</span> in <span class="ansi-cyan-fg">open_file_cm</span><span class="ansi-blue-intense-fg ansi-bold">(path_or_file, mode, encoding)</span>
<span class="ansi-green-fg">    416</span> <span class="ansi-green-intense-fg ansi-bold">def</span> open_file_cm<span class="ansi-yellow-intense-fg ansi-bold">(</span>path_or_file<span class="ansi-yellow-intense-fg ansi-bold">,</span> mode<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-blue-intense-fg ansi-bold">&#34;r&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> encoding<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    417</span>     <span class="ansi-blue-intense-fg ansi-bold">r&#34;&#34;&#34;Pass through file objects and context-manage `.PathLike`\s.&#34;&#34;&#34;</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 418</span><span class="ansi-yellow-intense-fg ansi-bold">     </span>fh<span class="ansi-yellow-intense-fg ansi-bold">,</span> opened <span class="ansi-yellow-intense-fg ansi-bold">=</span> to_filehandle<span class="ansi-yellow-intense-fg ansi-bold">(</span>path_or_file<span class="ansi-yellow-intense-fg ansi-bold">,</span> mode<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-green-intense-fg ansi-bold">True</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> encoding<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    419</span>     <span class="ansi-green-intense-fg ansi-bold">if</span> opened<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    420</span>         <span class="ansi-green-intense-fg ansi-bold">with</span> fh<span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\matplotlib\cbook\__init__.py</span> in <span class="ansi-cyan-fg">to_filehandle</span><span class="ansi-blue-intense-fg ansi-bold">(fname, flag, return_opened, encoding)</span>
<span class="ansi-green-fg">    401</span>             fh <span class="ansi-yellow-intense-fg ansi-bold">=</span> bz2<span class="ansi-yellow-intense-fg ansi-bold">.</span>BZ2File<span class="ansi-yellow-intense-fg ansi-bold">(</span>fname<span class="ansi-yellow-intense-fg ansi-bold">,</span> flag<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    402</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 403</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>fh <span class="ansi-yellow-intense-fg ansi-bold">=</span> open<span class="ansi-yellow-intense-fg ansi-bold">(</span>fname<span class="ansi-yellow-intense-fg ansi-bold">,</span> flag<span class="ansi-yellow-intense-fg ansi-bold">,</span> encoding<span class="ansi-yellow-intense-fg ansi-bold">=</span>encoding<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    404</span>         opened <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">True</span>
<span class="ansi-green-fg">    405</span>     <span class="ansi-green-intense-fg ansi-bold">elif</span> hasattr<span class="ansi-yellow-intense-fg ansi-bold">(</span>fname<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;seek&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-red-intense-fg ansi-bold">FileNotFoundError</span>: [Errno 2] No such file or directory: &#39;.\\images\\fundamentals\\money_happy_scatterplot.png&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;lifesat&quot;</span><span class="p">,</span> <span class="s2">&quot;lifesat.csv&quot;</span><span class="p">))</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">position_text</span><span class="o">.</span><span class="n">keys</span><span class="p">())]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">sample_data</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
<span class="n">X</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">X</span><span class="o">/</span><span class="mi">100000</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">40000</span><span class="p">,</span> <span class="mf">2.7</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_0 = 0$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;r&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">40000</span><span class="p">,</span> <span class="mf">1.8</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_1 = 2 \times 10^{-5}$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;r&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="mi">8</span> <span class="o">-</span> <span class="mi">5</span><span class="o">*</span><span class="n">X</span><span class="o">/</span><span class="mi">100000</span><span class="p">,</span> <span class="s2">&quot;g&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">9.1</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_0 = 8$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;g&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">8.2</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_1 = -5 \times 10^{-5}$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;g&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="mi">4</span> <span class="o">+</span> <span class="mi">5</span><span class="o">*</span><span class="n">X</span><span class="o">/</span><span class="mi">100000</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">3.5</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_0 = 4$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">2.6</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_1 = 5 \times 10^{-5}$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;tweaking_model_params_plot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">linear_model</span>
<span class="n">lin1</span> <span class="o">=</span> <span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">Xsample</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">ysample</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>
<span class="n">lin1</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">Xsample</span><span class="p">,</span> <span class="n">ysample</span><span class="p">)</span>
<span class="n">t0</span><span class="p">,</span> <span class="n">t1</span> <span class="o">=</span> <span class="n">lin1</span><span class="o">.</span><span class="n">intercept_</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">lin1</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
<span class="n">t0</span><span class="p">,</span> <span class="n">t1</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
<span class="n">X</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0</span> <span class="o">+</span> <span class="n">t1</span><span class="o">*</span><span class="n">X</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">3.1</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_0 = 4.85$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">2.2</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_1 = 4.91 \times 10^{-5}$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;best_fit_model_plot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cyprus_gdp_per_capita</span> <span class="o">=</span> <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s2">&quot;Cyprus&quot;</span><span class="p">][</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cyprus_gdp_per_capita</span><span class="p">)</span>
<span class="n">cyprus_predicted_life_satisfaction</span> <span class="o">=</span> <span class="n">lin1</span><span class="o">.</span><span class="n">predict</span><span class="p">([[</span><span class="n">cyprus_gdp_per_capita</span><span class="p">]])[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
<span class="n">cyprus_predicted_life_satisfaction</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="p">[</span><span class="mi">7</span><span class="p">:</span><span class="mi">10</span><span class="p">]</span>
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
      <th>GDP per capita</th>
      <th>Life satisfaction</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>Portugal</th>
      <td>19121.592</td>
      <td>5.1</td>
    </tr>
    <tr>
      <th>Slovenia</th>
      <td>20732.482</td>
      <td>5.7</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>25864.721</td>
      <td>6.5</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">(</span><span class="mf">5.1</span><span class="o">+</span><span class="mf">5.7</span><span class="o">+</span><span class="mf">6.5</span><span class="p">)</span><span class="o">/</span><span class="mi">3</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[34]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>5.766666666666667</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">backup</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span>

<span class="k">def</span> <span class="nf">prepare_country_stats</span><span class="p">(</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span><span class="p">):</span>
    <span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="p">[</span><span class="n">oecd_bli</span><span class="p">[</span><span class="s2">&quot;INEQUALITY&quot;</span><span class="p">]</span><span class="o">==</span><span class="s2">&quot;TOT&quot;</span><span class="p">]</span>
    <span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="o">.</span><span class="n">pivot</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="s2">&quot;Indicator&quot;</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="s2">&quot;Value&quot;</span><span class="p">)</span>
    <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;2015&quot;</span><span class="p">:</span> <span class="s2">&quot;GDP per capita&quot;</span><span class="p">},</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">full_country_stats</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">left</span><span class="o">=</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">right</span><span class="o">=</span><span class="n">gdp_per_capita</span><span class="p">,</span>
                                  <span class="n">left_index</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">right_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">full_country_stats</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">remove_indices</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span> <span class="mi">35</span><span class="p">]</span>
    <span class="n">keep_indices</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">36</span><span class="p">))</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">remove_indices</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">keep_indices</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Code example</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">sklearn</span>

<span class="c1"># Load the data</span>
<span class="n">oecd_bli</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span> <span class="o">+</span> <span class="s2">&quot;oecd_bli_2015.csv&quot;</span><span class="p">,</span> <span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">)</span>
<span class="n">gdp_per_capita</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">datapath</span> <span class="o">+</span> <span class="s2">&quot;gdp_per_capita.csv&quot;</span><span class="p">,</span><span class="n">thousands</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">,</span>
                             <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;latin1&#39;</span><span class="p">,</span> <span class="n">na_values</span><span class="o">=</span><span class="s2">&quot;n/a&quot;</span><span class="p">)</span>

<span class="c1"># Prepare the data</span>
<span class="n">country_stats</span> <span class="o">=</span> <span class="n">prepare_country_stats</span><span class="p">(</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span><span class="p">)</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>

<span class="c1"># Visualize the data</span>
<span class="n">country_stats</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1"># Select a linear model</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">sklearn</span><span class="o">.</span><span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="268.003125pt" version="1.1" viewBox="0 0 392.833125 268.003125" width="392.833125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 268.003125 

L 392.833125 268.003125 

L 392.833125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 50.833125 224.64 

L 385.633125 224.64 

L 385.633125 7.2 

L 50.833125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_1">

    <defs>

     <path d="M 0 2.236068 

C 0.593012 2.236068 1.161816 2.000462 1.581139 1.581139 

C 2.000462 1.161816 2.236068 0.593012 2.236068 0 

C 2.236068 -0.593012 2.000462 -1.161816 1.581139 -1.581139 

C 1.161816 -2.000462 0.593012 -2.236068 0 -2.236068 

C -0.593012 -2.236068 -1.161816 -2.000462 -1.581139 -1.581139 

C -2.000462 -1.161816 -2.236068 -0.593012 -2.236068 0 

C -2.236068 0.593012 -2.000462 1.161816 -1.581139 1.581139 

C -1.161816 2.000462 -0.593012 2.236068 0 2.236068 

z

" id="mf5f0f3200c" style="stroke:#1f77b4;"/>

    </defs>

    <g clip-path="url(#pb47d2f8981)">

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="66.051307" xlink:href="#mf5f0f3200c" y="126.901818"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="68.541266" xlink:href="#mf5f0f3200c" y="156.186667"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="86.786838" xlink:href="#mf5f0f3200c" y="207.435152"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="88.449858" xlink:href="#mf5f0f3200c" y="141.544242"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="111.212874" xlink:href="#mf5f0f3200c" y="119.580606"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="119.652627" xlink:href="#mf5f0f3200c" y="156.186667"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="124.706041" xlink:href="#mf5f0f3200c" y="214.756364"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="131.589525" xlink:href="#mf5f0f3200c" y="192.792727"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="142.077082" xlink:href="#mf5f0f3200c" y="148.865455"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="175.490071" xlink:href="#mf5f0f3200c" y="90.295758"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="184.152018" xlink:href="#mf5f0f3200c" y="141.544242"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="201.543828" xlink:href="#mf5f0f3200c" y="126.901818"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="218.594362" xlink:href="#mf5f0f3200c" y="134.22303"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="237.199758" xlink:href="#mf5f0f3200c" y="24.404848"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="248.277581" xlink:href="#mf5f0f3200c" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="252.379889" xlink:href="#mf5f0f3200c" y="90.295758"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="268.210776" xlink:href="#mf5f0f3200c" y="61.010909"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="274.004255" xlink:href="#mf5f0f3200c" y="53.689697"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="280.368032" xlink:href="#mf5f0f3200c" y="24.404848"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="289.208996" xlink:href="#mf5f0f3200c" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="290.97432" xlink:href="#mf5f0f3200c" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="291.761533" xlink:href="#mf5f0f3200c" y="61.010909"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="292.065289" xlink:href="#mf5f0f3200c" y="68.332121"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="331.750012" xlink:href="#mf5f0f3200c" y="39.047273"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="338.184362" xlink:href="#mf5f0f3200c" y="17.083636"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="338.882812" xlink:href="#mf5f0f3200c" y="31.726061"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="341.414575" xlink:href="#mf5f0f3200c" y="53.689697"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="346.38476" xlink:href="#mf5f0f3200c" y="17.083636"/>

     <use style="fill:#1f77b4;stroke:#1f77b4;" x="370.414943" xlink:href="#mf5f0f3200c" y="39.047273"/>

    </g>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m6b862ca9f3" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="72.204206" xlink:href="#m6b862ca9f3" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 10000 -->

      <defs>

       <path d="M 12.40625 8.296875 

L 28.515625 8.296875 

L 28.515625 63.921875 

L 10.984375 60.40625 

L 10.984375 69.390625 

L 28.421875 72.90625 

L 38.28125 72.90625 

L 38.28125 8.296875 

L 54.390625 8.296875 

L 54.390625 0 

L 12.40625 0 

z

" id="DejaVuSans-49"/>

       <path d="M 31.78125 66.40625 

Q 24.171875 66.40625 20.328125 58.90625 

Q 16.5 51.421875 16.5 36.375 

Q 16.5 21.390625 20.328125 13.890625 

Q 24.171875 6.390625 31.78125 6.390625 

Q 39.453125 6.390625 43.28125 13.890625 

Q 47.125 21.390625 47.125 36.375 

Q 47.125 51.421875 43.28125 58.90625 

Q 39.453125 66.40625 31.78125 66.40625 

z

M 31.78125 74.21875 

Q 44.046875 74.21875 50.515625 64.515625 

Q 56.984375 54.828125 56.984375 36.375 

Q 56.984375 17.96875 50.515625 8.265625 

Q 44.046875 -1.421875 31.78125 -1.421875 

Q 19.53125 -1.421875 13.0625 8.265625 

Q 6.59375 17.96875 6.59375 36.375 

Q 6.59375 54.828125 13.0625 64.515625 

Q 19.53125 74.21875 31.78125 74.21875 

z

" id="DejaVuSans-48"/>

      </defs>

      <g transform="translate(53.116706 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="137.308323" xlink:href="#m6b862ca9f3" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 20000 -->

      <defs>

       <path d="M 19.1875 8.296875 

L 53.609375 8.296875 

L 53.609375 0 

L 7.328125 0 

L 7.328125 8.296875 

Q 12.9375 14.109375 22.625 23.890625 

Q 32.328125 33.6875 34.8125 36.53125 

Q 39.546875 41.84375 41.421875 45.53125 

Q 43.3125 49.21875 43.3125 52.78125 

Q 43.3125 58.59375 39.234375 62.25 

Q 35.15625 65.921875 28.609375 65.921875 

Q 23.96875 65.921875 18.8125 64.3125 

Q 13.671875 62.703125 7.8125 59.421875 

L 7.8125 69.390625 

Q 13.765625 71.78125 18.9375 73 

Q 24.125 74.21875 28.421875 74.21875 

Q 39.75 74.21875 46.484375 68.546875 

Q 53.21875 62.890625 53.21875 53.421875 

Q 53.21875 48.921875 51.53125 44.890625 

Q 49.859375 40.875 45.40625 35.40625 

Q 44.1875 33.984375 37.640625 27.21875 

Q 31.109375 20.453125 19.1875 8.296875 

z

" id="DejaVuSans-50"/>

      </defs>

      <g transform="translate(118.220823 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="202.41244" xlink:href="#m6b862ca9f3" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 30000 -->

      <defs>

       <path d="M 40.578125 39.3125 

Q 47.65625 37.796875 51.625 33 

Q 55.609375 28.21875 55.609375 21.1875 

Q 55.609375 10.40625 48.1875 4.484375 

Q 40.765625 -1.421875 27.09375 -1.421875 

Q 22.515625 -1.421875 17.65625 -0.515625 

Q 12.796875 0.390625 7.625 2.203125 

L 7.625 11.71875 

Q 11.71875 9.328125 16.59375 8.109375 

Q 21.484375 6.890625 26.8125 6.890625 

Q 36.078125 6.890625 40.9375 10.546875 

Q 45.796875 14.203125 45.796875 21.1875 

Q 45.796875 27.640625 41.28125 31.265625 

Q 36.765625 34.90625 28.71875 34.90625 

L 20.21875 34.90625 

L 20.21875 43.015625 

L 29.109375 43.015625 

Q 36.375 43.015625 40.234375 45.921875 

Q 44.09375 48.828125 44.09375 54.296875 

Q 44.09375 59.90625 40.109375 62.90625 

Q 36.140625 65.921875 28.71875 65.921875 

Q 24.65625 65.921875 20.015625 65.03125 

Q 15.375 64.15625 9.8125 62.3125 

L 9.8125 71.09375 

Q 15.4375 72.65625 20.34375 73.4375 

Q 25.25 74.21875 29.59375 74.21875 

Q 40.828125 74.21875 47.359375 69.109375 

Q 53.90625 64.015625 53.90625 55.328125 

Q 53.90625 49.265625 50.4375 45.09375 

Q 46.96875 40.921875 40.578125 39.3125 

z

" id="DejaVuSans-51"/>

      </defs>

      <g transform="translate(183.32494 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="267.516558" xlink:href="#m6b862ca9f3" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 40000 -->

      <defs>

       <path d="M 37.796875 64.3125 

L 12.890625 25.390625 

L 37.796875 25.390625 

z

M 35.203125 72.90625 

L 47.609375 72.90625 

L 47.609375 25.390625 

L 58.015625 25.390625 

L 58.015625 17.1875 

L 47.609375 17.1875 

L 47.609375 0 

L 37.796875 0 

L 37.796875 17.1875 

L 4.890625 17.1875 

L 4.890625 26.703125 

z

" id="DejaVuSans-52"/>

      </defs>

      <g transform="translate(248.429058 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="332.620675" xlink:href="#m6b862ca9f3" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 50000 -->

      <defs>

       <path d="M 10.796875 72.90625 

L 49.515625 72.90625 

L 49.515625 64.59375 

L 19.828125 64.59375 

L 19.828125 46.734375 

Q 21.96875 47.46875 24.109375 47.828125 

Q 26.265625 48.1875 28.421875 48.1875 

Q 40.625 48.1875 47.75 41.5 

Q 54.890625 34.8125 54.890625 23.390625 

Q 54.890625 11.625 47.5625 5.09375 

Q 40.234375 -1.421875 26.90625 -1.421875 

Q 22.3125 -1.421875 17.546875 -0.640625 

Q 12.796875 0.140625 7.71875 1.703125 

L 7.71875 11.625 

Q 12.109375 9.234375 16.796875 8.0625 

Q 21.484375 6.890625 26.703125 6.890625 

Q 35.15625 6.890625 40.078125 11.328125 

Q 45.015625 15.765625 45.015625 23.390625 

Q 45.015625 31 40.078125 35.4375 

Q 35.15625 39.890625 26.703125 39.890625 

Q 22.75 39.890625 18.8125 39.015625 

Q 14.890625 38.140625 10.796875 36.28125 

z

" id="DejaVuSans-53"/>

      </defs>

      <g transform="translate(313.533175 240.758125)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

       <use x="254.492188" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="text_6">

     <!-- GDP per capita -->

     <defs>

      <path d="M 59.515625 10.40625 

L 59.515625 29.984375 

L 43.40625 29.984375 

L 43.40625 38.09375 

L 69.28125 38.09375 

L 69.28125 6.78125 

Q 63.578125 2.734375 56.6875 0.65625 

Q 49.8125 -1.421875 42 -1.421875 

Q 24.90625 -1.421875 15.25 8.5625 

Q 5.609375 18.5625 5.609375 36.375 

Q 5.609375 54.25 15.25 64.234375 

Q 24.90625 74.21875 42 74.21875 

Q 49.125 74.21875 55.546875 72.453125 

Q 61.96875 70.703125 67.390625 67.28125 

L 67.390625 56.78125 

Q 61.921875 61.421875 55.765625 63.765625 

Q 49.609375 66.109375 42.828125 66.109375 

Q 29.4375 66.109375 22.71875 58.640625 

Q 16.015625 51.171875 16.015625 36.375 

Q 16.015625 21.625 22.71875 14.15625 

Q 29.4375 6.6875 42.828125 6.6875 

Q 48.046875 6.6875 52.140625 7.59375 

Q 56.25 8.5 59.515625 10.40625 

z

" id="DejaVuSans-71"/>

      <path d="M 19.671875 64.796875 

L 19.671875 8.109375 

L 31.59375 8.109375 

Q 46.6875 8.109375 53.6875 14.9375 

Q 60.6875 21.78125 60.6875 36.53125 

Q 60.6875 51.171875 53.6875 57.984375 

Q 46.6875 64.796875 31.59375 64.796875 

z

M 9.8125 72.90625 

L 30.078125 72.90625 

Q 51.265625 72.90625 61.171875 64.09375 

Q 71.09375 55.28125 71.09375 36.53125 

Q 71.09375 17.671875 61.125 8.828125 

Q 51.171875 0 30.078125 0 

L 9.8125 0 

z

" id="DejaVuSans-68"/>

      <path d="M 19.671875 64.796875 

L 19.671875 37.40625 

L 32.078125 37.40625 

Q 38.96875 37.40625 42.71875 40.96875 

Q 46.484375 44.53125 46.484375 51.125 

Q 46.484375 57.671875 42.71875 61.234375 

Q 38.96875 64.796875 32.078125 64.796875 

z

M 9.8125 72.90625 

L 32.078125 72.90625 

Q 44.34375 72.90625 50.609375 67.359375 

Q 56.890625 61.8125 56.890625 51.125 

Q 56.890625 40.328125 50.609375 34.8125 

Q 44.34375 29.296875 32.078125 29.296875 

L 19.671875 29.296875 

L 19.671875 0 

L 9.8125 0 

z

" id="DejaVuSans-80"/>

      <path id="DejaVuSans-32"/>

      <path d="M 18.109375 8.203125 

L 18.109375 -20.796875 

L 9.078125 -20.796875 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.390625 

Q 20.953125 51.265625 25.265625 53.625 

Q 29.59375 56 35.59375 56 

Q 45.5625 56 51.78125 48.09375 

Q 58.015625 40.1875 58.015625 27.296875 

Q 58.015625 14.40625 51.78125 6.484375 

Q 45.5625 -1.421875 35.59375 -1.421875 

Q 29.59375 -1.421875 25.265625 0.953125 

Q 20.953125 3.328125 18.109375 8.203125 

z

M 48.6875 27.296875 

Q 48.6875 37.203125 44.609375 42.84375 

Q 40.53125 48.484375 33.40625 48.484375 

Q 26.265625 48.484375 22.1875 42.84375 

Q 18.109375 37.203125 18.109375 27.296875 

Q 18.109375 17.390625 22.1875 11.75 

Q 26.265625 6.109375 33.40625 6.109375 

Q 40.53125 6.109375 44.609375 11.75 

Q 48.6875 17.390625 48.6875 27.296875 

z

" id="DejaVuSans-112"/>

      <path d="M 56.203125 29.59375 

L 56.203125 25.203125 

L 14.890625 25.203125 

Q 15.484375 15.921875 20.484375 11.0625 

Q 25.484375 6.203125 34.421875 6.203125 

Q 39.59375 6.203125 44.453125 7.46875 

Q 49.3125 8.734375 54.109375 11.28125 

L 54.109375 2.78125 

Q 49.265625 0.734375 44.1875 -0.34375 

Q 39.109375 -1.421875 33.890625 -1.421875 

Q 20.796875 -1.421875 13.15625 6.1875 

Q 5.515625 13.8125 5.515625 26.8125 

Q 5.515625 40.234375 12.765625 48.109375 

Q 20.015625 56 32.328125 56 

Q 43.359375 56 49.78125 48.890625 

Q 56.203125 41.796875 56.203125 29.59375 

z

M 47.21875 32.234375 

Q 47.125 39.59375 43.09375 43.984375 

Q 39.0625 48.390625 32.421875 48.390625 

Q 24.90625 48.390625 20.390625 44.140625 

Q 15.875 39.890625 15.1875 32.171875 

z

" id="DejaVuSans-101"/>

      <path d="M 41.109375 46.296875 

Q 39.59375 47.171875 37.8125 47.578125 

Q 36.03125 48 33.890625 48 

Q 26.265625 48 22.1875 43.046875 

Q 18.109375 38.09375 18.109375 28.8125 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 20.953125 51.171875 25.484375 53.578125 

Q 30.03125 56 36.53125 56 

Q 37.453125 56 38.578125 55.875 

Q 39.703125 55.765625 41.0625 55.515625 

z

" id="DejaVuSans-114"/>

      <path d="M 48.78125 52.59375 

L 48.78125 44.1875 

Q 44.96875 46.296875 41.140625 47.34375 

Q 37.3125 48.390625 33.40625 48.390625 

Q 24.65625 48.390625 19.8125 42.84375 

Q 14.984375 37.3125 14.984375 27.296875 

Q 14.984375 17.28125 19.8125 11.734375 

Q 24.65625 6.203125 33.40625 6.203125 

Q 37.3125 6.203125 41.140625 7.25 

Q 44.96875 8.296875 48.78125 10.40625 

L 48.78125 2.09375 

Q 45.015625 0.34375 40.984375 -0.53125 

Q 36.96875 -1.421875 32.421875 -1.421875 

Q 20.0625 -1.421875 12.78125 6.34375 

Q 5.515625 14.109375 5.515625 27.296875 

Q 5.515625 40.671875 12.859375 48.328125 

Q 20.21875 56 33.015625 56 

Q 37.15625 56 41.109375 55.140625 

Q 45.0625 54.296875 48.78125 52.59375 

z

" id="DejaVuSans-99"/>

      <path d="M 34.28125 27.484375 

Q 23.390625 27.484375 19.1875 25 

Q 14.984375 22.515625 14.984375 16.5 

Q 14.984375 11.71875 18.140625 8.90625 

Q 21.296875 6.109375 26.703125 6.109375 

Q 34.1875 6.109375 38.703125 11.40625 

Q 43.21875 16.703125 43.21875 25.484375 

L 43.21875 27.484375 

z

M 52.203125 31.203125 

L 52.203125 0 

L 43.21875 0 

L 43.21875 8.296875 

Q 40.140625 3.328125 35.546875 0.953125 

Q 30.953125 -1.421875 24.3125 -1.421875 

Q 15.921875 -1.421875 10.953125 3.296875 

Q 6 8.015625 6 15.921875 

Q 6 25.140625 12.171875 29.828125 

Q 18.359375 34.515625 30.609375 34.515625 

L 43.21875 34.515625 

L 43.21875 35.40625 

Q 43.21875 41.609375 39.140625 45 

Q 35.0625 48.390625 27.6875 48.390625 

Q 23 48.390625 18.546875 47.265625 

Q 14.109375 46.140625 10.015625 43.890625 

L 10.015625 52.203125 

Q 14.9375 54.109375 19.578125 55.046875 

Q 24.21875 56 28.609375 56 

Q 40.484375 56 46.34375 49.84375 

Q 52.203125 43.703125 52.203125 31.203125 

z

" id="DejaVuSans-97"/>

      <path d="M 9.421875 54.6875 

L 18.40625 54.6875 

L 18.40625 0 

L 9.421875 0 

z

M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 64.59375 

L 9.421875 64.59375 

z

" id="DejaVuSans-105"/>

      <path d="M 18.3125 70.21875 

L 18.3125 54.6875 

L 36.8125 54.6875 

L 36.8125 47.703125 

L 18.3125 47.703125 

L 18.3125 18.015625 

Q 18.3125 11.328125 20.140625 9.421875 

Q 21.96875 7.515625 27.59375 7.515625 

L 36.8125 7.515625 

L 36.8125 0 

L 27.59375 0 

Q 17.1875 0 13.234375 3.875 

Q 9.28125 7.765625 9.28125 18.015625 

L 9.28125 47.703125 

L 2.6875 47.703125 

L 2.6875 54.6875 

L 9.28125 54.6875 

L 9.28125 70.21875 

z

" id="DejaVuSans-116"/>

     </defs>

     <g transform="translate(165.559219 257.891562)scale(0.14 -0.14)">

      <use xlink:href="#DejaVuSans-71"/>

      <use x="77.490234" xlink:href="#DejaVuSans-68"/>

      <use x="154.492188" xlink:href="#DejaVuSans-80"/>

      <use x="214.794922" xlink:href="#DejaVuSans-32"/>

      <use x="246.582031" xlink:href="#DejaVuSans-112"/>

      <use x="310.058594" xlink:href="#DejaVuSans-101"/>

      <use x="371.582031" xlink:href="#DejaVuSans-114"/>

      <use x="412.695312" xlink:href="#DejaVuSans-32"/>

      <use x="444.482422" xlink:href="#DejaVuSans-99"/>

      <use x="499.462891" xlink:href="#DejaVuSans-97"/>

      <use x="560.742188" xlink:href="#DejaVuSans-112"/>

      <use x="624.21875" xlink:href="#DejaVuSans-105"/>

      <use x="652.001953" xlink:href="#DejaVuSans-116"/>

      <use x="691.210938" xlink:href="#DejaVuSans-97"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_6">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="ma0acebd0ee" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="200.113939"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 5.0 -->

      <defs>

       <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

      </defs>

      <g transform="translate(24.749375 204.673002)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="163.507879"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 5.5 -->

      <g transform="translate(24.749375 168.066941)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="126.901818"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 6.0 -->

      <defs>

       <path d="M 33.015625 40.375 

Q 26.375 40.375 22.484375 35.828125 

Q 18.609375 31.296875 18.609375 23.390625 

Q 18.609375 15.53125 22.484375 10.953125 

Q 26.375 6.390625 33.015625 6.390625 

Q 39.65625 6.390625 43.53125 10.953125 

Q 47.40625 15.53125 47.40625 23.390625 

Q 47.40625 31.296875 43.53125 35.828125 

Q 39.65625 40.375 33.015625 40.375 

z

M 52.59375 71.296875 

L 52.59375 62.3125 

Q 48.875 64.0625 45.09375 64.984375 

Q 41.3125 65.921875 37.59375 65.921875 

Q 27.828125 65.921875 22.671875 59.328125 

Q 17.53125 52.734375 16.796875 39.40625 

Q 19.671875 43.65625 24.015625 45.921875 

Q 28.375 48.1875 33.59375 48.1875 

Q 44.578125 48.1875 50.953125 41.515625 

Q 57.328125 34.859375 57.328125 23.390625 

Q 57.328125 12.15625 50.6875 5.359375 

Q 44.046875 -1.421875 33.015625 -1.421875 

Q 20.359375 -1.421875 13.671875 8.265625 

Q 6.984375 17.96875 6.984375 36.375 

Q 6.984375 53.65625 15.1875 63.9375 

Q 23.390625 74.21875 37.203125 74.21875 

Q 40.921875 74.21875 44.703125 73.484375 

Q 48.484375 72.75 52.59375 71.296875 

z

" id="DejaVuSans-54"/>

      </defs>

      <g transform="translate(24.749375 131.460881)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="90.295758"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 6.5 -->

      <g transform="translate(24.749375 94.85482)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="53.689697"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 7.0 -->

      <defs>

       <path d="M 8.203125 72.90625 

L 55.078125 72.90625 

L 55.078125 68.703125 

L 28.609375 0 

L 18.3125 0 

L 43.21875 64.59375 

L 8.203125 64.59375 

z

" id="DejaVuSans-55"/>

      </defs>

      <g transform="translate(24.749375 58.248759)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.833125" xlink:href="#ma0acebd0ee" y="17.083636"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 7.5 -->

      <g transform="translate(24.749375 21.642699)scale(0.12 -0.12)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_13">

     <!-- Life satisfaction -->

     <defs>

      <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

      <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

      <path d="M 44.28125 53.078125 

L 44.28125 44.578125 

Q 40.484375 46.53125 36.375 47.5 

Q 32.28125 48.484375 27.875 48.484375 

Q 21.1875 48.484375 17.84375 46.4375 

Q 14.5 44.390625 14.5 40.28125 

Q 14.5 37.15625 16.890625 35.375 

Q 19.28125 33.59375 26.515625 31.984375 

L 29.59375 31.296875 

Q 39.15625 29.25 43.1875 25.515625 

Q 47.21875 21.78125 47.21875 15.09375 

Q 47.21875 7.46875 41.1875 3.015625 

Q 35.15625 -1.421875 24.609375 -1.421875 

Q 20.21875 -1.421875 15.453125 -0.5625 

Q 10.6875 0.296875 5.421875 2 

L 5.421875 11.28125 

Q 10.40625 8.6875 15.234375 7.390625 

Q 20.0625 6.109375 24.8125 6.109375 

Q 31.15625 6.109375 34.5625 8.28125 

Q 37.984375 10.453125 37.984375 14.40625 

Q 37.984375 18.0625 35.515625 20.015625 

Q 33.0625 21.96875 24.703125 23.78125 

L 21.578125 24.515625 

Q 13.234375 26.265625 9.515625 29.90625 

Q 5.8125 33.546875 5.8125 39.890625 

Q 5.8125 47.609375 11.28125 51.796875 

Q 16.75 56 26.8125 56 

Q 31.78125 56 36.171875 55.265625 

Q 40.578125 54.546875 44.28125 53.078125 

z

" id="DejaVuSans-115"/>

      <path d="M 30.609375 48.390625 

Q 23.390625 48.390625 19.1875 42.75 

Q 14.984375 37.109375 14.984375 27.296875 

Q 14.984375 17.484375 19.15625 11.84375 

Q 23.34375 6.203125 30.609375 6.203125 

Q 37.796875 6.203125 41.984375 11.859375 

Q 46.1875 17.53125 46.1875 27.296875 

Q 46.1875 37.015625 41.984375 42.703125 

Q 37.796875 48.390625 30.609375 48.390625 

z

M 30.609375 56 

Q 42.328125 56 49.015625 48.375 

Q 55.71875 40.765625 55.71875 27.296875 

Q 55.71875 13.875 49.015625 6.21875 

Q 42.328125 -1.421875 30.609375 -1.421875 

Q 18.84375 -1.421875 12.171875 6.21875 

Q 5.515625 13.875 5.515625 27.296875 

Q 5.515625 40.765625 12.171875 48.375 

Q 18.84375 56 30.609375 56 

z

" id="DejaVuSans-111"/>

      <path d="M 54.890625 33.015625 

L 54.890625 0 

L 45.90625 0 

L 45.90625 32.71875 

Q 45.90625 40.484375 42.875 44.328125 

Q 39.84375 48.1875 33.796875 48.1875 

Q 26.515625 48.1875 22.3125 43.546875 

Q 18.109375 38.921875 18.109375 30.90625 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-110"/>

     </defs>

     <g transform="translate(17.837812 171.043906)rotate(-90)scale(0.14 -0.14)">

      <use xlink:href="#DejaVuSans-76"/>

      <use x="55.712891" xlink:href="#DejaVuSans-105"/>

      <use x="83.496094" xlink:href="#DejaVuSans-102"/>

      <use x="118.701172" xlink:href="#DejaVuSans-101"/>

      <use x="180.224609" xlink:href="#DejaVuSans-32"/>

      <use x="212.011719" xlink:href="#DejaVuSans-115"/>

      <use x="264.111328" xlink:href="#DejaVuSans-97"/>

      <use x="325.390625" xlink:href="#DejaVuSans-116"/>

      <use x="364.599609" xlink:href="#DejaVuSans-105"/>

      <use x="392.382812" xlink:href="#DejaVuSans-115"/>

      <use x="444.482422" xlink:href="#DejaVuSans-102"/>

      <use x="479.6875" xlink:href="#DejaVuSans-97"/>

      <use x="540.966797" xlink:href="#DejaVuSans-99"/>

      <use x="595.947266" xlink:href="#DejaVuSans-116"/>

      <use x="635.15625" xlink:href="#DejaVuSans-105"/>

      <use x="662.939453" xlink:href="#DejaVuSans-111"/>

      <use x="724.121094" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="patch_3">

    <path d="M 50.833125 224.64 

L 50.833125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 385.633125 224.64 

L 385.633125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 50.833125 224.64 

L 385.633125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 50.833125 7.2 

L 385.633125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pb47d2f8981">

   <rect height="217.44" width="334.8" x="50.833125" y="7.2"/>

  </clipPath>

 </defs>

</svg>


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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Train the model</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
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
<span class="ansi-red-intense-fg ansi-bold">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-39-d56b524fad29&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold"># Train the model</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 2</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>model<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\sklearn\linear_model\_base.py</span> in <span class="ansi-cyan-fg">fit</span><span class="ansi-blue-intense-fg ansi-bold">(self, X, y, sample_weight)</span>
<span class="ansi-green-fg">    545</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    546</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>coef_<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_residues<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>rank_<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>singular_ <span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-red-fg"> </span><span class="ansi-red-fg">\</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 547</span><span class="ansi-yellow-intense-fg ansi-bold">                 </span>linalg<span class="ansi-yellow-intense-fg ansi-bold">.</span>lstsq<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    548</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>coef_ <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>coef_<span class="ansi-yellow-intense-fg ansi-bold">.</span>T
<span class="ansi-green-fg">    549</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\scipy\linalg\basic.py</span> in <span class="ansi-cyan-fg">lstsq</span><span class="ansi-blue-intense-fg ansi-bold">(a, b, cond, overwrite_a, overwrite_b, check_finite, lapack_driver)</span>
<span class="ansi-green-fg">   1223</span>             <span class="ansi-green-intense-fg ansi-bold">raise</span> LinAlgError<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;SVD did not converge in Linear Least Squares&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1224</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> info <span class="ansi-yellow-intense-fg ansi-bold">&lt;</span> <span class="ansi-cyan-intense-fg ansi-bold">0</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1225</span><span class="ansi-yellow-intense-fg ansi-bold">             raise ValueError(&#39;illegal value in %d-th argument of internal %s&#39;
</span><span class="ansi-green-fg">   1226</span>                              % (-info, lapack_driver))
<span class="ansi-green-fg">   1227</span>         resids <span class="ansi-yellow-intense-fg ansi-bold">=</span> np<span class="ansi-yellow-intense-fg ansi-bold">.</span>asarray<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> dtype<span class="ansi-yellow-intense-fg ansi-bold">=</span>x<span class="ansi-yellow-intense-fg ansi-bold">.</span>dtype<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-red-intense-fg ansi-bold">ValueError</span>: illegal value in 4-th argument of internal None</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Make a prediction for Cyprus</span>
<span class="n">X_new</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">22587</span><span class="p">]]</span>  <span class="c1"># Cyprus&#39; GDP per capita</span>
<span class="nb">print</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_new</span><span class="p">))</span> <span class="c1"># outputs [[ 5.96242338]]</span>
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
<span class="ansi-red-intense-fg ansi-bold">AttributeError</span>                            Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-40-025ceefc2d44&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold"># Make a prediction for Cyprus</span>
<span class="ansi-green-fg">      2</span> X_new <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">22587</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">]</span>  <span class="ansi-red-intense-fg ansi-bold"># Cyprus&#39; GDP per capita</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 3</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>print<span class="ansi-yellow-intense-fg ansi-bold">(</span>model<span class="ansi-yellow-intense-fg ansi-bold">.</span>predict<span class="ansi-yellow-intense-fg ansi-bold">(</span>X_new<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-red-intense-fg ansi-bold"># outputs [[ 5.96242338]]</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\sklearn\linear_model\_base.py</span> in <span class="ansi-cyan-fg">predict</span><span class="ansi-blue-intense-fg ansi-bold">(self, X)</span>
<span class="ansi-green-fg">    234</span>             Returns predicted values<span class="ansi-yellow-intense-fg ansi-bold">.</span>
<span class="ansi-green-fg">    235</span>         &#34;&#34;&#34;
<span class="ansi-green-intense-fg ansi-bold">--&gt; 236</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_decision_function<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    237</span> 
<span class="ansi-green-fg">    238</span>     _preprocess_data <span class="ansi-yellow-intense-fg ansi-bold">=</span> staticmethod<span class="ansi-yellow-intense-fg ansi-bold">(</span>_preprocess_data<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\sklearn\linear_model\_base.py</span> in <span class="ansi-cyan-fg">_decision_function</span><span class="ansi-blue-intense-fg ansi-bold">(self, X)</span>
<span class="ansi-green-fg">    217</span> 
<span class="ansi-green-fg">    218</span>         X <span class="ansi-yellow-intense-fg ansi-bold">=</span> check_array<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> accept_sparse<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-blue-intense-fg ansi-bold">&#39;csr&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;csc&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;coo&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 219</span><span class="ansi-yellow-intense-fg ansi-bold">         return safe_sparse_dot(X, self.coef_.T,
</span><span class="ansi-green-fg">    220</span>                                dense_output=True) + self.intercept_
<span class="ansi-green-fg">    221</span> 

<span class="ansi-red-intense-fg ansi-bold">AttributeError</span>: &#39;LinearRegression&#39; object has no attribute &#39;coef_&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span> <span class="o">=</span> <span class="n">backup</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">missing_data</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">position_text2</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;Brazil&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">1000</span><span class="p">,</span> <span class="mf">9.0</span><span class="p">),</span>
    <span class="s2">&quot;Mexico&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">11000</span><span class="p">,</span> <span class="mf">9.0</span><span class="p">),</span>
    <span class="s2">&quot;Chile&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">25000</span><span class="p">,</span> <span class="mf">9.0</span><span class="p">),</span>
    <span class="s2">&quot;Czech Republic&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">35000</span><span class="p">,</span> <span class="mf">9.0</span><span class="p">),</span>
    <span class="s2">&quot;Norway&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">60000</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span>
    <span class="s2">&quot;Switzerland&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">72000</span><span class="p">,</span> <span class="mf">3.0</span><span class="p">),</span>
    <span class="s2">&quot;Luxembourg&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">90000</span><span class="p">,</span> <span class="mf">3.0</span><span class="p">),</span>
<span class="p">}</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>

<span class="k">for</span> <span class="n">country</span><span class="p">,</span> <span class="n">pos_text</span> <span class="ow">in</span> <span class="n">position_text2</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span> <span class="o">=</span> <span class="n">missing_data</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">country</span><span class="p">]</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">annotate</span><span class="p">(</span><span class="n">country</span><span class="p">,</span> <span class="n">xy</span><span class="o">=</span><span class="p">(</span><span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span><span class="p">),</span> <span class="n">xytext</span><span class="o">=</span><span class="n">pos_text</span><span class="p">,</span>
            <span class="n">arrowprops</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">facecolor</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">shrink</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="n">head123width</span><span class="o">=</span><span class="mi">5</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">pos_data_x</span><span class="p">,</span> <span class="n">pos_data_y</span><span class="p">,</span> <span class="s2">&quot;rs&quot;</span><span class="p">)</span>

<span class="n">X</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0</span> <span class="o">+</span> <span class="n">t1</span><span class="o">*</span><span class="n">X</span><span class="p">,</span> <span class="s2">&quot;b:&quot;</span><span class="p">)</span>

<span class="n">lin_reg_full</span> <span class="o">=</span> <span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">Xfull</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">full_country_stats</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">yfull</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">full_country_stats</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>
<span class="n">lin_reg_full</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">Xfull</span><span class="p">,</span> <span class="n">yfull</span><span class="p">)</span>

<span class="n">t0full</span><span class="p">,</span> <span class="n">t1full</span> <span class="o">=</span> <span class="n">lin_reg_full</span><span class="o">.</span><span class="n">intercept_</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">lin_reg_full</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0full</span> <span class="o">+</span> <span class="n">t1full</span> <span class="o">*</span> <span class="n">X</span><span class="p">,</span> <span class="s2">&quot;k&quot;</span><span class="p">)</span>

<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;representative_training_data_scatterplot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>

<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">preprocessing</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">pipeline</span>

<span class="n">poly</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">PolynomialFeatures</span><span class="p">(</span><span class="n">degree</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span> <span class="n">include_bias</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">lin_reg2</span> <span class="o">=</span> <span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>

<span class="n">pipeline_reg</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">Pipeline</span><span class="p">([(</span><span class="s1">&#39;poly&#39;</span><span class="p">,</span> <span class="n">poly</span><span class="p">),</span> <span class="p">(</span><span class="s1">&#39;scal&#39;</span><span class="p">,</span> <span class="n">scaler</span><span class="p">),</span> <span class="p">(</span><span class="s1">&#39;lin&#39;</span><span class="p">,</span> <span class="n">lin_reg2</span><span class="p">)])</span>
<span class="n">pipeline_reg</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">Xfull</span><span class="p">,</span> <span class="n">yfull</span><span class="p">)</span>
<span class="n">curve</span> <span class="o">=</span> <span class="n">pipeline_reg</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X</span><span class="p">[:,</span> <span class="n">np</span><span class="o">.</span><span class="n">newaxis</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">curve</span><span class="p">)</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;overfitting_model_plot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span><span class="o">.</span><span class="n">loc</span><span class="p">[[</span><span class="n">c</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">full_country_stats</span><span class="o">.</span><span class="n">index</span> <span class="k">if</span> <span class="s2">&quot;W&quot;</span> <span class="ow">in</span> <span class="n">c</span><span class="o">.</span><span class="n">upper</span><span class="p">()]][</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">loc</span><span class="p">[[</span><span class="n">c</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">gdp_per_capita</span><span class="o">.</span><span class="n">index</span> <span class="k">if</span> <span class="s2">&quot;W&quot;</span> <span class="ow">in</span> <span class="n">c</span><span class="o">.</span><span class="n">upper</span><span class="p">()]]</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]),</span> <span class="nb">list</span><span class="p">(</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]),</span> <span class="s2">&quot;bo&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">missing_data</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]),</span> <span class="nb">list</span><span class="p">(</span><span class="n">missing_data</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]),</span> <span class="s2">&quot;rs&quot;</span><span class="p">)</span>

<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0full</span> <span class="o">+</span> <span class="n">t1full</span> <span class="o">*</span> <span class="n">X</span><span class="p">,</span> <span class="s2">&quot;r--&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Linear model on all data&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0</span> <span class="o">+</span> <span class="n">t1</span><span class="o">*</span><span class="n">X</span><span class="p">,</span> <span class="s2">&quot;b:&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Linear model on partial data&quot;</span><span class="p">)</span>

<span class="n">ridge</span> <span class="o">=</span> <span class="n">linear_model</span><span class="o">.</span><span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mi">10</span><span class="o">**</span><span class="mf">9.5</span><span class="p">)</span>
<span class="n">Xsample</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">ysample</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">sample_data</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>
<span class="n">ridge</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">Xsample</span><span class="p">,</span> <span class="n">ysample</span><span class="p">)</span>
<span class="n">t0ridge</span><span class="p">,</span> <span class="n">t1ridge</span> <span class="o">=</span> <span class="n">ridge</span><span class="o">.</span><span class="n">intercept_</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">ridge</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0ridge</span> <span class="o">+</span> <span class="n">t1ridge</span> <span class="o">*</span> <span class="n">X</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Regularized linear model on partial data&quot;</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="s2">&quot;lower right&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">110000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;ridge_model_plot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">backup</span> <span class="o">=</span> <span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span>

<span class="k">def</span> <span class="nf">prepare_country_stats</span><span class="p">(</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">gdp_per_capita</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">sample_data</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Replace this linear model:</span>
<span class="kn">import</span> <span class="nn">sklearn.linear_model</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">sklearn</span><span class="o">.</span><span class="n">linear_model</span><span class="o">.</span><span class="n">LinearRegression</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># with this k-neighbors regression model:</span>
<span class="kn">import</span> <span class="nn">sklearn.neighbors</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">sklearn</span><span class="o">.</span><span class="n">neighbors</span><span class="o">.</span><span class="n">KNeighborsRegressor</span><span class="p">(</span><span class="n">n_neighbors</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">]]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">c_</span><span class="p">[</span><span class="n">country_stats</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]]</span>

<span class="c1"># Train the model</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

<span class="c1"># Make a prediction for Cyprus</span>
<span class="n">X_new</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="mf">22587.0</span><span class="p">]])</span>  <span class="c1"># Cyprus&#39; GDP per capita</span>
<span class="nb">print</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_new</span><span class="p">))</span> <span class="c1"># outputs [[ 5.76666667]]</span>
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
 

