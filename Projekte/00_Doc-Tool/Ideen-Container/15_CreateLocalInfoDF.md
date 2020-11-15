<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39;&#39;&#39;</span>
<span class="sd">{</span>
<span class="sd">&quot;title&quot;: &quot;15_CreateLocaInfoDF&quot;,</span>
<span class="sd">&quot;keywords&quot;: &quot;15_CreateLocaInfoDF, CreateLocalInfo&quot;,</span>
<span class="sd">&quot;categories&quot;: &quot;&quot;,</span>
<span class="sd">&quot;description&quot;: &quot;Hier die Implementierungsnotizen zu der Erstellung der Info-Datei&quot;,</span>
<span class="sd">&quot;level&quot;: &quot;120&quot;,</span>
<span class="sd">&quot;pageID&quot;: &quot;07112020200718-15_CreateLocaInfoDF&quot;</span>
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
<pre>&#39;\&#39;\&#39;\n{\n&#34;title&#34;: &#34;15_CreateLocaInfoDF&#34;,\n&#34;keywords&#34;: &#34;15_CreateLocaInfoDF, CreateLocalInfo&#34;,\n&#34;categories&#34;: &#34;&#34;,\n&#34;description&#34;: &#34;Hier die Implementierungsnotizen zu der Erstellung der Info-Datei&#34;,\n&#34;level&#34;: &#34;120&#34;,\n&#34;pageID&#34;: &#34;07112020200718-15_CreateLocaInfoDF&#34;\n}\n&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1>Erstellen einer lokalen Info-Datei</h1><p>Dev-ID: 15_CreateLocaInfoDF</p>
<h1 id="Ziel">Ziel<a class="anchor-link" href="#Ziel">&#182;</a></h1><p>Mit diesem Skript soll eine lokale Info-Datei im CSV Format enstehen, welche als weiter führende Grundlage für die bessere Struktuierung meiner Website dienen soll. Konkret soll ein Pandas-DF entstehen und lokal gespeichert werden welche folgende Informationen zu jedem HTML-File enthält:</p>
<ul>
<li>[x]  pageid</li>
<li>[x]  Absoluter Pfad lokal</li>
<li>[x]  Relativer Pfad Remote</li>
<li>[x]  FielCreationDate</li>
<li>[x]  FileModifiedDate</li>
<li>[x]  FileSize</li>
<li>[x]  level für die Hierarchie</li>
<li>[x]  Keywords = Tags</li>
<li>[x]  categories=Manuell</li>
<li>[x]  description</li>
<li>[x]  categoriesList = Automatisch von Directory Struktuierung</li>
<li>[x]  section = höchste Categorie</li>
<li>[x]  sectionPathAbsolute</li>
<li>[x]  sectionPathRelative</li>
<li>[x]  Remote-Adresse = webadresse der Seite</li>
<li>[x]  Vorgelagerter Page-ID = File das im gleichen Ordner liegt aber ein kleineres Level hat</li>
<li>[x]  nachgelagerte Page-ID = File das im gleichen Ordner liegt aber ein größeres Level hat</li>
</ul>
<h1 id="Vorbedingung">Vorbedingung<a class="anchor-link" href="#Vorbedingung">&#182;</a></h1><ul>
<li>Es müssen die Content-Seiten mit einem Frame-Matter ausgestattet sein und dort müssen folgende Informationen <ul>
<li>gepflegt sein:<ul>
<li>pageID</li>
<li>level</li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 id="Anschluss">Anschluss<a class="anchor-link" href="#Anschluss">&#182;</a></h1><ul>
<li>Es müssen die Content-Seiten mit einem Frame-Matter ausgestattet sein und dort müssen folgende Informationen <ul>
<li>gepflegt sein:<ul>
<li>pageID</li>
<li>level</li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 id="Technologien">Technologien<a class="anchor-link" href="#Technologien">&#182;</a></h1><ul>
<li>Python</li>
</ul>
<h1 id="Status-der-Idee">Status der Idee<a class="anchor-link" href="#Status-der-Idee">&#182;</a></h1><ul>
<li>[x]  Die Iddee exisitiert &amp; Die Ideenentwicklung wurde gestarte</li>
<li>[x]  Implementierung und die Technologie bekannt &amp; dokumentiert</li>
<li>[x]  Git Checkout-Developmentbranch </li>
<li>[x]  Implementierung der Technologie in diesem Notebook</li>
<li>[x]  Implementierung der Technologie in den Produktivbereich = *.py Erstellt und in den Publish Prozess implementiert</li>
<li>[x]  Test Local </li>
<li>[x]  Test Remote </li>
<li>[x]  Idee abgeschlossens</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Umsetzung">Umsetzung<a class="anchor-link" href="#Umsetzung">&#182;</a></h1><p>Ich iterier hierbei durch das "content", da hierbei weniger Transfomrationen ausgeführt werden müssen und die resultierend Info dennoch gleich ist.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">glob</span> <span class="kn">import</span> <span class="n">glob</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">shutil</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">from</span> <span class="nn">markdown2</span> <span class="kn">import</span> <span class="n">markdown</span> 
<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">from</span> <span class="nn">json</span> <span class="kn">import</span> <span class="n">load</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">os.path</span>
<span class="kn">import</span> <span class="nn">time</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ErrorMessage</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
<span class="n">dir_path</span> <span class="o">=</span> <span class="s2">&quot;C:/DocTool/&quot;</span>
<span class="n">completeList</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">root</span><span class="p">,</span> <span class="n">dirs</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="n">dir_path</span><span class="o">+</span><span class="s2">&quot;content/&quot;</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
        <span class="n">currentRow</span><span class="o">=</span><span class="p">[]</span>
        <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">&quot;.md&quot;</span><span class="p">):</span>
            <span class="n">sourceAbsolute</span> <span class="o">=</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">file</span><span class="p">))</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot;/&quot;</span><span class="p">)</span>
            <span class="n">sourceRelative</span> <span class="o">=</span> <span class="n">sourceAbsolute</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;C:/DocTool/content&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
            <span class="n">fileCreationTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">ctime</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getmtime</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">))</span>
            <span class="n">fileLastModifiedTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">ctime</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getctime</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">))</span>
            <span class="n">filesize</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span>

            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">markdown_file</span><span class="p">:</span>
                    <span class="n">article</span> <span class="o">=</span> <span class="n">markdown</span><span class="p">(</span>
                        <span class="n">markdown_file</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
                    
                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
                    <span class="k">if</span><span class="p">(</span><span class="s2">&quot;&#39;&#39;&#39;&#39;&#39;&quot;</span> <span class="ow">in</span> <span class="n">article</span><span class="p">):</span>
                        <span class="n">splited</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;&#39;&#39;&#39;&#39;&#39;&quot;</span><span class="p">,</span> <span class="n">article</span><span class="p">)</span>
                        <span class="n">metadata</span> <span class="o">=</span> <span class="p">(</span><span class="n">splited</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                        <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;p&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
                        <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;&lt;/p&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
                        <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
                        <span class="n">article</span> <span class="o">=</span> <span class="n">splited</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">pageID</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;pageID&quot;</span><span class="p">]</span>
            <span class="k">except</span><span class="p">:</span>
                <span class="n">pageID</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
                <span class="n">ErrorMessage</span> <span class="o">=</span> <span class="n">ErrorMessage</span> <span class="o">+</span> <span class="s2">&quot;Die Website: </span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span><span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">hat keine Page-ID </span><span class="se">\n\n</span><span class="s2">&quot;</span>
            
            <span class="k">try</span><span class="p">:</span>
                <span class="n">keywords</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;keywords&quot;</span><span class="p">]</span>
            <span class="k">except</span><span class="p">:</span>
                <span class="n">keywords</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
                <span class="n">ErrorMessage</span> <span class="o">=</span> <span class="n">ErrorMessage</span> <span class="o">+</span> <span class="s2">&quot;Die Website: </span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span><span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">hat keine keywords </span><span class="se">\n\n</span><span class="s2">&quot;</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">categories</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;categories&quot;</span><span class="p">]</span>
            <span class="k">except</span><span class="p">:</span>
                <span class="n">categories</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
                <span class="n">ErrorMessage</span> <span class="o">=</span> <span class="n">ErrorMessage</span> <span class="o">+</span> <span class="s2">&quot;Die Website: </span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span><span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">hat keine categories </span><span class="se">\n\n</span><span class="s2">&quot;</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">level</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;level&quot;</span><span class="p">]</span>
            <span class="k">except</span><span class="p">:</span>
                <span class="n">level</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
                <span class="n">ErrorMessage</span> <span class="o">=</span> <span class="n">ErrorMessage</span> <span class="o">+</span> <span class="s2">&quot;Die Website: </span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span><span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">hat keine level </span><span class="se">\n\n</span><span class="s2">&quot;</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">description</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;description&quot;</span><span class="p">]</span>
            <span class="k">except</span><span class="p">:</span>
                <span class="n">description</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
                <span class="n">ErrorMessage</span> <span class="o">=</span> <span class="n">ErrorMessage</span> <span class="o">+</span> <span class="s2">&quot;Die Website: </span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span><span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">hat keine description </span><span class="se">\n\n</span><span class="s2">&quot;</span>


            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pageID</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sourceAbsolute</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sourceRelative</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">fileCreationTime</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">fileLastModifiedTime</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">filesize</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">level</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">keywords</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">categories</span><span class="p">)</span>
            <span class="n">currentRow</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">description</span><span class="p">)</span>
            <span class="n">completeList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentRow</span><span class="p">)</span>

            <span class="c1"># Ablegen in df</span>


