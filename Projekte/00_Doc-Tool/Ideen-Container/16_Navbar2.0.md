'''''

{
"title": "16_Navbar2.",
"keywords": ",navBar2.0",
"categories": "",
"description": "Dieses Notebook liefert die Grunlagen für die Nav-Bar 2.0. Die Navbar 2.0 integirert die hierarchie stufen kommend von dem local Metadatainfo File ",
"level": "120",
"pageID": "07112020200718-16_NavBar2"
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
<h1>Erstellen der Nav-bar 2.0 </h1><p>Dev-ID: 16_Navbar2</p>
<h1 id="Status-der-Idee">Status der Idee<a class="anchor-link" href="#Status-der-Idee">&#182;</a></h1><ul>
<li>[x]  Die Idee exisitiert &amp; Die Ideenentwicklung wurde gestartet</li>
<li>[x]  Branch erstellt</li>
<li>[x]  Kopie von FunctionContainer in IdeenBereich</li>
<li>[ ]  implementierung der Idee</li>
<li>[ ]  Merge back to master</li>
<li>[ ]  Push Doc-Tool to remote master mit dem commit-Namen "01-DocTools-JPYNB-HTML-Converter"</li>
<li>[ ]  Lösche den lokalen Branch </li>
<li>[ ]  Ideenimplementierung abgeschlossen</li>
<li>[ ]  Kopie von FunctionContainer zurück in DocToolMaintainingScript</li>
</ul>
<h1 id="Ziel">Ziel<a class="anchor-link" href="#Ziel">&#182;</a></h1><p>Mit diesem Skript soll nun die Navbar die Informationen von dem Metadata File einlesen und verwenden.
Konkret sollen die Informationen:</p>
<ul>
<li>[ ] TabIndex,</li>
<li>[ ] ListPage</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Entwicklung">Entwicklung<a class="anchor-link" href="#Entwicklung">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">glob</span> <span class="kn">import</span> <span class="n">glob</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span> <span class="k">as</span> <span class="n">bs</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">functionContainer</span> <span class="k">as</span> <span class="nn">fc</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dir_path</span> <span class="o">=</span> <span class="s2">&quot;C:/DocTool/&quot;</span>
<span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">dir_path</span><span class="p">)</span>
<span class="n">debug</span> <span class="o">=</span> <span class="kc">True</span>

<span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
    <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Hammerfest&quot;</span><span class="p">,</span> <span class="s2">&quot;Skript startet&quot;</span><span class="p">)</span>


<span class="n">listOfDirs</span><span class="o">=</span><span class="n">glob</span><span class="p">(</span><span class="s2">&quot;./content/*/&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">listOfDirs</span><span class="p">)</span>

<span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
    <span class="n">message</span> <span class="o">=</span> <span class="s2">&quot;Zunäcsht haben wir insgesammt &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">listOfDirs</span><span class="p">))</span> <span class="o">+</span><span class="s2">&quot; BASE-DIRECTORIES welche in die ERSTE(!!!!) Ebene UNGEFILTERT(!!!) der Navbar aufgenommen werden müssen&quot;</span>
    <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Oslo&quot;</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>


<span class="c1"># Finalbaselist = Welche reiter als erste dropdowns angezeigt werden BSPW: &quot;docus&quot;, &quot;Projekte&quot; usw</span>
<span class="c1"># Konkret werden die ersten Subfolder angezeigt</span>
<span class="n">finalBaseList</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">listOfDirs</span><span class="p">),</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">&quot;</span><span class="p">,</span><span class="s2">&quot;/&quot;</span><span class="p">)</span>
    <span class="k">if</span><span class="p">(</span><span class="s2">&quot;imgs&quot;</span> <span class="ow">in</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
        <span class="k">continue</span>
    <span class="k">elif</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span> <span class="ow">in</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
        <span class="k">continue</span>
    <span class="k">elif</span><span class="p">(</span><span class="s2">&quot;images&quot;</span> <span class="ow">in</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
        <span class="k">continue</span>
    <span class="k">elif</span><span class="p">(</span><span class="s2">&quot;images&quot;</span> <span class="ow">in</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
        <span class="k">continue</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
        <span class="n">finalBaseList</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">listOfDirs</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">name</span><span class="p">])</span>

<span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
    <span class="n">message</span> <span class="o">=</span> <span class="s2">&quot;Gefiltert haben wir insgesammt haben wir &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">finalBaseList</span><span class="p">))</span> <span class="o">+</span><span class="s2">&quot; BASE-DIRECTORIES welche in die ERSTE(!!!!) Ebene der Navbar aufgenommen werden müssen&quot;</span>
    <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Stockholm&quot;</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

<span class="c1"># Einlesen des Metainfos files</span>
<span class="n">metaInfosPDDF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;C:\DocTool\DocToolMaintainingScripts\SiteMetaInfos.csv&quot;</span><span class="p">)</span>
<span class="c1">#print(metaInfos.head123)</span>
<span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
    <span class="n">message</span> <span class="o">=</span> <span class="s2">&quot;Das pandas dataframe wurde eingelesen. Das shape ist  &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">metaInfosPDDF</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
    <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Berlin&quot;</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

<span class="c1"># Start der Navigation // hier auch das Theme // hier sind in erster Linie die Index und die About Seite verlinkt</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="s1">&#39;&lt;ul class=&quot;nav nav-pills navbar navbar-inverse&quot;&gt; &lt;li role=&quot;presentation&quot; name=&quot;index&quot; tabindex=&quot;00&quot;&gt;&lt;a href=&quot;./index.html&quot;&gt;Start&lt;/a&gt;&lt;/li&gt;&lt;li role=&quot;presentation&quot; name =&quot;about&quot; tabindex=&quot;10&quot;&gt;&lt;a href=&quot;./about.html&quot;&gt;About&lt;/a&gt;&lt;/li&gt;&#39;</span>

<span class="n">tabindexFolder</span> <span class="o">=</span> <span class="mi">10</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">eachBaseMenu</span> <span class="ow">in</span> <span class="n">finalBaseList</span><span class="p">:</span>
    <span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
        <span class="n">message</span> <span class="o">=</span> <span class="s2">&quot;Folgendes Base-Menu wurde geöffnet: &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">eachBaseMenu</span><span class="p">)</span>
        <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Hamburg&quot;</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
    <span class="n">tabindexFolder</span> <span class="o">=</span> <span class="n">tabindexFolder</span> <span class="o">+</span> <span class="mi">10</span>
    <span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span> <span class="o">+</span> <span class="s1">&#39;&lt;li role=&quot;presentation&quot; class=&quot;dropdown&quot; name=&quot;&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">eachBaseMenu</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&lt;a class=&quot;dropdown-toggle&quot; data-toggle=&quot;dropdown&quot; href=&quot;LinkZurFolderIndex&quot; role=&quot;button&quot; aria-haspopup=&quot;true&quot; aria-expanded=&quot;false&quot; tabindex=&quot;&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">tabindexFolder</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">eachBaseMenu</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="s1">&#39;&lt;/a&gt;&#39;</span>
    
    <span class="n">navbar</span> <span class="o">=</span> <span class="n">fc</span><span class="o">.</span><span class="n">recursiveFolderHandling</span><span class="p">(</span><span class="n">eachBaseMenu</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">navbar</span><span class="p">,</span> <span class="n">metaInfosPDDF</span><span class="p">)</span>
    <span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span> <span class="o">+</span> <span class="s1">&#39;&lt;/li&gt;&#39;</span> 

<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">+</span><span class="s2">&quot;&lt;/ul&gt;&quot;</span>
<span class="c1"># bisher wurde alles auf der content seite gemacht. Wir wollen aber später html Dateien verlinken</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered celltag_outputPrepend">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">+</span><span class="s2">&quot;&lt;/ul&gt;&quot;</span>
<span class="c1"># bisher wurde alles auf der content seite gemacht. Wir wollen aber später html Dateien verlinken</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;.md&quot;</span><span class="p">,</span><span class="s2">&quot;.html&quot;</span><span class="p">)</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;./&quot;</span><span class="p">,</span><span class="s2">&quot;/&quot;</span><span class="p">)</span>
<span class="n">soup</span> <span class="o">=</span> <span class="n">bs</span><span class="p">(</span><span class="n">navbar</span><span class="p">)</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">prettify</span><span class="p">()</span> 
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;html&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;body123&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;/body123&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">navbar</span> <span class="o">=</span> <span class="n">navbar</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;/html&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">navbar</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">navbar</span><span class="p">))</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Speichern in Navbar, diese Datei wird dann im Layout aufgegriffen</span>
<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;navbar.html&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">navbar</span><span class="p">)</span>
<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

<span class="k">if</span><span class="p">(</span><span class="n">debug</span> <span class="o">==</span> <span class="kc">True</span><span class="p">):</span>
    <span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;hallo&quot;</span>
    <span class="n">message</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot; -Skript ist erfolgreich durchgelaufen.  Kontrolle ob im Explorer die Datei Navbar exisitiert und ob diese geöffnet werden kann, Die datei navbar kann auch im Browser geöffnet werden.&quot;</span>
    <span class="n">fc</span><span class="o">.</span><span class="n">printDebugErrorPart</span><span class="p">(</span><span class="s2">&quot;Ushuaia&quot;</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
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
 

