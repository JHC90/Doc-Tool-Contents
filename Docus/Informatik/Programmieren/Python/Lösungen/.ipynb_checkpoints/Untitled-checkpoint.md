<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39;&#39;&#39;</span>
<span class="sd">{</span>
<span class="sd">&quot;title&quot;: &quot;Train-Validation-Test-Split&quot;,</span>
<span class="sd">&quot;keywords&quot;: &quot;SK-Learn&quot;,</span>
<span class="sd">&quot;categories&quot;: &quot;&quot;,</span>
<span class="sd">&quot;description&quot;: &quot;hier werden die Möglihckeiten gelitste wie man ein Train Test split vollziehen kann&quot;,</span>
<span class="sd">&quot;level&quot;: &quot;40&quot;,</span>
<span class="sd">&quot;pageID&quot;: &quot;16112020-TrainTestSplit-Implementation&quot;</span>
<span class="sd">}</span>
<span class="sd">&#39;&#39;&#39;</span><span class="s1">&#39;&#39;</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[1]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\&#39;\&#39;\n{\n&#34;title&#34;: &#34;Train-Validation-Test-Split&#34;,\n&#34;keywords&#34;: &#34;SK-Learn&#34;,\n&#34;categories&#34;: &#34;&#34;,\n&#34;description&#34;: &#34;hier werden die Möglihckeiten gelitste wie man ein Train Test split vollziehen kann&#34;,\n&#34;level&#34;: &#34;40&#34;,\n&#34;pageID&#34;: &#34;14112020-10-California-Housing&#34;\n}\n&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Train-Test-Split">Train Test Split<a class="anchor-link" href="#Train-Test-Split">&#182;</a></h1><p>Die Theorie zu den Train-Test-Validation-Datensätzen wird <a href="07112020200718-Data">hier</a> erklärt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">HOUSING_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;housing&quot;</span><span class="p">)</span>
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

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(20640, 10)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Split mit Numpy, Manuelle erstellung</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="k">def</span> <span class="nf">split_train_test</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">):</span>
    <span class="n">shuffled_indices</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">permutation</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
    <span class="n">test_set_size</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span> <span class="o">*</span> <span class="n">test_ratio</span><span class="p">)</span>
    <span class="n">test_indices</span> <span class="o">=</span> <span class="n">shuffled_indices</span><span class="p">[:</span><span class="n">test_set_size</span><span class="p">]</span>
    <span class="n">train_indices</span> <span class="o">=</span> <span class="n">shuffled_indices</span><span class="p">[</span><span class="n">test_set_size</span><span class="p">:]</span>
    <span class="k">return</span> <span class="n">data</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">train_indices</span><span class="p">],</span> <span class="n">data</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">test_indices</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Split mit SK-Learn</span>
<span class="n">train_set</span><span class="p">,</span> <span class="n">test_set</span> <span class="o">=</span> <span class="n">split_train_test</span><span class="p">(</span><span class="n">housing</span><span class="p">,</span> <span class="mf">0.2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">train_set</span><span class="p">),</span> <span class="s2">&quot;train +&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">test_set</span><span class="p">),</span> <span class="s2">&quot;test&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>16512 train + 4128 test
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">zlib</span> <span class="kn">import</span> <span class="n">crc32</span>

<span class="k">def</span> <span class="nf">test_set_check</span><span class="p">(</span><span class="n">identifier</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">crc32</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int64</span><span class="p">(</span><span class="n">identifier</span><span class="p">))</span> <span class="o">&amp;</span> <span class="mh">0xffffffff</span> <span class="o">&lt;</span> <span class="n">test_ratio</span> <span class="o">*</span> <span class="mi">2</span><span class="o">**</span><span class="mi">32</span>

<span class="k">def</span> <span class="nf">split_train_test_by_id</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">,</span> <span class="n">id_column</span><span class="p">):</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">id_column</span><span class="p">]</span>
    <span class="n">in_test_set</span> <span class="o">=</span> <span class="n">ids</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">id_</span><span class="p">:</span> <span class="n">test_set_check</span><span class="p">(</span><span class="n">id_</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">data</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="o">~</span><span class="n">in_test_set</span><span class="p">],</span> <span class="n">data</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">in_test_set</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">hashlib</span>

