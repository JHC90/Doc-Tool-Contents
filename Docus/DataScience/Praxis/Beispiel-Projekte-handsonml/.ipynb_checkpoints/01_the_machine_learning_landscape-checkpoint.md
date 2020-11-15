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
<p><a href="https://www.google.de/">TestLink-Google</a><br>
<a href="...../Docus/DataScience/Theorie/000_AI_ML_DL.md">TestLink-Internal</a><br>
<a href="./../../../../index.md">link-index</a><br>
<a href="./../../../../about.md">link-about</a><br>
<a href="./../../../Informatik/Web-Development/CSS/01_CSS_Basics.md">link-css</a><br>
<a href="./../../../../Projekte/00_Doc-Tool/Ideen-Container/00_SwitchMarkdownHtml%20copy.md">link-doctool</a><br></p>

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
<div class="prompt input_prompt">In&nbsp;[1]:</div>
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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
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
<div class="prompt input_prompt">In&nbsp;[3]:</div>
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
<div class="prompt input_prompt">In&nbsp;[4]:</div>
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

<span class="c1"># Train the model</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

<span class="c1"># Make a prediction for Cyprus</span>
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




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-4-1ae6d5bba27c&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">     23</span> 
<span class="ansi-green-fg">     24</span> <span class="ansi-red-intense-fg ansi-bold"># Train the model</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 25</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>model<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">     26</span> 
<span class="ansi-green-fg">     27</span> <span class="ansi-red-intense-fg ansi-bold"># Make a prediction for Cyprus</span>

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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
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
<h1 id="Note:-you-can-ignore-the-rest-of-this-notebook,-it-just-generates-many-of-the-figure123s-in-chapter-1.">Note: you can ignore the rest of this notebook, it just generates many of the figure123s in chapter 1.<a class="anchor-link" href="#Note:-you-can-ignore-the-rest-of-this-notebook,-it-just-generates-many-of-the-figure123s-in-chapter-1.">&#182;</a></h1>
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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
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

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">oecd_bli</span><span class="p">[</span><span class="s2">&quot;Life satisfaction&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
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

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">left</span><span class="o">=</span><span class="n">oecd_bli</span><span class="p">,</span> <span class="n">right</span><span class="o">=</span><span class="n">gdp_per_capita</span><span class="p">,</span> <span class="n">left_index</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">right_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">full_country_stats</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">full_country_stats</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">full_country_stats</span><span class="p">[[</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="s1">&#39;Life satisfaction&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="s2">&quot;United States&quot;</span><span class="p">]</span>
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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;GDP per capita&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">&#39;Life satisfaction&#39;</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">),</span> <span class="n">s</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">X</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">t0</span> <span class="o">+</span> <span class="n">t1</span><span class="o">*</span><span class="n">X</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">60000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">7.5</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_0 = 4.85$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">5000</span><span class="p">,</span> <span class="mf">6.6</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;$\theta_1 = 4.91 \times 10^{-5}$&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">([</span><span class="n">cyprus_gdp_per_capita</span><span class="p">,</span> <span class="n">cyprus_gdp_per_capita</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="n">cyprus_predicted_life_satisfaction</span><span class="p">],</span> <span class="s2">&quot;r--&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">25000</span><span class="p">,</span> <span class="mf">5.0</span><span class="p">,</span> <span class="sa">r</span><span class="s2">&quot;Prediction = 5.96&quot;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">cyprus_gdp_per_capita</span><span class="p">,</span> <span class="n">cyprus_predicted_life_satisfaction</span><span class="p">,</span> <span class="s2">&quot;ro&quot;</span><span class="p">)</span>
<span class="n">save_fig</span><span class="p">(</span><span class="s1">&#39;cyprus_prediction_plot&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sample_data</span><span class="p">[</span><span class="mi">7</span><span class="p">:</span><span class="mi">10</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">(</span><span class="mf">5.1</span><span class="o">+</span><span class="mf">5.7</span><span class="o">+</span><span class="mf">6.5</span><span class="p">)</span><span class="o">/</span><span class="mi">3</span>
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
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
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

<span class="c1"># Train the model</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

<span class="c1"># Make a prediction for Cyprus</span>
<span class="n">X_new</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">22587</span><span class="p">]]</span>  <span class="c1"># Cyprus&#39; GDP per capita</span>
<span class="nb">print</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_new</span><span class="p">))</span> <span class="c1"># outputs [[ 5.96242338]]</span>
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
 

