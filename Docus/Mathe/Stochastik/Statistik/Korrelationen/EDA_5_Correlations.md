'''''

{
"title": "Korrelation-Python",
"keywords": "Statistic-Basics",
"categories": "",
"description": "Hier die Erklärung meiner Webseite",
"level": "10",
"pageID": "16112020-KorrelationPythonImplementierung"
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
<h1 id="Correlations">Correlations<a class="anchor-link" href="#Correlations">&#182;</a></h1><p><a href="16112020-KorrelationDefinition">Theorie Korrelation</a></p>

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
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="c1">#iris = pd.read_csv(&#39;./Sample-Projects/Iris/data/iris.data&#39;,delimiter=&#39;,&#39;,encoding=&#39;utf-8&#39;)</span>
<span class="n">iris</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;../Sample-Projects/Iris/data/iris.data&#39;</span><span class="p">,</span><span class="n">delimiter</span><span class="o">=</span><span class="s1">&#39;,&#39;</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
<span class="n">iris</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;SepalLengthCm&#39;</span><span class="p">,</span><span class="s1">&#39;SepalWidthCm&#39;</span><span class="p">,</span><span class="s1">&#39;PetalLengthCm&#39;</span><span class="p">,</span><span class="s1">&#39;PetalWidthCm&#39;</span><span class="p">,</span><span class="s1">&#39;Species&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Korrelations-Matrix">Korrelations-Matrix<a class="anchor-link" href="#Korrelations-Matrix">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">iris</span><span class="o">.</span><span class="n">corr</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[9]:</div>



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
      <th>SepalLengthCm</th>
      <th>SepalWidthCm</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
    </tr>
  </thead123>
  <tbody123>
    <tr>
      <th>SepalLengthCm</th>
      <td>1.000000</td>
      <td>-0.103784</td>
      <td>0.871283</td>
      <td>0.816971</td>
    </tr>
    <tr>
      <th>SepalWidthCm</th>
      <td>-0.103784</td>
      <td>1.000000</td>
      <td>-0.415218</td>
      <td>-0.350733</td>
    </tr>
    <tr>
      <th>PetalLengthCm</th>
      <td>0.871283</td>
      <td>-0.415218</td>
      <td>1.000000</td>
      <td>0.962314</td>
    </tr>
    <tr>
      <th>PetalWidthCm</th>
      <td>0.816971</td>
      <td>-0.350733</td>
      <td>0.962314</td>
      <td>1.000000</td>
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
<p>es sind die Interesaant die so nah wie möglich an entweder 1 oder -1 dran sind, 0 würde bedeuten kein Zusammenhang</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Seaborn">Seaborn<a class="anchor-link" href="#Seaborn">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Simple-Clustermatrix">Simple Clustermatrix<a class="anchor-link" href="#Simple-Clustermatrix">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="n">sns</span><span class="o">.</span><span class="n">clustermap</span><span class="p">(</span><span class="n">iris</span><span class="o">.</span><span class="n">corr</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;seaborn.matrix.ClusterGrid at 0x1dadb8f78b0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="712.677344pt" version="1.1" viewBox="0 0 712.478125 712.677344" width="712.478125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 712.677344 

L 712.478125 712.677344 

L 712.478125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="LineCollection_1">

    <path clip-path="url(#pe71a10a2f3)" d="M 143.44 484.439219 

L 138.227871 484.439219 

L 138.227871 620.679219 

L 143.44 620.679219 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

    <path clip-path="url(#pe71a10a2f3)" d="M 143.44 348.199219 

L 123.633428 348.199219 

L 123.633428 552.559219 

L 138.227871 552.559219 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

    <path clip-path="url(#pe71a10a2f3)" d="M 143.44 211.959219 

L 13.687619 211.959219 

L 13.687619 450.379219 

L 123.633428 450.379219 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

   </g>

  </g>

  <g id="axes_2">

   <g id="LineCollection_2">

    <path clip-path="url(#p8a1d515db4)" d="M 484.24 143.639219 

L 484.24 138.427089 

L 620.48 138.427089 

L 620.48 143.639219 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

    <path clip-path="url(#p8a1d515db4)" d="M 348 143.639219 

L 348 123.832647 

L 552.36 123.832647 

L 552.36 138.427089 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

    <path clip-path="url(#p8a1d515db4)" d="M 211.76 143.639219 

L 211.76 13.886838 

L 450.18 13.886838 

L 450.18 123.832647 

" style="fill:none;stroke:#333333;stroke-width:0.5;"/>

   </g>

  </g>

  <g id="axes_3">

   <g id="patch_2">

    <path d="M 143.64 688.799219 

L 688.6 688.799219 

L 688.6 143.839219 

L 143.64 143.839219 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="QuadMesh_1">

    <path clip-path="url(#p9d4fe9e66a)" d="M 143.64 143.839219 

L 279.88 143.839219 

L 279.88 280.079219 

L 143.64 280.079219 

L 143.64 143.839219 

" style="fill:#faebdd;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 279.88 143.839219 

L 416.12 143.839219 

L 416.12 280.079219 

L 279.88 280.079219 

L 279.88 143.839219 

" style="fill:#541e4e;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 416.12 143.839219 

L 552.36 143.839219 

L 552.36 280.079219 

L 416.12 280.079219 

L 416.12 143.839219 

" style="fill:#03051a;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 552.36 143.839219 

L 688.6 143.839219 

L 688.6 280.079219 

L 552.36 280.079219 

L 552.36 143.839219 

" style="fill:#110c24;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 143.64 280.079219 

L 279.88 280.079219 

L 279.88 416.319219 

L 143.64 416.319219 

L 143.64 280.079219 

" style="fill:#541e4e;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 279.88 280.079219 

L 416.12 280.079219 

L 416.12 416.319219 

L 279.88 416.319219 

L 279.88 280.079219 

" style="fill:#faebdd;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 416.12 280.079219 

L 552.36 280.079219 

L 552.36 416.319219 

L 416.12 416.319219 

L 416.12 280.079219 

" style="fill:#f7c9aa;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 552.36 280.079219 

L 688.6 280.079219 

L 688.6 416.319219 

L 552.36 416.319219 

L 552.36 280.079219 

" style="fill:#f6b995;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 143.64 416.319219 

L 279.88 416.319219 

L 279.88 552.559219 

L 143.64 552.559219 

L 143.64 416.319219 

" style="fill:#03051a;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 279.88 416.319219 

L 416.12 416.319219 

L 416.12 552.559219 

L 279.88 552.559219 

L 279.88 416.319219 

" style="fill:#f7c9aa;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 416.12 416.319219 

L 552.36 416.319219 

L 552.36 552.559219 

L 416.12 552.559219 

L 416.12 416.319219 

" style="fill:#faebdd;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 552.36 416.319219 

L 688.6 416.319219 

L 688.6 552.559219 

L 552.36 552.559219 

L 552.36 416.319219 

" style="fill:#f9e2d0;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 143.64 552.559219 

L 279.88 552.559219 

L 279.88 688.799219 

L 143.64 688.799219 

L 143.64 552.559219 

" style="fill:#110c24;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 279.88 552.559219 

L 416.12 552.559219 

L 416.12 688.799219 

L 279.88 688.799219 

L 279.88 552.559219 

" style="fill:#f6b995;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 416.12 552.559219 

L 552.36 552.559219 

L 552.36 688.799219 

L 416.12 688.799219 

L 416.12 552.559219 

" style="fill:#f9e2d0;"/>

    <path clip-path="url(#p9d4fe9e66a)" d="M 552.36 552.559219 

L 688.6 552.559219 

L 688.6 688.799219 

L 552.36 688.799219 

L 552.36 552.559219 

" style="fill:#faebdd;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m114fcb6382" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="211.76" xlink:href="#m114fcb6382" y="688.799219"/>

      </g>

     </g>

     <g id="text_1">

      <!-- SepalWidthCm -->

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

       <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

       <path d="M 3.328125 72.90625 

L 13.28125 72.90625 

L 28.609375 11.28125 

L 43.890625 72.90625 

L 54.984375 72.90625 

L 70.3125 11.28125 

L 85.59375 72.90625 

L 95.609375 72.90625 

L 77.296875 0 

L 64.890625 0 

L 49.515625 63.28125 

L 33.984375 0 

L 21.578125 0 

z

" id="DejaVuSans-87"/>

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

      </defs>

      <g transform="translate(174.996719 703.397656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-87"/>

       <use x="374.166016" xlink:href="#DejaVuSans-105"/>

       <use x="401.949219" xlink:href="#DejaVuSans-100"/>

       <use x="465.425781" xlink:href="#DejaVuSans-116"/>

       <use x="504.634766" xlink:href="#DejaVuSans-104"/>

       <use x="568.013672" xlink:href="#DejaVuSans-67"/>

       <use x="637.837891" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="348" xlink:href="#m114fcb6382" y="688.799219"/>

      </g>

     </g>

     <g id="text_2">

      <!-- SepalLengthCm -->

      <defs>

       <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

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

      </defs>

      <g transform="translate(308.513281 703.397656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-76"/>

       <use x="331.501953" xlink:href="#DejaVuSans-101"/>

       <use x="393.025391" xlink:href="#DejaVuSans-110"/>

       <use x="456.404297" xlink:href="#DejaVuSans-103"/>

       <use x="519.880859" xlink:href="#DejaVuSans-116"/>

       <use x="559.089844" xlink:href="#DejaVuSans-104"/>

       <use x="622.46875" xlink:href="#DejaVuSans-67"/>

       <use x="692.292969" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="484.24" xlink:href="#m114fcb6382" y="688.799219"/>

      </g>

     </g>

     <g id="text_3">

      <!-- PetalLengthCm -->

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

      </defs>

      <g transform="translate(446.307969 703.397656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-76"/>

       <use x="300.435547" xlink:href="#DejaVuSans-101"/>

       <use x="361.958984" xlink:href="#DejaVuSans-110"/>

       <use x="425.337891" xlink:href="#DejaVuSans-103"/>

       <use x="488.814453" xlink:href="#DejaVuSans-116"/>

       <use x="528.023438" xlink:href="#DejaVuSans-104"/>

       <use x="591.402344" xlink:href="#DejaVuSans-67"/>

       <use x="661.226562" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="620.48" xlink:href="#m114fcb6382" y="688.799219"/>

      </g>

     </g>

     <g id="text_4">

      <!-- PetalWidthCm -->

      <g transform="translate(585.271406 703.397656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-87"/>

       <use x="343.099609" xlink:href="#DejaVuSans-105"/>

       <use x="370.882812" xlink:href="#DejaVuSans-100"/>

       <use x="434.359375" xlink:href="#DejaVuSans-116"/>

       <use x="473.568359" xlink:href="#DejaVuSans-104"/>

       <use x="536.947266" xlink:href="#DejaVuSans-67"/>

       <use x="606.771484" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_5">

      <defs>

       <path d="M 0 0 

L 3.5 0 

" id="m5bc6cf89c7" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="688.6" xlink:href="#m5bc6cf89c7" y="211.959219"/>

      </g>

     </g>

     <g id="text_5">

      <!-- SepalWidthCm -->

      <g transform="translate(703.198438 281.686562)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-87"/>

       <use x="374.166016" xlink:href="#DejaVuSans-105"/>

       <use x="401.949219" xlink:href="#DejaVuSans-100"/>

       <use x="465.425781" xlink:href="#DejaVuSans-116"/>

       <use x="504.634766" xlink:href="#DejaVuSans-104"/>

       <use x="568.013672" xlink:href="#DejaVuSans-67"/>

       <use x="637.837891" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="688.6" xlink:href="#m5bc6cf89c7" y="348.199219"/>

      </g>

     </g>

     <g id="text_6">

      <!-- SepalLengthCm -->

      <g transform="translate(703.198438 423.373438)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-76"/>

       <use x="331.501953" xlink:href="#DejaVuSans-101"/>

       <use x="393.025391" xlink:href="#DejaVuSans-110"/>

       <use x="456.404297" xlink:href="#DejaVuSans-103"/>

       <use x="519.880859" xlink:href="#DejaVuSans-116"/>

       <use x="559.089844" xlink:href="#DejaVuSans-104"/>

       <use x="622.46875" xlink:href="#DejaVuSans-67"/>

       <use x="692.292969" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="688.6" xlink:href="#m5bc6cf89c7" y="484.439219"/>

      </g>

     </g>

     <g id="text_7">

      <!-- PetalLengthCm -->

      <g transform="translate(703.198438 556.504063)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-76"/>

       <use x="300.435547" xlink:href="#DejaVuSans-101"/>

       <use x="361.958984" xlink:href="#DejaVuSans-110"/>

       <use x="425.337891" xlink:href="#DejaVuSans-103"/>

       <use x="488.814453" xlink:href="#DejaVuSans-116"/>

       <use x="528.023438" xlink:href="#DejaVuSans-104"/>

       <use x="591.402344" xlink:href="#DejaVuSans-67"/>

       <use x="661.226562" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="688.6" xlink:href="#m5bc6cf89c7" y="620.679219"/>

      </g>

     </g>

     <g id="text_8">

      <!-- PetalWidthCm -->

      <g transform="translate(703.198438 687.297188)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-87"/>

       <use x="343.099609" xlink:href="#DejaVuSans-105"/>

       <use x="370.882812" xlink:href="#DejaVuSans-100"/>

       <use x="434.359375" xlink:href="#DejaVuSans-116"/>

       <use x="473.568359" xlink:href="#DejaVuSans-104"/>

       <use x="536.947266" xlink:href="#DejaVuSans-67"/>

       <use x="606.771484" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

   </g>

  </g>

  <g id="axes_4">

   <g id="patch_3">

    <path clip-path="url(#p8c7195d508)" d="M 10.8 140.599219 

L 10.8 140.092969 

L 10.8 11.505469 

L 10.8 10.999219 

L 46.8 10.999219 

L 46.8 11.505469 

L 46.8 140.092969 

L 46.8 140.599219 

z

" style="fill:#ffffff;stroke:#ffffff;stroke-linejoin:miter;stroke-width:0.01;"/>

   </g>

   <image height="130" id="image4cec0e0fba" transform="scale(1 -1)translate(0 -130)" width="36" x="11" xlink:href="data:image/png;base64,

iVBORw0KGgoAAAANSUhEUgAAACQAAACCCAYAAAAuRWprAAAABHNCSVQICAgIfAhkiAAAAUVJREFUeJzt27F1wzAMAFEChJfI/nPGqZkCLPkL3AT3DqBkS3bU5+e7ICozXzscVAYmtDkhbWRT6AJYaIR6PKGM/drhwCs0QhdG6AYotDQhr1C8djgAC3FC3lJrO6QVKu+UaULayLwLoyZU3g6NUEulJsQVAoUswHuZJ2RR9Z1CLeJSW9SmXr2sVfXa4B9T6AZYSBOaY3+h6msZeSMDC2lCWiHvSs2NbP2+djioHVqhEeqpndoO5RRqqeQKba0Q9gkN3CGtkCdU2MiwNwurEvumKO4QJhReodcKJxUj1FNR1oXIE1qaEFcoCvtlw9KEYmNC2kM9cIc2Vshbam2HwJFpQlqh2aELoBD2LN8rBC71jKwFLDSnrAcc2Qj1iEs9Qi2eUGj/c52lvlBrf147HHiFIqdQiyiEjSy8QpzQjKwFHFlad/s/VO0lx06/HlIAAAAASUVORK5CYII=" y="-10"/>

   <g id="matplotlib.axis_3"/>

   <g id="matplotlib.axis_4">

    <g id="ytick_5">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="125.469238"/>

      </g>

     </g>

     <g id="text_9">

      <!-- −0.25 -->

      <defs>

       <path d="M 10.59375 35.5 

L 73.1875 35.5 

L 73.1875 27.203125 

L 10.59375 27.203125 

z

" id="DejaVuSans-8722"/>

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

       <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

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

       <path d="M 10.796875 72.90625 

L 49.515625 72.90625 

L 49.515625 64.59375 

L 19.828125 64.59375 

L 19.828125 46.734375 

Q 21.96875 47.46875 24.109375 47.828125 

Q 26.265625 48.1875 28.421875 48.1875 

Q 40.625 48.1875 47.75 41.5 

Q 54.890625 34.8125 54.890625 23.390625 

Q 54.890625 11.625 47.5625 5.09375 

Q 40.234375 -1.421875 26.90625 -1.421875 

Q 22.3125 -1.421875 17.546875 -0.640625 

Q 12.796875 0.140625 7.71875 1.703125 

L 7.71875 11.625 

Q 12.109375 9.234375 16.796875 8.0625 

Q 21.484375 6.890625 26.703125 6.890625 

Q 35.15625 6.890625 40.078125 11.328125 

Q 45.015625 15.765625 45.015625 23.390625 

Q 45.015625 31 40.078125 35.4375 

Q 35.15625 39.890625 26.703125 39.890625 

Q 22.75 39.890625 18.8125 39.015625 

Q 14.890625 38.140625 10.796875 36.28125 

z

" id="DejaVuSans-53"/>

      </defs>

      <g transform="translate(53.8 129.268456)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-48"/>

       <use x="147.412109" xlink:href="#DejaVuSans-46"/>

       <use x="179.199219" xlink:href="#DejaVuSans-50"/>

       <use x="242.822266" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="102.575234"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 0.00 -->

      <g transform="translate(53.8 106.374453)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="79.68123"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 0.25 -->

      <g transform="translate(53.8 83.480449)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

       <use x="159.033203" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="56.787226"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 0.50 -->

      <g transform="translate(53.8 60.586445)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="33.893223"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 0.75 -->

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

      </defs>

      <g transform="translate(53.8 37.692441)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-55"/>

       <use x="159.033203" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_10">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.8" xlink:href="#m5bc6cf89c7" y="10.999219"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 1.00 -->

      <defs>

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

      <g transform="translate(53.8 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_4">

    <path d="M 10.8 140.599219 

L 10.8 140.092969 

L 10.8 11.505469 

L 10.8 10.999219 

L 46.8 10.999219 

L 46.8 11.505469 

L 46.8 140.092969 

L 46.8 140.599219 

z

" style="fill:none;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pe71a10a2f3">

   <rect height="544.96" width="136.24" x="7.2" y="143.839219"/>

  </clipPath>

  <clipPath id="p8a1d515db4">

   <rect height="136.24" width="544.96" x="143.64" y="7.399219"/>

  </clipPath>

  <clipPath id="p9d4fe9e66a">

   <rect height="544.96" width="544.96" x="143.64" y="143.839219"/>

  </clipPath>

  <clipPath id="p8c7195d508">

   <rect height="129.6" width="36" x="10.8" y="10.999219"/>

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
<h3 id="Complex-Clustermatrix-with-seaborn&amp;Matplotlib">Complex Clustermatrix with seaborn&amp;Matplotlib<a class="anchor-link" href="#Complex-Clustermatrix-with-seaborn&amp;Matplotlib">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">8</span><span class="p">))</span>
<span class="n">df_corr</span> <span class="o">=</span> <span class="n">iris</span><span class="o">.</span><span class="n">corr</span><span class="p">()</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">df_corr</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">&quot;RdYlGn&quot;</span><span class="p">)</span> 
<span class="n">bottom</span><span class="p">,</span> <span class="n">top</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">get_ylim</span><span class="p">()</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="n">bottom</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">,</span> <span class="n">top</span> <span class="o">-</span> <span class="mf">0.5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[11]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(4.5, -0.5)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="469.757344pt" version="1.1" viewBox="0 0 558.404938 469.757344" width="558.404938pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 469.757344 

L 558.404938 469.757344 

L 558.404938 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 23.878125 445.879219 

L 470.278125 445.879219 

L 470.278125 10.999219 

L 23.878125 10.999219 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="QuadMesh_1">

    <path clip-path="url(#p194fb5f47f)" d="M 23.878125 54.487219 

L 135.478125 54.487219 

L 135.478125 141.463219 

L 23.878125 141.463219 

L 23.878125 54.487219 

" style="fill:#006837;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 135.478125 54.487219 

L 247.078125 54.487219 

L 247.078125 141.463219 

L 135.478125 141.463219 

L 135.478125 54.487219 

" style="fill:#f67a49;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 247.078125 54.487219 

L 358.678125 54.487219 

L 358.678125 141.463219 

L 247.078125 141.463219 

L 247.078125 54.487219 

" style="fill:#17934e;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 358.678125 54.487219 

L 470.278125 54.487219 

L 470.278125 141.463219 

L 358.678125 141.463219 

L 358.678125 54.487219 

" style="fill:#30a356;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 23.878125 141.463219 

L 135.478125 141.463219 

L 135.478125 228.439219 

L 23.878125 228.439219 

L 23.878125 141.463219 

" style="fill:#f67a49;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 135.478125 141.463219 

L 247.078125 141.463219 

L 247.078125 228.439219 

L 135.478125 228.439219 

L 135.478125 141.463219 

" style="fill:#006837;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 247.078125 141.463219 

L 358.678125 141.463219 

L 358.678125 228.439219 

L 247.078125 228.439219 

L 247.078125 141.463219 

" style="fill:#a50026;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 358.678125 141.463219 

L 470.278125 141.463219 

L 470.278125 228.439219 

L 358.678125 228.439219 

L 358.678125 141.463219 

" style="fill:#bb1526;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 23.878125 228.439219 

L 135.478125 228.439219 

L 135.478125 315.415219 

L 23.878125 315.415219 

L 23.878125 228.439219 

" style="fill:#17934e;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 135.478125 228.439219 

L 247.078125 228.439219 

L 247.078125 315.415219 

L 135.478125 315.415219 

L 135.478125 228.439219 

" style="fill:#a50026;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 247.078125 228.439219 

L 358.678125 228.439219 

L 358.678125 315.415219 

L 247.078125 315.415219 

L 247.078125 228.439219 

" style="fill:#006837;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 358.678125 228.439219 

L 470.278125 228.439219 

L 470.278125 315.415219 

L 358.678125 315.415219 

L 358.678125 228.439219 

" style="fill:#06733d;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 23.878125 315.415219 

L 135.478125 315.415219 

L 135.478125 402.391219 

L 23.878125 402.391219 

L 23.878125 315.415219 

" style="fill:#30a356;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 135.478125 315.415219 

L 247.078125 315.415219 

L 247.078125 402.391219 

L 135.478125 402.391219 

L 135.478125 315.415219 

" style="fill:#bb1526;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 247.078125 315.415219 

L 358.678125 315.415219 

L 358.678125 402.391219 

L 247.078125 402.391219 

L 247.078125 315.415219 

" style="fill:#06733d;"/>

    <path clip-path="url(#p194fb5f47f)" d="M 358.678125 315.415219 

L 470.278125 315.415219 

L 470.278125 402.391219 

L 358.678125 402.391219 

L 358.678125 315.415219 

" style="fill:#006837;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m02cb8a5634" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="79.678125" xlink:href="#m02cb8a5634" y="445.879219"/>

      </g>

     </g>

     <g id="text_1">

      <!-- SepalLengthCm -->

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

      </defs>

      <g transform="translate(40.191406 460.477656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-76"/>

       <use x="331.501953" xlink:href="#DejaVuSans-101"/>

       <use x="393.025391" xlink:href="#DejaVuSans-110"/>

       <use x="456.404297" xlink:href="#DejaVuSans-103"/>

       <use x="519.880859" xlink:href="#DejaVuSans-116"/>

       <use x="559.089844" xlink:href="#DejaVuSans-104"/>

       <use x="622.46875" xlink:href="#DejaVuSans-67"/>

       <use x="692.292969" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="191.278125" xlink:href="#m02cb8a5634" y="445.879219"/>

      </g>

     </g>

     <g id="text_2">

      <!-- SepalWidthCm -->

      <defs>

       <path d="M 3.328125 72.90625 

L 13.28125 72.90625 

L 28.609375 11.28125 

L 43.890625 72.90625 

L 54.984375 72.90625 

L 70.3125 11.28125 

L 85.59375 72.90625 

L 95.609375 72.90625 

L 77.296875 0 

L 64.890625 0 

L 49.515625 63.28125 

L 33.984375 0 

L 21.578125 0 

z

" id="DejaVuSans-87"/>

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

      <g transform="translate(154.514844 460.477656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-87"/>

       <use x="374.166016" xlink:href="#DejaVuSans-105"/>

       <use x="401.949219" xlink:href="#DejaVuSans-100"/>

       <use x="465.425781" xlink:href="#DejaVuSans-116"/>

       <use x="504.634766" xlink:href="#DejaVuSans-104"/>

       <use x="568.013672" xlink:href="#DejaVuSans-67"/>

       <use x="637.837891" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="302.878125" xlink:href="#m02cb8a5634" y="445.879219"/>

      </g>

     </g>

     <g id="text_3">

      <!-- PetalLengthCm -->

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

      </defs>

      <g transform="translate(264.946094 460.477656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-76"/>

       <use x="300.435547" xlink:href="#DejaVuSans-101"/>

       <use x="361.958984" xlink:href="#DejaVuSans-110"/>

       <use x="425.337891" xlink:href="#DejaVuSans-103"/>

       <use x="488.814453" xlink:href="#DejaVuSans-116"/>

       <use x="528.023438" xlink:href="#DejaVuSans-104"/>

       <use x="591.402344" xlink:href="#DejaVuSans-67"/>

       <use x="661.226562" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="414.478125" xlink:href="#m02cb8a5634" y="445.879219"/>

      </g>

     </g>

     <g id="text_4">

      <!-- PetalWidthCm -->

      <g transform="translate(379.269531 460.477656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-87"/>

       <use x="343.099609" xlink:href="#DejaVuSans-105"/>

       <use x="370.882812" xlink:href="#DejaVuSans-100"/>

       <use x="434.359375" xlink:href="#DejaVuSans-116"/>

       <use x="473.568359" xlink:href="#DejaVuSans-104"/>

       <use x="536.947266" xlink:href="#DejaVuSans-67"/>

       <use x="606.771484" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_5">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m9f5932d154" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="23.878125" xlink:href="#m9f5932d154" y="97.975219"/>

      </g>

     </g>

     <g id="text_5">

      <!-- SepalLengthCm -->

      <g transform="translate(14.798438 173.149437)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-76"/>

       <use x="331.501953" xlink:href="#DejaVuSans-101"/>

       <use x="393.025391" xlink:href="#DejaVuSans-110"/>

       <use x="456.404297" xlink:href="#DejaVuSans-103"/>

       <use x="519.880859" xlink:href="#DejaVuSans-116"/>

       <use x="559.089844" xlink:href="#DejaVuSans-104"/>

       <use x="622.46875" xlink:href="#DejaVuSans-67"/>

       <use x="692.292969" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="23.878125" xlink:href="#m9f5932d154" y="184.951219"/>

      </g>

     </g>

     <g id="text_6">

      <!-- SepalWidthCm -->

      <g transform="translate(14.798438 254.678562)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-83"/>

       <use x="63.476562" xlink:href="#DejaVuSans-101"/>

       <use x="125" xlink:href="#DejaVuSans-112"/>

       <use x="188.476562" xlink:href="#DejaVuSans-97"/>

       <use x="249.755859" xlink:href="#DejaVuSans-108"/>

       <use x="277.539062" xlink:href="#DejaVuSans-87"/>

       <use x="374.166016" xlink:href="#DejaVuSans-105"/>

       <use x="401.949219" xlink:href="#DejaVuSans-100"/>

       <use x="465.425781" xlink:href="#DejaVuSans-116"/>

       <use x="504.634766" xlink:href="#DejaVuSans-104"/>

       <use x="568.013672" xlink:href="#DejaVuSans-67"/>

       <use x="637.837891" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="23.878125" xlink:href="#m9f5932d154" y="271.927219"/>

      </g>

     </g>

     <g id="text_7">

      <!-- PetalLengthCm -->

      <g transform="translate(14.798438 343.992062)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-76"/>

       <use x="300.435547" xlink:href="#DejaVuSans-101"/>

       <use x="361.958984" xlink:href="#DejaVuSans-110"/>

       <use x="425.337891" xlink:href="#DejaVuSans-103"/>

       <use x="488.814453" xlink:href="#DejaVuSans-116"/>

       <use x="528.023438" xlink:href="#DejaVuSans-104"/>

       <use x="591.402344" xlink:href="#DejaVuSans-67"/>

       <use x="661.226562" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="23.878125" xlink:href="#m9f5932d154" y="358.903219"/>

      </g>

     </g>

     <g id="text_8">

      <!-- PetalWidthCm -->

      <g transform="translate(14.798438 425.521187)rotate(-90)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-80"/>

       <use x="56.677734" xlink:href="#DejaVuSans-101"/>

       <use x="118.201172" xlink:href="#DejaVuSans-116"/>

       <use x="157.410156" xlink:href="#DejaVuSans-97"/>

       <use x="218.689453" xlink:href="#DejaVuSans-108"/>

       <use x="246.472656" xlink:href="#DejaVuSans-87"/>

       <use x="343.099609" xlink:href="#DejaVuSans-105"/>

       <use x="370.882812" xlink:href="#DejaVuSans-100"/>

       <use x="434.359375" xlink:href="#DejaVuSans-116"/>

       <use x="473.568359" xlink:href="#DejaVuSans-104"/>

       <use x="536.947266" xlink:href="#DejaVuSans-67"/>

       <use x="606.771484" xlink:href="#DejaVuSans-109"/>

      </g>

     </g>

    </g>

   </g>

   <g id="text_9">

    <!-- 1 -->

    <defs>

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

    <g style="fill:#ffffff;" transform="translate(76.496875 100.734594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_10">

    <!-- -0.1 -->

    <defs>

     <path d="M 4.890625 31.390625 

L 31.203125 31.390625 

L 31.203125 23.390625 

L 4.890625 23.390625 

z

" id="DejaVuSans-45"/>

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

     <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

    </defs>

    <g style="fill:#ffffff;" transform="translate(181.522656 100.734594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_11">

    <!-- 0.87 -->

    <defs>

     <path d="M 31.78125 34.625 

Q 24.75 34.625 20.71875 30.859375 

Q 16.703125 27.09375 16.703125 20.515625 

Q 16.703125 13.921875 20.71875 10.15625 

Q 24.75 6.390625 31.78125 6.390625 

Q 38.8125 6.390625 42.859375 10.171875 

Q 46.921875 13.96875 46.921875 20.515625 

Q 46.921875 27.09375 42.890625 30.859375 

Q 38.875 34.625 31.78125 34.625 

z

M 21.921875 38.8125 

Q 15.578125 40.375 12.03125 44.71875 

Q 8.5 49.078125 8.5 55.328125 

Q 8.5 64.0625 14.71875 69.140625 

Q 20.953125 74.21875 31.78125 74.21875 

Q 42.671875 74.21875 48.875 69.140625 

Q 55.078125 64.0625 55.078125 55.328125 

Q 55.078125 49.078125 51.53125 44.71875 

Q 48 40.375 41.703125 38.8125 

Q 48.828125 37.15625 52.796875 32.3125 

Q 56.78125 27.484375 56.78125 20.515625 

Q 56.78125 9.90625 50.3125 4.234375 

Q 43.84375 -1.421875 31.78125 -1.421875 

Q 19.734375 -1.421875 13.25 4.234375 

Q 6.78125 9.90625 6.78125 20.515625 

Q 6.78125 27.484375 10.78125 32.3125 

Q 14.796875 37.15625 21.921875 38.8125 

z

M 18.3125 54.390625 

Q 18.3125 48.734375 21.84375 45.5625 

Q 25.390625 42.390625 31.78125 42.390625 

Q 38.140625 42.390625 41.71875 45.5625 

Q 45.3125 48.734375 45.3125 54.390625 

Q 45.3125 60.0625 41.71875 63.234375 

Q 38.140625 66.40625 31.78125 66.40625 

Q 25.390625 66.40625 21.84375 63.234375 

Q 18.3125 60.0625 18.3125 54.390625 

z

" id="DejaVuSans-56"/>

     <path d="M 8.203125 72.90625 

L 55.078125 72.90625 

L 55.078125 68.703125 

L 28.609375 0 

L 18.3125 0 

L 43.21875 64.59375 

L 8.203125 64.59375 

z

" id="DejaVuSans-55"/>

    </defs>

    <g style="fill:#ffffff;" transform="translate(291.745313 100.734594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-56"/>

     <use x="159.033203" xlink:href="#DejaVuSans-55"/>

    </g>

   </g>

   <g id="text_12">

    <!-- 0.82 -->

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

    </defs>

    <g style="fill:#ffffff;" transform="translate(403.345313 100.734594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-56"/>

     <use x="159.033203" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

   <g id="text_13">

    <!-- -0.1 -->

    <g style="fill:#ffffff;" transform="translate(69.922656 187.710594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_14">

    <!-- 1 -->

    <g style="fill:#ffffff;" transform="translate(188.096875 187.710594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_15">

    <!-- -0.42 -->

    <defs>

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

    </defs>

    <g style="fill:#ffffff;" transform="translate(289.941406 187.710594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-52"/>

     <use x="195.117188" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

   <g id="text_16">

    <!-- -0.35 -->

    <defs>

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

     <path d="M 10.796875 72.90625 

L 49.515625 72.90625 

L 49.515625 64.59375 

L 19.828125 64.59375 

L 19.828125 46.734375 

Q 21.96875 47.46875 24.109375 47.828125 

Q 26.265625 48.1875 28.421875 48.1875 

Q 40.625 48.1875 47.75 41.5 

Q 54.890625 34.8125 54.890625 23.390625 

Q 54.890625 11.625 47.5625 5.09375 

Q 40.234375 -1.421875 26.90625 -1.421875 

Q 22.3125 -1.421875 17.546875 -0.640625 

Q 12.796875 0.140625 7.71875 1.703125 

L 7.71875 11.625 

Q 12.109375 9.234375 16.796875 8.0625 

Q 21.484375 6.890625 26.703125 6.890625 

Q 35.15625 6.890625 40.078125 11.328125 

Q 45.015625 15.765625 45.015625 23.390625 

Q 45.015625 31 40.078125 35.4375 

Q 35.15625 39.890625 26.703125 39.890625 

Q 22.75 39.890625 18.8125 39.015625 

Q 14.890625 38.140625 10.796875 36.28125 

z

" id="DejaVuSans-53"/>

    </defs>

    <g style="fill:#ffffff;" transform="translate(401.541406 187.710594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-51"/>

     <use x="195.117188" xlink:href="#DejaVuSans-53"/>

    </g>

   </g>

   <g id="text_17">

    <!-- 0.87 -->

    <g style="fill:#ffffff;" transform="translate(68.545313 274.686594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-56"/>

     <use x="159.033203" xlink:href="#DejaVuSans-55"/>

    </g>

   </g>

   <g id="text_18">

    <!-- -0.42 -->

    <g style="fill:#ffffff;" transform="translate(178.341406 274.686594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-52"/>

     <use x="195.117188" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

   <g id="text_19">

    <!-- 1 -->

    <g style="fill:#ffffff;" transform="translate(299.696875 274.686594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

   <g id="text_20">

    <!-- 0.96 -->

    <defs>

     <path d="M 10.984375 1.515625 

L 10.984375 10.5 

Q 14.703125 8.734375 18.5 7.8125 

Q 22.3125 6.890625 25.984375 6.890625 

Q 35.75 6.890625 40.890625 13.453125 

Q 46.046875 20.015625 46.78125 33.40625 

Q 43.953125 29.203125 39.59375 26.953125 

Q 35.25 24.703125 29.984375 24.703125 

Q 19.046875 24.703125 12.671875 31.3125 

Q 6.296875 37.9375 6.296875 49.421875 

Q 6.296875 60.640625 12.9375 67.421875 

Q 19.578125 74.21875 30.609375 74.21875 

Q 43.265625 74.21875 49.921875 64.515625 

Q 56.59375 54.828125 56.59375 36.375 

Q 56.59375 19.140625 48.40625 8.859375 

Q 40.234375 -1.421875 26.421875 -1.421875 

Q 22.703125 -1.421875 18.890625 -0.6875 

Q 15.09375 0.046875 10.984375 1.515625 

z

M 30.609375 32.421875 

Q 37.25 32.421875 41.125 36.953125 

Q 45.015625 41.5 45.015625 49.421875 

Q 45.015625 57.28125 41.125 61.84375 

Q 37.25 66.40625 30.609375 66.40625 

Q 23.96875 66.40625 20.09375 61.84375 

Q 16.21875 57.28125 16.21875 49.421875 

Q 16.21875 41.5 20.09375 36.953125 

Q 23.96875 32.421875 30.609375 32.421875 

z

" id="DejaVuSans-57"/>

     <path d="M 33.015625 40.375 

Q 26.375 40.375 22.484375 35.828125 

Q 18.609375 31.296875 18.609375 23.390625 

Q 18.609375 15.53125 22.484375 10.953125 

Q 26.375 6.390625 33.015625 6.390625 

Q 39.65625 6.390625 43.53125 10.953125 

Q 47.40625 15.53125 47.40625 23.390625 

Q 47.40625 31.296875 43.53125 35.828125 

Q 39.65625 40.375 33.015625 40.375 

z

M 52.59375 71.296875 

L 52.59375 62.3125 

Q 48.875 64.0625 45.09375 64.984375 

Q 41.3125 65.921875 37.59375 65.921875 

Q 27.828125 65.921875 22.671875 59.328125 

Q 17.53125 52.734375 16.796875 39.40625 

Q 19.671875 43.65625 24.015625 45.921875 

Q 28.375 48.1875 33.59375 48.1875 

Q 44.578125 48.1875 50.953125 41.515625 

Q 57.328125 34.859375 57.328125 23.390625 

Q 57.328125 12.15625 50.6875 5.359375 

Q 44.046875 -1.421875 33.015625 -1.421875 

Q 20.359375 -1.421875 13.671875 8.265625 

Q 6.984375 17.96875 6.984375 36.375 

Q 6.984375 53.65625 15.1875 63.9375 

Q 23.390625 74.21875 37.203125 74.21875 

Q 40.921875 74.21875 44.703125 73.484375 

Q 48.484375 72.75 52.59375 71.296875 

z

" id="DejaVuSans-54"/>

    </defs>

    <g style="fill:#ffffff;" transform="translate(403.345313 274.686594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-57"/>

     <use x="159.033203" xlink:href="#DejaVuSans-54"/>

    </g>

   </g>

   <g id="text_21">

    <!-- 0.82 -->

    <g style="fill:#ffffff;" transform="translate(68.545313 361.662594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-56"/>

     <use x="159.033203" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

   <g id="text_22">

    <!-- -0.35 -->

    <g style="fill:#ffffff;" transform="translate(178.341406 361.662594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-45"/>

     <use x="36.083984" xlink:href="#DejaVuSans-48"/>

     <use x="99.707031" xlink:href="#DejaVuSans-46"/>

     <use x="131.494141" xlink:href="#DejaVuSans-51"/>

     <use x="195.117188" xlink:href="#DejaVuSans-53"/>

    </g>

   </g>

   <g id="text_23">

    <!-- 0.96 -->

    <g style="fill:#ffffff;" transform="translate(291.745313 361.662594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-48"/>

     <use x="63.623047" xlink:href="#DejaVuSans-46"/>

     <use x="95.410156" xlink:href="#DejaVuSans-57"/>

     <use x="159.033203" xlink:href="#DejaVuSans-54"/>

    </g>

   </g>

   <g id="text_24">

    <!-- 1 -->

    <g style="fill:#ffffff;" transform="translate(411.296875 361.662594)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_3">

    <path clip-path="url(#p844105ff00)" d="M 498.178125 445.879219 

L 498.178125 444.180469 

L 498.178125 12.697969 

L 498.178125 10.999219 

L 519.922125 10.999219 

L 519.922125 12.697969 

L 519.922125 444.180469 

L 519.922125 445.879219 

z

" style="fill:#ffffff;stroke:#ffffff;stroke-linejoin:miter;stroke-width:0.01;"/>

   </g>

   <image height="435" id="image337d68e9f6" transform="scale(1 -1)translate(0 -435)" width="22" x="498" xlink:href="data:image/png;base64,

iVBORw0KGgoAAAANSUhEUgAAABYAAAGzCAYAAAArEufSAAAABHNCSVQICAgIfAhkiAAAAj5JREFUeJztnMtxw1AMA/Uc1ZLOU6alHCTRbmAPO7MoAIMBSDw6H6+/7ffcAOyvF0G7bRAtqDgrBqDixRD7PDaGl2Ka2GeFT/G+FtNCPitSPKgrBinmiX1W+I5CoxUpvkEqZuZtXz+2u2JBVvgUF94AVAx5jK104Q2UC8JwK61I8UOsC692+xDrwhNuntBjquh14b2E4dUVF4TjtlEXvdEKhhtUrPMY+wDps4LaPF+7CTfP2G5YeDYrCu9DDB3evhekV3rQUTgQPk2F90D4NFFdoaxN3eb5FoT6uVvhPSi8QeENCm9QeAOfYuGfYhfeF3HhXfC1m9IKn+IWBCYuvAEY3tKF51NceDdSPGjcBoU3wBQbrdDdFWv9MMTC8FJ8w7cgRitSPMS62iw8nNhnBaf41H1R0XkeDPEBEYNWbDbFlMdZMTBuni48yorGbYCttNKKN0LsGzfj5tVuD7Fx82yKO7EeGMdNp5hqN6MVJ/Ld1cIFMVqx6RRDHgtrUzhuQsV1xQVlVxTehRR/E1f0F1I84C56oRUp/hDXFRd8ioVWvBnBwvB8Hu+HLry3LjzKY+XmMcS+cdsP5pEWllDjNgDHTWgFQ+y7K5RWMMS+cdsPyAufFY3bgLzoG7cLwlf6LTwKdeMGlYXSCoa4cRs0boPGjSf2zbHvrlBaoVMs9JgiFlqR4oe4N++GryuEVvh+q3BS4VHEPivIf4LQKW7cbqSYJ/ZZ4VNstKLavOFTnBUDn+KsGPjazWhFim+kePAPFPVgEVR5gc8AAAAASUVORK5CYII=" y="-10"/>

   <g id="matplotlib.axis_3"/>

   <g id="matplotlib.axis_4">

    <g id="ytick_5">

     <g id="line2d_9">

      <defs>

       <path d="M 0 0 

L 3.5 0 

" id="m46868362f7" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="441.202987"/>

      </g>

     </g>

     <g id="text_25">

      <!-- −0.4 -->

      <defs>

       <path d="M 10.59375 35.5 

L 73.1875 35.5 

L 73.1875 27.203125 

L 10.59375 27.203125 

z

" id="DejaVuSans-8722"/>

      </defs>

      <g transform="translate(526.922125 445.002206)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-48"/>

       <use x="147.412109" xlink:href="#DejaVuSans-46"/>

       <use x="179.199219" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="379.745306"/>

      </g>

     </g>

     <g id="text_26">

      <!-- −0.2 -->

      <g transform="translate(526.922125 383.544525)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-48"/>

       <use x="147.412109" xlink:href="#DejaVuSans-46"/>

       <use x="179.199219" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="318.287625"/>

      </g>

     </g>

     <g id="text_27">

      <!-- 0.0 -->

      <g transform="translate(526.922125 322.086843)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="256.829943"/>

      </g>

     </g>

     <g id="text_28">

      <!-- 0.2 -->

      <g transform="translate(526.922125 260.629162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="195.372262"/>

      </g>

     </g>

     <g id="text_29">

      <!-- 0.4 -->

      <g transform="translate(526.922125 199.171481)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_10">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="133.914581"/>

      </g>

     </g>

     <g id="text_30">

      <!-- 0.6 -->

      <g transform="translate(526.922125 137.7138)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_11">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="72.4569"/>

      </g>

     </g>

     <g id="text_31">

      <!-- 0.8 -->

      <g transform="translate(526.922125 76.256119)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_12">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="519.922125" xlink:href="#m46868362f7" y="10.999219"/>

      </g>

     </g>

     <g id="text_32">

      <!-- 1.0 -->

      <g transform="translate(526.922125 14.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_4">

    <path d="M 498.178125 445.879219 

L 498.178125 444.180469 

L 498.178125 12.697969 

L 498.178125 10.999219 

L 519.922125 10.999219 

L 519.922125 12.697969 

L 519.922125 444.180469 

L 519.922125 445.879219 

z

" style="fill:none;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p194fb5f47f">

   <rect height="434.88" width="446.4" x="23.878125" y="10.999219"/>

  </clipPath>

  <clipPath id="p844105ff00">

   <rect height="434.88" width="21.744" x="498.178125" y="10.999219"/>

  </clipPath>

 </defs>

</svg>


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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Pandas">Pandas<a class="anchor-link" href="#Pandas">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">pandas.plotting</span> <span class="kn">import</span> <span class="n">scatter_matrix</span>
<span class="n">attributes</span> <span class="o">=</span> <span class="n">iris</span><span class="o">.</span><span class="n">columns</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">scatter_matrix</span><span class="p">(</span><span class="n">iris</span><span class="p">[</span><span class="n">attributes</span><span class="p">],</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">8</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC224F70&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC3FE130&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC435520&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC4672B0&gt;],
       [&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC491A30&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC4C6130&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADC4C6220&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD4BDA00&gt;],
       [&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD51C8B0&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD5470D0&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD57E820&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD5A7FA0&gt;],
       [&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD5DC760&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD606EE0&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD63B6A0&gt;,
        &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001DADD664E20&gt;]],
      dtype=object)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="475.048125pt" version="1.1" viewBox="0 0 709.768125 475.048125" width="709.768125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 475.048125 

L 709.768125 475.048125 

L 709.768125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 32.968125 115.92 

L 200.368125 115.92 

L 200.368125 7.2 

L 32.968125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="patch_3">

    <path clip-path="url(#p1e3eba2890)" d="M 36.953839 115.92 

L 52.896696 115.92 

L 52.896696 81.405714 

L 36.953839 81.405714 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_4">

    <path clip-path="url(#p1e3eba2890)" d="M 52.896696 115.92 

L 68.839554 115.92 

L 68.839554 27.716825 

L 52.896696 27.716825 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_5">

    <path clip-path="url(#p1e3eba2890)" d="M 68.839554 115.92 

L 84.782411 115.92 

L 84.782411 66.066032 

L 68.839554 66.066032 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_6">

    <path clip-path="url(#p1e3eba2890)" d="M 84.782411 115.92 

L 100.725268 115.92 

L 100.725268 12.377143 

L 84.782411 12.377143 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_7">

    <path clip-path="url(#p1e3eba2890)" d="M 100.725268 115.92 

L 116.668125 115.92 

L 116.668125 54.56127 

L 100.725268 54.56127 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_8">

    <path clip-path="url(#p1e3eba2890)" d="M 116.668125 115.92 

L 132.610982 115.92 

L 132.610982 16.212063 

L 116.668125 16.212063 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_9">

    <path clip-path="url(#p1e3eba2890)" d="M 132.610982 115.92 

L 148.553839 115.92 

L 148.553839 46.891429 

L 132.610982 46.891429 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_10">

    <path clip-path="url(#p1e3eba2890)" d="M 148.553839 115.92 

L 164.496696 115.92 

L 164.496696 92.910476 

L 148.553839 92.910476 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_11">

    <path clip-path="url(#p1e3eba2890)" d="M 164.496696 115.92 

L 180.439554 115.92 

L 180.439554 96.745397 

L 164.496696 96.745397 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_12">

    <path clip-path="url(#p1e3eba2890)" d="M 180.439554 115.92 

L 196.382411 115.92 

L 196.382411 92.910476 

L 180.439554 92.910476 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="ytick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m60453630f8" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="93.198095"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 5 -->

      <defs>

       <path d="M 10.796875 72.90625 

L 49.515625 72.90625 

L 49.515625 64.59375 

L 19.828125 64.59375 

L 19.828125 46.734375 

Q 21.96875 47.46875 24.109375 47.828125 

Q 26.265625 48.1875 28.421875 48.1875 

Q 40.625 48.1875 47.75 41.5 

Q 54.890625 34.8125 54.890625 23.390625 

Q 54.890625 11.625 47.5625 5.09375 

Q 40.234375 -1.421875 26.90625 -1.421875 

Q 22.3125 -1.421875 17.546875 -0.640625 

Q 12.796875 0.140625 7.71875 1.703125 

L 7.71875 11.625 

Q 12.109375 9.234375 16.796875 8.0625 

Q 21.484375 6.890625 26.703125 6.890625 

Q 35.15625 6.890625 40.078125 11.328125 

Q 45.015625 15.765625 45.015625 23.390625 

Q 45.015625 31 40.078125 35.4375 

Q 35.15625 39.890625 26.703125 39.890625 

Q 22.75 39.890625 18.8125 39.015625 

Q 14.890625 38.140625 10.796875 36.28125 

z

" id="DejaVuSans-53"/>

      </defs>

      <g transform="translate(20.878125 96.23747)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="64.43619"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 6 -->

      <defs>

       <path d="M 33.015625 40.375 

Q 26.375 40.375 22.484375 35.828125 

Q 18.609375 31.296875 18.609375 23.390625 

Q 18.609375 15.53125 22.484375 10.953125 

Q 26.375 6.390625 33.015625 6.390625 

Q 39.65625 6.390625 43.53125 10.953125 

Q 47.40625 15.53125 47.40625 23.390625 

Q 47.40625 31.296875 43.53125 35.828125 

Q 39.65625 40.375 33.015625 40.375 

z

M 52.59375 71.296875 

L 52.59375 62.3125 

Q 48.875 64.0625 45.09375 64.984375 

Q 41.3125 65.921875 37.59375 65.921875 

Q 27.828125 65.921875 22.671875 59.328125 

Q 17.53125 52.734375 16.796875 39.40625 

Q 19.671875 43.65625 24.015625 45.921875 

Q 28.375 48.1875 33.59375 48.1875 

Q 44.578125 48.1875 50.953125 41.515625 

Q 57.328125 34.859375 57.328125 23.390625 

Q 57.328125 12.15625 50.6875 5.359375 

Q 44.046875 -1.421875 33.015625 -1.421875 

Q 20.359375 -1.421875 13.671875 8.265625 

Q 6.984375 17.96875 6.984375 36.375 

Q 6.984375 53.65625 15.1875 63.9375 

Q 23.390625 74.21875 37.203125 74.21875 

Q 40.921875 74.21875 44.703125 73.484375 

Q 48.484375 72.75 52.59375 71.296875 

z

" id="DejaVuSans-54"/>

      </defs>

      <g transform="translate(20.878125 67.475565)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="35.674286"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 7 -->

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

      </defs>

      <g transform="translate(20.878125 38.713661)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-55"/>

      </g>

     </g>

    </g>

    <g id="text_4">

     <!-- SepalLengthCm -->

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

     </defs>

     <g transform="translate(14.798438 101.046719)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-83"/>

      <use x="63.476562" xlink:href="#DejaVuSans-101"/>

      <use x="125" xlink:href="#DejaVuSans-112"/>

      <use x="188.476562" xlink:href="#DejaVuSans-97"/>

      <use x="249.755859" xlink:href="#DejaVuSans-108"/>

      <use x="277.539062" xlink:href="#DejaVuSans-76"/>

      <use x="331.501953" xlink:href="#DejaVuSans-101"/>

      <use x="393.025391" xlink:href="#DejaVuSans-110"/>

      <use x="456.404297" xlink:href="#DejaVuSans-103"/>

      <use x="519.880859" xlink:href="#DejaVuSans-116"/>

      <use x="559.089844" xlink:href="#DejaVuSans-104"/>

      <use x="622.46875" xlink:href="#DejaVuSans-67"/>

      <use x="692.292969" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_13">

    <path d="M 32.968125 115.92 

L 32.968125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_14">

    <path d="M 200.368125 115.92 

L 200.368125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_15">

    <path d="M 32.968125 115.92 

L 200.368125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_16">

    <path d="M 32.968125 7.2 

L 200.368125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_17">

    <path d="M 200.368125 115.92 

L 367.768125 115.92 

L 367.768125 7.2 

L 200.368125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_1">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C0_0_b52962a722"/>

    </defs>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="101.826667"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="104.702857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="104.702857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="110.455238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="98.950476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="98.950476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="113.331429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="337.210982" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="363.782411" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C0_0_b52962a722" y="104.702857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="98.950476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C0_0_b52962a722" y="87.445714"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="87.445714"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="101.826667"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="98.950476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="343.853839" xlink:href="#C0_0_b52962a722" y="87.445714"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="350.496696" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="110.455238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C0_0_b52962a722" y="107.579048"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="110.455238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="98.950476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="104.702857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C0_0_b52962a722" y="84.569524"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="35.674286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="38.550476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="50.055238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="47.179048"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="87.445714"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="204.353839" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="67.312381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C0_0_b52962a722" y="58.68381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="67.312381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="47.179048"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="41.426667"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="81.693333"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C0_0_b52962a722" y="78.817143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C0_0_b52962a722" y="93.198095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="58.68381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="90.321905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="32.798095"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="50.055238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="18.417143"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="96.074286"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C0_0_b52962a722" y="27.045714"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C0_0_b52962a722" y="29.921905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="50.055238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="41.426667"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="73.064762"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="50.055238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="15.540952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C0_0_b52962a722" y="15.540952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="38.550476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="75.940952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="15.540952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="29.921905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="58.68381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="29.921905"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="24.169524"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C0_0_b52962a722" y="9.788571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C0_0_b52962a722" y="61.56"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="15.540952"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="52.931429"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="64.43619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="38.550476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C0_0_b52962a722" y="38.550476"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C0_0_b52962a722" y="70.188571"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C0_0_b52962a722" y="41.426667"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="44.302857"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C0_0_b52962a722" y="55.807619"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="50.055238"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C0_0_b52962a722" y="58.68381"/>

    </g>

    <g clip-path="url(#p9c3456b21f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C0_0_b52962a722" y="67.312381"/>

    </g>

   </g>

   <g id="patch_18">

    <path d="M 200.368125 115.92 

L 200.368125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_19">

    <path d="M 367.768125 115.92 

L 367.768125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_20">

    <path d="M 200.368125 115.92 

L 367.768125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_21">

    <path d="M 200.368125 7.2 

L 367.768125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_3">

   <g id="patch_22">

    <path d="M 367.768125 115.92 

L 535.168125 115.92 

L 535.168125 7.2 

L 367.768125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_2">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C1_0_ca8c8ac221"/>

    </defs>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="101.826667"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="104.702857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="104.702857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="110.455238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="98.950476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="98.950476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="374.456018" xlink:href="#C1_0_ca8c8ac221" y="113.331429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="371.753839" xlink:href="#C1_0_ca8c8ac221" y="104.702857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#C1_0_ca8c8ac221" y="98.950476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="87.445714"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="87.445714"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="101.826667"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="98.950476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="87.445714"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="110.455238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="107.579048"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C1_0_ca8c8ac221" y="110.455238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="98.950476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="104.702857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C1_0_ca8c8ac221" y="84.569524"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C1_0_ca8c8ac221" y="35.674286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C1_0_ca8c8ac221" y="38.550476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C1_0_ca8c8ac221" y="50.055238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C1_0_ca8c8ac221" y="47.179048"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C1_0_ca8c8ac221" y="87.445714"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C1_0_ca8c8ac221" y="67.312381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="442.010498" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="58.68381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C1_0_ca8c8ac221" y="67.312381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C1_0_ca8c8ac221" y="47.179048"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C1_0_ca8c8ac221" y="41.426667"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="447.414856" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="444.712677" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="81.693333"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C1_0_ca8c8ac221" y="78.817143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#C1_0_ca8c8ac221" y="93.198095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#C1_0_ca8c8ac221" y="58.68381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="425.797423" xlink:href="#C1_0_ca8c8ac221" y="90.321905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#C1_0_ca8c8ac221" y="32.798095"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C1_0_ca8c8ac221" y="50.055238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="523.075873" xlink:href="#C1_0_ca8c8ac221" y="18.417143"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C1_0_ca8c8ac221" y="96.074286"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="514.969336" xlink:href="#C1_0_ca8c8ac221" y="27.045714"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C1_0_ca8c8ac221" y="29.921905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="50.055238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C1_0_ca8c8ac221" y="41.426667"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C1_0_ca8c8ac221" y="73.064762"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C1_0_ca8c8ac221" y="50.055238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#C1_0_ca8c8ac221" y="15.540952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="531.182411" xlink:href="#C1_0_ca8c8ac221" y="15.540952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C1_0_ca8c8ac221" y="38.550476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C1_0_ca8c8ac221" y="75.940952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#C1_0_ca8c8ac221" y="15.540952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#C1_0_ca8c8ac221" y="29.921905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C1_0_ca8c8ac221" y="58.68381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C1_0_ca8c8ac221" y="29.921905"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C1_0_ca8c8ac221" y="24.169524"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="517.671515" xlink:href="#C1_0_ca8c8ac221" y="9.788571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="61.56"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C1_0_ca8c8ac221" y="15.540952"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C1_0_ca8c8ac221" y="52.931429"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C1_0_ca8c8ac221" y="64.43619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#C1_0_ca8c8ac221" y="38.550476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="38.550476"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="70.188571"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#C1_0_ca8c8ac221" y="41.426667"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#C1_0_ca8c8ac221" y="44.302857"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C1_0_ca8c8ac221" y="55.807619"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#C1_0_ca8c8ac221" y="50.055238"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#C1_0_ca8c8ac221" y="58.68381"/>

    </g>

    <g clip-path="url(#p181218a914)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C1_0_ca8c8ac221" y="67.312381"/>

    </g>

   </g>

   <g id="patch_23">

    <path d="M 367.768125 115.92 

L 367.768125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_24">

    <path d="M 535.168125 115.92 

L 535.168125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_25">

    <path d="M 367.768125 115.92 

L 535.168125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_26">

    <path d="M 367.768125 7.2 

L 535.168125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_4">

   <g id="patch_27">

    <path d="M 535.168125 115.92 

L 702.568125 115.92 

L 702.568125 7.2 

L 535.168125 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_3">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C2_0_195ae34c1f"/>

    </defs>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="101.826667"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="104.702857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="104.702857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="110.455238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="98.950476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="98.950476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="113.331429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="104.702857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="565.725268" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="98.950476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="87.445714"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="87.445714"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="101.826667"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="98.950476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="87.445714"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="110.455238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="107.579048"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="110.455238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="572.368125" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C2_0_195ae34c1f" y="98.950476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="104.702857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="84.569524"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="35.674286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="38.550476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="50.055238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="47.179048"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="87.445714"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="67.312381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="58.68381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="67.312381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="47.179048"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="41.426667"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="81.693333"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C2_0_195ae34c1f" y="78.817143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C2_0_195ae34c1f" y="93.198095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="58.68381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C2_0_195ae34c1f" y="90.321905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="32.798095"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C2_0_195ae34c1f" y="50.055238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="18.417143"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C2_0_195ae34c1f" y="96.074286"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="27.045714"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C2_0_195ae34c1f" y="29.921905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="50.055238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="41.426667"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="73.064762"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="50.055238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C2_0_195ae34c1f" y="15.540952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="15.540952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="38.550476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="75.940952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="15.540952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="29.921905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="58.68381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C2_0_195ae34c1f" y="29.921905"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C2_0_195ae34c1f" y="24.169524"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="9.788571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C2_0_195ae34c1f" y="61.56"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="15.540952"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="52.931429"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="64.43619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C2_0_195ae34c1f" y="38.550476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="38.550476"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C2_0_195ae34c1f" y="70.188571"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="41.426667"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="44.302857"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C2_0_195ae34c1f" y="55.807619"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C2_0_195ae34c1f" y="50.055238"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C2_0_195ae34c1f" y="58.68381"/>

    </g>

    <g clip-path="url(#p630b29a36a)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C2_0_195ae34c1f" y="67.312381"/>

    </g>

   </g>

   <g id="patch_28">

    <path d="M 535.168125 115.92 

L 535.168125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_29">

    <path d="M 702.568125 115.92 

L 702.568125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_30">

    <path d="M 535.168125 115.92 

L 702.568125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_31">

    <path d="M 535.168125 7.2 

L 702.568125 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_5">

   <g id="patch_32">

    <path d="M 32.968125 224.64 

L 200.368125 224.64 

L 200.368125 115.92 

L 32.968125 115.92 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_4">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C3_0_ce3c583915"/>

    </defs>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="153.022857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="140.08"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="148.708571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="36.953839" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="135.765714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="118.508571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="140.08"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="157.337143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="148.708571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C3_0_ce3c583915" y="153.022857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C3_0_ce3c583915" y="157.337143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C3_0_ce3c583915" y="131.451429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="127.137143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="157.337143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="157.337143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="45.810982" xlink:href="#C3_0_ce3c583915" y="209.108571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="157.337143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="81.239554" xlink:href="#C3_0_ce3c583915" y="148.708571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="156.525268" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="209.108571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="204.794286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="222.051429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="213.422857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C3_0_ce3c583915" y="213.422857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="196.165714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="204.794286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="204.794286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="209.108571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C3_0_ce3c583915" y="196.165714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="196.165714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C3_0_ce3c583915" y="209.108571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="160.953839" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="183.096696" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="169.810982" xlink:href="#C3_0_ce3c583915" y="183.222857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C3_0_ce3c583915" y="153.022857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C3_0_ce3c583915" y="196.165714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="213.422857"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="174.239554" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="196.382411" xlink:href="#C3_0_ce3c583915" y="144.394286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="187.537143"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C3_0_ce3c583915" y="196.165714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C3_0_ce3c583915" y="174.594286"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C3_0_ce3c583915" y="191.851429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C3_0_ce3c583915" y="170.28"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="165.965714"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C3_0_ce3c583915" y="200.48"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C3_0_ce3c583915" y="161.651429"/>

    </g>

    <g clip-path="url(#pf147c76d04)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C3_0_ce3c583915" y="178.908571"/>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="222.051429"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 2 -->

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

      </defs>

      <g transform="translate(20.878125 225.090804)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="178.908571"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 3 -->

      <defs>

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

      <g transform="translate(20.878125 181.947946)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="135.765714"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 4 -->

      <defs>

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

      </defs>

      <g transform="translate(20.878125 138.805089)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="text_8">

     <!-- SepalWidthCm -->

     <defs>

      <path d="M 3.328125 72.90625 

L 13.28125 72.90625 

L 28.609375 11.28125 

L 43.890625 72.90625 

L 54.984375 72.90625 

L 70.3125 11.28125 

L 85.59375 72.90625 

L 95.609375 72.90625 

L 77.296875 0 

L 64.890625 0 

L 49.515625 63.28125 

L 33.984375 0 

L 21.578125 0 

z

" id="DejaVuSans-87"/>

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

     <g transform="translate(14.798438 207.043281)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-83"/>

      <use x="63.476562" xlink:href="#DejaVuSans-101"/>

      <use x="125" xlink:href="#DejaVuSans-112"/>

      <use x="188.476562" xlink:href="#DejaVuSans-97"/>

      <use x="249.755859" xlink:href="#DejaVuSans-108"/>

      <use x="277.539062" xlink:href="#DejaVuSans-87"/>

      <use x="374.166016" xlink:href="#DejaVuSans-105"/>

      <use x="401.949219" xlink:href="#DejaVuSans-100"/>

      <use x="465.425781" xlink:href="#DejaVuSans-116"/>

      <use x="504.634766" xlink:href="#DejaVuSans-104"/>

      <use x="568.013672" xlink:href="#DejaVuSans-67"/>

      <use x="637.837891" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_33">

    <path d="M 32.968125 224.64 

L 32.968125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_34">

    <path d="M 200.368125 224.64 

L 200.368125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_35">

    <path d="M 32.968125 224.64 

L 200.368125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_36">

    <path d="M 32.968125 115.92 

L 200.368125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_6">

   <g id="patch_37">

    <path d="M 200.368125 224.64 

L 367.768125 224.64 

L 367.768125 115.92 

L 200.368125 115.92 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="patch_38">

    <path clip-path="url(#p5ac31d3c11)" d="M 204.353839 224.64 

L 220.296696 224.64 

L 220.296696 213.740752 

L 204.353839 213.740752 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_39">

    <path clip-path="url(#p5ac31d3c11)" d="M 220.296696 224.64 

L 236.239554 224.64 

L 236.239554 205.566316 

L 220.296696 205.566316 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_40">

    <path clip-path="url(#p5ac31d3c11)" d="M 236.239554 224.64 

L 252.182411 224.64 

L 252.182411 164.694135 

L 236.239554 164.694135 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_41">

    <path clip-path="url(#p5ac31d3c11)" d="M 252.182411 224.64 

L 268.125268 224.64 

L 268.125268 159.244511 

L 252.182411 159.244511 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_42">

    <path clip-path="url(#p5ac31d3c11)" d="M 268.125268 224.64 

L 284.068125 224.64 

L 284.068125 121.097143 

L 268.125268 121.097143 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_43">

    <path clip-path="url(#p5ac31d3c11)" d="M 284.068125 224.64 

L 300.010982 224.64 

L 300.010982 140.170827 

L 284.068125 140.170827 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_44">

    <path clip-path="url(#p5ac31d3c11)" d="M 300.010982 224.64 

L 315.953839 224.64 

L 315.953839 202.841504 

L 300.010982 202.841504 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_45">

    <path clip-path="url(#p5ac31d3c11)" d="M 315.953839 224.64 

L 331.896696 224.64 

L 331.896696 194.667068 

L 315.953839 194.667068 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_46">

    <path clip-path="url(#p5ac31d3c11)" d="M 331.896696 224.64 

L 347.839554 224.64 

L 347.839554 219.190376 

L 331.896696 219.190376 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_47">

    <path clip-path="url(#p5ac31d3c11)" d="M 347.839554 224.64 

L 363.782411 224.64 

L 363.782411 219.190376 

L 347.839554 219.190376 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_48">

    <path d="M 200.368125 224.64 

L 200.368125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_49">

    <path d="M 367.768125 224.64 

L 367.768125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_50">

    <path d="M 200.368125 224.64 

L 367.768125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_51">

    <path d="M 200.368125 115.92 

L 367.768125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_7">

   <g id="patch_52">

    <path d="M 367.768125 224.64 

L 535.168125 224.64 

L 535.168125 115.92 

L 367.768125 115.92 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_5">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C4_0_10857472f7"/>

    </defs>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="153.022857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C4_0_10857472f7" y="140.08"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="148.708571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="374.456018" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#C4_0_10857472f7" y="135.765714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="118.508571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="140.08"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="157.337143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="148.708571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="371.753839" xlink:href="#C4_0_10857472f7" y="153.022857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="157.337143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="131.451429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="127.137143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="157.337143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="157.337143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="209.108571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="157.337143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#C4_0_10857472f7" y="148.708571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C4_0_10857472f7" y="209.108571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#C4_0_10857472f7" y="204.794286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#C4_0_10857472f7" y="222.051429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C4_0_10857472f7" y="213.422857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="442.010498" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="213.422857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#C4_0_10857472f7" y="196.165714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="447.414856" xlink:href="#C4_0_10857472f7" y="204.794286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="444.712677" xlink:href="#C4_0_10857472f7" y="204.794286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C4_0_10857472f7" y="209.108571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#C4_0_10857472f7" y="196.165714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#C4_0_10857472f7" y="196.165714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#C4_0_10857472f7" y="209.108571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="425.797423" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="523.075873" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="514.969336" xlink:href="#C4_0_10857472f7" y="183.222857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C4_0_10857472f7" y="153.022857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="531.182411" xlink:href="#C4_0_10857472f7" y="196.165714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C4_0_10857472f7" y="213.422857"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="517.671515" xlink:href="#C4_0_10857472f7" y="144.394286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="187.537143"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="196.165714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="174.594286"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="191.851429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#C4_0_10857472f7" y="170.28"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#C4_0_10857472f7" y="165.965714"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#C4_0_10857472f7" y="200.48"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#C4_0_10857472f7" y="161.651429"/>

    </g>

    <g clip-path="url(#p8690fc581c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#C4_0_10857472f7" y="178.908571"/>

    </g>

   </g>

   <g id="patch_53">

    <path d="M 367.768125 224.64 

L 367.768125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_54">

    <path d="M 535.168125 224.64 

L 535.168125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_55">

    <path d="M 367.768125 224.64 

L 535.168125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_56">

    <path d="M 367.768125 115.92 

L 535.168125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_8">

   <g id="patch_57">

    <path d="M 535.168125 224.64 

L 702.568125 224.64 

L 702.568125 115.92 

L 535.168125 115.92 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_6">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C5_0_857496cf08"/>

    </defs>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="153.022857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="140.08"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="148.708571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="135.765714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="118.508571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="140.08"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="157.337143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="148.708571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="153.022857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="565.725268" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="157.337143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="131.451429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="127.137143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="157.337143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="157.337143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="209.108571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="572.368125" xlink:href="#C5_0_857496cf08" y="157.337143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="148.708571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="209.108571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="204.794286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="222.051429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="213.422857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="213.422857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="196.165714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C5_0_857496cf08" y="204.794286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="204.794286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="209.108571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C5_0_857496cf08" y="196.165714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C5_0_857496cf08" y="196.165714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C5_0_857496cf08" y="209.108571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="183.222857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C5_0_857496cf08" y="153.022857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="196.165714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="213.422857"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="144.394286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C5_0_857496cf08" y="187.537143"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C5_0_857496cf08" y="196.165714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="174.594286"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C5_0_857496cf08" y="191.851429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="170.28"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C5_0_857496cf08" y="165.965714"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C5_0_857496cf08" y="200.48"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C5_0_857496cf08" y="161.651429"/>

    </g>

    <g clip-path="url(#pba906d30d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C5_0_857496cf08" y="178.908571"/>

    </g>

   </g>

   <g id="patch_58">

    <path d="M 535.168125 224.64 

L 535.168125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_59">

    <path d="M 702.568125 224.64 

L 702.568125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_60">

    <path d="M 535.168125 224.64 

L 702.568125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_61">

    <path d="M 535.168125 115.92 

L 702.568125 115.92 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_9">

   <g id="patch_62">

    <path d="M 32.968125 333.36 

L 200.368125 333.36 

L 200.368125 224.64 

L 32.968125 224.64 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_7">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C6_0_95ed624480"/>

    </defs>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="318.486683"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="36.953839" xlink:href="#C6_0_95ed624480" y="329.016465"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="327.261501"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="318.486683"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="318.486683"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C6_0_95ed624480" y="330.771429"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="318.486683"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C6_0_95ed624480" y="314.976755"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="327.261501"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="45.810982" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C6_0_95ed624480" y="325.506538"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="314.976755"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="320.241646"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="81.239554" xlink:href="#C6_0_95ed624480" y="321.99661"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="323.751574"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="156.525268" xlink:href="#C6_0_95ed624480" y="265.837772"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C6_0_95ed624480" y="262.327845"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="278.122518"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C6_0_95ed624480" y="267.592736"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="265.837772"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="290.407264"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C6_0_95ed624480" y="267.592736"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C6_0_95ed624480" y="279.877482"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="286.897337"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C6_0_95ed624480" y="274.612591"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="278.122518"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="265.837772"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="285.142373"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="271.102663"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="276.367554"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="279.877482"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C6_0_95ed624480" y="264.082809"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="278.122518"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="262.327845"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="265.837772"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="272.857627"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C6_0_95ed624480" y="271.102663"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C6_0_95ed624480" y="264.082809"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="260.572881"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="286.897337"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="281.632446"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="283.387409"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="279.877482"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="265.837772"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="271.102663"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="276.367554"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="278.122518"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C6_0_95ed624480" y="271.102663"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="267.592736"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="278.122518"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C6_0_95ed624480" y="290.407264"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="274.612591"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="274.612591"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="274.612591"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C6_0_95ed624480" y="272.857627"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C6_0_95ed624480" y="295.672155"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="276.367554"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="243.023245"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="160.953839" xlink:href="#C6_0_95ed624480" y="244.778208"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C6_0_95ed624480" y="246.533172"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="183.096696" xlink:href="#C6_0_95ed624480" y="232.493462"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C6_0_95ed624480" y="269.3477"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="169.810982" xlink:href="#C6_0_95ed624480" y="237.758354"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="246.533172"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C6_0_95ed624480" y="241.268281"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="255.30799"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C6_0_95ed624480" y="251.798063"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C6_0_95ed624480" y="260.572881"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="255.30799"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C6_0_95ed624480" y="251.798063"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C6_0_95ed624480" y="230.738499"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C6_0_95ed624480" y="227.228571"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="260.572881"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C6_0_95ed624480" y="248.288136"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C6_0_95ed624480" y="262.327845"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C6_0_95ed624480" y="230.738499"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="262.327845"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="248.288136"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C6_0_95ed624480" y="243.023245"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C6_0_95ed624480" y="264.082809"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="262.327845"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C6_0_95ed624480" y="246.533172"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="174.239554" xlink:href="#C6_0_95ed624480" y="241.268281"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="196.382411" xlink:href="#C6_0_95ed624480" y="236.00339"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C6_0_95ed624480" y="241.268281"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C6_0_95ed624480" y="251.798063"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C6_0_95ed624480" y="264.082809"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C6_0_95ed624480" y="253.553027"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="250.043099"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C6_0_95ed624480" y="244.778208"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="248.288136"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C6_0_95ed624480" y="257.062954"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C6_0_95ed624480" y="260.572881"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C6_0_95ed624480" y="257.062954"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C6_0_95ed624480" y="253.553027"/>

    </g>

    <g clip-path="url(#p5bd16baee8)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C6_0_95ed624480" y="258.817918"/>

    </g>

   </g>

   <g id="matplotlib.axis_3">

    <g id="ytick_7">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="313.221792"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 2 -->

      <g transform="translate(20.878125 316.261167)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="278.122518"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 4 -->

      <g transform="translate(20.878125 281.161893)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="243.023245"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 6 -->

      <g transform="translate(20.878125 246.06262)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="text_12">

     <!-- PetalLengthCm -->

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

     </defs>

     <g transform="translate(14.798438 316.932031)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-80"/>

      <use x="56.677734" xlink:href="#DejaVuSans-101"/>

      <use x="118.201172" xlink:href="#DejaVuSans-116"/>

      <use x="157.410156" xlink:href="#DejaVuSans-97"/>

      <use x="218.689453" xlink:href="#DejaVuSans-108"/>

      <use x="246.472656" xlink:href="#DejaVuSans-76"/>

      <use x="300.435547" xlink:href="#DejaVuSans-101"/>

      <use x="361.958984" xlink:href="#DejaVuSans-110"/>

      <use x="425.337891" xlink:href="#DejaVuSans-103"/>

      <use x="488.814453" xlink:href="#DejaVuSans-116"/>

      <use x="528.023438" xlink:href="#DejaVuSans-104"/>

      <use x="591.402344" xlink:href="#DejaVuSans-67"/>

      <use x="661.226562" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_63">

    <path d="M 32.968125 333.36 

L 32.968125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_64">

    <path d="M 200.368125 333.36 

L 200.368125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_65">

    <path d="M 32.968125 333.36 

L 200.368125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_66">

    <path d="M 32.968125 224.64 

L 200.368125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_10">

   <g id="patch_67">

    <path d="M 200.368125 333.36 

L 367.768125 333.36 

L 367.768125 224.64 

L 200.368125 224.64 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_8">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C7_0_b235c3c1c7"/>

    </defs>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#C7_0_b235c3c1c7" y="318.486683"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="329.016465"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="337.210982" xlink:href="#C7_0_b235c3c1c7" y="327.261501"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="363.782411" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="318.486683"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="318.486683"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C7_0_b235c3c1c7" y="330.771429"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="318.486683"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="314.976755"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="343.853839" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="350.496696" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="327.261501"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="325.506538"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="314.976755"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="320.241646"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#C7_0_b235c3c1c7" y="321.99661"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="323.751574"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="265.837772"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="262.327845"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C7_0_b235c3c1c7" y="278.122518"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="267.592736"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="265.837772"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C7_0_b235c3c1c7" y="290.407264"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="267.592736"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="279.877482"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="204.353839" xlink:href="#C7_0_b235c3c1c7" y="286.897337"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="274.612591"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C7_0_b235c3c1c7" y="278.122518"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="265.837772"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="285.142373"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="271.102663"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="276.367554"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="279.877482"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="264.082809"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="278.122518"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="262.327845"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="265.837772"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="272.857627"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="271.102663"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="264.082809"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="260.572881"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C7_0_b235c3c1c7" y="286.897337"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C7_0_b235c3c1c7" y="281.632446"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#C7_0_b235c3c1c7" y="283.387409"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="279.877482"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="265.837772"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C7_0_b235c3c1c7" y="271.102663"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="276.367554"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="278.122518"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C7_0_b235c3c1c7" y="271.102663"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="267.592736"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C7_0_b235c3c1c7" y="278.122518"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#C7_0_b235c3c1c7" y="290.407264"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="274.612591"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="274.612591"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="274.612591"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="272.857627"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="295.672155"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="276.367554"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="243.023245"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="244.778208"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="246.533172"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="232.493462"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="269.3477"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#C7_0_b235c3c1c7" y="237.758354"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="246.533172"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#C7_0_b235c3c1c7" y="241.268281"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="255.30799"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="251.798063"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="260.572881"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="255.30799"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="251.798063"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="230.738499"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C7_0_b235c3c1c7" y="227.228571"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#C7_0_b235c3c1c7" y="260.572881"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="248.288136"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="262.327845"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="230.738499"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="262.327845"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="248.288136"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="243.023245"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="264.082809"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="262.327845"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="246.533172"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="241.268281"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#C7_0_b235c3c1c7" y="236.00339"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="241.268281"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="251.798063"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="264.082809"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="253.553027"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="250.043099"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#C7_0_b235c3c1c7" y="244.778208"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#C7_0_b235c3c1c7" y="248.288136"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="257.062954"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#C7_0_b235c3c1c7" y="260.572881"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="257.062954"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#C7_0_b235c3c1c7" y="253.553027"/>

    </g>

    <g clip-path="url(#pd9b1e8b8d6)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#C7_0_b235c3c1c7" y="258.817918"/>

    </g>

   </g>

   <g id="patch_68">

    <path d="M 200.368125 333.36 

L 200.368125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_69">

    <path d="M 367.768125 333.36 

L 367.768125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_70">

    <path d="M 200.368125 333.36 

L 367.768125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_71">

    <path d="M 200.368125 224.64 

L 367.768125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_11">

   <g id="patch_72">

    <path d="M 367.768125 333.36 

L 535.168125 333.36 

L 535.168125 224.64 

L 367.768125 224.64 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="patch_73">

    <path clip-path="url(#p483e01def2)" d="M 371.753839 333.36 

L 387.696696 333.36 

L 387.696696 229.817143 

L 371.753839 229.817143 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_74">

    <path clip-path="url(#p483e01def2)" d="M 387.696696 333.36 

L 403.639554 333.36 

L 403.639554 295.969524 

L 387.696696 295.969524 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_75">

    <path clip-path="url(#p483e01def2)" d="M 403.639554 333.36 

L 419.582411 333.36 

L 419.582411 333.36 

L 403.639554 333.36 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_76">

    <path clip-path="url(#p483e01def2)" d="M 419.582411 333.36 

L 435.525268 333.36 

L 435.525268 324.731429 

L 419.582411 324.731429 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_77">

    <path clip-path="url(#p483e01def2)" d="M 435.525268 333.36 

L 451.468125 333.36 

L 451.468125 310.350476 

L 435.525268 310.350476 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_78">

    <path clip-path="url(#p483e01def2)" d="M 451.468125 333.36 

L 467.410982 333.36 

L 467.410982 258.579048 

L 451.468125 258.579048 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_79">

    <path clip-path="url(#p483e01def2)" d="M 467.410982 333.36 

L 483.353839 333.36 

L 483.353839 249.950476 

L 467.410982 249.950476 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_80">

    <path clip-path="url(#p483e01def2)" d="M 483.353839 333.36 

L 499.296696 333.36 

L 499.296696 281.588571 

L 483.353839 281.588571 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_81">

    <path clip-path="url(#p483e01def2)" d="M 499.296696 333.36 

L 515.239554 333.36 

L 515.239554 301.721905 

L 499.296696 301.721905 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_82">

    <path clip-path="url(#p483e01def2)" d="M 515.239554 333.36 

L 531.182411 333.36 

L 531.182411 318.979048 

L 515.239554 318.979048 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_83">

    <path d="M 367.768125 333.36 

L 367.768125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_84">

    <path d="M 535.168125 333.36 

L 535.168125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_85">

    <path d="M 367.768125 333.36 

L 535.168125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_86">

    <path d="M 367.768125 224.64 

L 535.168125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_12">

   <g id="patch_87">

    <path d="M 535.168125 333.36 

L 702.568125 333.36 

L 702.568125 224.64 

L 535.168125 224.64 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_9">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C8_0_7b1106a78f"/>

    </defs>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="318.486683"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="329.016465"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="327.261501"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="318.486683"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="318.486683"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="330.771429"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="565.725268" xlink:href="#C8_0_7b1106a78f" y="318.486683"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="314.976755"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="327.261501"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="539.153839" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="325.506538"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="572.368125" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="559.082411" xlink:href="#C8_0_7b1106a78f" y="314.976755"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="552.439554" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="320.241646"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="321.99661"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="545.796696" xlink:href="#C8_0_7b1106a78f" y="323.751574"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="265.837772"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="262.327845"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="278.122518"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="267.592736"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C8_0_7b1106a78f" y="265.837772"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="290.407264"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="267.592736"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="279.877482"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="286.897337"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="274.612591"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="278.122518"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="265.837772"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="285.142373"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="271.102663"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="276.367554"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C8_0_7b1106a78f" y="279.877482"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="264.082809"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="278.122518"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="262.327845"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C8_0_7b1106a78f" y="265.837772"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="272.857627"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="271.102663"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="264.082809"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C8_0_7b1106a78f" y="260.572881"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="286.897337"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C8_0_7b1106a78f" y="281.632446"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="283.387409"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C8_0_7b1106a78f" y="279.877482"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="265.837772"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="271.102663"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="276.367554"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="278.122518"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C8_0_7b1106a78f" y="271.102663"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="267.592736"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C8_0_7b1106a78f" y="278.122518"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="598.939554" xlink:href="#C8_0_7b1106a78f" y="290.407264"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="274.612591"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="612.225268" xlink:href="#C8_0_7b1106a78f" y="274.612591"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="274.612591"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="272.857627"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="605.582411" xlink:href="#C8_0_7b1106a78f" y="295.672155"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="618.868125" xlink:href="#C8_0_7b1106a78f" y="276.367554"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C8_0_7b1106a78f" y="243.023245"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="244.778208"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C8_0_7b1106a78f" y="246.533172"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="232.493462"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="645.439554" xlink:href="#C8_0_7b1106a78f" y="269.3477"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="237.758354"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="246.533172"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C8_0_7b1106a78f" y="241.268281"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C8_0_7b1106a78f" y="255.30799"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="251.798063"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="260.572881"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="255.30799"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="251.798063"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C8_0_7b1106a78f" y="230.738499"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="227.228571"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="260.572881"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="248.288136"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="262.327845"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="230.738499"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="262.327845"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="248.288136"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="243.023245"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="264.082809"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="262.327845"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="638.796696" xlink:href="#C8_0_7b1106a78f" y="246.533172"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C8_0_7b1106a78f" y="241.268281"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="236.00339"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="678.653839" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="632.153839" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="625.510982" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="241.268281"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="251.798063"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="264.082809"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="672.010982" xlink:href="#C8_0_7b1106a78f" y="253.553027"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="691.939554" xlink:href="#C8_0_7b1106a78f" y="250.043099"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="244.778208"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="698.582411" xlink:href="#C8_0_7b1106a78f" y="248.288136"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="257.062954"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="658.725268" xlink:href="#C8_0_7b1106a78f" y="260.572881"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="665.368125" xlink:href="#C8_0_7b1106a78f" y="257.062954"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="685.296696" xlink:href="#C8_0_7b1106a78f" y="253.553027"/>

    </g>

    <g clip-path="url(#pb4a692a22c)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="652.082411" xlink:href="#C8_0_7b1106a78f" y="258.817918"/>

    </g>

   </g>

   <g id="patch_88">

    <path d="M 535.168125 333.36 

L 535.168125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_89">

    <path d="M 702.568125 333.36 

L 702.568125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_90">

    <path d="M 535.168125 333.36 

L 702.568125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_91">

    <path d="M 535.168125 224.64 

L 702.568125 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_13">

   <g id="patch_92">

    <path d="M 32.968125 442.08 

L 200.368125 442.08 

L 200.368125 333.36 

L 32.968125 333.36 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_10">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="C9_0_b82fbde30e"/>

    </defs>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="36.953839" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="422.234286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="54.668125" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="439.491429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="45.810982" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="41.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="417.92"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="426.548571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="59.096696" xlink:href="#C9_0_b82fbde30e" y="430.862857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="50.239554" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="81.239554" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="435.177143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="156.525268" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="374.777143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="76.810982" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="396.348571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="392.034286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="138.810982" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="370.462857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="396.348571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="392.034286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="374.777143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="85.668125" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="374.777143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="90.096696" xlink:href="#C9_0_b82fbde30e" y="392.034286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="392.034286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="67.953839" xlink:href="#C9_0_b82fbde30e" y="400.662857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="392.034286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="72.382411" xlink:href="#C9_0_b82fbde30e" y="396.348571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="387.72"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="335.948571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="361.834286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="160.953839" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C9_0_b82fbde30e" y="348.891429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="183.096696" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="63.525268" xlink:href="#C9_0_b82fbde30e" y="370.462857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="169.810982" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C9_0_b82fbde30e" y="335.948571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="361.834286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="98.953839" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="340.262857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C9_0_b82fbde30e" y="348.891429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="94.525268" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="165.382411" xlink:href="#C9_0_b82fbde30e" y="374.777143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="174.239554" xlink:href="#C9_0_b82fbde30e" y="361.834286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="196.382411" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="348.891429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="379.091429"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="116.668125" xlink:href="#C9_0_b82fbde30e" y="383.405714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="187.525268" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="340.262857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="129.953839" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="112.239554" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C9_0_b82fbde30e" y="353.205714"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="340.262857"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="152.096696" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="103.382411" xlink:href="#C9_0_b82fbde30e" y="361.834286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="147.668125" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="335.948571"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="143.239554" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="125.525268" xlink:href="#C9_0_b82fbde30e" y="361.834286"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="134.382411" xlink:href="#C9_0_b82fbde30e" y="357.52"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="121.096696" xlink:href="#C9_0_b82fbde30e" y="344.577143"/>

    </g>

    <g clip-path="url(#p030a453e9f)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="107.810982" xlink:href="#C9_0_b82fbde30e" y="366.148571"/>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="xtick_1">

     <g id="line2d_10">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="md24634eec9" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="67.953839" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 5 -->

      <g transform="translate(70.161339 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="112.239554" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 6 -->

      <g transform="translate(114.447054 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="156.525268" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 7 -->

      <g transform="translate(158.732768 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-55"/>

      </g>

     </g>

    </g>

    <g id="text_16">

     <!-- SepalLengthCm -->

     <g transform="translate(77.181406 465.768437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-83"/>

      <use x="63.476562" xlink:href="#DejaVuSans-101"/>

      <use x="125" xlink:href="#DejaVuSans-112"/>

      <use x="188.476562" xlink:href="#DejaVuSans-97"/>

      <use x="249.755859" xlink:href="#DejaVuSans-108"/>

      <use x="277.539062" xlink:href="#DejaVuSans-76"/>

      <use x="331.501953" xlink:href="#DejaVuSans-101"/>

      <use x="393.025391" xlink:href="#DejaVuSans-110"/>

      <use x="456.404297" xlink:href="#DejaVuSans-103"/>

      <use x="519.880859" xlink:href="#DejaVuSans-116"/>

      <use x="559.089844" xlink:href="#DejaVuSans-104"/>

      <use x="622.46875" xlink:href="#DejaVuSans-67"/>

      <use x="692.292969" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_5">

    <g id="ytick_10">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="400.662857"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 1 -->

      <defs>

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

      <g transform="translate(20.878125 403.702232)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_11">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="32.968125" xlink:href="#m60453630f8" y="357.52"/>

      </g>

     </g>

     <g id="text_18">

      <!-- 2 -->

      <g transform="translate(20.878125 360.559375)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="text_19">

     <!-- PetalWidthCm -->

     <g transform="translate(14.798438 422.928594)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-80"/>

      <use x="56.677734" xlink:href="#DejaVuSans-101"/>

      <use x="118.201172" xlink:href="#DejaVuSans-116"/>

      <use x="157.410156" xlink:href="#DejaVuSans-97"/>

      <use x="218.689453" xlink:href="#DejaVuSans-108"/>

      <use x="246.472656" xlink:href="#DejaVuSans-87"/>

      <use x="343.099609" xlink:href="#DejaVuSans-105"/>

      <use x="370.882812" xlink:href="#DejaVuSans-100"/>

      <use x="434.359375" xlink:href="#DejaVuSans-116"/>

      <use x="473.568359" xlink:href="#DejaVuSans-104"/>

      <use x="536.947266" xlink:href="#DejaVuSans-67"/>

      <use x="606.771484" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_93">

    <path d="M 32.968125 442.08 

L 32.968125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_94">

    <path d="M 200.368125 442.08 

L 200.368125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_95">

    <path d="M 32.968125 442.08 

L 200.368125 442.08 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_96">

    <path d="M 32.968125 333.36 

L 200.368125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_14">

   <g id="patch_97">

    <path d="M 200.368125 442.08 

L 367.768125 442.08 

L 367.768125 333.36 

L 200.368125 333.36 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_11">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="Ca_0_4266e3bba3"/>

    </defs>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="337.210982" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="363.782411" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="330.568125" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="422.234286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="343.853839" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="350.496696" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="439.491429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="303.996696" xlink:href="#Ca_0_4266e3bba3" y="417.92"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="426.548571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="430.862857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="317.282411" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="435.177143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="374.777143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="204.353839" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="396.348571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="392.034286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="370.462857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#Ca_0_4266e3bba3" y="396.348571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="230.925268" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="392.034286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="374.777143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="374.777143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#Ca_0_4266e3bba3" y="392.034286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#Ca_0_4266e3bba3" y="392.034286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="224.282411" xlink:href="#Ca_0_4266e3bba3" y="400.662857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="392.034286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="396.348571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="387.72"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="335.948571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="361.834286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="348.891429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="370.462857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="264.139554" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="310.639554" xlink:href="#Ca_0_4266e3bba3" y="335.948571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="361.834286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="340.262857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="348.891429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="217.639554" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="374.777143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="361.834286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="323.925268" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="348.891429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="257.496696" xlink:href="#Ca_0_4266e3bba3" y="379.091429"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="244.210982" xlink:href="#Ca_0_4266e3bba3" y="383.405714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="340.262857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="353.205714"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="340.262857"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="277.425268" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="250.853839" xlink:href="#Ca_0_4266e3bba3" y="361.834286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="284.068125" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="290.710982" xlink:href="#Ca_0_4266e3bba3" y="335.948571"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="237.568125" xlink:href="#Ca_0_4266e3bba3" y="361.834286"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="357.52"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="297.353839" xlink:href="#Ca_0_4266e3bba3" y="344.577143"/>

    </g>

    <g clip-path="url(#pf504188c70)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="270.782411" xlink:href="#Ca_0_4266e3bba3" y="366.148571"/>

    </g>

   </g>

   <g id="matplotlib.axis_6">

    <g id="xtick_4">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="204.353839" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_20">

      <!-- 2 -->

      <g transform="translate(206.561339 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="270.782411" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_21">

      <!-- 3 -->

      <g transform="translate(272.989911 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="337.210982" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_22">

      <!-- 4 -->

      <g transform="translate(339.418482 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="text_23">

     <!-- SepalWidthCm -->

     <g transform="translate(247.304844 465.768437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-83"/>

      <use x="63.476562" xlink:href="#DejaVuSans-101"/>

      <use x="125" xlink:href="#DejaVuSans-112"/>

      <use x="188.476562" xlink:href="#DejaVuSans-97"/>

      <use x="249.755859" xlink:href="#DejaVuSans-108"/>

      <use x="277.539062" xlink:href="#DejaVuSans-87"/>

      <use x="374.166016" xlink:href="#DejaVuSans-105"/>

      <use x="401.949219" xlink:href="#DejaVuSans-100"/>

      <use x="465.425781" xlink:href="#DejaVuSans-116"/>

      <use x="504.634766" xlink:href="#DejaVuSans-104"/>

      <use x="568.013672" xlink:href="#DejaVuSans-67"/>

      <use x="637.837891" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_98">

    <path d="M 200.368125 442.08 

L 200.368125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_99">

    <path d="M 367.768125 442.08 

L 367.768125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_100">

    <path d="M 200.368125 442.08 

L 367.768125 442.08 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_101">

    <path d="M 200.368125 333.36 

L 367.768125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_15">

   <g id="patch_102">

    <path d="M 367.768125 442.08 

L 535.168125 442.08 

L 535.168125 333.36 

L 367.768125 333.36 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="PathCollection_12">

    <defs>

     <path d="M 0 1.5 

C 0.397805 1.5 0.77937 1.341951 1.06066 1.06066 

C 1.341951 0.77937 1.5 0.397805 1.5 0 

C 1.5 -0.397805 1.341951 -0.77937 1.06066 -1.06066 

C 0.77937 -1.341951 0.397805 -1.5 0 -1.5 

C -0.397805 -1.5 -0.77937 -1.341951 -1.06066 -1.06066 

C -1.341951 -0.77937 -1.5 -0.397805 -1.5 0 

C -1.5 0.397805 -1.341951 0.77937 -1.06066 1.06066 

C -0.77937 1.341951 -0.397805 1.5 0 1.5 

z

" id="Cb_0_c477e8125e"/>

    </defs>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="374.456018" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="371.753839" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="390.669094" xlink:href="#Cb_0_c477e8125e" y="422.234286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="377.158198" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="439.491429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="379.860377" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="417.92"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="396.073452" xlink:href="#Cb_0_c477e8125e" y="426.548571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="430.862857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="387.966914" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="385.264735" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="382.562556" xlink:href="#Cb_0_c477e8125e" y="435.177143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#Cb_0_c477e8125e" y="374.777143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="442.010498" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#Cb_0_c477e8125e" y="396.348571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#Cb_0_c477e8125e" y="392.034286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#Cb_0_c477e8125e" y="370.462857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="439.308319" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="447.414856" xlink:href="#Cb_0_c477e8125e" y="396.348571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="444.712677" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="450.117035" xlink:href="#Cb_0_c477e8125e" y="392.034286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="374.777143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="374.777143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="471.734469" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="463.627931" xlink:href="#Cb_0_c477e8125e" y="392.034286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="469.03229" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="452.819215" xlink:href="#Cb_0_c477e8125e" y="392.034286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="433.90396" xlink:href="#Cb_0_c477e8125e" y="400.662857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#Cb_0_c477e8125e" y="392.034286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="458.223573" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="460.925752" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="425.797423" xlink:href="#Cb_0_c477e8125e" y="396.348571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="455.521394" xlink:href="#Cb_0_c477e8125e" y="387.72"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#Cb_0_c477e8125e" y="335.948571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="361.834286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#Cb_0_c477e8125e" y="348.891429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="523.075873" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="466.33011" xlink:href="#Cb_0_c477e8125e" y="370.462857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="514.969336" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#Cb_0_c477e8125e" y="335.948571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#Cb_0_c477e8125e" y="361.834286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="340.262857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="487.947544" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#Cb_0_c477e8125e" y="348.891429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="531.182411" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="525.778052" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="506.862798" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="477.138827" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="501.45844" xlink:href="#Cb_0_c477e8125e" y="374.777143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#Cb_0_c477e8125e" y="361.834286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="517.671515" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="348.891429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="379.091429"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="383.405714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="509.564977" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="340.262857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="493.351902" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="474.436648" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#Cb_0_c477e8125e" y="353.205714"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="496.054081" xlink:href="#Cb_0_c477e8125e" y="340.262857"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="361.834286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="504.160619" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="498.756261" xlink:href="#Cb_0_c477e8125e" y="335.948571"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="479.841006" xlink:href="#Cb_0_c477e8125e" y="361.834286"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="485.245365" xlink:href="#Cb_0_c477e8125e" y="357.52"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="490.649723" xlink:href="#Cb_0_c477e8125e" y="344.577143"/>

    </g>

    <g clip-path="url(#p5d30e327af)">

     <use style="fill:#1f77b4;fill-opacity:0.5;" x="482.543186" xlink:href="#Cb_0_c477e8125e" y="366.148571"/>

    </g>

   </g>

   <g id="matplotlib.axis_7">

    <g id="xtick_7">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="398.775631" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_24">

      <!-- 2 -->

      <g transform="translate(400.983131 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="452.819215" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_25">

      <!-- 4 -->

      <g transform="translate(455.026715 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="line2d_20">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="506.862798" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_26">

      <!-- 6 -->

      <g transform="translate(509.070298 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="text_27">

     <!-- PetalLengthCm -->

     <g transform="translate(413.536094 465.768437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-80"/>

      <use x="56.677734" xlink:href="#DejaVuSans-101"/>

      <use x="118.201172" xlink:href="#DejaVuSans-116"/>

      <use x="157.410156" xlink:href="#DejaVuSans-97"/>

      <use x="218.689453" xlink:href="#DejaVuSans-108"/>

      <use x="246.472656" xlink:href="#DejaVuSans-76"/>

      <use x="300.435547" xlink:href="#DejaVuSans-101"/>

      <use x="361.958984" xlink:href="#DejaVuSans-110"/>

      <use x="425.337891" xlink:href="#DejaVuSans-103"/>

      <use x="488.814453" xlink:href="#DejaVuSans-116"/>

      <use x="528.023438" xlink:href="#DejaVuSans-104"/>

      <use x="591.402344" xlink:href="#DejaVuSans-67"/>

      <use x="661.226562" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_103">

    <path d="M 367.768125 442.08 

L 367.768125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_104">

    <path d="M 535.168125 442.08 

L 535.168125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_105">

    <path d="M 367.768125 442.08 

L 535.168125 442.08 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_106">

    <path d="M 367.768125 333.36 

L 535.168125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_16">

   <g id="patch_107">

    <path d="M 535.168125 442.08 

L 702.568125 442.08 

L 702.568125 333.36 

L 535.168125 333.36 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="patch_108">

    <path clip-path="url(#p6c3a9606c0)" d="M 539.153839 442.08 

L 555.096696 442.08 

L 555.096696 338.537143 

L 539.153839 338.537143 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_109">

    <path clip-path="url(#p6c3a9606c0)" d="M 555.096696 442.08 

L 571.039554 442.08 

L 571.039554 421.371429 

L 555.096696 421.371429 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_110">

    <path clip-path="url(#p6c3a9606c0)" d="M 571.039554 442.08 

L 586.982411 442.08 

L 586.982411 439.491429 

L 571.039554 439.491429 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_111">

    <path clip-path="url(#p6c3a9606c0)" d="M 586.982411 442.08 

L 602.925268 442.08 

L 602.925268 423.96 

L 586.982411 423.96 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_112">

    <path clip-path="url(#p6c3a9606c0)" d="M 602.925268 442.08 

L 618.868125 442.08 

L 618.868125 421.371429 

L 602.925268 421.371429 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_113">

    <path clip-path="url(#p6c3a9606c0)" d="M 618.868125 442.08 

L 634.810982 442.08 

L 634.810982 356.657143 

L 618.868125 356.657143 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_114">

    <path clip-path="url(#p6c3a9606c0)" d="M 634.810982 442.08 

L 650.753839 442.08 

L 650.753839 426.548571 

L 634.810982 426.548571 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_115">

    <path clip-path="url(#p6c3a9606c0)" d="M 650.753839 442.08 

L 666.696696 442.08 

L 666.696696 382.542857 

L 650.753839 382.542857 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_116">

    <path clip-path="url(#p6c3a9606c0)" d="M 666.696696 442.08 

L 682.639554 442.08 

L 682.639554 418.782857 

L 666.696696 418.782857 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_117">

    <path clip-path="url(#p6c3a9606c0)" d="M 682.639554 442.08 

L 698.582411 442.08 

L 698.582411 405.84 

L 682.639554 405.84 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="matplotlib.axis_8">

    <g id="xtick_10">

     <g id="line2d_21">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="598.939554" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_28">

      <!-- 1 -->

      <g transform="translate(601.147054 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_11">

     <g id="line2d_22">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="665.368125" xlink:href="#md24634eec9" y="442.08"/>

      </g>

     </g>

     <g id="text_29">

      <!-- 2 -->

      <g transform="translate(667.575625 454.17)rotate(-90)scale(0.08 -0.08)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="text_30">

     <!-- PetalWidthCm -->

     <g transform="translate(583.659531 465.768437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-80"/>

      <use x="56.677734" xlink:href="#DejaVuSans-101"/>

      <use x="118.201172" xlink:href="#DejaVuSans-116"/>

      <use x="157.410156" xlink:href="#DejaVuSans-97"/>

      <use x="218.689453" xlink:href="#DejaVuSans-108"/>

      <use x="246.472656" xlink:href="#DejaVuSans-87"/>

      <use x="343.099609" xlink:href="#DejaVuSans-105"/>

      <use x="370.882812" xlink:href="#DejaVuSans-100"/>

      <use x="434.359375" xlink:href="#DejaVuSans-116"/>

      <use x="473.568359" xlink:href="#DejaVuSans-104"/>

      <use x="536.947266" xlink:href="#DejaVuSans-67"/>

      <use x="606.771484" xlink:href="#DejaVuSans-109"/>

     </g>

    </g>

   </g>

   <g id="patch_118">

    <path d="M 535.168125 442.08 

L 535.168125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_119">

    <path d="M 702.568125 442.08 

L 702.568125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_120">

    <path d="M 535.168125 442.08 

L 702.568125 442.08 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_121">

    <path d="M 535.168125 333.36 

L 702.568125 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p1e3eba2890">

   <rect height="108.72" width="167.4" x="32.968125" y="7.2"/>

  </clipPath>

  <clipPath id="p9c3456b21f">

   <rect height="108.72" width="167.4" x="200.368125" y="7.2"/>

  </clipPath>

  <clipPath id="p181218a914">

   <rect height="108.72" width="167.4" x="367.768125" y="7.2"/>

  </clipPath>

  <clipPath id="p630b29a36a">

   <rect height="108.72" width="167.4" x="535.168125" y="7.2"/>

  </clipPath>

  <clipPath id="pf147c76d04">

   <rect height="108.72" width="167.4" x="32.968125" y="115.92"/>

  </clipPath>

  <clipPath id="p5ac31d3c11">

   <rect height="108.72" width="167.4" x="200.368125" y="115.92"/>

  </clipPath>

  <clipPath id="p8690fc581c">

   <rect height="108.72" width="167.4" x="367.768125" y="115.92"/>

  </clipPath>

  <clipPath id="pba906d30d6">

   <rect height="108.72" width="167.4" x="535.168125" y="115.92"/>

  </clipPath>

  <clipPath id="p5bd16baee8">

   <rect height="108.72" width="167.4" x="32.968125" y="224.64"/>

  </clipPath>

  <clipPath id="pd9b1e8b8d6">

   <rect height="108.72" width="167.4" x="200.368125" y="224.64"/>

  </clipPath>

  <clipPath id="p483e01def2">

   <rect height="108.72" width="167.4" x="367.768125" y="224.64"/>

  </clipPath>

  <clipPath id="pb4a692a22c">

   <rect height="108.72" width="167.4" x="535.168125" y="224.64"/>

  </clipPath>

  <clipPath id="p030a453e9f">

   <rect height="108.72" width="167.4" x="32.968125" y="333.36"/>

  </clipPath>

  <clipPath id="pf504188c70">

   <rect height="108.72" width="167.4" x="200.368125" y="333.36"/>

  </clipPath>

  <clipPath id="p5d30e327af">

   <rect height="108.72" width="167.4" x="367.768125" y="333.36"/>

  </clipPath>

  <clipPath id="p6c3a9606c0">

   <rect height="108.72" width="167.4" x="535.168125" y="333.36"/>

  </clipPath>

 </defs>

</svg>


</div>

</div>

</div>
</div>

</div>
 