<span class="k">def</span> <span class="nf">test_set_check</span><span class="p">(</span><span class="n">identifier</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">,</span> <span class="nb">hash</span><span class="o">=</span><span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int64</span><span class="p">(</span><span class="n">identifier</span><span class="p">))</span><span class="o">.</span><span class="n">digest</span><span class="p">()[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">256</span> <span class="o">*</span> <span class="n">test_ratio</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">test_set_check</span><span class="p">(</span><span class="n">identifier</span><span class="p">,</span> <span class="n">test_ratio</span><span class="p">,</span> <span class="nb">hash</span><span class="o">=</span><span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">bytearray</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int64</span><span class="p">(</span><span class="n">identifier</span><span class="p">))</span><span class="o">.</span><span class="n">digest</span><span class="p">())[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">256</span> <span class="o">*</span> <span class="n">test_ratio</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_with_id</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>   <span class="c1"># adds an `index` column</span>
<span class="n">train_set</span><span class="p">,</span> <span class="n">test_set</span> <span class="o">=</span> <span class="n">split_train_test_by_id</span><span class="p">(</span><span class="n">housing_with_id</span><span class="p">,</span> <span class="mf">0.2</span><span class="p">,</span> <span class="s2">&quot;index&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_with_id</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">housing</span><span class="p">[</span><span class="s2">&quot;longitude&quot;</span><span class="p">]</span> <span class="o">*</span> <span class="mi">1000</span> <span class="o">+</span> <span class="n">housing</span><span class="p">[</span><span class="s2">&quot;latitude&quot;</span><span class="p">]</span>
<span class="n">train_set</span><span class="p">,</span> <span class="n">test_set</span> <span class="o">=</span> <span class="n">split_train_test_by_id</span><span class="p">(</span><span class="n">housing_with_id</span><span class="p">,</span> <span class="mf">0.2</span><span class="p">,</span> <span class="s2">&quot;id&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test_set</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>



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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
      <th>id</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>-122.26</td>
      <td>37.84</td>
      <td>42.0</td>
      <td>2555.0</td>
      <td>665.0</td>
      <td>1206.0</td>
      <td>595.0</td>
      <td>2.0804</td>
      <td>226700.0</td>
      <td>NEAR BAY</td>
      <td>-122222.16</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2202.0</td>
      <td>434.0</td>
      <td>910.0</td>
      <td>402.0</td>
      <td>3.2031</td>
      <td>281500.0</td>
      <td>NEAR BAY</td>
      <td>-122222.15</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>3503.0</td>
      <td>752.0</td>
      <td>1504.0</td>
      <td>734.0</td>
      <td>3.2705</td>
      <td>241800.0</td>
      <td>NEAR BAY</td>
      <td>-122222.15</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2491.0</td>
      <td>474.0</td>
      <td>1098.0</td>
      <td>468.0</td>
      <td>3.0750</td>
      <td>213500.0</td>
      <td>NEAR BAY</td>
      <td>-122222.15</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>-122.26</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>696.0</td>
      <td>191.0</td>
      <td>345.0</td>
      <td>174.0</td>
      <td>2.6736</td>
      <td>191300.0</td>
      <td>NEAR BAY</td>
      <td>-122222.16</td>
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
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># SK-Learn</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>

<span class="n">train_set</span><span class="p">,</span> <span class="n">test_set</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">housing</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">test_set</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>



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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>20046</th>
      <td>-119.01</td>
      <td>36.06</td>
      <td>25.0</td>
      <td>1505.0</td>
      <td>NaN</td>
      <td>1392.0</td>
      <td>359.0</td>
      <td>1.6812</td>
      <td>47700.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>3024</th>
      <td>-119.46</td>
      <td>35.14</td>
      <td>30.0</td>
      <td>2943.0</td>
      <td>NaN</td>
      <td>1565.0</td>
      <td>584.0</td>
      <td>2.5313</td>
      <td>45800.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>15663</th>
      <td>-122.44</td>
      <td>37.80</td>
      <td>52.0</td>
      <td>3830.0</td>
      <td>NaN</td>
      <td>1310.0</td>
      <td>963.0</td>
      <td>3.4801</td>
      <td>500001.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>20484</th>
      <td>-118.72</td>
      <td>34.28</td>
      <td>17.0</td>
      <td>3051.0</td>
      <td>NaN</td>
      <td>1705.0</td>
      <td>495.0</td>
      <td>5.7376</td>
      <td>218600.0</td>
      <td>&lt;1H OCEAN</td>
    </tr>
    <tr>
      <th>9814</th>
      <td>-121.93</td>
      <td>36.62</td>
      <td>34.0</td>
      <td>2351.0</td>
      <td>NaN</td>
      <td>1063.0</td>
      <td>428.0</td>
      <td>3.7250</td>
      <td>278000.0</td>
      <td>NEAR OCEAN</td>
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
<h1 id="Straatified-Sampling">Straatified Sampling<a class="anchor-link" href="#Straatified-Sampling">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span><span class="p">[</span><span class="s2">&quot;median_income&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x167045697c0&gt;</pre>
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
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">cut</span><span class="p">(</span><span class="n">housing</span><span class="p">[</span><span class="s2">&quot;median_income&quot;</span><span class="p">],</span>
                               <span class="n">bins</span><span class="o">=</span><span class="p">[</span><span class="mf">0.</span><span class="p">,</span> <span class="mf">1.5</span><span class="p">,</span> <span class="mf">3.0</span><span class="p">,</span> <span class="mf">4.5</span><span class="p">,</span> <span class="mf">6.</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">inf</span><span class="p">],</span>
                               <span class="n">labels</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="n">housing</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>3    7236
2    6581
4    3639
5    2362
1     822
Name: income_cat, dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">StratifiedShuffleSplit</span>

<span class="n">split</span> <span class="o">=</span> <span class="n">StratifiedShuffleSplit</span><span class="p">(</span><span class="n">n_splits</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
<span class="k">for</span> <span class="n">train_index</span><span class="p">,</span> <span class="n">test_index</span> <span class="ow">in</span> <span class="n">split</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">housing</span><span class="p">,</span> <span class="n">housing</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]):</span>
    <span class="n">strat_train_set</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">train_index</span><span class="p">]</span>
    <span class="n">strat_test_set</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">test_index</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">strat_test_set</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">strat_test_set</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[19]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>3    0.350533
2    0.318798
4    0.176357
5    0.114583
1    0.039729
Name: income_cat, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">housing</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>3    0.350581
2    0.318847
4    0.176308
5    0.114438
1    0.039826
Name: income_cat, dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">income_cat_proportions</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;income_cat&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="n">train_set</span><span class="p">,</span> <span class="n">test_set</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">housing</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>

<span class="n">compare_props</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
    <span class="s2">&quot;Overall&quot;</span><span class="p">:</span> <span class="n">income_cat_proportions</span><span class="p">(</span><span class="n">housing</span><span class="p">),</span>
    <span class="s2">&quot;Stratified&quot;</span><span class="p">:</span> <span class="n">income_cat_proportions</span><span class="p">(</span><span class="n">strat_test_set</span><span class="p">),</span>
    <span class="s2">&quot;Random&quot;</span><span class="p">:</span> <span class="n">income_cat_proportions</span><span class="p">(</span><span class="n">test_set</span><span class="p">),</span>
<span class="p">})</span><span class="o">.</span><span class="n">sort_index</span><span class="p">()</span>
<span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Rand. </span><span class="si">%e</span><span class="s2">rror&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span> <span class="o">*</span> <span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Random&quot;</span><span class="p">]</span> <span class="o">/</span> <span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Overall&quot;</span><span class="p">]</span> <span class="o">-</span> <span class="mi">100</span>
<span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Strat. </span><span class="si">%e</span><span class="s2">rror&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span> <span class="o">*</span> <span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Stratified&quot;</span><span class="p">]</span> <span class="o">/</span> <span class="n">compare_props</span><span class="p">[</span><span class="s2">&quot;Overall&quot;</span><span class="p">]</span> <span class="o">-</span> <span class="mi">100</span>
<span class="n">compare_props</span>
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
      <th></th>
      <th>Overall</th>
      <th>Stratified</th>
      <th>Random</th>
      <th>Rand. %error</th>
      <th>Strat. %error</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>1</th>
      <td>0.039826</td>
      <td>0.039729</td>
      <td>0.040213</td>
      <td>0.973236</td>
      <td>-0.243309</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.318847</td>
      <td>0.318798</td>
      <td>0.324370</td>
      <td>1.732260</td>
      <td>-0.015195</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.350581</td>
      <td>0.350533</td>
      <td>0.358527</td>
      <td>2.266446</td>
      <td>-0.013820</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.176308</td>
      <td>0.176357</td>
      <td>0.167393</td>
      <td>-5.056334</td>
      <td>0.027480</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.114438</td>
      <td>0.114583</td>
      <td>0.109496</td>
      <td>-4.318374</td>
      <td>0.127011</td>
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
 

