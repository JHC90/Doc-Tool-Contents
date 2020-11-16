<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Video-2">Video 2<a class="anchor-link" href="#Video-2">&#182;</a></h1><p>erste Bsp:</p>
<p>hier wird das "Googeln" automatisiert. Sprich es wird die Google Webseite geöffnet und automatisch etwas in die Suchzeile eingegeben und dieser Suchbegriff bestätigt.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">YouTubeVideo</span>

<span class="n">YouTubeVideo</span><span class="p">(</span><span class="s1">&#39;X_oTF5aSGcA&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">800</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">

        <iframe
            width="800"
            height="300"
            src="https://www.youtube.com/embed/X_oTF5aSGcA"
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
<div class="prompt input_prompt">In&nbsp;[44]:</div>
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
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># erstellt ein Browser in Viruteller Einheit</span>
<span class="c1">#driver = webdriver.Chrome(&#39;C:/Webdriver/chromedriver.exe&#39;)# absoluter pfad</span>
<span class="n">driver</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">()</span> <span class="c1"># Wenn der Webdriver im Path</span>
<span class="c1">#driverFF = webdriver.Firefox()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[51]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Einfacher Websiten-Call</span>
<span class="c1">#driver.get(&#39;https://www.tz.de&#39;)</span>
<span class="c1">#driver.close()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Einfacher Websiten-Call mit User Interaktion</span>
<span class="n">driver</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;https://www.google.de&#39;</span><span class="p">)</span>
<span class="n">search_field</span> <span class="o">=</span> <span class="n">driver</span><span class="o">.</span><span class="n">find_element_by_name</span><span class="p">(</span><span class="s1">&#39;q&#39;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="s1">&#39;Silvia Ruidisch&#39;</span><span class="p">)</span>
<span class="n">search_field</span><span class="o">.</span><span class="n">submit</span><span class="p">()</span>
<span class="n">driver</span><span class="o">.</span><span class="n">quit</span><span class="p">()</span>
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
<span class="ansi-red-intense-fg ansi-bold">ConnectionRefusedError</span>                    Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connection.py</span> in <span class="ansi-cyan-fg">_new_conn</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    158</span>         <span class="ansi-green-intense-fg ansi-bold">try</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 159</span><span class="ansi-yellow-intense-fg ansi-bold">             conn = connection.create_connection(
</span><span class="ansi-green-fg">    160</span>                 <span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_dns_host<span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>port<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>timeout<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>extra_kw

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\util\connection.py</span> in <span class="ansi-cyan-fg">create_connection</span><span class="ansi-blue-intense-fg ansi-bold">(address, timeout, source_address, socket_options)</span>
<span class="ansi-green-fg">     83</span>     <span class="ansi-green-intense-fg ansi-bold">if</span> err <span class="ansi-green-intense-fg ansi-bold">is</span> <span class="ansi-green-intense-fg ansi-bold">not</span> <span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 84</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">raise</span> err
<span class="ansi-green-fg">     85</span> 

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\util\connection.py</span> in <span class="ansi-cyan-fg">create_connection</span><span class="ansi-blue-intense-fg ansi-bold">(address, timeout, source_address, socket_options)</span>
<span class="ansi-green-fg">     73</span>                 sock<span class="ansi-yellow-intense-fg ansi-bold">.</span>bind<span class="ansi-yellow-intense-fg ansi-bold">(</span>source_address<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 74</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>sock<span class="ansi-yellow-intense-fg ansi-bold">.</span>connect<span class="ansi-yellow-intense-fg ansi-bold">(</span>sa<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">     75</span>             <span class="ansi-green-intense-fg ansi-bold">return</span> sock

<span class="ansi-red-intense-fg ansi-bold">ConnectionRefusedError</span>: [WinError 10061] Es konnte keine Verbindung hergestellt werden, da der Zielcomputer die Verbindung verweigerte

During handling of the above exception, another exception occurred:

<span class="ansi-red-intense-fg ansi-bold">NewConnectionError</span>                        Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body123_pos, **response_kw)</span>
<span class="ansi-green-fg">    669</span>             <span class="ansi-red-intense-fg ansi-bold"># Make the request on the httplib connection object.</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 670</span><span class="ansi-yellow-intense-fg ansi-bold">             httplib_response = self._make_request(
</span><span class="ansi-green-fg">    671</span>                 conn<span class="ansi-yellow-intense-fg ansi-bold">,</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">_make_request</span><span class="ansi-blue-intense-fg ansi-bold">(self, conn, method, url, timeout, chunked, **httplib_request_kw)</span>
<span class="ansi-green-fg">    391</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 392</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>conn<span class="ansi-yellow-intense-fg ansi-bold">.</span>request<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>httplib_request_kw<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    393</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\http\client.py</span> in <span class="ansi-cyan-fg">request</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, encode_chunked)</span>
<span class="ansi-green-fg">   1239</span>         <span class="ansi-blue-intense-fg ansi-bold">&#34;&#34;&#34;Send a complete request to the server.&#34;&#34;&#34;</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1240</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_send_request<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> body123<span class="ansi-yellow-intense-fg ansi-bold">,</span> head123er123s<span class="ansi-yellow-intense-fg ansi-bold">,</span> encode_chunked<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1241</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\http\client.py</span> in <span class="ansi-cyan-fg">_send_request</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, encode_chunked)</span>
<span class="ansi-green-fg">   1285</span>             body123 <span class="ansi-yellow-intense-fg ansi-bold">=</span> _encode<span class="ansi-yellow-intense-fg ansi-bold">(</span>body123<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;body123&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1286</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>endhead123er123s<span class="ansi-yellow-intense-fg ansi-bold">(</span>body123<span class="ansi-yellow-intense-fg ansi-bold">,</span> encode_chunked<span class="ansi-yellow-intense-fg ansi-bold">=</span>encode_chunked<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1287</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\http\client.py</span> in <span class="ansi-cyan-fg">endhead123er123s</span><span class="ansi-blue-intense-fg ansi-bold">(self, message_body123, encode_chunked)</span>
<span class="ansi-green-fg">   1234</span>             <span class="ansi-green-intense-fg ansi-bold">raise</span> CannotSendHeader<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1235</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_send_output<span class="ansi-yellow-intense-fg ansi-bold">(</span>message_body123<span class="ansi-yellow-intense-fg ansi-bold">,</span> encode_chunked<span class="ansi-yellow-intense-fg ansi-bold">=</span>encode_chunked<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1236</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\http\client.py</span> in <span class="ansi-cyan-fg">_send_output</span><span class="ansi-blue-intense-fg ansi-bold">(self, message_body123, encode_chunked)</span>
<span class="ansi-green-fg">   1005</span>         <span class="ansi-green-intense-fg ansi-bold">del</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_buffer<span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-yellow-intense-fg ansi-bold">:</span><span class="ansi-yellow-intense-fg ansi-bold">]</span>
<span class="ansi-green-intense-fg ansi-bold">-&gt; 1006</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>send<span class="ansi-yellow-intense-fg ansi-bold">(</span>msg<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">   1007</span> 

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\http\client.py</span> in <span class="ansi-cyan-fg">send</span><span class="ansi-blue-intense-fg ansi-bold">(self, data)</span>
<span class="ansi-green-fg">    945</span>             <span class="ansi-green-intense-fg ansi-bold">if</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>auto_open<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 946</span><span class="ansi-yellow-intense-fg ansi-bold">                 </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>connect<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    947</span>             <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connection.py</span> in <span class="ansi-cyan-fg">connect</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    186</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> connect<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 187</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>conn <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_new_conn<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    188</span>         self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_prepare_conn<span class="ansi-yellow-intense-fg ansi-bold">(</span>conn<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connection.py</span> in <span class="ansi-cyan-fg">_new_conn</span><span class="ansi-blue-intense-fg ansi-bold">(self)</span>
<span class="ansi-green-fg">    170</span>         <span class="ansi-green-intense-fg ansi-bold">except</span> SocketError <span class="ansi-green-intense-fg ansi-bold">as</span> e<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 171</span><span class="ansi-yellow-intense-fg ansi-bold">             raise NewConnectionError(
</span><span class="ansi-green-fg">    172</span>                 self<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-blue-intense-fg ansi-bold">&#34;Failed to establish a new connection: %s&#34;</span> <span class="ansi-yellow-intense-fg ansi-bold">%</span> e

<span class="ansi-red-intense-fg ansi-bold">NewConnectionError</span>: &lt;urllib3.connection.HTTPConnection object at 0x000001FBC3E8BC70&gt;: Failed to establish a new connection: [WinError 10061] Es konnte keine Verbindung hergestellt werden, da der Zielcomputer die Verbindung verweigerte

During handling of the above exception, another exception occurred:

<span class="ansi-red-intense-fg ansi-bold">MaxRetryError</span>                             Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-54-9ea16a89e908&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold"># Einfacher Websiten-Call mit User Interaktion</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 2</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>driver<span class="ansi-yellow-intense-fg ansi-bold">.</span>get<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;https://www.google.de&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      3</span> search_field <span class="ansi-yellow-intense-fg ansi-bold">=</span> driver<span class="ansi-yellow-intense-fg ansi-bold">.</span>find_element_by_name<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;q&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      4</span> search_field<span class="ansi-yellow-intense-fg ansi-bold">.</span>send_keys<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#39;Silvia Ruidisch&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      5</span> search_field<span class="ansi-yellow-intense-fg ansi-bold">.</span>submit<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py</span> in <span class="ansi-cyan-fg">get</span><span class="ansi-blue-intense-fg ansi-bold">(self, url)</span>
<span class="ansi-green-fg">    331</span>         Loads a web page <span class="ansi-green-intense-fg ansi-bold">in</span> the current browser session<span class="ansi-yellow-intense-fg ansi-bold">.</span>
<span class="ansi-green-fg">    332</span>         &#34;&#34;&#34;
<span class="ansi-green-intense-fg ansi-bold">--&gt; 333</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>execute<span class="ansi-yellow-intense-fg ansi-bold">(</span>Command<span class="ansi-yellow-intense-fg ansi-bold">.</span>GET<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">{</span><span class="ansi-blue-intense-fg ansi-bold">&#39;url&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">:</span> url<span class="ansi-yellow-intense-fg ansi-bold">}</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    334</span> 
<span class="ansi-green-fg">    335</span>     <span class="ansi-yellow-intense-fg ansi-bold">@</span>property

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py</span> in <span class="ansi-cyan-fg">execute</span><span class="ansi-blue-intense-fg ansi-bold">(self, driver_command, params)</span>
<span class="ansi-green-fg">    317</span> 
<span class="ansi-green-fg">    318</span>         params <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_wrap_value<span class="ansi-yellow-intense-fg ansi-bold">(</span>params<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 319</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>response <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>command_executor<span class="ansi-yellow-intense-fg ansi-bold">.</span>execute<span class="ansi-yellow-intense-fg ansi-bold">(</span>driver_command<span class="ansi-yellow-intense-fg ansi-bold">,</span> params<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    320</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> response<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    321</span>             self<span class="ansi-yellow-intense-fg ansi-bold">.</span>error_handler<span class="ansi-yellow-intense-fg ansi-bold">.</span>check_response<span class="ansi-yellow-intense-fg ansi-bold">(</span>response<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\selenium\webdriver\remote\remote_connection.py</span> in <span class="ansi-cyan-fg">execute</span><span class="ansi-blue-intense-fg ansi-bold">(self, command, params)</span>
<span class="ansi-green-fg">    372</span>         data <span class="ansi-yellow-intense-fg ansi-bold">=</span> utils<span class="ansi-yellow-intense-fg ansi-bold">.</span>dump_json<span class="ansi-yellow-intense-fg ansi-bold">(</span>params<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    373</span>         url <span class="ansi-yellow-intense-fg ansi-bold">=</span> <span class="ansi-blue-intense-fg ansi-bold">&#39;%s%s&#39;</span> <span class="ansi-yellow-intense-fg ansi-bold">%</span> <span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_url<span class="ansi-yellow-intense-fg ansi-bold">,</span> path<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 374</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_request<span class="ansi-yellow-intense-fg ansi-bold">(</span>command_info<span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">0</span><span class="ansi-yellow-intense-fg ansi-bold">]</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> body123<span class="ansi-yellow-intense-fg ansi-bold">=</span>data<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    375</span> 
<span class="ansi-green-fg">    376</span>     <span class="ansi-green-intense-fg ansi-bold">def</span> _request<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> body123<span class="ansi-yellow-intense-fg ansi-bold">=</span><span class="ansi-green-intense-fg ansi-bold">None</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>

<span class="ansi-green-intense-fg ansi-bold">~\Anaconda3\lib\site-packages\selenium\webdriver\remote\remote_connection.py</span> in <span class="ansi-cyan-fg">_request</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123)</span>
<span class="ansi-green-fg">    395</span> 
<span class="ansi-green-fg">    396</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>keep_alive<span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 397</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>resp <span class="ansi-yellow-intense-fg ansi-bold">=</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>_conn<span class="ansi-yellow-intense-fg ansi-bold">.</span>request<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> body123<span class="ansi-yellow-intense-fg ansi-bold">=</span>body123<span class="ansi-yellow-intense-fg ansi-bold">,</span> head123er123s<span class="ansi-yellow-intense-fg ansi-bold">=</span>head123er123s<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    398</span> 
<span class="ansi-green-fg">    399</span>             statuscode <span class="ansi-yellow-intense-fg ansi-bold">=</span> resp<span class="ansi-yellow-intense-fg ansi-bold">.</span>status

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\request.py</span> in <span class="ansi-cyan-fg">request</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, fields, head123er123s, **urlopen_kw)</span>
<span class="ansi-green-fg">     77</span>             )
<span class="ansi-green-fg">     78</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">---&gt; 79</span><span class="ansi-yellow-intense-fg ansi-bold">             return self.request_encode_body123(
</span><span class="ansi-green-fg">     80</span>                 method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> fields<span class="ansi-yellow-intense-fg ansi-bold">=</span>fields<span class="ansi-yellow-intense-fg ansi-bold">,</span> head123er123s<span class="ansi-yellow-intense-fg ansi-bold">=</span>head123er123s<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>urlopen_kw
<span class="ansi-green-fg">     81</span>             )

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\request.py</span> in <span class="ansi-cyan-fg">request_encode_body123</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, fields, head123er123s, encode_multipart, multipart_boundary, **urlopen_kw)</span>
<span class="ansi-green-fg">    169</span>         extra_kw<span class="ansi-yellow-intense-fg ansi-bold">.</span>update<span class="ansi-yellow-intense-fg ansi-bold">(</span>urlopen_kw<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    170</span> 
<span class="ansi-green-intense-fg ansi-bold">--&gt; 171</span><span class="ansi-yellow-intense-fg ansi-bold">         </span><span class="ansi-green-intense-fg ansi-bold">return</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>urlopen<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>extra_kw<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\poolmanager.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, redirect, **kw)</span>
<span class="ansi-green-fg">    334</span>             response <span class="ansi-yellow-intense-fg ansi-bold">=</span> conn<span class="ansi-yellow-intense-fg ansi-bold">.</span>urlopen<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kw<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    335</span>         <span class="ansi-green-intense-fg ansi-bold">else</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 336</span><span class="ansi-yellow-intense-fg ansi-bold">             </span>response <span class="ansi-yellow-intense-fg ansi-bold">=</span> conn<span class="ansi-yellow-intense-fg ansi-bold">.</span>urlopen<span class="ansi-yellow-intense-fg ansi-bold">(</span>method<span class="ansi-yellow-intense-fg ansi-bold">,</span> u<span class="ansi-yellow-intense-fg ansi-bold">.</span>request_uri<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kw<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    337</span> 
<span class="ansi-green-fg">    338</span>         redirect_location <span class="ansi-yellow-intense-fg ansi-bold">=</span> redirect <span class="ansi-green-intense-fg ansi-bold">and</span> response<span class="ansi-yellow-intense-fg ansi-bold">.</span>get_redirect_location<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body123_pos, **response_kw)</span>
<span class="ansi-green-fg">    752</span>                 <span class="ansi-blue-intense-fg ansi-bold">&#34;Retrying (%r) after connection broken by &#39;%r&#39;: %s&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> retries<span class="ansi-yellow-intense-fg ansi-bold">,</span> err<span class="ansi-yellow-intense-fg ansi-bold">,</span> url
<span class="ansi-green-fg">    753</span>             )
<span class="ansi-green-intense-fg ansi-bold">--&gt; 754</span><span class="ansi-yellow-intense-fg ansi-bold">             return self.urlopen(
</span><span class="ansi-green-fg">    755</span>                 method<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">    756</span>                 url<span class="ansi-yellow-intense-fg ansi-bold">,</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body123_pos, **response_kw)</span>
<span class="ansi-green-fg">    752</span>                 <span class="ansi-blue-intense-fg ansi-bold">&#34;Retrying (%r) after connection broken by &#39;%r&#39;: %s&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> retries<span class="ansi-yellow-intense-fg ansi-bold">,</span> err<span class="ansi-yellow-intense-fg ansi-bold">,</span> url
<span class="ansi-green-fg">    753</span>             )
<span class="ansi-green-intense-fg ansi-bold">--&gt; 754</span><span class="ansi-yellow-intense-fg ansi-bold">             return self.urlopen(
</span><span class="ansi-green-fg">    755</span>                 method<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">    756</span>                 url<span class="ansi-yellow-intense-fg ansi-bold">,</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body123_pos, **response_kw)</span>
<span class="ansi-green-fg">    752</span>                 <span class="ansi-blue-intense-fg ansi-bold">&#34;Retrying (%r) after connection broken by &#39;%r&#39;: %s&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> retries<span class="ansi-yellow-intense-fg ansi-bold">,</span> err<span class="ansi-yellow-intense-fg ansi-bold">,</span> url
<span class="ansi-green-fg">    753</span>             )
<span class="ansi-green-intense-fg ansi-bold">--&gt; 754</span><span class="ansi-yellow-intense-fg ansi-bold">             return self.urlopen(
</span><span class="ansi-green-fg">    755</span>                 method<span class="ansi-yellow-intense-fg ansi-bold">,</span>
<span class="ansi-green-fg">    756</span>                 url<span class="ansi-yellow-intense-fg ansi-bold">,</span>

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\connectionpool.py</span> in <span class="ansi-cyan-fg">urlopen</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, body123, head123er123s, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body123_pos, **response_kw)</span>
<span class="ansi-green-fg">    724</span>                 e <span class="ansi-yellow-intense-fg ansi-bold">=</span> ProtocolError<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;Connection aborted.&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> e<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    725</span> 
<span class="ansi-green-intense-fg ansi-bold">--&gt; 726</span><span class="ansi-yellow-intense-fg ansi-bold">             retries = retries.increment(
</span><span class="ansi-green-fg">    727</span>                 method<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> error<span class="ansi-yellow-intense-fg ansi-bold">=</span>e<span class="ansi-yellow-intense-fg ansi-bold">,</span> _pool<span class="ansi-yellow-intense-fg ansi-bold">=</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> _stacktrace<span class="ansi-yellow-intense-fg ansi-bold">=</span>sys<span class="ansi-yellow-intense-fg ansi-bold">.</span>exc_info<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">[</span><span class="ansi-cyan-intense-fg ansi-bold">2</span><span class="ansi-yellow-intense-fg ansi-bold">]</span>
<span class="ansi-green-fg">    728</span>             )

<span class="ansi-green-intense-fg ansi-bold">~\AppData\Roaming\Python\Python38\site-packages\urllib3\util\retry.py</span> in <span class="ansi-cyan-fg">increment</span><span class="ansi-blue-intense-fg ansi-bold">(self, method, url, response, error, _pool, _stacktrace)</span>
<span class="ansi-green-fg">    444</span> 
<span class="ansi-green-fg">    445</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> new_retry<span class="ansi-yellow-intense-fg ansi-bold">.</span>is_exhausted<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 446</span><span class="ansi-yellow-intense-fg ansi-bold">             </span><span class="ansi-green-intense-fg ansi-bold">raise</span> MaxRetryError<span class="ansi-yellow-intense-fg ansi-bold">(</span>_pool<span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> error <span class="ansi-green-intense-fg ansi-bold">or</span> ResponseError<span class="ansi-yellow-intense-fg ansi-bold">(</span>cause<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    447</span> 
<span class="ansi-green-fg">    448</span>         log<span class="ansi-yellow-intense-fg ansi-bold">.</span>debug<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-blue-intense-fg ansi-bold">&#34;Incremented Retry for (url=&#39;%s&#39;): %r&#34;</span><span class="ansi-yellow-intense-fg ansi-bold">,</span> url<span class="ansi-yellow-intense-fg ansi-bold">,</span> new_retry<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-red-intense-fg ansi-bold">MaxRetryError</span>: HTTPConnectionPool(host=&#39;127.0.0.1&#39;, port=5869): Max retries exceeded with url: /session/a5c4205de93790bd31a0d07d70fa340a/url (Caused by NewConnectionError(&#39;&lt;urllib3.connection.HTTPConnection object at 0x000001FBC3E8BC70&gt;: Failed to establish a new connection: [WinError 10061] Es konnte keine Verbindung hergestellt werden, da der Zielcomputer die Verbindung verweigerte&#39;))</pre>
</div>
</div>

</div>
</div>

</div>
 

