1) lege den folder an
   1) css <=  dent eil aus #particles-js
   2) JS <= die beiden Files aus particles.js && particles.min.js
   3) Images <= das screen.jpg
  
   4) im baseof erstelle einen div Container in welchen das Konzept geladen werden kann
   > <div id="particles-js"></div>

   1) 



----

static/css
#particles-js {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #2FA7DC;
  background-image: url("../images/screen.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 50% 50%;
}


static/images
	screen.jpg

static/js
	particles-js
	particles.min.js

partial header
	hat einen Tag der auf die JS verweist

layouts index.html
	hat einen Verweis auf den partial Header
	<body>
	   <div id="particles-js"></div>
	</body>

die bilder liegen unter statics