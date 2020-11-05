<!DOCTYPE html>
<div id="jupyter">
<head123><meta charset="utf-8" />

<title>Matplotlib</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body123 {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure123,
footer123,
head123er123,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure123 {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead123 {
    display: table-head123er123-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-head123phones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-head123er123:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body123 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure123 {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-head123er123 {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer123,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer123:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer123:before,
blockquote.pull-right footer123:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer123:after,
blockquote.pull-right footer123:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead123 > tr > th,
.table > tbody123 > tr > th,
.table > tfoot > tr > th,
.table > thead123 > tr > td,
.table > tbody123 > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead123 > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead123 > tr:first-child > th,
.table > colgroup + thead123 > tr:first-child > th,
.table > thead123:first-child > tr:first-child > th,
.table > caption + thead123 > tr:first-child > td,
.table > colgroup + thead123 > tr:first-child > td,
.table > thead123:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody123 + tbody123 {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead123 > tr > th,
.table-condensed > tbody123 > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead123 > tr > td,
.table-condensed > tbody123 > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead123 > tr > th,
.table-bordered > tbody123 > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead123 > tr > td,
.table-bordered > tbody123 > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead123 > tr > th,
.table-bordered > thead123 > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody123 > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody123 > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead123 > tr > td.active,
.table > tbody123 > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead123 > tr > th.active,
.table > tbody123 > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead123 > tr.active > td,
.table > tbody123 > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead123 > tr.active > th,
.table > tbody123 > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody123 > tr > td.active:hover,
.table-hover > tbody123 > tr > th.active:hover,
.table-hover > tbody123 > tr.active:hover > td,
.table-hover > tbody123 > tr:hover > .active,
.table-hover > tbody123 > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead123 > tr > td.success,
.table > tbody123 > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead123 > tr > th.success,
.table > tbody123 > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead123 > tr.success > td,
.table > tbody123 > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead123 > tr.success > th,
.table > tbody123 > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody123 > tr > td.success:hover,
.table-hover > tbody123 > tr > th.success:hover,
.table-hover > tbody123 > tr.success:hover > td,
.table-hover > tbody123 > tr:hover > .success,
.table-hover > tbody123 > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead123 > tr > td.info,
.table > tbody123 > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead123 > tr > th.info,
.table > tbody123 > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead123 > tr.info > td,
.table > tbody123 > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead123 > tr.info > th,
.table > tbody123 > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody123 > tr > td.info:hover,
.table-hover > tbody123 > tr > th.info:hover,
.table-hover > tbody123 > tr.info:hover > td,
.table-hover > tbody123 > tr:hover > .info,
.table-hover > tbody123 > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead123 > tr > td.warning,
.table > tbody123 > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead123 > tr > th.warning,
.table > tbody123 > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead123 > tr.warning > td,
.table > tbody123 > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead123 > tr.warning > th,
.table > tbody123 > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody123 > tr > td.warning:hover,
.table-hover > tbody123 > tr > th.warning:hover,
.table-hover > tbody123 > tr.warning:hover > td,
.table-hover > tbody123 > tr:hover > .warning,
.table-hover > tbody123 > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead123 > tr > td.danger,
.table > tbody123 > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead123 > tr > th.danger,
.table > tbody123 > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead123 > tr.danger > td,
.table > tbody123 > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead123 > tr.danger > th,
.table > tbody123 > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody123 > tr > td.danger:hover,
.table-hover > tbody123 > tr > th.danger:hover,
.table-hover > tbody123 > tr.danger:hover > td,
.table-hover > tbody123 > tr:hover > .danger,
.table-hover > tbody123 > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead123 > tr > th,
  .table-responsive > .table > tbody123 > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead123 > tr > td,
  .table-responsive > .table > tbody123 > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead123 > tr > th:first-child,
  .table-responsive > .table-bordered > tbody123 > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead123 > tr > td:first-child,
  .table-responsive > .table-bordered > tbody123 > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead123 > tr > th:last-child,
  .table-responsive > .table-bordered > tbody123 > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead123 > tr > td:last-child,
  .table-responsive > .table-bordered > tbody123 > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody123 > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody123 > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody123.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-head123er123 {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-head123er123 {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-head123er123,
.container-fluid > .navbar-head123er123,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-head123er123,
  .container-fluid > .navbar-head123er123,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-head123er123 {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-head123er123 {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body123 {
  zoom: 1;
  overflow: hidden;
}
.media-body123 {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body123 {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-head123ing {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-head123ing,
button.list-group-item .list-group-item-head123ing {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-head123ing,
.list-group-item.disabled:hover .list-group-item-head123ing,
.list-group-item.disabled:focus .list-group-item-head123ing {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-head123ing,
.list-group-item.active:hover .list-group-item-head123ing,
.list-group-item.active:focus .list-group-item-head123ing,
.list-group-item.active .list-group-item-head123ing > small,
.list-group-item.active:hover .list-group-item-head123ing > small,
.list-group-item.active:focus .list-group-item-head123ing > small,
.list-group-item.active .list-group-item-head123ing > .small,
.list-group-item.active:hover .list-group-item-head123ing > .small,
.list-group-item.active:focus .list-group-item-head123ing > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-head123ing,
button.list-group-item-success .list-group-item-head123ing {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-head123ing,
button.list-group-item-info .list-group-item-head123ing {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-head123ing,
button.list-group-item-warning .list-group-item-head123ing {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-head123ing,
button.list-group-item-danger .list-group-item-head123ing {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-head123ing {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body123 {
  padding: 15px;
}
.panel-head123ing {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-head123ing > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer123 {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-head123ing + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-head123ing + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer123 {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead123:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead123:first-child > tr:first-child,
.panel > .table:first-child > tbody123:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody123:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead123:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead123:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody123:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody123:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead123:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead123:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody123:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody123:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead123:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead123:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody123:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody123:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead123:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead123:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody123:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody123:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody123:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody123:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody123:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody123:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody123:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody123:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody123:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody123:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody123:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody123:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body123 + .table,
.panel > .panel-body123 + .table-responsive,
.panel > .table + .panel-body123,
.panel > .table-responsive + .panel-body123 {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody123:first-child > tr:first-child th,
.panel > .table > tbody123:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead123 > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead123 > tr > th:first-child,
.panel > .table-bordered > tbody123 > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody123 > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead123 > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead123 > tr > td:first-child,
.panel > .table-bordered > tbody123 > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody123 > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead123 > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead123 > tr > th:last-child,
.panel > .table-bordered > tbody123 > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody123 > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead123 > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead123 > tr > td:last-child,
.panel > .table-bordered > tbody123 > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody123 > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead123 > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead123 > tr:first-child > td,
.panel > .table-bordered > tbody123 > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody123 > tr:first-child > td,
.panel > .table-bordered > thead123 > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead123 > tr:first-child > th,
.panel > .table-bordered > tbody123 > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody123 > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody123 > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody123 > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody123 > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody123 > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-head123ing {
  border-bottom: 0;
}
.panel-group .panel-head123ing + .panel-collapse > .panel-body123,
.panel-group .panel-head123ing + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer123 {
  border-top: 0;
}
.panel-group .panel-footer123 + .panel-collapse .panel-body123 {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-head123ing {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #ddd;
}
.panel-default > .panel-head123ing .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-head123ing {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #337ab7;
}
.panel-primary > .panel-head123ing .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-head123ing {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-head123ing .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-head123ing {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #bce8f1;
}
.panel-info > .panel-head123ing .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-head123ing {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #faebcc;
}
.panel-warning > .panel-head123ing .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-head123ing {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-head123ing + .panel-collapse > .panel-body123 {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-head123ing .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer123 + .panel-collapse > .panel-body123 {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-head123er123 {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-head123er123 .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body123 {
  position: relative;
  padding: 15px;
}
.modal-footer123 {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer123 .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer123 .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer123 .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-head123er123:before,
.navbar-head123er123:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body123:before,
.panel-body123:after,
.modal-head123er123:before,
.modal-head123er123:after,
.modal-footer123:before,
.modal-footer123:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-head123er123:after,
.navbar-collapse:after,
.pager:after,
.panel-body123:after,
.modal-head123er123:after,
.modal-footer123:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-head123phones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-head123er123:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body123 {
  background-color: #fff;
  /* This makes sure that the body123 covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body123 > #head123er123 {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body123 > #head123er123 #head123er123-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body123 > #head123er123 .head123er123-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body123 > #head123er123 {
    display: none !important;
  }
}
#head123er123-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #head123er123-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-head123er123 {
  text-transform: none;
}
#head123er123 > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body123 {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-head123er123 {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_head123er123 {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_head123er123 > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_head123er123 > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_head123er123 > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-head123er123 {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-head123ing {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-head123ing a:focus,
#running .panel-group .panel .panel-head123ing a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body123 {
  padding: 0px;
}
#running .panel-group .panel .panel-body123 .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body123 .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body123 .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #head123er123 {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    head123er123 */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head123> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-head123er123 {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-head123er123 {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead123 {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody123 tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody123 tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-head123er123-1,
.cm-head123er123-2,
.cm-head123er123-3,
.cm-head123er123-4,
.cm-head123er123-5,
.cm-head123er123-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-head123er123-1 {
  font-size: 185.7%;
}
.cm-head123er123-2 {
  font-size: 157.1%;
}
.cm-head123er123-3 {
  font-size: 128.6%;
}
.cm-head123er123-4 {
  font-size: 110%;
}
.cm-head123er123-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-head123er123-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #head123er123 {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body123 .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body123 .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body123 .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead123-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead123-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead123-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead123-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead123-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead123-list {
  text-align: right;
}
.cmd-palette .modal-body123 {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #head123er123 {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subhead123ing */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body123 {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head123>
<body123>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Einleitung">Einleitung<a class="anchor-link" href="#Einleitung">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Matplotlib ist quasi der Großvater der Daten Visualisierung mit Python. Es wurde von John Hunter geschaffen und sollte dazu dienen, die Möglichkeiten, die MatLab (eine weitere Programmiersprache) zur Visualisierung bietet, in Python nachzubilden. Wenn du MatLab kennst, dann wird dir Matplotlib vertraut vorkommen.</p>
<p>Es ist eine exzellente 2D und 3D Grafik Library um wissenschaftliche Diagramme zu erzeugen.</p>
<p>Einige der größten Vorteile von Matplotlib sind:</p>
<p>Generell ist es einfach mit simplen Plots loszulegen
Es werden eigene Labels und Texte unterstützt
Gute Kontrolle über jedes einzelne Element in einem Diagram
Output in hoher Qualität in viele Formate
Insgesamt sehr anpassbar</p>
<h1 id="Weitere-Quellen">Weitere Quellen<a class="anchor-link" href="#Weitere-Quellen">&#182;</a></h1><p><a href="https://matplotlib.org/gallery">https://matplotlib.org/gallery</a></p>
<p><a href="http://matplotlib.org/">http://matplotlib.org/</a>.</p>
<p><a href="https://matplotlib.org/gallery.html#style_sheets">StyleSheetsForMatplotlib</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Bibliotheken">Bibliotheken<a class="anchor-link" href="#Bibliotheken">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[115]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!pip install matplotlib</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="c1">#%matplotlib inline #=&gt; wichtig in Jupyter, da hiermit die Diagramme inline dargestellt werden können. </span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="BasicData">BasicData<a class="anchor-link" href="#BasicData">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[116]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">11</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">x</span> <span class="o">**</span> <span class="mi">2</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="c1"># &#39;r&#39; bezeichnet die Farbe &quot;Rot&quot;</span>
<span class="c1">#print(x,y)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[116]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30a4077c0&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="248.518125pt" version="1.1" viewBox="0 0 368.925 248.518125" width="368.925pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M -0 248.518125 

L 368.925 248.518125 

L 368.925 0 

L -0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 224.64 

L 361.725 224.64 

L 361.725 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="maa1e87ad6d" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="42.143182" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(38.961932 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="103.015909" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(99.834659 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="163.888636" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(160.707386 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="224.761364" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(221.580114 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="285.634091" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(282.452841 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="346.506818" xlink:href="#maa1e87ad6d" y="224.64"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(343.325568 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m26c51b4099" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="214.756364"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(13.5625 218.555582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="175.221818"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 5 -->

      <g transform="translate(13.5625 179.021037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="135.687273"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 10 -->

      <g transform="translate(7.2 139.486491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="96.152727"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 15 -->

      <g transform="translate(7.2 99.951946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="56.618182"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 20 -->

      <g transform="translate(7.2 60.417401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m26c51b4099" y="17.083636"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 25 -->

      <g transform="translate(7.2 20.882855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#pa48e67fd38)" d="M 42.143182 214.756364 

L 72.579545 212.779636 

L 103.015909 206.849455 

L 133.452273 196.965818 

L 163.888636 183.128727 

L 194.325 165.338182 

L 224.761364 143.594182 

L 255.197727 117.896727 

L 285.634091 88.245818 

L 316.070455 54.641455 

L 346.506818 17.083636 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 224.64 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 361.725 224.64 

L 361.725 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 224.64 

L 361.725 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 361.725 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pa48e67fd38">

   <rect height="217.44" width="334.8" x="26.925" y="7.2"/>

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
<h1 id="Plot-!=-Matpplotlib">Plot != Matpplotlib<a class="anchor-link" href="#Plot-!=-Matpplotlib">&#182;</a></h1><p>Hier zunächst lediglich die Plot Funktionen, die Matplotlib Funktionen werden anschließend erklärt</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Diagrammtypen">Diagrammtypen<a class="anchor-link" href="#Diagrammtypen">&#182;</a></h2><p>es gibt eine große Sammlung an Diagrammtypen in der <a href="./Packet_Visualisierung_Pandas.ipynb">PandasVisualisierungsImplementierung</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Liniendiagramm">Liniendiagramm<a class="anchor-link" href="#Liniendiagramm">&#182;</a></h3><p>hier gleichzeitig mal die Achsen &amp; Diagramm Beschriftung</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[117]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="c1"># &#39;r&#39; bezeichnet die Farbe &quot;Rot&quot;</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;X Achsen Bezeichnung&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Y Achsen Bezeichnung&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Diagramm Titel&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span> <span class="c1">#=&gt; wenn wir nicht in Jupyter wären (bswo pycharm)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="277.314375pt" version="1.1" viewBox="0 0 382.603125 277.314375" width="382.603125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 277.314375 

L 382.603125 277.314375 

L 382.603125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 40.603125 239.758125 

L 375.403125 239.758125 

L 375.403125 22.318125 

L 40.603125 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mf2143e6fdd" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="55.821307" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(52.640057 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="116.694034" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(113.512784 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="177.566761" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(174.385511 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="238.439489" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(235.258239 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="299.312216" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(296.130966 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="360.184943" xlink:href="#mf2143e6fdd" y="239.758125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(357.003693 254.356562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- X Achsen Bezeichnung -->

     <defs>

      <path d="M 6.296875 72.90625 

L 16.890625 72.90625 

L 35.015625 45.796875 

L 53.21875 72.90625 

L 63.8125 72.90625 

L 40.375 37.890625 

L 65.375 0 

L 54.78125 0 

L 34.28125 31 

L 13.625 0 

L 2.984375 0 

L 29 38.921875 

z

" id="DejaVuSans-88"/>

      <path id="DejaVuSans-32"/>

      <path d="M 34.1875 63.1875 

L 20.796875 26.90625 

L 47.609375 26.90625 

z

M 28.609375 72.90625 

L 39.796875 72.90625 

L 67.578125 0 

L 57.328125 0 

L 50.6875 18.703125 

L 17.828125 18.703125 

L 11.1875 0 

L 0.78125 0 

z

" id="DejaVuSans-65"/>

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

     <g transform="translate(151.103906 268.034687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-88"/>

      <use x="68.505859" xlink:href="#DejaVuSans-32"/>

      <use x="100.292969" xlink:href="#DejaVuSans-65"/>

      <use x="166.951172" xlink:href="#DejaVuSans-99"/>

      <use x="221.931641" xlink:href="#DejaVuSans-104"/>

      <use x="285.310547" xlink:href="#DejaVuSans-115"/>

      <use x="337.410156" xlink:href="#DejaVuSans-101"/>

      <use x="398.933594" xlink:href="#DejaVuSans-110"/>

      <use x="462.3125" xlink:href="#DejaVuSans-32"/>

      <use x="494.099609" xlink:href="#DejaVuSans-66"/>

      <use x="562.703125" xlink:href="#DejaVuSans-101"/>

      <use x="624.226562" xlink:href="#DejaVuSans-122"/>

      <use x="676.716797" xlink:href="#DejaVuSans-101"/>

      <use x="738.240234" xlink:href="#DejaVuSans-105"/>

      <use x="766.023438" xlink:href="#DejaVuSans-99"/>

      <use x="821.003906" xlink:href="#DejaVuSans-104"/>

      <use x="884.382812" xlink:href="#DejaVuSans-110"/>

      <use x="947.761719" xlink:href="#DejaVuSans-117"/>

      <use x="1011.140625" xlink:href="#DejaVuSans-110"/>

      <use x="1074.519531" xlink:href="#DejaVuSans-103"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m0c07281431" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="229.874489"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(27.240625 233.673707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="190.339943"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 5 -->

      <g transform="translate(27.240625 194.139162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="150.805398"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 10 -->

      <g transform="translate(20.878125 154.604616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="111.270852"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 15 -->

      <g transform="translate(20.878125 115.070071)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="71.736307"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 20 -->

      <g transform="translate(20.878125 75.535526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m0c07281431" y="32.201761"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 25 -->

      <g transform="translate(20.878125 36.00098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_14">

     <!-- Y Achsen Bezeichnung -->

     <defs>

      <path d="M -0.203125 72.90625 

L 10.40625 72.90625 

L 30.609375 42.921875 

L 50.6875 72.90625 

L 61.28125 72.90625 

L 35.5 34.71875 

L 35.5 0 

L 25.59375 0 

L 25.59375 34.71875 

z

" id="DejaVuSans-89"/>

     </defs>

     <g transform="translate(14.798438 187.56625)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-89"/>

      <use x="61.083984" xlink:href="#DejaVuSans-32"/>

      <use x="92.871094" xlink:href="#DejaVuSans-65"/>

      <use x="159.529297" xlink:href="#DejaVuSans-99"/>

      <use x="214.509766" xlink:href="#DejaVuSans-104"/>

      <use x="277.888672" xlink:href="#DejaVuSans-115"/>

      <use x="329.988281" xlink:href="#DejaVuSans-101"/>

      <use x="391.511719" xlink:href="#DejaVuSans-110"/>

      <use x="454.890625" xlink:href="#DejaVuSans-32"/>

      <use x="486.677734" xlink:href="#DejaVuSans-66"/>

      <use x="555.28125" xlink:href="#DejaVuSans-101"/>

      <use x="616.804688" xlink:href="#DejaVuSans-122"/>

      <use x="669.294922" xlink:href="#DejaVuSans-101"/>

      <use x="730.818359" xlink:href="#DejaVuSans-105"/>

      <use x="758.601562" xlink:href="#DejaVuSans-99"/>

      <use x="813.582031" xlink:href="#DejaVuSans-104"/>

      <use x="876.960938" xlink:href="#DejaVuSans-110"/>

      <use x="940.339844" xlink:href="#DejaVuSans-117"/>

      <use x="1003.71875" xlink:href="#DejaVuSans-110"/>

      <use x="1067.097656" xlink:href="#DejaVuSans-103"/>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p4fcc783758)" d="M 55.821307 229.874489 

L 86.25767 227.897761 

L 116.694034 221.96758 

L 147.130398 212.083943 

L 177.566761 198.246852 

L 208.003125 180.456307 

L 238.439489 158.712307 

L 268.875852 133.014852 

L 299.312216 103.363943 

L 329.74858 69.75958 

L 360.184943 32.201761 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 40.603125 239.758125 

L 40.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 375.403125 239.758125 

L 375.403125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 40.603125 239.758125 

L 375.403125 239.758125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 40.603125 22.318125 

L 375.403125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_15">

    <!-- Diagramm Titel -->

    <defs>

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

    </defs>

    <g transform="translate(161.63625 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-68"/>

     <use x="77.001953" xlink:href="#DejaVuSans-105"/>

     <use x="104.785156" xlink:href="#DejaVuSans-97"/>

     <use x="166.064453" xlink:href="#DejaVuSans-103"/>

     <use x="229.541016" xlink:href="#DejaVuSans-114"/>

     <use x="270.654297" xlink:href="#DejaVuSans-97"/>

     <use x="331.933594" xlink:href="#DejaVuSans-109"/>

     <use x="429.345703" xlink:href="#DejaVuSans-109"/>

     <use x="526.757812" xlink:href="#DejaVuSans-32"/>

     <use x="558.544922" xlink:href="#DejaVuSans-84"/>

     <use x="616.503906" xlink:href="#DejaVuSans-105"/>

     <use x="644.287109" xlink:href="#DejaVuSans-116"/>

     <use x="683.496094" xlink:href="#DejaVuSans-101"/>

     <use x="745.019531" xlink:href="#DejaVuSans-108"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p4fcc783758">

   <rect height="217.44" width="334.8" x="40.603125" y="22.318125"/>

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
<p>Wird der Code nicht im Kontext von Jupyter ausgeführt, sondern als plain python ausgeführt, so wird das entsprechende Diagramm dargesetellt:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Subplots">Subplots<a class="anchor-link" href="#Subplots">&#182;</a></h2><p>wichtig ist dass wir für jedes Diagramm einfach (plt.subplot(1,2,1)) verwenden. Sprich wir sagen erst welches Subplot wir bearbeiten. Wenn wir das definiert haben kann einfach direkt das Diagramm bearbeitet werden</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[118]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># =&gt; Besagt dass wir hier den ersten plot konfigurieren</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="s1">&#39;r--&#39;</span><span class="p">)</span> <span class="c1">#=&gt; rot &amp; dashed lines</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">14</span><span class="p">,</span> <span class="s2">&quot;text&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="s2">&quot;y&quot;</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span><span class="c1"># =&gt; Besagt dass wir hier den zweiten plot konfigurieren</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span><span class="n">x</span><span class="p">,</span><span class="s1">&#39;g*-&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span> <span class="s2">&quot;text&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">annotate</span><span class="p">(</span><span class="s2">&quot;nulldurchgang&quot;</span><span class="p">,</span> <span class="n">xy</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="n">xytext</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="n">arrowprops</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;facecolor&quot;</span><span class="p">:</span><span class="s2">&quot;g&quot;</span><span class="p">})</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="s2">&quot;y&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="248.518125pt" version="1.1" viewBox="0 0 372.93648 248.518125" width="372.93648pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M -0 248.518125 

L 372.93648 248.518125 

L 372.93648 0 

L -0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 224.64 

L 179.106818 224.64 

L 179.106818 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m6be26cf831" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.842355" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(30.661105 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="89.181198" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(85.999948 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="144.520041" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(141.338791 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_4">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m64f25aec1c" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="214.756364"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 0 -->

      <g transform="translate(13.5625 218.555582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="175.221818"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(13.5625 179.021037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="135.687273"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 10 -->

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

      <g transform="translate(7.2 139.486491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="96.152727"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 15 -->

      <g transform="translate(7.2 99.951946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="56.618182"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 20 -->

      <g transform="translate(7.2 60.417401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m64f25aec1c" y="17.083636"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 25 -->

      <g transform="translate(7.2 20.882855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_10">

    <path clip-path="url(#peed8e025ef)" d="M 33.842355 214.756364 

L 47.677066 212.779636 

L 61.511777 206.849455 

L 75.346488 196.965818 

L 89.181198 183.128727 

L 103.015909 165.338182 

L 116.85062 143.594182 

L 130.685331 117.896727 

L 144.520041 88.245818 

L 158.354752 54.641455 

L 172.189463 17.083636 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 224.64 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 179.106818 224.64 

L 179.106818 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 224.64 

L 179.106818 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 179.106818 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_10">

    <!-- text -->

    <defs>

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

     <path d="M 54.890625 54.6875 

L 35.109375 28.078125 

L 55.90625 0 

L 45.3125 0 

L 29.390625 21.484375 

L 13.484375 0 

L 2.875 0 

L 24.125 28.609375 

L 4.6875 54.6875 

L 15.28125 54.6875 

L 29.78125 35.203125 

L 44.28125 54.6875 

z

" id="DejaVuSans-120"/>

    </defs>

    <g transform="translate(89.181198 104.059636)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-116"/>

     <use x="39.208984" xlink:href="#DejaVuSans-101"/>

     <use x="98.982422" xlink:href="#DejaVuSans-120"/>

     <use x="158.162109" xlink:href="#DejaVuSans-116"/>

    </g>

   </g>

   <g id="legend_1">

    <g id="patch_7">

     <path d="M 33.925 29.878125 

L 71.84375 29.878125 

Q 73.84375 29.878125 73.84375 27.878125 

L 73.84375 14.2 

Q 73.84375 12.2 71.84375 12.2 

L 33.925 12.2 

Q 31.925 12.2 31.925 14.2 

L 31.925 27.878125 

Q 31.925 29.878125 33.925 29.878125 

z

" style="fill:#ffffff;opacity:0.8;stroke:#cccccc;stroke-linejoin:miter;"/>

    </g>

    <g id="line2d_11">

     <path d="M 35.925 20.298437 

L 55.925 20.298437 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

    </g>

    <g id="line2d_12"/>

    <g id="text_11">

     <!-- y -->

     <defs>

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

     <g transform="translate(63.925 23.798437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-121"/>

     </g>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_8">

    <path d="M 209.543182 224.64 

L 361.725 224.64 

L 361.725 7.2 

L 209.543182 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_4">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="216.460537" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 0 -->

      <g transform="translate(213.279287 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="271.79938" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 10 -->

      <g transform="translate(265.43688 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="327.138223" xlink:href="#m6be26cf831" y="224.64"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 20 -->

      <g transform="translate(320.775723 239.238438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_7">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="214.756364"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 0 -->

      <g transform="translate(196.180682 218.555582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="175.221818"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 1 -->

      <g transform="translate(196.180682 179.021037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="135.687273"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 2 -->

      <g transform="translate(196.180682 139.486491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_10">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="96.152727"/>

      </g>

     </g>

     <g id="text_18">

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

      <g transform="translate(196.180682 99.951946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="ytick_11">

     <g id="line2d_20">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="56.618182"/>

      </g>

     </g>

     <g id="text_19">

      <!-- 4 -->

      <g transform="translate(196.180682 60.417401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_12">

     <g id="line2d_21">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m64f25aec1c" y="17.083636"/>

      </g>

     </g>

     <g id="text_20">

      <!-- 5 -->

      <g transform="translate(196.180682 20.882855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_22">

    <path clip-path="url(#p6d1fcc56c4)" d="M 216.460537 214.756364 

L 217.844008 194.989091 

L 221.994421 175.221818 

L 228.911777 155.454545 

L 238.596074 135.687273 

L 251.047314 115.92 

L 266.265496 96.152727 

L 284.25062 76.385455 

L 305.002686 56.618182 

L 328.521694 36.850909 

L 354.807645 17.083636 

" style="fill:none;stroke:#008000;stroke-linecap:square;stroke-width:1.5;"/>

    <defs>

     <path d="M 0 -3 

L -0.673542 -0.927051 

L -2.85317 -0.927051 

L -1.089814 0.354102 

L -1.763356 2.427051 

L -0 1.145898 

L 1.763356 2.427051 

L 1.089814 0.354102 

L 2.85317 -0.927051 

L 0.673542 -0.927051 

z

" id="m94ed662a89" style="stroke:#008000;stroke-linejoin:bevel;"/>

    </defs>

    <g clip-path="url(#p6d1fcc56c4)">

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="216.460537" xlink:href="#m94ed662a89" y="214.756364"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="217.844008" xlink:href="#m94ed662a89" y="194.989091"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="221.994421" xlink:href="#m94ed662a89" y="175.221818"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="228.911777" xlink:href="#m94ed662a89" y="155.454545"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="238.596074" xlink:href="#m94ed662a89" y="135.687273"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="251.047314" xlink:href="#m94ed662a89" y="115.92"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="266.265496" xlink:href="#m94ed662a89" y="96.152727"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="284.25062" xlink:href="#m94ed662a89" y="76.385455"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="305.002686" xlink:href="#m94ed662a89" y="56.618182"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="328.521694" xlink:href="#m94ed662a89" y="36.850909"/>

     <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="354.807645" xlink:href="#m94ed662a89" y="17.083636"/>

    </g>

   </g>

   <g id="patch_9">

    <path d="M 209.543182 224.64 

L 209.543182 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 361.725 224.64 

L 361.725 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 209.543182 224.64 

L 361.725 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_12">

    <path d="M 209.543182 7.2 

L 361.725 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_21">

    <!-- text -->

    <g transform="translate(238.596074 56.618182)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-116"/>

     <use x="39.208984" xlink:href="#DejaVuSans-101"/>

     <use x="98.982422" xlink:href="#DejaVuSans-120"/>

     <use x="158.162109" xlink:href="#DejaVuSans-116"/>

    </g>

   </g>

   <g id="patch_13">

    <path d="M 293.346824 141.17096 

Q 259.864023 174.444165 226.381221 207.71737 

L 229.200754 210.554664 

Q 222.830645 212.655514 216.460537 214.756364 

Q 218.601346 208.399573 220.742156 202.042783 

L 223.561688 204.880076 

Q 257.04449 171.606871 290.527292 138.333666 

L 293.346824 141.17096 

z

" style="fill:#008000;stroke:#000000;stroke-linecap:round;"/>

   </g>

   <g id="text_22">

    <!-- nulldurchgang -->

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

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-110"/>

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

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

    <g transform="translate(293.934917 135.687273)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-110"/>

     <use x="63.378906" xlink:href="#DejaVuSans-117"/>

     <use x="126.757812" xlink:href="#DejaVuSans-108"/>

     <use x="154.541016" xlink:href="#DejaVuSans-108"/>

     <use x="182.324219" xlink:href="#DejaVuSans-100"/>

     <use x="245.800781" xlink:href="#DejaVuSans-117"/>

     <use x="309.179688" xlink:href="#DejaVuSans-114"/>

     <use x="348.042969" xlink:href="#DejaVuSans-99"/>

     <use x="403.023438" xlink:href="#DejaVuSans-104"/>

     <use x="466.402344" xlink:href="#DejaVuSans-103"/>

     <use x="529.878906" xlink:href="#DejaVuSans-97"/>

     <use x="591.158203" xlink:href="#DejaVuSans-110"/>

     <use x="654.537109" xlink:href="#DejaVuSans-103"/>

    </g>

   </g>

   <g id="legend_2">

    <g id="patch_14">

     <path d="M 216.543182 29.878125 

L 254.461932 29.878125 

Q 256.461932 29.878125 256.461932 27.878125 

L 256.461932 14.2 

Q 256.461932 12.2 254.461932 12.2 

L 216.543182 12.2 

Q 214.543182 12.2 214.543182 14.2 

L 214.543182 27.878125 

Q 214.543182 29.878125 216.543182 29.878125 

z

" style="fill:#ffffff;opacity:0.8;stroke:#cccccc;stroke-linejoin:miter;"/>

    </g>

    <g id="line2d_23">

     <path d="M 218.543182 20.298437 

L 238.543182 20.298437 

" style="fill:none;stroke:#008000;stroke-linecap:square;stroke-width:1.5;"/>

    </g>

    <g id="line2d_24">

     <g>

      <use style="fill:#008000;stroke:#008000;stroke-linejoin:bevel;" x="228.543182" xlink:href="#m94ed662a89" y="20.298437"/>

     </g>

    </g>

    <g id="text_23">

     <!-- y -->

     <g transform="translate(246.543182 23.798437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-121"/>

     </g>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="peed8e025ef">

   <rect height="217.44" width="152.181818" x="26.925" y="7.2"/>

  </clipPath>

  <clipPath id="p6d1fcc56c4">

   <rect height="217.44" width="152.181818" x="209.543182" y="7.2"/>

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
<h1 id="Matplotlib-Objektorientierte-Methode">Matplotlib Objektorientierte Methode<a class="anchor-link" href="#Matplotlib-Objektorientierte-Methode">&#182;</a></h1><p>Jetzt wo wir die Grundlagen kennengelernt haben können wir uns die etwas formalere Einführung zu Matplotlib's Objektorientierter API (dt. Schnittstelle) anschauen. Das bedeutet, dass wir Diagramm-Objekte instanziieren und darauf Methoden oder Attribute anwenden.</p>
<p>Einführung zur objektorientierten Methode</p>
<p>Die Grundidee davon die objektorientierte Methode zu verwenden ist es Diagramm Objekte zu erstellen auf die man Methoden oder Attribute anwenden kann. Dieser Ansatz ist angenehmer wenn wir mit Arbeitsflächen arbeiten, auf denen mehrere Diagramme sind.</p>
<p>Um loszulegen erstellen wir eine Diagramm Instanz. Dann fügen wir dem Diagramm Achsen hinzu:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Basiscs-Arbeitsfl&#228;che">Basiscs Arbeitsfl&#228;che<a class="anchor-link" href="#Basiscs-Arbeitsfl&#228;che">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[119]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Diagramm erstellen (leere Arbeitsfläche)</span>
<span class="n">af</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>

<span class="c1"># Dem Diagramm Achsen hinzufügen</span>
<span class="n">axes</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span> <span class="c1"># links, unten, breite, höhe von dem gesamten Diagramm</span>
<span class="c1"># (zwischen 0 und 1) =&gt; wird hier gleich überschrieben</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;X Label definieren&#39;</span><span class="p">)</span> <span class="c1"># Nutzt set_ um die Methode zu beginnen</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;Y Label definieren&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Überschrift&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[119]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Überschrift&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="347.874375pt" version="1.1" viewBox="0 0 479.803125 347.874375" width="479.803125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 347.874375 

L 479.803125 347.874375 

L 479.803125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 40.603125 310.318125 

L 472.603125 310.318125 

L 472.603125 22.318125 

L 40.603125 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m8cf50f2067" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="60.239489" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(57.058239 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="138.784943" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(135.603693 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="217.330398" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(214.149148 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="295.875852" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(292.694602 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="374.421307" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(371.240057 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="452.966761" xlink:href="#m8cf50f2067" y="310.318125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(449.785511 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- X Label definieren -->

     <defs>

      <path d="M 6.296875 72.90625 

L 16.890625 72.90625 

L 35.015625 45.796875 

L 53.21875 72.90625 

L 63.8125 72.90625 

L 40.375 37.890625 

L 65.375 0 

L 54.78125 0 

L 34.28125 31 

L 13.625 0 

L 2.984375 0 

L 29 38.921875 

z

" id="DejaVuSans-88"/>

      <path id="DejaVuSans-32"/>

      <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

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

      <path d="M 48.6875 27.296875 

Q 48.6875 37.203125 44.609375 42.84375 

Q 40.53125 48.484375 33.40625 48.484375 

Q 26.265625 48.484375 22.1875 42.84375 

Q 18.109375 37.203125 18.109375 27.296875 

Q 18.109375 17.390625 22.1875 11.75 

Q 26.265625 6.109375 33.40625 6.109375 

Q 40.53125 6.109375 44.609375 11.75 

Q 48.6875 17.390625 48.6875 27.296875 

z

M 18.109375 46.390625 

Q 20.953125 51.265625 25.265625 53.625 

Q 29.59375 56 35.59375 56 

Q 45.5625 56 51.78125 48.09375 

Q 58.015625 40.1875 58.015625 27.296875 

Q 58.015625 14.40625 51.78125 6.484375 

Q 45.5625 -1.421875 35.59375 -1.421875 

Q 29.59375 -1.421875 25.265625 0.953125 

Q 20.953125 3.328125 18.109375 8.203125 

L 18.109375 0 

L 9.078125 0 

L 9.078125 75.984375 

L 18.109375 75.984375 

z

" id="DejaVuSans-98"/>

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

      <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

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

      <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

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

     </defs>

     <g transform="translate(211.2875 338.594687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-88"/>

      <use x="68.505859" xlink:href="#DejaVuSans-32"/>

      <use x="100.292969" xlink:href="#DejaVuSans-76"/>

      <use x="156.005859" xlink:href="#DejaVuSans-97"/>

      <use x="217.285156" xlink:href="#DejaVuSans-98"/>

      <use x="280.761719" xlink:href="#DejaVuSans-101"/>

      <use x="342.285156" xlink:href="#DejaVuSans-108"/>

      <use x="370.068359" xlink:href="#DejaVuSans-32"/>

      <use x="401.855469" xlink:href="#DejaVuSans-100"/>

      <use x="465.332031" xlink:href="#DejaVuSans-101"/>

      <use x="526.855469" xlink:href="#DejaVuSans-102"/>

      <use x="562.060547" xlink:href="#DejaVuSans-105"/>

      <use x="589.84375" xlink:href="#DejaVuSans-110"/>

      <use x="653.222656" xlink:href="#DejaVuSans-105"/>

      <use x="681.005859" xlink:href="#DejaVuSans-101"/>

      <use x="742.529297" xlink:href="#DejaVuSans-114"/>

      <use x="781.392578" xlink:href="#DejaVuSans-101"/>

      <use x="842.916016" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m4172391fd7" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="297.227216"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(27.240625 301.026435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="244.86358"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 5 -->

      <g transform="translate(27.240625 248.662798)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="192.499943"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 10 -->

      <g transform="translate(20.878125 196.299162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="140.136307"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 15 -->

      <g transform="translate(20.878125 143.935526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="87.77267"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 20 -->

      <g transform="translate(20.878125 91.571889)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m4172391fd7" y="35.409034"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 25 -->

      <g transform="translate(20.878125 39.208253)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_14">

     <!-- Y Label definieren -->

     <defs>

      <path d="M -0.203125 72.90625 

L 10.40625 72.90625 

L 30.609375 42.921875 

L 50.6875 72.90625 

L 61.28125 72.90625 

L 35.5 34.71875 

L 35.5 0 

L 25.59375 0 

L 25.59375 34.71875 

z

" id="DejaVuSans-89"/>

     </defs>

     <g transform="translate(14.798438 211.262656)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-89"/>

      <use x="61.083984" xlink:href="#DejaVuSans-32"/>

      <use x="92.871094" xlink:href="#DejaVuSans-76"/>

      <use x="148.583984" xlink:href="#DejaVuSans-97"/>

      <use x="209.863281" xlink:href="#DejaVuSans-98"/>

      <use x="273.339844" xlink:href="#DejaVuSans-101"/>

      <use x="334.863281" xlink:href="#DejaVuSans-108"/>

      <use x="362.646484" xlink:href="#DejaVuSans-32"/>

      <use x="394.433594" xlink:href="#DejaVuSans-100"/>

      <use x="457.910156" xlink:href="#DejaVuSans-101"/>

      <use x="519.433594" xlink:href="#DejaVuSans-102"/>

      <use x="554.638672" xlink:href="#DejaVuSans-105"/>

      <use x="582.421875" xlink:href="#DejaVuSans-110"/>

      <use x="645.800781" xlink:href="#DejaVuSans-105"/>

      <use x="673.583984" xlink:href="#DejaVuSans-101"/>

      <use x="735.107422" xlink:href="#DejaVuSans-114"/>

      <use x="773.970703" xlink:href="#DejaVuSans-101"/>

      <use x="835.494141" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p06775fdec0)" d="M 60.239489 297.227216 

L 99.512216 294.609034 

L 138.784943 286.754489 

L 178.05767 273.66358 

L 217.330398 255.336307 

L 256.603125 231.77267 

L 295.875852 202.97267 

L 335.14858 168.936307 

L 374.421307 129.66358 

L 413.694034 85.154489 

L 452.966761 35.409034 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 40.603125 310.318125 

L 40.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 472.603125 310.318125 

L 472.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 40.603125 310.318125 

L 472.603125 310.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 40.603125 22.318125 

L 472.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_15">

    <!-- Überschrift -->

    <defs>

     <path d="M 8.6875 72.90625 

L 18.609375 72.90625 

L 18.609375 28.609375 

Q 18.609375 16.890625 22.84375 11.734375 

Q 27.09375 6.59375 36.625 6.59375 

Q 46.09375 6.59375 50.34375 11.734375 

Q 54.59375 16.890625 54.59375 28.609375 

L 54.59375 72.90625 

L 64.5 72.90625 

L 64.5 27.390625 

Q 64.5 13.140625 57.4375 5.859375 

Q 50.390625 -1.421875 36.625 -1.421875 

Q 22.796875 -1.421875 15.734375 5.859375 

Q 8.6875 13.140625 8.6875 27.390625 

z

M 41.21875 91.3125 

L 51.125 91.3125 

L 51.125 81.40625 

L 41.21875 81.40625 

z

M 22.125 91.3125 

L 32.03125 91.3125 

L 32.03125 81.40625 

L 22.125 81.40625 

z

" id="DejaVuSans-220"/>

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

    </defs>

    <g transform="translate(223.524375 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-220"/>

     <use x="73.193359" xlink:href="#DejaVuSans-98"/>

     <use x="136.669922" xlink:href="#DejaVuSans-101"/>

     <use x="198.193359" xlink:href="#DejaVuSans-114"/>

     <use x="239.306641" xlink:href="#DejaVuSans-115"/>

     <use x="291.40625" xlink:href="#DejaVuSans-99"/>

     <use x="346.386719" xlink:href="#DejaVuSans-104"/>

     <use x="409.765625" xlink:href="#DejaVuSans-114"/>

     <use x="450.878906" xlink:href="#DejaVuSans-105"/>

     <use x="478.662109" xlink:href="#DejaVuSans-102"/>

     <use x="512.117188" xlink:href="#DejaVuSans-116"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p06775fdec0">

   <rect height="288" width="432" x="40.603125" y="22.318125"/>

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
<div class="prompt input_prompt">In&nbsp;[120]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Demo Add_Axes</span>
<span class="n">af</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>
<span class="n">axes</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span> <span class="c1"># links, unten, breite, höhe (zwischen 0 und 1) =&gt; wird hier gleich überschrieben</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;X Label definieren&#39;</span><span class="p">)</span> <span class="c1"># Nutzt set_ um die Methode zu beginnen</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;Y Label definieren&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Überschrift&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[120]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Überschrift&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="635.874375pt" version="1.1" viewBox="0 0 263.803125 635.874375" width="263.803125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 635.874375 

L 263.803125 635.874375 

L 263.803125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 40.603125 598.318125 

L 256.603125 598.318125 

L 256.603125 22.318125 

L 40.603125 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m1a824acc74" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="50.421307" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(47.240057 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="89.694034" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(86.512784 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="128.966761" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(125.785511 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="168.239489" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(165.058239 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="207.512216" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(204.330966 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="246.784943" xlink:href="#m1a824acc74" y="598.318125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(243.603693 612.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- X Label definieren -->

     <defs>

      <path d="M 6.296875 72.90625 

L 16.890625 72.90625 

L 35.015625 45.796875 

L 53.21875 72.90625 

L 63.8125 72.90625 

L 40.375 37.890625 

L 65.375 0 

L 54.78125 0 

L 34.28125 31 

L 13.625 0 

L 2.984375 0 

L 29 38.921875 

z

" id="DejaVuSans-88"/>

      <path id="DejaVuSans-32"/>

      <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 8.296875 

L 55.171875 8.296875 

L 55.171875 0 

L 9.8125 0 

z

" id="DejaVuSans-76"/>

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

      <path d="M 48.6875 27.296875 

Q 48.6875 37.203125 44.609375 42.84375 

Q 40.53125 48.484375 33.40625 48.484375 

Q 26.265625 48.484375 22.1875 42.84375 

Q 18.109375 37.203125 18.109375 27.296875 

Q 18.109375 17.390625 22.1875 11.75 

Q 26.265625 6.109375 33.40625 6.109375 

Q 40.53125 6.109375 44.609375 11.75 

Q 48.6875 17.390625 48.6875 27.296875 

z

M 18.109375 46.390625 

Q 20.953125 51.265625 25.265625 53.625 

Q 29.59375 56 35.59375 56 

Q 45.5625 56 51.78125 48.09375 

Q 58.015625 40.1875 58.015625 27.296875 

Q 58.015625 14.40625 51.78125 6.484375 

Q 45.5625 -1.421875 35.59375 -1.421875 

Q 29.59375 -1.421875 25.265625 0.953125 

Q 20.953125 3.328125 18.109375 8.203125 

L 18.109375 0 

L 9.078125 0 

L 9.078125 75.984375 

L 18.109375 75.984375 

z

" id="DejaVuSans-98"/>

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

      <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

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

      <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

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

     </defs>

     <g transform="translate(103.2875 626.594687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-88"/>

      <use x="68.505859" xlink:href="#DejaVuSans-32"/>

      <use x="100.292969" xlink:href="#DejaVuSans-76"/>

      <use x="156.005859" xlink:href="#DejaVuSans-97"/>

      <use x="217.285156" xlink:href="#DejaVuSans-98"/>

      <use x="280.761719" xlink:href="#DejaVuSans-101"/>

      <use x="342.285156" xlink:href="#DejaVuSans-108"/>

      <use x="370.068359" xlink:href="#DejaVuSans-32"/>

      <use x="401.855469" xlink:href="#DejaVuSans-100"/>

      <use x="465.332031" xlink:href="#DejaVuSans-101"/>

      <use x="526.855469" xlink:href="#DejaVuSans-102"/>

      <use x="562.060547" xlink:href="#DejaVuSans-105"/>

      <use x="589.84375" xlink:href="#DejaVuSans-110"/>

      <use x="653.222656" xlink:href="#DejaVuSans-105"/>

      <use x="681.005859" xlink:href="#DejaVuSans-101"/>

      <use x="742.529297" xlink:href="#DejaVuSans-114"/>

      <use x="781.392578" xlink:href="#DejaVuSans-101"/>

      <use x="842.916016" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m1bcfcbf06c" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="572.136307"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(27.240625 575.935526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="467.409034"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 5 -->

      <g transform="translate(27.240625 471.208253)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="362.681761"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 10 -->

      <g transform="translate(20.878125 366.48098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="257.954489"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 15 -->

      <g transform="translate(20.878125 261.753707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="153.227216"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 20 -->

      <g transform="translate(20.878125 157.026435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#m1bcfcbf06c" y="48.499943"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 25 -->

      <g transform="translate(20.878125 52.299162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_14">

     <!-- Y Label definieren -->

     <defs>

      <path d="M -0.203125 72.90625 

L 10.40625 72.90625 

L 30.609375 42.921875 

L 50.6875 72.90625 

L 61.28125 72.90625 

L 35.5 34.71875 

L 35.5 0 

L 25.59375 0 

L 25.59375 34.71875 

z

" id="DejaVuSans-89"/>

     </defs>

     <g transform="translate(14.798438 355.262656)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-89"/>

      <use x="61.083984" xlink:href="#DejaVuSans-32"/>

      <use x="92.871094" xlink:href="#DejaVuSans-76"/>

      <use x="148.583984" xlink:href="#DejaVuSans-97"/>

      <use x="209.863281" xlink:href="#DejaVuSans-98"/>

      <use x="273.339844" xlink:href="#DejaVuSans-101"/>

      <use x="334.863281" xlink:href="#DejaVuSans-108"/>

      <use x="362.646484" xlink:href="#DejaVuSans-32"/>

      <use x="394.433594" xlink:href="#DejaVuSans-100"/>

      <use x="457.910156" xlink:href="#DejaVuSans-101"/>

      <use x="519.433594" xlink:href="#DejaVuSans-102"/>

      <use x="554.638672" xlink:href="#DejaVuSans-105"/>

      <use x="582.421875" xlink:href="#DejaVuSans-110"/>

      <use x="645.800781" xlink:href="#DejaVuSans-105"/>

      <use x="673.583984" xlink:href="#DejaVuSans-101"/>

      <use x="735.107422" xlink:href="#DejaVuSans-114"/>

      <use x="773.970703" xlink:href="#DejaVuSans-101"/>

      <use x="835.494141" xlink:href="#DejaVuSans-110"/>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p059a93da3b)" d="M 50.421307 572.136307 

L 70.05767 566.899943 

L 89.694034 551.190852 

L 109.330398 525.009034 

L 128.966761 488.354489 

L 148.603125 441.227216 

L 168.239489 383.627216 

L 187.875852 315.554489 

L 207.512216 237.009034 

L 227.14858 147.990852 

L 246.784943 48.499943 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 40.603125 598.318125 

L 40.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 256.603125 598.318125 

L 256.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 40.603125 598.318125 

L 256.603125 598.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 40.603125 22.318125 

L 256.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_15">

    <!-- Überschrift -->

    <defs>

     <path d="M 8.6875 72.90625 

L 18.609375 72.90625 

L 18.609375 28.609375 

Q 18.609375 16.890625 22.84375 11.734375 

Q 27.09375 6.59375 36.625 6.59375 

Q 46.09375 6.59375 50.34375 11.734375 

Q 54.59375 16.890625 54.59375 28.609375 

L 54.59375 72.90625 

L 64.5 72.90625 

L 64.5 27.390625 

Q 64.5 13.140625 57.4375 5.859375 

Q 50.390625 -1.421875 36.625 -1.421875 

Q 22.796875 -1.421875 15.734375 5.859375 

Q 8.6875 13.140625 8.6875 27.390625 

z

M 41.21875 91.3125 

L 51.125 91.3125 

L 51.125 81.40625 

L 41.21875 81.40625 

z

M 22.125 91.3125 

L 32.03125 91.3125 

L 32.03125 81.40625 

L 22.125 81.40625 

z

" id="DejaVuSans-220"/>

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

    </defs>

    <g transform="translate(115.524375 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-220"/>

     <use x="73.193359" xlink:href="#DejaVuSans-98"/>

     <use x="136.669922" xlink:href="#DejaVuSans-101"/>

     <use x="198.193359" xlink:href="#DejaVuSans-114"/>

     <use x="239.306641" xlink:href="#DejaVuSans-115"/>

     <use x="291.40625" xlink:href="#DejaVuSans-99"/>

     <use x="346.386719" xlink:href="#DejaVuSans-104"/>

     <use x="409.765625" xlink:href="#DejaVuSans-114"/>

     <use x="450.878906" xlink:href="#DejaVuSans-105"/>

     <use x="478.662109" xlink:href="#DejaVuSans-102"/>

     <use x="512.117188" xlink:href="#DejaVuSans-116"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p059a93da3b">

   <rect height="576" width="216" x="40.603125" y="22.318125"/>

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
<h2 id="Arbeitsfl&#228;che(~-Diagramm)-in-Variable-Speichern">Arbeitsfl&#228;che(~ Diagramm) in Variable Speichern<a class="anchor-link" href="#Arbeitsfl&#228;che(~-Diagramm)-in-Variable-Speichern">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[121]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Diagramm erstellen</span>
<span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">100</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[121]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30a5d92b0&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="103.078125pt" version="1.1" viewBox="0 0 106.125 103.078125" width="106.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 103.078125 

L 106.125 103.078125 

L 106.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 79.2 

L 98.925 79.2 

L 98.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mc538beaccb" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.197727" xlink:href="#mc538beaccb" y="79.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.016477 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="95.652273" xlink:href="#mc538beaccb" y="79.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(92.471023 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_3">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m6ca5407890" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m6ca5407890" y="75.927273"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(13.5625 79.726491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m6ca5407890" y="49.745455"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 10 -->

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

      <g transform="translate(7.2 53.544673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m6ca5407890" y="23.563636"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 20 -->

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

      <g transform="translate(7.2 27.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#pf24008ee81)" d="M 30.197727 75.927273 

L 36.743182 75.272727 

L 43.288636 73.309091 

L 49.834091 70.036364 

L 56.379545 65.454545 

L 62.925 59.563636 

L 69.470455 52.363636 

L 76.015909 43.854545 

L 82.561364 34.036364 

L 89.106818 22.909091 

L 95.652273 10.472727 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 79.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 98.925 79.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 79.2 

L 98.925 79.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pf24008ee81">

   <rect height="72" width="72" x="26.925" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Diagramm aus der Variable Plotten</span>
<span class="n">diag</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[122]:</div>



<div class="output_svg output_subarea output_execute_result">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="103.078125pt" version="1.1" viewBox="0 0 106.125 103.078125" width="106.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 103.078125 

L 106.125 103.078125 

L 106.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 79.2 

L 98.925 79.2 

L 98.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mb1996f4738" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.197727" xlink:href="#mb1996f4738" y="79.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.016477 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="95.652273" xlink:href="#mb1996f4738" y="79.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(92.471023 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_3">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m44fb370bc5" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m44fb370bc5" y="75.927273"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(13.5625 79.726491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m44fb370bc5" y="49.745455"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 10 -->

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

      <g transform="translate(7.2 53.544673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m44fb370bc5" y="23.563636"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 20 -->

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

      <g transform="translate(7.2 27.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#p2cae45fc6f)" d="M 30.197727 75.927273 

L 36.743182 75.272727 

L 43.288636 73.309091 

L 49.834091 70.036364 

L 56.379545 65.454545 

L 62.925 59.563636 

L 69.470455 52.363636 

L 76.015909 43.854545 

L 82.561364 34.036364 

L 89.106818 22.909091 

L 95.652273 10.472727 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 79.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 98.925 79.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 79.2 

L 98.925 79.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p2cae45fc6f">

   <rect height="72" width="72" x="26.925" y="7.2"/>

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
<h2 id="Arbeitsfl&#228;che-mt-mehreren-Diagrammen">Arbeitsfl&#228;che mt mehreren Diagrammen<a class="anchor-link" href="#Arbeitsfl&#228;che-mt-mehreren-Diagrammen">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[123]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Leere Arbeitsfläche erstellen</span>
<span class="n">af</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>

<span class="n">axes1</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mf">0.1</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">])</span> <span class="c1"># Hauptachse</span>
<span class="n">axes2</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mf">0.2</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.4</span><span class="p">,</span> <span class="mf">0.3</span><span class="p">])</span> <span class="c1"># Eingesetzte Achse</span>

<span class="c1"># Größeres Diagramm mit Achse 1</span>
<span class="n">axes1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">)</span>
<span class="n">axes1</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;x Beschriftung Achse 1&#39;</span><span class="p">)</span>
<span class="n">axes1</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;y Beschriftung Achse 1&#39;</span><span class="p">)</span>
<span class="n">axes1</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Titel größeres Diagramm&#39;</span><span class="p">)</span>

<span class="c1"># Eingesetztes Diagramm mit Achse 2</span>
<span class="n">axes2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="s1">&#39;r--&#39;</span><span class="p">)</span>
<span class="n">axes2</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;x Beschriftung Achse 2&#39;</span><span class="p">)</span>
<span class="n">axes2</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;y Beschriftung Achse 2&#39;</span><span class="p">)</span>
<span class="n">axes2</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Titel eingesetztes Diagramm&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="290.274375pt" version="1.1" viewBox="0 0 393.403125 290.274375" width="393.403125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 290.274375 

L 393.403125 290.274375 

L 393.403125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 40.603125 252.718125 

L 386.203125 252.718125 

L 386.203125 22.318125 

L 40.603125 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m4020e7cc9b" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="56.312216" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(53.130966 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="119.14858" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(115.96733 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="181.984943" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(178.803693 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="244.821307" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(241.640057 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="307.65767" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(304.47642 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="370.494034" xlink:href="#m4020e7cc9b" y="252.718125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(367.312784 267.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- x Beschriftung Achse 1 -->

     <defs>

      <path d="M 54.890625 54.6875 

L 35.109375 28.078125 

L 55.90625 0 

L 45.3125 0 

L 29.390625 21.484375 

L 13.484375 0 

L 2.875 0 

L 24.125 28.609375 

L 4.6875 54.6875 

L 15.28125 54.6875 

L 29.78125 35.203125 

L 44.28125 54.6875 

z

" id="DejaVuSans-120"/>

      <path id="DejaVuSans-32"/>

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

      <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

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

      <path d="M 34.1875 63.1875 

L 20.796875 26.90625 

L 47.609375 26.90625 

z

M 28.609375 72.90625 

L 39.796875 72.90625 

L 67.578125 0 

L 57.328125 0 

L 50.6875 18.703125 

L 17.828125 18.703125 

L 11.1875 0 

L 0.78125 0 

z

" id="DejaVuSans-65"/>

     </defs>

     <g transform="translate(155.944531 280.994687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-32"/>

      <use x="90.966797" xlink:href="#DejaVuSans-66"/>

      <use x="159.570312" xlink:href="#DejaVuSans-101"/>

      <use x="221.09375" xlink:href="#DejaVuSans-115"/>

      <use x="273.193359" xlink:href="#DejaVuSans-99"/>

      <use x="328.173828" xlink:href="#DejaVuSans-104"/>

      <use x="391.552734" xlink:href="#DejaVuSans-114"/>

      <use x="432.666016" xlink:href="#DejaVuSans-105"/>

      <use x="460.449219" xlink:href="#DejaVuSans-102"/>

      <use x="493.904297" xlink:href="#DejaVuSans-116"/>

      <use x="533.113281" xlink:href="#DejaVuSans-117"/>

      <use x="596.492188" xlink:href="#DejaVuSans-110"/>

      <use x="659.871094" xlink:href="#DejaVuSans-103"/>

      <use x="723.347656" xlink:href="#DejaVuSans-32"/>

      <use x="755.134766" xlink:href="#DejaVuSans-65"/>

      <use x="821.792969" xlink:href="#DejaVuSans-99"/>

      <use x="876.773438" xlink:href="#DejaVuSans-104"/>

      <use x="940.152344" xlink:href="#DejaVuSans-115"/>

      <use x="992.251953" xlink:href="#DejaVuSans-101"/>

      <use x="1053.775391" xlink:href="#DejaVuSans-32"/>

      <use x="1085.5625" xlink:href="#DejaVuSans-49"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="ma453f7d0a0" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="242.245398"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(27.240625 246.044616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="200.354489"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 5 -->

      <g transform="translate(27.240625 204.153707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="158.46358"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 10 -->

      <g transform="translate(20.878125 162.262798)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="116.57267"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 15 -->

      <g transform="translate(20.878125 120.371889)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="74.681761"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 20 -->

      <g transform="translate(20.878125 78.48098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.603125" xlink:href="#ma453f7d0a0" y="32.790852"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 25 -->

      <g transform="translate(20.878125 36.590071)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_14">

     <!-- y Beschriftung Achse 1 -->

     <defs>

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

     <g transform="translate(14.798438 194.976719)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-121"/>

      <use x="59.179688" xlink:href="#DejaVuSans-32"/>

      <use x="90.966797" xlink:href="#DejaVuSans-66"/>

      <use x="159.570312" xlink:href="#DejaVuSans-101"/>

      <use x="221.09375" xlink:href="#DejaVuSans-115"/>

      <use x="273.193359" xlink:href="#DejaVuSans-99"/>

      <use x="328.173828" xlink:href="#DejaVuSans-104"/>

      <use x="391.552734" xlink:href="#DejaVuSans-114"/>

      <use x="432.666016" xlink:href="#DejaVuSans-105"/>

      <use x="460.449219" xlink:href="#DejaVuSans-102"/>

      <use x="493.904297" xlink:href="#DejaVuSans-116"/>

      <use x="533.113281" xlink:href="#DejaVuSans-117"/>

      <use x="596.492188" xlink:href="#DejaVuSans-110"/>

      <use x="659.871094" xlink:href="#DejaVuSans-103"/>

      <use x="723.347656" xlink:href="#DejaVuSans-32"/>

      <use x="755.134766" xlink:href="#DejaVuSans-65"/>

      <use x="821.792969" xlink:href="#DejaVuSans-99"/>

      <use x="876.773438" xlink:href="#DejaVuSans-104"/>

      <use x="940.152344" xlink:href="#DejaVuSans-115"/>

      <use x="992.251953" xlink:href="#DejaVuSans-101"/>

      <use x="1053.775391" xlink:href="#DejaVuSans-32"/>

      <use x="1085.5625" xlink:href="#DejaVuSans-49"/>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p8ec4e03f61)" d="M 56.312216 242.245398 

L 87.730398 240.150852 

L 119.14858 233.867216 

L 150.566761 223.394489 

L 181.984943 208.73267 

L 213.403125 189.881761 

L 244.821307 166.841761 

L 276.239489 139.61267 

L 307.65767 108.194489 

L 339.075852 72.587216 

L 370.494034 32.790852 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 40.603125 252.718125 

L 40.603125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 386.203125 252.718125 

L 386.203125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 40.603125 252.718125 

L 386.203125 252.718125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 40.603125 22.318125 

L 386.203125 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_15">

    <!-- Titel größeres Diagramm -->

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

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

M 35.203125 75.78125 

L 45.125 75.78125 

L 45.125 65.921875 

L 35.203125 65.921875 

z

M 16.109375 75.78125 

L 26.03125 75.78125 

L 26.03125 65.921875 

L 16.109375 65.921875 

z

" id="DejaVuSans-246"/>

     <path d="M 9.078125 55.515625 

Q 9.078125 65.28125 14.90625 70.625 

Q 20.75 75.984375 31.390625 75.984375 

Q 41.546875 75.984375 46.890625 70.3125 

Q 52.25 64.65625 52.390625 53.71875 

Q 45.015625 53.328125 40.90625 50.515625 

Q 36.8125 47.703125 36.8125 43.015625 

Q 36.8125 40.71875 38.234375 38.734375 

Q 39.65625 36.765625 42.828125 34.71875 

L 45.609375 32.90625 

Q 53.71875 27.734375 56.0625 24.265625 

Q 58.40625 20.796875 58.40625 15.921875 

Q 58.40625 7.515625 52.90625 3.046875 

Q 47.40625 -1.421875 37.109375 -1.421875 

Q 33.984375 -1.421875 30.65625 -0.8125 

Q 27.34375 -0.203125 23.78125 0.984375 

L 23.78125 8.984375 

Q 27.6875 7.515625 31.09375 6.8125 

Q 34.515625 6.109375 37.703125 6.109375 

Q 43.359375 6.109375 46.28125 8.421875 

Q 49.21875 10.75 49.21875 15.1875 

Q 49.21875 18.265625 47.78125 20.3125 

Q 46.34375 22.359375 41.40625 25.390625 

L 36.921875 28.078125 

Q 32.234375 30.953125 30.109375 34.25 

Q 27.984375 37.546875 27.984375 42 

Q 27.984375 48.1875 32.0625 52.390625 

Q 36.140625 56.59375 43.5 58.015625 

Q 43.109375 63.03125 39.90625 65.765625 

Q 36.71875 68.5 31.203125 68.5 

Q 24.859375 68.5 21.53125 65.109375 

Q 18.21875 61.71875 18.21875 55.328125 

L 18.21875 0 

L 9.078125 0 

z

" id="DejaVuSans-223"/>

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

    <g transform="translate(138.6975 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-84"/>

     <use x="57.958984" xlink:href="#DejaVuSans-105"/>

     <use x="85.742188" xlink:href="#DejaVuSans-116"/>

     <use x="124.951172" xlink:href="#DejaVuSans-101"/>

     <use x="186.474609" xlink:href="#DejaVuSans-108"/>

     <use x="214.257812" xlink:href="#DejaVuSans-32"/>

     <use x="246.044922" xlink:href="#DejaVuSans-103"/>

     <use x="309.521484" xlink:href="#DejaVuSans-114"/>

     <use x="348.384766" xlink:href="#DejaVuSans-246"/>

     <use x="409.566406" xlink:href="#DejaVuSans-223"/>

     <use x="472.554688" xlink:href="#DejaVuSans-101"/>

     <use x="534.078125" xlink:href="#DejaVuSans-114"/>

     <use x="572.941406" xlink:href="#DejaVuSans-101"/>

     <use x="634.464844" xlink:href="#DejaVuSans-115"/>

     <use x="686.564453" xlink:href="#DejaVuSans-32"/>

     <use x="718.351562" xlink:href="#DejaVuSans-68"/>

     <use x="795.353516" xlink:href="#DejaVuSans-105"/>

     <use x="823.136719" xlink:href="#DejaVuSans-97"/>

     <use x="884.416016" xlink:href="#DejaVuSans-103"/>

     <use x="947.892578" xlink:href="#DejaVuSans-114"/>

     <use x="989.005859" xlink:href="#DejaVuSans-97"/>

     <use x="1050.285156" xlink:href="#DejaVuSans-109"/>

     <use x="1147.697266" xlink:href="#DejaVuSans-109"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 83.803125 137.518125 

L 256.603125 137.518125 

L 256.603125 51.118125 

L 83.803125 51.118125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_7">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="91.65767" xlink:href="#m4020e7cc9b" y="137.518125"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 0 -->

      <g transform="translate(88.47642 152.116563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="154.494034" xlink:href="#m4020e7cc9b" y="137.518125"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 10 -->

      <g transform="translate(148.131534 152.116563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="217.330398" xlink:href="#m4020e7cc9b" y="137.518125"/>

      </g>

     </g>

     <g id="text_18">

      <!-- 20 -->

      <g transform="translate(210.967898 152.116563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="text_19">

     <!-- x Beschriftung Achse 2 -->

     <g transform="translate(112.744531 165.794688)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-32"/>

      <use x="90.966797" xlink:href="#DejaVuSans-66"/>

      <use x="159.570312" xlink:href="#DejaVuSans-101"/>

      <use x="221.09375" xlink:href="#DejaVuSans-115"/>

      <use x="273.193359" xlink:href="#DejaVuSans-99"/>

      <use x="328.173828" xlink:href="#DejaVuSans-104"/>

      <use x="391.552734" xlink:href="#DejaVuSans-114"/>

      <use x="432.666016" xlink:href="#DejaVuSans-105"/>

      <use x="460.449219" xlink:href="#DejaVuSans-102"/>

      <use x="493.904297" xlink:href="#DejaVuSans-116"/>

      <use x="533.113281" xlink:href="#DejaVuSans-117"/>

      <use x="596.492188" xlink:href="#DejaVuSans-110"/>

      <use x="659.871094" xlink:href="#DejaVuSans-103"/>

      <use x="723.347656" xlink:href="#DejaVuSans-32"/>

      <use x="755.134766" xlink:href="#DejaVuSans-65"/>

      <use x="821.792969" xlink:href="#DejaVuSans-99"/>

      <use x="876.773438" xlink:href="#DejaVuSans-104"/>

      <use x="940.152344" xlink:href="#DejaVuSans-115"/>

      <use x="992.251953" xlink:href="#DejaVuSans-101"/>

      <use x="1053.775391" xlink:href="#DejaVuSans-32"/>

      <use x="1085.5625" xlink:href="#DejaVuSans-50"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_7">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="83.803125" xlink:href="#ma453f7d0a0" y="133.590852"/>

      </g>

     </g>

     <g id="text_20">

      <!-- 0 -->

      <g transform="translate(70.440625 137.390071)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="83.803125" xlink:href="#ma453f7d0a0" y="102.17267"/>

      </g>

     </g>

     <g id="text_21">

      <!-- 2 -->

      <g transform="translate(70.440625 105.971889)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="83.803125" xlink:href="#ma453f7d0a0" y="70.754489"/>

      </g>

     </g>

     <g id="text_22">

      <!-- 4 -->

      <g transform="translate(70.440625 74.553707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="text_23">

     <!-- y Beschriftung Achse 2 -->

     <g transform="translate(64.360938 151.776719)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-121"/>

      <use x="59.179688" xlink:href="#DejaVuSans-32"/>

      <use x="90.966797" xlink:href="#DejaVuSans-66"/>

      <use x="159.570312" xlink:href="#DejaVuSans-101"/>

      <use x="221.09375" xlink:href="#DejaVuSans-115"/>

      <use x="273.193359" xlink:href="#DejaVuSans-99"/>

      <use x="328.173828" xlink:href="#DejaVuSans-104"/>

      <use x="391.552734" xlink:href="#DejaVuSans-114"/>

      <use x="432.666016" xlink:href="#DejaVuSans-105"/>

      <use x="460.449219" xlink:href="#DejaVuSans-102"/>

      <use x="493.904297" xlink:href="#DejaVuSans-116"/>

      <use x="533.113281" xlink:href="#DejaVuSans-117"/>

      <use x="596.492188" xlink:href="#DejaVuSans-110"/>

      <use x="659.871094" xlink:href="#DejaVuSans-103"/>

      <use x="723.347656" xlink:href="#DejaVuSans-32"/>

      <use x="755.134766" xlink:href="#DejaVuSans-65"/>

      <use x="821.792969" xlink:href="#DejaVuSans-99"/>

      <use x="876.773438" xlink:href="#DejaVuSans-104"/>

      <use x="940.152344" xlink:href="#DejaVuSans-115"/>

      <use x="992.251953" xlink:href="#DejaVuSans-101"/>

      <use x="1053.775391" xlink:href="#DejaVuSans-32"/>

      <use x="1085.5625" xlink:href="#DejaVuSans-50"/>

     </g>

    </g>

   </g>

   <g id="line2d_20">

    <path clip-path="url(#pe5457978c3)" d="M 91.65767 133.590852 

L 93.22858 125.736307 

L 97.941307 117.881761 

L 105.795852 110.027216 

L 116.792216 102.17267 

L 130.930398 94.318125 

L 148.210398 86.46358 

L 168.632216 78.609034 

L 192.195852 70.754489 

L 218.901307 62.899943 

L 248.74858 55.045398 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_8">

    <path d="M 83.803125 137.518125 

L 83.803125 51.118125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 256.603125 137.518125 

L 256.603125 51.118125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 83.803125 137.518125 

L 256.603125 137.518125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 83.803125 51.118125 

L 256.603125 51.118125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_24">

    <!-- Titel eingesetztes Diagramm -->

    <defs>

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

    <g transform="translate(83.77875 45.118125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-84"/>

     <use x="57.958984" xlink:href="#DejaVuSans-105"/>

     <use x="85.742188" xlink:href="#DejaVuSans-116"/>

     <use x="124.951172" xlink:href="#DejaVuSans-101"/>

     <use x="186.474609" xlink:href="#DejaVuSans-108"/>

     <use x="214.257812" xlink:href="#DejaVuSans-32"/>

     <use x="246.044922" xlink:href="#DejaVuSans-101"/>

     <use x="307.568359" xlink:href="#DejaVuSans-105"/>

     <use x="335.351562" xlink:href="#DejaVuSans-110"/>

     <use x="398.730469" xlink:href="#DejaVuSans-103"/>

     <use x="462.207031" xlink:href="#DejaVuSans-101"/>

     <use x="523.730469" xlink:href="#DejaVuSans-115"/>

     <use x="575.830078" xlink:href="#DejaVuSans-101"/>

     <use x="637.353516" xlink:href="#DejaVuSans-116"/>

     <use x="676.5625" xlink:href="#DejaVuSans-122"/>

     <use x="729.052734" xlink:href="#DejaVuSans-116"/>

     <use x="768.261719" xlink:href="#DejaVuSans-101"/>

     <use x="829.785156" xlink:href="#DejaVuSans-115"/>

     <use x="881.884766" xlink:href="#DejaVuSans-32"/>

     <use x="913.671875" xlink:href="#DejaVuSans-68"/>

     <use x="990.673828" xlink:href="#DejaVuSans-105"/>

     <use x="1018.457031" xlink:href="#DejaVuSans-97"/>

     <use x="1079.736328" xlink:href="#DejaVuSans-103"/>

     <use x="1143.212891" xlink:href="#DejaVuSans-114"/>

     <use x="1184.326172" xlink:href="#DejaVuSans-97"/>

     <use x="1245.605469" xlink:href="#DejaVuSans-109"/>

     <use x="1343.017578" xlink:href="#DejaVuSans-109"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p8ec4e03f61">

   <rect height="230.4" width="345.6" x="40.603125" y="22.318125"/>

  </clipPath>

  <clipPath id="pe5457978c3">

   <rect height="86.4" width="172.8" x="83.803125" y="51.118125"/>

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
<h2 id="Diagramm-mit-mehreren-Wertepaaren-||-Erstellen-einer-Legende">Diagramm mit mehreren Wertepaaren || Erstellen einer Legende<a class="anchor-link" href="#Diagramm-mit-mehreren-Wertepaaren-||-Erstellen-einer-Legende">&#182;</a></h2><p>Sprich in einem Diagramm mehr als ein Linienpaar, dann muss ich wissen welche Linie zu welchen Daten gehört</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="innerhalb-der-Diagrammes">innerhalb der Diagrammes<a class="anchor-link" href="#innerhalb-der-Diagrammes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[124]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Diagramm erstellen (leere Arbeitsfläche)</span>
<span class="n">af</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>
<span class="c1"># Dem Diagramm Achsen hinzufügen</span>
<span class="n">axes</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span> <span class="c1"># links, unten, breite, höhe von dem gesamten Diagramm</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;mehr Wertepaare in eienm Diagramm&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;X&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Y&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;x**2&quot;</span><span class="p">)</span> <span class="c1">#</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">3</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;x**3&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> <span class="c1"># =&gt; ohne diesen Befehl wird die Legende nicht angezeigt. || über loc wird die Legende positioniert kann zwischen 0 &amp; 10 sein</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[124]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x1c30a615310&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="347.874375pt" version="1.1" viewBox="0 0 486.165625 347.874375" width="486.165625pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 347.874375 

L 486.165625 347.874375 

L 486.165625 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 46.965625 310.318125 

L 478.965625 310.318125 

L 478.965625 22.318125 

L 46.965625 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m12d9c01096" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="66.601989" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(63.420739 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="145.147443" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(141.966193 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="223.692898" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(220.511648 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="302.238352" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(299.057102 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="380.783807" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(377.602557 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="459.329261" xlink:href="#m12d9c01096" y="310.318125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(456.148011 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- X -->

     <defs>

      <path d="M 6.296875 72.90625 

L 16.890625 72.90625 

L 35.015625 45.796875 

L 53.21875 72.90625 

L 63.8125 72.90625 

L 40.375 37.890625 

L 65.375 0 

L 54.78125 0 

L 34.28125 31 

L 13.625 0 

L 2.984375 0 

L 29 38.921875 

z

" id="DejaVuSans-88"/>

     </defs>

     <g transform="translate(259.540625 338.594687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-88"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m1ee82eb805" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="297.227216"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(33.603125 301.026435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="255.336307"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 20 -->

      <g transform="translate(27.240625 259.135526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="213.445398"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 40 -->

      <g transform="translate(27.240625 217.244616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="171.554489"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 60 -->

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

      <g transform="translate(27.240625 175.353707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="129.66358"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 80 -->

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

      </defs>

      <g transform="translate(27.240625 133.462798)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="87.77267"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 100 -->

      <g transform="translate(20.878125 91.571889)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m1ee82eb805" y="45.881761"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 120 -->

      <g transform="translate(20.878125 49.68098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="text_15">

     <!-- Y -->

     <defs>

      <path d="M -0.203125 72.90625 

L 10.40625 72.90625 

L 30.609375 42.921875 

L 50.6875 72.90625 

L 61.28125 72.90625 

L 35.5 34.71875 

L 35.5 0 

L 25.59375 0 

L 25.59375 34.71875 

z

" id="DejaVuSans-89"/>

     </defs>

     <g transform="translate(14.798437 169.372031)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-89"/>

     </g>

    </g>

   </g>

   <g id="line2d_14">

    <path clip-path="url(#pd5a5260816)" d="M 66.601989 297.227216 

L 105.874716 296.70358 

L 145.147443 295.13267 

L 184.42017 292.514489 

L 223.692898 288.849034 

L 262.965625 284.136307 

L 302.238352 278.376307 

L 341.51108 271.569034 

L 380.783807 263.714489 

L 420.056534 254.81267 

L 459.329261 244.86358 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_15">

    <path clip-path="url(#pd5a5260816)" d="M 66.601989 297.227216 

L 105.874716 296.965398 

L 145.147443 295.13267 

L 184.42017 290.158125 

L 223.692898 280.470852 

L 262.965625 264.499943 

L 302.238352 240.674489 

L 341.51108 207.42358 

L 380.783807 163.176307 

L 420.056534 106.361761 

L 459.329261 35.409034 

" style="fill:none;stroke:#ff7f0e;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 46.965625 310.318125 

L 46.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 478.965625 310.318125 

L 478.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 46.965625 310.318125 

L 478.965625 310.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 46.965625 22.318125 

L 478.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_16">

    <!-- mehr Wertepaare in eienm Diagramm -->

    <defs>

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

     <path id="DejaVuSans-32"/>

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

    <g transform="translate(148.792188 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-109"/>

     <use x="97.412109" xlink:href="#DejaVuSans-101"/>

     <use x="158.935547" xlink:href="#DejaVuSans-104"/>

     <use x="222.314453" xlink:href="#DejaVuSans-114"/>

     <use x="263.427734" xlink:href="#DejaVuSans-32"/>

     <use x="295.214844" xlink:href="#DejaVuSans-87"/>

     <use x="388.216797" xlink:href="#DejaVuSans-101"/>

     <use x="449.740234" xlink:href="#DejaVuSans-114"/>

     <use x="490.853516" xlink:href="#DejaVuSans-116"/>

     <use x="530.0625" xlink:href="#DejaVuSans-101"/>

     <use x="591.585938" xlink:href="#DejaVuSans-112"/>

     <use x="655.0625" xlink:href="#DejaVuSans-97"/>

     <use x="716.341797" xlink:href="#DejaVuSans-97"/>

     <use x="777.621094" xlink:href="#DejaVuSans-114"/>

     <use x="816.484375" xlink:href="#DejaVuSans-101"/>

     <use x="878.007812" xlink:href="#DejaVuSans-32"/>

     <use x="909.794922" xlink:href="#DejaVuSans-105"/>

     <use x="937.578125" xlink:href="#DejaVuSans-110"/>

     <use x="1000.957031" xlink:href="#DejaVuSans-32"/>

     <use x="1032.744141" xlink:href="#DejaVuSans-101"/>

     <use x="1094.267578" xlink:href="#DejaVuSans-105"/>

     <use x="1122.050781" xlink:href="#DejaVuSans-101"/>

     <use x="1183.574219" xlink:href="#DejaVuSans-110"/>

     <use x="1246.953125" xlink:href="#DejaVuSans-109"/>

     <use x="1344.365234" xlink:href="#DejaVuSans-32"/>

     <use x="1376.152344" xlink:href="#DejaVuSans-68"/>

     <use x="1453.154297" xlink:href="#DejaVuSans-105"/>

     <use x="1480.9375" xlink:href="#DejaVuSans-97"/>

     <use x="1542.216797" xlink:href="#DejaVuSans-103"/>

     <use x="1605.693359" xlink:href="#DejaVuSans-114"/>

     <use x="1646.806641" xlink:href="#DejaVuSans-97"/>

     <use x="1708.085938" xlink:href="#DejaVuSans-109"/>

     <use x="1805.498047" xlink:href="#DejaVuSans-109"/>

    </g>

   </g>

   <g id="legend_1">

    <g id="patch_7">

     <path d="M 53.965625 59.674375 

L 108.246875 59.674375 

Q 110.246875 59.674375 110.246875 57.674375 

L 110.246875 29.318125 

Q 110.246875 27.318125 108.246875 27.318125 

L 53.965625 27.318125 

Q 51.965625 27.318125 51.965625 29.318125 

L 51.965625 57.674375 

Q 51.965625 59.674375 53.965625 59.674375 

z

" style="fill:#ffffff;opacity:0.8;stroke:#cccccc;stroke-linejoin:miter;"/>

    </g>

    <g id="line2d_16">

     <path d="M 55.965625 35.416562 

L 75.965625 35.416562 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

    </g>

    <g id="line2d_17"/>

    <g id="text_17">

     <!-- x**2 -->

     <defs>

      <path d="M 54.890625 54.6875 

L 35.109375 28.078125 

L 55.90625 0 

L 45.3125 0 

L 29.390625 21.484375 

L 13.484375 0 

L 2.875 0 

L 24.125 28.609375 

L 4.6875 54.6875 

L 15.28125 54.6875 

L 29.78125 35.203125 

L 44.28125 54.6875 

z

" id="DejaVuSans-120"/>

      <path d="M 47.015625 60.890625 

L 29.5 51.421875 

L 47.015625 41.890625 

L 44.1875 37.109375 

L 27.78125 47.015625 

L 27.78125 28.609375 

L 22.21875 28.609375 

L 22.21875 47.015625 

L 5.8125 37.109375 

L 2.984375 41.890625 

L 20.515625 51.421875 

L 2.984375 60.890625 

L 5.8125 65.71875 

L 22.21875 55.8125 

L 22.21875 74.21875 

L 27.78125 74.21875 

L 27.78125 55.8125 

L 44.1875 65.71875 

z

" id="DejaVuSans-42"/>

     </defs>

     <g transform="translate(83.965625 38.916562)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-42"/>

      <use x="109.179688" xlink:href="#DejaVuSans-42"/>

      <use x="159.179688" xlink:href="#DejaVuSans-50"/>

     </g>

    </g>

    <g id="line2d_18">

     <path d="M 55.965625 50.094687 

L 75.965625 50.094687 

" style="fill:none;stroke:#ff7f0e;stroke-linecap:square;stroke-width:1.5;"/>

    </g>

    <g id="line2d_19"/>

    <g id="text_18">

     <!-- x**3 -->

     <g transform="translate(83.965625 53.594687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-42"/>

      <use x="109.179688" xlink:href="#DejaVuSans-42"/>

      <use x="159.179688" xlink:href="#DejaVuSans-51"/>

     </g>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pd5a5260816">

   <rect height="288" width="432" x="46.965625" y="22.318125"/>

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
<div class="prompt input_prompt">In&nbsp;[125]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">af</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>
<span class="c1"># Dem Diagramm Achsen hinzufügen</span>
<span class="n">axes</span> <span class="o">=</span> <span class="n">af</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span> <span class="c1"># links, unten, breite, höhe von dem gesamten Diagramm</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;mehr Wertepaare in eienm Diagramm&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">&quot;X&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Y&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;x**2&quot;</span><span class="p">)</span> <span class="c1">#</span>
<span class="n">axes</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">3</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;x**3&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="s1">&#39;center left&#39;</span><span class="p">,</span> <span class="n">bbox_to_anchor</span><span class="o">=</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">))</span> <span class="c1"># &lt;= Anzeige der Legende Außerhalb des Diagrammes</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[125]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.legend.Legend at 0x1c30a6edee0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="347.874375pt" version="1.1" viewBox="0 0 549.446875 347.874375" width="549.446875pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 347.874375 

L 549.446875 347.874375 

L 549.446875 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 46.965625 310.318125 

L 478.965625 310.318125 

L 478.965625 22.318125 

L 46.965625 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mcdd68f37ac" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="66.601989" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(63.420739 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="145.147443" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(141.966193 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="223.692898" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(220.511648 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="302.238352" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(299.057102 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="380.783807" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(377.602557 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="459.329261" xlink:href="#mcdd68f37ac" y="310.318125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(456.148011 324.916562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="text_7">

     <!-- X -->

     <defs>

      <path d="M 6.296875 72.90625 

L 16.890625 72.90625 

L 35.015625 45.796875 

L 53.21875 72.90625 

L 63.8125 72.90625 

L 40.375 37.890625 

L 65.375 0 

L 54.78125 0 

L 34.28125 31 

L 13.625 0 

L 2.984375 0 

L 29 38.921875 

z

" id="DejaVuSans-88"/>

     </defs>

     <g transform="translate(259.540625 338.594687)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-88"/>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m94fb8169a0" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="297.227216"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0 -->

      <g transform="translate(33.603125 301.026435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="255.336307"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 20 -->

      <g transform="translate(27.240625 259.135526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="213.445398"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 40 -->

      <g transform="translate(27.240625 217.244616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="171.554489"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 60 -->

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

      <g transform="translate(27.240625 175.353707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="129.66358"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 80 -->

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

      </defs>

      <g transform="translate(27.240625 133.462798)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="87.77267"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 100 -->

      <g transform="translate(20.878125 91.571889)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="46.965625" xlink:href="#m94fb8169a0" y="45.881761"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 120 -->

      <g transform="translate(20.878125 49.68098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="text_15">

     <!-- Y -->

     <defs>

      <path d="M -0.203125 72.90625 

L 10.40625 72.90625 

L 30.609375 42.921875 

L 50.6875 72.90625 

L 61.28125 72.90625 

L 35.5 34.71875 

L 35.5 0 

L 25.59375 0 

L 25.59375 34.71875 

z

" id="DejaVuSans-89"/>

     </defs>

     <g transform="translate(14.798437 169.372031)rotate(-90)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-89"/>

     </g>

    </g>

   </g>

   <g id="line2d_14">

    <path clip-path="url(#p60cb0682a8)" d="M 66.601989 297.227216 

L 105.874716 296.70358 

L 145.147443 295.13267 

L 184.42017 292.514489 

L 223.692898 288.849034 

L 262.965625 284.136307 

L 302.238352 278.376307 

L 341.51108 271.569034 

L 380.783807 263.714489 

L 420.056534 254.81267 

L 459.329261 244.86358 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="line2d_15">

    <path clip-path="url(#p60cb0682a8)" d="M 66.601989 297.227216 

L 105.874716 296.965398 

L 145.147443 295.13267 

L 184.42017 290.158125 

L 223.692898 280.470852 

L 262.965625 264.499943 

L 302.238352 240.674489 

L 341.51108 207.42358 

L 380.783807 163.176307 

L 420.056534 106.361761 

L 459.329261 35.409034 

" style="fill:none;stroke:#ff7f0e;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 46.965625 310.318125 

L 46.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 478.965625 310.318125 

L 478.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 46.965625 310.318125 

L 478.965625 310.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 46.965625 22.318125 

L 478.965625 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_16">

    <!-- mehr Wertepaare in eienm Diagramm -->

    <defs>

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

     <path id="DejaVuSans-32"/>

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

    <g transform="translate(148.792188 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-109"/>

     <use x="97.412109" xlink:href="#DejaVuSans-101"/>

     <use x="158.935547" xlink:href="#DejaVuSans-104"/>

     <use x="222.314453" xlink:href="#DejaVuSans-114"/>

     <use x="263.427734" xlink:href="#DejaVuSans-32"/>

     <use x="295.214844" xlink:href="#DejaVuSans-87"/>

     <use x="388.216797" xlink:href="#DejaVuSans-101"/>

     <use x="449.740234" xlink:href="#DejaVuSans-114"/>

     <use x="490.853516" xlink:href="#DejaVuSans-116"/>

     <use x="530.0625" xlink:href="#DejaVuSans-101"/>

     <use x="591.585938" xlink:href="#DejaVuSans-112"/>

     <use x="655.0625" xlink:href="#DejaVuSans-97"/>

     <use x="716.341797" xlink:href="#DejaVuSans-97"/>

     <use x="777.621094" xlink:href="#DejaVuSans-114"/>

     <use x="816.484375" xlink:href="#DejaVuSans-101"/>

     <use x="878.007812" xlink:href="#DejaVuSans-32"/>

     <use x="909.794922" xlink:href="#DejaVuSans-105"/>

     <use x="937.578125" xlink:href="#DejaVuSans-110"/>

     <use x="1000.957031" xlink:href="#DejaVuSans-32"/>

     <use x="1032.744141" xlink:href="#DejaVuSans-101"/>

     <use x="1094.267578" xlink:href="#DejaVuSans-105"/>

     <use x="1122.050781" xlink:href="#DejaVuSans-101"/>

     <use x="1183.574219" xlink:href="#DejaVuSans-110"/>

     <use x="1246.953125" xlink:href="#DejaVuSans-109"/>

     <use x="1344.365234" xlink:href="#DejaVuSans-32"/>

     <use x="1376.152344" xlink:href="#DejaVuSans-68"/>

     <use x="1453.154297" xlink:href="#DejaVuSans-105"/>

     <use x="1480.9375" xlink:href="#DejaVuSans-97"/>

     <use x="1542.216797" xlink:href="#DejaVuSans-103"/>

     <use x="1605.693359" xlink:href="#DejaVuSans-114"/>

     <use x="1646.806641" xlink:href="#DejaVuSans-97"/>

     <use x="1708.085938" xlink:href="#DejaVuSans-109"/>

     <use x="1805.498047" xlink:href="#DejaVuSans-109"/>

    </g>

   </g>

   <g id="legend_1">

    <g id="patch_7">

     <path d="M 485.965625 182.49625 

L 540.246875 182.49625 

Q 542.246875 182.49625 542.246875 180.49625 

L 542.246875 152.14 

Q 542.246875 150.14 540.246875 150.14 

L 485.965625 150.14 

Q 483.965625 150.14 483.965625 152.14 

L 483.965625 180.49625 

Q 483.965625 182.49625 485.965625 182.49625 

z

" style="fill:#ffffff;opacity:0.8;stroke:#cccccc;stroke-linejoin:miter;"/>

    </g>

    <g id="line2d_16">

     <path d="M 487.965625 158.238437 

L 507.965625 158.238437 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

    </g>

    <g id="line2d_17"/>

    <g id="text_17">

     <!-- x**2 -->

     <defs>

      <path d="M 54.890625 54.6875 

L 35.109375 28.078125 

L 55.90625 0 

L 45.3125 0 

L 29.390625 21.484375 

L 13.484375 0 

L 2.875 0 

L 24.125 28.609375 

L 4.6875 54.6875 

L 15.28125 54.6875 

L 29.78125 35.203125 

L 44.28125 54.6875 

z

" id="DejaVuSans-120"/>

      <path d="M 47.015625 60.890625 

L 29.5 51.421875 

L 47.015625 41.890625 

L 44.1875 37.109375 

L 27.78125 47.015625 

L 27.78125 28.609375 

L 22.21875 28.609375 

L 22.21875 47.015625 

L 5.8125 37.109375 

L 2.984375 41.890625 

L 20.515625 51.421875 

L 2.984375 60.890625 

L 5.8125 65.71875 

L 22.21875 55.8125 

L 22.21875 74.21875 

L 27.78125 74.21875 

L 27.78125 55.8125 

L 44.1875 65.71875 

z

" id="DejaVuSans-42"/>

     </defs>

     <g transform="translate(515.965625 161.738437)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-42"/>

      <use x="109.179688" xlink:href="#DejaVuSans-42"/>

      <use x="159.179688" xlink:href="#DejaVuSans-50"/>

     </g>

    </g>

    <g id="line2d_18">

     <path d="M 487.965625 172.916562 

L 507.965625 172.916562 

" style="fill:none;stroke:#ff7f0e;stroke-linecap:square;stroke-width:1.5;"/>

    </g>

    <g id="line2d_19"/>

    <g id="text_18">

     <!-- x**3 -->

     <g transform="translate(515.965625 176.416562)scale(0.1 -0.1)">

      <use xlink:href="#DejaVuSans-120"/>

      <use x="59.179688" xlink:href="#DejaVuSans-42"/>

      <use x="109.179688" xlink:href="#DejaVuSans-42"/>

      <use x="159.179688" xlink:href="#DejaVuSans-51"/>

     </g>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p60cb0682a8">

   <rect height="288" width="432" x="46.965625" y="22.318125"/>

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
<h3 id="Auserhalb-des-Diagrammes">Auserhalb des Diagrammes<a class="anchor-link" href="#Auserhalb-des-Diagrammes">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Subplots-in-Matplotlib">Subplots in Matplotlib<a class="anchor-link" href="#Subplots-in-Matplotlib">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Manuelle-Bef&#252;llung-von-Subplots">Manuelle Bef&#252;llung von Subplots<a class="anchor-link" href="#Manuelle-Bef&#252;llung-von-Subplots">&#182;</a></h3><p>die Arbeitsfläche af kann auf basis der achsen verändert werden. in diese af wiederum kann ich nun weitere Diagramme hineinfügen. Das ganze Diagramme heist figure123 und besteht aus meheren Subplots</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[126]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Leere Arbeitsfläche von 1 x 2 Subplots</span>
<span class="n">diag</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span><span class="p">)</span> <span class="c1"># eine Zeile &amp; zwei spalten</span>

<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Titel Position1&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="s1">&#39;r--&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;STitel Position2&quot;</span><span class="p">)</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">go ahead123 mit Label-Beschriftung</span>
<span class="sd">go ahead123mit Diagrammtyp &amp; </span>
<span class="sd">&#39;&#39;&#39;</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[126]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\ngo ahead123 mit Label-Beschriftung\ngo ahead123mit Diagrammtyp &amp; \n&#39;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="263.63625pt" version="1.1" viewBox="0 0 368.925 263.63625" width="368.925pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M -0 263.63625 

L 368.925 263.63625 

L 368.925 0 

L -0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 239.758125 

L 179.106818 239.758125 

L 179.106818 22.318125 

L 26.925 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="me8ef9cccc1" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.842355" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(30.661105 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="89.181198" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(85.999948 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="144.520041" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(141.338791 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_4">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m545e158d42" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="229.874489"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 0 -->

      <g transform="translate(13.5625 233.673707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="190.339943"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(13.5625 194.139162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="150.805398"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 10 -->

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

      <g transform="translate(7.2 154.604616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="111.270852"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 15 -->

      <g transform="translate(7.2 115.070071)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="71.736307"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 20 -->

      <g transform="translate(7.2 75.535526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m545e158d42" y="32.201761"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 25 -->

      <g transform="translate(7.2 36.00098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_10">

    <path clip-path="url(#p883eb97d0a)" d="M 33.842355 229.874489 

L 47.677066 227.897761 

L 61.511777 221.96758 

L 75.346488 212.083943 

L 89.181198 198.246852 

L 103.015909 180.456307 

L 116.85062 158.712307 

L 130.685331 133.014852 

L 144.520041 103.363943 

L 158.354752 69.75958 

L 172.189463 32.201761 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 239.758125 

L 26.925 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 179.106818 239.758125 

L 179.106818 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 239.758125 

L 179.106818 239.758125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 22.318125 

L 179.106818 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_10">

    <!-- Titel Position1 -->

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

     <path id="DejaVuSans-32"/>

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

    </defs>

    <g transform="translate(61.079659 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-84"/>

     <use x="57.958984" xlink:href="#DejaVuSans-105"/>

     <use x="85.742188" xlink:href="#DejaVuSans-116"/>

     <use x="124.951172" xlink:href="#DejaVuSans-101"/>

     <use x="186.474609" xlink:href="#DejaVuSans-108"/>

     <use x="214.257812" xlink:href="#DejaVuSans-32"/>

     <use x="246.044922" xlink:href="#DejaVuSans-80"/>

     <use x="302.722656" xlink:href="#DejaVuSans-111"/>

     <use x="363.904297" xlink:href="#DejaVuSans-115"/>

     <use x="416.003906" xlink:href="#DejaVuSans-105"/>

     <use x="443.787109" xlink:href="#DejaVuSans-116"/>

     <use x="482.996094" xlink:href="#DejaVuSans-105"/>

     <use x="510.779297" xlink:href="#DejaVuSans-111"/>

     <use x="571.960938" xlink:href="#DejaVuSans-110"/>

     <use x="635.339844" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 209.543182 239.758125 

L 361.725 239.758125 

L 361.725 22.318125 

L 209.543182 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_4">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="216.460537" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 0 -->

      <g transform="translate(213.279287 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="271.79938" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 10 -->

      <g transform="translate(265.43688 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="327.138223" xlink:href="#me8ef9cccc1" y="239.758125"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 20 -->

      <g transform="translate(320.775723 254.356563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_7">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="229.874489"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 0 -->

      <g transform="translate(196.180682 233.673707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="190.339943"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 1 -->

      <g transform="translate(196.180682 194.139162)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="150.805398"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 2 -->

      <g transform="translate(196.180682 154.604616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_10">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="111.270852"/>

      </g>

     </g>

     <g id="text_17">

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

      <g transform="translate(196.180682 115.070071)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="ytick_11">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="71.736307"/>

      </g>

     </g>

     <g id="text_18">

      <!-- 4 -->

      <g transform="translate(196.180682 75.535526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_12">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="209.543182" xlink:href="#m545e158d42" y="32.201761"/>

      </g>

     </g>

     <g id="text_19">

      <!-- 5 -->

      <g transform="translate(196.180682 36.00098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_20">

    <path clip-path="url(#p1ae987ecc8)" d="M 216.460537 229.874489 

L 217.844008 210.107216 

L 221.994421 190.339943 

L 228.911777 170.57267 

L 238.596074 150.805398 

L 251.047314 131.038125 

L 266.265496 111.270852 

L 284.25062 91.50358 

L 305.002686 71.736307 

L 328.521694 51.969034 

L 354.807645 32.201761 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_8">

    <path d="M 209.543182 239.758125 

L 209.543182 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 361.725 239.758125 

L 361.725 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 209.543182 239.758125 

L 361.725 239.758125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 209.543182 22.318125 

L 361.725 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_20">

    <!-- STitel Position2 -->

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

    </defs>

    <g transform="translate(239.888778 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-83"/>

     <use x="63.476562" xlink:href="#DejaVuSans-84"/>

     <use x="121.435547" xlink:href="#DejaVuSans-105"/>

     <use x="149.21875" xlink:href="#DejaVuSans-116"/>

     <use x="188.427734" xlink:href="#DejaVuSans-101"/>

     <use x="249.951172" xlink:href="#DejaVuSans-108"/>

     <use x="277.734375" xlink:href="#DejaVuSans-32"/>

     <use x="309.521484" xlink:href="#DejaVuSans-80"/>

     <use x="366.199219" xlink:href="#DejaVuSans-111"/>

     <use x="427.380859" xlink:href="#DejaVuSans-115"/>

     <use x="479.480469" xlink:href="#DejaVuSans-105"/>

     <use x="507.263672" xlink:href="#DejaVuSans-116"/>

     <use x="546.472656" xlink:href="#DejaVuSans-105"/>

     <use x="574.255859" xlink:href="#DejaVuSans-111"/>

     <use x="635.4375" xlink:href="#DejaVuSans-110"/>

     <use x="698.816406" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p883eb97d0a">

   <rect height="217.44" width="152.181818" x="26.925" y="22.318125"/>

  </clipPath>

  <clipPath id="p1ae987ecc8">

   <rect height="217.44" width="152.181818" x="209.543182" y="22.318125"/>

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
<div class="prompt input_prompt">In&nbsp;[127]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span><span class="mf">6.4</span><span class="p">,</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">sinf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">cosf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">tanf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">tan</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">gesamt</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>

<span class="n">diag1</span> <span class="o">=</span> <span class="n">gesamt</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">diag1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">sinf</span><span class="p">)</span>
<span class="n">diag2</span> <span class="o">=</span> <span class="n">gesamt</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="n">diag2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">cosf</span><span class="p">)</span>
<span class="n">diag2</span> <span class="o">=</span> <span class="n">gesamt</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="n">diag2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">cosf</span><span class="p">)</span>
<span class="n">gesamt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="249.42279pt" version="1.1" viewBox="0 0 370.942187 249.42279" width="370.942187pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 249.42279 

L 370.942187 249.42279 

L 370.942187 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 28.942188 72.057606 

L 363.742188 72.057606 

L 363.742188 8.104665 

L 28.942188 8.104665 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m027a990882" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="44.160369" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(40.979119 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="92.472058" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 10 -->

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

      <g transform="translate(86.109558 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="140.783746" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 20 -->

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

      <g transform="translate(134.421246 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="189.095434" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 30 -->

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

      <g transform="translate(182.732934 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="237.407123" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 40 -->

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

      <g transform="translate(231.044623 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="285.718811" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 50 -->

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

      <g transform="translate(279.356311 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="334.030499" xlink:href="#m027a990882" y="72.057606"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 60 -->

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

      <g transform="translate(327.667999 86.656044)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_8">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="ma0fca39f9b" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="69.152886"/>

      </g>

     </g>

     <g id="text_8">

      <!-- −5 -->

      <defs>

       <path d="M 10.59375 35.5 

L 73.1875 35.5 

L 73.1875 27.203125 

L 10.59375 27.203125 

z

" id="DejaVuSans-8722"/>

      </defs>

      <g transform="translate(7.2 72.952105)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="40.076052"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 0 -->

      <g transform="translate(15.579688 43.875271)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="10.999219"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 5 -->

      <g transform="translate(15.579688 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_11">

    <path clip-path="url(#p076b8a1cea)" d="M 44.160369 40.076052 

L 48.991538 37.173213 

L 53.822707 34.299377 

L 58.653876 31.48326 

L 63.485045 28.753 

L 68.316213 26.135876 

L 73.147382 23.658037 

L 77.978551 21.344242 

L 82.80972 19.217609 

L 87.640889 17.299386 

L 92.472058 15.608741 

L 97.303226 14.162564 

L 102.134395 12.975307 

L 106.965564 12.058831 

L 111.796733 11.422295 

L 116.627902 11.072057 

L 121.459071 11.011617 

L 126.290239 11.24158 

L 131.121408 11.759647 

L 135.952577 12.560642 

L 140.783746 13.636562 

L 145.614915 14.976657 

L 150.446084 16.567537 

L 155.277252 18.393306 

L 160.108421 20.435722 

L 164.93959 22.674377 

L 169.770759 25.086905 

L 174.601928 27.649199 

L 179.433097 30.335658 

L 184.264265 33.119439 

L 189.095434 35.972729 

L 193.926603 38.867018 

L 198.757772 41.773388 

L 203.588941 44.662798 

L 208.42011 47.506378 

L 213.251278 50.275718 

L 218.082447 52.943146 

L 222.913616 55.48201 

L 227.744785 57.866942 

L 232.575954 60.074114 

L 237.407123 62.081473 

L 242.238291 63.86896 

L 247.06946 65.418716 

L 251.900629 66.715257 

L 256.731798 67.745627 

L 261.562967 68.499533 

L 266.394136 68.96944 

L 271.225304 69.150654 

L 276.056473 69.041365 

L 280.887642 68.642663 

L 285.718811 67.958534 

L 290.54998 66.995812 

L 295.381149 65.764116 

L 300.212317 64.275754 

L 305.043486 62.545597 

L 309.874655 60.590931 

L 314.705824 58.431287 

L 319.536993 56.088244 

L 324.368162 53.585213 

L 329.19933 50.947202 

L 334.030499 48.20057 

L 338.861668 45.372761 

L 343.692837 42.492029 

L 348.524006 39.587157 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 28.942188 72.057606 

L 28.942188 8.104665 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 363.742188 72.057606 

L 363.742188 8.104665 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 28.942188 72.057606 

L 363.742188 72.057606 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 28.942188 8.104665 

L 363.742188 8.104665 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 28.942188 148.801136 

L 363.742188 148.801136 

L 363.742188 84.848195 

L 28.942188 84.848195 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_8">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="44.160369" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 0 -->

      <g transform="translate(40.979119 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="92.472058" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 10 -->

      <g transform="translate(86.109558 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_10">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="140.783746" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 20 -->

      <g transform="translate(134.421246 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_11">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="189.095434" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 30 -->

      <g transform="translate(182.732934 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_12">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="237.407123" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 40 -->

      <g transform="translate(231.044623 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_13">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="285.718811" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 50 -->

      <g transform="translate(279.356311 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_14">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="334.030499" xlink:href="#m027a990882" y="148.801136"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 60 -->

      <g transform="translate(327.667999 163.399573)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_4">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="145.919336"/>

      </g>

     </g>

     <g id="text_18">

      <!-- −5 -->

      <g transform="translate(7.2 149.718554)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_20">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="116.837241"/>

      </g>

     </g>

     <g id="text_19">

      <!-- 0 -->

      <g transform="translate(15.579688 120.63646)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_21">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="87.755146"/>

      </g>

     </g>

     <g id="text_20">

      <!-- 5 -->

      <g transform="translate(15.579688 91.554365)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_22">

    <path clip-path="url(#p61710f0acf)" d="M 44.160369 87.755146 

L 48.991538 87.900436 

L 53.822707 88.334852 

L 58.653876 89.054055 

L 63.485045 90.050858 

L 68.316213 91.315302 

L 73.147382 92.834753 

L 77.978551 94.594028 

L 82.80972 96.575551 

L 87.640889 98.759521 

L 92.472058 101.124118 

L 97.303226 103.645716 

L 102.134395 106.299119 

L 106.965564 109.057815 

L 111.796733 111.89424 

L 116.627902 114.780055 

L 121.459071 117.686424 

L 126.290239 120.584309 

L 131.121408 123.444754 

L 135.952577 126.239179 

L 140.783746 128.939663 

L 145.614915 131.519223 

L 150.446084 133.952086 

L 155.277252 136.213943 

L 160.108421 138.282195 

L 164.93959 140.136175 

L 169.770759 141.757361 

L 174.601928 143.129552 

L 179.433097 144.23904 

L 184.264265 145.074738 

L 189.095434 145.628296 

L 193.926603 145.894184 

L 198.757772 145.869744 

L 203.588941 145.555221 

L 208.42011 144.953757 

L 213.251278 144.071363 

L 218.082447 142.916854 

L 222.913616 141.501766 

L 227.744785 139.840239 

L 232.575954 137.948873 

L 237.407123 135.846567 

L 242.238291 133.554325 

L 247.06946 131.095053 

L 251.900629 128.49332 

L 256.731798 125.775125 

L 261.562967 122.967624 

L 266.394136 120.098871 

L 271.225304 117.197529 

L 276.056473 114.292587 

L 280.887642 111.413071 

L 285.718811 108.58775 

L 290.54998 105.844857 

L 295.381149 103.211795 

L 300.212317 100.714874 

L 305.043486 98.379043 

L 309.874655 96.22764 

L 314.705824 94.282161 

L 319.536993 92.562045 

L 324.368162 91.084479 

L 329.19933 89.864226 

L 334.030499 88.913478 

L 338.861668 88.241735 

L 343.692837 87.855709 

L 348.524006 87.759258 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_8">

    <path d="M 28.942188 148.801136 

L 28.942188 84.848195 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 363.742188 148.801136 

L 363.742188 84.848195 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 28.942188 148.801136 

L 363.742188 148.801136 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 28.942188 84.848195 

L 363.742188 84.848195 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_3">

   <g id="patch_12">

    <path d="M 28.942188 225.544665 

L 363.742188 225.544665 

L 363.742188 161.591724 

L 28.942188 161.591724 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_5">

    <g id="xtick_15">

     <g id="line2d_23">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="44.160369" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_21">

      <!-- 0 -->

      <g transform="translate(40.979119 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_16">

     <g id="line2d_24">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="92.472058" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_22">

      <!-- 10 -->

      <g transform="translate(86.109558 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_17">

     <g id="line2d_25">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="140.783746" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_23">

      <!-- 20 -->

      <g transform="translate(134.421246 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_18">

     <g id="line2d_26">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="189.095434" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_24">

      <!-- 30 -->

      <g transform="translate(182.732934 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_19">

     <g id="line2d_27">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="237.407123" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_25">

      <!-- 40 -->

      <g transform="translate(231.044623 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_20">

     <g id="line2d_28">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="285.718811" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_26">

      <!-- 50 -->

      <g transform="translate(279.356311 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_21">

     <g id="line2d_29">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="334.030499" xlink:href="#m027a990882" y="225.544665"/>

      </g>

     </g>

     <g id="text_27">

      <!-- 60 -->

      <g transform="translate(327.667999 240.143103)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_6">

    <g id="ytick_7">

     <g id="line2d_30">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="222.662865"/>

      </g>

     </g>

     <g id="text_28">

      <!-- −5 -->

      <g transform="translate(7.2 226.462084)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_31">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="193.58077"/>

      </g>

     </g>

     <g id="text_29">

      <!-- 0 -->

      <g transform="translate(15.579688 197.379989)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_32">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#ma0fca39f9b" y="164.498676"/>

      </g>

     </g>

     <g id="text_30">

      <!-- 5 -->

      <g transform="translate(15.579688 168.297895)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_33">

    <path clip-path="url(#p6a31184d5a)" d="M 44.160369 164.498676 

L 48.991538 164.643965 

L 53.822707 165.078382 

L 58.653876 165.797584 

L 63.485045 166.794387 

L 68.316213 168.058831 

L 73.147382 169.578282 

L 77.978551 171.337558 

L 82.80972 173.31908 

L 87.640889 175.503051 

L 92.472058 177.867648 

L 97.303226 180.389245 

L 102.134395 183.042648 

L 106.965564 185.801344 

L 111.796733 188.63777 

L 116.627902 191.523584 

L 121.459071 194.429954 

L 126.290239 197.327838 

L 131.121408 200.188283 

L 135.952577 202.982708 

L 140.783746 205.683192 

L 145.614915 208.262753 

L 150.446084 210.695616 

L 155.277252 212.957473 

L 160.108421 215.025724 

L 164.93959 216.879705 

L 169.770759 218.50089 

L 174.601928 219.873082 

L 179.433097 220.98257 

L 184.264265 221.818268 

L 189.095434 222.371826 

L 193.926603 222.637713 

L 198.757772 222.613273 

L 203.588941 222.29875 

L 208.42011 221.697287 

L 213.251278 220.814892 

L 218.082447 219.660383 

L 222.913616 218.245296 

L 227.744785 216.583768 

L 232.575954 214.692402 

L 237.407123 212.590096 

L 242.238291 210.297855 

L 247.06946 207.838582 

L 251.900629 205.23685 

L 256.731798 202.518654 

L 261.562967 199.711154 

L 266.394136 196.842401 

L 271.225304 193.941059 

L 276.056473 191.036117 

L 280.887642 188.1566 

L 285.718811 185.33128 

L 290.54998 182.588386 

L 295.381149 179.955324 

L 300.212317 177.458404 

L 305.043486 175.122572 

L 309.874655 172.971169 

L 314.705824 171.02569 

L 319.536993 169.305574 

L 324.368162 167.828008 

L 329.19933 166.607755 

L 334.030499 165.657007 

L 338.861668 164.985265 

L 343.692837 164.599239 

L 348.524006 164.502787 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_13">

    <path d="M 28.942188 225.544665 

L 28.942188 161.591724 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_14">

    <path d="M 363.742188 225.544665 

L 363.742188 161.591724 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_15">

    <path d="M 28.942188 225.544665 

L 363.742188 225.544665 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_16">

    <path d="M 28.942188 161.591724 

L 363.742188 161.591724 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p076b8a1cea">

   <rect height="63.952941" width="334.8" x="28.942188" y="8.104665"/>

  </clipPath>

  <clipPath id="p61710f0acf">

   <rect height="63.952941" width="334.8" x="28.942188" y="84.848195"/>

  </clipPath>

  <clipPath id="p6a31184d5a">

   <rect height="63.952941" width="334.8" x="28.942188" y="161.591724"/>

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
<h2 id="Beschriftung-Datenpunkte">Beschriftung Datenpunkte<a class="anchor-link" href="#Beschriftung-Datenpunkte">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[128]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span><span class="mf">6.4</span><span class="p">,</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">sinf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">cosf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">tanf</span> <span class="o">=</span> <span class="mi">5</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">tan</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
<span class="n">gesamt</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">()</span>


<span class="n">diag1</span> <span class="o">=</span> <span class="n">gesamt</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">diag1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">sinf</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[128]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30811bc40&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="248.518125pt" version="1.1" viewBox="0 0 370.942187 248.518125" width="370.942187pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 248.518125 

L 370.942187 248.518125 

L 370.942187 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 28.942188 224.64 

L 363.742188 224.64 

L 363.742188 7.2 

L 28.942188 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m10de25d9dc" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="44.160369" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(40.979119 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="92.472058" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 10 -->

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

      <g transform="translate(86.109558 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="140.783746" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 20 -->

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

      <g transform="translate(134.421246 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="189.095434" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 30 -->

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

      <g transform="translate(182.732934 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="237.407123" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 40 -->

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

      <g transform="translate(231.044623 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="285.718811" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 50 -->

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

      <g transform="translate(279.356311 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="334.030499" xlink:href="#m10de25d9dc" y="224.64"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 60 -->

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

      <g transform="translate(327.667999 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_8">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="mceab1a791d" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#mceab1a791d" y="194.991704"/>

      </g>

     </g>

     <g id="text_8">

      <!-- −4 -->

      <defs>

       <path d="M 10.59375 35.5 

L 73.1875 35.5 

L 73.1875 27.203125 

L 10.59375 27.203125 

z

" id="DejaVuSans-8722"/>

      </defs>

      <g transform="translate(7.2 198.790922)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#mceab1a791d" y="155.44721"/>

      </g>

     </g>

     <g id="text_9">

      <!-- −2 -->

      <g transform="translate(7.2 159.246429)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#mceab1a791d" y="115.902716"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 0 -->

      <g transform="translate(15.579688 119.701935)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#mceab1a791d" y="76.358223"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 2 -->

      <g transform="translate(15.579688 80.157441)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="28.942188" xlink:href="#mceab1a791d" y="36.813729"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 4 -->

      <g transform="translate(15.579688 40.612948)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#p926da7d5be)" d="M 44.160369 115.902716 

L 48.991538 106.033062 

L 53.822707 96.262021 

L 58.653876 86.687224 

L 63.485045 77.404338 

L 68.316213 68.506116 

L 73.147382 60.081465 

L 77.978551 52.214561 

L 82.80972 44.984008 

L 87.640889 38.462051 

L 92.472058 32.713856 

L 97.303226 27.796857 

L 102.134395 23.760182 

L 106.965564 20.644165 

L 111.796733 18.47994 

L 116.627902 17.289131 

L 121.459071 17.083636 

L 126.290239 17.865509 

L 131.121408 19.626938 

L 135.952577 22.350322 

L 140.783746 26.008451 

L 145.614915 30.564773 

L 150.446084 35.973764 

L 155.277252 42.181379 

L 160.108421 49.125593 

L 164.93959 56.737022 

L 169.770759 64.939615 

L 174.601928 73.651414 

L 179.433097 82.785374 

L 184.264265 92.250232 

L 189.095434 101.951418 

L 193.926603 111.792001 

L 198.757772 121.673656 

L 203.588941 131.49765 

L 208.42011 141.165825 

L 213.251278 150.581579 

L 218.082447 159.650834 

L 222.913616 168.282971 

L 227.744785 176.391743 

L 232.575954 183.896128 

L 237.407123 190.721145 

L 242.238291 196.798601 

L 247.06946 202.067773 

L 251.900629 206.476012 

L 256.731798 209.979272 

L 261.562967 212.54255 

L 266.394136 214.140235 

L 271.225304 214.756364 

L 276.056473 214.384779 

L 280.887642 213.029194 

L 285.718811 210.703154 

L 290.54998 207.429898 

L 295.381149 203.242134 

L 300.212317 198.181703 

L 305.043486 192.299167 

L 309.874655 185.653304 

L 314.705824 178.310515 

L 319.536993 170.344169 

L 324.368162 161.833861 

L 329.19933 152.864625 

L 334.030499 143.526077 

L 338.861668 133.911526 

L 343.692837 124.117037 

L 348.524006 114.240473 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 28.942188 224.64 

L 28.942188 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 363.742188 224.64 

L 363.742188 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 28.942188 224.64 

L 363.742188 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 28.942188 7.2 

L 363.742188 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p926da7d5be">

   <rect height="217.44" width="334.8" x="28.942188" y="7.2"/>

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
<h3 id="Basics-f&#252;r-die-automatische-Bef&#252;llung-von-Subplots">Basics f&#252;r die automatische Bef&#252;llung von Subplots<a class="anchor-link" href="#Basics-f&#252;r-die-automatische-Bef&#252;llung-von-Subplots">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[129]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span><span class="p">)</span> <span class="c1"># hier lege ich die Anzahl der Axes fest</span>
<span class="nb">print</span><span class="p">(</span><span class="n">axes</span><span class="p">)</span><span class="c1"># durch die Axes kann ich iterieren. Die anzahl der Axes </span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">axes</span><span class="p">))</span> <span class="c1"># =&gt; = nd.array =&gt; ergo kann ich darüber itterieren</span>
<span class="sd">&#39;&#39;&#39;</span>
<span class="sd">Diese Ittartionsmöglichkeit ist wichtig wenn ich später die Diagramme on the fly publishen möchte</span>
<span class="sd">&#39;&#39;&#39;</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001C308C5C910&gt;
 &lt;matplotlib.axes._subplots.AxesSubplot object at 0x000001C308BA2D00&gt;]
&lt;class &#39;numpy.ndarray&#39;&gt;
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[129]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&#39;\nDiese Ittartionsmöglichkeit ist wichtig wenn ich später die Diagramme on the fly publishen möchte\n&#39;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="252.317344pt" version="1.1" viewBox="0 0 380.054687 252.317344" width="380.054687pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 252.317344 

L 380.054687 252.317344 

L 380.054687 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 30.103125 228.439219 

L 182.284943 228.439219 

L 182.284943 10.999219 

L 30.103125 10.999219 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mb4d4168bd9" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0.0 -->

      <defs>

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

      <g transform="translate(22.151563 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="60.539489" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 0.2 -->

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

      <g transform="translate(52.587926 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="90.975852" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0.4 -->

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

      <g transform="translate(83.02429 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="121.412216" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 0.6 -->

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

      <g transform="translate(113.460653 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="151.84858" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 0.8 -->

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

      </defs>

      <g transform="translate(143.897017 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="182.284943" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 1.0 -->

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

      <g transform="translate(174.333381 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m057cd85de6" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="228.439219"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0.0 -->

      <g transform="translate(7.2 232.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="184.951219"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 0.2 -->

      <g transform="translate(7.2 188.750437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="141.463219"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 0.4 -->

      <g transform="translate(7.2 145.262437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="97.975219"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 0.6 -->

      <g transform="translate(7.2 101.774437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="54.487219"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 0.8 -->

      <g transform="translate(7.2 58.286437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.103125" xlink:href="#m057cd85de6" y="10.999219"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 1.0 -->

      <g transform="translate(7.2 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_3">

    <path d="M 30.103125 228.439219 

L 30.103125 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 182.284943 228.439219 

L 182.284943 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 30.103125 228.439219 

L 182.284943 228.439219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 30.103125 10.999219 

L 182.284943 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 212.721307 228.439219 

L 364.903125 228.439219 

L 364.903125 10.999219 

L 212.721307 10.999219 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 0.0 -->

      <g transform="translate(204.769744 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="243.15767" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 0.2 -->

      <g transform="translate(235.206108 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="273.594034" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 0.4 -->

      <g transform="translate(265.642472 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_10">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="304.030398" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 0.6 -->

      <g transform="translate(296.078835 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="xtick_11">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="334.466761" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 0.8 -->

      <g transform="translate(326.515199 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="xtick_12">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="364.903125" xlink:href="#mb4d4168bd9" y="228.439219"/>

      </g>

     </g>

     <g id="text_18">

      <!-- 1.0 -->

      <g transform="translate(356.951562 243.037656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_7">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="228.439219"/>

      </g>

     </g>

     <g id="text_19">

      <!-- 0.0 -->

      <g transform="translate(189.818182 232.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_20">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="184.951219"/>

      </g>

     </g>

     <g id="text_20">

      <!-- 0.2 -->

      <g transform="translate(189.818182 188.750437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_21">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="141.463219"/>

      </g>

     </g>

     <g id="text_21">

      <!-- 0.4 -->

      <g transform="translate(189.818182 145.262437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_10">

     <g id="line2d_22">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="97.975219"/>

      </g>

     </g>

     <g id="text_22">

      <!-- 0.6 -->

      <g transform="translate(189.818182 101.774437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_11">

     <g id="line2d_23">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="54.487219"/>

      </g>

     </g>

     <g id="text_23">

      <!-- 0.8 -->

      <g transform="translate(189.818182 58.286437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_12">

     <g id="line2d_24">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="212.721307" xlink:href="#m057cd85de6" y="10.999219"/>

      </g>

     </g>

     <g id="text_24">

      <!-- 1.0 -->

      <g transform="translate(189.818182 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_8">

    <path d="M 212.721307 228.439219 

L 212.721307 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 364.903125 228.439219 

L 364.903125 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 212.721307 228.439219 

L 364.903125 228.439219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 212.721307 10.999219 

L 364.903125 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

</svg>


</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[130]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># BspIteation durch die Axes</span>
<span class="c1"># Das ganze wird natürlich deutlich interssanter, wenn ich mehrere unterschiedliche Listen abbilde</span>
<span class="c1"># Vorteil ist dass hier </span>
<span class="k">for</span> <span class="n">ax</span> <span class="ow">in</span> <span class="n">axes</span><span class="p">:</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;x&#39;</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;y&#39;</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;titel&#39;</span><span class="p">)</span>

<span class="c1"># Anzeigen</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Diagrammg&#246;&#223;e-//-Gr&#246;&#223;e-Arbeitsfl&#228;che">Diagrammg&#246;&#223;e // Gr&#246;&#223;e Arbeitsfl&#228;che<a class="anchor-link" href="#Diagrammg&#246;&#223;e-//-Gr&#246;&#223;e-Arbeitsfl&#228;che">&#182;</a></h2><p>egal ob subplot oder nicht hier kann ich die größe der Arbeitsfläche mit der Variabel Figsize definieren</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[131]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bsp1</span>
<span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">100</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[131]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c308e8e040&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="103.078125pt" version="1.1" viewBox="0 0 106.125 103.078125" width="106.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 103.078125 

L 106.125 103.078125 

L 106.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 79.2 

L 98.925 79.2 

L 98.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="ma1e2d7f555" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.197727" xlink:href="#ma1e2d7f555" y="79.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.016477 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="95.652273" xlink:href="#ma1e2d7f555" y="79.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(92.471023 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_3">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m699b082d67" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m699b082d67" y="75.927273"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(13.5625 79.726491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m699b082d67" y="49.745455"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 10 -->

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

      <g transform="translate(7.2 53.544673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m699b082d67" y="23.563636"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 20 -->

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

      <g transform="translate(7.2 27.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#pb18223741b)" d="M 30.197727 75.927273 

L 36.743182 75.272727 

L 43.288636 73.309091 

L 49.834091 70.036364 

L 56.379545 65.454545 

L 62.925 59.563636 

L 69.470455 52.363636 

L 76.015909 43.854545 

L 82.561364 34.036364 

L 89.106818 22.909091 

L 95.652273 10.472727 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 79.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 98.925 79.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 79.2 

L 98.925 79.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pb18223741b">

   <rect height="72" width="72" x="26.925" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[132]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">100</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[132]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c308bf8be0&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="175.078125pt" version="1.1" viewBox="0 0 178.125 175.078125" width="178.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 175.078125 

L 178.125 175.078125 

L 178.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 151.2 

L 170.925 151.2 

L 170.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="ma628d7e1b6" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.470455" xlink:href="#ma628d7e1b6" y="151.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(30.289205 165.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="85.834091" xlink:href="#ma628d7e1b6" y="151.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(82.652841 165.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="138.197727" xlink:href="#ma628d7e1b6" y="151.2"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(135.016477 165.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_4">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m0bd271103d" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="144.654545"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 0 -->

      <g transform="translate(13.5625 148.453764)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="118.472727"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(13.5625 122.271946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="92.290909"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 10 -->

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

      <g transform="translate(7.2 96.090128)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="66.109091"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 15 -->

      <g transform="translate(7.2 69.90831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="39.927273"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 20 -->

      <g transform="translate(7.2 43.726491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m0bd271103d" y="13.745455"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 25 -->

      <g transform="translate(7.2 17.544673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_10">

    <path clip-path="url(#p1ef8bb7d7c)" d="M 33.470455 144.654545 

L 46.561364 143.345455 

L 59.652273 139.418182 

L 72.743182 132.872727 

L 85.834091 123.709091 

L 98.925 111.927273 

L 112.015909 97.527273 

L 125.106818 80.509091 

L 138.197727 60.872727 

L 151.288636 38.618182 

L 164.379545 13.745455 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 151.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 170.925 151.2 

L 170.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 151.2 

L 170.925 151.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 170.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p1ef8bb7d7c">

   <rect height="144" width="144" x="26.925" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[133]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bsp-Subplots</span>
<span class="n">diag</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span> <span class="c1"># eine Zeile &amp; zwei spalten</span>

<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Titel Position1&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="s1">&#39;r--&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;STitel Position2&quot;</span><span class="p">)</span>
<span class="n">diag</span>    
<span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="135.59625pt" version="1.1" viewBox="0 0 167.155994 135.59625" width="167.155994pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 135.59625 

L 167.155994 135.59625 

L 167.155994 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 40.572898 111.718125 

L 57.699602 111.718125 

L 57.699602 22.318125 

L 40.572898 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m107111c4f0" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="41.351384" xlink:href="#m107111c4f0" y="111.718125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(38.170134 126.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="56.921116" xlink:href="#m107111c4f0" y="111.718125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(53.739866 126.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_3">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m8b5063f86b" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.572898" xlink:href="#m8b5063f86b" y="107.654489"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(27.210398 111.453707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.572898" xlink:href="#m8b5063f86b" y="75.145398"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 10 -->

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

      <g transform="translate(20.847898 78.944616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="40.572898" xlink:href="#m8b5063f86b" y="42.636307"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 20 -->

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

      <g transform="translate(20.847898 46.435526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#p8873340fa5)" d="M 41.351384 107.654489 

L 42.908357 106.841761 

L 44.465331 104.40358 

L 46.022304 100.339943 

L 47.579277 94.650852 

L 49.13625 87.336307 

L 50.693223 78.396307 

L 52.250196 67.830852 

L 53.807169 55.639943 

L 55.364143 41.82358 

L 56.921116 26.381761 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 40.572898 111.718125 

L 40.572898 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 57.699602 111.718125 

L 57.699602 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 40.572898 111.718125 

L 57.699602 111.718125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 40.572898 22.318125 

L 57.699602 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_6">

    <!-- Titel Position1 -->

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

     <path id="DejaVuSans-32"/>

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

    </defs>

    <g transform="translate(7.2 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-84"/>

     <use x="57.958984" xlink:href="#DejaVuSans-105"/>

     <use x="85.742188" xlink:href="#DejaVuSans-116"/>

     <use x="124.951172" xlink:href="#DejaVuSans-101"/>

     <use x="186.474609" xlink:href="#DejaVuSans-108"/>

     <use x="214.257812" xlink:href="#DejaVuSans-32"/>

     <use x="246.044922" xlink:href="#DejaVuSans-80"/>

     <use x="302.722656" xlink:href="#DejaVuSans-111"/>

     <use x="363.904297" xlink:href="#DejaVuSans-115"/>

     <use x="416.003906" xlink:href="#DejaVuSans-105"/>

     <use x="443.787109" xlink:href="#DejaVuSans-116"/>

     <use x="482.996094" xlink:href="#DejaVuSans-105"/>

     <use x="510.779297" xlink:href="#DejaVuSans-111"/>

     <use x="571.960938" xlink:href="#DejaVuSans-110"/>

     <use x="635.339844" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 105.64733 111.718125 

L 122.774034 111.718125 

L 122.774034 22.318125 

L 105.64733 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_3">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="106.425816" xlink:href="#m107111c4f0" y="111.718125"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(103.244566 126.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="121.995548" xlink:href="#m107111c4f0" y="111.718125"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 25 -->

      <g transform="translate(115.633048 126.316563)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_4">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="105.64733" xlink:href="#m8b5063f86b" y="107.654489"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 0 -->

      <g transform="translate(92.28483 111.453707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="105.64733" xlink:href="#m8b5063f86b" y="75.145398"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 2 -->

      <g transform="translate(92.28483 78.944616)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="105.64733" xlink:href="#m8b5063f86b" y="42.636307"/>

      </g>

     </g>

     <g id="text_11">

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

      <g transform="translate(92.28483 46.435526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_12">

    <path clip-path="url(#p7378446390)" d="M 106.425816 107.654489 

L 106.581513 99.527216 

L 107.048605 91.399943 

L 107.827092 83.27267 

L 108.916973 75.145398 

L 110.318249 67.018125 

L 112.030919 58.890852 

L 114.054985 50.76358 

L 116.390444 42.636307 

L 119.037299 34.509034 

L 121.995548 26.381761 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_8">

    <path d="M 105.64733 111.718125 

L 105.64733 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 122.774034 111.718125 

L 122.774034 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 105.64733 111.718125 

L 122.774034 111.718125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 105.64733 22.318125 

L 122.774034 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_12">

    <!-- STitel Position2 -->

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

    </defs>

    <g transform="translate(68.465369 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-83"/>

     <use x="63.476562" xlink:href="#DejaVuSans-84"/>

     <use x="121.435547" xlink:href="#DejaVuSans-105"/>

     <use x="149.21875" xlink:href="#DejaVuSans-116"/>

     <use x="188.427734" xlink:href="#DejaVuSans-101"/>

     <use x="249.951172" xlink:href="#DejaVuSans-108"/>

     <use x="277.734375" xlink:href="#DejaVuSans-32"/>

     <use x="309.521484" xlink:href="#DejaVuSans-80"/>

     <use x="366.199219" xlink:href="#DejaVuSans-111"/>

     <use x="427.380859" xlink:href="#DejaVuSans-115"/>

     <use x="479.480469" xlink:href="#DejaVuSans-105"/>

     <use x="507.263672" xlink:href="#DejaVuSans-116"/>

     <use x="546.472656" xlink:href="#DejaVuSans-105"/>

     <use x="574.255859" xlink:href="#DejaVuSans-111"/>

     <use x="635.4375" xlink:href="#DejaVuSans-110"/>

     <use x="698.816406" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p8873340fa5">

   <rect height="89.4" width="17.126705" x="40.572898" y="22.318125"/>

  </clipPath>

  <clipPath id="p7378446390">

   <rect height="89.4" width="17.126705" x="105.64733" y="22.318125"/>

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
<div class="prompt input_prompt">In&nbsp;[134]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bsp-Subplots</span>
<span class="n">diag</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span> <span class="c1"># eine Zeile &amp; zwei spalten</span>

<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Titel Position1&quot;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="s1">&#39;r--&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;STitel Position2&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[134]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;STitel Position2&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="154.91625pt" version="1.1" viewBox="0 0 592.125 154.91625" width="592.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 154.91625 

L 592.125 154.91625 

L 592.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 131.038125 

L 280.561364 131.038125 

L 280.561364 22.318125 

L 26.925 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m7116cd6f72" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="38.453926" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(35.272676 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="84.569628" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(81.388378 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="130.685331" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(127.504081 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="176.801033" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(173.619783 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="222.916736" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(219.735486 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="269.032438" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(265.851188 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="mdbda022846" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mdbda022846" y="126.096307"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(13.5625 129.895526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mdbda022846" y="86.561761"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 10 -->

      <g transform="translate(7.2 90.36098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mdbda022846" y="47.027216"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 20 -->

      <g transform="translate(7.2 50.826435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_10">

    <path clip-path="url(#p033a9c4040)" d="M 38.453926 126.096307 

L 61.511777 125.107943 

L 84.569628 122.142852 

L 107.627479 117.201034 

L 130.685331 110.282489 

L 153.743182 101.387216 

L 176.801033 90.515216 

L 199.858884 77.666489 

L 222.916736 62.841034 

L 245.974587 46.038852 

L 269.032438 27.259943 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 131.038125 

L 26.925 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 280.561364 131.038125 

L 280.561364 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 131.038125 

L 280.561364 131.038125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 22.318125 

L 280.561364 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_10">

    <!-- Titel Position1 -->

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

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

     <path id="DejaVuSans-32"/>

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

    </defs>

    <g transform="translate(111.806932 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-84"/>

     <use x="57.958984" xlink:href="#DejaVuSans-105"/>

     <use x="85.742188" xlink:href="#DejaVuSans-116"/>

     <use x="124.951172" xlink:href="#DejaVuSans-101"/>

     <use x="186.474609" xlink:href="#DejaVuSans-108"/>

     <use x="214.257812" xlink:href="#DejaVuSans-32"/>

     <use x="246.044922" xlink:href="#DejaVuSans-80"/>

     <use x="302.722656" xlink:href="#DejaVuSans-111"/>

     <use x="363.904297" xlink:href="#DejaVuSans-115"/>

     <use x="416.003906" xlink:href="#DejaVuSans-105"/>

     <use x="443.787109" xlink:href="#DejaVuSans-116"/>

     <use x="482.996094" xlink:href="#DejaVuSans-105"/>

     <use x="510.779297" xlink:href="#DejaVuSans-111"/>

     <use x="571.960938" xlink:href="#DejaVuSans-110"/>

     <use x="635.339844" xlink:href="#DejaVuSans-49"/>

    </g>

   </g>

  </g>

  <g id="axes_2">

   <g id="patch_7">

    <path d="M 331.288636 131.038125 

L 584.925 131.038125 

L 584.925 22.318125 

L 331.288636 22.318125 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_3">

    <g id="xtick_7">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="342.817562" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 0 -->

      <g transform="translate(339.636312 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="388.933264" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 5 -->

      <g transform="translate(385.752014 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="xtick_9">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="435.048967" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 10 -->

      <g transform="translate(428.686467 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_10">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="481.164669" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 15 -->

      <g transform="translate(474.802169 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="xtick_11">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="527.280372" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 20 -->

      <g transform="translate(520.917872 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_12">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="573.396074" xlink:href="#m7116cd6f72" y="131.038125"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 25 -->

      <g transform="translate(567.033574 145.636562)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_4">

    <g id="ytick_4">

     <g id="line2d_17">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="331.288636" xlink:href="#mdbda022846" y="126.096307"/>

      </g>

     </g>

     <g id="text_17">

      <!-- 0 -->

      <g transform="translate(317.926136 129.895526)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_18">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="331.288636" xlink:href="#mdbda022846" y="86.561761"/>

      </g>

     </g>

     <g id="text_18">

      <!-- 2 -->

      <g transform="translate(317.926136 90.36098)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_19">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="331.288636" xlink:href="#mdbda022846" y="47.027216"/>

      </g>

     </g>

     <g id="text_19">

      <!-- 4 -->

      <g transform="translate(317.926136 50.826435)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_20">

    <path clip-path="url(#pe20411ed95)" d="M 342.817562 126.096307 

L 345.123347 116.21267 

L 352.040702 106.329034 

L 363.569628 96.445398 

L 379.710124 86.561761 

L 400.46219 76.678125 

L 425.825826 66.794489 

L 455.801033 56.910852 

L 490.38781 47.027216 

L 529.586157 37.14358 

L 573.396074 27.259943 

" style="fill:none;stroke:#ff0000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_8">

    <path d="M 331.288636 131.038125 

L 331.288636 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_9">

    <path d="M 584.925 131.038125 

L 584.925 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_10">

    <path d="M 331.288636 131.038125 

L 584.925 131.038125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_11">

    <path d="M 331.288636 22.318125 

L 584.925 22.318125 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="text_20">

    <!-- STitel Position2 -->

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

    </defs>

    <g transform="translate(412.361506 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-83"/>

     <use x="63.476562" xlink:href="#DejaVuSans-84"/>

     <use x="121.435547" xlink:href="#DejaVuSans-105"/>

     <use x="149.21875" xlink:href="#DejaVuSans-116"/>

     <use x="188.427734" xlink:href="#DejaVuSans-101"/>

     <use x="249.951172" xlink:href="#DejaVuSans-108"/>

     <use x="277.734375" xlink:href="#DejaVuSans-32"/>

     <use x="309.521484" xlink:href="#DejaVuSans-80"/>

     <use x="366.199219" xlink:href="#DejaVuSans-111"/>

     <use x="427.380859" xlink:href="#DejaVuSans-115"/>

     <use x="479.480469" xlink:href="#DejaVuSans-105"/>

     <use x="507.263672" xlink:href="#DejaVuSans-116"/>

     <use x="546.472656" xlink:href="#DejaVuSans-105"/>

     <use x="574.255859" xlink:href="#DejaVuSans-111"/>

     <use x="635.4375" xlink:href="#DejaVuSans-110"/>

     <use x="698.816406" xlink:href="#DejaVuSans-50"/>

    </g>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p033a9c4040">

   <rect height="108.72" width="253.636364" x="26.925" y="22.318125"/>

  </clipPath>

  <clipPath id="pe20411ed95">

   <rect height="108.72" width="253.636364" x="331.288636" y="22.318125"/>

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
<h2 id="Linienkonfigurationen-(Farben,-Stricheliert,-Bold,-Marker)">Linienkonfigurationen (Farben, Stricheliert, Bold, Marker)<a class="anchor-link" href="#Linienkonfigurationen-(Farben,-Stricheliert,-Bold,-Marker)">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[135]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># MatLab Style</span>
<span class="n">diag</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;b.-&#39;</span><span class="p">)</span> <span class="c1"># blaue Linie mit Punkten</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">3</span><span class="p">,</span> <span class="s1">&#39;g--&#39;</span><span class="p">)</span> <span class="c1"># grüne gestrichelte Lini</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[135]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30a075880&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="248.518125pt" version="1.1" viewBox="0 0 375.2875 248.518125" width="375.2875pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 248.518125 

L 375.2875 248.518125 

L 375.2875 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 33.2875 224.64 

L 368.0875 224.64 

L 368.0875 7.2 

L 33.2875 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mc9ab54e6df" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="48.505682" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(45.324432 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="109.378409" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(106.197159 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="170.251136" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(167.069886 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="231.123864" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(227.942614 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="291.996591" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(288.815341 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="352.869318" xlink:href="#mc9ab54e6df" y="224.64"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(349.688068 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m1e3c52125b" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="214.756364"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(19.925 218.555582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="183.128727"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 20 -->

      <g transform="translate(13.5625 186.927946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="151.501091"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 40 -->

      <g transform="translate(13.5625 155.30031)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="119.873455"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 60 -->

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

      <g transform="translate(13.5625 123.672673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="88.245818"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 80 -->

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

      </defs>

      <g transform="translate(13.5625 92.045037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="56.618182"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 100 -->

      <g transform="translate(7.2 60.417401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="33.2875" xlink:href="#m1e3c52125b" y="24.990545"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 120 -->

      <g transform="translate(7.2 28.789764)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_14">

    <path clip-path="url(#p22b06f4576)" d="M 48.505682 214.756364 

L 78.942045 214.361018 

L 109.378409 213.174982 

L 139.814773 211.198255 

L 170.251136 208.430836 

L 200.6875 204.872727 

L 231.123864 200.523927 

L 261.560227 195.384436 

L 291.996591 189.454255 

L 322.432955 182.733382 

L 352.869318 175.221818 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:1.5;"/>

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

" id="m2fa7b82d79" style="stroke:#0000ff;"/>

    </defs>

    <g clip-path="url(#p22b06f4576)">

     <use style="fill:#0000ff;stroke:#0000ff;" x="48.505682" xlink:href="#m2fa7b82d79" y="214.756364"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="78.942045" xlink:href="#m2fa7b82d79" y="214.361018"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="109.378409" xlink:href="#m2fa7b82d79" y="213.174982"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="139.814773" xlink:href="#m2fa7b82d79" y="211.198255"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="170.251136" xlink:href="#m2fa7b82d79" y="208.430836"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="200.6875" xlink:href="#m2fa7b82d79" y="204.872727"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="231.123864" xlink:href="#m2fa7b82d79" y="200.523927"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="261.560227" xlink:href="#m2fa7b82d79" y="195.384436"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="291.996591" xlink:href="#m2fa7b82d79" y="189.454255"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="322.432955" xlink:href="#m2fa7b82d79" y="182.733382"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="352.869318" xlink:href="#m2fa7b82d79" y="175.221818"/>

    </g>

   </g>

   <g id="line2d_15">

    <path clip-path="url(#p22b06f4576)" d="M 48.505682 214.756364 

L 78.942045 214.558691 

L 109.378409 213.174982 

L 139.814773 209.4192 

L 170.251136 202.105309 

L 200.6875 190.047273 

L 231.123864 172.059055 

L 261.560227 146.954618 

L 291.996591 113.547927 

L 322.432955 70.652945 

L 352.869318 17.083636 

" style="fill:none;stroke:#008000;stroke-dasharray:5.55,2.4;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 33.2875 224.64 

L 33.2875 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 368.0875 224.64 

L 368.0875 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 33.2875 224.64 

L 368.0875 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 33.2875 7.2 

L 368.0875 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p22b06f4576">

   <rect height="217.44" width="334.8" x="33.2875" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[136]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Colour Paramter</span>
<span class="n">diag</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">lw</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-.&#39;</span><span class="p">)</span> <span class="c1"># Transparenz 50%</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">2</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#8B008B&quot;</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;:&#39;</span><span class="p">)</span>        <span class="c1"># RGB Hex Code</span>
<span class="c1">#ax.plot(x, x+3, color=&quot;#FF8C00&quot;,ls=&#39;steps&#39;)        # RGB Hex Code </span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">4</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">)</span>        
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[136]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c303a224c0&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="248.518125pt" version="1.1" viewBox="0 0 362.5625 248.518125" width="362.5625pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 248.518125 

L 362.5625 248.518125 

L 362.5625 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 20.5625 224.64 

L 355.3625 224.64 

L 355.3625 7.2 

L 20.5625 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="mee2a39f536" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="35.780682" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(32.599432 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="96.653409" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(93.472159 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="157.526136" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(154.344886 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="218.398864" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(215.217614 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="279.271591" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(276.090341 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="340.144318" xlink:href="#mee2a39f536" y="224.64"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(336.963068 239.238437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="mbbe1c628fc" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="214.756364"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 1 -->

      <g transform="translate(7.2 218.555582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="190.047273"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 2 -->

      <g transform="translate(7.2 193.846491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="165.338182"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 3 -->

      <g transform="translate(7.2 169.137401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="140.629091"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 4 -->

      <g transform="translate(7.2 144.42831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="115.92"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 5 -->

      <g transform="translate(7.2 119.719219)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="91.210909"/>

      </g>

     </g>

     <g id="text_12">

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

      <g transform="translate(7.2 95.010128)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="66.501818"/>

      </g>

     </g>

     <g id="text_13">

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

      <g transform="translate(7.2 70.301037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-55"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="41.792727"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 8 -->

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

      </defs>

      <g transform="translate(7.2 45.591946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#mbbe1c628fc" y="17.083636"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 9 -->

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

      </defs>

      <g transform="translate(7.2 20.882855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-57"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_16">

    <path clip-path="url(#p97253e8019)" d="M 35.780682 214.756364 

L 66.217045 202.401818 

L 96.653409 190.047273 

L 127.089773 177.692727 

L 157.526136 165.338182 

L 187.9625 152.983636 

L 218.398864 140.629091 

L 248.835227 128.274545 

L 279.271591 115.92 

L 309.707955 103.565455 

L 340.144318 91.210909 

" style="fill:none;stroke:#0000ff;stroke-dasharray:64,16,10,16;stroke-dashoffset:0;stroke-opacity:0.5;stroke-width:10;"/>

   </g>

   <g id="line2d_17">

    <path clip-path="url(#p97253e8019)" d="M 35.780682 190.047273 

L 66.217045 177.692727 

L 96.653409 165.338182 

L 127.089773 152.983636 

L 157.526136 140.629091 

L 187.9625 128.274545 

L 218.398864 115.92 

L 248.835227 103.565455 

L 279.271591 91.210909 

L 309.707955 78.856364 

L 340.144318 66.501818 

" style="fill:none;stroke:#8b008b;stroke-dasharray:1.5,2.475;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="line2d_18">

    <path clip-path="url(#p97253e8019)" d="M 35.780682 140.629091 

L 66.217045 128.274545 

L 96.653409 115.92 

L 127.089773 103.565455 

L 157.526136 91.210909 

L 187.9625 78.856364 

L 218.398864 66.501818 

L 248.835227 54.147273 

L 279.271591 41.792727 

L 309.707955 29.438182 

L 340.144318 17.083636 

" style="fill:none;stroke:#008000;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 20.5625 224.64 

L 20.5625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 355.3625 224.64 

L 355.3625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 20.5625 224.64 

L 355.3625 224.64 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 20.5625 7.2 

L 355.3625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p97253e8019">

   <rect height="217.44" width="334.8" x="20.5625" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[137]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>

<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.25</span><span class="p">)</span> 
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">2</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.50</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">3</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">1.00</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">4</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">2.00</span><span class="p">)</span>

<span class="c1"># Mögliche Linienstile ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">5</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">6</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-.&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">7</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;:&#39;</span><span class="p">)</span>

<span class="c1"># Benutzerdefinierte Querstrich</span>
<span class="n">line</span><span class="p">,</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">8</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;black&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mf">1.50</span><span class="p">)</span>
<span class="n">line</span><span class="o">.</span><span class="n">set_dashes</span><span class="p">([</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">])</span> <span class="c1"># Format: Linienlänge, Abstandslänge, ...</span>

<span class="c1"># Mögliche Markierungen: marker = &#39;+&#39;, &#39;o&#39;, &#39;*&#39;, &#39;s&#39;, &#39;,&#39;, &#39;.&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, ...</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span> <span class="mi">9</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;+&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">10</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;--&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;o&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">11</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;s&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">12</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;--&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;1&#39;</span><span class="p">)</span>

<span class="c1"># Markierungsgröße und Farbe</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">13</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;purple&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;o&#39;</span><span class="p">,</span> <span class="n">markersize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">14</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;purple&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;o&#39;</span><span class="p">,</span> <span class="n">markersize</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">15</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;purple&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;o&#39;</span><span class="p">,</span> <span class="n">markersize</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span> <span class="n">markerfacecolor</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">+</span><span class="mi">16</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;purple&quot;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">ls</span><span class="o">=</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">&#39;s&#39;</span><span class="p">,</span> <span class="n">markersize</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span> <span class="n">markerfacecolor</span><span class="o">=</span><span class="s2">&quot;yellow&quot;</span><span class="p">,</span> <span class="n">markeredgewidth</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">markeredgecolor</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="357.238125pt" version="1.1" viewBox="0 0 713.265625 357.238125" width="713.265625pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 357.238125 

L 713.265625 357.238125 

L 713.265625 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 36.465625 333.36 

L 706.065625 333.36 

L 706.065625 7.2 

L 36.465625 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m480a95c5c6" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="66.901989" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(63.720739 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="188.647443" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(185.466193 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="310.392898" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(307.211648 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="432.138352" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(428.957102 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="553.883807" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(550.702557 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="675.629261" xlink:href="#m480a95c5c6" y="333.36"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(672.448011 347.958438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m87259d34d5" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="333.36"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0.0 -->

      <defs>

       <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

      </defs>

      <g transform="translate(13.5625 337.159219)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="296.296364"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 2.5 -->

      <g transform="translate(13.5625 300.095582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="259.232727"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 5.0 -->

      <g transform="translate(13.5625 263.031946)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="222.169091"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 7.5 -->

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

      <g transform="translate(13.5625 225.96831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-55"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="185.105455"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 10.0 -->

      <g transform="translate(7.2 188.904673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-46"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="148.041818"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 12.5 -->

      <g transform="translate(7.2 151.841037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-46"/>

       <use x="159.033203" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="110.978182"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 15.0 -->

      <g transform="translate(7.2 114.777401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

       <use x="127.246094" xlink:href="#DejaVuSans-46"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="73.914545"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 17.5 -->

      <g transform="translate(7.2 77.713764)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-55"/>

       <use x="127.246094" xlink:href="#DejaVuSans-46"/>

       <use x="159.033203" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.465625" xlink:href="#m87259d34d5" y="36.850909"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 20.0 -->

      <g transform="translate(7.2 40.650128)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-46"/>

       <use x="159.033203" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_16">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 318.534545 

L 127.774716 311.121818 

L 188.647443 303.709091 

L 249.52017 296.296364 

L 310.392898 288.883636 

L 371.265625 281.470909 

L 432.138352 274.058182 

L 493.01108 266.645455 

L 553.883807 259.232727 

L 614.756534 251.82 

L 675.629261 244.407273 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;stroke-width:0.25;"/>

   </g>

   <g id="line2d_17">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 303.709091 

L 127.774716 296.296364 

L 188.647443 288.883636 

L 249.52017 281.470909 

L 310.392898 274.058182 

L 371.265625 266.645455 

L 432.138352 259.232727 

L 493.01108 251.82 

L 553.883807 244.407273 

L 614.756534 236.994545 

L 675.629261 229.581818 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;stroke-width:0.5;"/>

   </g>

   <g id="line2d_18">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 288.883636 

L 127.774716 281.470909 

L 188.647443 274.058182 

L 249.52017 266.645455 

L 310.392898 259.232727 

L 371.265625 251.82 

L 432.138352 244.407273 

L 493.01108 236.994545 

L 553.883807 229.581818 

L 614.756534 222.169091 

L 675.629261 214.756364 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;"/>

   </g>

   <g id="line2d_19">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 274.058182 

L 127.774716 266.645455 

L 188.647443 259.232727 

L 249.52017 251.82 

L 310.392898 244.407273 

L 371.265625 236.994545 

L 432.138352 229.581818 

L 493.01108 222.169091 

L 553.883807 214.756364 

L 614.756534 207.343636 

L 675.629261 199.930909 

" style="fill:none;stroke:#ff0000;stroke-linecap:square;stroke-width:2;"/>

   </g>

   <g id="line2d_20">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 259.232727 

L 127.774716 251.82 

L 188.647443 244.407273 

L 249.52017 236.994545 

L 310.392898 229.581818 

L 371.265625 222.169091 

L 432.138352 214.756364 

L 493.01108 207.343636 

L 553.883807 199.930909 

L 614.756534 192.518182 

L 675.629261 185.105455 

" style="fill:none;stroke:#008000;stroke-linecap:square;stroke-width:3;"/>

   </g>

   <g id="line2d_21">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 244.407273 

L 127.774716 236.994545 

L 188.647443 229.581818 

L 249.52017 222.169091 

L 310.392898 214.756364 

L 371.265625 207.343636 

L 432.138352 199.930909 

L 493.01108 192.518182 

L 553.883807 185.105455 

L 614.756534 177.692727 

L 675.629261 170.28 

" style="fill:none;stroke:#008000;stroke-dasharray:19.2,4.8,3,4.8;stroke-dashoffset:0;stroke-width:3;"/>

   </g>

   <g id="line2d_22">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 229.581818 

L 127.774716 222.169091 

L 188.647443 214.756364 

L 249.52017 207.343636 

L 310.392898 199.930909 

L 371.265625 192.518182 

L 432.138352 185.105455 

L 493.01108 177.692727 

L 553.883807 170.28 

L 614.756534 162.867273 

L 675.629261 155.454545 

" style="fill:none;stroke:#008000;stroke-dasharray:3,4.95;stroke-dashoffset:0;stroke-width:3;"/>

   </g>

   <g id="line2d_23">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 214.756364 

L 127.774716 207.343636 

L 188.647443 199.930909 

L 249.52017 192.518182 

L 310.392898 185.105455 

L 371.265625 177.692727 

L 432.138352 170.28 

L 493.01108 162.867273 

L 553.883807 155.454545 

L 614.756534 148.041818 

L 675.629261 140.629091 

" style="fill:none;stroke:#000000;stroke-dasharray:7.5,15,22.5,15;stroke-dashoffset:0;stroke-width:1.5;"/>

   </g>

   <g id="line2d_24">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 199.930909 

L 127.774716 192.518182 

L 188.647443 185.105455 

L 249.52017 177.692727 

L 310.392898 170.28 

L 371.265625 162.867273 

L 432.138352 155.454545 

L 493.01108 148.041818 

L 553.883807 140.629091 

L 614.756534 133.216364 

L 675.629261 125.803636 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:3;"/>

    <defs>

     <path d="M -3 0 

L 3 0 

M 0 3 

L 0 -3 

" id="m720ba6e241" style="stroke:#0000ff;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#0000ff;stroke:#0000ff;" x="66.901989" xlink:href="#m720ba6e241" y="199.930909"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="127.774716" xlink:href="#m720ba6e241" y="192.518182"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="188.647443" xlink:href="#m720ba6e241" y="185.105455"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="249.52017" xlink:href="#m720ba6e241" y="177.692727"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="310.392898" xlink:href="#m720ba6e241" y="170.28"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="371.265625" xlink:href="#m720ba6e241" y="162.867273"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="432.138352" xlink:href="#m720ba6e241" y="155.454545"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="493.01108" xlink:href="#m720ba6e241" y="148.041818"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="553.883807" xlink:href="#m720ba6e241" y="140.629091"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="614.756534" xlink:href="#m720ba6e241" y="133.216364"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="675.629261" xlink:href="#m720ba6e241" y="125.803636"/>

    </g>

   </g>

   <g id="line2d_25">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 185.105455 

L 127.774716 177.692727 

L 188.647443 170.28 

L 249.52017 162.867273 

L 310.392898 155.454545 

L 371.265625 148.041818 

L 432.138352 140.629091 

L 493.01108 133.216364 

L 553.883807 125.803636 

L 614.756534 118.390909 

L 675.629261 110.978182 

" style="fill:none;stroke:#0000ff;stroke-dasharray:11.1,4.8;stroke-dashoffset:0;stroke-width:3;"/>

    <defs>

     <path d="M 0 3 

C 0.795609 3 1.55874 2.683901 2.12132 2.12132 

C 2.683901 1.55874 3 0.795609 3 0 

C 3 -0.795609 2.683901 -1.55874 2.12132 -2.12132 

C 1.55874 -2.683901 0.795609 -3 0 -3 

C -0.795609 -3 -1.55874 -2.683901 -2.12132 -2.12132 

C -2.683901 -1.55874 -3 -0.795609 -3 0 

C -3 0.795609 -2.683901 1.55874 -2.12132 2.12132 

C -1.55874 2.683901 -0.795609 3 0 3 

z

" id="md6a910000f" style="stroke:#0000ff;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#0000ff;stroke:#0000ff;" x="66.901989" xlink:href="#md6a910000f" y="185.105455"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="127.774716" xlink:href="#md6a910000f" y="177.692727"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="188.647443" xlink:href="#md6a910000f" y="170.28"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="249.52017" xlink:href="#md6a910000f" y="162.867273"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="310.392898" xlink:href="#md6a910000f" y="155.454545"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="371.265625" xlink:href="#md6a910000f" y="148.041818"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="432.138352" xlink:href="#md6a910000f" y="140.629091"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="493.01108" xlink:href="#md6a910000f" y="133.216364"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="553.883807" xlink:href="#md6a910000f" y="125.803636"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="614.756534" xlink:href="#md6a910000f" y="118.390909"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="675.629261" xlink:href="#md6a910000f" y="110.978182"/>

    </g>

   </g>

   <g id="line2d_26">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 170.28 

L 127.774716 162.867273 

L 188.647443 155.454545 

L 249.52017 148.041818 

L 310.392898 140.629091 

L 371.265625 133.216364 

L 432.138352 125.803636 

L 493.01108 118.390909 

L 553.883807 110.978182 

L 614.756534 103.565455 

L 675.629261 96.152727 

" style="fill:none;stroke:#0000ff;stroke-linecap:square;stroke-width:3;"/>

    <defs>

     <path d="M -3 3 

L 3 3 

L 3 -3 

L -3 -3 

z

" id="m962899cc49" style="stroke:#0000ff;stroke-linejoin:miter;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="66.901989" xlink:href="#m962899cc49" y="170.28"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="127.774716" xlink:href="#m962899cc49" y="162.867273"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="188.647443" xlink:href="#m962899cc49" y="155.454545"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="249.52017" xlink:href="#m962899cc49" y="148.041818"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="310.392898" xlink:href="#m962899cc49" y="140.629091"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="371.265625" xlink:href="#m962899cc49" y="133.216364"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="432.138352" xlink:href="#m962899cc49" y="125.803636"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="493.01108" xlink:href="#m962899cc49" y="118.390909"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="553.883807" xlink:href="#m962899cc49" y="110.978182"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="614.756534" xlink:href="#m962899cc49" y="103.565455"/>

     <use style="fill:#0000ff;stroke:#0000ff;stroke-linejoin:miter;" x="675.629261" xlink:href="#m962899cc49" y="96.152727"/>

    </g>

   </g>

   <g id="line2d_27">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 155.454545 

L 127.774716 148.041818 

L 188.647443 140.629091 

L 249.52017 133.216364 

L 310.392898 125.803636 

L 371.265625 118.390909 

L 432.138352 110.978182 

L 493.01108 103.565455 

L 553.883807 96.152727 

L 614.756534 88.74 

L 675.629261 81.327273 

" style="fill:none;stroke:#0000ff;stroke-dasharray:11.1,4.8;stroke-dashoffset:0;stroke-width:3;"/>

    <defs>

     <path d="M 0 0 

L 0 3 

M 0 0 

L 2.4 -1.5 

M 0 0 

L -2.4 -1.5 

" id="m648928b847" style="stroke:#0000ff;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#0000ff;stroke:#0000ff;" x="66.901989" xlink:href="#m648928b847" y="155.454545"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="127.774716" xlink:href="#m648928b847" y="148.041818"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="188.647443" xlink:href="#m648928b847" y="140.629091"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="249.52017" xlink:href="#m648928b847" y="133.216364"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="310.392898" xlink:href="#m648928b847" y="125.803636"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="371.265625" xlink:href="#m648928b847" y="118.390909"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="432.138352" xlink:href="#m648928b847" y="110.978182"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="493.01108" xlink:href="#m648928b847" y="103.565455"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="553.883807" xlink:href="#m648928b847" y="96.152727"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="614.756534" xlink:href="#m648928b847" y="88.74"/>

     <use style="fill:#0000ff;stroke:#0000ff;" x="675.629261" xlink:href="#m648928b847" y="81.327273"/>

    </g>

   </g>

   <g id="line2d_28">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 140.629091 

L 127.774716 133.216364 

L 188.647443 125.803636 

L 249.52017 118.390909 

L 310.392898 110.978182 

L 371.265625 103.565455 

L 432.138352 96.152727 

L 493.01108 88.74 

L 553.883807 81.327273 

L 614.756534 73.914545 

L 675.629261 66.501818 

" style="fill:none;stroke:#800080;stroke-linecap:square;"/>

    <defs>

     <path d="M 0 1 

C 0.265203 1 0.51958 0.894634 0.707107 0.707107 

C 0.894634 0.51958 1 0.265203 1 0 

C 1 -0.265203 0.894634 -0.51958 0.707107 -0.707107 

C 0.51958 -0.894634 0.265203 -1 0 -1 

C -0.265203 -1 -0.51958 -0.894634 -0.707107 -0.707107 

C -0.894634 -0.51958 -1 -0.265203 -1 0 

C -1 0.265203 -0.894634 0.51958 -0.707107 0.707107 

C -0.51958 0.894634 -0.265203 1 0 1 

z

" id="m68f45a2307" style="stroke:#800080;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#800080;stroke:#800080;" x="66.901989" xlink:href="#m68f45a2307" y="140.629091"/>

     <use style="fill:#800080;stroke:#800080;" x="127.774716" xlink:href="#m68f45a2307" y="133.216364"/>

     <use style="fill:#800080;stroke:#800080;" x="188.647443" xlink:href="#m68f45a2307" y="125.803636"/>

     <use style="fill:#800080;stroke:#800080;" x="249.52017" xlink:href="#m68f45a2307" y="118.390909"/>

     <use style="fill:#800080;stroke:#800080;" x="310.392898" xlink:href="#m68f45a2307" y="110.978182"/>

     <use style="fill:#800080;stroke:#800080;" x="371.265625" xlink:href="#m68f45a2307" y="103.565455"/>

     <use style="fill:#800080;stroke:#800080;" x="432.138352" xlink:href="#m68f45a2307" y="96.152727"/>

     <use style="fill:#800080;stroke:#800080;" x="493.01108" xlink:href="#m68f45a2307" y="88.74"/>

     <use style="fill:#800080;stroke:#800080;" x="553.883807" xlink:href="#m68f45a2307" y="81.327273"/>

     <use style="fill:#800080;stroke:#800080;" x="614.756534" xlink:href="#m68f45a2307" y="73.914545"/>

     <use style="fill:#800080;stroke:#800080;" x="675.629261" xlink:href="#m68f45a2307" y="66.501818"/>

    </g>

   </g>

   <g id="line2d_29">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 125.803636 

L 127.774716 118.390909 

L 188.647443 110.978182 

L 249.52017 103.565455 

L 310.392898 96.152727 

L 371.265625 88.74 

L 432.138352 81.327273 

L 493.01108 73.914545 

L 553.883807 66.501818 

L 614.756534 59.089091 

L 675.629261 51.676364 

" style="fill:none;stroke:#800080;stroke-linecap:square;"/>

    <defs>

     <path d="M 0 2 

C 0.530406 2 1.03916 1.789267 1.414214 1.414214 

C 1.789267 1.03916 2 0.530406 2 0 

C 2 -0.530406 1.789267 -1.03916 1.414214 -1.414214 

C 1.03916 -1.789267 0.530406 -2 0 -2 

C -0.530406 -2 -1.03916 -1.789267 -1.414214 -1.414214 

C -1.789267 -1.03916 -2 -0.530406 -2 0 

C -2 0.530406 -1.789267 1.03916 -1.414214 1.414214 

C -1.03916 1.789267 -0.530406 2 0 2 

z

" id="m997780159e" style="stroke:#800080;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#800080;stroke:#800080;" x="66.901989" xlink:href="#m997780159e" y="125.803636"/>

     <use style="fill:#800080;stroke:#800080;" x="127.774716" xlink:href="#m997780159e" y="118.390909"/>

     <use style="fill:#800080;stroke:#800080;" x="188.647443" xlink:href="#m997780159e" y="110.978182"/>

     <use style="fill:#800080;stroke:#800080;" x="249.52017" xlink:href="#m997780159e" y="103.565455"/>

     <use style="fill:#800080;stroke:#800080;" x="310.392898" xlink:href="#m997780159e" y="96.152727"/>

     <use style="fill:#800080;stroke:#800080;" x="371.265625" xlink:href="#m997780159e" y="88.74"/>

     <use style="fill:#800080;stroke:#800080;" x="432.138352" xlink:href="#m997780159e" y="81.327273"/>

     <use style="fill:#800080;stroke:#800080;" x="493.01108" xlink:href="#m997780159e" y="73.914545"/>

     <use style="fill:#800080;stroke:#800080;" x="553.883807" xlink:href="#m997780159e" y="66.501818"/>

     <use style="fill:#800080;stroke:#800080;" x="614.756534" xlink:href="#m997780159e" y="59.089091"/>

     <use style="fill:#800080;stroke:#800080;" x="675.629261" xlink:href="#m997780159e" y="51.676364"/>

    </g>

   </g>

   <g id="line2d_30">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 110.978182 

L 127.774716 103.565455 

L 188.647443 96.152727 

L 249.52017 88.74 

L 310.392898 81.327273 

L 371.265625 73.914545 

L 432.138352 66.501818 

L 493.01108 59.089091 

L 553.883807 51.676364 

L 614.756534 44.263636 

L 675.629261 36.850909 

" style="fill:none;stroke:#800080;stroke-linecap:square;"/>

    <defs>

     <path d="M 0 4 

C 1.060812 4 2.078319 3.578535 2.828427 2.828427 

C 3.578535 2.078319 4 1.060812 4 0 

C 4 -1.060812 3.578535 -2.078319 2.828427 -2.828427 

C 2.078319 -3.578535 1.060812 -4 0 -4 

C -1.060812 -4 -2.078319 -3.578535 -2.828427 -2.828427 

C -3.578535 -2.078319 -4 -1.060812 -4 0 

C -4 1.060812 -3.578535 2.078319 -2.828427 2.828427 

C -2.078319 3.578535 -1.060812 4 0 4 

z

" id="m0f5040b19f" style="stroke:#800080;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#ff0000;stroke:#800080;" x="66.901989" xlink:href="#m0f5040b19f" y="110.978182"/>

     <use style="fill:#ff0000;stroke:#800080;" x="127.774716" xlink:href="#m0f5040b19f" y="103.565455"/>

     <use style="fill:#ff0000;stroke:#800080;" x="188.647443" xlink:href="#m0f5040b19f" y="96.152727"/>

     <use style="fill:#ff0000;stroke:#800080;" x="249.52017" xlink:href="#m0f5040b19f" y="88.74"/>

     <use style="fill:#ff0000;stroke:#800080;" x="310.392898" xlink:href="#m0f5040b19f" y="81.327273"/>

     <use style="fill:#ff0000;stroke:#800080;" x="371.265625" xlink:href="#m0f5040b19f" y="73.914545"/>

     <use style="fill:#ff0000;stroke:#800080;" x="432.138352" xlink:href="#m0f5040b19f" y="66.501818"/>

     <use style="fill:#ff0000;stroke:#800080;" x="493.01108" xlink:href="#m0f5040b19f" y="59.089091"/>

     <use style="fill:#ff0000;stroke:#800080;" x="553.883807" xlink:href="#m0f5040b19f" y="51.676364"/>

     <use style="fill:#ff0000;stroke:#800080;" x="614.756534" xlink:href="#m0f5040b19f" y="44.263636"/>

     <use style="fill:#ff0000;stroke:#800080;" x="675.629261" xlink:href="#m0f5040b19f" y="36.850909"/>

    </g>

   </g>

   <g id="line2d_31">

    <path clip-path="url(#pfae5e7ec9a)" d="M 66.901989 96.152727 

L 127.774716 88.74 

L 188.647443 81.327273 

L 249.52017 73.914545 

L 310.392898 66.501818 

L 371.265625 59.089091 

L 432.138352 51.676364 

L 493.01108 44.263636 

L 553.883807 36.850909 

L 614.756534 29.438182 

L 675.629261 22.025455 

" style="fill:none;stroke:#800080;stroke-linecap:square;"/>

    <defs>

     <path d="M -4 4 

L 4 4 

L 4 -4 

L -4 -4 

z

" id="ma188cd53e6" style="stroke:#008000;stroke-linejoin:miter;stroke-width:3;"/>

    </defs>

    <g clip-path="url(#pfae5e7ec9a)">

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="66.901989" xlink:href="#ma188cd53e6" y="96.152727"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="127.774716" xlink:href="#ma188cd53e6" y="88.74"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="188.647443" xlink:href="#ma188cd53e6" y="81.327273"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="249.52017" xlink:href="#ma188cd53e6" y="73.914545"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="310.392898" xlink:href="#ma188cd53e6" y="66.501818"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="371.265625" xlink:href="#ma188cd53e6" y="59.089091"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="432.138352" xlink:href="#ma188cd53e6" y="51.676364"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="493.01108" xlink:href="#ma188cd53e6" y="44.263636"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="553.883807" xlink:href="#ma188cd53e6" y="36.850909"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="614.756534" xlink:href="#ma188cd53e6" y="29.438182"/>

     <use style="fill:#ffff00;stroke:#008000;stroke-linejoin:miter;stroke-width:3;" x="675.629261" xlink:href="#ma188cd53e6" y="22.025455"/>

    </g>

   </g>

   <g id="patch_3">

    <path d="M 36.465625 333.36 

L 36.465625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 706.065625 333.36 

L 706.065625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 36.465625 333.36 

L 706.065625 333.36 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 36.465625 7.2 

L 706.065625 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pfae5e7ec9a">

   <rect height="326.16" width="669.6" x="36.465625" y="7.2"/>

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
<h2 id="Diagramm-ausschneiden">Diagramm ausschneiden<a class="anchor-link" href="#Diagramm-ausschneiden">&#182;</a></h2><p>Sprich man möchte lediglich einen bestimmten Beriech aus dem Modell sehen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[138]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bsp1</span>
<span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[138]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30b788190&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="247.078125pt" version="1.1" viewBox="0 0 250.125 247.078125" width="250.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 247.078125 

L 250.125 247.078125 

L 250.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 223.2 

L 242.925 223.2 

L 242.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="me9600db883" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="36.743182" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(33.561932 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="76.015909" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(72.834659 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="115.288636" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(112.107386 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="154.561364" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(151.380114 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="193.834091" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(190.652841 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="233.106818" xlink:href="#me9600db883" y="223.2"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(229.925568 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m55a2041a4a" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="213.381818"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(13.5625 217.181037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="174.109091"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 5 -->

      <g transform="translate(13.5625 177.90831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="134.836364"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 10 -->

      <g transform="translate(7.2 138.635582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="95.563636"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 15 -->

      <g transform="translate(7.2 99.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="56.290909"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 20 -->

      <g transform="translate(7.2 60.090128)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m55a2041a4a" y="17.018182"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 25 -->

      <g transform="translate(7.2 20.817401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#pc6c9184daa)" d="M 36.743182 213.381818 

L 56.379545 211.418182 

L 76.015909 205.527273 

L 95.652273 195.709091 

L 115.288636 181.963636 

L 134.925 164.290909 

L 154.561364 142.690909 

L 174.197727 117.163636 

L 193.834091 87.709091 

L 213.470455 54.327273 

L 233.106818 17.018182 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 223.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 242.925 223.2 

L 242.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 223.2 

L 242.925 223.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 242.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pc6c9184daa">

   <rect height="216" width="216" x="26.925" y="7.2"/>

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
<h3 id="Y-Achse-abschneiden">Y-Achse abschneiden<a class="anchor-link" href="#Y-Achse-abschneiden">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[139]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[139]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30b7e6670&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="250.877344pt" version="1.1" viewBox="0 0 243.7625 250.877344" width="243.7625pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 250.877344 

L 243.7625 250.877344 

L 243.7625 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 20.5625 226.999219 

L 236.5625 226.999219 

L 236.5625 10.999219 

L 20.5625 10.999219 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m04ec898d68" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.380682" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.199432 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="69.653409" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(66.472159 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="108.926136" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_3">

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

      <g transform="translate(105.744886 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="148.198864" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_4">

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

      <g transform="translate(145.017614 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="187.471591" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_5">

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

      <g transform="translate(184.290341 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="226.744318" xlink:href="#m04ec898d68" y="226.999219"/>

      </g>

     </g>

     <g id="text_6">

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

      <g transform="translate(223.563068 241.597656)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_7">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="m94fce061f8" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="226.999219"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 0 -->

      <g transform="translate(7.2 230.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="183.799219"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 1 -->

      <g transform="translate(7.2 187.598437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="140.599219"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 2 -->

      <g transform="translate(7.2 144.398438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="97.399219"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 3 -->

      <g transform="translate(7.2 101.198437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="54.199219"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 4 -->

      <g transform="translate(7.2 57.998437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="20.5625" xlink:href="#m94fce061f8" y="10.999219"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 5 -->

      <g transform="translate(7.2 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_13">

    <path clip-path="url(#pb84c4ffbf6)" d="M 30.380682 226.999219 

L 50.017045 216.199219 

L 69.653409 183.799219 

L 89.289773 129.799219 

L 108.926136 54.199219 

L 120.077494 -1 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 20.5625 226.999219 

L 20.5625 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 236.5625 226.999219 

L 236.5625 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 20.5625 226.999219 

L 236.5625 226.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 20.5625 10.999219 

L 236.5625 10.999219 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pb84c4ffbf6">

   <rect height="216" width="216" x="20.5625" y="10.999219"/>

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
<h3 id="X-Achse-abschneiden">X-Achse abschneiden<a class="anchor-link" href="#X-Achse-abschneiden">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[140]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[140]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30b82dd00&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="247.078125pt" version="1.1" viewBox="0 0 258.076562 247.078125" width="258.076562pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 247.078125 

L 258.076562 247.078125 

L 258.076562 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 223.2 

L 242.925 223.2 

L 242.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m390a8501bb" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#m390a8501bb" y="223.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0.0 -->

      <defs>

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

      <g transform="translate(18.973438 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="80.925" xlink:href="#m390a8501bb" y="223.2"/>

      </g>

     </g>

     <g id="text_2">

      <!-- 0.5 -->

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

      <g transform="translate(72.973438 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="134.925" xlink:href="#m390a8501bb" y="223.2"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 1.0 -->

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

      <g transform="translate(126.973438 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="188.925" xlink:href="#m390a8501bb" y="223.2"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 1.5 -->

      <g transform="translate(180.973438 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="242.925" xlink:href="#m390a8501bb" y="223.2"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 2.0 -->

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

      <g transform="translate(234.973438 237.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_6">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="me7cc0ef79a" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="213.381818"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 0 -->

      <g transform="translate(13.5625 217.181037)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="174.109091"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 5 -->

      <g transform="translate(13.5625 177.90831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="134.836364"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 10 -->

      <g transform="translate(7.2 138.635582)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_9">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="95.563636"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 15 -->

      <g transform="translate(7.2 99.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="56.290909"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 20 -->

      <g transform="translate(7.2 60.090128)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#me7cc0ef79a" y="17.018182"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 25 -->

      <g transform="translate(7.2 20.817401)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_12">

    <path clip-path="url(#pf365d1612d)" d="M 26.925 213.381818 

L 80.925 211.418182 

L 134.925 205.527273 

L 188.925 195.709091 

L 242.925 181.963636 

L 259.076562 176.67767 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 223.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 242.925 223.2 

L 242.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 223.2 

L 242.925 223.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 242.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pf365d1612d">

   <rect height="216" width="216" x="26.925" y="7.2"/>

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
<h2 id="Diagramm-in-Datei-Speichern">Diagramm in Datei Speichern<a class="anchor-link" href="#Diagramm-in-Datei-Speichern">&#182;</a></h2><h4 id="Hardcoded">Hardcoded<a class="anchor-link" href="#Hardcoded">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[141]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># supported format: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.png&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.eps&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.pdf&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.ps&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.raw&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.rgba&quot;</span><span class="p">)</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlib.svg&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Mit-Funktion">Mit Funktion<a class="anchor-link" href="#Mit-Funktion">&#182;</a></h3><p>Hierbei kann geprüft und sichergestellt werden dass der Ordner der Ablage exisitert</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[142]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">PROJECT_ROOT_DIR</span> <span class="o">=</span> <span class="s2">&quot;.&quot;</span>
<span class="n">IMAGES_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_ROOT_DIR</span><span class="p">,</span> <span class="s2">&quot;imgs&quot;</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">save_fig</span><span class="p">(</span><span class="n">fig_id</span><span class="p">,</span> <span class="n">tight_layout</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">fig_extension</span><span class="o">=</span><span class="s2">&quot;png&quot;</span><span class="p">):</span>
    <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">IMAGES_PATH</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="c1"># Erstelle den Folder wenn er nicht existiert</span>
    <span class="n">path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">IMAGES_PATH</span><span class="p">,</span> <span class="n">fig_id</span> <span class="o">+</span> <span class="s2">&quot;-Function.&quot;</span> <span class="o">+</span> <span class="n">fig_extension</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Saving figure123&quot;</span><span class="p">,</span> <span class="n">fig_id</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">tight_layout</span><span class="p">:</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="n">fig_extension</span><span class="p">)</span>

<span class="n">save_fig</span><span class="p">(</span><span class="s2">&quot;diag&quot;</span><span class="p">)</span>
<span class="c1">#save_fig(&quot;diag&quot; fig_extension=&quot;eps&quot;)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Saving figure123 diag
.\imgs\diag-Function.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>&lt;Figure size 432x288 with 0 Axes&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[143]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Auflösung Besser</span>
<span class="n">diag</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./imgs/DiagrammFromCheatsheetMatplotlibSpecialResolution2.png&quot;</span><span class="p">,</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">400</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Style-Paletten">Style Paletten<a class="anchor-link" href="#Style-Paletten">&#182;</a></h2><p>hier geht es nich tum die Diagramm erstellung sondern lediglich der vergleich zwischen Anwendung einer Palette und Ohne. Das kann auch in den Pandas Built-In function inkludiert werden. Wir empfehlen die Nutzung der Stylesheets, da sie allen Diagrammen einen einheitlichen Look verleihen. Außerdem ist es möglich eigene Stylesheets zu erstellen, um z.B. eine Firma zu repräsentieren.
Style Paletten können auch selbst erstellt werden =&gt; Verwendung der Firmenfarben.</p>
<h3 id="Ohne-Palette">Ohne Palette<a class="anchor-link" href="#Ohne-Palette">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[144]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">100</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[144]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30b878670&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="103.078125pt" version="1.1" viewBox="0 0 106.125 103.078125" width="106.125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 103.078125 

L 106.125 103.078125 

L 106.125 0 

L 0 0 

z

" style="fill:none;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.925 79.2 

L 98.925 79.2 

L 98.925 7.2 

L 26.925 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="me2ab4a78a8" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="30.197727" xlink:href="#me2ab4a78a8" y="79.2"/>

      </g>

     </g>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.016477 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="95.652273" xlink:href="#me2ab4a78a8" y="79.2"/>

      </g>

     </g>

     <g id="text_2">

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

      <g transform="translate(92.471023 93.798438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_3">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="mff6dcb2e4a" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mff6dcb2e4a" y="75.927273"/>

      </g>

     </g>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(13.5625 79.726491)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mff6dcb2e4a" y="49.745455"/>

      </g>

     </g>

     <g id="text_4">

      <!-- 10 -->

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

      <g transform="translate(7.2 53.544673)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="26.925" xlink:href="#mff6dcb2e4a" y="23.563636"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 20 -->

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

      <g transform="translate(7.2 27.362855)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_6">

    <path clip-path="url(#pb6f258b81b)" d="M 30.197727 75.927273 

L 36.743182 75.272727 

L 43.288636 73.309091 

L 49.834091 70.036364 

L 56.379545 65.454545 

L 62.925 59.563636 

L 69.470455 52.363636 

L 76.015909 43.854545 

L 82.561364 34.036364 

L 89.106818 22.909091 

L 95.652273 10.472727 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 26.925 79.2 

L 26.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_4">

    <path d="M 98.925 79.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_5">

    <path d="M 26.925 79.2 

L 98.925 79.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_6">

    <path d="M 26.925 7.2 

L 98.925 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="pb6f258b81b">

   <rect height="72" width="72" x="26.925" y="7.2"/>

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
<h3 id="Mit-Palette">Mit Palette<a class="anchor-link" href="#Mit-Palette">&#182;</a></h3><p>erst die Palette wählen, dann das Diagramm erstellen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[145]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># GG-plot =&gt; hier andere styles: https://matplotlib.org/gallery.html#style_sheets</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;fivethirtyeight&#39;</span><span class="p">)</span> <span class="c1"># &lt;= dark_background, bmh,fivethirtyeight, ggplot</span>
<span class="n">diag</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure123</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="n">dpi</span><span class="o">=</span> <span class="mi">100</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">diag</span><span class="o">.</span><span class="n">add_axes</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[145]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30be46160&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="103.449375pt" version="1.1" viewBox="0 0 108.896023 103.449375" width="108.896023pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 103.449375 

L 108.896023 103.449375 

L 108.896023 0 

L 0 0 

z

" style="fill:#f0f0f0;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 28.515 79.2 

L 100.515 79.2 

L 100.515 7.2 

L 28.515 7.2 

z

" style="fill:#f0f0f0;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <path clip-path="url(#p0da3e40a8e)" d="M 31.787727 79.2 

L 31.787727 7.2 

" style="fill:none;stroke:#cbcbcb;"/>

     </g>

     <g id="line2d_2"/>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(27.333977 93.337813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_3">

      <path clip-path="url(#p0da3e40a8e)" d="M 97.242273 79.2 

L 97.242273 7.2 

" style="fill:none;stroke:#cbcbcb;"/>

     </g>

     <g id="line2d_4"/>

     <g id="text_2">

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

      <g transform="translate(92.788523 93.337813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_5">

      <path clip-path="url(#p0da3e40a8e)" d="M 28.515 75.927273 

L 100.515 75.927273 

" style="fill:none;stroke:#cbcbcb;"/>

     </g>

     <g id="line2d_6"/>

     <g id="text_3">

      <!-- 0 -->

      <g transform="translate(16.1075 81.246179)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_7">

      <path clip-path="url(#p0da3e40a8e)" d="M 28.515 23.563636 

L 100.515 23.563636 

" style="fill:none;stroke:#cbcbcb;"/>

     </g>

     <g id="line2d_8"/>

     <g id="text_4">

      <!-- 20 -->

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

      <g transform="translate(7.2 28.882543)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_9">

    <path clip-path="url(#p0da3e40a8e)" d="M 31.787727 75.927273 

L 38.333182 75.272727 

L 44.878636 73.309091 

L 51.424091 70.036364 

L 57.969545 65.454545 

L 64.515 59.563636 

L 71.060455 52.363636 

L 77.605909 43.854545 

L 84.151364 34.036364 

L 90.696818 22.909091 

L 97.242273 10.472727 

" style="fill:none;stroke:#008fd5;stroke-width:4;"/>

   </g>

   <g id="patch_3">

    <path d="M 28.515 79.2 

L 28.515 7.2 

" style="fill:none;stroke:#f0f0f0;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_4">

    <path d="M 100.515 79.2 

L 100.515 7.2 

" style="fill:none;stroke:#f0f0f0;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_5">

    <path d="M 28.515 79.2 

L 100.515 79.2 

" style="fill:none;stroke:#f0f0f0;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_6">

    <path d="M 28.515 7.2 

L 100.515 7.2 

" style="fill:none;stroke:#f0f0f0;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p0da3e40a8e">

   <rect height="72" width="72" x="28.515" y="7.2"/>

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
<h1 id="Balkendiagramm">Balkendiagramm<a class="anchor-link" href="#Balkendiagramm">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[146]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Quartal</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span>
<span class="n">Umsatz</span> <span class="o">=</span> <span class="p">[</span><span class="mi">12</span><span class="p">,</span><span class="mi">15</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">14</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;dark_background&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">Quartal</span><span class="p">,</span> <span class="n">Umsatz</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[146]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;BarContainer object of 4 artists&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="264.729375pt" version="1.1" viewBox="0 0 411.555 264.729375" width="411.555pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 264.729375 

L 411.555 264.729375 

L 411.555 0 

L 0 0 

z

"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 28.515 240.48 

L 404.355 240.48 

L 404.355 7.2 

L 28.515 7.2 

z

"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <path clip-path="url(#p9032e2169d)" d="M 81.564187 240.48 

L 81.564187 7.2 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_2"/>

     <g id="text_1">

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

      <g style="fill:#ffffff;" transform="translate(77.110437 254.617813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_3">

      <path clip-path="url(#p9032e2169d)" d="M 171.478062 240.48 

L 171.478062 7.2 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_4"/>

     <g id="text_2">

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

      <g style="fill:#ffffff;" transform="translate(167.024312 254.617813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_5">

      <path clip-path="url(#p9032e2169d)" d="M 261.391938 240.48 

L 261.391938 7.2 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_6"/>

     <g id="text_3">

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

      <g style="fill:#ffffff;" transform="translate(256.938188 254.617813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_7">

      <path clip-path="url(#p9032e2169d)" d="M 351.305813 240.48 

L 351.305813 7.2 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_8"/>

     <g id="text_4">

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

      <g style="fill:#ffffff;" transform="translate(346.852063 254.617813)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_9">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 240.48 

L 404.355 240.48 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_10"/>

     <g id="text_5">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g style="fill:#ffffff;" transform="translate(16.1075 245.798906)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_11">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 210.857143 

L 404.355 210.857143 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_12"/>

     <g id="text_6">

      <!-- 2 -->

      <g style="fill:#ffffff;" transform="translate(16.1075 216.176049)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_13">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 181.234286 

L 404.355 181.234286 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_14"/>

     <g id="text_7">

      <!-- 4 -->

      <g style="fill:#ffffff;" transform="translate(16.1075 186.553192)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_15">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 151.611429 

L 404.355 151.611429 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_16"/>

     <g id="text_8">

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

      <g style="fill:#ffffff;" transform="translate(16.1075 156.930335)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_17">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 121.988571 

L 404.355 121.988571 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_18"/>

     <g id="text_9">

      <!-- 8 -->

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

      </defs>

      <g style="fill:#ffffff;" transform="translate(16.1075 127.307478)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_19">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 92.365714 

L 404.355 92.365714 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_20"/>

     <g id="text_10">

      <!-- 10 -->

      <g style="fill:#ffffff;" transform="translate(7.2 97.684621)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_21">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 62.742857 

L 404.355 62.742857 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_22"/>

     <g id="text_11">

      <!-- 12 -->

      <g style="fill:#ffffff;" transform="translate(7.2 68.061763)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_23">

      <path clip-path="url(#p9032e2169d)" d="M 28.515 33.12 

L 404.355 33.12 

" style="fill:none;stroke:#ffffff;"/>

     </g>

     <g id="line2d_24"/>

     <g id="text_12">

      <!-- 14 -->

      <g style="fill:#ffffff;" transform="translate(7.2 38.438906)scale(0.14 -0.14)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_3">

    <path clip-path="url(#p9032e2169d)" d="M 45.598636 240.48 

L 117.529737 240.48 

L 117.529737 62.742857 

L 45.598636 62.742857 

z

" style="fill:#8dd3c7;"/>

   </g>

   <g id="patch_4">

    <path clip-path="url(#p9032e2169d)" d="M 135.512512 240.48 

L 207.443612 240.48 

L 207.443612 18.308571 

L 135.512512 18.308571 

z

" style="fill:#8dd3c7;"/>

   </g>

   <g id="patch_5">

    <path clip-path="url(#p9032e2169d)" d="M 225.426388 240.48 

L 297.357488 240.48 

L 297.357488 47.931429 

L 225.426388 47.931429 

z

" style="fill:#8dd3c7;"/>

   </g>

   <g id="patch_6">

    <path clip-path="url(#p9032e2169d)" d="M 315.340263 240.48 

L 387.271364 240.48 

L 387.271364 33.12 

L 315.340263 33.12 

z

" style="fill:#8dd3c7;"/>

   </g>

   <g id="patch_7">

    <path d="M 28.515 240.48 

L 28.515 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_8">

    <path d="M 404.355 240.48 

L 404.355 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_9">

    <path d="M 28.515 240.48 

L 404.355 240.48 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

   <g id="patch_10">

    <path d="M 28.515 7.2 

L 404.355 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;stroke-width:3;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p9032e2169d">

   <rect height="233.28" width="375.84" x="28.515" y="7.2"/>

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
<div class="prompt input_prompt">In&nbsp;[147]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Horizontales</span>
<span class="n">Quartal</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">]</span>
<span class="n">Umsatz</span> <span class="o">=</span> <span class="p">[</span><span class="mi">12</span><span class="p">,</span><span class="mi">15</span><span class="p">,</span><span class="mi">13</span><span class="p">,</span><span class="mi">14</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;ggplot&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">barh</span><span class="p">(</span><span class="n">Quartal</span><span class="p">,</span> <span class="n">Umsatz</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[147]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;BarContainer object of 4 artists&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="260.858125pt" version="1.1" viewBox="0 0 409.643125 260.858125" width="409.643125pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M -0 260.858125 

L 409.643125 260.858125 

L 409.643125 0 

L -0 0 

z

" style="fill:#ffffff;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 26.603125 240.48 

L 402.443125 240.48 

L 402.443125 7.2 

L 26.603125 7.2 

z

" style="fill:#e5e5e5;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1"/>

     <g id="text_1">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g style="fill:#555555;" transform="translate(23.421875 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2"/>

     <g id="text_2">

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

      <g style="fill:#555555;" transform="translate(71.147589 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3"/>

     <g id="text_3">

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

      <g style="fill:#555555;" transform="translate(118.873304 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4"/>

     <g id="text_4">

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

      <g style="fill:#555555;" transform="translate(166.599018 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5"/>

     <g id="text_5">

      <!-- 8 -->

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

      </defs>

      <g style="fill:#555555;" transform="translate(214.324732 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6"/>

     <g id="text_6">

      <!-- 10 -->

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

      <g style="fill:#555555;" transform="translate(258.869196 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="line2d_7"/>

     <g id="text_7">

      <!-- 12 -->

      <g style="fill:#555555;" transform="translate(306.594911 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_8"/>

     <g id="text_8">

      <!-- 14 -->

      <g style="fill:#555555;" transform="translate(354.320625 251.578438)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_9"/>

     <g id="text_9">

      <!-- 0.5 -->

      <defs>

       <path d="M 10.6875 12.40625 

L 21 12.40625 

L 21 0 

L 10.6875 0 

z

" id="DejaVuSans-46"/>

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

      <g style="fill:#555555;" transform="translate(7.2 239.256444)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_10"/>

     <g id="text_10">

      <!-- 1.0 -->

      <g style="fill:#555555;" transform="translate(7.2 211.352137)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_11"/>

     <g id="text_11">

      <!-- 1.5 -->

      <g style="fill:#555555;" transform="translate(7.2 183.447831)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_12"/>

     <g id="text_12">

      <!-- 2.0 -->

      <g style="fill:#555555;" transform="translate(7.2 155.543525)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_13"/>

     <g id="text_13">

      <!-- 2.5 -->

      <g style="fill:#555555;" transform="translate(7.2 127.639219)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_14"/>

     <g id="text_14">

      <!-- 3.0 -->

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

      <g style="fill:#555555;" transform="translate(7.2 99.734913)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_15"/>

     <g id="text_15">

      <!-- 3.5 -->

      <g style="fill:#555555;" transform="translate(7.2 71.830606)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_16"/>

     <g id="text_16">

      <!-- 4.0 -->

      <g style="fill:#555555;" transform="translate(7.2 43.9263)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_9">

     <g id="line2d_17"/>

     <g id="text_17">

      <!-- 4.5 -->

      <g style="fill:#555555;" transform="translate(7.2 16.021994)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-46"/>

       <use x="95.410156" xlink:href="#DejaVuSans-53"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_3">

    <path clip-path="url(#p35f4911c68)" d="M 26.603125 229.876364 

L 312.957411 229.876364 

L 312.957411 185.229474 

L 26.603125 185.229474 

z

" style="fill:#e24a33;"/>

   </g>

   <g id="patch_4">

    <path clip-path="url(#p35f4911c68)" d="M 26.603125 174.067751 

L 384.545982 174.067751 

L 384.545982 129.420861 

L 26.603125 129.420861 

z

" style="fill:#e24a33;"/>

   </g>

   <g id="patch_5">

    <path clip-path="url(#p35f4911c68)" d="M 26.603125 118.259139 

L 336.820268 118.259139 

L 336.820268 73.612249 

L 26.603125 73.612249 

z

" style="fill:#e24a33;"/>

   </g>

   <g id="patch_6">

    <path clip-path="url(#p35f4911c68)" d="M 26.603125 62.450526 

L 360.683125 62.450526 

L 360.683125 17.803636 

L 26.603125 17.803636 

z

" style="fill:#e24a33;"/>

   </g>

   <g id="patch_7">

    <path d="M 26.603125 240.48 

L 26.603125 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;"/>

   </g>

   <g id="patch_8">

    <path d="M 402.443125 240.48 

L 402.443125 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;"/>

   </g>

   <g id="patch_9">

    <path d="M 26.603125 240.48 

L 402.443125 240.48 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;"/>

   </g>

   <g id="patch_10">

    <path d="M 26.603125 7.2 

L 402.443125 7.2 

" style="fill:none;stroke:#ffffff;stroke-linecap:square;stroke-linejoin:miter;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p35f4911c68">

   <rect height="233.28" width="375.84" x="26.603125" y="7.2"/>

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
<h1 id="pi-Charts--Tortendiagramme">pi-Charts- Tortendiagramme<a class="anchor-link" href="#pi-Charts--Tortendiagramme">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[148]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;default&#39;</span><span class="p">)</span>
<span class="n">Stimmen</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span><span class="mi">12</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">7</span><span class="p">]</span>
<span class="n">Personen</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;jhc&quot;</span><span class="p">,</span> <span class="s2">&quot;sr&quot;</span><span class="p">,</span> <span class="s2">&quot;df&quot;</span><span class="p">,</span> <span class="s2">&quot;ne&quot;</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">pie</span><span class="p">(</span><span class="n">Stimmen</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="n">Personen</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Klassenesprecherwahl&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[148]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Klassenesprecherwahl&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="295.630125pt" version="1.1" viewBox="0 0 280.512 295.630125" width="280.512pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 295.630125 

L 280.512 295.630125 

L 280.512 0 

L 0 0 

z

" style="fill:#ffffff;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 246.7008 155.374125 

C 246.7008 137.870178 242.383236 120.633497 234.131933 105.196394 

C 225.880629 89.759291 213.947562 76.59318 199.393562 66.868508 

C 184.839562 57.143837 168.109075 51.157573 150.689415 49.441886 

C 133.269754 47.726199 115.692877 50.333482 99.521339 57.031953 

L 140.256 155.374125 

L 246.7008 155.374125 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_3">

    <path d="M 99.521339 57.031953 

C 80.073422 65.087544 63.445288 78.733901 51.750383 96.236563 

C 40.055478 113.739225 33.8112 134.323852 33.8112 155.374125 

C 33.8112 176.424398 40.055478 197.009025 51.750383 214.511687 

C 63.445288 232.014349 80.073422 245.660706 99.521339 253.716297 

L 140.256 155.374125 

L 99.521339 57.031953 

z

" style="fill:#ff7f0e;"/>

   </g>

   <g id="patch_4">

    <path d="M 99.521339 253.716297 

C 109.193473 257.722626 119.403953 260.280219 129.822585 261.306364 

C 140.241217 262.33251 150.754467 261.816027 161.02235 259.773618 

L 140.256 155.374125 

L 99.521339 253.716297 

z

" style="fill:#2ca02c;"/>

   </g>

   <g id="patch_5">

    <path d="M 161.02235 259.773618 

C 185.170334 254.970285 206.919501 241.934336 222.538943 222.901991 

C 238.158385 203.869646 246.7008 179.995196 246.7008 155.374125 

L 140.256 155.374125 

L 161.02235 259.773618 

z

" style="fill:#d62728;"/>

   </g>

   <g id="matplotlib.axis_1"/>

   <g id="matplotlib.axis_2"/>

   <g id="text_1">

    <!-- jhc -->

    <defs>

     <path d="M 9.421875 54.6875 

L 18.40625 54.6875 

L 18.40625 -0.984375 

Q 18.40625 -11.421875 14.421875 -16.109375 

Q 10.453125 -20.796875 1.609375 -20.796875 

L -1.8125 -20.796875 

L -1.8125 -13.1875 

L 0.59375 -13.1875 

Q 5.71875 -13.1875 7.5625 -10.8125 

Q 9.421875 -8.453125 9.421875 -0.984375 

z

M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 64.59375 

L 9.421875 64.59375 

z

" id="DejaVuSans-106"/>

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

    </defs>

    <g transform="translate(205.307319 60.777322)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-106"/>

     <use x="27.783203" xlink:href="#DejaVuSans-104"/>

     <use x="91.162109" xlink:href="#DejaVuSans-99"/>

    </g>

   </g>

   <g id="text_2">

    <!-- sr -->

    <defs>

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

    </defs>

    <g transform="translate(13.846407 158.1335)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-115"/>

     <use x="52.099609" xlink:href="#DejaVuSans-114"/>

    </g>

   </g>

   <g id="text_3">

    <!-- df -->

    <defs>

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

     <path d="M 37.109375 75.984375 

L 37.109375 68.5 

L 28.515625 68.5 

Q 23.6875 68.5 21.796875 66.546875 

Q 19.921875 64.59375 19.921875 59.515625 

L 19.921875 54.6875 

L 34.71875 54.6875 

L 34.71875 47.703125 

L 19.921875 47.703125 

L 19.921875 0 

L 10.890625 0 

L 10.890625 47.703125 

L 2.296875 47.703125 

L 2.296875 54.6875 

L 10.890625 54.6875 

L 10.890625 58.5 

Q 10.890625 67.625 15.140625 71.796875 

Q 19.390625 75.984375 28.609375 75.984375 

z

" id="DejaVuSans-102"/>

    </defs>

    <g transform="translate(118.910494 274.658963)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-100"/>

     <use x="63.476562" xlink:href="#DejaVuSans-102"/>

    </g>

   </g>

   <g id="text_4">

    <!-- ne -->

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

L 9.078125 54.6875 

L 18.109375 54.6875 

L 18.109375 46.1875 

Q 21.34375 51.125 25.703125 53.5625 

Q 30.078125 56 35.796875 56 

Q 45.21875 56 50.046875 50.171875 

Q 54.890625 44.34375 54.890625 33.015625 

z

" id="DejaVuSans-110"/>

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

    </defs>

    <g transform="translate(230.767237 232.414153)scale(0.1 -0.1)">

     <use xlink:href="#DejaVuSans-110"/>

     <use x="63.378906" xlink:href="#DejaVuSans-101"/>

    </g>

   </g>

   <g id="text_5">

    <!-- Klassenesprecherwahl -->

    <defs>

     <path d="M 9.8125 72.90625 

L 19.671875 72.90625 

L 19.671875 42.09375 

L 52.390625 72.90625 

L 65.09375 72.90625 

L 28.90625 38.921875 

L 67.671875 0 

L 54.6875 0 

L 19.671875 35.109375 

L 19.671875 0 

L 9.8125 0 

z

" id="DejaVuSans-75"/>

     <path d="M 9.421875 75.984375 

L 18.40625 75.984375 

L 18.40625 0 

L 9.421875 0 

z

" id="DejaVuSans-108"/>

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

     <path d="M 4.203125 54.6875 

L 13.1875 54.6875 

L 24.421875 12.015625 

L 35.59375 54.6875 

L 46.1875 54.6875 

L 57.421875 12.015625 

L 68.609375 54.6875 

L 77.59375 54.6875 

L 63.28125 0 

L 52.6875 0 

L 40.921875 44.828125 

L 29.109375 0 

L 18.5 0 

z

" id="DejaVuSans-119"/>

    </defs>

    <g transform="translate(73.268812 16.318125)scale(0.12 -0.12)">

     <use xlink:href="#DejaVuSans-75"/>

     <use x="65.576172" xlink:href="#DejaVuSans-108"/>

     <use x="93.359375" xlink:href="#DejaVuSans-97"/>

     <use x="154.638672" xlink:href="#DejaVuSans-115"/>

     <use x="206.738281" xlink:href="#DejaVuSans-115"/>

     <use x="258.837891" xlink:href="#DejaVuSans-101"/>

     <use x="320.361328" xlink:href="#DejaVuSans-110"/>

     <use x="383.740234" xlink:href="#DejaVuSans-101"/>

     <use x="445.263672" xlink:href="#DejaVuSans-115"/>

     <use x="497.363281" xlink:href="#DejaVuSans-112"/>

     <use x="560.839844" xlink:href="#DejaVuSans-114"/>

     <use x="599.703125" xlink:href="#DejaVuSans-101"/>

     <use x="661.226562" xlink:href="#DejaVuSans-99"/>

     <use x="716.207031" xlink:href="#DejaVuSans-104"/>

     <use x="779.585938" xlink:href="#DejaVuSans-101"/>

     <use x="841.109375" xlink:href="#DejaVuSans-114"/>

     <use x="882.222656" xlink:href="#DejaVuSans-119"/>

     <use x="964.009766" xlink:href="#DejaVuSans-97"/>

     <use x="1025.289062" xlink:href="#DejaVuSans-104"/>

     <use x="1088.667969" xlink:href="#DejaVuSans-108"/>

    </g>

   </g>

  </g>

 </g>

</svg>


</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Polardiagramme--Archimedische-Spirale">Polardiagramme -Archimedische Spirale<a class="anchor-link" href="#Polardiagramme--Archimedische-Spirale">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[149]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">theta</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">361</span><span class="p">)</span>
<span class="n">theta2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">radians</span><span class="p">(</span><span class="n">theta</span><span class="p">)</span>
<span class="n">r</span> <span class="o">=</span> <span class="mi">2</span><span class="o">*</span><span class="n">theta2</span>
<span class="n">plt</span><span class="o">.</span><span class="n">polar</span><span class="p">(</span><span class="n">theta2</span><span class="p">,</span><span class="n">r</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[149]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.lines.Line2D at 0x1c30bf92250&gt;]</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="318.190125pt" version="1.1" viewBox="0 0 326.237 318.190125" width="326.237pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 318.190125 

L 326.237 318.190125 

L 326.237 0 

L 0 0 

z

" style="fill:#ffffff;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 299.35575 159.095062 

C 299.35575 141.622309 295.913998 124.319455 289.227465 108.176736 

C 282.540932 92.034016 272.739653 77.365365 260.38455 65.010263 

C 248.029447 52.65516 233.360796 42.853881 217.218077 36.167347 

C 201.075357 29.480814 183.772504 26.039062 166.29975 26.039062 

C 148.826996 26.039062 131.524143 29.480814 115.381423 36.167347 

C 99.238704 42.853881 84.570053 52.65516 72.21495 65.010263 

C 59.859847 77.365365 50.058568 92.034016 43.372035 108.176736 

C 36.685502 124.319455 33.24375 141.622309 33.24375 159.095062 

C 33.24375 176.567816 36.685502 193.87067 43.372035 210.013389 

C 50.058568 226.156109 59.859847 240.82476 72.21495 253.179862 

C 84.570053 265.534965 99.238704 275.336244 115.381423 282.022778 

C 131.524143 288.709311 148.826996 292.151062 166.29975 292.151062 

C 183.772504 292.151062 201.075357 288.709311 217.218077 282.022778 

C 233.360796 275.336244 248.029447 265.534965 260.38455 253.179862 

C 272.739653 240.82476 282.540932 226.156109 289.227465 210.013389 

C 295.913998 193.87067 299.35575 176.567816 299.35575 159.095062 

M 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

M 299.35575 159.095062 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 299.35575 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_1">

      <!-- 0° -->

      <defs>

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

       <path d="M 25 67.921875 

Q 21.09375 67.921875 18.40625 65.203125 

Q 15.71875 62.5 15.71875 58.59375 

Q 15.71875 54.734375 18.40625 52.078125 

Q 21.09375 49.421875 25 49.421875 

Q 28.90625 49.421875 31.59375 52.078125 

Q 34.28125 54.734375 34.28125 58.59375 

Q 34.28125 62.453125 31.5625 65.1875 

Q 28.859375 67.921875 25 67.921875 

z

M 25 74.21875 

Q 28.125 74.21875 31 73.015625 

Q 33.890625 71.828125 35.984375 69.578125 

Q 38.234375 67.390625 39.359375 64.59375 

Q 40.484375 61.8125 40.484375 58.59375 

Q 40.484375 52.15625 35.96875 47.6875 

Q 31.453125 43.21875 24.90625 43.21875 

Q 18.3125 43.21875 13.90625 47.609375 

Q 9.515625 52 9.515625 58.59375 

Q 9.515625 65.140625 14 69.671875 

Q 18.5 74.21875 25 74.21875 

z

" id="DejaVuSans-176"/>

      </defs>

      <g transform="translate(307.6745 161.854437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

       <use x="63.623047" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 260.38455 65.010263 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_2">

      <!-- 45° -->

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

      <g transform="translate(261.421545 57.870143)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-53"/>

       <use x="127.246094" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 166.29975 26.039062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_3">

      <!-- 90° -->

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

      </defs>

      <g transform="translate(157.43725 14.798437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-57"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 72.21495 65.010263 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_4">

      <!-- 135° -->

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

      <g transform="translate(50.271705 57.870143)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-51"/>

       <use x="127.246094" xlink:href="#DejaVuSans-53"/>

       <use x="190.869141" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 33.24375 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_5">

      <!-- 180° -->

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

      </defs>

      <g transform="translate(7.2 161.854437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-56"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 72.21495 253.179862 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_6">

      <!-- 225° -->

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

      <g transform="translate(50.271705 265.838732)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-53"/>

       <use x="190.869141" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="line2d_7">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 166.29975 292.151062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_7">

      <!-- 270° -->

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

      <g transform="translate(154.256 308.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-55"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_8">

      <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 260.38455 253.179862 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_8">

      <!-- 315° -->

      <g transform="translate(258.240295 265.838732)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

       <use x="63.623047" xlink:href="#DejaVuSans-49"/>

       <use x="127.246094" xlink:href="#DejaVuSans-53"/>

       <use x="190.869141" xlink:href="#DejaVuSans-176"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_9">

      <path clip-path="url(#p2e984e04b5)" d="M 186.467864 159.095062 

L 186.357381 156.98692 

L 186.027143 154.901876 

L 185.480767 152.862772 

L 184.724239 150.891951 

L 183.765849 149.011005 

L 182.616097 147.240542 

L 181.28758 145.59996 

L 179.794853 144.107233 

L 178.15427 142.778715 

L 176.383807 141.628963 

L 174.502861 140.670573 

L 172.53204 139.914046 

L 170.492937 139.36767 

L 168.407892 139.037431 

L 166.29975 138.926948 

L 164.191608 139.037431 

L 162.106563 139.36767 

L 160.06746 139.914046 

L 158.096639 140.670573 

L 156.215693 141.628963 

L 154.44523 142.778715 

L 152.804647 144.107233 

L 151.31192 145.59996 

L 149.983403 147.240542 

L 148.833651 149.011005 

L 147.875261 150.891951 

L 147.118733 152.862772 

L 146.572357 154.901876 

L 146.242119 156.98692 

L 146.131636 159.095062 

L 146.242119 161.203205 

L 146.572357 163.288249 

L 147.118733 165.327353 

L 147.875261 167.298174 

L 148.833651 169.17912 

L 149.983403 170.949583 

L 151.31192 172.590165 

L 152.804647 174.082892 

L 154.44523 175.41141 

L 156.215693 176.561162 

L 158.096639 177.519552 

L 160.06746 178.276079 

L 162.106563 178.822455 

L 164.191608 179.152694 

L 166.29975 179.263177 

L 168.407892 179.152694 

L 170.492937 178.822455 

L 172.53204 178.276079 

L 174.502861 177.519552 

L 176.383807 176.561162 

L 178.15427 175.41141 

L 179.794853 174.082892 

L 181.28758 172.590165 

L 182.616097 170.949583 

L 183.765849 169.17912 

L 184.724239 167.298174 

L 185.480767 165.327353 

L 186.027143 163.288249 

L 186.357381 161.203205 

L 186.467864 159.095062 

L 186.467864 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_9">

      <!-- 2 -->

      <g transform="translate(184.932658 149.297372)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_10">

      <path clip-path="url(#p2e984e04b5)" d="M 206.635979 159.095062 

L 206.537722 156.281349 

L 206.243429 153.481344 

L 205.754535 150.708689 

L 205.073422 147.976891 

L 204.203407 145.29926 

L 203.148729 142.68884 

L 201.914526 140.15835 

L 200.506812 137.720118 

L 198.932445 135.386022 

L 197.199094 133.167434 

L 195.315205 131.075164 

L 193.289955 129.119403 

L 191.133212 127.30968 

L 188.855483 125.654813 

L 186.467864 124.162864 

L 183.981989 122.8411 

L 181.409967 121.695962 

L 178.76433 120.733029 

L 176.057967 119.956992 

L 173.304063 119.371632 

L 170.516034 118.9798 

L 167.707464 118.783405 

L 164.892036 118.783405 

L 162.083466 118.9798 

L 159.295437 119.371632 

L 156.541533 119.956992 

L 153.83517 120.733029 

L 151.189533 121.695962 

L 148.617511 122.8411 

L 146.131636 124.162864 

L 143.744017 125.654813 

L 141.466288 127.30968 

L 139.309545 129.119403 

L 137.284295 131.075164 

L 135.400406 133.167434 

L 133.667055 135.386022 

L 132.092688 137.720118 

L 130.684974 140.15835 

L 129.450771 142.68884 

L 128.396093 145.29926 

L 127.526078 147.976891 

L 126.844965 150.708689 

L 126.356071 153.481344 

L 126.061778 156.281349 

L 125.963521 159.095062 

L 126.061778 161.908776 

L 126.356071 164.708781 

L 126.844965 167.481436 

L 127.526078 170.213234 

L 128.396093 172.890865 

L 129.450771 175.501285 

L 130.684974 178.031775 

L 132.092688 180.470007 

L 133.667055 182.804103 

L 135.400406 185.022691 

L 137.284295 187.114961 

L 139.309545 189.070722 

L 141.466288 190.880445 

L 143.744017 192.535312 

L 146.131636 194.027261 

L 148.617511 195.349025 

L 151.189533 196.494163 

L 153.83517 197.457096 

L 156.541533 198.233133 

L 159.295437 198.818493 

L 162.083466 199.210325 

L 164.892036 199.40672 

L 167.707464 199.40672 

L 170.516034 199.210325 

L 173.304063 198.818493 

L 176.057967 198.233133 

L 178.76433 197.457096 

L 181.409967 196.494163 

L 183.981989 195.349025 

L 186.467864 194.027261 

L 188.855483 192.535312 

L 191.133212 190.880445 

L 193.289955 189.070722 

L 195.315205 187.114961 

L 197.199094 185.022691 

L 198.932445 182.804103 

L 200.506812 180.470007 

L 201.914526 178.031775 

L 203.148729 175.501285 

L 204.203407 172.890865 

L 205.073422 170.213234 

L 205.754535 167.481436 

L 206.243429 164.708781 

L 206.537722 161.908776 

L 206.635979 159.095062 

L 206.635979 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_10">

      <!-- 4 -->

      <g transform="translate(203.565566 141.579369)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_11">

      <path clip-path="url(#p2e984e04b5)" d="M 226.804093 159.095062 

L 226.656708 154.874493 

L 226.215269 150.674485 

L 225.481928 146.515502 

L 224.460258 142.417805 

L 223.155235 138.401358 

L 221.573218 134.485729 

L 219.721914 130.689994 

L 217.610343 127.032645 

L 215.248792 123.531502 

L 212.648766 120.20362 

L 209.822932 117.065214 

L 206.785058 114.131573 

L 203.549943 111.416989 

L 200.133349 108.934689 

L 196.551922 106.696764 

L 192.823108 104.714119 

L 188.965076 102.996412 

L 184.99662 101.552013 

L 180.937075 100.387957 

L 176.806219 99.509916 

L 172.624176 98.922168 

L 168.411321 98.627577 

L 164.188179 98.627577 

L 159.975324 98.922168 

L 155.793281 99.509916 

L 151.662425 100.387957 

L 147.60288 101.552013 

L 143.634424 102.996412 

L 139.776392 104.714119 

L 136.047578 106.696764 

L 132.466151 108.934689 

L 129.049557 111.416989 

L 125.814442 114.131573 

L 122.776568 117.065214 

L 119.950734 120.20362 

L 117.350708 123.531502 

L 114.989157 127.032645 

L 112.877586 130.689994 

L 111.026282 134.485729 

L 109.444265 138.401358 

L 108.139242 142.417805 

L 107.117572 146.515502 

L 106.384231 150.674485 

L 105.942792 154.874493 

L 105.795407 159.095062 

L 105.942792 163.315632 

L 106.384231 167.51564 

L 107.117572 171.674623 

L 108.139242 175.77232 

L 109.444265 179.788767 

L 111.026282 183.704396 

L 112.877586 187.500131 

L 114.989157 191.15748 

L 117.350708 194.658623 

L 119.950734 197.986505 

L 122.776568 201.124911 

L 125.814442 204.058552 

L 129.049557 206.773136 

L 132.466151 209.255436 

L 136.047578 211.493361 

L 139.776392 213.476006 

L 143.634424 215.193713 

L 147.60288 216.638112 

L 151.662425 217.802168 

L 155.793281 218.680209 

L 159.975324 219.267957 

L 164.188179 219.562548 

L 168.411321 219.562548 

L 172.624176 219.267957 

L 176.806219 218.680209 

L 180.937075 217.802168 

L 184.99662 216.638112 

L 188.965076 215.193713 

L 192.823108 213.476006 

L 196.551922 211.493361 

L 200.133349 209.255436 

L 203.549943 206.773136 

L 206.785058 204.058552 

L 209.822932 201.124911 

L 212.648766 197.986505 

L 215.248792 194.658623 

L 217.610343 191.15748 

L 219.721914 187.500131 

L 221.573218 183.704396 

L 223.155235 179.788767 

L 224.460258 175.77232 

L 225.481928 171.674623 

L 226.215269 167.51564 

L 226.656708 163.315632 

L 226.804093 159.095062 

L 226.804093 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_11">

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

      <g transform="translate(222.198474 133.861365)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_12">

      <path clip-path="url(#p2e984e04b5)" d="M 246.972208 159.095062 

L 246.775694 153.467636 

L 246.187109 147.867626 

L 245.209321 142.322315 

L 243.847093 136.85872 

L 242.107063 131.503457 

L 239.997707 126.282618 

L 237.529302 121.221638 

L 234.713874 116.345173 

L 231.565139 111.676982 

L 228.098438 107.239806 

L 224.33066 103.055265 

L 220.28016 99.143743 

L 215.966674 95.524298 

L 211.411216 92.214564 

L 206.635979 89.230665 

L 201.664228 86.587138 

L 196.520185 84.296862 

L 191.22891 82.370996 

L 185.816184 80.818922 

L 180.308375 79.648201 

L 174.732318 78.864537 

L 169.115178 78.471748 

L 163.484322 78.471748 

L 157.867182 78.864537 

L 152.291125 79.648201 

L 146.783316 80.818922 

L 141.37059 82.370996 

L 136.079315 84.296862 

L 130.935272 86.587138 

L 125.963521 89.230665 

L 121.188284 92.214564 

L 116.632826 95.524298 

L 112.31934 99.143743 

L 108.26884 103.055265 

L 104.501062 107.239806 

L 101.034361 111.676982 

L 97.885626 116.345173 

L 95.070198 121.221638 

L 92.601793 126.282618 

L 90.492437 131.503457 

L 88.752407 136.85872 

L 87.390179 142.322315 

L 86.412391 147.867626 

L 85.823806 153.467636 

L 85.627292 159.095062 

L 85.823806 164.722489 

L 86.412391 170.322499 

L 87.390179 175.86781 

L 88.752407 181.331405 

L 90.492437 186.686668 

L 92.601793 191.907507 

L 95.070198 196.968487 

L 97.885626 201.844952 

L 101.034361 206.513143 

L 104.501062 210.950319 

L 108.26884 215.13486 

L 112.31934 219.046382 

L 116.632826 222.665827 

L 121.188284 225.975561 

L 125.963521 228.95946 

L 130.935272 231.602987 

L 136.079315 233.893263 

L 141.37059 235.819129 

L 146.783316 237.371203 

L 152.291125 238.541924 

L 157.867182 239.325588 

L 163.484322 239.718377 

L 169.115178 239.718377 

L 174.732318 239.325588 

L 180.308375 238.541924 

L 185.816184 237.371203 

L 191.22891 235.819129 

L 196.520185 233.893263 

L 201.664228 231.602987 

L 206.635979 228.95946 

L 211.411216 225.975561 

L 215.966674 222.665827 

L 220.28016 219.046382 

L 224.33066 215.13486 

L 228.098438 210.950319 

L 231.565139 206.513143 

L 234.713874 201.844952 

L 237.529302 196.968487 

L 239.997707 191.907507 

L 242.107063 186.686668 

L 243.847093 181.331405 

L 245.209321 175.86781 

L 246.187109 170.322499 

L 246.775694 164.722489 

L 246.972208 159.095062 

L 246.972208 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_12">

      <!-- 8 -->

      <g transform="translate(240.831382 126.143362)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_13">

      <path clip-path="url(#p2e984e04b5)" d="M 267.140322 159.095062 

L 267.078893 155.575777 

L 266.894679 152.06078 

L 266.587907 148.554352 

L 266.158948 145.060767 

L 265.608327 141.584281 

L 264.936714 138.129129 

L 264.144926 134.69952 

L 263.233929 131.299634 

L 262.204833 127.933612 

L 261.058891 124.605556 

L 259.7975 121.319519 

L 258.422196 118.079507 

L 256.934656 114.889465 

L 255.33669 111.753282 

L 253.630247 108.674777 

L 251.817405 105.657701 

L 249.900373 102.70573 

L 247.881486 99.822461 

L 245.763205 97.011407 

L 243.54811 94.275992 

L 241.238899 91.619549 

L 238.838387 89.045315 

L 236.349497 86.556426 

L 233.775263 84.155913 

L 231.11882 81.846703 

L 228.383405 79.631607 

L 225.572351 77.513326 

L 222.689082 75.49444 

L 219.737112 73.577407 

L 216.720036 71.764565 

L 213.641531 70.058122 

L 210.505347 68.460157 

L 207.315306 66.972616 

L 204.075293 65.597312 

L 200.789257 64.335921 

L 197.4612 63.189979 

L 194.095179 62.160883 

L 190.695292 61.249887 

L 187.265684 60.458099 

L 183.810532 59.786485 

L 180.334045 59.235864 

L 176.84046 58.806906 

L 173.334033 58.500133 

L 169.819035 58.31592 

L 166.29975 58.254491 

L 162.780465 58.31592 

L 159.265467 58.500133 

L 155.75904 58.806906 

L 152.265455 59.235864 

L 148.788968 59.786485 

L 145.333816 60.458099 

L 141.904208 61.249887 

L 138.504321 62.160883 

L 135.1383 63.189979 

L 131.810243 64.335921 

L 128.524207 65.597312 

L 125.284194 66.972616 

L 122.094153 68.460157 

L 118.957969 70.058122 

L 115.879464 71.764565 

L 112.862388 73.577407 

L 109.910418 75.49444 

L 107.027149 77.513326 

L 104.216095 79.631607 

L 101.48068 81.846703 

L 98.824237 84.155913 

L 96.250003 86.556426 

L 93.761113 89.045315 

L 91.360601 91.619549 

L 89.05139 94.275992 

L 86.836295 97.011407 

L 84.718014 99.822461 

L 82.699127 102.70573 

L 80.782095 105.657701 

L 78.969253 108.674777 

L 77.26281 111.753282 

L 75.664844 114.889465 

L 74.177304 118.079507 

L 72.802 121.319519 

L 71.540609 124.605556 

L 70.394667 127.933612 

L 69.365571 131.299634 

L 68.454574 134.69952 

L 67.662786 138.129129 

L 66.991173 141.584281 

L 66.440552 145.060767 

L 66.011593 148.554352 

L 65.704821 152.06078 

L 65.520607 155.575777 

L 65.459178 159.095062 

L 65.520607 162.614348 

L 65.704821 166.129345 

L 66.011593 169.635773 

L 66.440552 173.129358 

L 66.991173 176.605844 

L 67.662786 180.060996 

L 68.454574 183.490605 

L 69.365571 186.890491 

L 70.394667 190.256513 

L 71.540609 193.584569 

L 72.802 196.870606 

L 74.177304 200.110618 

L 75.664844 203.30066 

L 77.26281 206.436843 

L 78.969253 209.515348 

L 80.782095 212.532424 

L 82.699127 215.484395 

L 84.718014 218.367664 

L 86.836295 221.178718 

L 89.05139 223.914133 

L 91.360601 226.570576 

L 93.761113 229.14481 

L 96.250003 231.633699 

L 98.824237 234.034212 

L 101.48068 236.343422 

L 104.216095 238.558518 

L 107.027149 240.676799 

L 109.910418 242.695685 

L 112.862388 244.612718 

L 115.879464 246.42556 

L 118.957969 248.132003 

L 122.094153 249.729968 

L 125.284194 251.217509 

L 128.524207 252.592813 

L 131.810243 253.854204 

L 135.1383 255.000146 

L 138.504321 256.029242 

L 141.904208 256.940238 

L 145.333816 257.732026 

L 148.788968 258.40364 

L 152.265455 258.954261 

L 155.75904 259.383219 

L 159.265467 259.689992 

L 162.780465 259.874205 

L 166.29975 259.935634 

L 169.819035 259.874205 

L 173.334033 259.689992 

L 176.84046 259.383219 

L 180.334045 258.954261 

L 183.810532 258.40364 

L 187.265684 257.732026 

L 190.695292 256.940238 

L 194.095179 256.029242 

L 197.4612 255.000146 

L 200.789257 253.854204 

L 204.075293 252.592813 

L 207.315306 251.217509 

L 210.505347 249.729968 

L 213.641531 248.132003 

L 216.720036 246.42556 

L 219.737112 244.612718 

L 222.689082 242.695685 

L 225.572351 240.676799 

L 228.383405 238.558518 

L 231.11882 236.343422 

L 233.775263 234.034212 

L 236.349497 231.633699 

L 238.838387 229.14481 

L 241.238899 226.570576 

L 243.54811 223.914133 

L 245.763205 221.178718 

L 247.881486 218.367664 

L 249.900373 215.484395 

L 251.817405 212.532424 

L 253.630247 209.515348 

L 255.33669 206.436843 

L 256.934656 203.30066 

L 258.422196 200.110618 

L 259.7975 196.870606 

L 261.058891 193.584569 

L 262.204833 190.256513 

L 263.233929 186.890491 

L 264.144926 183.490605 

L 264.936714 180.060996 

L 265.608327 176.605844 

L 266.158948 173.129358 

L 266.587907 169.635773 

L 266.894679 166.129345 

L 267.078893 162.614348 

L 267.140322 159.095062 

L 267.140322 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_13">

      <!-- 10 -->

      <g transform="translate(259.46429 118.425359)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_14">

      <path clip-path="url(#p2e984e04b5)" d="M 287.308436 159.095062 

L 287.234721 154.87192 

L 287.013665 150.653923 

L 286.645538 146.44621 

L 286.130788 142.253908 

L 285.470042 138.082125 

L 284.664106 133.935942 

L 283.713961 129.820412 

L 282.620765 125.740548 

L 281.38585 121.701322 

L 280.01072 117.707654 

L 278.49705 113.764411 

L 276.846686 109.876396 

L 275.061637 106.048346 

L 273.144078 102.284925 

L 271.096346 98.590719 

L 268.920936 94.970228 

L 266.620498 91.427864 

L 264.197834 87.967941 

L 261.655896 84.594676 

L 258.997782 81.312178 

L 256.226729 78.124447 

L 253.346114 75.035366 

L 250.359447 72.048698 

L 247.270366 69.168083 

L 244.082634 66.397031 

L 240.800136 63.738916 

L 237.426871 61.196979 

L 233.966949 58.774315 

L 230.424584 56.473876 

L 226.804093 54.298466 

L 223.109887 52.250734 

L 219.346467 50.333176 

L 215.518417 48.548127 

L 211.630402 46.897762 

L 207.687158 45.384093 

L 203.693491 44.008963 

L 199.654264 42.774047 

L 195.574401 41.680851 

L 191.458871 40.730706 

L 187.312688 39.92477 

L 183.140904 39.264024 

L 178.948602 38.749274 

L 174.740889 38.381147 

L 170.522892 38.160091 

L 166.29975 38.086376 

L 162.076608 38.160091 

L 157.858611 38.381147 

L 153.650898 38.749274 

L 149.458596 39.264024 

L 145.286812 39.92477 

L 141.140629 40.730706 

L 137.025099 41.680851 

L 132.945236 42.774047 

L 128.906009 44.008963 

L 124.912342 45.384093 

L 120.969098 46.897762 

L 117.081083 48.548127 

L 113.253033 50.333176 

L 109.489613 52.250734 

L 105.795407 54.298466 

L 102.174916 56.473876 

L 98.632551 58.774315 

L 95.172629 61.196979 

L 91.799364 63.738916 

L 88.516866 66.397031 

L 85.329134 69.168083 

L 82.240053 72.048698 

L 79.253386 75.035366 

L 76.372771 78.124447 

L 73.601718 81.312178 

L 70.943604 84.594676 

L 68.401666 87.967941 

L 65.979002 91.427864 

L 63.678564 94.970228 

L 61.503154 98.590719 

L 59.455422 102.284925 

L 57.537863 106.048346 

L 55.752814 109.876396 

L 54.10245 113.764411 

L 52.58878 117.707654 

L 51.21365 121.701322 

L 49.978735 125.740548 

L 48.885539 129.820412 

L 47.935394 133.935942 

L 47.129458 138.082125 

L 46.468712 142.253908 

L 45.953962 146.44621 

L 45.585835 150.653923 

L 45.364779 154.87192 

L 45.291064 159.095062 

L 45.364779 163.318205 

L 45.585835 167.536202 

L 45.953962 171.743915 

L 46.468712 175.936217 

L 47.129458 180.108 

L 47.935394 184.254183 

L 48.885539 188.369713 

L 49.978735 192.449577 

L 51.21365 196.488803 

L 52.58878 200.482471 

L 54.10245 204.425714 

L 55.752814 208.313729 

L 57.537863 212.141779 

L 59.455422 215.9052 

L 61.503154 219.599406 

L 63.678564 223.219897 

L 65.979002 226.762261 

L 68.401666 230.222184 

L 70.943604 233.595449 

L 73.601718 236.877947 

L 76.372771 240.065678 

L 79.253386 243.154759 

L 82.240053 246.141427 

L 85.329134 249.022042 

L 88.516866 251.793094 

L 91.799364 254.451209 

L 95.172629 256.993146 

L 98.632551 259.41581 

L 102.174916 261.716249 

L 105.795407 263.891659 

L 109.489613 265.939391 

L 113.253033 267.856949 

L 117.081083 269.641998 

L 120.969098 271.292363 

L 124.912342 272.806032 

L 128.906009 274.181162 

L 132.945236 275.416078 

L 137.025099 276.509274 

L 141.140629 277.459419 

L 145.286812 278.265355 

L 149.458596 278.926101 

L 153.650898 279.440851 

L 157.858611 279.808978 

L 162.076608 280.030034 

L 166.29975 280.103749 

L 170.522892 280.030034 

L 174.740889 279.808978 

L 178.948602 279.440851 

L 183.140904 278.926101 

L 187.312688 278.265355 

L 191.458871 277.459419 

L 195.574401 276.509274 

L 199.654264 275.416078 

L 203.693491 274.181162 

L 207.687158 272.806032 

L 211.630402 271.292363 

L 215.518417 269.641998 

L 219.346467 267.856949 

L 223.109887 265.939391 

L 226.804093 263.891659 

L 230.424584 261.716249 

L 233.966949 259.41581 

L 237.426871 256.993146 

L 240.800136 254.451209 

L 244.082634 251.793094 

L 247.270366 249.022042 

L 250.359447 246.141427 

L 253.346114 243.154759 

L 256.226729 240.065678 

L 258.997782 236.877947 

L 261.655896 233.595449 

L 264.197834 230.222184 

L 266.620498 226.762261 

L 268.920936 223.219897 

L 271.096346 219.599406 

L 273.144078 215.9052 

L 275.061637 212.141779 

L 276.846686 208.313729 

L 278.49705 204.425714 

L 280.01072 200.482471 

L 281.38585 196.488803 

L 282.620765 192.449577 

L 283.713961 188.369713 

L 284.664106 184.254183 

L 285.470042 180.108 

L 286.130788 175.936217 

L 286.645538 171.743915 

L 287.013665 167.536202 

L 287.234721 163.318205 

L 287.308436 159.095062 

L 287.308436 159.095062 

" style="fill:none;stroke:#b0b0b0;stroke-linecap:square;stroke-width:0.8;"/>

     </g>

     <g id="text_14">

      <!-- 12 -->

      <g transform="translate(278.097199 110.707356)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

   </g>

   <g id="line2d_15">

    <path clip-path="url(#p2e984e04b5)" d="M 166.29975 159.095062 

L 167.70432 158.996845 

L 169.088345 158.703151 

L 170.431445 158.216844 

L 171.713576 157.542673 

L 172.915186 156.687241 

L 174.017382 155.658951 

L 175.002081 154.467951 

L 175.852164 153.126052 

L 176.551613 151.646648 

L 177.085656 150.044613 

L 177.440885 148.336194 

L 177.605381 146.538888 

L 177.568818 144.671314 

L 177.322561 142.753074 

L 176.85975 140.804606 

L 176.175375 138.84703 

L 175.266333 136.90199 

L 174.131477 134.991486 

L 172.771645 133.137711 

L 171.189683 131.362876 

L 169.390448 129.689039 

L 167.380797 128.137932 

L 165.169565 126.73079 

L 162.767524 125.488179 

L 160.187334 124.42983 

L 157.443473 123.574477 

L 154.55216 122.939698 

L 151.53126 122.541766 

L 148.400179 122.395504 

L 145.17975 122.514149 

L 141.892098 122.909231 

L 138.560507 123.59045 

L 135.209266 124.565581 

L 131.863515 125.840377 

L 128.54908 127.418489 

L 126.099633 128.802101 

L 123.693851 130.357021 

L 121.343039 132.082346 

L 119.058522 133.976456 

L 116.851597 136.03701 

L 114.733493 138.260942 

L 112.715321 140.644464 

L 110.808035 143.183069 

L 109.02238 145.87154 

L 107.368854 148.703956 

L 105.85766 151.673707 

L 104.498662 154.773509 

L 103.301346 157.995421 

L 102.274776 161.330864 

L 101.427551 164.770644 

L 100.76777 168.304982 

L 100.302991 171.923533 

L 100.040195 175.615425 

L 99.985753 179.369286 

L 100.145389 183.173281 

L 100.524155 187.015146 

L 101.126396 190.882231 

L 101.955727 194.761537 

L 103.015009 198.639758 

L 104.306323 202.503327 

L 105.830957 206.338461 

L 107.589382 210.131206 

L 109.581245 213.867486 

L 111.805353 217.533149 

L 114.259665 221.114021 

L 116.941289 224.595952 

L 119.846477 227.964872 

L 122.970627 231.206833 

L 126.308284 234.30807 

L 129.853151 237.255046 

L 133.598093 240.034504 

L 137.535152 242.63352 

L 141.655565 245.039548 

L 145.949778 247.240476 

L 150.407469 249.224668 

L 155.017574 250.981015 

L 159.768312 252.49898 

L 164.647217 253.768641 

L 169.641167 254.780738 

L 174.736426 255.526709 

L 179.918673 255.998735 

L 185.173049 256.18977 

L 190.484198 256.093586 

L 195.836309 255.704794 

L 201.213166 255.018885 

L 206.598196 254.032251 

L 211.974517 252.742212 

L 217.324993 251.147037 

L 222.632287 249.245967 

L 227.878916 247.039226 

L 233.047305 244.528036 

L 238.119844 241.71463 

L 243.07895 238.602252 

L 247.907121 235.195168 

L 252.586996 231.498659 

L 257.101413 227.519023 

L 261.43347 223.263567 

L 265.566581 218.740592 

L 268.203441 215.581201 

L 270.739971 212.310013 

L 273.171564 208.930208 

L 275.493718 205.445152 

L 277.702035 201.858393 

L 279.792236 198.173659 

L 281.760161 194.394853 

L 283.601782 190.526047 

L 285.313207 186.571484 

L 286.890686 182.535566 

L 288.33062 178.422854 

L 289.629565 174.23806 

L 290.784239 169.986044 

L 291.791532 165.671808 

L 292.648504 161.300488 

L 293.01975 159.095062 

L 293.01975 159.095062 

" style="fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;"/>

   </g>

   <g id="patch_3">

    <path d="M 299.35575 159.095062 

C 299.35575 141.622309 295.913998 124.319455 289.227465 108.176736 

C 282.540932 92.034016 272.739653 77.365365 260.38455 65.010263 

C 248.029447 52.65516 233.360796 42.853881 217.218077 36.167347 

C 201.075357 29.480814 183.772504 26.039062 166.29975 26.039062 

C 148.826996 26.039062 131.524143 29.480814 115.381423 36.167347 

C 99.238704 42.853881 84.570053 52.65516 72.21495 65.010263 

C 59.859847 77.365365 50.058568 92.034016 43.372035 108.176736 

C 36.685502 124.319455 33.24375 141.622309 33.24375 159.095062 

C 33.24375 176.567816 36.685502 193.87067 43.372035 210.013389 

C 50.058568 226.156109 59.859847 240.82476 72.21495 253.179862 

C 84.570053 265.534965 99.238704 275.336244 115.381423 282.022778 

C 131.524143 288.709311 148.826996 292.151062 166.29975 292.151062 

C 183.772504 292.151062 201.075357 288.709311 217.218077 282.022778 

C 233.360796 275.336244 248.029447 265.534965 260.38455 253.179862 

C 272.739653 240.82476 282.540932 226.156109 289.227465 210.013389 

C 295.913998 193.87067 299.35575 176.567816 299.35575 159.095062 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p2e984e04b5">

   <path d="M 299.35575 159.095062 

C 299.35575 141.622309 295.913998 124.319455 289.227465 108.176736 

C 282.540932 92.034016 272.739653 77.365365 260.38455 65.010263 

C 248.029447 52.65516 233.360796 42.853881 217.218077 36.167347 

C 201.075357 29.480814 183.772504 26.039062 166.29975 26.039062 

C 148.826996 26.039062 131.524143 29.480814 115.381423 36.167347 

C 99.238704 42.853881 84.570053 52.65516 72.21495 65.010263 

C 59.859847 77.365365 50.058568 92.034016 43.372035 108.176736 

C 36.685502 124.319455 33.24375 141.622309 33.24375 159.095062 

C 33.24375 176.567816 36.685502 193.87067 43.372035 210.013389 

C 50.058568 226.156109 59.859847 240.82476 72.21495 253.179862 

C 84.570053 265.534965 99.238704 275.336244 115.381423 282.022778 

C 131.524143 288.709311 148.826996 292.151062 166.29975 292.151062 

C 183.772504 292.151062 201.075357 288.709311 217.218077 282.022778 

C 233.360796 275.336244 248.029447 265.534965 260.38455 253.179862 

C 272.739653 240.82476 282.540932 226.156109 289.227465 210.013389 

C 295.913998 193.87067 299.35575 176.567816 299.35575 159.095062 

M 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

C 166.29975 159.095062 166.29975 159.095062 166.29975 159.095062 

M 299.35575 159.095062 

z

"/>

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
<h2 id="Histogramme">Histogramme<a class="anchor-link" href="#Histogramme">&#182;</a></h2><p>Darstellung von Häufigkeitsverteilungen</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[150]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">zahlen</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">10000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">zahlen</span><span class="p">,</span><span class="n">bins</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[150]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([   2.,    9.,   39.,   94.,  185.,  371.,  618.,  914., 1176.,
        1385., 1419., 1303., 1040.,  662.,  412.,  207.,   99.,   40.,
          18.,    7.]),
 array([-3.70059034, -3.33461608, -2.96864181, -2.60266755, -2.23669328,
        -1.87071902, -1.50474475, -1.13877049, -0.77279622, -0.40682196,
        -0.04084769,  0.32512658,  0.69110084,  1.05707511,  1.42304937,
         1.78902364,  2.1549979 ,  2.52097217,  2.88694643,  3.2529207 ,
         3.61889496]),
 &lt;a list of 20 Patch objects&gt;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>



<div class="output_svg output_subarea ">
<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"

  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Created with matplotlib (https://matplotlib.org/) -->

<svg height="297.190125pt" version="1.1" viewBox="0 0 403.97 297.190125" width="403.97pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

 <defs>

  <style type="text/css">

*{stroke-linecap:butt;stroke-linejoin:round;}

  </style>

 </defs>

 <g id="figure123_1">

  <g id="patch_1">

   <path d="M 0 297.190125 

L 403.97 297.190125 

L 403.97 0 

L 0 0 

z

" style="fill:#ffffff;"/>

  </g>

  <g id="axes_1">

   <g id="patch_2">

    <path d="M 39.65 273.312 

L 396.77 273.312 

L 396.77 7.2 

L 39.65 7.2 

z

" style="fill:#ffffff;"/>

   </g>

   <g id="patch_3">

    <path clip-path="url(#p92230372ce)" d="M 55.882727 273.312 

L 72.115455 273.312 

L 72.115455 272.954791 

L 55.882727 272.954791 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_4">

    <path clip-path="url(#p92230372ce)" d="M 72.115455 273.312 

L 88.348182 273.312 

L 88.348182 271.704558 

L 72.115455 271.704558 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_5">

    <path clip-path="url(#p92230372ce)" d="M 88.348182 273.312 

L 104.580909 273.312 

L 104.580909 266.346419 

L 88.348182 266.346419 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_6">

    <path clip-path="url(#p92230372ce)" d="M 104.580909 273.312 

L 120.813636 273.312 

L 120.813636 256.523163 

L 104.580909 256.523163 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_7">

    <path clip-path="url(#p92230372ce)" d="M 120.813636 273.312 

L 137.046364 273.312 

L 137.046364 240.27014 

L 120.813636 240.27014 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_8">

    <path clip-path="url(#p92230372ce)" d="M 137.046364 273.312 

L 153.279091 273.312 

L 153.279091 207.049674 

L 137.046364 207.049674 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_9">

    <path clip-path="url(#p92230372ce)" d="M 153.279091 273.312 

L 169.511818 273.312 

L 169.511818 162.934326 

L 153.279091 162.934326 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_10">

    <path clip-path="url(#p92230372ce)" d="M 169.511818 273.312 

L 185.744545 273.312 

L 185.744545 110.067349 

L 169.511818 110.067349 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_11">

    <path clip-path="url(#p92230372ce)" d="M 185.744545 273.312 

L 201.977273 273.312 

L 201.977273 63.27293 

L 185.744545 63.27293 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_12">

    <path clip-path="url(#p92230372ce)" d="M 201.977273 273.312 

L 218.21 273.312 

L 218.21 25.944558 

L 201.977273 25.944558 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_13">

    <path clip-path="url(#p92230372ce)" d="M 218.21 273.312 

L 234.442727 273.312 

L 234.442727 19.872 

L 218.21 19.872 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_14">

    <path clip-path="url(#p92230372ce)" d="M 234.442727 273.312 

L 250.675455 273.312 

L 250.675455 40.59014 

L 234.442727 40.59014 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_15">

    <path clip-path="url(#p92230372ce)" d="M 250.675455 273.312 

L 266.908182 273.312 

L 266.908182 87.563163 

L 250.675455 87.563163 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_16">

    <path clip-path="url(#p92230372ce)" d="M 266.908182 273.312 

L 283.140909 273.312 

L 283.140909 155.075721 

L 266.908182 155.075721 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_17">

    <path clip-path="url(#p92230372ce)" d="M 283.140909 273.312 

L 299.373636 273.312 

L 299.373636 199.726884 

L 283.140909 199.726884 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_18">

    <path clip-path="url(#p92230372ce)" d="M 299.373636 273.312 

L 315.606364 273.312 

L 315.606364 236.340837 

L 299.373636 236.340837 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_19">

    <path clip-path="url(#p92230372ce)" d="M 315.606364 273.312 

L 331.839091 273.312 

L 331.839091 255.63014 

L 315.606364 255.63014 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_20">

    <path clip-path="url(#p92230372ce)" d="M 331.839091 273.312 

L 348.071818 273.312 

L 348.071818 266.167814 

L 331.839091 266.167814 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_21">

    <path clip-path="url(#p92230372ce)" d="M 348.071818 273.312 

L 364.304545 273.312 

L 364.304545 270.097116 

L 348.071818 270.097116 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="patch_22">

    <path clip-path="url(#p92230372ce)" d="M 364.304545 273.312 

L 380.537273 273.312 

L 380.537273 272.061767 

L 364.304545 272.061767 

z

" style="fill:#1f77b4;"/>

   </g>

   <g id="matplotlib.axis_1">

    <g id="xtick_1">

     <g id="line2d_1">

      <defs>

       <path d="M 0 0 

L 0 3.5 

" id="m5bd1a607e8" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="42.602462" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_1">

      <!-- −4 -->

      <defs>

       <path d="M 10.59375 35.5 

L 73.1875 35.5 

L 73.1875 27.203125 

L 10.59375 27.203125 

z

" id="DejaVuSans-8722"/>

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

      <g transform="translate(35.231368 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-52"/>

      </g>

     </g>

    </g>

    <g id="xtick_2">

     <g id="line2d_2">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="86.957295" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_2">

      <!-- −3 -->

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

      <g transform="translate(79.586201 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

    <g id="xtick_3">

     <g id="line2d_3">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="131.312127" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_3">

      <!-- −2 -->

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

      <g transform="translate(123.941034 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_4">

     <g id="line2d_4">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="175.66696" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_4">

      <!-- −1 -->

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

      <g transform="translate(168.295866 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-8722"/>

       <use x="83.789062" xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_5">

     <g id="line2d_5">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="220.021792" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_5">

      <!-- 0 -->

      <defs>

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

      </defs>

      <g transform="translate(216.840542 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="xtick_6">

     <g id="line2d_6">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="264.376625" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_6">

      <!-- 1 -->

      <g transform="translate(261.195375 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

      </g>

     </g>

    </g>

    <g id="xtick_7">

     <g id="line2d_7">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="308.731458" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_7">

      <!-- 2 -->

      <g transform="translate(305.550208 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

      </g>

     </g>

    </g>

    <g id="xtick_8">

     <g id="line2d_8">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="353.08629" xlink:href="#m5bd1a607e8" y="273.312"/>

      </g>

     </g>

     <g id="text_8">

      <!-- 3 -->

      <g transform="translate(349.90504 287.910437)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-51"/>

      </g>

     </g>

    </g>

   </g>

   <g id="matplotlib.axis_2">

    <g id="ytick_1">

     <g id="line2d_9">

      <defs>

       <path d="M 0 0 

L -3.5 0 

" id="mad5769c4a9" style="stroke:#000000;stroke-width:0.8;"/>

      </defs>

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="273.312"/>

      </g>

     </g>

     <g id="text_9">

      <!-- 0 -->

      <g transform="translate(26.2875 277.111219)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_2">

     <g id="line2d_10">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="237.59107"/>

      </g>

     </g>

     <g id="text_10">

      <!-- 200 -->

      <g transform="translate(13.5625 241.390289)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-50"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_3">

     <g id="line2d_11">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="201.87014"/>

      </g>

     </g>

     <g id="text_11">

      <!-- 400 -->

      <g transform="translate(13.5625 205.669358)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-52"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_4">

     <g id="line2d_12">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="166.149209"/>

      </g>

     </g>

     <g id="text_12">

      <!-- 600 -->

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

      <g transform="translate(13.5625 169.948428)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-54"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_5">

     <g id="line2d_13">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="130.428279"/>

      </g>

     </g>

     <g id="text_13">

      <!-- 800 -->

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

      </defs>

      <g transform="translate(13.5625 134.227498)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-56"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_6">

     <g id="line2d_14">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="94.707349"/>

      </g>

     </g>

     <g id="text_14">

      <!-- 1000 -->

      <g transform="translate(7.2 98.506568)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-48"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_7">

     <g id="line2d_15">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="58.986419"/>

      </g>

     </g>

     <g id="text_15">

      <!-- 1200 -->

      <g transform="translate(7.2 62.785637)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-50"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

    <g id="ytick_8">

     <g id="line2d_16">

      <g>

       <use style="stroke:#000000;stroke-width:0.8;" x="39.65" xlink:href="#mad5769c4a9" y="23.265488"/>

      </g>

     </g>

     <g id="text_16">

      <!-- 1400 -->

      <g transform="translate(7.2 27.064707)scale(0.1 -0.1)">

       <use xlink:href="#DejaVuSans-49"/>

       <use x="63.623047" xlink:href="#DejaVuSans-52"/>

       <use x="127.246094" xlink:href="#DejaVuSans-48"/>

       <use x="190.869141" xlink:href="#DejaVuSans-48"/>

      </g>

     </g>

    </g>

   </g>

   <g id="patch_23">

    <path d="M 39.65 273.312 

L 39.65 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_24">

    <path d="M 396.77 273.312 

L 396.77 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_25">

    <path d="M 39.65 273.312 

L 396.77 273.312 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

   <g id="patch_26">

    <path d="M 39.65 7.2 

L 396.77 7.2 

" style="fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;"/>

   </g>

  </g>

 </g>

 <defs>

  <clipPath id="p92230372ce">

   <rect height="266.112" width="357.12" x="39.65" y="7.2"/>

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
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Geogrpahische-Daten">Geogrpahische Daten<a class="anchor-link" href="#Geogrpahische-Daten">&#182;</a></h2><p>Mit Matplotlib können auch geografische Daten dargestellt werden. hier ein <a href="https://matplotlib.org/basemap/">Tutorial</a> . In Meinem Projekt <a href="../../../../../DataScience/Praxis/Beispiel-Projekte-handsonml/02_California_Housing.ipynb">California-Housing</a> wurden ebenfalls Geografische Daten berücksichtigt.</p>

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
    </div>
  </div>
</body123>

 


</div>
