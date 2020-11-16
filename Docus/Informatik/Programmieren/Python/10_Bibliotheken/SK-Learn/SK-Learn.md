<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="SK-Learn">SK-Learn<a class="anchor-link" href="#SK-Learn">&#182;</a></h1><p>Bekannte Bibliothek für DS-Projekte in Python. Hiermit lassen sich Bereiche des</p>
<ul>
<li>Data-Preprocessings</li>
<li>Modellierung</li>
</ul>
<p>durchführen.</p>
<p>SKlearnt strebt danach den gleichen Aufbau der unterschiedlichen Algorithmen mitzugeben =&gt; ausgehend von einem Estimator(den wir die Namenszuweisung "model" geben) gilt folgendes:</p>
<ul>
<li>model.fit() #=&gt; algorithmus wird auf Trainingsdaten gefittet</li>
<li>bei SL = model.fit(X,y)</li>
<li>bei USL = model.fit(X)</li>
</ul>
<p><strong>Nur Supervised</strong></p>
<ul>
<li>model.predict(X-Neu)</li>
<li>model.score(X-Neu) # =&gt; grad bei Klassifizierung</li>
</ul>
<p><strong>Nur Un-Supervised</strong></p>

<pre><code>* model.predict() # =&gt; Cluster
* model.transform() # =&gt; Ausgehend von unsupervised Model neue Daten als Grundlage
* model.fit:predict() # =&gt; bei manchen Estimatoren =&gt; Ziel effizienter ANppasunng und Transformation mit selben Input</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Installation">Installation<a class="anchor-link" href="#Installation">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install sklearn</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="BSP-Verwendung-Konzeptionell">BSP-Verwendung-Konzeptionell<a class="anchor-link" href="#BSP-Verwendung-Konzeptionell">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="./imgs/sklearn1.png" alt="image.png">
<img src="./imgs/sklearn2.png" alt="image.png">
<img src="./imgs/sklearn3.png" alt="image.png"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Vorgehen">Vorgehen<a class="anchor-link" href="#Vorgehen">&#182;</a></h1><ol>
<li>Beschaffen der Daten</li>
<li>Aufbereiten der Daten</li>
<li>Modelieren
hier wird in der Grundlage keine tatsächliche Implementierung geliefert =&gt; daher habe ich hier lediglich die Slides Eingefügt.
Der Teil ist easy sobal die Daten in einem Shape sind, der "i.O." ist. In diesem Teil muss man eben ein Verständniss des Algorithmus im Allgemeinen haben, besonders wenn es darum geht einen Algorithmus "performant" zu implementieren. (Bspw was kann parallel // muss sequentiell laufen).</li>
</ol>
<p>Konkret geht es hier um die implementierung je nach Anwendungsfall(Regression/ Klassifikation/)</p>
<ol>
<li>Predicten</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Trainieren-auf-Trainingsdaten">Trainieren auf Trainingsdaten<a class="anchor-link" href="#Trainieren-auf-Trainingsdaten">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Hilfestellung-bei-der-Algorithmusauswahl-im-SK-Learn-Kosmos">Hilfestellung bei der Algorithmusauswahl im SK-Learn Kosmos<a class="anchor-link" href="#Hilfestellung-bei-der-Algorithmusauswahl-im-SK-Learn-Kosmos">&#182;</a></h1><p><a href="https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html">Link</a>
<img src="https://scikit-learn.org/stable/_static/ml_map.png" alt="SK-CheatSheet"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Konkrete-Implementierungs-Templates">Konkrete Implementierungs-Templates<a class="anchor-link" href="#Konkrete-Implementierungs-Templates">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Weiteres-Bsp">Weiteres Bsp<a class="anchor-link" href="#Weiteres-Bsp">&#182;</a></h2><p>für die weitere Erklärung SK-Learn arbeite ich mit einer "Clean" Version vom California-Housing. Dieses Daten kommen in diesem konkreten Fall aus dem Udemy Kurs von Rene Brunner (Deep-Learning).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">dfCal</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./data/cal_housing_clean.csv&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">dfCal</span><span class="o">.</span><span class="n">columns</span> <span class="c1"># y = medianHouseValue || X = alles ohne y</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;housingMedianAge&#39;, &#39;totalRooms&#39;, &#39;totalBedrooms&#39;, &#39;population&#39;,
       &#39;households&#39;, &#39;medianIncome&#39;, &#39;medianHouseValue&#39;],
      dtype=&#39;object&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Train-/-Testsplit">Train / Testsplit<a class="anchor-link" href="#Train-/-Testsplit">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>

<span class="c1"># Best-Practice in horizontaler &amp; VertikalerSpaltung: </span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">dfCal</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;medianHouseValue&#39;</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> 
                                                    <span class="n">dfCal</span><span class="p">[</span><span class="s1">&#39;medianHouseValue&#39;</span><span class="p">],</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.30</span><span class="p">,</span> 
                                                    <span class="n">random_state</span><span class="o">=</span><span class="mi">101</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Side-Info</strong><br>
hier eine  etwas unelegantere Versionen den Train &amp; Test-Split hinzubiegen. Das ist jedoch der Standard in vielen Tutorials bzw Vo-Einheiten</p>

</div>
</div>
</div># Schritt 1 // hier wähle wir nur die Feature aus die von Bedeutung sind => vertikaler cut
# Das ist lediglich ein Biespiel, für die Auswahl ist das Pandas Packet hilfreich
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

# Schritt 2 // hier werden die Daten horizontal = Zeilenweise in train und testdaten aufgeteilt
# Das ist lediglich ein Biespiel, für die Auswahl ist das Pandas Packet hilfreich

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4) # Ohne Random => reproducibility nicht gewährleistetn
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Skalieren">Skalieren<a class="anchor-link" href="#Skalieren">&#182;</a></h2>
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
<h3 id="Min-Max-Scaler">Min-Max-Scaler<a class="anchor-link" href="#Min-Max-Scaler">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Extended">Extended<a class="anchor-link" href="#Extended">&#182;</a></h4><p>um das Vorgehen zu verstehen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Kopie für die Extended Version</span>
<span class="n">xtrainC</span> <span class="o">=</span> <span class="n">X_train</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="c1">#print(type(xtrainC))</span>
<span class="c1">#print(len(xtrainC))</span>
<span class="c1">#print(xtrainC.head123())</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">MinMaxScaler</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">MinMaxScaler</span><span class="p">()</span> <span class="c1"># Robust / standard</span>
<span class="n">scaler</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">xtrainC</span><span class="p">)</span>
<span class="c1"># print(scaler) # =&gt; Objekt</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MinMaxScaler(copy=True, feature_range=(0, 1))
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Transform</span>
<span class="n">xtrainC</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">xtrainC</span><span class="p">),</span><span class="n">columns</span> <span class="o">=</span> <span class="n">xtrainC</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="n">xtrainC</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">xtrainC</span><span class="o">.</span><span class="n">head123</span><span class="p">()</span> <span class="c1"># =&gt; Transfomriertes DF, alles im Featrue-Range 0- 1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>



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
      <th>housingMedianAge</th>
      <th>totalRooms</th>
      <th>totalBedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>medianIncome</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>6761</th>
      <td>0.352941</td>
      <td>0.069688</td>
      <td>0.117163</td>
      <td>0.048769</td>
      <td>0.115442</td>
      <td>0.142508</td>
    </tr>
    <tr>
      <th>3010</th>
      <td>0.607843</td>
      <td>0.011242</td>
      <td>0.015673</td>
      <td>0.008367</td>
      <td>0.014142</td>
      <td>0.045027</td>
    </tr>
    <tr>
      <th>7812</th>
      <td>0.666667</td>
      <td>0.025230</td>
      <td>0.031347</td>
      <td>0.020971</td>
      <td>0.030258</td>
      <td>0.212866</td>
    </tr>
    <tr>
      <th>8480</th>
      <td>0.666667</td>
      <td>0.032530</td>
      <td>0.033830</td>
      <td>0.024752</td>
      <td>0.030094</td>
      <td>0.298651</td>
    </tr>
    <tr>
      <th>1051</th>
      <td>0.294118</td>
      <td>0.031919</td>
      <td>0.035692</td>
      <td>0.019466</td>
      <td>0.034863</td>
      <td>0.272631</td>
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
<h4 id="Compact">Compact<a class="anchor-link" href="#Compact">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">MinMaxScaler</span>
<span class="n">scaler</span> <span class="o">=</span> <span class="n">MinMaxScaler</span><span class="p">()</span>
<span class="n">scaler</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_train</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">),</span><span class="n">columns</span> <span class="o">=</span> <span class="n">X_train</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="n">X_train</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">X_test</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">),</span><span class="n">columns</span> <span class="o">=</span> <span class="n">X_test</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="n">X_test</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Normalisieren">Normalisieren<a class="anchor-link" href="#Normalisieren">&#182;</a></h3>
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
<h2 id="One-Hot-Encoding">One Hot Encoding<a class="anchor-link" href="#One-Hot-Encoding">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Labelencoder">Labelencoder<a class="anchor-link" href="#Labelencoder">&#182;</a></h2><p><strong>BSP1</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">preprocessing</span>
<span class="n">le</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">LabelEncoder</span><span class="p">()</span>
<span class="n">le</span><span class="o">.</span><span class="n">fit</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LabelEncoder()</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">classes_</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([1, 2, 6])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">transform</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([0, 0, 1, 2], dtype=int64)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[8]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([1, 1, 2, 6])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>BSP2</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span> <span class="o">=</span> <span class="n">preprocessing</span><span class="o">.</span><span class="n">LabelEncoder</span><span class="p">()</span>
<span class="n">le</span><span class="o">.</span><span class="n">fit</span><span class="p">([</span><span class="s1">&#39;fb&#39;</span><span class="p">,</span> <span class="s1">&#39;fb&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[9]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LabelEncoder()</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">classes_</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;SZ&#39;, &#39;fb&#39;, &#39;wa&#39;], dtype=&#39;&lt;U2&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">transform</span><span class="p">([</span><span class="s1">&#39;fb&#39;</span><span class="p">,</span> <span class="s1">&#39;fb&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;wa&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">,</span><span class="s1">&#39;SZ&#39;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([1, 1, 2, 2, 2, 2, 0, 0, 0, 0], dtype=int64)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">le</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;fb&#39;, &#39;fb&#39;, &#39;wa&#39;, &#39;wa&#39;, &#39;wa&#39;, &#39;wa&#39;, &#39;SZ&#39;, &#39;SZ&#39;, &#39;SZ&#39;, &#39;SZ&#39;],
      dtype=&#39;&lt;U2&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Imputation">Imputation<a class="anchor-link" href="#Imputation">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Synthtthische-Datens&#228;tze-erzeugen">Synthtthische Datens&#228;tze erzeugen<a class="anchor-link" href="#Synthtthische-Datens&#228;tze-erzeugen">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Unsupervised-Learning">Unsupervised Learning<a class="anchor-link" href="#Unsupervised-Learning">&#182;</a></h2><h3 id="Clustering">Clustering<a class="anchor-link" href="#Clustering">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">sklearn.datasets</span> <span class="kn">import</span> <span class="n">make_blobs</span>
<span class="n">X</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">make_blobs</span><span class="p">(</span><span class="n">n_samples</span> <span class="o">=</span> <span class="mi">200</span><span class="p">,</span> <span class="n">centers</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">cluster_std</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span> <span class="n">random_state</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">X</span><span class="p">[:,</span> <span class="mi">0</span><span class="p">],</span> <span class="n">X</span><span class="p">[:,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">s</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.collections.PathCollection at 0x2a4d8bab9c8&gt;</pre>
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
 

