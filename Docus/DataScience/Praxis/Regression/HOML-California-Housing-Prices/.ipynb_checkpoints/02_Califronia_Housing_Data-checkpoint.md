'''''

{
"title": "California-Housing-Notebook-Data",
"keywords": "Regression, Big-Picture, ",
"categories": "",
"description": "Hier geht es um die individuelle Abarbeitung der Checkliste Data im Kontext der California-Housing Problematik",
"level": "20",
"pageID": "14112020-10-California-Housing-Data"
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
<center><h1>California Housing <br> Data-Checkliste</h1></center><p><img src="imgs/2020-11-14-21-31-19.png" alt=""></p>
<p>In diesem Notebook wird die <a href="15112020-DataChecklist">Data-Checkliste</a> im Kontext des California-Housing Problem abgeabreitet.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<ol>
<li><a href="07112020200718-ListNeededData">Auflistung der benötigten Daten</a></li>
<li><a href="07112020200718-ListNeededData">Dokumentiere DatenQuellen</a></li>
<li><a href="07112020200718-CheckDataSpace">Prüfe Speicherbedarf</a></li>
<li><a href="07112020200718-LegalObligations">Prüfe Legal Obligations</a></li>
<li><a href="07112020200718-GetAccess">Erhalte Zugriff</a></li>
<li><a href="07112020200718-CreateWorkspace">Erstelle Workspace</a></li>
<li><a href="07112020200718-GetDownloadData">Tatsächliche Datenbeschaffung</a></li>
<li><a href="07112020200718-ConvertData">Convert Data</a></li>
<li><a href="07112020200718-SensibleData">Sensible Daten</a></li>
<li><a href="07112020200718-CheckSizeAndType">Prüfe Größe und Typ des Datensatzes</a></li>
<li><a href="07112020200718-TrainTestValidation">Train Validation Test Split</a></li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Hier das <a href="15112020-PythonSolutionsDataDownload">Notebook</a>, welches Downloadoptionen listet</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">tarfile</span>
<span class="kn">from</span> <span class="nn">six.moves</span> <span class="kn">import</span> <span class="n">urllib</span>

<span class="n">DOWNLOAD_ROOT</span> <span class="o">=</span> <span class="s2">&quot;https://raw.githubusercontent.com/ageron/handson-ml/master/&quot;</span>
<span class="n">HOUSING_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;datasets&quot;</span><span class="p">,</span> <span class="s2">&quot;housing&quot;</span><span class="p">)</span>
<span class="n">HOUSING_URL</span> <span class="o">=</span> <span class="n">DOWNLOAD_ROOT</span> <span class="o">+</span> <span class="s2">&quot;datasets/housing/housing.tgz&quot;</span>

<span class="k">def</span> <span class="nf">fetch_housing_data</span><span class="p">(</span><span class="n">housing_url</span><span class="o">=</span><span class="n">HOUSING_URL</span><span class="p">,</span> <span class="n">housing_path</span><span class="o">=</span><span class="n">HOUSING_PATH</span><span class="p">):</span>
    <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">housing_path</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">tgz_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">housing_path</span><span class="p">,</span> <span class="s2">&quot;housing.tgz&quot;</span><span class="p">)</span>
    <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">urlretrieve</span><span class="p">(</span><span class="n">housing_url</span><span class="p">,</span> <span class="n">tgz_path</span><span class="p">)</span>
    <span class="n">housing_tgz</span> <span class="o">=</span> <span class="n">tarfile</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tgz_path</span><span class="p">)</span>
    <span class="n">housing_tgz</span><span class="o">.</span><span class="n">extractall</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">housing_path</span><span class="p">)</span>
    <span class="n">housing_tgz</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>11
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>und nochmals etwas Text</p>

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
 

