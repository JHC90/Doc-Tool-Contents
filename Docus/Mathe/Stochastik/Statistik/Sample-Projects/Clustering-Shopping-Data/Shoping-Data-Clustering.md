<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Shopping-Example">Shopping-Example<a class="anchor-link" href="#Shopping-Example">&#182;</a></h1><p>hier ein Beispiel zum Clustering
<a href="https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/">https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/</a></p>
<p>konkret werden hier in diesem Beispiel Kundengruppen geclustert.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Bibs</span>
<span class="kn">import</span> <span class="nn">requests</span>
<span class="kn">import</span> <span class="nn">csv</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Data-download-&amp;-einlesen">Data download &amp; einlesen<a class="anchor-link" href="#Data-download-&amp;-einlesen">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Starting...&#39;</span><span class="p">)</span>
<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;https://stackabuse.s3.amazonaws.com/files/hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv&#39;</span> <span class="c1"># =&gt; Checken ob die Datei bereits vorliegt oder nicht</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;./data/shopping-data.csv&quot;</span>
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
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">customer_data</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/shopping-data.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">customer_data</span><span class="o">.</span><span class="n">head123</span><span class="p">())</span>
<span class="n">customer_data</span><span class="o">.</span><span class="n">columns</span>
<span class="c1">#customer_data.shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   CustomerID   Genre  Age  Annual Income (k$)  Spending Score (1-100)
0           1    Male   19                  15                      39
1           2    Male   21                  15                      81
2           3  Female   20                  16                       6
3           4  Female   23                  16                      77
4           5  Female   31                  17                      40
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[35]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;CustomerID&#39;, &#39;Genre&#39;, &#39;Age&#39;, &#39;Annual Income (k$)&#39;,
       &#39;Spending Score (1-100)&#39;],
      dtype=&#39;object&#39;)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># weiteres EDA überspring ich an dieser Stelle, ist hier auch nicht wirklich wichtig</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Modelling-auf-2d">Modelling auf 2d<a class="anchor-link" href="#Modelling-auf-2d">&#182;</a></h2><p>2d bedeutet in diesem Fall dass die PCA auf zwei feature ausgeführt wird (vgl x&amp;y im Kartesischen), in diesem konkreten Beispiel mache wir das mnit annual income &amp; spending Score</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="n">customer_data</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span> <span class="mi">3</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="nb">print</span><span class="p">((</span><span class="n">data</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[ 15  39]
 [ 15  81]
 [ 16   6]
 [ 16  77]
 [ 17  40]
 [ 17  76]
 [ 18   6]
 [ 18  94]
 [ 19   3]
 [ 19  72]
 [ 19  14]
 [ 19  99]
 [ 20  15]
 [ 20  77]
 [ 20  13]
 [ 20  79]
 [ 21  35]
 [ 21  66]
 [ 23  29]
 [ 23  98]
 [ 24  35]
 [ 24  73]
 [ 25   5]
 [ 25  73]
 [ 28  14]
 [ 28  82]
 [ 28  32]
 [ 28  61]
 [ 29  31]
 [ 29  87]
 [ 30   4]
 [ 30  73]
 [ 33   4]
 [ 33  92]
 [ 33  14]
 [ 33  81]
 [ 34  17]
 [ 34  73]
 [ 37  26]
 [ 37  75]
 [ 38  35]
 [ 38  92]
 [ 39  36]
 [ 39  61]
 [ 39  28]
 [ 39  65]
 [ 40  55]
 [ 40  47]
 [ 40  42]
 [ 40  42]
 [ 42  52]
 [ 42  60]
 [ 43  54]
 [ 43  60]
 [ 43  45]
 [ 43  41]
 [ 44  50]
 [ 44  46]
 [ 46  51]
 [ 46  46]
 [ 46  56]
 [ 46  55]
 [ 47  52]
 [ 47  59]
 [ 48  51]
 [ 48  59]
 [ 48  50]
 [ 48  48]
 [ 48  59]
 [ 48  47]
 [ 49  55]
 [ 49  42]
 [ 50  49]
 [ 50  56]
 [ 54  47]
 [ 54  54]
 [ 54  53]
 [ 54  48]
 [ 54  52]
 [ 54  42]
 [ 54  51]
 [ 54  55]
 [ 54  41]
 [ 54  44]
 [ 54  57]
 [ 54  46]
 [ 57  58]
 [ 57  55]
 [ 58  60]
 [ 58  46]
 [ 59  55]
 [ 59  41]
 [ 60  49]
 [ 60  40]
 [ 60  42]
 [ 60  52]
 [ 60  47]
 [ 60  50]
 [ 61  42]
 [ 61  49]
 [ 62  41]
 [ 62  48]
 [ 62  59]
 [ 62  55]
 [ 62  56]
 [ 62  42]
 [ 63  50]
 [ 63  46]
 [ 63  43]
 [ 63  48]
 [ 63  52]
 [ 63  54]
 [ 64  42]
 [ 64  46]
 [ 65  48]
 [ 65  50]
 [ 65  43]
 [ 65  59]
 [ 67  43]
 [ 67  57]
 [ 67  56]
 [ 67  40]
 [ 69  58]
 [ 69  91]
 [ 70  29]
 [ 70  77]
 [ 71  35]
 [ 71  95]
 [ 71  11]
 [ 71  75]
 [ 71   9]
 [ 71  75]
 [ 72  34]
 [ 72  71]
 [ 73   5]
 [ 73  88]
 [ 73   7]
 [ 73  73]
 [ 74  10]
 [ 74  72]
 [ 75   5]
 [ 75  93]
 [ 76  40]
 [ 76  87]
 [ 77  12]
 [ 77  97]
 [ 77  36]
 [ 77  74]
 [ 78  22]
 [ 78  90]
 [ 78  17]
 [ 78  88]
 [ 78  20]
 [ 78  76]
 [ 78  16]
 [ 78  89]
 [ 78   1]
 [ 78  78]
 [ 78   1]
 [ 78  73]
 [ 79  35]
 [ 79  83]
 [ 81   5]
 [ 81  93]
 [ 85  26]
 [ 85  75]
 [ 86  20]
 [ 86  95]
 [ 87  27]
 [ 87  63]
 [ 87  13]
 [ 87  75]
 [ 87  10]
 [ 87  92]
 [ 88  13]
 [ 88  86]
 [ 88  15]
 [ 88  69]
 [ 93  14]
 [ 93  90]
 [ 97  32]
 [ 97  86]
 [ 98  15]
 [ 98  88]
 [ 99  39]
 [ 99  97]
 [101  24]
 [101  68]
 [103  17]
 [103  85]
 [103  23]
 [103  69]
 [113   8]
 [113  91]
 [120  16]
 [120  79]
 [126  28]
 [126  74]
 [137  18]
 [137  83]]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">scipy.cluster.hierarchy</span> <span class="k">as</span> <span class="nn">shc</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Customer Dendograms&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Customers&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Euclidean distances&#39;</span><span class="p">)</span>
