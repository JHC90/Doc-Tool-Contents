<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Beschreibung">Beschreibung<a class="anchor-link" href="#Beschreibung">&#182;</a></h1><p>Dieses Notebook dient dazu, Möglichkeiten darzustellen wie Inhalte von remote Geräten geladen werden können.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>hier der Link zu meinem Public-Google-Folder // sprich hierzu braucht es keine Google-Anmeldung:<br>
    <a href="https://drive.google.com/drive/folders/17cptzULW_4is3t2_3eNy2oCEHGiDWevt?usp=sharing">https://drive.google.com/drive/folders/17cptzULW_4is3t2_3eNy2oCEHGiDWevt?usp=sharing</a><br>
und hier der link zu den beiden Dateien, die sich in dem Folder befinden:<br>
  1) <a href="https://drive.google.com/open?id=1WsaoZuh6eJVryqXBUNh2QUn0VbbXRyof">https://drive.google.com/open?id=1WsaoZuh6eJVryqXBUNh2QUn0VbbXRyof</a>  || DATA<br>
  2) <a href="https://drive.google.com/open?id=1KgWXbB9jtVUncE5R0AL9enfwWGwTE0AB">https://drive.google.com/open?id=1KgWXbB9jtVUncE5R0AL9enfwWGwTE0AB</a> || DESCRITPION<br></p>
<p>ggf änderung des Links zu einem Downloadlink nach folgendem Vorgehen: <a href="http://apps-experts.de/2014/10/das-neue-google-drive-45-direkte-downloadlinks-in-google-drive-erstellen/">http://apps-experts.de/2014/10/das-neue-google-drive-45-direkte-downloadlinks-in-google-drive-erstellen/</a></p>
<p>a)
<a href="https://drive.google.com/open?id=1WsaoZuh6eJVryqXBUNh2QUn0VbbXRyof/export?format=csv">https://drive.google.com/open?id=1WsaoZuh6eJVryqXBUNh2QUn0VbbXRyof/export?format=csv</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Requests">Requests<a class="anchor-link" href="#Requests">&#182;</a></h2><p>Download PDF-Datei von willkürlicher Quelle. Ist aber an sich egal von wo, hier kann ich auch andere Daten mit herunterladen. Wichtig ist nur dass hierbei keine Anmeldung an dem Remote Standort stattfindet.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">requests</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Download Starting...&#39;</span><span class="p">)</span>
<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;http://www.tutorialspoint.com/python3/python_tutorial.pdf&#39;</span> <span class="c1"># =&gt; Checken ob die Datei bereits vorliegt oder nicht</span>
<span class="n">r</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;./datasets/Sample-PDF.pdf&quot;</span>
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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Github">Github<a class="anchor-link" href="#Github">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
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
<span class="n">fetch_housing_data</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Gdown-bei-Public-G-Drvie-=-keine-Anmeldung-bei-Google">Gdown bei Public-G-Drvie = keine Anmeldung bei Google<a class="anchor-link" href="#Gdown-bei-Public-G-Drvie-=-keine-Anmeldung-bei-Google">&#182;</a></h2><p><a href="https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url">https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url</a><br></p>
<p>die Bibloiothek ermöglicht es mir easy von Google-Drive Public daten herunterzuladen.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install gdown</span>
<span class="kn">import</span> <span class="nn">gdown</span>

<span class="n">url</span> <span class="o">=</span> <span class="s1">&#39;https://drive.google.com/uc?id=0B9P1L--7Wd2vU3VUVlFnbTgtS2c&#39;</span>
<span class="n">output</span> <span class="o">=</span> <span class="s1">&#39;./datasets/spam.txt&#39;</span>
<span class="n">gdown</span><span class="o">.</span><span class="n">download</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">output</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> 
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Downloading...
From: https://drive.google.com/uc?id=0B9P1L--7Wd2vU3VUVlFnbTgtS2c
To: c:\DocTool\content\Docus\Informatik\Programmieren\Python\Lösungen\datasets\spam.txt
100%|██████████| 5.00/5.00 [00:00&lt;00:00, 5.00kB/s]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;./datasets/spam.txt&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Funktion-Data-Download">Funktion Data-Download<a class="anchor-link" href="#Funktion-Data-Download">&#182;</a></h1><p>Die Funktion besitzt etwas Intelligenz, da diese zunächst prüft ob das Dataset bereits heruntergeladen wurde. Die Daten werden nur dann heruntergeladen, wenn diese nicht bereits loakl vorliegen. Im weiteren werden die Daten heru</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">urlretrieve</span>
<span class="k">def</span> <span class="nf">download_dataset</span><span class="p">(</span><span class="n">url</span><span class="p">,</span><span class="n">dataset_file_path</span><span class="p">,</span><span class="n">extraction_directory</span><span class="p">):</span>
    <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">extraction_directory</span><span class="p">)):</span>
        <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">extraction_directory</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dataset_file_path</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;archive already downloaded.&quot;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;started loading archive from url </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">url</span><span class="p">))</span>
        <span class="n">filename</span><span class="p">,</span> <span class="n">head123er123s</span> <span class="o">=</span> <span class="n">urlretrieve</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">dataset_file_path</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;finished loading archive from url </span><span class="si">{}</span><span class="s2"> to </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">url</span><span class="p">,</span><span class="n">filename</span><span class="p">))</span>

<span class="n">urlDataSource</span> <span class="o">=</span> <span class="s1">&#39;http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz&#39;</span>
<span class="n">localExtractionFolder</span> <span class="o">=</span> <span class="s1">&#39;datasets/moviereviews&#39;</span>
<span class="n">localDataArchive</span> <span class="o">=</span> <span class="n">localExtractionFolder</span> <span class="o">+</span> <span class="s1">&#39;/aclImdb_v1.tar.gz&#39;</span>
<span class="n">textData</span> <span class="o">=</span> <span class="n">localExtractionFolder</span> <span class="o">+</span> <span class="s1">&#39;/aclImdb/&#39;</span>

<span class="n">download_dataset</span><span class="p">(</span><span class="n">urlDataSource</span><span class="p">,</span><span class="n">localDataArchive</span><span class="p">,</span><span class="n">localExtractionFolder</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;############&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Hier ein erneuter aufruf der Funktion mit den gleichen Paramtertern =&gt; Kein weitere Download:&#39;</span><span class="p">)</span>
<span class="n">download_dataset</span><span class="p">(</span><span class="n">urlDataSource</span><span class="p">,</span><span class="n">localDataArchive</span><span class="p">,</span><span class="n">localExtractionFolder</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>started loading archive from url http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
finished loading archive from url http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz to datasets/moviereviews/aclImdb_v1.tar.gz
############
Hier ein erneuter aufruf der Funktion mit den gleichen Paramtertern =&gt; Kein weitere Download:
archive already downloaded.
</pre>
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
 