<span class="n">file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;./ErrorList-CreateLocalInfoFile.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
<span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">ErrorMessage</span><span class="p">)</span>
<span class="n">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">retrungCategoriesList</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die Kategorie Informaitonen vondem pfad und gebe eine Liste zurück</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;C:/DocTool/content/&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;/&quot;</span><span class="p">,</span> <span class="n">x</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">returnWebAdresse</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die Pfade, sodass die Webadresse ableitbar ist</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;C:/DocTool/content/&quot;</span><span class="p">,</span> <span class="s2">&quot;https://jhc90.github.io/&quot;</span><span class="p">)</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;.md&quot;</span><span class="p">,</span> <span class="s2">&quot;.html&quot;</span><span class="p">)</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">retrunSection</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die Pfade, sodass die Webadresse ableitbar ist</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="k">if</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">):</span>
        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">transformCSVsToList</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die Pfade, sodass die Webadresse ableitbar ist</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">returnSectionPathAbsolute</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die absoluten Pfade für die Sections</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;/&quot;</span><span class="p">,</span> <span class="n">x</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
    <span class="n">y</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
    <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="n">y</span> <span class="o">=</span> <span class="n">y</span> <span class="o">+</span> <span class="n">element</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">y</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">returnSectionPathRelative</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extrahiere die absoluten Pfade für die Sections</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;C:/DocTool/content&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
    <span class="k">if</span><span class="p">(</span><span class="n">x</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span><span class="p">):</span>
        <span class="n">x</span> <span class="o">=</span> <span class="s2">&quot;/&quot;</span>
    <span class="k">return</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">labels</span> <span class="o">=</span><span class="p">[</span><span class="s2">&quot;pageid&quot;</span><span class="p">,</span> <span class="s2">&quot;fileNameAbsolut&quot;</span><span class="p">,</span> <span class="s2">&quot;fileNameRelative&quot;</span><span class="p">,</span> <span class="s2">&quot;fileLastModifiedTime&quot;</span><span class="p">,</span> <span class="s2">&quot;fileCreationTime&quot;</span><span class="p">,</span> <span class="s2">&quot;fileSizeInBytes&quot;</span><span class="p">,</span> <span class="s2">&quot;level&quot;</span><span class="p">,</span> <span class="s2">&quot;keywords&quot;</span><span class="p">,</span> <span class="s2">&quot;categories&quot;</span><span class="p">,</span> <span class="s2">&quot;description&quot;</span> <span class="p">]</span>

