'''''

{
"title": "Python-DataChecker",
"keywords": "Checkliste, DataSources",
"categories": "",
"description": "Hier eine Sammlung von Coding Snippet für den first Data-Check",
"level": "30",
"pageID": "07112020200718-Mini-Exploration"
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
<h1 id="Check">Check<a class="anchor-link" href="#Check">&#182;</a></h1><p>hier geht es darum dass sobald ein Datensatz eingelesen wird, dieser zunächst einmal "grundlegend" gecheckt wird. Anschließend kommt die EDA.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bibs</span>
<span class="c1"># !pip install missingno</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">missingno</span> <span class="k">as</span> <span class="nn">msno</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="einlesen-DF">einlesen DF<a class="anchor-link" href="#einlesen-DF">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;./datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Erste-Visualisierung">Erste Visualisierung<a class="anchor-link" href="#Erste-Visualisierung">&#182;</a></h1><p>hier prüft man ob auf den ersten Blick na werte vorhanden sind. Im weiteren muss man prüfen ob anstelle von Nan (not a number) ggf ein Platzhalter verwendet wurd (bspw wenn immer ein"?" verwendet wurde, so muss hierbei das ? durch Nan geändert werden)</p>
<p>wäre bspw immer ein ? als zeichen für einen NAN dann kann man im Pandas das wiefolgt ersetzen</p>
<blockquote><p>df = df.replace("?", np.nan)<br></p>
</blockquote>
<p>möglichkeit das herauszufinden:<br></p>
<blockquote><p>df.isin([" "])<br>
df.isin([" "]).any()<br>
df.isin([" "]).any().any()<br><br><br></p>
<p>df.isin(["?"])<br>
df.isin(["?"]).any()<br>
df.isin(["?"]).any().any()<br></p>
<p>print(df.isna())
print(df.isna().any())
print(df.isna().any().any())</p>
<p>print(df.isnull())
print(df.isnull().any())
print(df.isnull().any().any())</p>
</blockquote>
<p>Möglcihe Zeichen für naN "?", " "(leerzeichen)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">msno</span><span class="o">.</span><span class="n">matrix</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x2307e9dd310&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="685.472244pt" version="1.1" viewBox="0 0 1485.115 685.472244" width="1485.115pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 685.472244 

L 1485.115 685.472244 

L 1485.115 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 1376.265865 666.553023 

L 1460.1 666.553023 

L 1460.1 122.953023 

L 1376.265865 122.953023 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1"/>

   <g id="matplotlib.axis_2"/>

   <g id="line2d_1">

    <path clip-path="url(#pc498415187)" d="M 1418.182933 666.553023 

L 1418.182933 122.953023 

L 1418.182933 122.953023 

" style="fill:none;stroke:#404040;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_2">

    <defs>

     <path d="M 0 2.5 

C 0.663008 2.5 1.29895 2.236584 1.767767 1.767767 

C 2.236584 1.29895 2.5 0.663008 2.5 0 

C 2.5 -0.663008 2.236584 -1.29895 1.767767 -1.767767 

C 1.29895 -2.236584 0.663008 -2.5 0 -2.5 

C -0.663008 -2.5 -1.29895 -2.236584 -1.767767 -1.767767 

C -2.236584 -1.29895 -2.5 -0.663008 -2.5 0 

C -2.5 0.663008 -2.236584 1.29895 -1.767767 1.767767 

C -1.29895 2.236584 -0.663008 2.5 0 2.5 

z

" id="m9bba88fbe2" style="stroke:#404040;"/>

    </defs>

    <g clip-path="url(#pc498415187)">

     <use style="fill:#404040;stroke:#404040;" x="1418.182933" xlink:href="#m9bba88fbe2" y="666.553023"/>

    </g>

   </g>

   <g id="line2d_3">

    <g clip-path="url(#pc498415187)">

     <use style="fill:#404040;stroke:#404040;" x="1418.182933" xlink:href="#m9bba88fbe2" y="666.553023"/>

    </g>

   </g>

   <g id="text_1">

    <!-- 21 -->

    <defs>

     <path d="M 19.1875 8.296875 

L 53.609375 8.296875 

L 53.609375 0 

L 7.328125 0 

L 7.328125 8.296875 

Q 12.9375 14.109375 22.625 23.890625 

Q 32.328125 33.6875 34.8125 36.53125 

Q 39.546875 41.84375 41.421875 45.53125 

Q 43.3125 49.21875 43.3125 52.78125 

Q 43.3125 58.59375 39.234375 62.25 

Q 35.15625 65.921875 28.609375 65.921875 

Q 23.96875 65.921875 18.8125 64.3125 

Q 13.671875 62.703125 7.8125 59.421875 

L 7.8125 69.390625 

Q 13.765625 71.78125 18.9375 73 

Q 24.125 74.21875 28.421875 74.21875 

Q 39.75 74.21875 46.484375 68.546875 

Q 53.21875 62.890625 53.21875 53.421875 

Q 53.21875 48.921875 51.53125 44.890625 

Q 49.859375 40.875 45.40625 35.40625 

Q 44.1875 33.984375 37.640625 27.21875 

Q 31.109375 20.453125 19.1875 8.296875 

z

" id="DejaVuSans-50"/>

     <path d="M 12.40625 8.296875 

L 28.515625 8.296875 

L 28.515625 63.921875 

L 10.984375 60.40625 

L 10.984375 69.390625 

L 28.421875 72.90625 

L 38.28125 72.90625 

L 38.28125 8.296875 

L 54.390625 8.296875 

L 54.390625 0 

L 12.40625 0 

z

" id="DejaVuSans-49"/>

    </defs>

    <g transform="translate(1460.1 670.416148)scale(0.14 -0.14)">

     <use xlink:href="#DejaVuSans-50"/>

     <use x="63.623047" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_2">

    <!-- 21 -->

    <g transform="translate(1358.450865 670.416148)scale(0.14 -0.14)">

     <use xlink:href="#DejaVuSans-50"/>

     <use x="63.623047" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_3">

    <path d="M 65.1 666.553023 

L 1322.612019 666.553023 

L 1322.612019 122.953023 

L 65.1 122.953023 

z

" style="fill:#ffffff;"/>

   </g>

   <g clip-path="url(#p1dc8b36260)">

    <image height="7043" id="imagea7d42d10ee" transform="matrix(59.904762 0 0 0.07724 65.1 122.553023)" width="21" xlink:href="data:image/png;base64,

iVBORw0KGgoAAAANSUhEUgAAABUAABuDCAYAAAAH8Zj8AAAABHNCSVQICAgIfAhkiAAACBBJREFUeJztzEENADAIBDDA2PlXNUzwWdIKaCd5dWyuQ6lUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqVSqVQqlUqlUqlUKpVKpVKpVCqVSqUfpwumCjjCYWAEwwAAAABJRU5ErkJggg=="/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_1">

     <g id="text_3">

      <!-- customerID -->

      <defs>

       <path d="M 48.78125 52.59375 

L 48.78125 44.1875 

Q 44.96875 46.296875 41.140625 47.34375 

Q 37.3125 48.390625 33.40625 48.390625 

Q 24.65625 48.390625 19.8125 42.84375 

Q 14.984375 37.3125 14.984375 27.296875 

Q 14.984375 17.28125 19.8125 11.734375 

Q 24.65625 6.203125 33.40625 6.203125 

Q 37.3125 6.203125 41.140625 7.25 

Q 44.96875 8.296875 48.78125 10.40625 

L 48.78125 2.09375 

Q 45.015625 0.34375 40.984375 -0.53125 

Q 36.96875 -1.421875 32.421875 -1.421875 

Q 20.0625 -1.421875 12.78125 6.34375 

Q 5.515625 14.109375 5.515625 27.296875 

Q 5.515625 40.671875 12.859375 48.328125 

Q 20.21875 56 33.015625 56 

Q 37.15625 56 41.109375 55.140625 

Q 45.0625 54.296875 48.78125 52.59375 

z

" id="DejaVuSans-99"/>

       <path d="M 8.5 21.578125 

L 8.5 54.6875 

L 17.484375 54.6875 

L 17.484375 21.921875 

Q 17.484375 14.15625 20.5 10.265625 

Q 23.53125 6.390625 29.59375 6.390625 

Q 36.859375 6.390625 41.078125 11.03125 

Q 45.3125 15.671875 45.3125 23.6875 

L 45.3125 54.6875 

L 54.296875 54.6875 

L 54.296875 0 

L 45.3125 0 

L 45.3125 8.40625 

Q 42.046875 3.421875 37.71875 1 

Q 33.40625 -1.421875 27.6875 -1.421875 

Q 18.265625 -1.421875 13.375 4.4375 

Q 8.5 10.296875 8.5 21.578125 

z

M 31.109375 56 

z

" id="DejaVuSans-117"/>

       <path d="M 44.28125 53.078125 

L 44.28125 44.578125 

Q 40.484375 46.53125 36.375 47.5 

Q 32.28125 48.484375 27.875 48.484375 

Q 21.1875 48.484375 17.84375 46.4375 

Q 14.5 44.390625 14.5 40.28125 

Q 14.5 37.15625 16.890625 35.375 

Q 19.28125 33.59375 26.515625 31.984375 

L 29.59375 31.296875 

Q 39.15625 29.25 43.1875 25.515625 

Q 47.21875 21.78125 47.21875 15.09375 

Q 47.21875 7.46875 41.1875 3.015625 

Q 35.15625 -1.421875 24.609375 -1.421875 

Q 20.21875 -1.421875 15.453125 -0.5625 

Q 10.6875 0.296875 5.421875 2 

L 5.421875 11.28125 

Q 10.40625 8.6875 15.234375 7.390625 

Q 20.0625 6.109375 24.8125 6.109375 

Q 31.15625 6.109375 34.5625 8.28125 

Q 37.984375 10.453125 37.984375 14.40625 

Q 37.984375 18.0625 35.515625 20.015625 

Q 33.0625 21.96875 24.703125 23.78125 

L 21.578125 24.515625 

Q 13.234375 26.265625 9.515625 29.90625 

Q 5.8125 33.546875 5.8125 39.890625 

Q 5.8125 47.609375 11.28125 51.796875 

Q 16.75 56 26.8125 56 

Q 31.78125 56 36.171875 55.265625 

Q 40.578125 54.546875 44.28125 53.078125 

z

" id="DejaVuSans-115"/>

       <path d="M 18.3125 70.21875 

L 18.3125 54.6875 

L 36.8125 54.6875 

L 36.8125 47.703125 

L 18.3125 47.703125 

L 18.3125 18.015625 

Q 18.3125 11.328125 20.140625 9.421875 

Q 21.96875 7.515625 27.59375 7.515625 

L 36.8125 7.515625 

L 36.8125 0 

L 27.59375 0 

Q 17.1875 0 13.234375 3.875 

Q 9.28125 7.765625 9.28125 18.015625 

L 9.28125 47.703125 

L 2.6875 47.703125 

L 2.6875 54.6875 

L 9.28125 54.6875 

L 9.28125 70.21875 

z

" id="DejaVuSans-116"/>

       <path d="M 30.609375 48.390625 

Q 23.390625 48.390625 19.1875 42.75 

Q 14.984375 37.109375 14.984375 27.296875 

Q 14.984375 17.484375 19.15625 11.84375 

Q 23.34375 6.203125 30.609375 6.203125 

Q 37.796875 6.203125 41.984375 11.859375 

Q 46.1875 17.53125 46.1875 27.296875 

Q 46.1875 37.015625 41.984375 42.703125 

Q 37.796875 48.390625 30.609375 48.390625 

z

M 30.609375 56 

Q 42.328125 56 49.015625 48.375 

Q 55.71875 40.765625 55.71875 27.296875 

Q 55.71875 13.875 49.015625 6.21875 

Q 42.328125 -1.421875 30.609375 -1.421875 

Q 18.84375 -1.421875 12.171875 6.21875 

Q 5.515625 13.875 5.515625 27.296875 

Q 5.515625 40.765625 12.171875 48.375 

Q 18.84375 56 30.609375 56 

z

" id="DejaVuSans-111"/>

       <path d="M 52 44.1875 

Q 55.375 50.25 60.0625 53.125 

Q 64.75 56 71.09375 56 

Q 79.640625 56 84.28125 50.015625 

Q 88.921875 44.046875 88.921875 33.015625 

L 88.921875 0 

L 79.890625 0 

L 79.890625 32.71875 

Q 79.890625 40.578125 77.09375 44.375 

Q 74.3125 48.1875 68.609375 48.1875 

Q 61.625 48.1875 57.5625 43.546875 

Q 53.515625 38.921875 53.515625 30.90625 

L 53.515625 0 

L 44.484375 0 

L 44.484375 32.71875 

Q 44.484375 40.625 41.703125 44.40625 

Q 38.921875 48.1875 33.109375 48.1875 

Q 26.21875 48.1875 22.15625 43.53125 

Q 18.109375 38.875 18.109375 30.90625 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.1875 51.21875 25.484375 53.609375 

Q 29.78125 56 35.6875 56 

Q 41.65625 56 45.828125 52.96875 

Q 50 49.953125 52 44.1875 

z

" id="DejaVuSans-109"/>

       <path d="M 56.203125 29.59375 

L 56.203125 25.203125 

L 14.890625 25.203125 

Q 15.484375 15.921875 20.484375 11.0625 

Q 25.484375 6.203125 34.421875 6.203125 

Q 39.59375 6.203125 44.453125 7.46875 

Q 49.3125 8.734375 54.109375 11.28125 

L 54.109375 2.78125 

Q 49.265625 0.734375 44.1875 -0.34375 

Q 39.109375 -1.421875 33.890625 -1.421875 

Q 20.796875 -1.421875 13.15625 6.1875 

Q 5.515625 13.8125 5.515625 26.8125 

Q 5.515625 40.234375 12.765625 48.109375 

Q 20.015625 56 32.328125 56 

Q 43.359375 56 49.78125 48.890625 

Q 56.203125 41.796875 56.203125 29.59375 

z

M 47.21875 32.234375 

Q 47.125 39.59375 43.09375 43.984375 

Q 39.0625 48.390625 32.421875 48.390625 

Q 24.90625 48.390625 20.390625 44.140625 

Q 15.875 39.890625 15.1875 32.171875 

z

" id="DejaVuSans-101"/>

       <path d="M 41.109375 46.296875 

Q 39.59375 47.171875 37.8125 47.578125 

Q 36.03125 48 33.890625 48 

Q 26.265625 48 22.1875 43.046875 

Q 18.109375 38.09375 18.109375 28.8125 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 20.953125 51.171875 25.484375 53.578125 

Q 30.03125 56 36.53125 56 

Q 37.453125 56 38.578125 55.875 

Q 39.703125 55.765625 41.0625 55.515625 

z

" id="DejaVuSans-114"/>

       <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 0 

L 9.8125 0 

z

" id="DejaVuSans-73"/>

       <path d="M 19.671875 64.796875 

L 19.671875 8.109375 

L 31.59375 8.109375 

Q 46.6875 8.109375 53.6875 14.9375 

Q 60.6875 21.78125 60.6875 36.53125 

Q 60.6875 51.171875 53.6875 57.984375 

Q 46.6875 64.796875 31.59375 64.796875 

z

M 9.8125 72.90625 

L 30.078125 72.90625 

Q 51.265625 72.90625 61.171875 64.09375 

Q 71.09375 55.28125 71.09375 36.53125 

Q 71.09375 17.671875 61.125 8.828125 

Q 51.171875 0 30.078125 0 

L 9.8125 0 

z

" id="DejaVuSans-68"/>

      </defs>

      <g transform="translate(103.637413 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-99"/>

       <use x="54.980469" xlink:href="#DejaVuSans-117"/>

       <use x="118.359375" xlink:href="#DejaVuSans-115"/>

       <use x="170.458984" xlink:href="#DejaVuSans-116"/>

       <use x="209.667969" xlink:href="#DejaVuSans-111"/>

       <use x="270.849609" xlink:href="#DejaVuSans-109"/>

       <use x="368.261719" xlink:href="#DejaVuSans-101"/>

       <use x="429.785156" xlink:href="#DejaVuSans-114"/>

       <use x="470.898438" xlink:href="#DejaVuSans-73"/>

       <use x="500.390625" xlink:href="#DejaVuSans-68"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="text_4">

      <!-- gender -->

      <defs>

       <path d="M 45.40625 27.984375 

Q 45.40625 37.75 41.375 43.109375 

Q 37.359375 48.484375 30.078125 48.484375 

Q 22.859375 48.484375 18.828125 43.109375 

Q 14.796875 37.75 14.796875 27.984375 

Q 14.796875 18.265625 18.828125 12.890625 

Q 22.859375 7.515625 30.078125 7.515625 

Q 37.359375 7.515625 41.375 12.890625 

Q 45.40625 18.265625 45.40625 27.984375 

z

M 54.390625 6.78125 

Q 54.390625 -7.171875 48.1875 -13.984375 

Q 42 -20.796875 29.203125 -20.796875 

Q 24.46875 -20.796875 20.265625 -20.09375 

Q 16.0625 -19.390625 12.109375 -17.921875 

L 12.109375 -9.1875 

Q 16.0625 -11.328125 19.921875 -12.34375 

Q 23.78125 -13.375 27.78125 -13.375 

Q 36.625 -13.375 41.015625 -8.765625 

Q 45.40625 -4.15625 45.40625 5.171875 

L 45.40625 9.625 

Q 42.625 4.78125 38.28125 2.390625 

Q 33.9375 0 27.875 0 

Q 17.828125 0 11.671875 7.65625 

Q 5.515625 15.328125 5.515625 27.984375 

Q 5.515625 40.671875 11.671875 48.328125 

Q 17.828125 56 27.875 56 

Q 33.9375 56 38.28125 53.609375 

Q 42.625 51.21875 45.40625 46.390625 

L 45.40625 54.6875 

L 54.390625 54.6875 

z

" id="DejaVuSans-103"/>

       <path d="M 54.890625 33.015625 

L 54.890625 0 

L 45.90625 0 

L 45.90625 32.71875 

Q 45.90625 40.484375 42.875 44.328125 

Q 39.84375 48.1875 33.796875 48.1875 

Q 26.515625 48.1875 22.3125 43.546875 

Q 18.109375 38.921875 18.109375 30.90625 

L 18.109375 0 

L 9.078125 0 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-110"/>

       <path d="M 45.40625 46.390625 

L 45.40625 75.984375 

L 54.390625 75.984375 

L 54.390625 0 

L 45.40625 0 

L 45.40625 8.203125 

Q 42.578125 3.328125 38.25 0.953125 

Q 33.9375 -1.421875 27.875 -1.421875 

Q 17.96875 -1.421875 11.734375 6.484375 

Q 5.515625 14.40625 5.515625 27.296875 

Q 5.515625 40.1875 11.734375 48.09375 

Q 17.96875 56 27.875 56 

Q 33.9375 56 38.25 53.625 

Q 42.578125 51.265625 45.40625 46.390625 

z

M 14.796875 27.296875 

Q 14.796875 17.390625 18.875 11.75 

Q 22.953125 6.109375 30.078125 6.109375 

Q 37.203125 6.109375 41.296875 11.75 

Q 45.40625 17.390625 45.40625 27.296875 

Q 45.40625 37.203125 41.296875 42.84375 

Q 37.203125 48.484375 30.078125 48.484375 

Q 22.953125 48.484375 18.875 42.84375 

Q 14.796875 37.203125 14.796875 27.296875 

z

" id="DejaVuSans-100"/>

      </defs>

      <g transform="translate(163.518938 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-103"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-110"/>

       <use x="188.378906" xlink:href="#DejaVuSans-100"/>

       <use x="251.855469" xlink:href="#DejaVuSans-101"/>

       <use x="313.378906" xlink:href="#DejaVuSans-114"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="text_5">

      <!-- SeniorCitizen -->

      <defs>

       <path d="M 53.515625 70.515625 

L 53.515625 60.890625 

Q 47.90625 63.578125 42.921875 64.890625 

Q 37.9375 66.21875 33.296875 66.21875 

Q 25.25 66.21875 20.875 63.09375 

Q 16.5 59.96875 16.5 54.203125 

Q 16.5 49.359375 19.40625 46.890625 

Q 22.3125 44.4375 30.421875 42.921875 

L 36.375 41.703125 

Q 47.40625 39.59375 52.65625 34.296875 

Q 57.90625 29 57.90625 20.125 

Q 57.90625 9.515625 50.796875 4.046875 

Q 43.703125 -1.421875 29.984375 -1.421875 

Q 24.8125 -1.421875 18.96875 -0.25 

Q 13.140625 0.921875 6.890625 3.21875 

L 6.890625 13.375 

Q 12.890625 10.015625 18.65625 8.296875 

Q 24.421875 6.59375 29.984375 6.59375 

Q 38.421875 6.59375 43.015625 9.90625 

Q 47.609375 13.234375 47.609375 19.390625 

Q 47.609375 24.75 44.3125 27.78125 

Q 41.015625 30.8125 33.5 32.328125 

L 27.484375 33.5 

Q 16.453125 35.6875 11.515625 40.375 

Q 6.59375 45.0625 6.59375 53.421875 

Q 6.59375 63.09375 13.40625 68.65625 

Q 20.21875 74.21875 32.171875 74.21875 

Q 37.3125 74.21875 42.625 73.28125 

Q 47.953125 72.359375 53.515625 70.515625 

z

" id="DejaVuSans-83"/>

       <path d="M 9.421875 54.6875 

L 18.40625 54.6875 

L 18.40625 0 

L 9.421875 0 

z

M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 64.59375 

L 9.421875 64.59375 

z

" id="DejaVuSans-105"/>

       <path d="M 64.40625 67.28125 

L 64.40625 56.890625 

Q 59.421875 61.53125 53.78125 63.8125 

Q 48.140625 66.109375 41.796875 66.109375 

Q 29.296875 66.109375 22.65625 58.46875 

Q 16.015625 50.828125 16.015625 36.375 

Q 16.015625 21.96875 22.65625 14.328125 

Q 29.296875 6.6875 41.796875 6.6875 

Q 48.140625 6.6875 53.78125 8.984375 

Q 59.421875 11.28125 64.40625 15.921875 

L 64.40625 5.609375 

Q 59.234375 2.09375 53.4375 0.328125 

Q 47.65625 -1.421875 41.21875 -1.421875 

Q 24.65625 -1.421875 15.125 8.703125 

Q 5.609375 18.84375 5.609375 36.375 

Q 5.609375 53.953125 15.125 64.078125 

Q 24.65625 74.21875 41.21875 74.21875 

Q 47.75 74.21875 53.53125 72.484375 

Q 59.328125 70.75 64.40625 67.28125 

z

" id="DejaVuSans-67"/>

       <path d="M 5.515625 54.6875 

L 48.1875 54.6875 

L 48.1875 46.484375 

L 14.40625 7.171875 

L 48.1875 7.171875 

L 48.1875 0 

L 4.296875 0 

L 4.296875 8.203125 

L 38.09375 47.515625 

L 5.515625 47.515625 

z

" id="DejaVuSans-122"/>

      </defs>

      <g transform="translate(223.400463 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-110"/>

       <use x="188.378906" xlink:href="#DejaVuSans-105"/>

       <use x="216.162109" xlink:href="#DejaVuSans-111"/>

       <use x="277.34375" xlink:href="#DejaVuSans-114"/>

       <use x="318.457031" xlink:href="#DejaVuSans-67"/>

       <use x="388.28125" xlink:href="#DejaVuSans-105"/>

       <use x="416.064453" xlink:href="#DejaVuSans-116"/>

       <use x="455.273438" xlink:href="#DejaVuSans-105"/>

       <use x="483.056641" xlink:href="#DejaVuSans-122"/>

       <use x="535.546875" xlink:href="#DejaVuSans-101"/>

       <use x="597.070312" xlink:href="#DejaVuSans-110"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="text_6">

      <!-- Partner -->

      <defs>

       <path d="M 19.671875 64.796875 

L 19.671875 37.40625 

L 32.078125 37.40625 

Q 38.96875 37.40625 42.71875 40.96875 

Q 46.484375 44.53125 46.484375 51.125 

Q 46.484375 57.671875 42.71875 61.234375 

Q 38.96875 64.796875 32.078125 64.796875 

z

M 9.8125 72.90625 

L 32.078125 72.90625 

Q 44.34375 72.90625 50.609375 67.359375 

Q 56.890625 61.8125 56.890625 51.125 

Q 56.890625 40.328125 50.609375 34.8125 

Q 44.34375 29.296875 32.078125 29.296875 

L 19.671875 29.296875 

L 19.671875 0 

L 9.8125 0 

z

" id="DejaVuSans-80"/>

       <path d="M 34.28125 27.484375 

Q 23.390625 27.484375 19.1875 25 

Q 14.984375 22.515625 14.984375 16.5 

Q 14.984375 11.71875 18.140625 8.90625 

Q 21.296875 6.109375 26.703125 6.109375 

Q 34.1875 6.109375 38.703125 11.40625 

Q 43.21875 16.703125 43.21875 25.484375 

L 43.21875 27.484375 

z

M 52.203125 31.203125 

L 52.203125 0 

L 43.21875 0 

L 43.21875 8.296875 

Q 40.140625 3.328125 35.546875 0.953125 

Q 30.953125 -1.421875 24.3125 -1.421875 

Q 15.921875 -1.421875 10.953125 3.296875 

Q 6 8.015625 6 15.921875 

Q 6 25.140625 12.171875 29.828125 

Q 18.359375 34.515625 30.609375 34.515625 

L 43.21875 34.515625 

L 43.21875 35.40625 

Q 43.21875 41.609375 39.140625 45 

Q 35.0625 48.390625 27.6875 48.390625 

Q 23 48.390625 18.546875 47.265625 

Q 14.109375 46.140625 10.015625 43.890625 

L 10.015625 52.203125 

Q 14.9375 54.109375 19.578125 55.046875 

Q 24.21875 56 28.609375 56 

Q 40.484375 56 46.34375 49.84375 

Q 52.203125 43.703125 52.203125 31.203125 

z

" id="DejaVuSans-97"/>

      </defs>

      <g transform="translate(283.281987 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="55.802734" xlink:href="#DejaVuSans-97"/>

       <use x="117.082031" xlink:href="#DejaVuSans-114"/>

       <use x="158.195312" xlink:href="#DejaVuSans-116"/>

       <use x="197.404297" xlink:href="#DejaVuSans-110"/>

       <use x="260.783203" xlink:href="#DejaVuSans-101"/>

       <use x="322.306641" xlink:href="#DejaVuSans-114"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="text_7">

      <!-- Dependents -->

      <defs>

       <path d="M 18.109375 8.203125 

L 18.109375 -20.796875 

L 9.078125 -20.796875 

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.390625 

Q 20.953125 51.265625 25.265625 53.625 

Q 29.59375 56 35.59375 56 

Q 45.5625 56 51.78125 48.09375 

Q 58.015625 40.1875 58.015625 27.296875 

Q 58.015625 14.40625 51.78125 6.484375 

Q 45.5625 -1.421875 35.59375 -1.421875 

Q 29.59375 -1.421875 25.265625 0.953125 

Q 20.953125 3.328125 18.109375 8.203125 

z

M 48.6875 27.296875 

Q 48.6875 37.203125 44.609375 42.84375 

Q 40.53125 48.484375 33.40625 48.484375 

Q 26.265625 48.484375 22.1875 42.84375 

Q 18.109375 37.203125 18.109375 27.296875 

Q 18.109375 17.390625 22.1875 11.75 

Q 26.265625 6.109375 33.40625 6.109375 

Q 40.53125 6.109375 44.609375 11.75 

Q 48.6875 17.390625 48.6875 27.296875 

z

" id="DejaVuSans-112"/>

      </defs>

      <g transform="translate(343.163512 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-68"/>

       <use x="77.001953" xlink:href="#DejaVuSans-101"/>

       <use x="138.525391" xlink:href="#DejaVuSans-112"/>

       <use x="202.001953" xlink:href="#DejaVuSans-101"/>

       <use x="263.525391" xlink:href="#DejaVuSans-110"/>

       <use x="326.904297" xlink:href="#DejaVuSans-100"/>

       <use x="390.380859" xlink:href="#DejaVuSans-101"/>

       <use x="451.904297" xlink:href="#DejaVuSans-110"/>

       <use x="515.283203" xlink:href="#DejaVuSans-116"/>

       <use x="554.492188" xlink:href="#DejaVuSans-115"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="text_8">

      <!-- tenure -->

      <g transform="translate(403.045037 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-116"/>

       <use x="39.208984" xlink:href="#DejaVuSans-101"/>

       <use x="100.732422" xlink:href="#DejaVuSans-110"/>

       <use x="164.111328" xlink:href="#DejaVuSans-117"/>

       <use x="227.490234" xlink:href="#DejaVuSans-114"/>

       <use x="266.353516" xlink:href="#DejaVuSans-101"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="text_9">

      <!-- PhoneService -->

      <defs>

       <path d="M 54.890625 33.015625 

L 54.890625 0 

L 45.90625 0 

L 45.90625 32.71875 

Q 45.90625 40.484375 42.875 44.328125 

Q 39.84375 48.1875 33.796875 48.1875 

Q 26.515625 48.1875 22.3125 43.546875 

Q 18.109375 38.921875 18.109375 30.90625 

L 18.109375 0 

L 9.078125 0 

L 9.078125 75.984375 

L 18.109375 75.984375 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-104"/>

       <path d="M 2.984375 54.6875 

L 12.5 54.6875 

L 29.59375 8.796875 

L 46.6875 54.6875 

L 56.203125 54.6875 

L 35.6875 0 

L 23.484375 0 

z

" id="DejaVuSans-118"/>

      </defs>

      <g transform="translate(462.926561 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="60.302734" xlink:href="#DejaVuSans-104"/>

       <use x="123.681641" xlink:href="#DejaVuSans-111"/>

       <use x="184.863281" xlink:href="#DejaVuSans-110"/>

       <use x="248.242188" xlink:href="#DejaVuSans-101"/>

       <use x="309.765625" xlink:href="#DejaVuSans-83"/>

       <use x="373.242188" xlink:href="#DejaVuSans-101"/>

       <use x="434.765625" xlink:href="#DejaVuSans-114"/>

       <use x="475.878906" xlink:href="#DejaVuSans-118"/>

       <use x="535.058594" xlink:href="#DejaVuSans-105"/>

       <use x="562.841797" xlink:href="#DejaVuSans-99"/>

       <use x="617.822266" xlink:href="#DejaVuSans-101"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="text_10">

      <!-- MultipleLines -->

      <defs>

       <path d="M 9.8125 72.90625 

L 24.515625 72.90625 

L 43.109375 23.296875 

L 61.8125 72.90625 

L 76.515625 72.90625 

L 76.515625 0 

L 66.890625 0 

L 66.890625 64.015625 

L 48.09375 14.015625 

L 38.1875 14.015625 

L 19.390625 64.015625 

L 19.390625 0 

L 9.8125 0 

z

" id="DejaVuSans-77"/>

       <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

       <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

      </defs>

      <g transform="translate(522.808086 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-77"/>

       <use x="86.279297" xlink:href="#DejaVuSans-117"/>

       <use x="149.658203" xlink:href="#DejaVuSans-108"/>

       <use x="177.441406" xlink:href="#DejaVuSans-116"/>

       <use x="216.650391" xlink:href="#DejaVuSans-105"/>

       <use x="244.433594" xlink:href="#DejaVuSans-112"/>

       <use x="307.910156" xlink:href="#DejaVuSans-108"/>

       <use x="335.693359" xlink:href="#DejaVuSans-101"/>

       <use x="397.216797" xlink:href="#DejaVuSans-76"/>

       <use x="452.929688" xlink:href="#DejaVuSans-105"/>

       <use x="480.712891" xlink:href="#DejaVuSans-110"/>

       <use x="544.091797" xlink:href="#DejaVuSans-101"/>

       <use x="605.615234" xlink:href="#DejaVuSans-115"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="text_11">

      <!-- InternetService -->

      <g transform="translate(582.689611 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-73"/>

       <use x="29.492188" xlink:href="#DejaVuSans-110"/>

       <use x="92.871094" xlink:href="#DejaVuSans-116"/>

       <use x="132.080078" xlink:href="#DejaVuSans-101"/>

       <use x="193.603516" xlink:href="#DejaVuSans-114"/>

       <use x="232.966797" xlink:href="#DejaVuSans-110"/>

       <use x="296.345703" xlink:href="#DejaVuSans-101"/>

       <use x="357.869141" xlink:href="#DejaVuSans-116"/>

       <use x="397.078125" xlink:href="#DejaVuSans-83"/>

       <use x="460.554688" xlink:href="#DejaVuSans-101"/>

       <use x="522.078125" xlink:href="#DejaVuSans-114"/>

       <use x="563.191406" xlink:href="#DejaVuSans-118"/>

       <use x="622.371094" xlink:href="#DejaVuSans-105"/>

       <use x="650.154297" xlink:href="#DejaVuSans-99"/>

       <use x="705.134766" xlink:href="#DejaVuSans-101"/>

      </g>

     </g>

    </g>

    <g id="xtick_10">

     <g id="text_12">

      <!-- OnlineSecurity -->

      <defs>

       <path d="M 39.40625 66.21875 

Q 28.65625 66.21875 22.328125 58.203125 

Q 16.015625 50.203125 16.015625 36.375 

Q 16.015625 22.609375 22.328125 14.59375 

Q 28.65625 6.59375 39.40625 6.59375 

Q 50.140625 6.59375 56.421875 14.59375 

Q 62.703125 22.609375 62.703125 36.375 

Q 62.703125 50.203125 56.421875 58.203125 

Q 50.140625 66.21875 39.40625 66.21875 

z

M 39.40625 74.21875 

Q 54.734375 74.21875 63.90625 63.9375 

Q 73.09375 53.65625 73.09375 36.375 

Q 73.09375 19.140625 63.90625 8.859375 

Q 54.734375 -1.421875 39.40625 -1.421875 

Q 24.03125 -1.421875 14.8125 8.828125 

Q 5.609375 19.09375 5.609375 36.375 

Q 5.609375 53.65625 14.8125 63.9375 

Q 24.03125 74.21875 39.40625 74.21875 

z

" id="DejaVuSans-79"/>

       <path d="M 32.171875 -5.078125 

Q 28.375 -14.84375 24.75 -17.8125 

Q 21.140625 -20.796875 15.09375 -20.796875 

L 7.90625 -20.796875 

L 7.90625 -13.28125 

L 13.1875 -13.28125 

Q 16.890625 -13.28125 18.9375 -11.515625 

Q 21 -9.765625 23.484375 -3.21875 

L 25.09375 0.875 

L 2.984375 54.6875 

L 12.5 54.6875 

L 29.59375 11.921875 

L 46.6875 54.6875 

L 56.203125 54.6875 

z

" id="DejaVuSans-121"/>

      </defs>

      <g transform="translate(642.571136 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-79"/>

       <use x="78.710938" xlink:href="#DejaVuSans-110"/>

       <use x="142.089844" xlink:href="#DejaVuSans-108"/>

       <use x="169.873047" xlink:href="#DejaVuSans-105"/>

       <use x="197.65625" xlink:href="#DejaVuSans-110"/>

       <use x="261.035156" xlink:href="#DejaVuSans-101"/>

       <use x="322.558594" xlink:href="#DejaVuSans-83"/>

       <use x="386.035156" xlink:href="#DejaVuSans-101"/>

       <use x="447.558594" xlink:href="#DejaVuSans-99"/>

       <use x="502.539062" xlink:href="#DejaVuSans-117"/>

       <use x="565.917969" xlink:href="#DejaVuSans-114"/>

       <use x="607.03125" xlink:href="#DejaVuSans-105"/>

       <use x="634.814453" xlink:href="#DejaVuSans-116"/>

       <use x="674.023438" xlink:href="#DejaVuSans-121"/>

      </g>

     </g>

    </g>

    <g id="xtick_11">

     <g id="text_13">

      <!-- OnlineBackup -->

      <defs>

       <path d="M 19.671875 34.8125 

L 19.671875 8.109375 

L 35.5 8.109375 

Q 43.453125 8.109375 47.28125 11.40625 

Q 51.125 14.703125 51.125 21.484375 

Q 51.125 28.328125 47.28125 31.5625 

Q 43.453125 34.8125 35.5 34.8125 

z

M 19.671875 64.796875 

L 19.671875 42.828125 

L 34.28125 42.828125 

Q 41.5 42.828125 45.03125 45.53125 

Q 48.578125 48.25 48.578125 53.8125 

Q 48.578125 59.328125 45.03125 62.0625 

Q 41.5 64.796875 34.28125 64.796875 

z

M 9.8125 72.90625 

L 35.015625 72.90625 

Q 46.296875 72.90625 52.390625 68.21875 

Q 58.5 63.53125 58.5 54.890625 

Q 58.5 48.1875 55.375 44.234375 

Q 52.25 40.28125 46.1875 39.3125 

Q 53.46875 37.75 57.5 32.78125 

Q 61.53125 27.828125 61.53125 20.40625 

Q 61.53125 10.640625 54.890625 5.3125 

Q 48.25 0 35.984375 0 

L 9.8125 0 

z

" id="DejaVuSans-66"/>

       <path d="M 9.078125 75.984375 

L 18.109375 75.984375 

L 18.109375 31.109375 

L 44.921875 54.6875 

L 56.390625 54.6875 

L 27.390625 29.109375 

L 57.625 0 

L 45.90625 0 

L 18.109375 26.703125 

L 18.109375 0 

L 9.078125 0 

z

" id="DejaVuSans-107"/>

      </defs>

      <g transform="translate(702.45266 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-79"/>

       <use x="78.710938" xlink:href="#DejaVuSans-110"/>

       <use x="142.089844" xlink:href="#DejaVuSans-108"/>

       <use x="169.873047" xlink:href="#DejaVuSans-105"/>

       <use x="197.65625" xlink:href="#DejaVuSans-110"/>

       <use x="261.035156" xlink:href="#DejaVuSans-101"/>

       <use x="322.558594" xlink:href="#DejaVuSans-66"/>

       <use x="391.162109" xlink:href="#DejaVuSans-97"/>

       <use x="452.441406" xlink:href="#DejaVuSans-99"/>

       <use x="507.421875" xlink:href="#DejaVuSans-107"/>

       <use x="562.207031" xlink:href="#DejaVuSans-117"/>

       <use x="625.585938" xlink:href="#DejaVuSans-112"/>

      </g>

     </g>

    </g>

    <g id="xtick_12">

     <g id="text_14">

      <!-- DeviceProtection -->

      <g transform="translate(762.334185 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-68"/>

       <use x="77.001953" xlink:href="#DejaVuSans-101"/>

       <use x="138.525391" xlink:href="#DejaVuSans-118"/>

       <use x="197.705078" xlink:href="#DejaVuSans-105"/>

       <use x="225.488281" xlink:href="#DejaVuSans-99"/>

       <use x="280.46875" xlink:href="#DejaVuSans-101"/>

       <use x="341.992188" xlink:href="#DejaVuSans-80"/>

       <use x="400.544922" xlink:href="#DejaVuSans-114"/>

       <use x="439.408203" xlink:href="#DejaVuSans-111"/>

       <use x="500.589844" xlink:href="#DejaVuSans-116"/>

       <use x="539.798828" xlink:href="#DejaVuSans-101"/>

       <use x="601.322266" xlink:href="#DejaVuSans-99"/>

       <use x="656.302734" xlink:href="#DejaVuSans-116"/>

       <use x="695.511719" xlink:href="#DejaVuSans-105"/>

       <use x="723.294922" xlink:href="#DejaVuSans-111"/>

       <use x="784.476562" xlink:href="#DejaVuSans-110"/>

      </g>

     </g>

    </g>

    <g id="xtick_13">

     <g id="text_15">

      <!-- TechSupport -->

      <defs>

       <path d="M -0.296875 72.90625 

L 61.375 72.90625 

L 61.375 64.59375 

L 35.5 64.59375 

L 35.5 0 

L 25.59375 0 

L 25.59375 64.59375 

L -0.296875 64.59375 

z

" id="DejaVuSans-84"/>

      </defs>

      <g transform="translate(822.21571 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-84"/>

       <use x="44.083984" xlink:href="#DejaVuSans-101"/>

       <use x="105.607422" xlink:href="#DejaVuSans-99"/>

       <use x="160.587891" xlink:href="#DejaVuSans-104"/>

       <use x="223.966797" xlink:href="#DejaVuSans-83"/>

       <use x="287.443359" xlink:href="#DejaVuSans-117"/>

       <use x="350.822266" xlink:href="#DejaVuSans-112"/>

       <use x="414.298828" xlink:href="#DejaVuSans-112"/>

       <use x="477.775391" xlink:href="#DejaVuSans-111"/>

       <use x="538.957031" xlink:href="#DejaVuSans-114"/>

       <use x="580.070312" xlink:href="#DejaVuSans-116"/>

      </g>

     </g>

    </g>

    <g id="xtick_14">

     <g id="text_16">

      <!-- StreamingTV -->

      <defs>

       <path d="M 28.609375 0 

L 0.78125 72.90625 

L 11.078125 72.90625 

L 34.1875 11.53125 

L 57.328125 72.90625 

L 67.578125 72.90625 

L 39.796875 0 

z

" id="DejaVuSans-86"/>

      </defs>

      <g transform="translate(882.097234 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-116"/>

       <use x="102.685547" xlink:href="#DejaVuSans-114"/>

       <use x="141.548828" xlink:href="#DejaVuSans-101"/>

       <use x="203.072266" xlink:href="#DejaVuSans-97"/>

       <use x="264.351562" xlink:href="#DejaVuSans-109"/>

       <use x="361.763672" xlink:href="#DejaVuSans-105"/>

       <use x="389.546875" xlink:href="#DejaVuSans-110"/>

       <use x="452.925781" xlink:href="#DejaVuSans-103"/>

       <use x="516.402344" xlink:href="#DejaVuSans-84"/>

       <use x="577.486328" xlink:href="#DejaVuSans-86"/>

      </g>

     </g>

    </g>

    <g id="xtick_15">

     <g id="text_17">

      <!-- StreamingMovies -->

      <g transform="translate(941.978759 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-116"/>

       <use x="102.685547" xlink:href="#DejaVuSans-114"/>

       <use x="141.548828" xlink:href="#DejaVuSans-101"/>

       <use x="203.072266" xlink:href="#DejaVuSans-97"/>

       <use x="264.351562" xlink:href="#DejaVuSans-109"/>

       <use x="361.763672" xlink:href="#DejaVuSans-105"/>

       <use x="389.546875" xlink:href="#DejaVuSans-110"/>

       <use x="452.925781" xlink:href="#DejaVuSans-103"/>

       <use x="516.402344" xlink:href="#DejaVuSans-77"/>

       <use x="602.681641" xlink:href="#DejaVuSans-111"/>

       <use x="663.863281" xlink:href="#DejaVuSans-118"/>

       <use x="723.042969" xlink:href="#DejaVuSans-105"/>

       <use x="750.826172" xlink:href="#DejaVuSans-101"/>

       <use x="812.349609" xlink:href="#DejaVuSans-115"/>

      </g>

     </g>

    </g>

    <g id="xtick_16">

     <g id="text_18">

      <!-- Contract -->

      <g transform="translate(1001.860284 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-67"/>

       <use x="69.824219" xlink:href="#DejaVuSans-111"/>

       <use x="131.005859" xlink:href="#DejaVuSans-110"/>

       <use x="194.384766" xlink:href="#DejaVuSans-116"/>

       <use x="233.59375" xlink:href="#DejaVuSans-114"/>

       <use x="274.707031" xlink:href="#DejaVuSans-97"/>

       <use x="335.986328" xlink:href="#DejaVuSans-99"/>

       <use x="390.966797" xlink:href="#DejaVuSans-116"/>

      </g>

     </g>

    </g>

    <g id="xtick_17">

     <g id="text_19">

      <!-- PaperlessBilling -->

      <g transform="translate(1061.741809 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="55.802734" xlink:href="#DejaVuSans-97"/>

       <use x="117.082031" xlink:href="#DejaVuSans-112"/>

       <use x="180.558594" xlink:href="#DejaVuSans-101"/>

       <use x="242.082031" xlink:href="#DejaVuSans-114"/>

       <use x="283.195312" xlink:href="#DejaVuSans-108"/>

       <use x="310.978516" xlink:href="#DejaVuSans-101"/>

       <use x="372.501953" xlink:href="#DejaVuSans-115"/>

       <use x="424.601562" xlink:href="#DejaVuSans-115"/>

       <use x="476.701172" xlink:href="#DejaVuSans-66"/>

       <use x="545.304688" xlink:href="#DejaVuSans-105"/>

       <use x="573.087891" xlink:href="#DejaVuSans-108"/>

       <use x="600.871094" xlink:href="#DejaVuSans-108"/>

       <use x="628.654297" xlink:href="#DejaVuSans-105"/>

       <use x="656.4375" xlink:href="#DejaVuSans-110"/>

       <use x="719.816406" xlink:href="#DejaVuSans-103"/>

      </g>

     </g>

    </g>

    <g id="xtick_18">

     <g id="text_20">

      <!-- PaymentMethod -->

      <g transform="translate(1121.623333 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="55.802734" xlink:href="#DejaVuSans-97"/>

       <use x="117.082031" xlink:href="#DejaVuSans-121"/>

       <use x="176.261719" xlink:href="#DejaVuSans-109"/>

       <use x="273.673828" xlink:href="#DejaVuSans-101"/>

       <use x="335.197266" xlink:href="#DejaVuSans-110"/>

       <use x="398.576172" xlink:href="#DejaVuSans-116"/>

       <use x="437.785156" xlink:href="#DejaVuSans-77"/>

       <use x="524.064453" xlink:href="#DejaVuSans-101"/>

       <use x="585.587891" xlink:href="#DejaVuSans-116"/>

       <use x="624.796875" xlink:href="#DejaVuSans-104"/>

       <use x="688.175781" xlink:href="#DejaVuSans-111"/>

       <use x="749.357422" xlink:href="#DejaVuSans-100"/>

      </g>

     </g>

    </g>

    <g id="xtick_19">

     <g id="text_21">

      <!-- MonthlyCharges -->

      <g transform="translate(1181.504858 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-77"/>

       <use x="86.279297" xlink:href="#DejaVuSans-111"/>

       <use x="147.460938" xlink:href="#DejaVuSans-110"/>

       <use x="210.839844" xlink:href="#DejaVuSans-116"/>

       <use x="250.048828" xlink:href="#DejaVuSans-104"/>

       <use x="313.427734" xlink:href="#DejaVuSans-108"/>

       <use x="341.210938" xlink:href="#DejaVuSans-121"/>

       <use x="400.390625" xlink:href="#DejaVuSans-67"/>

       <use x="470.214844" xlink:href="#DejaVuSans-104"/>

       <use x="533.59375" xlink:href="#DejaVuSans-97"/>

       <use x="594.873047" xlink:href="#DejaVuSans-114"/>

       <use x="634.236328" xlink:href="#DejaVuSans-103"/>

       <use x="697.712891" xlink:href="#DejaVuSans-101"/>

       <use x="759.236328" xlink:href="#DejaVuSans-115"/>

      </g>

     </g>

    </g>

    <g id="xtick_20">

     <g id="text_22">

      <!-- TotalCharges -->

      <g transform="translate(1241.386383 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-84"/>

       <use x="44.083984" xlink:href="#DejaVuSans-111"/>

       <use x="105.265625" xlink:href="#DejaVuSans-116"/>

       <use x="144.474609" xlink:href="#DejaVuSans-97"/>

       <use x="205.753906" xlink:href="#DejaVuSans-108"/>

       <use x="233.537109" xlink:href="#DejaVuSans-67"/>

       <use x="303.361328" xlink:href="#DejaVuSans-104"/>

       <use x="366.740234" xlink:href="#DejaVuSans-97"/>

       <use x="428.019531" xlink:href="#DejaVuSans-114"/>

       <use x="467.382812" xlink:href="#DejaVuSans-103"/>

       <use x="530.859375" xlink:href="#DejaVuSans-101"/>

       <use x="592.382812" xlink:href="#DejaVuSans-115"/>

      </g>

     </g>

    </g>

    <g id="xtick_21">

     <g id="text_23">

      <!-- Churn -->

      <g transform="translate(1301.267908 113.600125)rotate(-45)scale(0.16 -0.16)">

       <use xlink:href="#DejaVuSans-67"/>

       <use x="69.824219" xlink:href="#DejaVuSans-104"/>

       <use x="133.203125" xlink:href="#DejaVuSans-117"/>

       <use x="196.582031" xlink:href="#DejaVuSans-114"/>

       <use x="235.945312" xlink:href="#DejaVuSans-110"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_1">

     <g id="text_24">

      <!-- 1 -->

      <g transform="translate(45.375 130.590052)scale(0.2 -0.2)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="text_25">

      <!-- 7043 -->

      <defs>

       <path d="M 8.203125 72.90625 

L 55.078125 72.90625 

L 55.078125 68.703125 

L 28.609375 0 

L 18.3125 0 

L 43.21875 64.59375 

L 8.203125 64.59375 

z

" id="DejaVuSans-55"/>

       <path d="M 31.78125 66.40625 

Q 24.171875 66.40625 20.328125 58.90625 

Q 16.5 51.421875 16.5 36.375 

Q 16.5 21.390625 20.328125 13.890625 

Q 24.171875 6.390625 31.78125 6.390625 

Q 39.453125 6.390625 43.28125 13.890625 

Q 47.125 21.390625 47.125 36.375 

Q 47.125 51.421875 43.28125 58.90625 

Q 39.453125 66.40625 31.78125 66.40625 

z

M 31.78125 74.21875 

Q 44.046875 74.21875 50.515625 64.515625 

Q 56.984375 54.828125 56.984375 36.375 

Q 56.984375 17.96875 50.515625 8.265625 

Q 44.046875 -1.421875 31.78125 -1.421875 

Q 19.53125 -1.421875 13.0625 8.265625 

Q 6.59375 17.96875 6.59375 36.375 

Q 6.59375 54.828125 13.0625 64.515625 

Q 19.53125 74.21875 31.78125 74.21875 

z

" id="DejaVuSans-48"/>

       <path d="M 37.796875 64.3125 

L 12.890625 25.390625 

L 37.796875 25.390625 

z

M 35.203125 72.90625 

L 47.609375 72.90625 

L 47.609375 25.390625 

L 58.015625 25.390625 

L 58.015625 17.1875 

L 47.609375 17.1875 

L 47.609375 0 

L 37.796875 0 

L 37.796875 17.1875 

L 4.890625 17.1875 

L 4.890625 26.703125 

z

" id="DejaVuSans-52"/>

       <path d="M 40.578125 39.3125 

Q 47.65625 37.796875 51.625 33 

Q 55.609375 28.21875 55.609375 21.1875 

Q 55.609375 10.40625 48.1875 4.484375 

Q 40.765625 -1.421875 27.09375 -1.421875 

Q 22.515625 -1.421875 17.65625 -0.515625 

Q 12.796875 0.390625 7.625 2.203125 

L 7.625 11.71875 

Q 11.71875 9.328125 16.59375 8.109375 

Q 21.484375 6.890625 26.8125 6.890625 

Q 36.078125 6.890625 40.9375 10.546875 

Q 45.796875 14.203125 45.796875 21.1875 

Q 45.796875 27.640625 41.28125 31.265625 

Q 36.765625 34.90625 28.71875 34.90625 

L 20.21875 34.90625 

L 20.21875 43.015625 

L 29.109375 43.015625 

Q 36.375 43.015625 40.234375 45.921875 

Q 44.09375 48.828125 44.09375 54.296875 

Q 44.09375 59.90625 40.109375 62.90625 

Q 36.140625 65.921875 28.71875 65.921875 

Q 24.65625 65.921875 20.015625 65.03125 

Q 15.375 64.15625 9.8125 62.3125 

L 9.8125 71.09375 

Q 15.4375 72.65625 20.34375 73.4375 

Q 25.25 74.21875 29.59375 74.21875 

Q 40.828125 74.21875 47.359375 69.109375 

Q 53.90625 64.015625 53.90625 55.328125 

Q 53.90625 49.265625 50.4375 45.09375 

Q 46.96875 40.921875 40.578125 39.3125 

z

" id="DejaVuSans-51"/>

      </defs>

      <g transform="translate(7.2 674.112869)scale(0.2 -0.2)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-52"/>

       <use x="190.869141" xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_4">

    <path clip-path="url(#p1dc8b36260)" d="M 124.981525 666.553023 

L 124.981525 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_5">

    <path clip-path="url(#p1dc8b36260)" d="M 184.863049 666.553023 

L 184.863049 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#p1dc8b36260)" d="M 244.744574 666.553023 

L 244.744574 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_7">

    <path clip-path="url(#p1dc8b36260)" d="M 304.626099 666.553023 

L 304.626099 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_8">

    <path clip-path="url(#p1dc8b36260)" d="M 364.507624 666.553023 

L 364.507624 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_9">

    <path clip-path="url(#p1dc8b36260)" d="M 424.389148 666.553023 

L 424.389148 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_10">

    <path clip-path="url(#p1dc8b36260)" d="M 484.270673 666.553023 

L 484.270673 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_11">

    <path clip-path="url(#p1dc8b36260)" d="M 544.152198 666.553023 

L 544.152198 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_12">

    <path clip-path="url(#p1dc8b36260)" d="M 604.033723 666.553023 

L 604.033723 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p1dc8b36260)" d="M 663.915247 666.553023 

L 663.915247 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_14">

    <path clip-path="url(#p1dc8b36260)" d="M 723.796772 666.553023 

L 723.796772 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_15">

    <path clip-path="url(#p1dc8b36260)" d="M 783.678297 666.553023 

L 783.678297 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_16">

    <path clip-path="url(#p1dc8b36260)" d="M 843.559821 666.553023 

L 843.559821 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_17">

    <path clip-path="url(#p1dc8b36260)" d="M 903.441346 666.553023 

L 903.441346 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_18">

    <path clip-path="url(#p1dc8b36260)" d="M 963.322871 666.553023 

L 963.322871 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_19">

    <path clip-path="url(#p1dc8b36260)" d="M 1023.204396 666.553023 

L 1023.204396 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_20">

    <path clip-path="url(#p1dc8b36260)" d="M 1083.08592 666.553023 

L 1083.08592 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_21">

    <path clip-path="url(#p1dc8b36260)" d="M 1142.967445 666.553023 

L 1142.967445 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_22">

    <path clip-path="url(#p1dc8b36260)" d="M 1202.84897 666.553023 

L 1202.84897 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_23">

    <path clip-path="url(#p1dc8b36260)" d="M 1262.730495 666.553023 

L 1262.730495 122.953023 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pc498415187">

   <rect height="543.6" width="83.834135" x="1376.265865" y="122.953023"/>

  </clipPath>

  <clipPath id="p1dc8b36260">

   <rect height="543.6" width="1257.512019" x="65.1" y="122.953023"/>

  </clipPath>

 </defs>

</svg>


</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Methoden-um-den-Datensatz-zu-sichten">Methoden um den Datensatz zu sichten<a class="anchor-link" href="#Methoden-um-den-Datensatz-zu-sichten">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#df.head123</span>
<span class="c1">#df.head123(15)</span>
<span class="c1">#df.tail</span>
<span class="c1">#df.tail(15)</span>
<span class="c1">#df.describe</span>
<span class="c1">#df.info</span>
<span class="c1">#df.isna().any()</span>
<span class="c1">#df.isna().any().any()</span>
<span class="c1">#df.dtypes</span>
<span class="c1">#df[&#39;gender&#39;].value_counts()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Na-Werte">Na-Werte<a class="anchor-link" href="#Na-Werte">&#182;</a></h1><p>hier immer die Fragestellung wie man mit nas umgeht. Entweder kick ich diese, oder impute die fehlenden werte. Wenn ich impute habe ich unterschiedliche Optionen hierbiet vorzugehen(Mean/Mode/eigenes Modell für die Imputation / random usw.). Die Imputation muss mit dem Business entsprechend rückgesprochen werden</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># einfachstes: Drop na</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">()</span> <span class="c1"># remove samples with all missing values</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(7043, 21)
(7043, 21)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Duplicate">Duplicate<a class="anchor-link" href="#Duplicate">&#182;</a></h1><p>Duplikate müssen im Falle ebenfalls aus dem Datensatz gekickt werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="o">~</span><span class="n">df</span><span class="o">.</span><span class="n">duplicated</span><span class="p">()]</span> <span class="c1"># remove duplicates</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(7043, 21)
(7043, 21)
</pre>
</div>
</div>

</div>
</div>

</div>
 

