<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-3">Video 3<a class="anchor-link" href="#Video-3">&#182;</a></h1><p>Selenium kann gut für <a href="https://github.com/JHC90/PrivatePythonCheats/blob/master/Basics/11_Modul_tests.ipynb">Unittests</a> verwendet werden. Das Resultat checkt man dann in der Rückgabe gegen. Wichtig ist hier das Python Modul <a href="https://docs.python.org/3/library/unittest.html">unittest</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;bfk6mmYkOWI&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

        <iframe
            width="800"
            height="300"
            src="https://www.youtube.com/embed/bfk6mmYkOWI"
            frameborder="0"
            allowfullscreen
        ></iframe>
        
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span>
<span class="kn">import</span> <span class="nn">unittest</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span> <span class="c1"># Wenn der Webdriver im Path</span>
<span class="c1">#driverFF = webdriver.Firefox()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">GoogleTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span>
        
    <span class="k">def</span> <span class="nf">test_google_search</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de&#39;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">assertIn</span><span class="p">(</span><span class="s2">&quot;Google&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">driver</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
        <span class="n">search_field</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_name</span><span class="p">(</span><span class="s1">&#39;q&#39;</span><span class="p">)</span>
        <span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;Silvia Ruidisch&#39;</span><span class="p">)</span>
        <span class="n">search_field</span><span class="o">.</span><span class="n">submit</span><span class="p">()</span>
        <span class="k">assert</span> <span class="s2">&quot;Es wurde keine mit deiner Suchanfrage - &quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">driver</span><span class="o">.</span><span class="n">page_source</span>
        
    <span class="k">def</span> <span class="nf">tearDown</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">driver</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        
<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">&quot;__main__&quot;</span><span class="p">:</span>
    <span class="n">unittest</span><span class="o">.</span><span class="n">main</span><span class="p">()</span> <span class="c1"># alles was von Unittest erbt wird hier ausgeführt</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>usage: ipykernel_launcher [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
                          [-k TESTNAMEPATTERNS]
                          [tests [tests ...]]
ipykernel_launcher: error: argument -f/--failfast: ignored explicit argument &#39;C:\\Users\\181083~1\\AppData\\Local\\Temp\\tmp-4112068VsHL0w4Us.json&#39;
ERROR:root:Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 1800, in parse_known_args
    namespace, args = self._parse_known_args(args, namespace)
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 2006, in _parse_known_args
    start_index = consume_optional(start_index)
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 1928, in consume_optional
    raise ArgumentError(action, msg % explicit_arg)
argparse.ArgumentError: argument -f/--failfast: ignored explicit argument &#39;C:\\Users\\181083~1\\AppData\\Local\\Temp\\tmp-4112068VsHL0w4Us.json&#39;

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File &#34;C:\Users\1810837475\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py&#34;, line 3343, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File &#34;&lt;ipython-input-5-9f99e43e9aeb&gt;&#34;, line 17, in &lt;module&gt;
    unittest.main() # alles was von Unittest erbt wird hier ausgeführt
  File &#34;C:\Users\1810837475\Anaconda3\lib\unittest\main.py&#34;, line 100, in __init__
    self.parseArgs(argv)
  File &#34;C:\Users\1810837475\Anaconda3\lib\unittest\main.py&#34;, line 133, in parseArgs
    self._main_parser.parse_args(argv[1:], self)
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 1768, in parse_args
    args, argv = self.parse_known_args(args, namespace)
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 1807, in parse_known_args
    self.error(str(err))
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 2521, in error
    self.exit(2, _(&#39;%(prog)s: error: %(message)s\n&#39;) % args)
  File &#34;C:\Users\1810837475\Anaconda3\lib\argparse.py&#34;, line 2508, in exit
    _sys.exit(status)
SystemExit: 2

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File &#34;C:\Users\1810837475\Anaconda3\lib\site-packages\IPython\core\ultratb.py&#34;, line 1169, in get_records
    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)
  File &#34;C:\Users\1810837475\Anaconda3\lib\site-packages\IPython\core\ultratb.py&#34;, line 316, in wrapped
    return f(*args, **kwargs)
  File &#34;C:\Users\1810837475\Anaconda3\lib\site-packages\IPython\core\ultratb.py&#34;, line 350, in _fixed_getinnerframes
    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))
  File &#34;C:\Users\1810837475\Anaconda3\lib\inspect.py&#34;, line 1503, in getinnerframes
    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)
