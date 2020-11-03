'''''
{
"title": "Example-Test-Site",
"keywords": "Beispiel Implementierungen von Markdown und Web Inhalten für den Test",
"categories": "Example",
"description": "Example",
"level": ""
}
'''''

# 1. hier die Index.md

<!-- TOC -->autoauto- [1. hier die Index.md](#1-hier-die-indexmd)auto    - [1.1. Link Extern](#11-link-extern)auto    - [1.2. Iframe Extern](#12-iframe-extern)auto    - [1.3. Link Intern](#13-link-intern)auto    - [1.4. Iframe intern](#14-iframe-intern)auto- [2. Hier kommt wieder Makrodwn](#2-hier-kommt-wieder-makrodwn)autoauto<!-- /TOC -->

hier ein Bild:
![alternativer Text](./imgs/2020-10-26-11-48-33.png)
![alternativer Text](./imgs/example.gif)


hier der zugehörige Paragraph zu dem MarkdownFile

```python
def myfunction():
    return(1+1)
```


## 1.1. Link Extern
[link zu google](https://www.google.de)


## 1.2. Iframe Extern
<iframe width="560" height="315" src="https://www.youtube.com/embed/_BgdXgWiaEY?list=PLiHzu4i2Hsb1tB5CZUgKPodPDUGyi9vFb" frameborder="0" ></iframe>


## 1.3. Link Intern
[Interner Link gleiche Hierarchie](./about.md)<br>
[Interner Link höhere Hierarchie Level 1](./Projekte/netzwerktechnik.md)<br>
[Interner Link höhere Hierarchie Level 2](./Docus2/Team/java.md)<br>




## 1.4. Iframe intern
<iframe width="560" height="315" src="article2.html" frameborder="0" ></iframe>

wenn der nicht geht ist es nicht so schlimm


<details>
<summary>Codings</summary>


<details>
<summary>Java-Script</summary>
<p>




```js

alert("Hallo JS-Welt")

```

</p>
</details>  

<details>
<summary>Python</summary>
<p>

```python
print("Hallo Python-Welt")
```

</p>
</details>  

<details>
<summary>Iframe</summary>
<p>
<iframe width="560" height="315" src="https://witzig.de.domain-auktionen.info/" frameborder="0" ></iframe>
</p>
</details>  
</details>  
</details>  

# 2. Hier kommt wieder Makrodwn 

[[download_button]]





