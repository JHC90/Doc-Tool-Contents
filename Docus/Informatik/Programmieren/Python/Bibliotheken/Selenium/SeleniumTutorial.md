<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-4">Video 4<a class="anchor-link" href="#Video-4">&#182;</a></h1><p>Interkaktion mit Elementen auf einer Seite, dazu müssen diese zunächst heruasgefiltert werden und dann genutzt werden</p>
<p>find by:</p>
<ul>
<li>by_name</li>
<li>by_id // Das wäre das beste</li>
<li>by_class_name</li>
<li>by tag_name // wenn mögich das nicht nehmen</li>
</ul>
<p>Auf anderen Seite ist es Vergleichbar wie ein Reverse Engineering Projekt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">import</span> <span class="nn">time</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># erstellt ein Browser in Viruteller Einheit</span>
<span class="n">driverexample</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span>
<span class="c1"># URL-Call in dem oberen Driver</span>
<span class="n">driverexample</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.tz.de&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># erstellt ein Browser in Viruteller Einheit</span>
<span class="n">driverexample</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span>
<span class="c1"># Automatisch googlen</span>
<span class="n">driverexample</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
<span class="c1"># Suche Element via NAme</span>
<span class="n">search_field</span> <span class="o">=</span> <span class="n">driverexample</span><span class="o">.</span><span class="n">find_element_by_name</span><span class="p">(</span><span class="s1">&#39;q&#39;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;google&#39;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">submit</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div># Suche Element via ID
search_field = driver.find_element_by_id('lst-ib')
search_field.send_keys('google')
search_field.submit()
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Suche Element via classname # =&gt; nicht eindeutig</span>
<span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
<span class="n">search_field</span> <span class="o">=</span> <span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_class</span><span class="p">(</span><span class="s1">&#39;gLFyf gsfi&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">search_field</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">i</span><span class="o">.</span><span class="n">tag_name</span> <span class="o">==</span> <span class="s1">&#39;input&#39;</span><span class="p">:</span>
        <span class="n">i</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;google&#39;</span><span class="p">)</span>
        <span class="n">i</span><span class="o">.</span><span class="n">submit</span><span class="p">()</span>
        <span class="k">break</span>
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
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-9-9ec7feed4d21&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      4</span> driver <span class="ansi-yellow-intense-fg ansi-bold">=</span> webdriver<span class="ansi-yellow-intense-fg ansi-bold">.</span>Chrome<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      5</span> driver<span class="ansi-yellow-intense-fg ansi-bold">.</span>get<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;https://www.google.de/xhtml&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 6</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>search_field <span class="ansi-yellow-intense-fg ansi-bold">=</span> driver<span class="ansi-yellow-intense-fg ansi-bold">.</span>find_element_by_class<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;gLFyf gsfi&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      7</span> <span class="ansi-green-intense-fg ansi-bold">for</span> i <span class="ansi-green-intense-fg ansi-bold">in</span> search_field<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">      8</span>     <span class="ansi-green-intense-fg ansi-bold">if</span> i<span class="ansi-yellow-intense-fg ansi-bold">.</span>tag_name <span class="ansi-yellow-intense-fg ansi-bold">==</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;input&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-red-intense-fg ansi-bold">AttributeError</span>: &#39;WebDriver&#39; object has no attribute &#39;find_element_by_class&#39;</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-5">Video 5<a class="anchor-link" href="#Video-5">&#182;</a></h1><p>Hier geht es um das senden von Key</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>
<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;2iX3fQiqUdA&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver.common.keys</span> <span class="kn">import</span> <span class="n">Keys</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># erstellt ein Browser in Viruteller Einheit</span>
<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
<span class="c1"># URL-Call in dem oberen Driver</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">search_field</span> <span class="o">=</span> <span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_name</span><span class="p">(</span><span class="s1">&#39;q&#39;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;Silvia Ruidisch&#39;</span><span class="p">,</span> <span class="n">Keys</span><span class="o">.</span><span class="n">BACKSPACE</span><span class="p">,</span> <span class="n">Keys</span><span class="o">.</span><span class="n">ARROW_LEFT</span><span class="p">,</span>  <span class="n">Keys</span><span class="o">.</span><span class="n">BACKSPACE</span><span class="p">,</span>  <span class="n">Keys</span><span class="o">.</span><span class="n">ENTER</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-6">Video 6<a class="anchor-link" href="#Video-6">&#182;</a></h1><p>Hier geht es um die browser history, sprich vorwärts und Rückwärs schalten.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;wJsUvQAjUFs&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.tz.de&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.sueddeutsche.de&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.aldi.de&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<span class="n">driver</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<span class="n">driver</span><span class="o">.</span><span class="n">forward</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-7">Video 7<a class="anchor-link" href="#Video-7">&#182;</a></h1><p>Hier geht es um die browser Cookies. Vorallem bei Login-Sessions wichtig.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;nK6CMrNTWqY&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.tz.de&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cookie</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;name&#39;</span><span class="p">:</span><span class="s1">&#39;token&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">:</span><span class="s1">&#39;456123&#39;</span><span class="p">}</span>
<span class="n">driver</span><span class="o">.</span><span class="n">add_cookie</span><span class="p">(</span><span class="n">cookie</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.tz.de&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Auslesen derCookies</span>
<span class="nb">print</span><span class="p">(</span><span class="n">driver</span><span class="o">.</span><span class="n">get_cookie</span><span class="p">(</span><span class="s1">&#39;token&#39;</span><span class="p">))</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">driver</span><span class="o">.</span><span class="n">get_cookies</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-8">Video 8<a class="anchor-link" href="#Video-8">&#182;</a></h1><p>XPath, teil von XML. MIT XPATH kann man einzelne Elemente auslesen. Dazu hat man merer optionen</p>
<ol>
<li>Absoluter Pfad</li>
<li>//</li>
<li>// Feld mit ID</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;ScByEODsLiw&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Option2</span>
<span class="n">search_field</span> <span class="o">=</span> <span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_xpath</span><span class="p">(</span><span class="s2">&quot;//input[2]&quot;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Option3</span>
<span class="n">search_field</span> <span class="o">=</span> <span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_xpath</span><span class="p">(</span><span class="s2">&quot;//input[@name=&#39;q&#39;]&quot;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;Silvia Ruidisch&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-9">Video 9<a class="anchor-link" href="#Video-9">&#182;</a></h1><p>Wie lange braucht ein Element bis es geladen ist.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;A1XWkGMeso4&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver.support.ui</span> <span class="kn">import</span> <span class="n">WebDriverWait</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver.support</span> <span class="kn">import</span> <span class="n">expected_conditions</span> <span class="k">as</span> <span class="n">ExpectedCondtion</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver.common.by</span> <span class="kn">import</span> <span class="n">By</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="n">element</span> <span class="o">=</span> <span class="n">WebDriverWait</span><span class="p">(</span><span class="n">driver</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span><span class="o">.</span><span class="n">until</span><span class="p">(</span>
    <span class="n">ExpectedCondtion</span><span class="o">.</span><span class="n">presence_of_all_elements_located</span><span class="p">((</span><span class="n">By</span><span class="o">.</span><span class="n">NAME</span><span class="p">,</span> <span class="s1">&#39;q&#39;</span><span class="p">))</span>
        
    <span class="p">)</span> <span class="c1"># Prüfung ob das Element da ist, wartet solange bis das Element da ist</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;yes, element wurde gefunden&quot;</span><span class="p">)</span>
<span class="k">except</span><span class="p">:</span>
    <span class="k">pass</span>
<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video11">Video11<a class="anchor-link" href="#Video11">&#182;</a></h1><p>ActionChains, können nur auf einer seite ausgeführt werden und nicht auf folge-Seiten. Mit ActionChains können aber mehrere Aktionen auf einer Seite durchgeführt werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;BsWrl_AT_jQ&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver</span> <span class="kn">import</span> <span class="n">ActionChains</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="s1">&#39;C:/Webdriver/chromedriver.exe&#39;</span><span class="p">)</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de/xhtml&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video12">Video12<a class="anchor-link" href="#Video12">&#182;</a></h1><p>ActionChains, können nur auf einer seite ausgeführt werden und nicht auf folge-Seiten. Mit ActionChains können aber mehrere Aktionen auf einer Seite durchgeführt werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Neue-Quelle">Neue Quelle<a class="anchor-link" href="#Neue-Quelle">&#182;</a></h1><p>Hier geht es darum nicht den lokalen Webbrwoser zu nutzen sondern mit einem Selenium Hub unterschiedliche Webbrowser zu nutzen. Für das erstellen eines Selnium hubs im Kontext einer Dockerized Environment folge diesem Tutorial</p>
<p>DOCKER-Selenium
pip install selenium</p>
<p>Tut1
<a href="https://robotninja.com/blog/introduction-using-selenium-docker-containers-end-end-testing/">https://robotninja.com/blog/introduction-using-selenium-docker-containers-end-end-testing/</a></p>
<p>TUT2</p>
<p><a href="https://www.softwaretestinghelp.com/docker-selenium-tutorial/">https://www.softwaretestinghelp.com/docker-selenium-tutorial/</a>
docker pull selenium/hub
docker pull selenium/node-firefox
docker pull selenium/node-firefox-debug
docker pull selenium/node-chrome
docker pull selenium/node-chrome-debug</p>
<p>docker run -d -p 4444:4444 –-name selenium-hub selenium/hub
docker run -d -–link -P selenium-hub:hub --name node-chrome selenium/node-chrome</p>
<p>docker run -d -P --link selenium-hub:hub --name node-chrome-debug selenium/node-chrome-debug
docker rm -f node-chrome-debug</p>
<p>docker run -d –-link selenium-hub:hub --name node-firefox selenium/node-firefox
docker run -d -P –-link selenium-hub:hub --name node-firefox-debug selenium/node-firefox-debug</p>
<p><a href="http://127.0.0.1:4444/grid/console">http://127.0.0.1:4444/grid/console</a></p>
<p>mit vnc via IP + port(kommt aus docker ps -a)</p>
<p><strong>VerifiedDockerized Firefox öffnen mit gui</strong></p>
<blockquote><p>docker run -d --name=firefox -p 5800:5800 -v C:\Docker:/config:rw -e DISPLAY=192.168.178.36:0.0 --security-opt seccomp=C:\Users\1810837475\Downloads\seccomp.json --shm-size 2g jlesage/firefox</p>
</blockquote>
<p>mit XLAUNCH</p>
<p>docker container rm -f firefox</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install selenium</span>
<span class="kn">import</span> <span class="nn">selenium</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">from</span> <span class="nn">selenium.webdriver.common.desired_capabilities</span> <span class="kn">import</span> <span class="n">DesiredCapabilities</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Remote</span><span class="p">(</span>
   <span class="n">command_executor</span><span class="o">=</span><span class="s1">&#39;http://127.0.0.1:4444/wd/hub&#39;</span><span class="p">,</span>
   <span class="n">desired_capabilities</span><span class="o">=</span><span class="n">DesiredCapabilities</span><span class="o">.</span><span class="n">CHROME</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#desired_capabilities=DesiredCapabilities.CHROME)</span>
<span class="c1">#desired_capabilities=DesiredCapabilities.FIREFOX)</span>
<span class="c1"># Opera nein</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;http://www.google.de&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;http://www.whatsapp.de&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;https://www.netflix.com/de/&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
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
 

