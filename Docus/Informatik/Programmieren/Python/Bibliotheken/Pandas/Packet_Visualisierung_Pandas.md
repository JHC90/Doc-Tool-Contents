<!DOCTYPE html>
<div id="jupyter">
<head123><meta charset="utf-8" />

<title>Packet_Visualisierung_Pandas</title>

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
<h1 id="Pandas-BuiltIn-Visualisierung">Pandas BuiltIn Visualisierung<a class="anchor-link" href="#Pandas-BuiltIn-Visualisierung">&#182;</a></h1><p>Es basiert auf <em>Matplotlib</em>, ist aber direkt in Pandas verfügbar, um eine leichtere Handhabung zu gewährleisten. Geht erstmal leichter als die Matplotlib, kann aber um die entsprehcenden Funktionalitäten von Matplotlib erweitert werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Bibliotheken // hier wird kein matplotlib installiert</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Daten Laden</span>
<span class="n">df0</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;./data/df1&quot;</span><span class="p">)</span>
<span class="n">df1</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;./data/df1&quot;</span><span class="p">,</span><span class="n">index_col</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
<span class="n">df2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;./data/df2&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Info">Info<a class="anchor-link" href="#Info">&#182;</a></h2><p>wie in <a href="./Packet_Visualisierung_Matplotlib.ipynb">matplotlib</a> können ganze Stylesheets Paletten verwendet werden.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df1</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b12fac7f0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># use new style</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;fivethirtyeight&#39;</span><span class="p">)</span> <span class="c1"># &lt;= dark_background, bmh,fivethirtyeight, ggplot</span>
<span class="n">df1</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b13113d30&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Diagrammarten-In-Pandas">Diagrammarten In Pandas<a class="anchor-link" href="#Diagrammarten-In-Pandas">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Area-Plot">Area-Plot<a class="anchor-link" href="#Area-Plot">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">area</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.4</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b13150f28&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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sX379nPev3fvXm677Tai0Sjz58/n6aefxrbPXb5a43MVTvcKQin482MYJEnmRP1cDusOdkvV7K//AmbjbJojfhbXOmjwqSLxCMJnMK4nfUdHB2vXruWhhx7i73//O0uWLOHrX/86R48eHfP+WCzG1772NcLhMG+//TY//elPee6553j++efP+d+ZJYoMhDJQ61ZoCqqoDpUT0SY8DQ0sCru5otpBrVsR5f+CcAGMK/m88MILfPOb3+See+6hubmZ9evXE4lE2Lx585j3//GPfySVSvHSSy/R0tLC8uXL+d73vseLL754ztWPKDIQykVEU/i3OieLAhZzgw4xtE0QLrDzLjV0Xeef//wnDz744KjrN954Izt37hzzM7t27eKaa65B07TCtZtuuoknn3ySI0eOMHPmzDE/9x/N3gmELoyp+fJSR3Bpmec7/z3C+Infzwunwv8tz/t1rr+/H9M0qaurG3W9rq6Onp6eMT/T09Mz5v0jPxMEQRA+38a9l3Dm2QXbts95nmGs+8e6LgiCIHz+nDf51NTUoCjKWSuWvr6+s1Y3I8Lh8Jj3A5/6GUEQBOHz47zJx+l0cuWVV7J169ZR17du3crSpUvH/MySJUt47733SKfTo+6vr69nxowZnzFkQRAEodKNa9utvb2dLVu28Jvf/IaPPvqINWvW0N3dzb333gvAj3/8Y7761a8W7r/zzjvRNI1Vq1bR2dnJn//8Z5555hlWrVoltt0EQRCE8SWfFStW8JOf/IT169fzxS9+kR07dvCHP/yBxsZGALq7uzl06FDh/mAwyJ/+9Cc++eQTbrjhBh555BHa29t54IEHRv29Ez24KoztF7/4BTfccAPTp0+nqamJu+66i87OzlKHdUnYsGEDoVCIRx55pNShVKzu7m7uv/9+mpqaiEQiLF26lG3btpU6rIpkmiZPPPFE4bm5cOFCnnjiCbLZzz6Bd6pJg4OD45+adQF1dHSwcuVKNmzYQGtrK5s2bWLLli3s2LGD6dOnlyKkirVixQpWrFjB4sWLsW2bp556ivfff5+dO3dSVVVV6vAq1vvvv8+3vvUt/H4/1157LevXry91SBVncHCQtrY2WltbWblyJTU1NRw5coRoNEpzc3Opw6s4GzZs4Lnnniucody7dy/f/e53aW9v59FHHy11eBNSsuRz0003sWDBAn71q18Vri1evJjly5fzox/9qBQhXTISiQSNjY387ne/49Zbby11OBVpaGiItrY2nn32WX72s5/R0tIiks8krFu3jnfffZe33nqr1KFcEu666y6qqqp4+eWXC9fuv/9+BgYGeO2110oY2cSV5Nj2yMHVG2+8cdT1cx1cFcYvkUhgWRahUKjUoVSs1atXs3z5ctra2kodSkV74403uPrqq7n33nuZPXs2119/PRs3bjxvn0dhbK2trWzbto39+/cDsG/fPt555x1uvvnmEkc2cSVppjaZg6vC+K1du5YrrriCJUuWlDqUivTrX/+agwcP8sorr5Q6lIp3+PBhXn31VVatWsXq1avZs2cPa9asAWDlypUljq7yrF69mkQiwdKlS1EUhWw2y8MPP8y3v/3tUoc2YSXt5DnRg6vC+T3++OPs2LGDN998E0URc5Em6sCBA6xbt46//vWvOJ3OUodT8SzL4qqrripspS9atIiDBw+yadMmkXwmoaOjg9///vds2rSJefPmsWfPHtauXUtjYyN33313qcObkJIkn8kcXBXO77HHHqOjo4O//OUvn9o/Tzi3Xbt20d/fzzXXXFO4Zpom27dvZ/PmzZw4cQKXy1XCCCtLJBI5q7Bg7ty5HDt2rEQRVbYf/vCHPPDAA9xxxx0ALFiwgKNHj/LLX/5SJJ/xKD64evvttxeub926ddR5IWH81qxZQ0dHB6+//jpz584tdTgVa9myZVx11VWjrrW3t9PU1MT3v/99sRqaoNbWVrq6ukZd6+rqEhWtk5RMJs/a0VAUBcuyShTR5JVs2629vZ377ruPq6++mqVLl7J58+ZRB1eF8Xv44Yd57bXX+O1vf0soFOLkyZMAeL1efD7RlXkiQqHQWYUaHo+HqqoqWlpaShRV5Vq1ahW33HILP//5z1mxYgW7d+9m48aN/OAHPyh1aBXpy1/+Ms888wwzZsxg3rx57N69mxdeeIFvfOMbpQ5twkpWag25Q6bPPvssJ0+eZP78+Tz11FNcd911pQqnYn1aVduaNWt47LHHpjiaS8+yZctEqfVn8NZbb7Fu3Tq6urpoaGjgO9/5Dvfdd594vzsJ8XicJ598ktdff52+vj4ikQh33HEHjz76KG63u9ThTUhJk48gCILw+STGMwqCIAhTTiQfQRAEYcqJ5CMIgiBMOZF8BEEQhCknko8gCIIw5UTyEQRBEKacSD6CIAjClBPJRxAEQZhyIvkIgiAIU+7/AfO+bJho4UZXAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Bar-Plot">Bar-Plot<a class="anchor-link" href="#Bar-Plot">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b132584e0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">stacked</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b130bceb8&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Histogramm">Histogramm<a class="anchor-link" href="#Histogramm">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df1</span><span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">bins</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span> <span class="c1"># Anzahl der Bins kann man dynamisch hinzufügen</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[8]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b133ded68&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Lineplots">Lineplots<a class="anchor-link" href="#Lineplots">&#182;</a></h3><p>die grafische Konfiguration des Plots kann wie mit den <a href="./Packet_Visualisierung_Matplotlib.jpynb">matplotlib Funktionen</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df1</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">line</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">3</span><span class="p">),</span><span class="n">lw</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1"># index wird automatisch übernommen // klassisich die </span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[9]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b134fd320&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="ScatterPlott">ScatterPlott<a class="anchor-link" href="#ScatterPlott">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df1</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="n">y</span><span class="o">=</span><span class="s1">&#39;B&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b145304e0&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbQAAAEfCAYAAAAp7zNrAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nO2de3QcxZX/vz0zmpHkkRhJlt8PYlbGGLDATpRdHOzFTkQeJDY4xhDWzi9xIMuyyW9/CQmPQ+wYCN5ssuRsEsIJBjYJsCcmtnh5E3AAx8ZkA1kbbB7BKHHkp16WNJZG0rz798eoRt3VVT09L830zP2cw8Ga6empru6pb91bt+5V/H6/CoIgCIKwOY5CN4AgCIIgcgEJGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJQEJGkEQBFESlLygtbe3F7oJWUHtLyzU/sJC7S8sdmt/yQsaQRAEUR6QoBEEQRAlAQkaQRAEURKQoBEEQRAlAQkaQRAEURKQoBEEQRAlgavQDSAIO9IxGMFN+/w4E4phsseJbct9mFtTUehmEURZQxYaQWTATfv8eL03jKODMbzeG8aNe/2FbhJBlD0kaASRAWdCMdO/CYKYeEjQCCIDJnucpn8TBDHxkKARRAZsW+5DS6Mb82qdaGl0Y9tyX6GbRBBlj22CQrZt24b//M//xIkTJwAACxYswK233oorr7yywC0jypG5NRXYfVVjoZtB5AEK+LEvtrHQZsyYgS1btmDv3r3Ys2cPli1bhhtuuAFvv/12oZtGEEQJQQE/9sU2FtqnPvUp3d/f+ta38Mgjj+CPf/wjLrroogK1iiCIUoMCfuyLbSw0LbFYDDt37sTw8DBaWloK3RyCIEoICvixL4rf71cL3QirvPPOO2htbUUwGMSkSZOwbds20zU0u9XyIQii8JwaVbDpfTcGIgp8FSrumR/GzCrbDJMlTVNTk+n7thK0cDiMkydP4uzZs3j22Wfx85//HLt27cLChQuln2lvb0/ZCcUMtb+w2LH92qCGSWoYj1853bZBDXbsfy3U/onFVi5Ht9uNefPm4dJLL8XmzZtx8cUX4yc/+Umhm0UQRYU2qOGtIScFNRBlg60EjScejyMcDhe6GQRRVFBQA1Gu2CbK8dvf/jZaW1sxc+ZMBAIB7NixA/v378eTTz5Z6KYRRFEx2ePEUcR0fxNEOWAbQevu7sZNN92Enp4e1NbW4sILL8SOHTuwcuXKQjeNIIqKbct9uHHv+BoaZTEhygXbCNqDDz5Y6CYQREZMdOYJbRaT9vZ22waEEES62HoNjSDsAGWeIIiJgQSNIPIMBWkQxMRAgkYQeYYyTxDExECCRhB5hkrNEMTEYJugEIKwK1RqhiAmBhI0giByAtURIwoNuRwJgsgJFM1JFBoSNIIgcgJFcxKFhlyOBFFG5NMtSCm3iEJDFhpBlBH5dAtSNCdRaMhCI4gJoFgCJvLpFqRoTqLQkKARhEWyESVmGQHAUcRw415/QQb/QrgFi0XMidKHBI0gLJKNKBVLwIQ2Ez8Tl1zDC1gwGsfhgSgAcb+R4BG5ggSNIMYQDaxashGlYgmYkLkFcykqvPDzl8r3W7FYr4T9oaAQghgjVcBENjkZiz1gIpfBIgahV/V/8v1WLNYrYX/IQiOIMVINrNm464o9YCKXosJbowt8LnicDmm/FYv1StgfEjSCGCPVwFrsopQNuRQVkfCbuS8nYl2PKA9I0AhiDNHAGu4qj/RNuRSVdIW/lCcKxMRCgkYQY4gG1vauAjVmgillUaEoyvKBgkIIgihpKGly+UAWGlFW5Gq2Xkqz/lK6FhEURVk+kKARZUWu9jzZfe+UVsR6RuIIRBOx9Zlci0gQVRVFI5IURVk+kKARZUWuZut2n/VrBZkn3WsRiTuAjASfF8c75yhoSqs1RiiKsnwgQSPKilzN1u0+6zcTrXSvxYq4WxVJXhw3Bd3Ytyit5hgo5YAXQo9tgkLuv/9+XHHFFZg9ezbOO+88rFu3Du+++26hm0XYjFxl7Cj2zB+Mk6MKWnf1YvHOLrTu6sWxoQgAo2h5XUrG1yLKoJJpVhVe+AYiSlptIcob21ho+/fvx8aNG7F48WKoqor77rsPq1evxmuvvYa6urpCN4+wCbmardtl1r/pfTfeGjK6/tLd/GyGzKWXiZuPt3x9FarJ0QShxzaC1tbWpvv7pz/9KebMmYM//OEP+MQnPlGgVhFEcePnLBxmAeVSkGXnsnp+7bqZ16mgud6Foag6toZ2NidtJMoD2wgaTyAQQDweh89XnK4eIv+Uerg5I5vr9FWoOBEc/9uK62+i+5UPUGlpdGPvqoQYtrfTnjHCOrYVtNtvvx0XX3wxWlpaCt0UokDYPXTeKtlc5z3zw7jv+Dlpuf4mul8nImK02LcWELlB8fv9tnNS33nnnWhra8Pzzz+Pc889V3pce3v7xDWKmHCu+d9KnAiOxzXNroyj7YNBk0/Yh5OjCja974Y/oqA7pCCsjrsO832dE92vXzzkwVtD45bjxTUxPNocMhyn7RNfhYp75ocxs8ra8MV/x6KaGFTA8Nojgu8lioemJvNNHLaz0O644w60tbXhueeeMxUzIHHx7e3tKTuhmKH2y5l+pBcnguOuquk1lWhqmp3T7xC1fyJccrfs6k0Gc/Ckc52Z9P9E9KuWx6dFpAEq2vZr++REELjv+DmWLcfhw12AJtgkoLjH/qV/ralpTvYXpEHbfju6yO02/thK0G677Ta0tbVh165dmD9/fqGbQxSYQm2YteqSkw1gVgY23u3mcQIzJyXC4Tct8aJ1V2/eBsZs+jWTQdtqgEo+KoZP5F7CcnGRFxLbCNqtt96K7du34/HHH4fP50N3dzcAYNKkSfB6vQVuHVEIUg2E+ZoRWx1YZQOYlYGNH4Cb693JY1p39eZ1YOT7tWMwYllA8zloZ7OZPZdbCzLF7tll7IBtBO3hhx8GAKxatUr3+m233YY77rijEE0iipx8Da5WB9aukaj+79HE31YGNjMrKd2BkQ+LVxQkw+KtiHw6/ZjPQTsfFcMn0kKye3YZO2AbQfP7KXyXSI98Da7blvuw/qV+HBmMAioQisVxbChiEIb+kD5goT+Y+NvKwGZmfaY7MMryNloV+XT6MZ+Dtl02s8ugnJL5xzaCRhDpksvBlXdfKgrAxvVD/VGhMPg8QCCq/xvIfmDjP59qTc1MgLpGoindien0Iw3acuwuyHaABI0oWXI5uPJuNw+XBVUkGjOqK3ByOKz7G8h+YOM/n2pNjRckLf0hFceHxZ9lIt41GoXXpcDnSVyDWT/me9C2Y6QgMXGQoBElSy4HV4NgcTlzRVZLPq0V7cB+atjcJahth3YNzetU8N7ZqPSzvKtyYZ3b0J+ZCEw2olTskYL5KH9DWIcEjSh7rAywvJVzfq0LlS6HqVjl2lqRFeXk4cVV1o7WXb0Ix+WftbJ2lonAZCNKxR4pmI/yN4R1SNCIsqZjMIKPPNObsmJzLrPT56KdPB4HMNPrTMsSNOx1c0D3WStrZ5kITD72k+WDTCxJKn9TWEjQiLLmpn1+g0iIBthsrK1sXGzss4f6wzAb95sbjO7AVBj2ujW4de2y4jIVCUyq683HfrJ8kIklabfyN6W2JkmCRmRMKfwYROKV61l/qoHRrB9lIfdAYhnP7Uy4PzPJ5nF6JAKvS0F9pYJpVcZzWBFxkcDcuNf8ekWfsfosTWSkYCaWJH9txV7+ptjXJNOFBI3ImFL4MfAzaq9LyfmsX7bBmmHWj2aDqIrE1oFKlyOtiYQh2KMqPZFIJT58mw/1hXX79ESilO/sJ5mQiSXJX1uxl78p9jXJdHGkPoQgxJTCj2Hbch9aGt2YV+tES6Mbr65utBSl17qrF4t3dqF1Vy+ODUVMj5dtsGaY9SM/iHocsLRlwIxs7xsTxKODMbzeG8YlO3qw7OnuZD/wbQ7FEymmsm1Tuv2eLfyzUYp76vh7ZffsJWShERlj11Q+2bpK07VMZRusGWb9mMqlxx9vhWzvGy82KoDDA+Oby7ct96HlqR7dmt+h/jAW7+zKaPN2ch2xL4zQWFTmRFhx5bARutQ2wpOgERlj1x9Dtq7SdC0c2QZrhlk/igbVdDOF8GR737wuceQe64e5NRVornfrRDcUA44OxnAUMSx9uhdTqh26tpq1SbaOePBMGK27em25dlsslJpok6CVIBMVrGHXH0O2Lrd0LZxUApJuP6bKFLL06V5T12nW900SuCezLE8FYknLCgACURWBMXFjkwmzNsnuT1QFXu8N58VSK4WAp3KE1tBKEH6NI9X6RbmRybqBdv0mGI2jud5leW2FDdZtH2sAAFy9uy+na0D8gB+Iqmhp60Hrrl6cGs39PqhAzKhoi+pcQsvy4JppaG5wG45nWJlMpLo/+Vi7pd+QPSELrQTJ1AIpl1lpui430abmlkY39q5KzyrgXZ0bXu6Hx+nIur9FuRpD8YT1YiVThei+qyqkzwLvcmyud2HvqqnS82v7m89wYmUywd+vYDSOwwPji5KnArGcux5LIeCpHCFBK0EyXfQvhTB8K1gpYMkG9M6hSgxEjRk6tAOc1YkAPyi+549aCnJIdf5ty31o2dmDkMAVaCVThei+A5A/C9z3qNzfovayzx4biqS9fsffL3YOttmciXexFBMlCgcJWgmSyaJ/x2AEh/r0C+/lMis1H9AdEC0aaQc4qxMBfpDk8yimU/n6oWU+fTkbByBKqH8mrJhGF4q+V9QO7Wu8y5H/26w/crHuys6xeGcXjg6Ot6tYiokShYMErQTJZNC4aZ9ft3APlM+sVLTx2eWQWzYK9EU9rbqnzFxvgLy/RefnRUOE16UgEB2PLrQqtKwdMguFP74zEMPUX5wCVGCBz4W+CXLXUTFRgoeCQggAgkS1TpTNrFS08ZkfHL0uJbmhWcV4UU/AepCJNlBiSrX+p8cnBmZ0DEbQM6KfaUz2OFOKhNelGL6DhbmzYBTmaj05HIUDicHA61KweYnXdFOx9j2vS8FoHEnX36H+KPwhfVtSCU2mG6bT2fg80ZuyicJAgkYAMA46zfVu2wWEZDpo8RudfZ7xwXJ2ZTyZQWSmV99HTFQyyShh6O8GcX/zyZNZai6RSCgAXErimO0frTMcow1zZ+d+vTeM0yNxxAHEkYiQ3HIgYBqZaSbMABCOq1hUJ44CFd0jPqKQRWimun/adrDQfxkUtVgekMuRAFAaawaZBrWINj6zwbK9vR1NTbMByF1cZu4pWUCH1f7mLbEp1Y7k55c+rQ9WmTRmlU32ODHLmwijX/9CJ94NOKH1brJzyqw8WZFPUZ+KNlmH44n8kvtWG/uEP19LW4+hWKo2yOOB84VNTBuKWiwPSNAIAKWxZpDpoGVVXDIRfZkgpOpvJoR8NeqekXgyyGP7R+uw5UBAtybHNiyvf6kflS4HBiIKKp2KMFRelvFD+x2nR/RWkqFPJZusrYglAMO6rZVzAOlvMaGoxfKABI0oGTIdtKyKuei4dDPPWxVZPt2TxwFUOBSdaN35+iA8zoTLLxLXK8uRwehYLsVElKZXY70lhVggRgr0mTx40eP7VLTJWnQcIF4P1F4fFOjyP5rdv3St8VLwQBCpIUEjSoZcD1odgxF88ZAHw4f1Ye9aEdNGK4oG1kxFlhc+tn4X0ISpa/exGeB0Zkq1AwfXTNO9JhIjt0NvNdVXKlhYVSHtU/76PI7EeqCo70XFVBnsM/z9C3eNr3Vp+/1UIL2JQil4IIjUkKARJUOuB62b9vnx1pATgD7s3azoJj+wagdpr1NBKBaX7gvjhVKLKJSeX3vyOIGZk5yY7HFiMBTFe4Pj5/A6je5FUS2482qdONQ/vo1hWpXLkuVzeiQCfyghgDIMkbSOhFBr+4L/rvau8X+b9ftEuBDLJZOOnSFBI8qajsEINuzpxxF/FFAS1Z8fW1lvur/MzBrgB1btIJ2qiCU/YIvchOtf6seRwSigAvwQ3lzvxu6rGtExGMFlT/fo3lM4nekYjCAUiyddfey6gUTtsq6RKPpDKk6PRKRppbQDvD805qoMqDgeEGft4AW0ucGd1gSEX89zO4BZGkHMN+WSScfO2ErQXn31VfzoRz/CoUOH0NnZiQceeAA33HBDoZtF2Jib9vlxWGORaOt6iSyY1l29hkAN4frUGOm4yUQRjbybsNLl0K0zib77pn1+jHCaO8S5+jbs6dddt6IgKVi7r2pE665eHB8OIxAFTg4bBUqU31ILLz5A9i5hfn+b26EY+idTrFhfFClZ/NhK0IaHh7Fw4UJcf/31+Md//MdCN4ewMWwAO3jG6MLS7i9b/0InAoo7mRRXa0EpANxOYF6NM2nV8aTjJuMFtGdkPBsJ3zZGhE+kKDhG9F1H/PrsKO/5o2mJr9l6GGAUH0DuErbqyquvVBAIqLq/c4UV64siJYsfW22sbm1txaZNm7Bq1So4HLZqui0op2wKbAATjcna/WWPNIeSG3f5IAoViag8ZtWJ4C2VCgXSDdjblvt0UYWBqGo4Lz+IssKZ2s3CoiwnBmuI1wIF2PByf3LzsVkaNFHeT550xMbqpudpVS7Tv7PBivWVyQZ6YmIhVSCSFHs2hVwKrsxdVCVJQQWYz8hl5+MtlagKaUDIjXv9CHKiKQoyke0f+2NvGBc9eVpXr+3impiw2Of5tS7D30cG9VabArH4ivJ+8vBiY3bvzMTk5KiScR26dLCSvizfde2I7LGVy5HIL8W+RpDLRXlRDTEAmO51Ct1dfBCFE9CtU8nEjneTqRCXOpG5JkVBJlOqHbrwfe25Tw6rODkcRXO9CwfXTEN7e7vweu77cC2ue3EAwZiKCgUIqyqs3m4reSRvuqASy57pTgbbaPtLe+9kuSoZm953462h8X7JpA4dw8y1mc76HgWHFC8lLWjt7e26/9uViWr/JNUDbezcJDWck+/OVfs7hyqhdSp0DgUzPvedcxRsCrrxXsCBsDpu8VTEwrh8x3H4Iwp8FSruma8A7e344iHPWAh/gvOrY/A4E/XGfBUq7pxzFu3tRov2HEXfp7K289fmhIqFNXHhefn7JOJPAxHT5/+OQx4EoolzRFXgPb9YIFmm/mt/3YnHF4ck388EO9GPgaiKr+4/i5G43O3Irv+LmnYAQLVD35f+SKXwc5mgvYdHEcP6FzrxSPO4Ca1NsxXu8uu2DOjbkN5zSONP7mhqajJ9v6QFrampaSwXn3knFDMT2f7HpxmLL2a7zyZV+9PZ2zP9SC9OBMdn69NrKpN5FtM9bxOAfYuMBSe11ZBPBBMWwr7PzsHw4S5oC45FXG68ZiHCjvXpob6wzk3Ht52/tiWNHumsX3ufRGVoAEBxKLrnn++PgXgEsrxVLgWIqfp33x9xwj3tXKgq4Kjoh8eRsLwcKjAqEC4zMdNeP9+v07wu/P2iv0n+7Tt0HCeCxs9lAv9dR4YT15TuMy57DkXPXLirg8afCaSkBY1Ij0JkU0jHfZMrt5CZ2C3eqZ+WvxdwYPHOLlO3mBmsT1NVak7n2rT3iZ33zb6wrmAov0bG94dsHQ4AFk92G86nAsk1Ve3G63QC/URbDFJFDt4zP4z7jp+Tk+wv/HeF4sDfPdWDv6l1IRBTLU/iZPdK9MzlKrkyYQ1bCVogEMDRo0cBAPF4HCdPnsThw4dRV1eH2bMzm7URhSWddbt0BFd0XiZkWmuJFztDVWlVSVZFNttvxiMSTbO289fGgijYBmefJ1EFgB9wrQomX8S01q0gEld1VqNLSYjZtuU+/N1TPeBX9E6PRNAb5Kw6eeQ+3I4xJyS3YZ0FwLDsKc31LgxFVWG7Z1apaefPFNExGEEwaoxkGRmLUgWsr4fJnsNiX4MuB2wlaG+88QY+/elPJ//eunUrtm7diuuvvx4PPvhgAVtGZIpohp6LFEOi88oCL1jhy23LfbrZ96mAPnw9KJnFi9qbbeAA31bZBmdGKrHni5gOhlU0N7h137F48njmjnMqYNic7Q/BEDiywOeCx+kQuj8VJZG9hO8v/trSDfTIpG9v2udPCpcZ2YgQ7VMrPLYK27/88svh9/sN/5GY2RfR3p5cbB8QnVc2WGkLX2qLRjY3uKXHaTEUqHyqx7BPK92B0mr5FauYFTEVhcEPRfUuSQfEe8ve90exeYkXB9dMw6urG9HS6E5W9g7FEv3VvKMHsx47jVc7R4XXkG3fvN4bxvJnuoXh88zSFW2gF5GNCNE+tcJjKwuNKD1ElkUuXDei88pC9WXfIyuQqbXoRDkfRc09NRyT5kQUIWvrqUB652GYFTEV4fMkrMLk8ZMUTKty4XhALwyjcWDdiwM4ub4qeb7FO7uSblpGIKomj0tlyWgt3kmqB49P02dLEfXNof6o0FIzy9TCqHYC0yZlnxMyVXJlIv/YykIjygMrm1wzQTuDXlTvQhX39DOxYDN9lilk8WSxpbbh5X7T9nmcMFgrzLpLtUl823KfMOCCVXNe+nR6G3p562HTEq/w+1m7ekf1Lkq2ftfS6Dacm98MLusPdlyqtmgzlrw15DRYxLK+EU18RK99YBJ0G7T/5+opyWwwlD3f3pCgEUVHtq4bmVho3YmVTgdGuRgBJhaiAVQ0kL/bH8WyZ7rxRm/YkEkKSKwfsTpmDDbApnKrzq2pQHO98TsZorRYZmivffdVjbj7QED4/UxM2NphhYLkPWDn4CMkK7nSNKy/+D6pdCq6gBBmEfFt4TOW8KIk6xuWPFp730Xi2htSsHfVVBKxEoRcjkTRkSrAIVXQiJWgATM3pmgA3X1VI6b+4pTOnRgFdBnrAX0k5KYlXlz34oDufTbA8t9xqC9sSES8bbkvWS4mHDMGFJpdA+uj42crEfjDadRXJlyGm5Z4cfeBgGFNiZ2LFxOHA8mMHq27enEmFMOsagXHh1WE4wmR2v7ROkN/PbTMh3W/PYP3B+NQkXDrbf9onfDeGK6Du1BRkmZt30BNBKeoY5az9tzblvvQvENfSmc0plqKICXsB1lohO1IZd1YWYMzc2OK3usYjBhyc1QIfj0+T+LzZ0IxXPfigC7qT5sk2JBkOA6hlcbKxYii482ugfVRV9iBQFTF8UCiUsB1Lw4IkzL3jCQKj4b5rlL15zs6GMN7g3FcVO/Gmf8zEyfXz8DS6VXC7z8yJmYAcFG9G0unVwnvDX8dC3yulEma59ZUYN/qqXht9RQ0N7gxFFUNYnyoP4yrd/cZBjkmfMeHE1GZJ4fVguYuLaek4PmGBI2wHakES7YGt79zFLMeO43JPzuFt/rCuMDnxJxJDlQ7E641jyOxtiJycfI1xhwAZk8yCoo/hOTAz2fwmFLt0OUO5PXIyhqQxyHP1q/lxJA4EIJf73IpCaENRFUcHYwZhHOBzyVsR6pAHYMF2h8WugCZha11Mf9iRT2mVOuHpkN9YeGArxVavkmsEkEcifvFrrVRn03L8jWJyIUYFXtScDtBLkdiQsnXHjMtskwOWospqgLHhmJwKMq4UKmAx+kQtocf7OIAjg7pX6tyGJMR8+0Gxvsg1ftdI1EcH9Yv9J1/jgv7Vk8VrkWpKpJ92xk0nB5AwkWoFdrFk904E4rpkh17nMBMLupP1uey+2nIyhFD0gUoSq+WKiI1FB/PK7n06d6kW5cvz+NxADO9TsMewjgSk5bzap1QVaA7aNyTlknwUS4SFdOG7NxBgkZMKLkYANigyNZATo9EdKHs2gFSO/DzFlNCyMzLtTBEoeK8bE33JkSAD20HEhYCa2coFtenj3IAzQ3jFpdZqPn7g1FM/fkphOPj338UMbQ81YMKRTEturmozoWtH67FlgMBnaDcuNevu7bmerfhnsgmCdrK10cRw4aX+7F31dSE1dXWoxOVM6GY6fqoVhxZBpH+kTB6Ivoq3YGoisCYuPEBKs0N7mTFbb4PQ/FEeH9zvQstjW50jUbRH9SvoaVLLsSINmTnDhI0YkJJdwCQWQBs0Do+HDbNomFlH5IW2WCybbkPS5/uNRUMrUAcOBOG1rsXByvtEgZv/zVWKbp2m/VJUPJWKAaEzPJQAah0ObB0ehV2XzW+5sVSQnmcSAZXiAZ2QWFsAOLK18BYJCKXiUS2NsnuL59ppKXRjbYPBnHLEZ/0HtZXKlhYVZF8PtgWgNMjEXhdCkZjKjgvK94ZiGLxZDee+/jkrINAciFG6eTxJMwhQSsTcuHqywXpDgBmFh0/8DMLqGskijPBOCJxIMINZgoApwLE1YTIaBFWdh5jbk0FXl3dKEwErP0sE9tZj52Wih+/ysIXAU21ATxTRELJp4SSuVyl90FQ+ZphZaA2m3Cw9rLz8BULgEQhUe1kgLfMREEC2owv2SbjzoUYFSIpeKlCglYmFEtRwnQHADOLjh/4/SHosmGI+FCjW5jNwuOAsLKzlmT4/s9P6V5XYPwsn2mDP14rdXxKKZk1yH9OhMwqAcSTB6sWs+y482tdOkE8v9aFjsEINuzpTxb3PL/WJZ1AmVmjNWPuRFkGEo8TSYuMPU9do/pONyusnYu1qnTEqFgmlaUMRTmWCcWy8Mxv8JX9oFn02KmAPIKRj44T5RpkuDQbhPnzAIm1F8uDC/c1bicMn51RLT8XH+5/MhDHol91JqPkWFVqwzUgEYVp1qxXVzeiymnsBwWJ/uKj8rzcsWzPF48scvSxlfVoaXRjziQHvC4F/eEYLnu6B4f7owjFE67QwwNRaeSemYX+vj+KU6OK9NjmerdhU3Y/Xw1Ag4frUq/TuBE7n1A0Y/4hQSsT8pVOipHrvTTsx89cTB4nDKHqvDhOq5IP9pVOBWdCCcv02FAkKYZsIGbuSivt5muN8X8DCfGQ1Ry7gNtnFQeS+8TYICe6P4oD2LtqqrQGmQqg5akeoauT1TPTppV6vTcMZSyUnSHLQCLL3sLuwbRqV3JPF5+lHwC6RqPCZ2Tbcp9BaBijceBzb1Qmj9+8xJsy4bTPg+QxfP8v8Ll0n1cUTKjAFMukspQhQSsT8p0JPNezT/7HPnOSM6VFF4rFhUs6HgXJfVav94bxobYerH+5H8FoHN2j6W+uZVYJ68vHVtYbjmFrbqIf2J/8UUTv2EIAACAASURBVOn6mnbdiIfpmEhAGWZjpCit1FBUNWTi50PhRVsE+PuQanA+GYgbxJRVN+CrGmgZiSvJ47ccCOChZb7kxvUb9/oNFuaM6oTAtn2sAfNqnMl8ms31LvxiRb1uAjQUtRbhmivyPakkaA2tbMj3wnOuZ5+ZBI/wlZSb6xOJbz/9fL/u2HDcmLKKYaXdVvtybk0FHGMBKPz3y2DXObemAnO8DhwPjB/cOOaGfGxlPTa83I/3/FFd+L4luIMne5x4d0DfID5IRbb+ykcomhGHMa2WVrw3vNyPP41dj4wzoZihLSwEX1Q9OlWwy0SHyxc6mrEc1vBI0IickOvBQfTjN/tByiy61l29aQ34LAVUplWp+QGC38jM41SAKqeiy7XIghz49SDmUp1bU4G9q6YCgLBUixnagpyszZ9+/oxuMzi/FinLO8lHKHpdCoIx1ZBWK4lATPnr0Vbe5sP4mWWmZSiqCouDWplgMSF9byx4JRg15ozMJYWOZiyWwLB8QoJG5IRczz5FP35tSDb/g5QJqlVL0e0A3A5Ft2l36dO9eLxZQZPkM/wA0dLWk9wgzQbF7R+tw7oXBxCMqcKtAksmu/HQMl9SGK/9bb9uDSpVrS7+uhUAMyuBk4JMIR4H8IsV9bqMIjfu9aPO7cBxTct8bocucrCGW4sKxYGlT/cahM/nAfwhuYCLxJRHe9+PDUVw7a870RFyAioQisUNLkbZxMnKBGtuTQU8TkdynZYFr6QzyNvJ6imHNTwSNCInTMTs0+wHKRNUfmBzAJhW7UDnSFxnMCw4x4VATNWlgApEVWx63419i6y1h5Wf0Qrb0ulVOLm+Ch2DEVz3Uh/e849/ZoFvfCO2bC9WTAUOrpmme007iNa4FCyqS7Rdu7H7ZNB4PhbJyU8MFtXp3XbBaNzwvscJQ7YOcKJ5eljVCXalE5hfq2/b3JqKZPuv3t1nKgJzayrg1nzvof4oqp0w3QTOzs02VjPLVzbBynaQt5PVUw4ZSbIWtGg0ir/85S8YHh7G/Pnz4fV6c9EugjBg9oMUCaooC8YvVtTjxr1+nB7RD/hs0OU3NA9E5FsBeGuBwYRt/Uv9qHQ5hO4zAKitcGJuTYUhCENLOA786i9D+H+/H0IwpqLSqWBWtYL3Bselo6XRjX2rzTONLKh1JAd1/v1ATE1+vmMwgg8/1WN4v7nebRBdnwdYWOeWXp+qAvtWTzW0xUwEeIvnTFjfx1rrVbQuxrtBF1YlStnIglr4eyi7pzLsZPUUeg1vIrAsaG1tbdixYwcqKipw/fXX4+Mf/ziee+45fPOb30R3dzcAwO1245//+Z9x11135a3BRPmi/UF6nQpCMf16l2hwEwUGyMrJiDY0+yrk619KirFP+90imJDxQRhaVABf3jeYtHwCURXvDerbdKg/rOsHkTDXelzJ/jFLNPyRZ3oN2Th6RuKIxlU4oHeZsohCILGWF+DX8iT9wws4+5t9P+v/o4ih2iHvZCvVCUSBJFoB5e9hqnvKYyerp9BreBOBJUF79tlnsXHjRlRXV6O6uhq7du3CD37wA3zta1/DwoULcfXVVyMSiWDPnj24//77MXv2bHz+85/Pd9uJMkP7gzRbT2PIZs/8IKRNW8XSW7FZ7J1zziaP462HrhFzwUoFEzKzDP2AebYLYLxMCksO/IsV9fhQW48uYlCbQUOaaPjlfmF2kkBUTbbPAcChJIJdNi8Z98aIRFS2vYAXcPb3Tfv8RivWpeKiczxCl6xIPEQCY2ZF8aH7/N+pKAerx05YErQHH3wQF198MX7961/D6/Xim9/8Jr7xjW9g5cqV+OUvfwllbFoTjUbR2tqKRx99lASNyCtWi3iKZs+yEiaiBf5w1/i+NH6mn+0mThZUMa3KJczQz+AtI4ZLgSGi8N2BaGLtyaEgrNkvcGY0rgv0EFm0fFg9kAiW4cuwxNWEyK17cQCvrk5YfnzE4Pm1LuH+PHbdWgEPx1Xs7xzFoT5jH3SHFbhHo4Y+cEC8V090b/lqAlohzNbCKgerx05Y+k22t7dj3bp1yfWxjRs3IhwOY+3atUkxAwCXy4U1a9agvb09P60lygIrWUesbFJNld2CT7+VbiVsM/eUFc+Vr8KB/Z2jeEswkDO8LgXbltUKs44snmzckMySMfObpSNxC1kxBMbJB2rlA7w2qwgLve/+/Ex0b5iJfaunSqP9fG79sBOOA9f+tt/g6kw0ScHxQNxQpPO5j9dLA0n4e2uWVCDfCQeIicWShdbX14fGxvFZCPu39jXte8GgpLqgTbBTKG6pICsjInMnWnH1pDt7TmX18bN5WUkVr0vBlCrg6JC5+0pREkVHR018ilOqHVhzXg3WnFeT3KPF6sAdk1SlBhLrW9pEzQ4uszF/bR2DEaGguRUlUTtsJIqTw3GDpZhREITge0TpsngqHMDr10xJ+7do9hxkamHRGFGcWA4KUdJdLbUxdgrFLRWslBHRkitXj1m2C74q8+mRiM71FYd4M/GUasdYtJz5GttQVEVQlBZf0AZg/Jq1deBETPn5KY2FqKLaqWBOjVO3ZWCyx2m49pCgKWdCcQwOGYujitqnxWzAD6S4ZhmheGKdj9/LxguJtuJ3f0hfwDNXokNjRHFiWdA6Ojpw4MABAMDg4CCAhCuSD9P/61//msPmGXn44Yfxwx/+EN3d3ViwYAG2bt2Kyy67LKffYadQ3FLBrI/TWddINXPm3w9G47poRK9LwZRqR7JY5BdfHcX7wz1CdxiA5LF8IUsrz0zPSFxY5iVVsc1U59anj1IwEgP+4o8Z9mWtf6k/ZSRm14jRKgMSGU6WTJa76MwGfLN6bx5nYk+gqgL94RhODcehauT5PX80eS9kQsJPjlgB2PUv9Qu3EWQCjRHFiWVB27p1K7Zu3ap77Zvf/KbhOFVV82bNtbW14fbbb8e///u/42//9m/x8MMPY+3atfjDH/6A2bNn5+x77BSKO9Hky9UiijxkYpHOukaqmTP/Pn9r6z1KUpCue3EAgaj5vdcGHpgFIojgrZ5qJ/Crj9Vj6fRERWlZUuB090oBiaKikaiKhVXjlq0oCESLA/I8kR4HhPv+NrzcjyODUUOSZH4T/PqXxMfNnORMpsECgMt3HMdbQ5p7wF26ldB9RqrrTQcaI4oTS4L2wAMP5LsdlnjggQfwuc99LhlB+b3vfQ8vvfQSHn30UWzevDln30OhuHLy5WqRRR6mS6qZs2Gw40bs/pCK4ymKhPKh61r3JxOhrtFEVotIPPEdzrGMF2bOtovq3UkxA+R9zc8XtWm7UnGoPzyer9CC5092iOir+H1/WrQDvqoClS4HZk5yCvM1MhIVFPQWq6rq9/fxQtIxGJEnSpZcTCaTNNkYwZ/rzjny1GlE7rEkaJ/73Ofy3Y6UhMNhvPnmm/jKV76ie33FihV47bXXcvpdFIorJ1+uFlmfpzvYpJo58+/z+QVPj0Ska1NuRyLKbiQ2Hrp+5+uD2LtKLEJAIosHAOn6oJY/9obxaudoUtRkfc3vlZrldeKp1gZ8cGdPMsqRoUDVuexCMeDSHT2YWjkmthqqnfrgDLP9byInjOxZ8DgSeRiZkIqSGous8Zv2+fH+yPj98zgdKSebor1sjAU+8XCXySRN9rzy59oUlKdOI3KPbXI59vX1IRaLGSIrGxsb0dPTI/wM2z5g920ExdT+SaoH45W5gElqOGX7smn/Fw95ki6no4hh/QudeKRZnlrjzjkKNgXdGIgo8FWouHPOWbS3+6Xvb/nAKGZWjQ+ANxzUX5+WD1TG8NdRB7R+rz8NRJLXd3JUwZtnKnXvnxgMoi+sQBTI74CKuC58A1i7uw97LxsFIO9r0evhrg4s8Hp07rmLa2K4Z34Y1x6sRFjVFxTtNAQiq/BABRwKEgaOuVtzriemu6//O+DAXwc9ws+F4ok8jOzedQ5VQrtjqM4Vw/ZFwwCAcJcf7V2J1/njOoeCCHd14IHzx8+tPV70GRdUsGQjwVAIvzv8Z939ln1Pps8sf66BiKJ7Pja974Z/7Nm7Z37Y0JZipJjGn6Ymc3vXNoLG4NfnzNbsmpqa0N7enrITiplia//j08yLPRpdLmfx94v+xtK5RdbY8OE+QGNRBRQ3mprmSM/RBJjOiFO9X/VuNyDJAPL+iBP8djDFoSTvzy27ehFW9ZZYd8hhsHQ8jkSi4M1LvPgUX6tNHT+frK+3ekdx3VgG/0qngn9d2oim6VXC48NdHbhksjjTBnclGIilXptzO4BLuIoCAHDFY6ehpvBhsns3/UgvTmiSJ0+vqURTk3EN3OpxZp+pdDmSFtuRYSfuO36OwbLK5Husfr+vQtU9H2+NbbU4EYSwLcVGsY0/qbCNoDU0NMDpdBqssTNnzgj3wxH5IZU7NhuXi8j1M9GL72apj1TA4NLTpncSudwMYuYEXr96fC+V16Vf+4qqwLKnu/HYynppX999IJD8TCCq4prd/cns/vzx7V2J9Z5Ld/SkTKElQ1vCZtMSL+4+EDBkyk+1/QAATg3H0LqrF5uXeLHlQEDoNuQrCZxfHUPE5ba8ls27JLtGo7qsJLK6aLlaM+fPpU2dRpGR+cc2guZ2u3HJJZdgz549WL16dfL1PXv24DOf+UwBW0Zo4X+kZtnqU332TCiGp1obMhpsrKy9iY4xhpSr0LrRWLi6qD1m4eiM5no3TgSiWPp0L4IxFS5Brp7DA4n3X13dKFwv5HNIsuz+srWfuTUVmDFJwcnh9N1bHgfwPxoBluXQlBUy9boUROIqQvHE+t3rvWFsORDQBdGwiEeoif7VruOdP2l8G8SNe/0p11D5SUDrrl5dWjFZXbRcWUr8ubTubquTM9q0nTm2ETQAuOWWW/DlL38ZS5YswYc//GE8+uij6Orqwhe+8IVCN62sMducbJatnkf0g7cy2IgGACsL/aJj+Bn24b4QgppL8pgki2OfPdQXlu5bC8XiWPN8P9gqYFSifyytlOja+0U7oAEcPBNG665e4QDIZw6xSoVDSVpjm5Z4DfkWT48k0pTVuhWMRNWk/DdWAnNrElbj1bv7dFW1tRMXs8hIADgy7ACGrQds8JuqJ7lUS3XRJgKrliBt2s4cWwnaNddcg/7+fnzve99Dd3c3LrjgAjz55JOYM0e+plKKFNsMzixqTetySYXV8jD89YdicRzqTwyKbACw4t7hXzvUF04O3k+1NmBuTQV++fpfcOuRKl0tMtFgo20TCy9/ayBqWFVi7bQCax9/vR6HioDg+KhqtNROjiq4ZVcvTg6ntwerQkkUF9VW8L7uxQGDUPtD0AllS6PbMPjyE5WekfGIx9RuN72Fn+p40aZqQL//rlBYtQTJNZk5thI0APjSl76EL33pS4VuRkEpthkc/4ObUu3AwTXTEu6k3aMYbpfXLNNitTyMYXM0ZzWx2bkWK6VGQvHxMizs+5bUxXFy/YzkMYt3dunOwa59w8v6rBuL6lyYmaGbj29zuln+u0aiycz6nYFKjMbTt8z4tUIAhnUyj9OYOV80+G5a4sVnnu/X1XRj/Sty03JpJ3VoxVCEbPDPVhQ6BiPYsKcfR7hqAvmYSNKm7cyxnaARxTeDk/0Ab9rnHwsjH6/VJcvDp7VCvC4Ff+IsGe01Gq6XW6brD6m69RxW74xHaxGeGo7pslYwUegcqsT0I+NuPFFGk9ZdvQa32VsDUVxc5xJaRpVOIJjiljmQqGHWuqtXV8sMGNsDZqKTZ4Jxzebw3GXt4dfJKhQF3aPi/Jda7j4QkCY13rTEi7W7+zEaT7T0fJ8TbkXR9ac2f6bMFcuen1PD4o7Vtmt/ZyJKdDSmQlUT7tGpVS4oSiIoSDT5ummfH4c1z+ThgWjeJpKU2CFzSNBsSLHN4GQ/QF54zPLwmSUnBsxrWJ1f60KlS745ekq1w7TUCKC3CAFtxhAHTgTH3Xj8tQajcWG7VSSEp6XRjdMjEfhDSK7jsCi/g2fChowbHkdi3SoQVXE8EMfxQNhQOqZKEoABABWwlrk+XaqdwMxqBR3DajJ4Q9sGthXBau5Jdj/vPhBIVhtQAdRW6FOJTVLDOKtW4Hggbno+/vlh2VO0iYkZiZRm423vDgLdwfEHRuT1kLms8+H+p8QOmUOCZkOKbQYn+wEa3EkmefjMrEyPU1/MMVWarNZdvbp1HSuCz5+TF0XWPv5aFz3ZKT3nOwNRLJ7sxn9/whituPuqKoOIel0KXl3diKt39yGgCaIIRVU017uS1oM27J1PHeVyGDOAAAkBqnImBvj+oJpS9KqdQNM549+pXacEYMiBCQXSwVxk1comPWdCMagqEIzFcWIwhujY9nMtFVANxUr580yrcmBatUv4XFnZYpCqdBB7rdjc/+UOCZoNKcYZnGimum25D+tf6ERAcQsz25tZXVqa6926gTLV9Wci+KJwbyuiKIs4BMRBGnw71+0+g/cGEwN2IKqiZWcPPlCjXyWLAPjLYEwXxr/7qkR6rGNDEV2l6FGJUC2Z7MZDy3xjEYB6i9LDVaUGEgEhWvfb1bv79Adwlx2KAetf6tdZymzP2umRiCHSkF2HyNugd+8ZXaZHBuMAzPcranNy8kIj22Kghb/foorcon4ptPu/3CFBI3KCbKb6SHMomdmDFagUCY1WhGpcClQ1UTcrEws0F0Uba1wKFtW5MDAaxvSaSmkbfB5Icz8yZIPc3JoKnBzRD6whFTg+HIdnLJkxIxBV0dLWk3TrMUGYW1MBj9Mh3SYAqGiur0j2r8g9GheM7XyAjCgHptaFDOiTBrOoSK1wiCINRZMPg3imQLRfUWZhA8D2j9Zh3dgaGm+suZREJXD+frOK3DzF5v4vd0jQCB2ZrglYCVTJR+VgnnTbL6uUDSTWv9o+GNSlQeLPX+92GgI/+OwfokGOnUdkKYTjiUGVFx+2gZoPruGDRrRUKEgOxKJ70lzvQvvZKCImhoVsg7tMIBm8a4/tWePvTaow/1SI9iuaWdhLp1fh5Pqq5HHaa1g82bjtwIxic/+XOyRohI5M1wSKZabKt3/p0726gp13cymX0q2UzZ+/ud6FRXWuZKaLBT4X7mupTa5xyfbTmX1vpTOxxrT06V6h4PHBNXzQiJYPVI2bUCKh8DgdmFzl0AVduB36IqFMMJjLkmXtMAtuYdehbb92zxq7N1o3qrYyeLUTCMeA6NhWbVFgpzYQhZ9omKXX0pKtIPFC2jGoF20qHzOxkKAROjLdEjCRM1UzK4xvL78xmA2wsg3YWkSizB8/FFVxcM00w3FsjUu2n87se2sqVKx/uR8zqxUcHVKNe8I4/fJ5Em5DPtDD61LwtQ9Ekn9vW+5DS5u++vaZUAzTqly69FAuBVhQ5zK4fHkxZymseCvH40yse/KiwudV5EPwRaV3RoOjeGvImRQzvtSMLCUXaxt7Vj71m170B1VE1UT0qXYfWS7Xo6l8TGEhQSN0ZGppTWSgipkVaeau4q0dNtCaVcoOdyVy8cn2OaXKx3fwjN4KY6He0iKUADpHgU6JG9HrUjCvxqlbr5Jt3g5EVfzkeAWua0n8PbemAs0Nelcmu86/e6onKYgjscSgzwu1bLKjy/DiUgA18d6WAwGD6GiFkz+n6PwRLhco27TPI2ubzBLO1z6ybHKZEtmTKukAUWZsWuKF16XApSQGz81LvHn5HuaaWbyzC627enFsKJL6Q2OYWZHblvvQ0ug2hpULYIN5S6Mb82qdaGl049XVjWj7WAMA4OrdffjiIQ+ODUWSAyP7Ko8jYUFsWuIVXgc7nnfFsSg+K9WlRUTiKrZ+uBYtjW5LW6Z7QoqufZuXeHXXywSHD4443B81XBMv3uxvNpk5uGYaKp0OHB6I4uhgLBnhydi23Gdwj/KRrvx7fC5Q2QRC1jYzSzgfEYl8O9LJZZou2fyGShUSNEIHK00SHcvjt+WAKGtg9rABXzTwpYIfFGs0f7PBdeYkc0XzOMb3TT20zKfL6L7h5f5k294acgpdkzO9Tuy+qhF3HwjormP9S/1Y9ky30Cpg+6/4c3mcwLxap+laGCMUB7YcCOChZb4U1ccSnI0quvZdsztRf+2p1gbsvkqzP477ahUw3Bte/EVibjbZUFVgXo0THufY+le9K7n+xTKieF0KZk1SkmJ7z/ywQYBF8G1jx5l5GPKxzqttx6J6F0Ix5E1wsvkNlSrkciR0TFRaray+hxvJVcHIzrsS+aCC5obxvW2G3JDcOCdyTcosgCODUcguhWUs4c/VXJ+IrNNua2BbF/rDMYNL8fRIwmKU4QAwY5KCGdUVODEYxGhoXK1kpWbOr3VJs96fHkkMxHxgiGhN0sxlzWfW9zgT/cGvwS2sG480DFepltyCMpc3c4eeHokY1tDysc7LZ585PDKe+u3GvX5d/2WbWaTYUuAVAyRohI5M1tDSCZVPdy1KRIDzj/F/A8ZSLuwIUYomw0AgcBPKgl4Ma3YmZhO7Rtm5ZIPyrMdOG6IF3U754HVurTO5znT5juPoDBmP0V5zx2AEkqLvye9jpIoKNatfJxuA8zkwa0XY7bQuIrlIaSW6rlxmFimWyOJiggSN0JFJtGI6P1J+QDTLASjDyg+ZicPinV26WlzMVWh2vgU+V3Kf1yQ1LN0vBRj7i08RJbrGdANo+Iz29ZWKafCLtj/+aU4E3zjiMqzZ8ZaTWVmbcFzF/s5R3D0Woi+D3w/WMajfSF8jWT/L98CciYhkIzxmk7ZcijftgTNCgkboyCRaMZ0fqWwtKh3S+SFbGSzNckO2t7enVSGZT0WlDQ/vGIxg2dPdeO9sFJE4UOEAFpyTugwJH1bfNRJHt2bTsEcB5p3jRCgOQ3/85HhFyiTCqQbVcNyY0JfBR4Vq4UVhUZ0LLY3Gat/5HpitPp9aq4wXo3SEx2zSduNef87EuxhT4BUaEjQia9KZYediNs7WzKIxFe8ORPCp3/QmM6rzwmBlsDSzKtLdGCtLkQQY15DCcWvh47z7NMxF/IdUoKbCif/hNvjetM+Pd4f0cV9WLFQRvJhpU0RZrU0WiKnYt9p4nfkemK0+c2buVO1nUrkjzSZtZFXlFxI0ImvS+ZHm4gctqkp8clicBDjdwTJfG2M7BiM41G89I4kWmfvU7Bzj16F3850KxLDsmW5Akytz8xIvrvltvzSYRYSVFFEyIZnoiuvawBB/aLzOXCoh8jgSYsQ/p6nckWYCSlZVfiFBI3RkMtiYpf+ZpHrw+LTxCsO5+EHLBED0errXk87GWKvn7hiM4CPP9EoFw8xK1aaDOm1S/Zo/h6yPQnHoClWyrBrN9cbckTwKEmVoKp0KbrqgUpiXUYts8sILQstTPWiuN7f2shFB9syx/I6BgIrjgbAuLdq25T5j9GmDWLRTuTD5em5khU0cJGiEDrNciFYHEb0F5cx5RgaZi0zkFjrUP74Z2sriPn9us42xVgMHZBup3WNraGYDnswN5gDgBOBwikPQ+evwcNn7tWijE7X9xaMCyf2JN+0bTFYpk127bPLCC0AoZl5mh00I+C0CsqrVVl2B2rRoN+71W/YepHJhaq871RoskVtI0AgdqX70VoQp3/tj2MDTNRpFf1AVViWWCYFZWzoGIwjF4vA4kAzouHveqPA4WVor0bGH+oztaGl0J3MN8mmjAjE1+e93/eLoQ21oPr/ut225D5uWeHHdiwMYjcZR5XJgZrUyVkfMiDY6ke2FkyUcZvBnSuceyzaQi85xclTB+meMSZqtJI5O5Qrkz2fVe0DrYMULCRqhI9WPPpNz5DoM28rAI2urWVv48PVKlwMzq4yjukwsRee+aZ/fUKtMW7HZLBDBjJ6ROI4NRaCqEFovAAvkSGS8r3Q50dLoMggVy5jC0Lrn0mlXOvsV35OItOgcm953C61bK4mjZa5A5r7V3pZ0nlFaByteKPUVoUObuscs757Vc1xcEyvIDJZvK8u9aNYWK5alyOJyKfJzi9Jc/fKjdbhxrx+Ld3YJrTcrsEz1InfmmVAsmd2D0ReKJQJLJrv1J1KAG/f6cWwoossNGIrJkyfzVDmQLJFjluKJiTcfpcn6T5RKyy9Yw9ROCLTI8jkymBDNqK7QiZnsfIT9IAuN0KGdfZpVmLZ6jkKtIZjtLZNhxbIUWVxmEX+iNFcs/2O2mFmh7w7oG8myffBbALTrVwB07ap2GkvSMLQRgNrN5GauaV5kGaz/RKV2fBUqTgTHj/W6FF0NNS1WXYF8v7GUZIT9IUEjpBSra8VKxFs6bddGEnpdCuorFUyrcunKxzBEFhcbOEXtEg2yV+/uM5wDKnRC6YBxnYpnsseJIGdJVY+159PPn9FlFwnH1aSLEoAhu75IHM9xAwiLRU0bAbh4Z1fKcwH6FFpAImryQxrLVmQh3z8/jPuOn2NpYmL1nlPKqNKFBI2wHbnMh8efDwAWVmksTP1YLbS4ZEmOWbtSbWSOxIBty2rx0z8FkwN312hUV0Wa4XYAszR7o9a/1K97/29qXZhbU2HILhKOQ2iFadvE2s0YiigY0SifLCuIVYHgU3jN9jrw0LJxwedrxE32ODHTYnLidCiWoI6J3o9XDthG0H72s59hx44dOHz4MAYHB3Ho0CHMnTu30M0iCkCuoyjTOZ/ZYMh/rmskKtyrtW25D5fu6ElaYHEA//f3Q9i/qjE5wJ0ZFdtnF/hcukwkfGJmfziO1l29OD0SMVQYkF0Xq3s3y+vSpe0Kx/XnlhXX5At8BqOJ9TR+kOZFdlqVyzCZYKLJznPN/1Zi+hHjJuhsKBbPQ64nZoSNBG1kZAQrVqzAJz/5Sdx5552Fbg5RQFJZBLKZL3u9aySK/tB4uL8saa4Is8GQD6I5E4zj+PD4gPW3bT2YW+vEXwdjBndiMKZiw55+3aZnEXypHL4v+kNq8jt5RFYYkAgwufP1QXicDrx3NmpYI+Q/z8OXTJEN0lbcr0w0x8/jwIng+B61UrJqIqZRAQAAHAFJREFUqPxL7rGNoP3TP/0TAOCNN94ocEvsj90HhVQuI9nMV5YyS5Y01wravuziEtrya0+jceA9v3jQqnQqOCIJZ9fyrl+ftonvi9MjEQQ0p3ErKmbVuHTXJdpn9p5fLGQeJzBzkjH9k+j6matUy8EzYV17U7lfmWjKBvuJtGry/TuhtbzcYxtBI3KH3V0dqVxGVutuMQIxFb9YMV54kWWNSD8rSmYoAGZVKzgaMNnJPEZUTayBadNFafuCpXdinO+N4xXOTbj7qkYse7pblyhZZpWx4qMy+GepitsIxNore8as1plLJXT5IN+/k2JZyyslFL/fb6WSe9Hwxhtv4IorrrC0htbe3j5BrbIX1/xvJU4Ex0ee2ZVxtH0waPKJiePkqIJN77vhjyjwVai4Z35YuLnZjC8e8uCtofHZ7sU1MTzaHDK8rn0fgO69RTUxPNIsqIzJwfdlNnigIsQlE65QVFQoCcGJwbgny62oON8bT/bTqbH+G5D0H+vf9wIORFSTqp5QUeUAfnBBCEvqxGp3clTBuoOVCGvOU6GowvOm+4zJrkN2b/PBRPxOcvG8lxNNTea1Lwpqod177734/ve/b3rMc889h8svvzyj8zc1NaG9vT1lJxQz+Wj/9CO9OBEcn8VPr6lEU9PsnH4HI93237KrF28NJdp2Igjcd/yctGfFj08z7p+bW1ORfL1rNIrekThiSFhHjgoP+kIxaEMoAoobTU1zUraf70sr4fYypnqd6B6J66yl2TUuHFwzzWBRMcKqgreGnMl+agKS1QE6BiNYv7sTw4o72Q9b9/qT/WuOgtE48H/fq5QmDr5lVy/Cqv5cDkURVu3WPmOp1jjZ649d6UO4q0PX/7J7mylmbkWrvxOzc6R6fnLxvOcTu42fBRW0m2++Gddee63pMbNmzZqg1pQPxezqyIVLSeaSlAUvHOqPZpQVpWMwgmA0ntxHtsDnQl8ohpMmWfHNmFblwrQqfVg9a4diZkxBntswYc2M5+JM1Z8VChDRNN8scbCo3MoCn8tQ/ZrPxGFljZO9/sD5+vblOkLRzK1o9XeSjWuSAkNyS0EFraGhAQ0NDYVsQllSLGHLIrJdKLe6kM8PHPWVCs5zO5Mh68FoXJrCicEX7PQ4HZhR7dCtYVmBryItGkSHzDIFYzy3o1l2+YNnwqjghNEFoNKlJCM+3+4PIyIYU0UDrajcyrblPrQ81aPL2M9n4rC6xjkRg7vZd1r9nWTTbgoMyS22yeXY3d2Nw4cP489//jMA4MiRIzh8+DAGBgYK3LLyQZvrzyxnXzZo80Cmyr0ogs2Wjw7GdCmdePiBoz+YEAyWDopVkjZDNJBp239+rQOVY1+jAJhXo2BRnQt8svmpY5EUn/7NGSx9OrGHjBdjvr3VzsR/DJbb0ewao2oi0lLLhfUu7F+VyG94JhSTZtgXDbT8vdq0xJtog2BrgZW/+ddPDcfwxUMeS89Zps9mqrbl+xzZPu+EHtsEhWzduhXf/e53Da8/8MADuOGGG6Sfs5sPmKeY2s9nYGclUMyQtT9fIdEXPXla5/KbNUnB29fOMBx3bCiCpU/ry5J4HPpov3m1TmxfNCTt/1T9IXuff93rUoQZ5bXnE+XVvHp3n66C9TxNSRn2mfUvdOLdgFMqVPNqEyH5ZpGaHgews7Uedx8ImN4vUYZ+r0vB9o/WYen0Kl27ROtg7HWWZ1LUDzKsPJuiZw4Yt4i15XvSeSZl1wMU1+83E+zWftuE7d9xxx244447Ct2MsiaXLqF8hUTz+QL5vxlzayowpdqBgEYQ+CDCVDPtVGssIpdf665ebF7ixRaNOPB7x0Sfn1tTgYeW6bcWpNoQPremAo80h3DLEZ9UsCZ7nKnX1RwK7nxtMOleld0v0XnGN23rxdBsjXPxzi6dUPPnFQmTlWczVWoys03hZhSzC7/csI2gEYUnl/7+fK2X8PkC6yvl0RT89Zxf60Kly6EbKPnkxFpSDWT8+dmerC0HAqZ7xxhep77t/IAs2xCuHfAnqR7869JxAfU6FURUNSEYY2uFvDDyBKIqjgzqFdfKmhpDu2k7k6rh/HMmEiYrz2aqZ44CNOwPCRphmVxGR+ZrMVyUL1CGlRIzfHLidGBVo1NVW2bteLNPXyuMj2zsGtGLij8Sx+HVU8Gj3+ztTAooE7ojGpfe4YFoUhh5V5+OFOti2us41B/WBYXwlm8qodDel0lqOKXleyYUw1OtDSmfzVTPXK6eSX5C8fi0SE4zjNiRicpORIJWBuTqYcqlayVfWwfSOW++XUV3HwgI18a8LsWQtFjkamORjez+nRjWqw0LZOGxkjZKSyCmYt/qRt1aUM9IXNf2BT4XPE6Hab+y/uTXlILRuC4aNJVQpKqnJxIeK/cy1bORq2eSn1DYLRNPPpio7EQkaGVAoVJddQxG8MVDHgwfNmZez5eYFNN6Bi8sLiVRzDIYjQvvh8xCkAmRzyP+Xqtpo/j3UxV3tToJ4u9BpoViZWQqPKmejVw9O+S6NDJRfUKCVgYU6gfGb+xd+nSvrp5WKbphtNYwX9+LVWaWFcSUDdSy+zWjWtx/MpcdL3QeJ5JZQHhyOTHI9SSjmCYtIqy4Lu2eIDxdJmq/HQlaGVCozZv8QByIqggMxibUSpxoeGvKAWCW15GsgA0Y74fXqXdBPtXaoBvcRMEWCiC1TGQuOytrhvmkXAbxVGuAgP0ThKfLRGUnIkErAwqV6koW9QbY1w2TalDmryuORGCKdrDi70copndBbni5X7detXmJF596Xl+ZusKBtMWgkJZNx2AEH3lmfN9fPgbxYhHMVGuAQPm5JSfq2SNBKwMKNZBtW+7D+hc6EVDchiADu6b4STWzFok4P1jx94N3QfJh7lsOBFDt1NdXSxFpX3TctM+fMtpTCxOnziHrFavtZPVQyqv8YJvUV4T9YBt7D66ZhldXN5ZEip9UM+tty31pJzo2vC8Ic+f305ntrytGZPvWZCmrmDidCDpMU5iZfUcxWz1WU15NRLq5UoIsNCIviGbYxTpb1sK7re6co0Cb+CfVzHpuTQVeXd2YlouXd0GKwtyDMQUnh8dfa7DZjN6wbjiWgf/GvWKrKhNxspPVY9VrYiersxggQSPywvgP0YETQXnF4mKDH0A2Bd3J+mKAtfXIdF28VsLc17+kX0NT08jAmu7aUsdgBBv29OPIWOWB82tdeGxlfVbrUbKAFJlwZSJOxVwWKVPsZHUWAyRoRF6w6w+Rb+dARO/ay3Q9UisqXqcCRUlsnBYJjOg7AjHV9G8z0p3l37TPj8Oammas8kA2ExJZv8mEi4lT51AQ02sqLYlTrteKiyHIxE5WZzFAgkbkBbv+EPl2+ypyU4xCtjnaqhspm/5Md3Ihej9fExKZVcXEKZHtPT/V1FNRDO6+UrQ68wkJGpEXMplhp2IiZsz8AHLnnLM5Oa+ZIFgRi2wGNl4MRcVAzY5nr1nF6n0qBgvIjGLwMhT7JvJigwSNkJLNgJOPGfZEzJj5AaS9PXV0HcOsv8z25IlyO/L9nM3Atm25T1f7jRUDlZ1v23IfNrzcjz/5o4jEE4NEKGYuglr4+7T06V68urrR8NlisIDMsKuXoZyhsH1CitXqzxNFMcyYzTDrL22Y9qI6F5rrXcmQbYyVlclXP7Pab1rM+m5uTQX2rpqKSxrcUAFEABzqT13BW3buQFRFS1uPIey82O8nVZO2H2ShEVKKbcAp9hmzWX+ZWViy3I6ZIipfwvddx2AMi37VmUzJlctsFiJrNBRHUqxZPxT7/SR3n/0gC42QIqoXxTORGz+LfcZspb9y+TkZWkvxraFE+RJ+w3ccwPFA3NQizLRdos3lDK0oFvv9JOwHWWiEFCuBCBO5DpKLkPl8Bh9kGrhh5XPpXIPIsmJux8Cg9QjGbMq0sM3lfLFPrSims5eOIKxAgkZIsSIgxeaWFCES3YeW+QwCoaowvJYOmQqulc+lM3GQufJkgSm85cWLJ5/93+xYJrSyYp/aPi3GoJBij7wkzCFBI7Ki2NdBALHoigZTAIbXHjg/8+/N5eCYzsRBVr6EvX56JAJ/KJEPUlvWhpGO0KQ61kys+Ws4eCaM1l3WEhHni2IUWcI6JGhEVthh46dIdK0IRLbWZi4Hx3QmDjJXnlULMh3xzMZC568pqhoDR6ySq8mDHTwOhBwSNCIr8hEJlmu3Dy+6m5Z4cd2LA7pjmECYiUa67crl4JjOxEGflcSpEwgr15COeGZjobNrOngmDG1lGW0/nRxVcEuKPXr8NWczebCDx4GQQ4JGFB25dvvwotu6q1dXm4tlfgdgEI1w13gEYLrtynZwzFTYzYTUyjWkI57ZWOjsvrTu6tWlBdP206b33XhrKHWf52ryYAePAyHHFoI2MDCA++67D7/73e9w4sQJNDQ04Morr8Rdd92F+vr6QjePyDH5dvvw55tS7UgKhdaSSaTuGi9/k267sh0cMxV2MyG1cg3pWN25sNDN+snPJYeW9XmuLCvae2ZvbCFonZ2d6OzsxJYtW7BgwQKcPn0at956KzZu3Iinnnqq0M0jcky+3T5Wzs+Xv2lp60GFw1i408yKynZwzFTYZUEhrM3F5lIz6ydfhYoTwfG/Ze0ly4oAbCJoCxcuxOOPP578e968ebj77ruxbt06DA4Oora2toCtI3JNvgcnK+fnxSMUB0JxFV6XginVjuTnZAUqcwEvPn8djGH5M934xQrz2mRagWhvb9cda7eB/575Ydx3/JyU7SXLigBsImgihoaG4PF4UF1dXeimEDkm34OTlfPL9mxNqXbg4Jppyb9z6R7lrb3NS7xY9+JAcr1PxXhOxUz7x24D/8wqtWARj4T9sGXqK7/fj+985zvYsGEDXC7banLZMJHpsXIFS8vkVvQx8KnSQWXjwuOTG285EDAkFQYolJwhe66sJtW243NJmKP4/f6CJaC599578f3vf9/0mOeeew6XX3558u/h4WF89rOfhcPhwM6dO1FZWSn9bHt7e87aSmTOFw958NbQ+EC/qCaGR5pDBWyRdU6NKtj0vhsDEQW+ChX3zA9jZpVq+f10uOZ/K3EiOC5gsyvj8FWour4DgItrYnjUJv2XT2TPlagf2z4YtPx5onhpamoyfb+g5s3NN9+Ma6+91vSYWbNmJf8dCASwdu1aAMD27dtNxQxIXHyiHpd5JxQzpdD+YcUNaNx3AcWNpqY5lj6fS/dRRudqb8e+z8rb2gRg36KMmmNg+pFenAiOh6+zwqjrX+rHkcEooAILfC78YsUUy31QCs+PrP3Dh7sgeq5E/SiqySf7fC4p5f4vRgoqaA0NDWhoaLB07NDQENauXQtVVbFjxw54vd48t47IFdlE1uVyT1qxpzUSBWzMranAvtVTC920jMnnepbsubIa+FKMEZ9EdthiAWpoaAjXXHMNhoaG8MQTT2BkZAQjIyMAgLq6Orjd7gK3kDAjm8i6XAZdyM5VLEEEdgvYsEI+JxGy58pqP2b6XBbL80IYsYWgvfnmm/jjH/8IAFiyZInuPX6NjSg+shmoczmLlp2r2C03O5PPTfLZTgAy/Tw9L8WLLQTt8ssvh9+f27L0hD3I5b4p2bmKISFtqc76S9GtVwzPCyHGFoJGlC+5dMPJzlUMgy4/61/6dC9eXd1oe1HL90buQkwEiuF5IcSQoBFlTzFkz+Bn+YGoWhKurHyvCxbC/VcMzwshhgSNKHuKIRhDlJkkl66sUnVpFsL9VwzPCyHGlplCCKLU2LbcB6/LmPyYkW1WC6vZM+xGLjO1EPaHBI0g8kC6AjS3pgKvrm5ES6Mb82qdaGl061xZ2QpSqQYysBRloj4jyg9yORJEHshkbcfMlZWtIJVqIAO5/wgtJGgEoYFfa7pzjoJMEv/k2iLKVpAokIEoB0jQCEIDb1ltCrozytWYa4soW0EiS4YoB0jQCEIDb0kNRBTJkebk2iKaaEEq1ahIorQhQSMIDbxl5avIrBSM3S0iSu9E2BGKciQIDXzU3D3zw6k/VIKUalQkUdqQhUYQGnjLqr29NPZrpUuqNUBySRLFCFloBEEYSLW/q1Q3ahP2hiw0giAMpFoDJJckUYyQhUYQRNpQyimiGCFBIwgibSjlFFGMkMuRIIi0sfu2BKI0IUEjiBLm5KiCW3b1UjRiBlAkp/0glyNBlDCb3ndTNGKGUCSn/SBBI4gSxs+l7qJoROtQJKf9IEEjiBKGT91F0YjWoUhO+0GCRhAlzD3zwxSNmCEUyWk/KCiEIEqYmVUqRSNmCEVy2g+y0AiCIIiSgASNIAiCKAlsI2hf/epXcckll2DatGk477zzcP311+PIkSOFbhZBEARRJNhG0C699FL85Cc/wWuvvYadO3dCVVWsXr0akUik0E0jCIIgigDbBIV84QtfSP577ty5uOuuu/CRj3wEHR0daGpqKmDLCIIgiGLANhaaluHhYTzxxBOYNWsW5syZU+jmEARBEEWA4vf71dSHFQcPP/wwNm/ejOHhYTQ1NWH79u2YN29eoZtFEARBFAEFFbR7770X3//+902Pee6553D55ZcDAM6ePYszZ86gq6sLP/rRj3Dq1Cm88MILqK6unojmEgRBEEVMQQWtr68PfX19psfMmjVLKFjhcBjnnnsu7r//flx33XX5aiJBEARhEwoaFNLQ0ICGhoaMPquqKlRVRTgcznGrCIIgCDtiiyjHo0eP4tlnn8Xf//3fo6GhAadPn8YPfvADuN1uXHnllYVuHkEQBFEE2ELQ3G439u/fjx//+Mc4e/YspkyZgssuuwy//e1vMXXq1EI3jyAIgigCbBG2P2vWLOzYsQN//vOf0dvbi3feeQfbtm3D/Pnz0z6XqqpYs2YNfD4fnnnmmTy0Nj/YOVPKwMAAvvGNb+BDH/oQpk2bhgsvvBBf+9rX0N/fX+imWeZnP/sZrrrqKsyZMwc+nw/Hjh0rdJNMefjhh7Fo0SJMnToVy5cvx+9///tCN8kyr776Kq677jpccMEF8Pl8eOKJJwrdpLS4//77ccUVV2D27Nk477zzsG7dOrz77ruFbpZltm3bhssuuwyzZ8/G7Nmz8bGPfQwvvPBCoZtlCVsIWi758Y9/DKfTfnWN7JwppbOzE52dndiyZQt+//vf46c//Sl+//vfY+PGjYVummVGRkawYsUK3H777YVuSkra2tpw++234+tf/zr27duHlpYWrF27FidOnCh00ywxPDyMhQsX4l//9V9RVVVV6Oakzf79+7Fx40a88MILePbZZ+FyubB69WoMDAwUummWmDFjBrZs2YK9e/diz549WLZsGW644Qa8/fbbhW5aSmy1Dy1b3njjDfzDP/wDfve736GpqQk///nPsWrVqkI3KyPefvttfOQjH8Ef//hHW2ZK2b17N9atW4djx46htra20M2xzBtvvIErrrgChw4dwty5cwvdHCErV67EhRdeiB/+8IfJ1xYvXoxVq1Zh8+bNBWxZ+sycORP/9m//hhtuuKHQTcmYQCCAOXPm4IknnsAnPvGJQjcnI84991xs3rxZl7GpGCkbC21oaAgbN27ED37wAzQ22rvGUSlkShkaGoLH46E9hDkmHA7jzTffxIoVK3Svr1ixAq+99lqBWlXeBAIBxONx+Hz2KxAai8Wwc+dODA8Po6WlpdDNSYktgkJywde+9jWsXLkSra2thW5KxvCZUp599ll4PJ5CNytt/H4/vvOd72DDhg1wucrmEZwQ+vr6EIvFDJO2xsZG9PT0FKhV5c3tt9+Oiy++2BaCwHjnnXfQ2tqKYDCISZMm4fHHH8eFF15Y6GalxNYW2r333gufz2f63yuvvIJf/vKXePvtt3HPPfcUusk6rLafsXbtWuzbtw///d//jfPOOw+f//znMTIyYpv2Awnr8vrrr8f06dNx9913F6jlCTJpv11QFEX3t6qqhteI/HPnnXfiD3/4Ax577DFbrd03NTXhlVdewYsvvoiNGzfi5ptvtkVgi63X0KxmGvn617+OX/7yl3A4xvU7FovB4XCgpaUFzz//fL6bKsTumVLSbX8gEMDatWsBAL/61a/g9Xrz3kYzMun/Yl9DC4fDmD59Oh555BGsXr06+fqtt96Kd999F7/+9a8L2Lr0sfMa2h133IG2tjY899xzGUVkFxOrVq3C7Nmz8eMf/7jQTTHF1v4eq5lGvvWtb+ErX/mK7rXLLrsM99xzDz71qU/lq3kpsXumlHTaPzQ0hLVr10JVVezYsaPgYgZk1//FitvtxiWXXII9e/boBG3Pnj34zGc+U8CWlRe33XYb2trasGvXLtuLGQDE43FbZGWytaBZZcaMGZgxY4bh9VmzZuHcc8+d+Aalid0zpQwNDeGaa67B0NAQnnjiCYyMjCRdpXV1dXC73QVuYWq6u7vR3d2NP//5zwCAI0eO4OzZs5g9ezbq6uoK3Do9t9xyC7785S9jyZIl+PCHP4xHH30UXV1dRR+hxggEAjh69CiAxEB68uRJHD58GHV1dZg9e3aBW5eaW2+9Fdu3b8fjjz8On8+H7u5uAMCkSZOKYiKXim9/+9tobW3FzJkzEQgEsGPHDuzfvx9PPvlkoZuWElu7HLPB5/PZJmz/5MmT+Jd/+Re8+eabukwp3/jGN2wx+3vllVfw6U9/WvietppCMbN161Z897vfNbz+wAMPFKU77OGHH8Z//Md/oLu7GxdccAHuu+8+LF26tNDNsoTsebn++uvx4IMPFqBF6SGLZrzttttwxx13THBr0ufmm2/GK6+8gp6eHtTW1uLCCy/EV7/6VaxcubLQTUtJ2QoaQRAEUVrYOsqRIAiCIBgkaARBEERJQIJGEARBlAQkaARBEERJQIJGEARBlAQkaARBEERJQIJGEARBlAQkaARhY/7rv/4LPp8Pl156aaGbQhAFhwSNIGzMk08+iTlz5uCvf/0rXn/99UI3hyAKCgkaQdiUrq4u7Nu3D3fddRdmz55ti1x7BJFPSNAIwqb86le/QmVlJT75yU9izZo1aGtrQyQSKXSzCKJgkKARhE3Zvn07rrzySni9Xnz2s59Ff38/XnzxxUI3iyAKBgkaQdiQP/3pT3j77bdxzTXXAAAuuugiXHDBBeR2JMoaEjSCsCHbt29HbW0tWltbk6+tWbMGv/nNbzA4OFjAlhFE4SBBIwibwap+L126FF1dXTh27BiOHTuGD33oQwgGg3j22WcL3USCKAhUD40gbMa+ffvwmc98Rvr+smXLSNSIssRV6AYQBJEeTz75JOrq6vCjH/3I8N7evXvxyCOP4PTp05gxY0YBWkcQhYMsNIKwEcFgEPPnz8fHP/5xPPTQQ4b3Ozo6cMkll+Duu+/GV7/61QK0kCAKB62hEYSNYEEfn/zkJ4Xvn3vuubjggguwffv2CW4ZQRQeEjSCsBHbt2+H2+3GypUrpcd8/OMfxzvvvIO33357AltGEIWHXI4EQRBESUAWGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJQEJGkEQBFESkKARBEEQJcH/ByEEh5W5+CIbAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Weitere Configs wie BubbleSize &amp; Colour</span>
<span class="n">df1</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="n">y</span><span class="o">=</span><span class="s1">&#39;B&#39;</span><span class="p">,</span><span class="n">c</span><span class="o">=</span><span class="s1">&#39;red&#39;</span><span class="p">,</span><span class="n">s</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x23b1465b160&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Farben nach dritter Dimension</span>
<span class="n">df1</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="n">y</span><span class="o">=</span><span class="s1">&#39;B&#39;</span><span class="p">,</span><span class="n">c</span><span class="o">=</span><span class="s1">&#39;C&#39;</span><span class="p">,</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;coolwarm&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Größen &lt;= hier wird die Variable C auf die Größe der Punkte gesetzt</span>
<span class="n">df1</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="n">y</span><span class="o">=</span><span class="s1">&#39;B&#39;</span><span class="p">,</span><span class="n">s</span><span class="o">=</span><span class="n">df1</span><span class="p">[</span><span class="s1">&#39;C&#39;</span><span class="p">]</span><span class="o">*</span><span class="mi">100</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Boxplots">Boxplots<a class="anchor-link" href="#Boxplots">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">box</span><span class="p">()</span> <span class="c1"># Wir können mit by= auch gruppieren nach (en. group by)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Hexagonal-Bin-Plot">Hexagonal Bin Plot<a class="anchor-link" href="#Hexagonal-Bin-Plot">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Random = Normalverteilt </span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">1000</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">])</span>
<span class="n">df</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">hexbin</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;a&#39;</span><span class="p">,</span><span class="n">y</span><span class="o">=</span><span class="s1">&#39;b&#39;</span><span class="p">,</span><span class="n">gridsize</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;Oranges&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Erklärung</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">()</span> <span class="c1">#=&gt; normalveteil</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">hist</span><span class="p">()</span> <span class="c1"># Normalverteil</span>
<span class="c1"># =&gt; logisch dass wenn x = a &amp; y = b, dann die Dichte der Punkte in der Mitte liegt</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Kernel-Density-Estimation-(KDE)-Plot">Kernel Density Estimation (KDE) Plot<a class="anchor-link" href="#Kernel-Density-Estimation-(KDE)-Plot">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">kde</span><span class="p">()</span> <span class="c1"># =&gt; zeigt die KernelDensity Destination</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">plot</span><span class="o">.</span><span class="n">density</span><span class="p">()</span> <span class="c1">#&lt;= darstellung aller Spalten</span>
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>
</body123>

 


</div>