<span class="n">dend</span> <span class="o">=</span> <span class="n">shc</span><span class="o">.</span><span class="n">dendrogram</span><span class="p">(</span><span class="n">shc</span><span class="o">.</span><span class="n">linkage</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="s1">&#39;ward&#39;</span><span class="p">))</span>
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

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>sehe ich dass die längsten Cuts zwischen blau und rot bzw türkis laufen. Ich follge dem Sting in diesem fall soweit wie möglich weg vom Ursrpung (hier nach unten, kurz vor rot &amp; Türkis). dort setzte ich den Cut durch</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">## Sklearn for number of Clusters</span>
<span class="kn">from</span> <span class="nn">sklearn.cluster</span> <span class="kn">import</span> <span class="n">AgglomerativeClustering</span> 
<span class="n">cluster</span> <span class="o">=</span> <span class="n">AgglomerativeClustering</span><span class="p">(</span><span class="n">n_clusters</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">affinity</span><span class="o">=</span><span class="s1">&#39;euclidean&#39;</span><span class="p">,</span> <span class="n">linkage</span><span class="o">=</span><span class="s1">&#39;ward&#39;</span><span class="p">)</span>
<span class="n">cluster</span><span class="o">.</span><span class="n">fit_predict</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[38]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3,
       4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1,
       4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 0, 2, 0, 2,
       1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2,
       0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2,
       0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2,
       0, 2], dtype=int64)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span> <span class="n">data</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span> <span class="n">c</span><span class="o">=</span><span class="n">cluster</span><span class="o">.</span><span class="n">labels_</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;rainbow&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[39]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x179df402160&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlYAAAI/CAYAAAC1XpeNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nOzdeXxcZ3n3/899ZtFqyZIlebe8b3G8KokTsi8QCJSlLUvDUkohLRRa2gcK9FcoLRT6FPp7+vo9D31KWQokJYSlhC1A9sVJnNiJndiO992WLMnat9nO/fvjyI6WM7KW0ZzR6PvOyy9FZ2bOuWYsj6657+u+bmOtRUREREQmzgk6ABEREZF8ocRKREREJEOUWImIiIhkiBIrERERkQxRYiUiIiKSIUqsRERERDIkHHQAAFVVVXbx4sVBhyEiIiJySTt37my21lb73ZYTidXixYvZsWNH0GGIiIiIXJIx5kS62zQVKCIiIpIhSqxEREREMkSJlYiIiEiGKLESERERyRAlViIiIiIZosRKREREJEOUWImIiIhkiBIrERERkQxRYiUiIiKSIUqsRERERDJEiZWIiIhIhiixEhEREckQJVYiIiIiGaLESkRERCRDLplYGWO+ZYxpNMbsGXCs0hjzoDHmUP/XigG3fdoYc9gYc8AY87rJClxEREQk14xmxOo/gduHHPsU8LC1dgXwcP/3GGPWAu8ELut/zNeMMaGMRSsiIiKSwy6ZWFlrnwBahhx+M/Cd/v//DvCWAcfvtdbGrLXHgMPAlRmKVURERCSnjbfGara1th6g/2tN//H5wKkB9zvdf0xEREQk72W6eN34HLO+dzTmQ8aYHcaYHU1NTRkOQ0RERCT7xptYnTPGzAXo/9rYf/w0sHDA/RYAZ/1OYK39urW2zlpbV11dPc4wsiTWAUd+DXvugbPPg5sMOiIRERHJQeFxPu5nwPuAL/d/vX/A8f8yxvwLMA9YATw30SAD1XYUnvlnsClwE3DqSThUDa/5DISLgo5OREREcsho2i18H3gGWGWMOW2M+QBeQnWbMeYQcFv/91hr9wL3AfuAXwMfsdamJiv4SWctvPDvkOrzkiqAVAy6z8HhB4KNTURERHLOJUesrLXvSnPTLWnu/0XgixMJKmf0noe+1uHH3QScfRZWvy37MYmIiEjOUuf1kTgh0tTegxnvLKqIiIjkK2UHIymsgNJ50HGKQQmWE4XaG8Z2rs4z0PACGAfmbIHSORkNVURERIKnxOpStnwYnv4SJGNgk15iVLkaFvvOhPo7eD8c/qVXAI/xvl/9+7D0tkkLW0RERLJPidWllMyGW74CjS9BbwtULIOZS0b/+M4zXlJ1ofgdvARr/w9hziYorsp8zCIiIhIIJVaj4YRhzubxPbZ+J7hpFkaeexGWaNRKREQkX6h4fbIZ4/3xvzGroYiIiMjkUmI12ebWeXVZfuZsyW4sItOUi8t+GtjGEQ5wDjfdal/JiBa6eZajPMcxOugLOhyRrNJU4GQrnQur3gYHfuI1HL0wenXZnVBUEWxsItNAFzG+xTZ6iJMgRYQQMyjk/VxDMdGgw8s7T3GYJziExRuTf4j9vIF1bBy025lI/lJilQ3Lboe5W6Dhxf52C5uhqDLoqESmhV+xhw76Lo5SxUnRSg+/ZR9vYWPA0eWXRjp5gkMkcQcd/xV7WE4NpRQEFJlI9mgqMFuKq2Hpa2HJrUqqRLLEYjnoM/XnYtlHfUBR5a+9nCU1JKkCMBgOcC6AiESyT4mViIhkhE1Tu2b7/xOZDpRYiUjeMhiWUT1s/a2DYRWzA4kpn61lLqE0v1ZW6vWWaUKJlYjktTu4nFIKiBICINpfvP46Lgs4svwzh3K2soQwDgYvgQ3jcBtrKKMw6PBEskLF6yKS18oo5KPcxCs00EwXNcxgNXPSjqzIxNzMatYxn/00EMJhDXOopCTosESyRomViOS9MCEuZ37QYUwbNcyghhlBhyESCH1kExEREckQjViJSKAslrO000gnsyhhIRWYabLdUxcxjtJEmBDLqSaqt2SRKU//ikUkMHGS/BfPUU/HxWOVlPBetlJEJMDIJt92jvEw+/vLvD1vp46lVAUYlYhMlKYCRSQwj3CAM7STIHXxTxOd/IqXgw5tUjXQwcPsJ4lLnNTFPz9gB3GSQYcnIhOgxEpEArOb08M6dbtYXqEhrxtKvuTzvMHru3WYpgAiEpFMUWIlIoEZutXMBfneqTtByvfZWSwJUlmPR0QyR4mVHzcFTXvh7PMQ67j0/UVkXPy6ogMspAInj9+eVjOHSH/D0oFcLMtUYyUypal4faiOk/DsV8BNgAVsEla8BVbcEXRkInnndazlFC3E++urwjiECfFG1gcd2qRaShUrqeEgjSRIYYAQDjexilJ1KBeZ0pRYDWRd2P4vEO8cfPzwz6ByBcxaGUxcInmqnCL+jBvZzWnO0s5sytjIAoqIBh3apDIY3sYmjtLMK9QTIcQGFjCH8qBDE5EJUmI1UMshSMWGH0/F4cSjSqxEJkEBEa5kSdBhZN2FDaKXUR10KCKSQflbxDAeyT5I15gw0ZPVUERERGTq0YjVQJUrvcL1oUIFMP/K7McjIqNisZyilRhJFlJB4SQ0F3VxOUkrSVIsolJd0kXEl94ZBooUwWXvgr3f94rXsV5SVbYQ5l0VdHQi4qORTu5hOzGSGAwpXG5jDVewOGPXOEs73+e5/kJz7xpv5HLWsyBj1xCR/KDEaqjaG2HmEjjxOCQ6Yc4WmFsHjl4qkVzjYrmb7XQxuDbyIfYzj5nMZ+aEr5Ekxd1sp4/EoOO/4GXmUk41MyZ8DRHJH8oW/JTXwvr3Bh2FiFzCSVp8t4BJkmInJzKSWB2h2beRaQqXXZziNtZO+Boikj9UvC4iU1aMBMZnwYkFeoaMME3kGvgkVpm8hojkDyVWMlhfGzS/Aj3NmTtnVwM074d4V+bOKQIspJKkz557EUKsYU5GrrGYWb4b0EQIsYrZGbnGBS6WM7RxkhbfvQRFJPdpKlA8bgpe+k84u92rJ3OTUL0ONv8JhMbZrDHeBc//K7SfBCfkLQhY+jpY9btg0rS1EBmDYqLcxEoe59DFPfYihKimlHXMy8g1yijiGpbyLMcGXWMe5azMYGJ1hjZ+wI7+qU2DA7yNTSynJmPXEJHJp8RKPEd+BfXPecmP2z+90bQH9t47/nqzF/8d2o6BTXHxw/exh2DGApi/NSNhi1zDMuZTwU5O0EuCtczhcuYTyuCA/E2sopZZvMBJ4iRZxzwuYx5Our53Y5ToL5CPDakX+yEv8BFupEzb3IhMGUqsxHP8Ia/D/EBuAk4/BZe/G8wYf0nFOuD8fi+pGigVg6O/UWIlGVVLJbVUTuo1llLF0knaIPkADVif6UYXy0uc5lqWT8p1RSTzVGMlnmSf/3E36d809VISPWBC/rcN3YtRZJrrIZF25WE3cZ9HiEiuUmIlnsoV/sdnzIfQOLpYl9T4P86EoGb92M8nU1oL3ZyhjSTjSNKngcXM8j0eJcSySRolk8xopouztGmxgVykqUDxrH0XbPsCpBL903cOhMJw+Tjrq4wD694Hu/7j1S72JgyRYljxpkxGLjmskz5+wA4a6cTBASy3s46N6lg+SA0zWMc89lI/qEB+PhXapDlHtdLDveygjW5Mf7Xd77CeNcwNOjQJmBIr8cyYD9f/Axz7DbQeg7IF3gq+0gm8Scyrg+Iqr6aqpwmq1sKSW6GgLHNxS077L56jkc7+SS7vE/0D7KGKEhZQEWRoOedNrGc5NbzASVK4rGcB65nv26dLgmWxfI9naad30M/2f7OLKkrVjX+aU2IlryqugsvuzOw5Zy6GzXdl9pwyJTTSSQs9wyqHEqTYzjElVkMYDGuZy1qNeOS8k7TSQ3zYz3YKlx2c4PWsCyQuyQ2qsRKRSdFFLG07gg7SLJYQmQK6iUGajv/62RYlViIyKeZR7lvQG8ZhRQ40vUyQopFOeqbZqjuLpYVuWuj2bfEgl7aQCt+f7QghlqsmbtrTVKCITIpCIlzPCp7k8MWC7BAOJUSpozbQ2J7hCI9xCAOksKxiNm9mAxHStAjJEw2080NeoLN/VGUGhfwem5lLecCRTS0zKORKatnByYs/22EcyilivRZmTHtKrERk0lzLcmqYwXaO00OMlcxmK0soZBwtPDJkH/U8NmALHICDnOMXvMRb2RRYXJMtRpLv8ix9A7q7t9LDd3mWv+BmCgL8O5mKbmUNC6jgOY7TR5K1zOFKluR9ci6XpsRKRCbVSmZndE+9iXpqwAjaBUlc9tHAG0hSkKdvi69Q77uZtItlH/VsYlEAUU1dBsMa5qq9ggyjGisRmVa6iPkedzD05nG9VSd9vg1aE6ToTPOaiMjYKbESkWmllkrftYphnLze7HgBFb7TVBFCan0hkkFKrERkWrmRVcPaQBjgVlb3d4fPT4uZxVzKCQ94jmEc5lHOkjRb6ojI2OVnMYGISBrNdPV3M3+13sjBcJq2vK4zMhju5Eqe5wS7OAXARhZyBbXq7i6SQUqsRGRaeZLDJIf0IEpheZkzvI61RPP4bTFMiKtZytUsDToUkbyVv+PeIiI+Ouj1PW4w065ZqIhknhIrEZkSeogTH9CDabwWUuE78RXC5HXx+mSyWHqID2tjITId5e+Yt4jkhdO0cj+7aaUHgGVU82Y2UEx0XOe7kZUcpHHQliQOhptZldfF65PlGM38nJcudnNfxRzexOVqOCrTlt5FRCRntdPL3WznPN24WFwsR2jie2wf9z537fT5jlg10jmxYKehZrq4lx200UsKSwrLARq4lx1BhyYSGCVWIpKzdnBi2Ga3bv8mwmdpH9c5n+DgsOJ1F8suTmdkqnE6eZZjw5qOprCcoY1mugKKSiRYSqxEJGc10+W7DYsB2vqnBseqTcXrGdNMl++4YQgn7essku+UWOWbVAJcfeqW/LCIykENLS9wscyhfMTHuljiJIdNGc5L8zgHwwwVr49JLZWEfP5+krjMZkYAEYkET8Xr+aKrHnZ/C9qOAgZq1sP6P4SCsqAjExm3TSzkGY7STexiehTBYTk1zKLE9zEuLg9zgB2cIIlLOYXczmUXN4K+iVUc4/ygFWwRQtzISt8kQdK7gsXs4AR9uIP+fi5nvpJUmbaMteMrAM2kuro6u2OHih3HLd4Nj34SEgOmRkwIimvgxi+A0S8Lmbo66eMRDnCQc0QJs4VFXMPStCv4fsnL7Ob0oDqqMA7v4SoWUglAPe08zH7qaaeUQq5nOZcxLyvPJ9+00cPDHOAoTRQQ5iqWcCWL1c1d8poxZqe1ts7vNo1Y5YPT2yA1ZPrPpqCvFc7vh6q1wcQlkgEzKOTNbBjVfftIsIvTwwrek7g8wWHu5EoA5lLOu7kq47FORzMp5nfZFHQYIjlDQxn5oOssuD5Ft9aF7nPZj0ckIJ30EUozUnJeq9REJAuUWOWDmUsgVDD8uDFQtjD78YgEZCbFvqvUDN4o1VRk+//LNbkYk0gu0FRgPpi3FQ7eD27CG6UCcCJQtghmLgs2NpEsihDiapbwDMcGFaeHCXE9KwKMbOySpHiY/bzAKRKkmM9MXs+6tKsas+UwjfyGfZynmyIiXMNSrmGZaqpE+mnEKh+EC+Daz8G8qyBcCJFSqL0Jtv6VN2olMo3cwEpuYw3lFBEhRC2VvI+tzGZqrZD9MS+yk5MXE8QztPFdnrm4tU8QTnCe+9jJeboB6CXBExziUQ4EFpNIrtGIVb4oLIdNHwo6CpHAGQx11FJHbdChjFsbPRyhaViH+CQuz3KU17MukLge8+lan8BlO8e5nhWECQUSl0gu0YiViEiOOU+3b08tF0sDHQFE5LkwUuWni1gWIxHJXUqsRERyTBWlw0aGwOsOH2QRfjWlaW8rxWcBjcg0pKlAEZEcU04Rq5jNQc4Na3S6lSWBxXUjKznNdhIDYooQ4hqWZnQa8DBNPNhfID+DQm5gBRvRCmeZGjRiJSKSg97KRrayhEIiOBhqqeT9XMNMigOLaSGVvJMrmE0ZDoZSCriFVRldcXmUZu5jB0104WJpp5cH2MtzHMvYNUQmk0asRERyUAiHm1nNzawOOpRBllDFXVw3aed/hP0+BfIpHuMQV2irHJkCNGIlIiI5I12BfIIkfSR9bxPJJUqsREQkZ6Sb6gwTokCTLDIFKLESEZGccRMriQz51RQhxLUsw9E0oEwBSqxERCRnrGQ2b2Yj5RQBUESEm1jJNWh7LpkaNK4qIiI5ZS1zWctcXKxGqWTK0YiViIjkJCVVMhUpsRIRERHJEE0Fisi0104vj3CAIzRRQJirWKyeSSJTSC8JHucg+6jHwbCRBVzL8kA2BldiJSLTWjcxvs6T9JHAAj3EeZgDNNLJG1kfdHgicgkpXL7FNtroIYUF4GmOcoIW3svWrH9A0lSgiExrz3Oc+MW3Y0+CFLs5Qyd9gcUlIqPzCvV00jfoX3ESl7O0c5q2rMejxEpEprUTtJIasoUKeBseN9ARQEQiMhanaSNOathxi6VeiZWISHbNosR3oiCFy8z+XkoikrsqKCbsk844GMoD2LRcNVZTVW8LHLwfmvZAtBSW3Q7ztoJRsa3IWGxlCS9zhsSAT7whHOZSTjUzAoxMREZjPQt4jIODNu82GAqJsILqrMejEaupKNYOT34OTj0FfS3QcRJe+k848OOgIxOZcqoo5Z3UMZMiQjiEcFhBNe/iiqBDE5FRKCLCH3I1sykjhMHBsJAK3s81OAGkORqxmoqO/haSfTCwLiQV944vvd0bwRKRUVtCFR/lJrqJEyVEVG+NIlPKbMq4i+voIY7TP1oVFI1YTUXn94ObHH7cCUPnmezHI5IHDIZSCpRUiUxhxUQDTapAidXUVFQFfuW2bhIKK7IejoiIiHjy/6NZbysc/gU07/WSjqW3w+wNQUc1Mctuh3O7wI2/eswJw8ylUFIz/vN2noGDP4OOE1A6F1a8yTuniIiIjEp+J1Z9rfDEZyHZCzYF3eeg7Sis/j1YclvQ0Y3fzCWw6YPw8nchFQPrQtVlsOlD4z9n23F45kuQSgDWe62a90HdR6F6XaYiFxERyWv5nVgd/tWrSdUFqTjs/zEsugFC0eBim6i5dTBnM/Q0Q6R44gXr+77vvTYDpeKw52646csTO7eIiMg0kd81Vs37BidVFxgDXWezH0+mGceb+svEKsC2Y/7Huxv7R7FERETkUvI7sUpXyO2mIFqe3VhyXbrkLBQBJ/u7g4uIiExFE0qsjDEfN8bsNcbsMcZ83xhTaIypNMY8aIw51P81uGVqy98wfLrPCUPlSijS6rlBlr7e57WKQu1N3siYiIiIXNK4f2MaY+YDHwPqrLXrgBDwTuBTwMPW2hXAw/3fB6NqLax9F4QLIVToJVWzVsOWDwcWUs5acissvgWciPd6ORGYv9Ur9BcREZFRmWjxehgoMsYkgGLgLPBp4Mb+278DPAb89QSvM361N8KC10B3A0TLoFBTgL6MgTVv91os9DRDYSVES4KOSkREZEoZ94iVtfYM8BXgJFAPtFtrfwvMttbW99+nHphAY6UMCUWgbKGSqtEIF3mvlZIqERGRMZvIVGAF8GZgCTAPKDHGvHsMj/+QMWaHMWZHU1PTeMMQERERyRkTmQq8FThmrW0CMMb8BLgGOGeMmWutrTfGzAUa/R5srf068HWAuro6O4E4sq+nCY78xutQXl4LS18HxdVBRyUiInnuFC1s5zid9LGSGrZQG/jeeDLYRBKrk8BWY0wx0AvcAuwAuoH3AV/u/3r/RIPMKe0n4Okvefvy2ZTX/+nUU3DNZ6B8UdDRiYhInnqBk/yGfSTw+jPW085OTvIhrlNylUMmUmO1HfgR8ALwcv+5vo6XUN1mjDkE3Nb/ff7Y873+bWT6G4/alPf9nu8FG5eIiOStBKlBSRVAEpdOYmwnTYNnCcSEVgVaaz8HfG7I4Rje6FV+aj2a5viR7MYhIiLTxjk6cDDDjqdwOcg5bmBlAFGJH3V+HKtwQZrjhdmNQ0REpo0iIqRwfW8rJs3vJQmEEquxWnSj1zxzICfibeosIlNCLwm2cZh72M4D7OE8XUGHJDKiWZRSRSlmyKhVhBBXsSSgqMSPEquxWv27ULOhv0N5kfd19kbvuIjkvC76+Dce53EOcYRmdnCCr/MUR2kOOjSREb2TK6imlAghCggTxuF6lrMcrUrPJRPtvD79OGGo+wj0noeuBiidA0Wzgo5KREbpcQ7RQxwXr8uLxSsM/hm7+XNuHjYiIJIryijkLq6jkU66iTOPcq0GzEFKrMaraJYSKpEp6CCNF5OqgXqI00Ef5RQFEJXI6BgMsykLOgwZgaYCRWRaKUjzedICUULZDUZE8s70G7GyLjS8CPXPezVSi66DmUvHdo5YB5x83GsWWr4Yam+A6IxJCVck37TTy05OcJ5uaqlkAwvTJjuT4UoW8yCvDOoH5GCopZIiolmLQ0Ty0/RKrKwLz/2/0HLIa+qJgTNPw6q3edvSjEZXA2z7B0glwE1A40tw9AF4zd969VYiktYpWrib53BxSWE5TCPbOMqHuJaSLC0Z38IiGmhnN2cI4+BimUUJb2VjVq4vIvlteiVWDS8OSKoALKTisP9HMP9qKBjFvPXL34NEr/dY8JIrNwl77oat/2OyIheZ8iyWn7J70EhRApcUMR7jIHdweVbiMBjeyHquZwX1dFBGIXMoU9G6iGTE9Kqxatg5IKkawAnD+VdGd46W/TCs8NWO/vEi01Q3MTroG3bcxXKAc1mPp4wiVjGbuZQrqRKRjJleiVW4ENK9gYZGOQ3hpBnkS3dcRAAIE2L4hxJPREXjIpInplditfD64V3TAayFxj3edF7LIe/7dOZfMzyJcsKw4DWZjVUkzxQSoZZZw/Y7i+BQR21WY0mSYjen+Rm7eYpDdPmMpImIjMf0GmaZuRhW/x7s/yE4IcB4Reg2BSce8e5z6kkvAVt3p/851r4Dus5C+3G8vNSF8iWw5h1ZeQoiU9lb2Mj3eJZ2egFvGnAFs7mKxVmLoZcE32QbnfSRIEUIh6c4wru5igVUZC0OEclPxo40OpMldXV1dseOHdm7YLwLmvdBogf2/pdXgD6QE4XXfNprpZBO+wkvwSqdD+WLJjVckXxisZymlTZ6mUc5syjN6vV/yz6e5zipIdOSlRTzEW5UvZWIXJIxZqe1ts7vtuk1FXhBtBTmXdlfyO6TWLoJOLdr5HOU13orCZVUiYyJwbCQSi5nftaTKoB91A9LqgA66KNTU4IiMkHTM7G6wIng+xIYxxu1EpG8E07ztmeB0DR/SxSRiZteNVZDzd0C++4dftw43oiWjF1PM5x5xuv1VXM5zFoNRlMrkl4PcR5mP/W0U8MMbmU1pRRO2vU2s4jHOUgC9+Ixg2Ee5ZPapNRiOUwTx2imlAIuZz4zhjzPJjrZy1lSWFYzh/nMnLR4RGRyTO/EqqAcNn4Qdn3DS6awXnf2y98LxVVBRzf1nN0Bu/4DcL2mqScegarLoO4j/a+vyGDnaOfrPHVxYq6BDl7iDO9lK4uZnE3Or2IJJ2nlKE2Y/oqqIqK8jU2Tcj2AFC53s52ztF8smH+cQ7yDOpbivdds5xgPs59U/xbRz3GczSzkdVw2aXGJSOZN78QKYN4VUH0ZnNsNWKhZ79VgydikYrD7G+DGBx9r3gsNL8Bc3xo/mebuZYdvZ6v72Mknee2kXDOEwzupo4EO6mmjjCKWUDWsDUQmvchJztJ2cZQshUsK+Akv8pfcShd9PMx+kgNG0RKkeIFTrGO+Rq5EphAlVgCRYlhwddBRTG3nD/iPSqVicPppJVbiqz1NsXgfCZIkCU/iW9QcypjDKLaxyoCXODNo6vGCJCkaaOcs7b5pXYIUr9CgxEpkCtH8jGSGGaFztrrSy7jkz9uTM0LBvIMhhMFvVwjTf7uITB35884lwZq1Ct/tgkIFsPC6rIcjU0NVmnYLpRSkXb03HklS7OEsj3Owv93C8NGjybSZhb7b9hQRYTZlrGIO1mdSNITD5czLRogiF3UT4zmO8wSHOEWr78+mpKehBMkMJwxXfBSe+1/e97b/F9fC66B6XXBxSU57N1fyv3lsUG2Rg+E9XJWxa3TSxzfZRh8J4qSIEqKYKB/gNZO6CnCgy5nPYZo4QAMuEMLgYHgHdRgMxUR5Mxu4n90YzMVfZDexkmpmZCVGEYAjNHEfO7FYkrhs4wgrqOF32aTmuaM0PTuvy+RJ9MK5F7yv1ZdB6dygI5Ic5+LyDMc4QyuzKeM1LM/oaNW97OAQ5wZ95nYwrGXupK4E9NNAByc4TwlRVjFn2ChWNzEOcK5/q58ayinKanwyvaVw+QoPEiM56HiEEG9mA2vR+/kFI3Ve14iVZFakSBtSy5g4OLyGZZNybq93VOOwiQwXy34aJuWaI7lUwXwJBWxGuzlIME7R6ns8QYpdnFJiNUqqsRIREZERaRJw9DRiFZR4F9Tv8NoR1KyHwkpo2AmxdqhcCTOXTrxjeawd6nd6zTpnb4SSmrE93lpoOwotB71mqnO3eMXoIlnWRCeHaaKAMGuYQxGj23LKYFhJDQdp7G+7eeE4LKSSpzlCOUWsYjZhn+JykelkIRW+dVQRQmxkYQARTU2qsQrCud3wwte8/7eut+ba4LUscJNeIXjVGtjyZ+CM883+zHbY/c3+E7ve1+VvhJW/M7rHuynY8f/B+f2vxuSE4Oq/hjJNVUh2WCy/ZR87OXmxNQHA77OZ5Yzug0IXfXyTp+klToIUYZz+f3KGFC5hHMKEeD/XMIuSyXsyIlPAMZq5F+/3cQqXEA6rmc1b2Kji9QFGqrFSYpVtyT548M8hFR/5fqEorH0n1N409mvEu+ChvwQ3Mfi4E4XXfAbKay99juOPwL4fDO6kDlBcDTf9k/b/k6w4SjM/YAcJUoOORwjxP7jNt4WBnxQuBzlHM9000sEBzg1aiQgwlzI+iFqDiPQSZx8N9BJnKdXMozzokHLOSImVaqyyrWnP6PbNS8Xh5BPju8a5Xf7XcBPeSNZonHpieFIF3vRid/aLfmV6eonTw5Iq8EabjtI86vOEcOJqUtsAACAASURBVFjDXK5jOWdoH5ZUATTSRRexCcUrkg+KiLKFRVzLciVV46DEKtvGMkJox9nEcKTH2eG/pMZ2DjP+uETGyE3TmNDAuJsWjvQ4NUIUkYlSYjUabhIaXvSmx9qPT+xc1ZeBO4rExInCgmvHd43ZG/yTn1AE5l05unMseI0Xw1CREihVJ2jJjsuZ7zvdlyJFFzFe5BTdYxxlupx5vn2yKilmBoXjjlVEBLQq8NK6G+Hpf/RW77kpr7Zo1hqo+7Px7YEXKYYN74fd3wKsd04n5I1kmZA3/RYq8Oqgam8cX8wF5XDZH8De/+ovjne9pGrRjVAxyn5BtTd7Kwo7TnrP3Yl604tbPqz6Ksma5VSzhjm8QgMJUoRwcHFxgQd5BYAH2MPrWcemUa5aupblHKKJVrqJkyJCiBAm681CRSQ/qXj9Up74Oy+5GDhF4ERh9dtg6evGf97e8169U6oPajZ6ReFnt0OsDSpXeSNbo6nFGkl3I5x9zqutmrN5dEXrA1kXmvZCywEomAnzt0LUf283kclisZyhjUM0YrE8w7Fhe/2FcfgwNzCT4lGd08XlEE2cppWZFHEZ8ygkMhnhi0geUuf18eprha4zMLTuwo3DyccnllgVzYLlbxh8bMmt4z+fn5IaWPHG8T/eOFBzufdHJCAGwwIqWEAF2znmu+DbAq/QwNUsHdU5HRxWMZtVzM5orCIiqrEaiZsibb9ZN+l/XEQmTQrXt6DdYoeNYomIBEGJ1UiKZkHhzOHHnTDMuyr78YhME+fpZjenOULToERqJbMvNgkdyMGwUqNPIpIDNBU4EmNg013w7Fe8NgVuwissL64aPo0nIhNmsfyM3eyl/mICVUiE93E1FRRTRSlXs5RnOXaxv1WEEFeymBpmBBm6iAigxOrSKpbBzf8Ep7dBTzPMWglztoxvRaCIjGg3p9lHw6AGnglS3McO7uJ6AG5iFauZw17OYrFcxjzm4TOyLCISAGUHo1FQBsteH3QUInnveU4M67Ru8aYG2+i5uOpvLuXMVUdoEclBqrESkZzht30NeCsD090mIpJLlFiJSM64jLm+XdGjhKhCPdREJPcpsRKRnLGVpVRQfHEbmxCGCCHeyiZMutYnIiI5RDVWIpIzCgjzQa5lL/UcpYlyitjMolF3VBcRCZoSKxHJKWFCbGABG1gQdCgiImOmqUARERGRDFFiJSKSoy5sQH2YRvpIBB1OVrXTyyEaaaYr6FBExkRTgSIiOaiFbu7hObqJYTCkcLmZVWwd5UbTU5WL5ef93fdDOKRwWcBM3sEVFOhXlkwBGrESEckxFss9PEcbPcRJESNJEpdHOchxzgcd3qR6hqPspZ4k7sXnfYpWfsnLQYcmMipKrEREckw9HXQRG7D9tCdBiuc5HkRIWfM8xwdtaQSQwvIKDSTVJFamACVWIiI5po/ExU2oh+omnuVositG0ve4xQ5LuERykRIrEZEcM5+ZpHySiDAOa5gTQESZ10wXJzg/LJFaSpVvSllBMYVEshOcyASoElBEJMcUEOY21vAQ+y/ukRjBYSbFbGJhwNFNTBd9fJ8dNNOJ01+cPrAo/1bWcIzzJEiRwsXBEMLhTawPOHKR0VFiJSKSg65gMXMo43lO0E2M1cxhIwsvbvczVd3LDhpo768f80blHuUg1cxgGdVUUMyHuYHnOc4pWqmilKtYwixKggxbZNSUWImI5KiFVLKQyqDDyJgWummk07co/1mOsYxqAEop4CZWZT9AkQxQjZWIiGRFD3FCaX7tdBPLcjQik0OJlYiIZMVsynCHjVdBCIcV1AQQkUjmKbESEZGsiBDitawZVCcWxqGEKFtZEmBkIpmjGisREcmaLdRSxQy2c5QO+ljJbK5gMUVqpSB5QomViIhkVS2V1OZRUb7IQJoKFBEREckQJVaZkkpAVz3Eu4KORERERAKiqcBMOPYQ7P+x9/82CbM3wcYPQKgg2LhEREQkqzRiNVHndsH+H0Kqz/vjJr1ju78ddGQiIiKSZUqsJurQzyE1ZLd5NwENOyHRE0xMIiIiEgglVhPV1+Z/3IQg3pndWERERCRQSqwmatYqMD4vowlB0azsxzMF9KUsJ3tTxFLDOzCLiIhMZUqsJmrlWyAUBcyrx0JRWPN2cLQ2YCBrLZ892E3VQ+dZ80Qrsx46z+cPdWOtEiwREckP+s0/USU1cN3n4dDP4PwBb5Rq+R1Qc3nQkeWcrx7r5avHeulJvXrsfx7ppTxs+IslxcEFJiIikiFKrDKhpAY2/nHQUeS8fzoyOKkC6HHhy0d6lViJiEhe0FSgZIW1lvMJ/ym/5rimAkVEJD8osZKsMMawuiTke9vaGf7HRUREpholVpI1/2ttCcVDfuKKHPiXNSXBBCQiIpJhSqwka15bHeXXV5ZzU2WY2VHDzbPCPHhlObdWRYMOTUREJCNUvC5ZdV1lhEe2zgw6DBERkUmhESsRERGRDFFiJSKSQ1xcUrhBhyEi46SpQBGRHNBFjF/wModpxAKLqOBNrKcSLe4QmUo0YiUiEjAXy3/yNIdpxMVisZykhW+xjRjJoMMTkTFQYiUiErAjNNFFDJdXm+VaIIHLHs4GF5iIjJkSKxGRgLXQTYrhOxAkSNFEZwARich4KbESEQnYbMoIYYYdjxJiLuUBRCQi46XESkQkYLVUMotSQgPekh0MhUS4jLkBRiYiY6XESkQkYAbDe9nKZhZSSJgoIS5jHn/MtYTRXpoiU4naLYiI5IACwryedbyedUGHIiIToBErERERkQxRYiUiIiKSIZoKnKo6TsHe70PrYQgXwuJbYfkd4OR2PcZPGmJ85kA3x3tdlhQ5fGlVCW+ZUxB0WCIiIhmhEaupqKcJtv0jnH8F3ATEO+HwL+Gl/ww6shHdd7aP9+zq5EC3S8yF/d0ud+7q5Mf1fUGHJiIikhFKrKaiI78GNz74mBuHs89CX3swMY3CXx/ooWfI3rI9LnzqQE8wAYmIiGSYEqupqP0YWHf4cScC3fXZj2cUrLWc6PWJGTg6NNsSERGZopRYTUUzFoDx+atzk1Bck/14RsEYw7wC/x+3+YX6MRQRkfwwod9oxpiZxpgfGWP2G2NeMcZcbYypNMY8aIw51P+1IlPBSr9lrwdnyLoDJwI1G6CoMpiYRuHzK4soHlJbXxyCv19ZnPYxLXGXP93TSdWD56l56Dwf29vJp/d3M+/h81T+9jzv3dXJ2b7UJEeeGx5ojLPpyVbKftNM3VOtPNgUv/SDREQkq4y1wzf+HPWDjfkO8KS19hvGmChQDHwGaLHWftkY8ymgwlr71yOdp66uzu7YsWPccUxLLYfg5e9C5xkvqVp0Hax5B4QiQUc2on8/0cvnDvXQGLfURA1fXFXMBxYW+d437louf7KV4z0u8f4f0wu7qV34qQ0D1QWG/ddXUBbJ35Gv/26I8e5dnYNq1Iod+OHmMt5QEw0uMBGRacgYs9NaW+d723gTK2NMGbAbWGoHnMQYcwC40Vpbb4yZCzxmrV010rmUWE2AmwQTAjN8A9dcZa0lYSHqjBzzD+tjfOClTjovMSBV7MCXVxfz0cXpR76muuWPtXDEpxZtTUmIfTdoUFhEJJtGSqwm8hF/KdAEfNsY86Ix5hvGmBJgtrW2HqD/a24W/eQLJzylkirw6q0ulVQBvNCevGRSBd7KwmdakxmILDdZa32TKoCDPdNjGlREZKqYSGIVBjYD/2at3QR0A58a7YONMR8yxuwwxuxoamqaQBiSr5aXhCgZRb/TQgfWlOZ2Y9SJMMYwO+qfiM5NsyBARESCMZF35dPAaWvt9v7vf4SXaJ3rnwKk/2uj34OttV+31tZZa+uqq6snEIbkq3fMLaDIMVxqbCtiDB9c5F+n5edYT4o7d3Uy56HzrH28lX881M2GJ1sJ/aqZyAPNvHZ7G13J3GoB8TfLi30L/z+7fPTPO+Fa/vlID0sfbWHew+f5yJ5OmmIjP8+d7Uluf66dmofOc9W2Nn7VqIJ5EZGRTLR4/Ungj621B4wxfweU9N90fkDxeqW19pMjnUc1VpLOoe4U73+pk+1t3lTf1TPDFDmGR1sSAKybEeKbl89gU/nodmc625di3ZNttCcsI6UUVRFD022zJhp+xlhr+ZdjvXzhcC89KUtJ2PC55cV8bHEhZpRTwW/b2cFvmuIXC+AjBuYVOOy9voKS8PBzPN+W4Mbt7QycbSwOwf+9rJT3LCjMxNMSEZmSJqV4vf/EG4FvAFHgKPB+vFGw+4BFwEng9621LSOdR4mVXEpX0uIYKA55CUBfypKwlhnhsQ26/tUrXfzv430XVxmO5O4Npdw5P7cSiJS1dCQt5WGDM4baur2dSa7Y1sbQHq0lIfjq6hLuqh0+8nXL9jYeOT+8dq06ami4pXJM1xcRyScjJVYT2oTZWrsL8DvxLRM5r8hQpUNGVApDhsJLThIO90RLYlRJFcADTYmcS6xCxlARGfvz3tmeJOTzsO4UPNGS5K7a4be90O5fGN+RtLQkLFVp6r5ERKYzVb7KtLKiODzqH/p8KoivLfJ/LgUOrCwdW0f8kIEyn6lDERFRYiXTzCeWFjGaHXTCBj6xNNjRql+ci3PtM20sfqSF9+7q5Ej3+FsrXFcZZl6hM2yIOmLggwv9n+dnV/gXzH94UeGo2mWAVxt2z5k+tjzVypJHW/jwnk7q+3JrYYCISCYpsZJpZVN5mPs2lzG/wKHQ8UZsriwPMXBWqzwMT28tJ+oE98/ja8d7eceuDra1JjnR53LP2Ribt7WNO7lyjOGxq2Zyw6wIUeM971UlIR66qpx5hf6jWW+fW8A/ryphZthQ7ECRA3ctLORLq0p87+/nUwe6uWtPFy90pDje6/KNUzE2PtVKc1zJlYjkpwkVr2eKitcl26y11MdcZoTNxQL4PR1JSsKwpHhCpYcTFktZqh9qoTM1+N9mCLhzfgHf2TBjQudvS7j0uTBnlD2wkq7lXNxlVsSh0K9QK43muMvCR1oYOkBV6MAnlxbx+ZWjT9BERHLJZHVeF5myjDHMKwwNWlW4riwceFIFcLw3hWX4B54UXvH9RM2MOKNOqgDCjmF+YWhMSRXA7o4kfpfpc+GR8xN/HiIiuUiJlUiOqY46JNIMJC8cTYFYjphf6JDwmfFzgCVpiulFRKa6qfMuLTKFdSRcPn+om3VPtHL1023cc6aPdNPwlVGHN9dEhxXZF4fg08tya6Pp7qTlHw/3sP7JVq7c1sq3T/Xh9j+v1aVh1peFGdodotCBjy8Zfcd4EZGpJPh5D5E815uyXPl0Gyd63Yv1Ri93dvF0a5L/s67U9zHf3jCDP3qpk5+eixMxXv+q/7m6mNfXRLMY+cjiruXaZ9vY35W6+Lz27u3i0fMJvrvRqwP7RV0Zf7Crk8dbEoT7G7x+fV3pqDvli4hMNXp3E5lk3zvTx+k+d1ARd3cKvnW6j08uK/LtMVUcMty7qYzWhEtz3FJb5Iy6xUG2/KQhzuHu1KDn1ePCjxpifLqriDWlYWZFHX5zZTlNMZf2pGVJsUNIHdtFJI9pKlBkkj3YnMCvS0LEwLOtw7eMGagi4rCiJJRzSRXAQ81xunyelwG2DXle1QUOy0tCSqpEJO8psRKZZIsKHdI1Kh/L6rxcs7DI8V31FzIwJzp1n5eIyETo3U/y3qneFB/d28WWp1q5c1cnuzpGHiXy82BTnDueb+eKbW38w6Fu2vyWu6Vx16Iihm6r5wCzog7XVWZvNt5ay4/rY9y6vZ2tT7fxr8d66E2Nv4/dBxYU4re2rzgEr6uOjD9QEZEpTDVWktcOdae4YlsbPSlLwsKujhQ/PRfjJ5vLeF316ArBv3q0h88e6qGnf9prT2eSb5+O8eK1MymPXPqzycrSEPdtLuMPd3fS51pSFlaVhvjvzWU4WZwa+/N93XzrdN/FacmXO5J890yMZ66ZOa6pxjkFDrVFDq90v5pkGuDGyiiRHJy6FBHJBo1YSV771P5uOpP2Yl8oF+hJwV17utK2OxioI+HytwdfTarAa3DZEHP5vyf7Rh3HHTVRGm6t5OmrZ7Ln+gpevLaCxUM34ptEx3tS/MepvkG1Xj0uHOhO8eOG+LjOef+5OKeGtFW3wP2NcQ5NYF9DEZGpTImV5LVHWxL4TdrV97m0pOvCOcDOjqTvaE6vCz9vHFtCEjKGy8vCLM1iQnXBk60J3zqv7hQ8MMbnccGv0xSvh8hMh3gRkalIiZXktVlDu1P2MwZKRrFFS3XUIekzsmWAeVOo8Lw66uA3OxcxMHec3dznFjjDascAHAPVfjeIiEwDU+c3g+Sl83GXvz/UzQ3PtPFHL3Xy8jgKy0fy8SVFFA/5KY8aeMfcgrR731lr+dm5GG/a0c7H93VREXEYeteiEHxs8ei7h8dSln8/0cst29t5284OHmy69CjR7o4kf7i7kxueaeMLh3poiQ8ee2uOu/zdwdG9drfOilDkGIY+47CBP15YOOrnMdAfLSgk7PMOUuAYbh9l/ZqISL5R8boE5mxfik1PtdGRtPS5sK0tyQ/qY/xgYxlvnJ2ZX8y3V0X4qyHHUtZLrNL5s73dfOfMq/VIRQ4UO97jwo4hZS1fXV3CtZWjW/kWdy3XP9vOns4kPf250W+b43xiaRGfW1Hi+5j/bojx7l2d9LleXdhz7Um+drKXF6+tYHaB4//anY1x3+Yy7vDpzh52DG+qifLN07FBx2uLHJYUje/z1eLiEPdtKuM9uzpJYrEWqqIOP68ry8m+WyIi2aARKwnM3x/qoSVhL3buTlmvsPyDezov7jc3UZ852MOQgR5SwMf2+RevH+hK8u3Tg4u8e12vKPtf15bwwBVlNN46i7tqRz9adV99jL1dryZV4NU2fflILw2x4RVgKWv50Mtd9PQnVeAVzDfHvX35AD7v99q58MGX/V+7U70pvnc2xtBbTvW5/Pe58dVYgVeUf+7WSh68spynrp7J0RsrWDdDn9dEZPpSYiWB+VVTgqRP/tSRsJzoHX2fqJE82OxfvH6q1794/ZHz/kXXXSl4uTPFNRURikdRmzXQz87F03Ze9yvyPtLt0usOjy1hXy2YT/fatScsJ31eu8dbEsM2QwYvwfv5BBIrgIhjuGpmhA1lYYw6q4vINKfESgJTkaawPAWUpWtVPkblI5zHL0GqiPh3SY8aqBpnQXZN1Pg20gRDhc/FyiPGN2kCqOx/zdK+dtb/tauIOPjlPGGgpkDJkIhIpiixksB8fEkRJUMyjqiBmyojzBphS5QnWxK8Z1cnb9nRwffPxkj6jO5c8LHFhcOK1wsMvHVOlCKfxOp3Zkd9m3aGDLx3wfiKvD+0qAi/p1McgptmDa/Tml3gcM3MyLARppIQ/OUSbwryLxYXMrRrQ8TAzVURKn0udltVhII0z+t0n8sbn2/na8d76U6X0YmIyKgosZLAvG9+AR9aWEih440sFYdgc3mYuzfOSPuYLx7u4fbn27nnbIz7G+N88OVObn++g1SamqyPLS7izvkFF69R5MA1FRG+vq7U9/7FIcNvryyjOmqYEfJGf2aEDPdumkFt0fj6T60tDbGocHBSY4A75xUQTlPk/YNNM9hYFqY45MVd6MCHawt51zyv6P79CwoHv3YObCkPc/cG/9cu6hgeuqqceQUOM0KGsrAharzasR81xPllU4JP7O9m87ZWOsawXY+IiAxmRtN9erLV1dXZHTt2BB2GBKQx5rKrI8mCQoe1IxQ+1/e5LH2shSHNvikJwXc3zOBtc9Kv9Dvbl2JPZ4rFRSFWll46QUpZy7OtSeLWcs3MCAVjrKsa6N6zMf745c5hdVaFDpy4qZKaEfph7e1McqbPZVNZmGqf+432tbvAtZbn2pK0JVzesauLjiEjVIUO/M2yYv6fFcWje3IiItOQMWantbbO7zaNWEngagocXlsdvWRi8Oj5eNoC7J9eYluWeYUhXlsdHVVSBV6X9NdURrhpVnRCSRXAT8/F/IvXHa+ofCSXzQjz2uqob1IFo3/tLnCMYWtFhOqC0LAVguCtPvxxQ8znFhERGQ0lVjJllPl1o8TbQiVdMXcumBk2vv/QDJkr0h+rsrAhlaY2bWYOv5YiIrlOiZVMGbdVRXxrkqIOfGCc3cOz4UOLiny3fokaw80+xevZsKIkxPKS0LA3gJIQfHQMHeVFRGQwJVYyZRSEDL+5ooyqiLlYgF3keI0715flblPKDWUhlg5dmgh8YEEBkQA7lP+sroylxQ6lIUNZGAoc+EhtIW/NUNd7EZHpKHd/G4n4uGJmhPpbKnm8JUFPynJ9ZYTySG5/PvhpQ5wTQyvugX890ccnlhWP2FpiMtUWhTh4QwXPtiU5F3PZWhFhzhTaWFpEJBcpsZIpJ+wYbqmaOqMqP2pIU7xu4NHzCX5vhH0LJ5sxhqsrgpmOFBHJR/p4KjLJZqQrXjdQMsEVhyIikls0YiU57+nWBPedjRF24F3zCtlSPrEf26Rr+XljnN82x5kddXj/wsJxN/8cjQ8sLOTu0zF6hyzCC2G4pSpzo0WutTzQlOCXjTFmRRz+cEEhy4a2th/iVG+Kb5/u42yfy61VUd4yO5q2aamIiFyaGoRKTvuLfV1841QfPSmvPUGhA59cVsznxtnAMpay3PJcO7s7knSlvC10wgZ+uLmMN9RMzvSiay0bnmxlT9fgOqu/WVbIF1b5d4Afq6RrecPzHTzTlqAr5U0zhg18Z30pvz/Pf8Xkg01x3vpCB0kLMRdKQ7CmNMzjW8t9t/sRERGPGoTKlPRCe5L/ONlHd8rbesUFelz48pEejvgVLY3Ct0738WK7l1QBxK13zjt3dZIYYc/BifhFY5xjvcOL1//lWB9tGdo+5t76GE/3J1UACQu9Lrz/5S56U8OfV8pa/mCX1w0+1h9CVwr2dCb5txO9GYlJRGQ6UmIlOev+c7Fh29dc8IvGkTutp3P32Rg9Pud0sexoT47rnJfyg/p42s7rDzeP3Hl9tO45418gHzLwlE9395c6UsR8EsleF+45q87rIiLjpcRKclaBY/CbkXLwei6NR1Ga+iHXQuEk1RYVOt405jDWe46ZkG7qzlp8t+QpcLwRQD+T9TqIiEwHSqwkZ71jbgF+O75YGHHD5aHiruW++hiffKWLZcUhSnx+6otDhh/V9/GFQ90cHuc0Yzp/tKCQwjTLAm/NUPH6BxcW4lenXhgyXDNzeLH/mtIQcwucYQlfSQj+pDZ3u9iLiOQ6JVaSs5aVhPjXtSUUOl5hdWkIihyvILtmlENWrQmX9U+28oGXOvnnY33cfaaPhPVGbIpDUOpAgYGOpOVLR/v4+8O9rH+yla+fzFyd0TUVYVb4ZD1/XltIYYaKxG+vjnDXQi+BK3ZgRgjKw4Zf1JX5rvIzxnD/ljKqooYZIe+1KHLgd+cUcOe84PpqiYhMdVoVKDmvMebyq6Y4IQNvrIlSMYZO6x/b28W/n+wjPuDH3ADrSkN8dHERTfEUXzzSS8+QQapCB07cVDnqBG4kv2qM8/YXO4bVQBU7UH9LJWUZ7Bx/tCfFw80JKiKGO2qil1zdF3ctDzTFORezXFcZZk2pOrCIiFzKSKsC9S4qOa+mwOvJNB4/qI8NSqrAm0rc353i7XOj/O3BHnp9Zv7CBh5oivO+cV53oO+f9S8sDxt4+HyCt45hWvNSlhaHWLpo9D25oo7hzbM1QiUikimaCpS8NtKAjdPf6yndXfzqu8Yj7TWMydg1REQkNyixkimvPeHyHyf7+MLhHp5oSTBwevu984cXjoeMV/c0I+xw5/xC3xWGKQt3ZKhh6PsWFFDsM4jkWpvxPQ+fb0vwxcM9fO1EL83xS/fIGum1A6/f1S8b4/zDoR7uOdPn2xNLRERepalAmdKeb0tw63MdpKylNwVFIbi2IsLP68qIOIbPrijm8ZYEezqTxF2vaL084vDdDTMA2FIeZkt5mKdaB/ew+uDCAmZmqPbpxllR/nRRIf/nRB8WL7GzwI82l1GcoeJ111res7vL6/2VgqgDn9jfzf1byrg1TfK2vS3Ba4e8dtdVRvjZFu+160i4XPdsO0d7UnSnvBWDf/lKN89cM5OlfpmiiIioeF2mLmstix5t5fSQLqLFIfjK6hL+tLbo4v0eb0nwYkeKJUUOd9REifSvlHu2NcEt29uHNQ0tdOD0zZXMimZuUPdgV4pfN8cpDRneOmdsRfiX8uP6GO97qXNYLVd52NB4ayXRISsDXWtZ9EgrZ2JDXjsHvrqmhD+pLeLj+7r4t5N9DLyLA1xdEeb/b+++4+suy/+Pv+6zcnKymnTvzSjIamgpe8/KkCkCFUUUFRURRFAU/YoMEUUBRSjjBwgIBRHZUPYslNWWUujeK22zc8b9++NOacYnacbJ+Zwk7+fjwaPJfU7OuXKTnFznvq/Pdb82pU/aYhcR6W50pI30SHMqkpR5HAlTlXRH12xljOHgvhEuGp3LiYNyvkyqAB5Y6d3dPWTgfx3s7t6SHfKD/GhULt8aHk1rUgVw94oazwJ5i3fn9TnlSTYnPOYuBdOXu87r96+spUneRQp4Z1OCco+vFRERJVYiIiIiaaPESrqtXfKDlHis/MSCrtt5W3x9aI5nV/REk+L18kSKe5bX8OdF1Xy0pWvOFOyMaUO9O69ba/m4PMnfl1SzusHy0y4FQYpCHnMXgG8Nc+0XzhyS06ywPwBM6uMK/0VEpDm9Okq3ZYzhkb0KKAwZ8oLuhzkvCAcUhzlveNsSq8l9wvxwVJTcgNv+iwZcB/J/fiX/y/qqt8riDHuxjB/MqeCy+ZVMeWMT53xQTioL6hO3OnFgmMEelzdWp+AX8yu5eF4lo2du5J76LdKAMTwysfncHdg3zLfr5+6q8TF2zAtSEHTtIvKD0C9iviz8FxGR5lS8Lt3e5niKf6+uY3VtigNLwhxQHMKY9l1tN7c8weNr64gGDKcO13rZaAAAIABJREFUjjA06pZ/ktYy5IWNrG3SZTQvCHfuVsCpg7Ojuebja2o584PmxetNRQOw6JASBtUnYZvjKR5aVceauhQHlYTZv8ncJa3l6XVxZm9JMDo3wNcG5Wy3m7uISE+nzuvSoxWFA21eoWrJhIIQEwqa/zq8uynh2bupMgm3L6vJmsRq+jLv7u5NBYDHVtfyvforJovCAb4zouW5Cxp3NE66enqJiPR02goUaUXCttyZPZ4Fq71bJdoYSwr3PYmISNfQipUIsLImydPr4uQE3EHPRfVF8ZP7hAgag2tcsE1e0BWMt8fS6iTPro+THzRMHRAhP43n2Zw9NMpLG+PbXbWy1n0ndyyr4ah+YQbkBHhybR1r67wPYbbW8u7mRP1WYJDD+oXr50NERLwosZJe708Lq7jisyqC9Wf6pYCH9yzkmPpGog/sWcBJ728haaE25Yq49y8J840hbd8GvGpBJdd8UU3QuGViCzxRWsRBfcNp+R5OGRzhX6vCPL/eJVc5AUikXEF+3LpzEbc+7xXzK0kB8RSEA248iUu6Th2cw5275RMwhpqk5dh3t/DO5jjWuo7xA3ICvLpPHwZ7XUopIiIqXpfe7cMtCaa8sYnqJv0uY0FYdWgJhfUrV6trU9y3ooZ1dZYj+oU5tG+4zQXyr22Mc9S7m6lqsppUGDKsOayEaJqKwa21vLIxwVPr6ugbNpw5NId1dZYZq2tJWsufF9c0i6GpvCDcums+Zw+N8qv5lfxxUXWjBqoh4NB+YZ6ZVJSWmEVEuiMVr4u04N4VNXidVRwEnlhbx5n1232DcgJcPCbWoee4c3kN1V4JjbU8vz7O1IHpKQw3xnBQ33CjVbChUdijMMSM1bUEqWnlq53KJPx9SQ1nD41yx/KaZl3pE8DMDXEqE5a8NG5lioj0FFrPl16tOuW2/ppKQbPjXDqqJtW0QquegdpUZlaMa1uKwUNNfUwepwV9qa3F8iIivY0SK/HdZxVJ7ltRw8sb4hlvunnKoAgxj47lSQvHpKnFwOmDI55d0eMpOKxfemqstlpZk+T+FTU8ubaOeIOk7Yh+4TZdDZgb4Mvasa8NihD2WJT6SkHwy+J+ERFpTFuB4puktZzzYQUzVteydVdpUE6Al/Yp+rJBZ1c7qCTMbvlB3tzceK/uW8OiXzbR7KypAyKMzg3wSUXjJaCfjo7SJ40JypWfVXL9wmpC9UX4OQHDc5OL2KMwRL9IgBt3zuOn8yqJp9yWXjTgCttDZltR/s75IS6o73H1fzvk8cz6OBvqUlQkXdIVCRju2k2d10VEWqLidfHNzYuruXR+ZaOC6qCBKX1CvDqlT0ZimFueoPT15sXr+UFYdVjftLREeHtTnEPe3Ex1k1+14pBh9eElRAKdf47n19dx4ntbmrVbGJxjWHZoyZctEuaWJ7hnRS0VSctJAyPsEAtw94paltekOKJfhBMGRgg1iKc6aXlgZS1vbYqzY16QacOiXx71IyLSW6l4XbLSLUubX6WWtPDu5gRra1MMSNOKUWvuXlHrWUtkgP+treP0drRUaMkdy2qo9Xj/ksTywvp4WrYc/7G0xrOHVUXC8lZZgv1K3JbjhIIQ1+zU+Nf+l+NbfhnIDRrOHR7l3E52thcR6S301lN8U+lxVAy4H8rqDBV1VyRSJDzGU7QcX3uVJ6xngby16X0OL8ak7zlERGT7lFiJb04eGCHisQs2ICfAiHY0oLTW8kZZnMdW17KqaX+AegurksxYXcsHWxqnUScOzCG/heL1I9NUWH7KoBzv4nULh7SzQejc8gQzVtfyaUXj7+P0wd7PkbCwX3HLz9Fw7lbXXwb50Rb3HJ+35fBBERFpRFuB4psrxsV4dE0da+tSVCYhYlwn8Ht2L2hz882l1UkOe3szq2tTBOqLsH80Ksq1O+ZhjCGRskz7yBXIRwIuYdolP8TTkwopDgc4vF+YY/pHeHJdHZVJ904jGoQrxsYYlpueAvoTB0UYuSDA3CbF6z8e2fZ6paqk5YRZW3i9LE444K4oPKgkzKMTC4kGDd8YmsP05TXM3pKgMun6cEUCcOsu+S32m1pSP3dr6ueuJgn9I4ayuCUUgLoUHDcgwr/2KCCchjowEZHeQMXr4qvKhOW+lTXM3BBnbCzI+SOijGhHQrPna2V8tCXZaKstLwh37VbAKYNzuP6LKn6zoIqqBneIGJcwzJhYCEDKWp5eF+fBVbXEgnDusCiT+qSvDcL7mxPs/2bzAvl+YcPKw0ralLR8/5Ny7lxe26hhZzQAF4yI8qcJ+QAkUpZH19Tx2Jo6+kcM3xkeZZeClt877f5qGZ+UJz23KbfKDcBlY3O5cnzedmMUEektWiteV2Il3dbnlUl2e7WsWcICcGBxiJen9GHUixtZ4rE9GDFQdmRfYmk6TqY13/u4nH8uq22WwBSG4KE9Czmqf+vF69Za8p7Z4Pl9FoYMm4/s2+6YFlQm2ePVskYJZ0sG5RhWHdb+5xAR6alaS6xUYyXd1paEJdTCluGm+mLuilYKt2syVNS9qaXiddz30BYtdYGv6uD3sCVhCbZxe6/Sq7pfREQ8KbGSbidlLW+WxVlXm8QrN4gGXEd1gGP7R/DaWBwdC1KSoX5MJw5soXg9BQeXbH/L0RjDfsXNt/QMbft6L18pCLbplz8AHNU/vd3hRUR6MiVW0q18tCXBiBfLOOqdzZz2QQXVSUvE8GXyFAvC8GiAH41y3cOv3jFG34ght/4nPWxcDdb03fIzFvMpgyKUFoW+TK5MfZy/HR+jfxt7dd2yaz6FIcPWu+cE3DbgX3fpWO1TJGC4/St5xAKuKStATn3H9q1XakYDUBw2XL+T6qtERNpKNVbSbcRTlqEvbmRdXeOf2RwDJw2KUJ6wHNs/wrRh0UZXwm2sS3Hb0hpeK4uzc36I74+MMtrrgMAujv3fq2p5aFUdRWHD+cOjXzbtbKuVNUluXVLD+1sSTCwM8f1RuZ0+dufjLQluWVrNsuoUx/aPcGjfMHeuqGVOeYIpxWG+OyJKP3VaFxFpRMXr0iM8ubaOr8/ewpYm7ZVCwIWjtl0dJyIi0pVUvC49Qlk8haV5UVUCWFvn/xsEERERJVbSbRxUEibuscKaF4TjB3b+vL2uVpu0vFUW55PyBNmwUiwiIumnzuvSbQzLDfLT0bn8ZXH1lwcOx4Kwe0GIk7I8sfr3yhrO+6QSsCQtDMkJ8ERpETt4nacjIiLdlhIr6VZ+v2MeB5aE+fvSGsoTlq8PyeHsoTlZfeTK3PIE0z6qaNTg8/OqFIe9s5nFhxQTbOPxPSIikv2UWEm3c1T/yHa7lWeTfyytoa5Jg08LbI6neHlDnEP7dZ/vRUREWqcaK5EutrI2RbKF29bHVWslItKTKLES6WLHDYh4d163eHZUz7QVNUk+2JJo8Yif8kSK2ZsTrGvhXJ2ktXxSnmBBZUvpo4hI7+H/q7pID3fG4BxuXFTNgsrkl3VWeUG4YESUoVH/itc31qU4bXY5r5fFCRsDWP64cx7nj3Bd6621XPlZFTcsqiYcMNSmLCcNjHDnbgVE69u1v7i+jjM/KKcyaUlZGJkb5LGJhSrKF5FeSytWIl0sGjS8uW8f/m+HGJP7hDiiX5j79ijgOp+Pijn5/S28ujFOTQrKk5byJFw0r5KZG+oAuGNZDTcurqY65Q5trk3Bf9bU8eO5FQAsq05y/HtbWFNnqUhCVQo+rUxy0NubiKe0xSkivZMSK5EMiAUNPx0T4619+/DspCJOGJiD8fFqwKXVSd7elKBpX9WqJFy/sBqA6xZua2uxVXUK7llRS23SMn15DXGPovzKhOWZdfGuC15EJIspsRLphdbUpgi38Nu/vMZlS+tb6GafslCRtCyrTjVLzACSFlY3vQxSRKSXUGIlvqtIpHhuXR1LqhJ+h9LIipoki6uSaeuSbq3li8okq1soAk+HlLV8Xplkbf1zWGtZUp1kefW2padVNSliQYNXrXrEwCElYT6rSDK5OORxgBAMyAlQEjYc3i+CVymVBfbPgqJ8ERE/6NVPfHXG+5t5cPW2baORuQHe368PJRH/cv7PK5OcNnsL8yqSGGBwToD79yxgcp9whx/zhfV1TPuwgrK4a70wsTDEQ3sVpLV4/Yk1dXz743Iqkq67+24FITbUpVhVm8Li5jYnYJhfmSQIRAIQDUD9AhUhIGDgH8tqmL68hqSFsHErUEnAALkBuGWXPIwxfG1QhGsXBvm0IvnlY8QCcPKgHHbK10uLiPROJhvOLCstLbWzZs3yOwzJsCvmV3L1F9XNxkflBlh0SIkPEUE8ZRkxcyNray0N15Xyg7Dw4BL657Q/4VtYleQrr5ZR1aBeKWhgbCzApwcWp6XW6pPyBJNf30RVOxfDcgIuySuLW2JBmFuRbNQhPhqAvepvH5cX4PKxMfYp3pZgViYsf11czf2raskNGL43Isq0YTkE1E1eRHowY8x71tpSr9v0tlJ885fFzZMqgMXVKZZWJRgRy/yP55Pr6qhMNE6qwK3a3LOihovHxNr9mH9f2rzIO2lhZU2K18sS7F/S8ZWwrf6yqJraDrxHshYO6xvmyvEx+jy3oVFSBW41a01dis8P9k5080KGy8bFuGxc++dFRKQnUo2V+KamlX6SC5v+hc+QFTUpvJqhV6dgUXXHGmAurEp6Pqapf750WFSd8qyZ2p466+a6OuXaKXhZ04U1YSIiPY0SK/HN0GjL20WTilpfrdoUT7G6NpW2wvKtJvcJ43Wec34QDizp2Jl+h5aEibXQeX3vPp1blUtay/LqJAcUh4h24Lc5LwiH9g2THzQMaWGbs3Q7/y9ERGQbJVbim9t2LfAcP3tIhFjI+0dzdW2Kw9/ezMDnNzJq5kZ2emUTb5Wlr2fSxKIQh/YNE2vw9NEAjI4FOWlgxxKrc4ZFKQo2ztYCwAkDIozxyrja6K7lNQx8fiM7vFzGH76oJoArNm/4HA0fvemMGqA4HODrQ1xPrZsm5DX6vg0QC8L1PjcyFRHpTpRYiW+OGhDh2b0LGZUbIAgUBuGq8bncs0eh5/2ttRz81iZe3hCnzkJtCj6rTHLEO5tZ0dq+YjvN2KuQ3+8YY0J+kHGxAJeMzuX1KUWEvZay2mBDPMXmJvt0BvikouOtHJ5aW8cP5lSwIW6pTkGtdf2lxucFGJUbYM/CIH/fNY9fjctlfCzAjrEAxWEatU+wQFldirL6ArATBuXw1KQiDu8bZmQ0wIkDI7w5pQ+lnbgaUkSkt9FVgdJtvLIxznHvbqaiSQ6VE4Cfj8nlqh2yc2XlF59W8qdF1c2aaeYH4dlJRUwpbn/ist8bm3hjU/O+X9EArD28hIImK34vb4gzdZb33P1ibC6/Hp+dcyciko1auypQK1bSbSxpoXh868pVtvqsKunZodwASzpYpL+4ha8LGljn8WStzl2FitNFRNKl04mVMSZojJltjHmi/vMSY8xzxpgF9f8Wdz7MDKiqgspKv6OQVpQWhTyvfMsLwoFpaFnQVQ4qDjWqXdoqbl1NV0dM7uPdFT1kDIVBqG0yURNbnbvOF6eXJ1JUd+SyxC4UT1k2xdN/gYOISGvSsWL1Y2Beg88vA16w1o4HXqj/PHstXQqHHgpFRdCnDxxwAHz+ud9RiYed80Mc0z9CboOf2rCBvuEAZw+N+hfYdnxzWJTicKBRYXksCCcMjDA+r2PF67/bIUZesHHNVE59J/UhL5ZR+OwGvvFBOVvq66d2KQhxdP9IowQvbKBfOMBZnZi7j7ckKH1tEyXPbaTo2Q0c9+5m39sz1KUsP55TQZ9nNzDg+Y2MmFnGo6trfY1JRHqPTtVYGWOGAXcDvwd+aq2daoyZDxxsrV1ljBkMvGSt3bG1x/GtxqquDsaMgdWrIVm/VRIIQN++sGgR5KnuJNskUpYbF1Xz96U1VKcsXxsY4dfj8zrUET2T1tSm+M2CSh5bU0de0PCDkVEuHJlLqIMF8eC6rV8xv5K3NiXoFzF8UZVq1Isqx8CU4jAz9ykC3ArOn5vM3W92yKNfB48PWl+XYtxLZWxObHsNCRsYEwsw98Bi37qvn/dROfevrG3U7DQWgKcnFXFAFq9sikj30VqNVWcTq4eBPwAFwM/qE6tN1to+De5TZq1tdTvQt8TqkUfg3HOhvLzxeF4e/PWv7jaRbuDCORX8fWkNiSa/zrkBeH//Pl1ydt8fF1Zx5WdVzbq1FwThsYmFHNqvY+0pOmNTPMXgFzbi1Xf1yH5hnplUlPGYRKTn6ZLidWPMVGCttfa9Dn79+caYWcaYWevWretoGJ3zxRdQ7XGsSmUlLFyY+XhEOmhuebJZUgUQCRgWtfcAwTaa1+Rcwa2S+Nc5f1VtqtGWa0MLsvgCBxHpOTqzf7IfcLwxZjHwAHCoMeZeYE39FiD1/671+mJr7W3W2lJrbWn//v07EUYbxePuYLSG9tgDoh71Jfn57jaRbmLf4hBeu6G1KcuuBR1vQtqaffqEaKlEbI8ues7tGZkbxCt9CgB7q4N8RqUSkFIuK71QhxMra+0vrLXDrLWjgDOAF621ZwGPA9Pq7zYN+E+no+yMmTNhwgTIyYGCArjkEpdkARx+OIwf727bKhKBoUPh+OP9iVekA344Kpe8oGn0Cx0LwGmDcxie2zVJzplDopSEA4QarBBFAzC5KOxbU9FY0HDZmFizI4Ryg3DleB0UnQlli+Cew+H/ovD7KDz4Naj0fHst0jN1RcXvNcARxpgFwBH1n/tj9myYOhXmzXOrVZWVcMst8N3vutsDAXj5ZbjgAujf3xWtn3cevPkmhFXkKt3HwJwAs/brw8mDIhSFDMOjAX49Psb03fK77DnzQoZ39+vD2UNzKA4bBuUYLhqdy5N7e3fOz5RfjsvlrxPyGBcLUBgyHN43zGtT+rBLgVasulpdBdy+DyyeCTbpVq0++y9M30+rV9J79OzO66ee6grUm36P0SgsX+4SKRERSYv3b4enfwLxJi0BIwVwygMw/lh/4hJJt97beX3OnOZJFbjtvsWLMx6OiEhPtm5u86QKIFkHGz7LfDwifujZidXEiRD0qC+pq4OxYzMfj4hIDzZoT4h47D4HwzDgK5mPR8QPPTuxuvzy5lf9xWLwve+5LusiIpI2u5wKuSUQaFDOFoxA8VgYfYh/cYlkUs9OrHbe2RWnH3CAu/Jv8GC46iq44Qa/IxMR6XFCUTjvbZhwGoTzIKcQ9jgXvvkymJ7910bkSz27eF1EREQkzXpv8bqIiIhIBimxEhEREUkTJVYiIiIiaaLESkRERCRNlFiJiIiIpIkSKxEREZE0UWIlIiIikiZKrCSznn0W9t7bdb6fPBmef97viKQXeHpdHaWvldHn2Q3s8/omXlxf53dIItJDKbGSzPnvf+HEE2HWLNi8Gd55B44/Hp580u/IpAd7bHUtX3tvC+9tSbI5YXl7c4KvztrC0+uUXIlI+imxksy5+GKorm48Vl0NP/uZP/FIr3DxvEqqU43HqlLws3mV/gQkIj2aEivJDGvh88+9b/vss8zGIr1GyloWNs2q6s2vTGY4GhHpDZRYSWYYAwMGeN82cGBmY5FeI2AM/cLG87ZBOXr5E5H00ytLOsydCyefDIMHw8SJ8Oijrd8/kYAbb4QddoBhw+DCC2H9+szEmmkzZrg5GTzYJVC5uY1vj8Xgl7/0JzbJCm9vinPk25sZ9PwGDnxzEzM3pLf26YpxucSCjcdiQbhy3LafxRU1Sc77qJwhL2xgwstl3La0mlQWHFAvIt2PsVnw4lFaWmpnzZrldxgd8+mn7iq3ykq33QUuWbjmGpcweTn9dHjiCaiqcp+Hwy7xmDMH8vMzE3cm/OUvcPnl275PgEjE/RePuyTrV7+Ciy5yK1rS67yyMc4x72ymqsFuXSwA/9qjgOMH5aTlOay1XLewmqu/qKY2ZckNGH49Ppcfj8rFGMP6uhQTXimjrM6SaBDDN4dFuXnXHvT7KCJpY4x5z1pb6nmbEqtOOv10ePhhSDWp4ygshHXrXBLR0Pz5sOeezYu48/Lg+uvhggu6Nt5Mqa2F/v2hvLzxeCAAp54Kf/sbFBdDMOj99dIr7P36JmZtTjQbH5Mb4ItDStL6XImUZVPCUhw2BBsk8r9dUMkfvqimpsmvcE4AFh1cwuCoFvZFpLHWEiu9YnTWG280T6rAjS1d2nx81izvZKKyEl5+Of3x+WXx4m0reA2lUvDWW9Cvn5Iq4ePy5kkVwKLqFHWp9L7pCwUM/SKBRkkVwMwN8WZJFUA0YPiwhfhERFqixKqzRo3yHk8k3IpNUyNGeN8/EoHx49MWlu8GDnTbfV5GjsxsLJK1BkS8X4IKQ4YWas7TbnxekKDHc8WtZYRWq0SknfSq0Vm//KWrqWooN9dtERYVNb///vvD0KEQCjUeD4fh/PO7Ls5M69MHTjtNxerSKq/C8qiBsbEAY18qY/83N/HEmq5t5PmTUbnkNEmsIgZ2LwgxoSDk/UUiIi1QYtVZRx0FN98MJSUuiYhG4etfh3/8w/v+xsBLL8EBB7hVqmgUxo6FZ56B4cMzGnqXu+02OOMM9z3m5kLfvnDLLXDEEX5HJlni/OFRfjk2Rn7QXakXDYA18OGWJIuqU7xeluD0D7Zw0+Lq7T9YB00oCPHoxEKGRQPkBlxSdWS/ME+UFnbZc4pIz6Xi9XRJJGDVKpdg5eW17Ws2boSaGndFYE++Kq6iAsrKYMgQ1VWJp7qUZXVtit8uqOLuFbUkmrws5Qdh3eF9iXrt2aWJtZYVNSnyQ4Y+Yb3nFJGWtVa8rnXudAmF2r/iVJLeq56yVn5+z2ojIWkXCRhG5AZ5dWO8WVIFYIDPKpPsVth1L1nGGIblKvEXkc7R2zIRyRrDc71fkuosDFSndBHpBvRKJSJZ4+djYs2K2XMCcFS/sBIrEekW9EolIlnjiP4R/rxzHoUhQ37QJVXH9I9w7x4FfocmItImqrESkazynRG5TBsWZWFVkn6RAP1a6HUlIpKNlFiJSNaJBAw75evlSUS6H70VFBEREUkTJVbd1aZN8Pvfwz77wAknuKajIiJdrHwVPHcp/HMSPHImrHrf74hEsovW2rujTZtgzz1h9WrXYBTg+efh2mvhhz/0NzYR6bE2LYHbJkJtOaTqYNV7MP8/cPK/YMfj/Y5OJDtoxao7uvnmxkkVQFUVXHqp63IuItIFXvo11GxySRWATUG8Cp74nvtYRJRYdU9PPNE4qdoqEoHZszMfj4j0Cl88BzbZfLxmE2xZkfl4RLKREqvuaOBA7/F43B10LCLSBWItnMJlU5CjM6tFACVW3dNPfgKxWOOxQMAlVT/9KZx0Ejz5JGTBAdsi0nNMuRjCTV56gjkw/liIFvkTk0i2UWLVHR18MFx3nUuuioogN9d9vGEDPPMMPPYYnHYaXHyx35GKSA+y+zTY+4cQikJOEYRyYcT+cOJdfkcmkj2MzYJVjdLSUjtr1iy/w+h+KipcTdWcOXDJJc0L16NR+OQTGDvWn/hEpEeq3ghrP4HCYVA8xu9oRDLPGPOetbbU6zatWHVn+flwwAHw0UfeVwMGAvDii5mPS0R6tNwSGHmgkioRL0qseoJ+/SAcbj4eDEJxcebjERER6aWUWPUE3/wmhDx6vQaDcNxxGQ9HRESkt1Ji1ROMGQP33OO2BgsLoaAA+vd3hey5uX5HJyIi0mvoSJue4pRT3OrU669DTg7su69bsRIREZGMUWLVk+TmwuGH+x2FiIhIr6WtQBEREZE00YpVJlgLM2fCAw+47bmzzoL99vM7KhFfrKxJcvuyGj6rTHFAcYizhkbJCxm/wxIRSQslVplwwQVw771QWQnGuELzCy+Ea67xOzKRjHp7U5zD395M3EJtCh5bU8sfvqjm3f360D9HC+gi0v3playrzZoF/+//uaQK3OpVVRXcdBPMn+9vbCIZZK1l2ocVVCRdUgVQmYSVtSmuWlDpb3AiImmixKqr/fe/UFPTfDyVcgcli/QSa+ssi6uTzcbjFmasqfMhIhGR9FNi1dXy8lpu3hmLNR8X6aFyAm7B1ks0oBorEekZlFh1tdNP9+4nZS2cfHLm4/FbeTn8/e+u7uwf//A+41B6pD7hAPuXhJsVdsYC8L0RUV9iEpHmNi2Gl66Cpy6EBU+BTfkdUfdibEtvITOotLTUzpo1y+8wus6998L5529buUom4f774YQT/I0r0xYvhsmTXb1ZZaVbzcvPh3fegREj/I5OMmBVTYqD397Eyhr3Sp20cFT/CA/tWUBYq1Yivpv3KMz4BtgkJOsgkg/D94Uz/wcBXe72JWPMe9baUs/blFhlSFmZO2ImGISjj3bHzvQ2xx0HTz/t6su2CgRg6lT4z3/8i0syKmUtr2yMs6Q6RWlRiF0K9Gotkg0SNXD9AKgrbzwezoPjboXdz/YnrmzUWmKlV7RMKS6GM87wOwr/WAvPPts4qQL3+dNP+xOT+CJgDAf3jfgdhog0sewN1xGoqXglfHyfEqu2Uo2VZE5LZxfqTEMREd8Fwi1fYBJSGWSbKbGSzDAGTj0VIk1WKiKR3r2SJ9LAhgXwyu/hpd/A6g/8jkZ6m+FTvBOocB7sdV7m4+mutBUomXPTTfDhh7BokSvgDwZh7Fi48Ua/IxPx3Tu3wHM/g1TCXYX1+nUw6UI44lq/I5PeIhCCr/8X7j3K/QymEoCFPc+F8cf5HV33oeJ1ySxr4aWXYN48mDABDjrIe1NfpBcpXwk3jXXFww2FY/DNV2DIRH/ikt4pXgWfPQHVG2H0YdB3vN8RZR8Vr0v2MAYOOcT9JyIAzP8vGI/CjHgNzP23EivJrHAMdjnN7yi6L9VYiYj4LBAEPBZujQGjaztEuhWtWEl6rV8PDz8MmzfDkUfCnnv6HZFIVrAWlr8Ji1+GvP4w4VSIFrnbdjzedbluKhiBr3w9s3GKSOcosZL0efZEcy8lAAAfdElEQVRZOOkk93FdHfz2t+6Kv9tvVx2V9GqpJDz0NVj4AiRqIZQDz/wUzn4Whu0DeQPg+Nvh8e+4+9uU+5U56EoYsKu/sYtI+6h4XdKjpgYGDoQtWxqP5+XBAw+47uoivdTsO92KVLyy8Xj+YPjp8m31VRWr3ZEiyTq3ilU8OvOxisj2tVa8rhorSY9XXvEer6yEu+7KaCgi2Wb29OZJFbijQxr2q8ofBHtfAPv8WEmVSHelxErSo7WVzyxYFRXxlX49RHoNJVaSHgcd5P0XIi8Ppk3LfDwiWWSPc1336qbCeTBY13eI9ChKrCQ9olFXSxWLuY8DAZdUnXQSfPWrfkcn4qs9psGog+qTKwOhGETy4bSHvftXiUj3pasCJX2OPRYWLoQHH3RF7EcdBXvv7XdUIr4LhODrT8CSV2DJyxDrD7ueDrklfkcmIummqwJFRERE2kFXBYqIiIhkgLYCRUQko5J18PnTULkORh4AfXfwOyKR9FFiJSIiGbNuLtx1CCSqwSbdxcRf+QZ89TYd0CA9g7YCRUQkI6yFfx0PVWtdc9R4lUuwPvkXzHnQ7+hE0kOJlYiIZMS6Oe7YnqbilTDr1szHI9IVlFiJiEhGJGpa7tsVr8psLCJdRTVWIiKSEYP2gGC4+XgoF75yVuOxdXPdOYrFY2HoJNVfSfehxEpERDIiEIKT7oV/nwKphLs6MJIP/XaG0u+6+yTr4KFTYeFz7v425a4aPOd5NVSV7kGJlYiIZMz4Y+D7c2H2dChfCWOPhJ1O3LaS9erVLqlKVG/7mrWfwOPnwekz/IlZpD2UWImISEb1GQmHXOV923v/bJxUAaTi8NkTrkYrFO36+EQ6Q8XrIiKSNZomVQ0l6zIXh0hHKbESkV5py3L49D+warbrryTZYfyxYILNx/tPgJzCzMcj0l7aChSRXsWm4IkL4MO7IZQDqaQrjj7rGcjr73d0cvi1sPB5qC2HRBUEcyAYgePv8DsykbZRYiUivcp7t8HH90Ky1v0Hrjh6xllw9jP+xiZQOBR+ON8Vty9/c9sVgwVD/I5MpG2UWIlIr/L2X5s3o0zFYclLUL1Rl/Rng2gRTLkIuMjvSETaTzVWItKr1G7xHjdBqKvIbCwi0vMosRKRXmWHqRDw6P4d6weFwzMfj4j0LEqsRKRXOfjXLokK5brPTQjCMThhuo5NEZHOU42ViPQq+YPg+3Pg/X/Coheh73iYdKG7MlBEpLOUWIlIr5NbDPtd6v4TEUknbQWKiIiIpEmHEytjzHBjzExjzDxjzBxjzI/rx0uMMc8ZYxbU/1ucvnBFRNKjZjMsexM2L/UvhlQCVs5yfbTU/V2kZ+jMVmACuNha+74xpgB4zxjzHPBN4AVr7TXGmMuAy4Cfdz5UEZHOsxZe+g28cZ3r6J2sg5EHwan/hpyCzMWx4EnXlDSVcN3g8wfB1x93R7eISPfV4RUra+0qa+379R+XA/OAocAJwN31d7sbOLGzQYqIpMvH98ObN0CixvW0StTA4pfgP+dmLoZNi+GhU6GmDOrKIV4JZQvhrkMgGc9cHCKSfmmpsTLGjAL2BN4GBlprV4FLvoAB6XgOEZF0eON6l8g0lKyFz55w24OZMHs62ESTQQuJavhCx+qIdGudTqyMMfnAI8BPrLUt9DT2/LrzjTGzjDGz1q1b19kwRETapKqFl5tAEGo2ZSaG8hVuC7Ipm4LKtZmJQUS6RqcSK2NMGJdU3WetnVE/vMYYM7j+9sGA58uEtfY2a22ptba0f38dKS8imTH6cHd8TVORfCjKUOf1sUdBOL/5uE3CiAMyE4OIdI3OXBVogDuAedbaPzW46XFgWv3H04D/dDw8EZH0OuQqyClscKyNcZ3Xj70FTIYa0Ox0EvTfaVv3d4BwHux+jmtYKiLdl7EdvMbXGLM/8CrwMZCqH74cV2f1EDACWAqcaq3d2NpjlZaW2lmzZnUoDhGR9tqyAt78oytaLx4D+14KwyZnNoZ4Nbx3G3x8n0vsSi+AXU7TsToi3YEx5j1rbannbR1NrNJJiZWIiIh0F60lVuq8LiIiIpImSqxERESk27PWnaRQvsrfOHQIs4iIiHRrK2fBI2fCluWubcmAXeCUh6BkbOZj0YqViIiIdFtV6+HuQ2HjAtdkN1kLqz+AO/f37hfX1ZRYiYiISLf14f9zZ242ZFNQV+nO5Mw0JVYiIiLSbW1e4laqmkrF3dZgpimxktalUrB6NVRV+R2JSFqlkq7INVHjdyTiJZWo//9T63ckku2G7+dOTmjKBGDopMzHo8RKWjZjBgwbBqNHQ0kJnHsuVHu8LRDpZj64B24YBDeNgWtL4H8/gGTc76hkq3dugev7w01j4boSeO5SlwiLeNnpROgzGoI528ZCuTDiQH8SK10VKN5efx3OPrvxStUDD0BlJTz0kH9xiXTSgqfgyQsg3uBH+4M7XU3G1Fv9i0ucTx6E5y9p/P/n3ZshEILDrvYvLslewTB863V4/Tp3kkEwAnt9Byb/yJ941HldvE2dCv/7X/PxnBxYuhQGDMh8TCJpcMcUWP5W8/FQFC5ZD5G8zMck29y8M6z/tPl4OA8u2+QSLBG/qfO6tN8XX3iP5+TAihWZjUUkjTYt8R43Qahal9lYpLnyld7jyTjUlmc2FpGOUGIl3vbdF4LB5uPxOIwfn/l4RNJk6CTA46DjQAgKhmY8HGli4B7e47ESiBZlNpZstTXJzIINJ/GgxEq8XXEFxGJgGvwFisXg5z+HfI/LL0S6iUN+B4Fw4zETgoN/62o1xF9HXAvhWOOxcAyOuN5d5dWbJWrgie/CNYWuqP9vO8DCF/yOSprq5T+m0qIxY+Ddd+Gkk6BfP5gwAW69Fa680u/IRDqlci0EmrzyBYKwaZE/8Uhjw/aBaTNh9GEQ6weDJ7qjSXY7y+/I/DfjLPjwHpdgpRKw8XN44HhY85HfkUlDKl4XkV5l+gGw7LXm46FcuHR989USkWywZQX8dVzzvmsmALucASff509cvZWK10VE6pW1cF2GCbjVLJFstHlJ4z5NW9kUrJ+X+XikZUqsOiOpjnUi3c2gPfEsXjcBKBiS8XC2y9ru0RwzlVQxdVfqu6M7XLipQAiGTs58PNIyJVYdMX06DBkCoZD7d/p0vyMSkTY69HcQzm08Fo7BQb9yjQWzRaIGnrwQrs6D34Xhtr1hxbt+R9Xcylnwz71djFfnwZM/hLgOaEi7WF/X9LLRVrVxW9j7XepbWOJBiVV73XUXXHghrFrlPl+1yn1+992+hiUibTN4LzjnRXfcRSQfSsbBsbfAlJ/5HVljD58Os2+vP1zWwqpZcPehsLGFrUw/lC2Euw9xyRXWxTr7Dnj4NL8j65mO/jMc+nsoGgGRAhh3NJz3FhSP9jsyaUjF6+01YgQsW9Z8fPhw15FcRKSTyhbBLROaFyoHwjDxu3DsX/2Jq6mnfgyzboVUk3MWQ1H4/hwoHuNPXCJdTcXr6bR8ufe4upGLSJps/Ny7UDkVhzUfZD6elqz+oHlSBS72DQsyH49INlBi1V6jRnmPjxyZ0TBEpOfqt1MLhcphGOL5HtkfQyd516Ulat33INIbKbHaHmvhT3+CQYMgHIZUyp2X11AsBtdck9m4PvgADjzQxVRS4hp3JhKde8zHH4eddnJF+SNHqm5MxCdFw2HHE11hckOhKOxzUccft3IdPPIN+H0Mfp8Lj5zpxjpq8o9cTA2vsgzlwk7HQx+915ReSjVW23PFFfDnP0NV1baxSAQGDoTVq2H0aLj6ajj55MzF9MUXsMceUFGxbSw3F045Be65p2OP+cQTcPrpjb/PWAxuvBHOP79z8YpIuyXj8PJvXQ1TXTmMOMAVLw/YteOPd/POsHnptu27QAgKR8APP+34cT5r58AzP4Elr7iC6tLvwUG/1vFA0rO1VmOlxKo1VVXuOJfqJtcOGwPHHAP/+58/cV1wAdx+e/MVqpwcWLQIBg9u/2PuuivMmdN8fMAAl0Aaj8Y/ItJtzHsUHjsH6ioaj0cK4IQ7YUIG3xuKdHcqXu+oFSsgGGw+bi18/HHm49nqvfe8t/2iUfjss4495hctXMO9YQPU1HjfJiLdxro5UFfZfLyuwt0mIumhxKo1Q4a03F19woTMxtLQ7rt7J3y1tTBuXMces6Wi/OJil7CJSLfWbyeI5DUfj+Sr0FwknZRYtSYvD37wA1dr1FBODixY4G7fbTdXn5RJl1zSPNnJzYUTToChQzv2mH/4Q/PvMxaD3/xG24AiGVBX4fpCXdcXrimCR8+BFy6HG4bA1flw/1RYP7/jj7/j8ZDbF0xo25gJQW4x7HRi5+MXEUeJ1fZcey1cfrlbuYFticvCha4G6+OP4bTT4NFHMxfTDjvAiy9CaalLevLzXQLY0cJ1gBNPhDvv3NY2YtAguOEG+P730xOziLTIWtdV/b1/QPVGqN0CH90Lr10DFasgXgkLnoTbJ8OWDrbMC0Zcl+4dj3dF64EQ7PhV+PZb2XWUj0h3p+L19kilXFLjVY80bpxbxfIjpkCa8+OueEwRadHil+FfU5sXljcVjMCkH8GR13fu+ba+7GsxWqRjWiteD3kNSgsCAbdS5aWl8a7WFQmQkiqRjFrzoWuHsD3JOljxVuefTwmVSNfRX9D2aqmVQUdaHIiI4A6Cbst2nAlB/w72sRKRzFBi1V6/+U3LRd4ikpW+eM7VJ11bAnfsC4tf8juixsYeBXkDXN1Ta0I5MKUTnddFpOspsWqv886D665zjUNDIffv9de7cRHJOp/+Bx44AVa8AzVlsPxNuO9Y+OJZvyPbJhCEb70O4452yZUJwrD9YMKp7kBjE3Qd189+Fvru4He0ItIaFa93lLXuqsBYTAULIlnspnFQ5nG9Sf9d4fs+9vltSbIObKr+DD4glXBj4VjrXycimaPi9a5gjOtjJSJZy6a8kyqADZ9mNpa2alprtbU1goh0D9oKFJEeywQg1s/7tvxBmY1FRHoHJVYi4qsV78K9R8MNQ+HuQ2DJK+l9/P1/0XwbLRyDA36Z3ucREQFtBYqIj5a+BvceBfEq93nFSrj3GDj1QdhhanqeY5+LIFHjupin4q4Y/MBfwcTz0/P4IiINqXhdRHzzz0mw8t3m48Vj4Ect1EZ1VDLurgrMLVHNkoh0TmvF69oKFBHfrPnIe7xsUds6kbdHMNy2XlEiIp2hxEpEfJM3wHs8p0AJkIh0T0qsRMQ3LRWWT7m45fZwyTp4809wy67uvzf+CInaro+1q6US8M7N8Pfd4eYJ8Mrvt9WeiUj3oRorEfGNtfDq/8Hr17mPbQom/QAOv9a1SvC6/z2HwfK3IFHtxkK5MKQUvvmS99d0Fw+cCAuf25ZMhaLQfxc47y2t3olkGzUIFZGsZIy7Qm/fS6B8FeQPbL3D+JKX3dE0W5MqcB+vng0LX4CxR3R9zF1h5XuNkypwVzJumA/z/ws7n+RfbCLSPt34/Z2I9BShKBSP3v6xLcvedAlHU3WV7gzA7mrZG261rqm6ivT39RKRrqXESkS6jYLBbuuvqXAM8gdnPp50KRgCgXDz8VAuFA3PfDwi0nFKrETEVxs+g/98C27dDR45s+UWDAATToGgRwFDIAS7nt51MXa1HabWJ4xNCvYDQdjtbF9CEpEOUmIlIr5ZNRv+MRE+vAfWfgxzHoQ7psDil73vH8mHaS9ByXi3ShWOQfFYmPYi5BRmNPS0CuXAuS9D/51dghWOQdEIOOtZyOvvd3Qi0h66KlBEfHPnQbDUo4ao/y7w/U9a/jproWwhYF1i1VJrhu6obJE7eqdkfM/6vkR6El0VKCJZacXb3uPr5rrO60GPuiNwCUfJ2K6Ly0/Fo/2OQEQ6Q1uBIuKbaB/v8XBMvZtEpHtSYiUivtnnJ81bLIRyYeL52gaT7LfgKbh/KkzfH96+SZ3yxdF7QhHxzX6XwpblMPsOCOa4HlUTToHDr/E7MpHWzfw1vHkDxCvd56tnw+zprlN+KOpvbOIvJVYi4hsTgGP/Bof8FjYscPVFLR3MLJItKta4Y5iSDZrVxqtg4+fw8b9gz3P9i038p61AEfFdbgkMm6ykSrqHpa95X1gRr4T5j2c+HskuSqxERETaIdbXe9wEIX9QZmOR7KOtQBHJask6+Og+mPMQRIug9AIYdZDfUUlvNuIAyClyZznSoBVkKAf2vsC3sCRLKLESkayVjMNdB7tjbrYWCX/2XzjgCjjgcl9Dk14sEIRpL8B9x0DlWlcraFNw3K0wcDe/oxO/KbESkaw156HGSRW4IuFXfgd7naeaLPFP3x3gws9h9QdQVw5D9oawxwHh0vuoxkpEstanjzVOqrYKRmCJx1E4IplkDAzeE0YeqKRKtlFiJSJZK9bPbbM0ZW3LXdtFRPzU+xKrZBIefhhOPx3OOw/e9jis7P334Xvfg9NOg/vvh3g883GKCBPPh6BHs8VwLow6OOPhiIhsl7HWbv9eXay0tNTOmjWr658omYRjj4XXX4fKSggEIBqFq66Cn/3M3ee22+Cii6CmBlIpyMuD3XeHmTMhEun6GEWkkff/CU/92PUNshYi+XDW0yoSFhH/GGPes9aWet7WqxKrGTPgnHNcUtVQNApLlrh/Bw2C6urGt+flwS23uK8VkYyrLXdNGXMKYNgUd1WWiIhfWkusetdW4COPNE+qAMJhePFFeO0193FTlZXw4INdH5+IeMopgPHHwIj9lVSJSHbrXYlVUZHb/mvKGCgogPx8t9fgdXsfVcqKiIhI63pXH6vzzoO774aqqsbjwSAcfjiEQm7br7y88e25ua6YvSstWQK33w7LlsGRR8Ipp6imSwTXeHHBU/DpDHcl4B7nwoBdG99n3VyYPR1qymDHE2GH47yvJuyM1R/CB3e5btsTToaxR7n3XCIiDfWuGiuAv/0NLrlkW9ISDMJTT8Hkye7zDz90iU1NjVu9qquDX/8afvGLrovp2WfhpJMgkXDPl58PY8e6Ivu8vK57XpEsl0rCAyfC4pcgXuHOYgtG4Og/uysGAWbfCU/+wHVptwlX3D58Pzjzf+nbNnz7Jnj+MkjWukQvnAfjj4VTHlRyJdIbqXi9qY0b3VV+eXlw6KHNV4YSCXf75s1w0EHQv3/XxZJMwuDBsG5d4/Fo1CV0l13Wdc8tkuXmzYBHz2neJDQUhZ+udInTHwdBosn1JuE8OP4O2PX0zsdQuRb+PBISNc2f49R/u9ovEeldVLzeVEkJnHwyHH2093ZbKARHHOG247oyqQKYM6f5VYjgVsweeKBrn1sky815qOXO64tnwuKXXRuGpuKVMCdNvz5fPAcBj6KJeCXMezg9zyEiPUfvqrHKRtGo65flJRbLbCwiWSacBxjAY2E9lOud8ID7mnB+emIIRetjaPoUwfr4REQaUGLlt/HjYeRI+PTTxlck5uXBBRd07rHnznWd42tr4WtfgylTWr9/dbVrK/H++7DzzvCNb0BhYediEOmEvb7tVp7iTa43IQCjD3UF6l7JVTgXJn4nPTGMPwbPxC6Y4wrpRUQa6p1bgdnEGHjsMdeYtKDAJVTRqDtO5xvf6Pjj3nQTlJbCtdfCDTe4qx4vuMC7nQTA6tWw445w4YXw17+6Av8xY+Dzzzseg0gnDd8X9r/crRpF8iFSADmFcOYTEMpx24Bn/g9y+kCk0K1ShaKw76XuYNx0CMfgjMe3PX+k/jkO/Z07gFdEpKHeWbyejRIJeO45l+Dsv79byeqolSvdVYU1TaptYzH3HPvu2/xrzjrLrVYlEtvGAgE48EBXyC/io/KVsPB5l9SMO8atSDWUqHEtGWq3wJjDoXBo+mOoq4TPn4J4NYw9AvIHpf85RKR7aK14XVuB2SIUgmPSdHnRU095N0KtrnYHUHslVo8/3jipAlf79eqrrgWEemqJjwqGwO6tnCgVisLOJ3VtDJE8mHBK1z6HiHR/2grsicJh78QqEGg5QQq20PDHGO/HEhERkWb0F7MtNm+G226DK6+EJ590vaey2Ve/6h1jJNJy3dZZZ0FOTuOxUAimTnX/ioiIyHbpL+b2fPihaxIaj7ujcPLz3RVzL72Uve0QiovhvvtcEhUIuIL1VAp+9zv4yle8v+bqq+Gtt9zViYmEW/UaNAj+8Y/Mxi4iItKNqXi9Nda6JGr+/Mbj0Shcfjn86lf+xNVWGze62qnaWjjuOBg2rPX7WwuvvAIff+yK5484QtuAIiIiTehIm45auhR22sm7M/q4cbBgQeZjEhEREV/pSJuO2rqN1tJtIiIiIg0oO2jNsGFuZarp8fW5ufCtb/kTk4iIiGQtJVbb89BD7tDm/Hx3dVx+PkyaBD/5id+RiYiISJbRVYHbs/POsGwZzJgBK1bA5MmuG3nTVSwRERHp9ZRYtUVubufO7RMREZFeQVuBIiIiImmiFSsR6XVSKfjgTvjiaSgZDwf8EiJZ2u9XRLoXJVYi0qvUVcCfR0H1hm1jr18L58yEUQf6FpaI9BDaChSRXuWhUxsnVQA2Bfcf6088ItKzKLESkV5l0fPe4/FKWDsns7GISM+jxEpEepXWTvFK1mYuDhHpmbossTLGHG2MmW+M+dwYc1lXPY+ISHsMnug9HozA4L0yG4uI9DxdklgZY4LAzcAxwATg68aYCV3xXCIi7XH6Iy6JauqE6ZmPRUR6nq66KnAS8Lm1diGAMeYB4ARgbhc9n4hImxQOg0s3wIu/gsUzoc9oOOI66Dve78hEpCfoqsRqKLCswefLgcld9FwiIu0SyYejb/Q7ChHpibqqxsrrIL1GJaPGmPONMbOMMbPWrVvXRWGIiIiIZE5XJVbLgeENPh8GrGx4B2vtbdbaUmttaf/+/bsoDBEREZHM6arE6l1gvDFmtDEmApwBPN5FzyUiIiKSFbqkxspamzDG/BB4BggC0621ar0nIiIiPVqXnRVorX0SeLKrHl9EREQk26jzuoiIiEiaKLESERERSRMlViIiIiJposRKREREJE2UWImIiIikiRIrERERkTRRYiUiIiKSJkqsRERERNJEiZWIiIhImiixEhEREUkTJVYiIiIiaaLESkRERCRNlFiJiIiIpIkSKxEREZE0UWIlIiIikibGWut3DBhj1gFL/I6jA/oB6/0OogfRfKaP5jJ9NJfpo7lMH81l+nRkLkdaa/t73ZAViVV3ZYyZZa0t9TuOnkLzmT6ay/TRXKaP5jJ9NJfpk+651FagiIiISJoosRIRERFJEyVWnXOb3wH0MJrP9NFcpo/mMn00l+mjuUyftM6laqxERERE0kQrViIiIiJposSqjYwxw40xM40x84wxc4wxP64fLzHGPGeMWVD/b7HfsXYXxpigMWa2MeaJ+s81lx1gjOljjHnYGPNp/c/nFM1lxxhjLqr//f7EGPMvY0xUc9l2xpjpxpi1xphPGoy1OH/GmF8YYz43xsw3xhzlT9TZqYW5vL7+9/wjY8yjxpg+DW7TXLbAay4b3PYzY4w1xvRrMNapuVRi1XYJ4GJr7c7APsAPjDETgMuAF6y144EX6j+XtvkxMK/B55rLjvkL8LS1didgd9ycai7byRgzFPgRUGqt3RUIAmeguWyPu4Cjm4x5zl/96+cZwC71X3OLMSaYuVCz3l00n8vngF2ttbsBnwG/AM1lG9xF87nEGDMcOAJY2mCs03OpxKqNrLWrrLXv139cjvvjNRQ4Abi7/m53Ayf6E2H3YowZBhwH3N5gWHPZTsaYQuBA4A4Aa22dtXYTmsuOCgG5xpgQEANWorlsM2vtK8DGJsMtzd8JwAPW2lpr7SLgc2BSRgLtBrzm0lr7rLU2Uf/pW8Cw+o81l61o4ecS4EbgUqBhsXmn51KJVQcYY0YBewJvAwOttavAJV/AAP8i61b+jPuBTjUY01y23xhgHXBn/bbq7caYPDSX7WatXQH8EffudRWw2Vr7LJrLzmpp/oYCyxrcb3n9mLTNt4Cn6j/WXLaTMeZ4YIW19sMmN3V6LpVYtZMxJh94BPiJtXaL3/F0R8aYqcBaa+17fsfSA4SAvYBbrbV7ApVoq6pD6mt/TgBGA0OAPGPMWf5G1aMZjzFdpt4GxpgrcOUp920d8rib5rIFxpgYcAVwpdfNHmPtmkslVu1gjAnjkqr7rLUz6ofXGGMG198+GFjrV3zdyH7A8caYxcADwKHGmHvRXHbEcmC5tfbt+s8fxiVamsv2OxxYZK1dZ62NAzOAfdFcdlZL87ccGN7gfsNwW6/SCmPMNGAq8A27rV+S5rJ9xuLeQH1Y/3doGPC+MWYQaZhLJVZtZIwxuDqWedbaPzW46XFgWv3H04D/ZDq27sZa+wtr7TBr7ShckeCL1tqz0Fy2m7V2NbDMGLNj/dBhwFw0lx2xFNjHGBOr/30/DFdLqbnsnJbm73HgDGNMjjFmNDAeeMeH+LoNY8zRwM+B4621VQ1u0ly2g7X2Y2vtAGvtqPq/Q8uBvepfTzs9l6G0R9xz7QecDXxsjPmgfuxy4BrgIWPMt3EvzKf6FF9PoLnsmAuB+4wxEWAhcC7uTZPmsh2stW8bYx4G3sdts8zGdWTOR3PZJsaYfwEHA/2MMcuBX9PC77W1do4x5iHcG4EE8ANrbdKXwLNQC3P5CyAHeM7l/rxlrf2e5rJ1XnNprb3D677pmEt1XhcRERFJE20FioiIiKSJEisRERGRNFFiJSIiIpImSqxERERE0kSJlYiIiEiaKLESERERSRMlViIiIiJposRKREREJE3+P6WQT0mGv2muAAAAAElFTkSuQmCC
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
<h1 id="interpreation">interpreation<a class="anchor-link" href="#interpreation">&#182;</a></h1><p>You can see the data points in the form of five clusters. The data points in the bottom right belong to the customers with high salaries but low spending. These are the customers that spend their money carefully. Similarly, the customers at top right (green data points), these are the customers with high salaries and high spending. These are the type of customers that companies target. The customers in the middle (blue data points) are the ones with average income and average salaries. The highest numbers of customers belong to this category. Companies can also target these customers given the fact that they are in huge numbers, etc.</p>

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
 
