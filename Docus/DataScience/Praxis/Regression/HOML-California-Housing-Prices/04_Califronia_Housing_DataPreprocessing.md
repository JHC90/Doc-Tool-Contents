'''''

{
"title": "Data-Preprocessing-Checklist",
"keywords": "DataPreprocessing, ",
"categories": "",
"description": "Hier geht es um die individuelle Abarbeitung der <em>EDA</em>-Checkliste im Kontext der California-Housing Problematik",
"level": "30",
"pageID": "16112020-10-California-Housing-Data-Preprocessing-Checklist"
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
<center><h1>California Housing <br> Data Preprocessing</h1></center><p><img src="imgs/2020-11-14-21-31-19.png" alt=""></p>
<p>In diesem Notebook wird die <a href="16112020-EDA-Checklite">EDA-Checkliste</a> im Kontext des California-Housing Problem abgeabreitet. Bei dieser Checkliste geht es darum, die Datenstruktur grundlegend zu verstehen. Hier werden die Daten lediglich beschrieben, das ist wichtig bevor die Modellierung startet.</p>
<h1 id="Laden-der-Daten">Laden der Daten<a class="anchor-link" href="#Laden-der-Daten">&#182;</a></h1><p>Die Daten wurden bereits im vorherigen <a href="14112020-10-California-Housing-Data">Notebook - California Housing Priceses Data</a> gesplittet und persistent auf der Festplatte gespeichert. Somit müssen diese Daten in diesem Notebook zunächst geladen werden. Die Funktion Daten-Laden wurde in diesem Notebook der übersichtlichkeit wegen ebenfalls ausgelagert.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># To support both python 2 and python 3</span>

<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">tarfile</span>
<span class="kn">from</span> <span class="nn">six.moves</span> <span class="kn">import</span> <span class="n">urllib</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="kn">import</span> <span class="nn">FunctionFileCalifornia</span> <span class="k">as</span> <span class="nn">ffc</span>

<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">matplotlib</span> <span class="k">as</span> <span class="nn">mpl</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Basic Variables</span>
<span class="n">DOWNLOAD_ROOT</span> <span class="o">=</span> <span class="s2">&quot;https://raw.githubusercontent.com/ageron/handson-ml/master/&quot;</span>
<span class="n">HOUSING_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;housing&quot;</span><span class="p">)</span>
<span class="n">HOUSING_URL</span> <span class="o">=</span> <span class="n">DOWNLOAD_ROOT</span> <span class="o">+</span> <span class="s2">&quot;datasets/housing/housing.tgz&quot;</span>
<span class="n">PROJECT_ROOT_DIR</span> <span class="o">=</span> <span class="s2">&quot;.&quot;</span>
<span class="n">CHAPTER_ID</span> <span class="o">=</span> <span class="s2">&quot;end_to_end_project&quot;</span>
<span class="n">IMAGES_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_ROOT_DIR</span><span class="p">,</span> <span class="s2">&quot;images&quot;</span><span class="p">,</span> <span class="n">CHAPTER_ID</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>.\images\end_to_end_project
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">()</span>
<span class="n">strat_test_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_test_set.csv&quot;</span><span class="p">)</span>
<span class="n">strat_train_set</span> <span class="o">=</span> <span class="n">ffc</span><span class="o">.</span><span class="n">load_housing_data</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;strat_train_set.csv&quot;</span><span class="p">)</span>
<span class="c1">#print(housing.shape, strat_test_set.shape, strat_train_set.shape)</span>
<span class="c1">#print(strat_test_set.head123(5))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Vertikaler-Cut">Vertikaler Cut<a class="anchor-link" href="#Vertikaler-Cut">&#182;</a></h1><p>Im vorherigen <a href="14112020-10-California-Housing-Data">horizontalen Cut</a> wurden die Trainings und Testdaten erstellt und auf der Festplatte gepseichert. In dem Vertikalen Cut werden nun die Trainings und Testdaten in jeweils beschreibende und zu erklärende Variable aufgeteilt = Supervised Learning.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">strat_train_set</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">housing</span> <span class="o">=</span> <span class="n">strat_train_set</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">&quot;median_house_value&quot;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># drop labels for training set</span>
<span class="n">housing_labels</span> <span class="o">=</span> <span class="n">strat_train_set</span><span class="p">[</span><span class="s2">&quot;median_house_value&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(16512, 12)
(16512, 11)
(16512,)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Nan--Values">Nan -Values<a class="anchor-link" href="#Nan--Values">&#182;</a></h1><p>Aus dem <a href="14112020-10-California-Housing-Data">Data-Management-Notebook</a> ist klar, dass NAN/0/"" Werte in dem Feature "total bedrooms" existieren. Diese Werte werden nun in dieser Rubrik behandelt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">missingno</span> <span class="k">as</span> <span class="nn">msno</span>
<span class="n">msno</span><span class="o">.</span><span class="n">matrix</span><span class="p">(</span><span class="n">housing</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x27b8137c760&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABdkAAALECAYAAAD0PjlYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdedxtY/nH8c/3OGZCpsafSqFo1kQlKkpSFJVkiApRRKlkypShkiGZKQ2mNEgTCQ2mlNCECCVDmclwzvf3x3VvZ53tOZLhWfs5vu/Xy6vnWXut/bqfs9pr3+ta131dsk1ERERERERERERERPzvJvU9gIiIiIiIiIiIiIiIiSpB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIiIiIiIiIiIhylB9oiIiIhHiST1PYaIiIiIiIgYXwmyR0RERDwC3cC6bc/otYiIiIiIiJg5aeheMCIiIiIeIkkaBNYlrQC8AlgA+Jvtr/Q6uIiIiIiIiBgXCbJHREREPEKSNgD2A/4ELAIsCFwIfBS4YDjDPSIiIiIiImYeKRcTERER8Qi0DPZ9gJ2B1W0/A1gDWA7YCJi9v9FFRERERETEYy1B9oiIiIhH5jXAX4HjbP+zbduqbTvM9n8GO6ZGe0RERERExMwnQfaIiIiIh0HSYB71cuA/tq9u208Bng+safsCSW+W9Gl4YGPUiIiIiIiImPgSZI+IiIh4CIaz0G1PbT9eACwp6VmSTqIC7Kvb/r2k+YDXAktLWnB8RxwRERERERHjYXLfA4iIiIiYCAZZ6JLeBDzN9mHtpfOBu4BfAgZeZftvkmYF1gTWBba1/a8ehh0RERERERGPsQTZIyIiIh6EJHUC7AsBewDzS7rL9tdtnyzplcDWwLnAQpKeStVq3xH4rO1vDL9XREREREREzBwSZI+IiIiYgaEA+xrAM4EFgIWBvSVNtn207c9IuhNYA/gVcBvV+HRb2/u34yd1SsxERERERETETEJJpoqIiIh4cJLWAY4E9gSuA6YCOwO3ArvbPqLt9xTgaVSQ/Q7bV7XtCbBHRERERETMpBJkj4iIiHgQkhYGfgL8Ftjc9p1t++uALwHzAdvZ/vrQcbLtlIiJiIiIiIiYuU3qewARERERI25OYDHgEtt3SpqlZab/HPgk8H/ArpLW6x40CKwnwB4RERERETFzS5A9IiIi4sHdBFwFvELSnLanAAKw/UPg9Pb7RyS9ob9hRkRERERERB8SZI+IiIjokKTOz5Ns3wacD6wMvLUTaEfSQlR99qOBpwKr9zDkiIiIiIiI6FGC7BEREfG41w2sAwtKWljSfINmpbY3Bv4KfBF4v6TZJS0ArAosDuwDnASsJekJ4zz8iIiIiIiI6FGC7BEREfG41m1MKumdwPeA3wN/k/RxSUu2XV8PXE4F1K8DzgYOAw5t2e7zAxcDd4zznxARERERERE9mtz3ACIiIiL61Amwvw84qP23JbAZsB2wmKT9bP8FeK2k9wJLt8N/YfsUSa8AVgCOHJSSiYiIiIiIiMcHtfvKiIiIiMctScsBRwKH2P68pOcBvwL+BjwfOAT4ku0/Dh23CFWrfWfgIttvb9vvz46PiIiIiIiImVvKxURERETAYlSJmANaeZhfAMfZfiFwALARsImkpYaOewHwceBnnQD7pATYIyIiIiIiHj+SyR4RERGPe5IWBv4P+C3wY+AWYDPb10t6GXAqMBfwLeDDtm/tHPvcQYZ7C7BPHfc/ICIiIiIiInqTmuwRERHxuGf7BuAGSU8HlgJ2sX19e1nAucBfgT93A+zt2EGAXQmwR0REREREPP4kyB4RERExzWyAgWUAJM0CvBy41/aHBjuNVXM9JWIiIiIiIiIenxJkj4iIiJjmauAM4B2SngtcBbwb2L67UwLqERERERERMZCa7BERERFMy06X9ATgc8ArgHuBr9r+cnefPscZERERETOfzDMjJrYE2SMiIiIaSbPYniJpMlWLfV7b/26vpalpRERERDymJD130PMnIiaOSX0PICIiImJUtAC7bN9n+17gJkhT04iIiIh47ElaEfippBf0PZaI+N8kyB4REREzHUl6OK/B9PXWBz9n6W5EREREjINrgScBK/Y9kIj436RcTERERMxUuvUsJa0EvByYFfgO8Cfb9/630i9D77EQ8K8E2iMiIiLisdIpW3g41RtoVdtX9T2uiHhokskeERERM5VOcHwD4AfAB4CdgVOALSTNYXuqpDHnQUMB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
"
>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Unnamed: 0            False
longitude             False
latitude              False
housing_median_age    False
total_rooms           False
total_bedrooms         True
population            False
households            False
median_income         False
ocean_proximity       False
income_cat            False
dtype: bool
Unnamed: 0              int64
longitude             float64
latitude              float64
housing_median_age    float64
total_rooms           float64
total_bedrooms        float64
population            float64
households            float64
median_income         float64
ocean_proximity        object
income_cat              int64
dtype: object
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Imputation">Imputation<a class="anchor-link" href="#Imputation">&#182;</a></h2><p>In dieser Lösung entscheide ich mich dazu eine Imputaion durchzuführen. Ander Lösungen finden sich in diesem <a href="16112020-NAWerte">Notebook</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span> <span class="c1"># Scikit-Learn 0.20+</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">Imputer</span> <span class="k">as</span> <span class="n">SimpleImputer</span>
<span class="n">imputer</span> <span class="o">=</span> <span class="n">SimpleImputer</span><span class="p">(</span><span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;median&quot;</span><span class="p">)</span>
<span class="c1"># erstellen eines Sub-DF welches nur die numerischen Werte beinhaltet</span>
<span class="n">housing_num</span> <span class="o">=</span> <span class="n">housing</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;ocean_proximity&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">imputer</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="c1"># imputer.statistics_</span>
<span class="c1"># housing_num.median().values</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
<span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">housing_tr</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#print(housing_tr.isnull().any())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">housing</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#print(housing.isnull().any())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(16512, 10)
(16512, 11)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="OHE">OHE<a class="anchor-link" href="#OHE">&#182;</a></h1><p>für die kategorischen Variablen check out das <a href="16112020-OneHotEncodingOrdinalEncoding">OHE-Notebook</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">housing_num</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">housing_tr</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">sample_incomplete_rows</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">values</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">imputer</span><span class="o">.</span><span class="n">strategy</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">housing_tr</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span>
                          <span class="n">index</span><span class="o">=</span><span class="n">housing_num</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">housing_tr</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Encoder</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Feature Engineering</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Pipeline</span>
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
 