<span class="n">DF_MetaData</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">completeList</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="o">.</span><span class="n">columns</span><span class="o">=</span><span class="n">labels</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;keywords&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;keywords&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">transformCSVsToList</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">transformCSVsToList</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;categoriesList&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;fileNameAbsolut&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">retrungCategoriesList</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;section&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;categoriesList&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">retrunSection</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;sectionPathAbsoulte&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;fileNameAbsolut&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">returnSectionPathAbsolute</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;sectionPathRelative&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;sectionPathAbsoulte&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">returnSectionPathRelative</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;webadress&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;fileNameAbsolut&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">returnWebAdresse</span><span class="p">)</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;vorgelagerteSectionPage&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;nachgelagerteSectionPage&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
<span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;sectionIndex&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;https://jhc90.github.io/index.html&quot;</span>


<span class="c1"># in diesem block werden nun die Level ausgelesen und in eine Reihenfolge gebracht, sodass die Sequent der Files angepasst ist</span>
<span class="c1"># Das ist wichtig für die vor und nachgelagerten Dateien für die Sections.</span>
<span class="c1"># DF_MetaData.head123()</span>
<span class="n">uniqueSectionPathes</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="o">.</span><span class="n">sectionPathRelative</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>


<span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">uniqueSectionPathes</span><span class="p">:</span>
    <span class="n">currentDF</span>  <span class="o">=</span> <span class="n">DF_MetaData</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">DF_MetaData</span><span class="p">[</span><span class="s1">&#39;sectionPathRelative&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">element</span><span class="p">]</span>
    <span class="c1">#print(currentDF.shape) =&gt; shape 12</span>
    <span class="n">currentDFsorted</span> <span class="o">=</span> <span class="n">currentDF</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">&#39;level&#39;</span><span class="p">)</span>
    <span class="c1">#print(currentDFsorted.shape)=&gt; shape 12</span>
    
    <span class="n">currentDFsorted</span> <span class="o">=</span> <span class="n">currentDFsorted</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
    <span class="n">currentDFsorted</span><span class="p">[</span><span class="s1">&#39;level&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">currentDFsorted</span><span class="o">.</span><span class="n">index</span>
    <span class="n">currentDFsorted</span> <span class="o">=</span> <span class="n">currentDFsorted</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;index&#39;</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">currentDFsorted</span><span class="p">[</span><span class="s1">&#39;vorgelagerteSectionPage&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">currentDFsorted</span><span class="p">[</span><span class="s1">&#39;pageid&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">shift</span><span class="p">(</span><span class="n">periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">currentDFsorted</span><span class="p">[</span><span class="s1">&#39;nachgelagerteSectionPage&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">currentDFsorted</span><span class="p">[</span><span class="s1">&#39;pageid&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">shift</span><span class="p">(</span><span class="n">periods</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
   
    <span class="n">DF_MetaData</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentDFsorted</span><span class="p">)</span>
    <span class="n">DF_MetaData</span> <span class="o">=</span> <span class="n">DF_MetaData</span><span class="o">.</span><span class="n">drop_duplicates</span><span class="p">(</span><span class="n">subset</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;fileNameAbsolut&#39;</span><span class="p">],</span> <span class="n">keep</span><span class="o">=</span><span class="s1">&#39;last&#39;</span><span class="p">)</span>
    
<span class="c1">#print(DF_MetaData[[&#39;fileNameAbsolut&#39;, &#39;vorgelagerteSectionPage&#39;, &#39;nachgelagerteSectionPage&#39;]].head123(50))</span>
<span class="c1">#DF_check = DF_MetaData[[&#39;fileNameAbsolut&#39;, &#39;sectionPathAbsoulte&#39;,&#39;vorgelagerteSectionPage&#39;, &#39;nachgelagerteSectionPage&#39;]]</span>
<span class="c1">#DF_check.to_csv(&#39;./ExcelCheck.csv&#39;,index=False)</span>

<span class="c1"># Speicher DF als CV lokal</span>

<span class="n">DF_MetaData</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;C:/DocTool/DocToolMaintainingScripts/SiteMetaInfos.csv&#39;</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
 

