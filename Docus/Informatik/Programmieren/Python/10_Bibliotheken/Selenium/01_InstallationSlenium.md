<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-1">Video 1<a class="anchor-link" href="#Video-1">&#182;</a></h1><ul>
<li>Erklärung warum Selenium gut ist</li>
<li>Erklärung Basic-Installation <ul>
<li>Installation Bibliothek Selenium</li>
<li>Einbinden der Executable (Chromedriver, geko, etc) in dem OS</li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;u1T2v2Ucuuc&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

        <iframe
            width="800"
            height="300"
            src="https://www.youtube.com/embed/u1T2v2Ucuuc"
            frameborder="0"
            allowfullscreen
        ></iframe>
        
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Selenium = Programm, welches auch in Python genutzt werden kann</p>
<p>Automatisches User-Verhalten</p>
<ul>
<li>testen</li>
<li>Stupide Aufgaben Automatisieren</li>
<li>In Kombination mit Python </li>
</ul>
<h2 id="Technologien">Technologien<a class="anchor-link" href="#Technologien">&#182;</a></h2><ul>
<li>Python</li>
<li>pip</li>
<li><p>WebDriver für Browser</p>
<ul>
<li><p><a href="https://chromedriver.chromium.org/">Chrome</a> // Auswahl Linux / Windows
<img src="./imgs/InstallationChromium.png" alt=""></p>
</li>
<li><p><a href="https://github.com/mozilla/geckodriver/releases">Firefox</a> // windows und Linux</p>
</li>
<li><a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">Web-Driver-Edge</a> // nur Windows</li>
</ul>
</li>
</ul>
<p>der Webdriver muss heruntergeladen werden und im jeweiligen OS in die Pfad-Variablen hinzugefügt werden. <a href="https://github.com/JHC90/Windows/blob/master/Umgebungsvaribalen.md">Pfadvaribalen Windows</a>  oder <a href="https://github.com/JHC90/Linux/blob/master/Path-Variable.md">Pfadvariablen Linux</a></p>
<hr>
<p>Hier ein BSP für das einbinden einer Umgebungsvariable in Windows
<img src="./imgs/WindowsUmgebungsvariablen.png" alt=""></p>
<p>hier der <a href="./../../../../Operating-Informatik/Windows/Path-Variable.md">Link</a> zu der Erklärung wie man in Windows Dateien zum Pfad hinzufügt.</p>
<p>FUnktionsfähigt ist der Spass wenn chromedriver somit von der CLI aus aufgerufen werden kann:
<img src="./imgs/ChromeDriverVerify.png" alt=""></p>
<hr>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Installation von Slenium</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install selenium</span>
</pre></div>

    </div>
</div>
</div>

</div>
 