AttributeError: &#39;tuple&#39; object has no attribute &#39;tb_frame&#39;
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">ArgumentError</span>                             Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">parse_known_args</span><span class="ansi-blue-intense-fg ansi-bold">(self, args, namespace)</span>
<span class="ansi-green-fg">   1799</span>         <span class="ansi-green-intense-fg ansi-bold">try</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1800</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>namespace<span class="ansi-yellow-intense-fg ansi-bold">,</span> args <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_parse_known_args<span class="ansi-yellow-intense-fg ansi-bold">(</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> namespace<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1801</span>             <span class="ansi-green-intense-fg ansi-bold">if</span> hasattr<span class="ansi-yellow-intense-fg ansi-bold">(</span>namespace<span class="ansi-yellow-intense-fg ansi-bold">,</span> _UNRECOGNIZED_ARGS_ATTR<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">_parse_known_args</span><span class="ansi-blue-intense-fg ansi-bold">(self, arg_strings, namespace)</span>
<span class="ansi-green-fg">   2005</span>             <span class="ansi-red-intense-fg ansi-bold"># consume the next optional and any arguments for it</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2006</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>start_index <span class="ansi-yellow-intense-fg ansi-bold">=</span> consume_optional<span class="ansi-yellow-intense-fg ansi-bold">(</span>start_index<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   2007</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">consume_optional</span><span class="ansi-blue-intense-fg ansi-bold">(start_index)</span>
<span class="ansi-green-fg">   1927</span>                         msg <span class="ansi-yellow-intense-fg ansi-bold">=</span> _<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;ignored explicit argument %r&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1928</span><span class="ansi-yellow-intense-fg ansi-bold">                         </span><span class="ansi-green-intense-fg ansi-bold">raise</span> ArgumentError<span class="ansi-yellow-intense-fg ansi-bold">(</span>action<span class="ansi-yellow-intense-fg ansi-bold">,</span> msg <span class="ansi-yellow-intense-fg ansi-bold">%</span> explicit_arg<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1929</span> 

<span class="ansi-red-intense-fg ansi-bold">ArgumentError</span>: argument -f/--failfast: ignored explicit argument &#39;C:\\Users\\181083~1\\AppData\\Local\\Temp\\tmp-4112068VsHL0w4Us.json&#39;

During handling of the above exception, another exception occurred:

<span class="ansi-red-intense-fg ansi-bold">SystemExit</span>                                Traceback (most recent call last)
    <span class="ansi-red-intense-fg ansi-bold">[... skipping hidden 1 frame]</span>

<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-5-9f99e43e9aeb&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">     16</span> <span class="ansi-green-intense-fg ansi-bold">if</span> __name__ <span class="ansi-yellow-intense-fg ansi-bold">==</span> <span class="ansi-blue-intense-fg ansi-bold">&#34;__main__&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 17</span><span class="ansi-yellow-intense-fg ansi-bold">     </span>unittest<span class="ansi-yellow-intense-fg ansi-bold">.</span>main<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-red-intense-fg ansi-bold"># alles was von Unittest erbt wird hier ausgeführt</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\unittest\main.py</span> in <span class="ansi-cyan-fg">__init__</span><span class="ansi-blue-intense-fg ansi-bold">(self, module, defaultTest, argv, testRunner, testLoader, exit, verbosity, failfast, catchbreak, buffer, warnings, tb_locals)</span>
<span class="ansi-green-fg">     99</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>progName <span class="ansi-yellow-intense-fg ansi-bold">=</span> os<span class="ansi-yellow-intense-fg ansi-bold">.</span>path<span class="ansi-yellow-intense-fg ansi-bold">.</span>basename<span class="ansi-yellow-intense-fg ansi-bold">(</span>argv<span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">0</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 100</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>parseArgs<span class="ansi-yellow-intense-fg ansi-bold">(</span>argv<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    101</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>runTests<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\unittest\main.py</span> in <span class="ansi-cyan-fg">parseArgs</span><span class="ansi-blue-intense-fg ansi-bold">(self, argv)</span>
<span class="ansi-green-fg">    132</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 133</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_main_parser<span class="ansi-yellow-intense-fg ansi-bold">.</span>parse_args<span class="ansi-yellow-intense-fg ansi-bold">(</span>argv<span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">1</span><span class="ansi-yellow-intense-fg ansi-bold">:</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    134</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">parse_args</span><span class="ansi-blue-intense-fg ansi-bold">(self, args, namespace)</span>
<span class="ansi-green-fg">   1767</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> parse_args<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> args<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> namespace<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1768</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> argv <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>parse_known_args<span class="ansi-yellow-intense-fg ansi-bold">(</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> namespace<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1769</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> argv<span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">parse_known_args</span><span class="ansi-blue-intense-fg ansi-bold">(self, args, namespace)</span>
<span class="ansi-green-fg">   1806</span>             err <span class="ansi-yellow-intense-fg ansi-bold">=</span> _sys<span class="ansi-yellow-intense-fg ansi-bold">.</span>exc_info<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">1</span><span class="ansi-yellow-intense-fg ansi-bold">]</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1807</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>error<span class="ansi-yellow-intense-fg ansi-bold">(</span>str<span class="ansi-yellow-intense-fg ansi-bold">(</span>err<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1808</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">error</span><span class="ansi-blue-intense-fg ansi-bold">(self, message)</span>
<span class="ansi-green-fg">   2520</span>         args <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-yellow-intense-fg ansi-bold">{</span><span class="ansi-blue-intense-fg ansi-bold">&#39;prog&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">:</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>prog<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;message&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">:</span> message<span class="ansi-yellow-intense-fg ansi-bold">}</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2521</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>exit<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-cyan-intense-fg ansi-bold">2</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> _<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;%(prog)s: error: %(message)s\n&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-yellow-intense-fg ansi-bold">%</span> args<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\argparse.py</span> in <span class="ansi-cyan-fg">exit</span><span class="ansi-blue-intense-fg ansi-bold">(self, status, message)</span>
<span class="ansi-green-fg">   2507</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_print_message<span class="ansi-yellow-intense-fg ansi-bold">(</span>message<span class="ansi-yellow-intense-fg ansi-bold">,</span> _sys<span class="ansi-yellow-intense-fg ansi-bold">.</span>stderr<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2508</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>_sys<span class="ansi-yellow-intense-fg ansi-bold">.</span>exit<span class="ansi-yellow-intense-fg ansi-bold">(</span>status<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   2509</span> 

<span class="ansi-red-intense-fg ansi-bold">SystemExit</span>: 2

During handling of the above exception, another exception occurred:

<span class="ansi-red-intense-fg ansi-bold">TypeError</span>                                 Traceback (most recent call last)
    <span class="ansi-red-intense-fg ansi-bold">[... skipping hidden 1 frame]</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py</span> in <span class="ansi-cyan-fg">showtraceback</span><span class="ansi-blue-intense-fg ansi-bold">(self, exc_tuple, filename, tb_offset, exception_only, running_compiled_code)</span>
<span class="ansi-green-fg">   2035</span>                     stb = [&#39;An exception has occurred, use %tb to see &#39;
<span class="ansi-green-fg">   2036</span>                            &#39;the full traceback.\n&#39;]
<span class="ansi-green-intense-fg ansi-bold">-&gt; 2037</span><span class="ansi-yellow-intense-fg ansi-bold">                     stb.extend(self.InteractiveTB.get_exception_only(etype,
</span><span class="ansi-green-fg">   2038</span>                                                                      value))
<span class="ansi-green-fg">   2039</span>                 <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">get_exception_only</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, value)</span>
<span class="ansi-green-fg">    821</span>         value <span class="ansi-yellow-intense-fg ansi-bold">:</span> exception value
<span class="ansi-green-fg">    822</span>         &#34;&#34;&#34;
<span class="ansi-green-intense-fg ansi-bold">--&gt; 823</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> ListTB<span class="ansi-yellow-intense-fg ansi-bold">.</span>structured_traceback<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> value<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    824</span> 
<span class="ansi-green-fg">    825</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> show_exception_only<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> evalue<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">structured_traceback</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, evalue, etb, tb_offset, context)</span>
<span class="ansi-green-fg">    696</span>             chained_exceptions_tb_offset <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-cyan-intense-fg ansi-bold">0</span>
<span class="ansi-green-fg">    697</span>             out_list = (
<span class="ansi-green-intense-fg ansi-bold">--&gt; 698</span><span class="ansi-yellow-intense-fg ansi-bold">                 self.structured_traceback(
</span><span class="ansi-green-fg">    699</span>                     etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> evalue<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">(</span>etb<span class="ansi-yellow-intense-fg ansi-bold">,</span> chained_exc_ids<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">    700</span>                     chained_exceptions_tb_offset, context)

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">structured_traceback</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, value, tb, tb_offset, number_of_lines_of_context)</span>
<span class="ansi-green-fg">   1433</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">   1434</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>tb <span class="ansi-yellow-intense-fg ansi-bold">=</span> tb
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1435</span><span class="ansi-yellow-intense-fg ansi-bold">         return FormattedTB.structured_traceback(
</span><span class="ansi-green-fg">   1436</span>             self, etype, value, tb, tb_offset, number_of_lines_of_context)
<span class="ansi-green-fg">   1437</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">structured_traceback</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, value, tb, tb_offset, number_of_lines_of_context)</span>
<span class="ansi-green-fg">   1333</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> mode <span class="ansi-green-intense-fg ansi-bold">in</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>verbose_modes<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">   1334</span>             <span class="ansi-red-intense-fg ansi-bold"># Verbose modes need a full traceback</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1335</span><span class="ansi-yellow-intense-fg ansi-bold">             return VerboseTB.structured_traceback(
</span><span class="ansi-green-fg">   1336</span>                 self<span class="ansi-yellow-intense-fg ansi-bold">,</span> etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> value<span class="ansi-yellow-intense-fg ansi-bold">,</span> tb<span class="ansi-yellow-intense-fg ansi-bold">,</span> tb_offset<span class="ansi-yellow-intense-fg ansi-bold">,</span> number_of_lines_of_context
<span class="ansi-green-fg">   1337</span>             )

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">structured_traceback</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)</span>
<span class="ansi-green-fg">   1190</span>         <span class="ansi-blue-intense-fg ansi-bold">&#34;&#34;&#34;Return a nice text document describing the traceback.&#34;&#34;&#34;</span>
<span class="ansi-green-fg">   1191</span> 
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1192</span><span class="ansi-yellow-intense-fg ansi-bold">         formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
</span><span class="ansi-green-fg">   1193</span>                                                                tb_offset)
<span class="ansi-green-fg">   1194</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">format_exception_as_a_whole</span><span class="ansi-blue-intense-fg ansi-bold">(self, etype, evalue, etb, number_of_lines_of_context, tb_offset)</span>
<span class="ansi-green-fg">   1148</span> 
<span class="ansi-green-fg">   1149</span> 
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1150</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>last_unique<span class="ansi-yellow-intense-fg ansi-bold">,</span> recursion_repeat <span class="ansi-yellow-intense-fg ansi-bold">=</span> find_recursion<span class="ansi-yellow-intense-fg ansi-bold">(</span>orig_etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> evalue<span class="ansi-yellow-intense-fg ansi-bold">,</span> records<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1151</span> 
<span class="ansi-green-fg">   1152</span>         frames <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>format_records<span class="ansi-yellow-intense-fg ansi-bold">(</span>records<span class="ansi-yellow-intense-fg ansi-bold">,</span> last_unique<span class="ansi-yellow-intense-fg ansi-bold">,</span> recursion_repeat<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\IPython\core\ultratb.py</span> in <span class="ansi-cyan-fg">find_recursion</span><span class="ansi-blue-intense-fg ansi-bold">(etype, value, records)</span>
<span class="ansi-green-fg">    449</span>     <span class="ansi-red-intense-fg ansi-bold"># first frame (from in to out) that looks different.</span>
<span class="ansi-green-fg">    450</span>     <span class="ansi-green-intense-fg ansi-bold">if</span> <span class="ansi-green-intense-fg ansi-bold">not</span> is_recursion_error<span class="ansi-yellow-intense-fg ansi-bold">(</span>etype<span class="ansi-yellow-intense-fg ansi-bold">,</span> value<span class="ansi-yellow-intense-fg ansi-bold">,</span> records<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 451</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> len<span class="ansi-yellow-intense-fg ansi-bold">(</span>records<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-cyan-intense-fg ansi-bold">0</span>
<span class="ansi-green-fg">    452</span> 
<span class="ansi-green-fg">    453</span>     <span class="ansi-red-intense-fg ansi-bold"># Select filename, lineno, func_name to track frames with</span>

<span class="ansi-red-intense-fg ansi-bold">TypeError</span>: object of type &#39;NoneType&#39; has no len()</pre>
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
 

