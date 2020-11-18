<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>source: <a href="https://jorisvandenbossche.github.io/blog/2018/05/28/scikit-learn-columntransformer/">https://jorisvandenbossche.github.io/blog/2018/05/28/scikit-learn-columntransformer/</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">titanic</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/master/notebooks/datasets/titanic3.csv&quot;</span><span class="p">)</span>
<span class="c1"># there is still a small problem with using the OneHotEncoder and missing values,</span>
<span class="c1"># so for now I am going to assume there are no missing values by dropping them</span>
<span class="n">titanic2</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">subset</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;pclass&#39;</span><span class="p">,</span> <span class="s1">&#39;sex&#39;</span><span class="p">,</span> <span class="s1">&#39;age&#39;</span><span class="p">,</span> <span class="s1">&#39;sibsp&#39;</span><span class="p">,</span> <span class="s1">&#39;parch&#39;</span><span class="p">,</span> <span class="s1">&#39;fare&#39;</span><span class="p">,</span> <span class="s1">&#39;embarked&#39;</span><span class="p">])</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">target</span> <span class="o">=</span> <span class="n">titanic2</span><span class="o">.</span><span class="n">survived</span><span class="o">.</span><span class="n">values</span>
<span class="n">features</span> <span class="o">=</span> <span class="n">titanic2</span><span class="p">[[</span><span class="s1">&#39;pclass&#39;</span><span class="p">,</span> <span class="s1">&#39;sex&#39;</span><span class="p">,</span> <span class="s1">&#39;age&#39;</span><span class="p">,</span> <span class="s1">&#39;fare&#39;</span><span class="p">,</span> <span class="s1">&#39;embarked&#39;</span><span class="p">]]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">features</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
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
Int64Index: 1043 entries, 0 to 1308
Data columns (total 5 columns):
pclass      1043 non-null int64
sex         1043 non-null object
age         1043 non-null float64
fare        1043 non-null float64
embarked    1043 non-null object
dtypes: float64(2), int64(1), object(2)
memory usage: 48.9+ KB
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span><span class="p">,</span> <span class="n">OneHotEncoder</span>
<span class="kn">from</span> <span class="nn">sklearn.compose</span> <span class="kn">import</span> <span class="n">ColumnTransformer</span><span class="p">,</span> <span class="n">make_column_transformer</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">preprocess</span> <span class="o">=</span> <span class="n">make_column_transformer</span><span class="p">(</span>
    <span class="p">([</span><span class="s1">&#39;age&#39;</span><span class="p">,</span> <span class="s1">&#39;fare&#39;</span><span class="p">],</span> <span class="n">StandardScaler</span><span class="p">()),</span>
    <span class="p">([</span><span class="s1">&#39;pclass&#39;</span><span class="p">,</span> <span class="s1">&#39;sex&#39;</span><span class="p">,</span> <span class="s1">&#39;embarked&#39;</span><span class="p">],</span> <span class="n">OneHotEncoder</span><span class="p">())</span>
<span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">preprocess</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">features</span><span class="p">)</span>
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
<span class="ansi-red-intense-fg ansi-bold">TypeError</span>                                 Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-10-eaef8b606cd9&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>preprocess<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit_transform<span class="ansi-yellow-intense-fg ansi-bold">(</span>features<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\compose\_column_transformer.py</span> in <span class="ansi-cyan-fg">fit_transform</span><span class="ansi-blue-intense-fg ansi-bold">(self, X, y)</span>
<span class="ansi-green-fg">    512</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_feature_names_in <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">None</span>
<span class="ansi-green-fg">    513</span>         X <span class="ansi-yellow-intense-fg ansi-bold">=</span> _check_X<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 514</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_transformers<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    515</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_column_callables<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    516</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_remainder<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\compose\_column_transformer.py</span> in <span class="ansi-cyan-fg">_validate_transformers</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    285</span>                                 <span class="ansi-blue-intense-fg ansi-bold">&#34;transform, or can be &#39;drop&#39; or &#39;passthrough&#39; &#34;</span>
<span class="ansi-green-fg">    286</span>                                 <span class="ansi-blue-intense-fg ansi-bold">&#34;specifiers. &#39;%s&#39; (type %s) doesn&#39;t.&#34;</span> <span class="ansi-yellow-intense-fg ansi-bold">%</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 287</span><span class="ansi-yellow-intense-fg ansi-bold">                                 (t, type(t)))
</span><span class="ansi-green-fg">    288</span> 
<span class="ansi-green-fg">    289</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> _validate_column_callables<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> X<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-red-intense-fg ansi-bold">TypeError</span>: All estimators should implement fit and transform, or can be &#39;drop&#39; or &#39;passthrough&#39; specifiers. &#39;[&#39;age&#39;, &#39;fare&#39;]&#39; (type &lt;class &#39;list&#39;&gt;) doesn&#39;t.</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="2nd-Example">2nd Example<a class="anchor-link" href="#2nd-Example">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="kn">import</span> <span class="n">make_pipeline</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">target</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">survived</span><span class="o">.</span><span class="n">values</span>
<span class="n">features</span> <span class="o">=</span> <span class="n">titanic</span><span class="p">[[</span><span class="s1">&#39;pclass&#39;</span><span class="p">,</span> <span class="s1">&#39;sex&#39;</span><span class="p">,</span> <span class="s1">&#39;age&#39;</span><span class="p">,</span> <span class="s1">&#39;fare&#39;</span><span class="p">,</span> <span class="s1">&#39;embarked&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="c1"># I still fill the missing values for the embarked column, because we cannot (yet) easily handle categorical missing values</span>
<span class="n">features</span><span class="p">[</span><span class="s1">&#39;embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">features</span><span class="p">[</span><span class="s1">&#39;embarked&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">index</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">features</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">numerical_features</span> <span class="o">=</span> <span class="n">features</span><span class="o">.</span><span class="n">dtypes</span> <span class="o">==</span> <span class="s1">&#39;float&#39;</span>
<span class="n">categorical_features</span> <span class="o">=</span> <span class="o">~</span><span class="n">numerical_features</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">preprocess</span> <span class="o">=</span> <span class="n">make_column_transformer</span><span class="p">(</span>
    <span class="p">(</span><span class="n">numerical_features</span><span class="p">,</span> <span class="n">make_pipeline</span><span class="p">(</span><span class="n">SimpleImputer</span><span class="p">(),</span> <span class="n">StandardScaler</span><span class="p">())),</span>
    <span class="p">(</span><span class="n">categorical_features</span><span class="p">,</span> <span class="n">OneHotEncoder</span><span class="p">()))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">model</span> <span class="o">=</span> <span class="n">make_pipeline</span><span class="p">(</span>
    <span class="n">preprocess</span><span class="p">,</span>
    <span class="n">LogisticRegression</span><span class="p">())</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;logistic regression score: </span><span class="si">%f</span><span class="s2">&quot;</span> <span class="o">%</span> <span class="n">model</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test</span><span class="p">,</span> <span class="n">y_test</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\1810837475\.conda\envs\Kompensationsarbeit\lib\site-packages\pandas\core\ops\__init__.py:1115: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
  result = method(y)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-18-08d3a7470a71&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>model<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit<span class="ansi-yellow-intense-fg ansi-bold">(</span>X_train<span class="ansi-yellow-intense-fg ansi-bold">,</span> y_train<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      2</span> print<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;logistic regression score: %f&#34;</span> <span class="ansi-yellow-intense-fg ansi-bold">%</span> model<span class="ansi-yellow-intense-fg ansi-bold">.</span>score<span class="ansi-yellow-intense-fg ansi-bold">(</span>X_test<span class="ansi-yellow-intense-fg ansi-bold">,</span> y_test<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\pipeline.py</span> in <span class="ansi-cyan-fg">fit</span><span class="ansi-blue-intense-fg ansi-bold">(self, X, y, **fit_params)</span>
<span class="ansi-green-fg">    346</span>             This estimator
<span class="ansi-green-fg">    347</span>         &#34;&#34;&#34;
<span class="ansi-green-intense-fg ansi-bold">--&gt; 348</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>Xt<span class="ansi-yellow-intense-fg ansi-bold">,</span> fit_params <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_fit<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>fit_params<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    349</span>         with _print_elapsed_time(&#39;Pipeline&#39;,
<span class="ansi-green-fg">    350</span>                                  self._log_message(len(self.steps) - 1)):

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\pipeline.py</span> in <span class="ansi-cyan-fg">_fit</span><span class="ansi-blue-intense-fg ansi-bold">(self, X, y, **fit_params)</span>
<span class="ansi-green-fg">    311</span>                 message_clsname<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-blue-intense-fg ansi-bold">&#39;Pipeline&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">    312</span>                 message<span class="ansi-yellow-intense-fg ansi-bold">=</span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_log_message<span class="ansi-yellow-intense-fg ansi-bold">(</span>step_idx<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 313</span><span class="ansi-yellow-intense-fg ansi-bold">                 **fit_params_steps[name])
</span><span class="ansi-green-fg">    314</span>             <span class="ansi-red-intense-fg ansi-bold"># Replace the transformer of the step with the fitted</span>
<span class="ansi-green-fg">    315</span>             <span class="ansi-red-intense-fg ansi-bold"># transformer. This is necessary when loading the transformer</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\joblib\memory.py</span> in <span class="ansi-cyan-fg">__call__</span><span class="ansi-blue-intense-fg ansi-bold">(self, *args, **kwargs)</span>
<span class="ansi-green-fg">    353</span> 
<span class="ansi-green-fg">    354</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> __call__<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 355</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>func<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    356</span> 
<span class="ansi-green-fg">    357</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> call_and_shelve<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\pipeline.py</span> in <span class="ansi-cyan-fg">_fit_transform_one</span><span class="ansi-blue-intense-fg ansi-bold">(transformer, X, y, weight, message_clsname, message, **fit_params)</span>
<span class="ansi-green-fg">    724</span>     <span class="ansi-green-intense-fg ansi-bold">with</span> _print_elapsed_time<span class="ansi-yellow-intense-fg ansi-bold">(</span>message_clsname<span class="ansi-yellow-intense-fg ansi-bold">,</span> message<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    725</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> hasattr<span class="ansi-yellow-intense-fg ansi-bold">(</span>transformer<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;fit_transform&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 726</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>res <span class="ansi-yellow-intense-fg ansi-bold">=</span> transformer<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit_transform<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>fit_params<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    727</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    728</span>             res <span class="ansi-yellow-intense-fg ansi-bold">=</span> transformer<span class="ansi-yellow-intense-fg ansi-bold">.</span>fit<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">,</span> y<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>fit_params<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">.</span>transform<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\compose\_column_transformer.py</span> in <span class="ansi-cyan-fg">fit_transform</span><span class="ansi-blue-intense-fg ansi-bold">(self, X, y)</span>
<span class="ansi-green-fg">    512</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_feature_names_in <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-green-intense-fg ansi-bold">None</span>
<span class="ansi-green-fg">    513</span>         X <span class="ansi-yellow-intense-fg ansi-bold">=</span> _check_X<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 514</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_transformers<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    515</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_column_callables<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    516</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_validate_remainder<span class="ansi-yellow-intense-fg ansi-bold">(</span>X<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\sklearn\compose\_column_transformer.py</span> in <span class="ansi-cyan-fg">_validate_transformers</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    278</span>         <span class="ansi-red-intense-fg ansi-bold"># validate estimators</span>
<span class="ansi-green-fg">    279</span>         <span class="ansi-green-intense-fg ansi-bold">for</span> t <span class="ansi-green-intense-fg ansi-bold">in</span> transformers<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 280</span><span class="ansi-yellow-intense-fg ansi-bold">             </span><span class="ansi-green-intense-fg ansi-bold">if</span> t <span class="ansi-green-intense-fg ansi-bold">in</span> <span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;drop&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;passthrough&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    281</span>                 <span class="ansi-green-intense-fg ansi-bold">continue</span>
<span class="ansi-green-fg">    282</span>             if (not (hasattr(t, &#34;fit&#34;) or hasattr(t, &#34;fit_transform&#34;)) or not

<span class="ansi-green-intense-fg ansi-bold">~\.conda\envs\Kompensationsarbeit\lib\site-packages\pandas\core\generic.py</span> in <span class="ansi-cyan-fg">__nonzero__</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">   1553</span>             <span class="ansi-blue-intense-fg ansi-bold">&#34;The truth value of a {0} is ambiguous. &#34;</span>
<span class="ansi-green-fg">   1554</span>             &#34;Use a.empty, a.bool(), a.item(), a.any() or a.all().&#34;.format(
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1555</span><span class="ansi-yellow-intense-fg ansi-bold">                 </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>__class__<span class="ansi-yellow-intense-fg ansi-bold">.</span>__name__
<span class="ansi-green-fg">   1556</span>             )
<span class="ansi-green-fg">   1557</span>         )

<span class="ansi-red-intense-fg ansi-bold">ValueError</span>: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().</pre>
</div>
</div>

</div>
</div>

</div>
 

