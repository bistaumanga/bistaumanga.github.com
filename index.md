---
layout: page
homepage: True
permalink: /
---


<ul class="nav nav-tabs" role="tablist" id="myTab">
  <li class="active"><a href="#profile" role="tab" data-toggle="tab">Profile</a></li>
  <li><a href="#learning" role="tab" data-toggle="tab">Learning</a></li>
  <li><a href="#toolbox" role="tab" data-toggle="tab">Toolbox</a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane active" id="profile"> 
  	{% include profile.html %}
  </div>

  <div class="tab-pane" id="learning"> 
	  {% include learning.html %}
	</div>

  <div class="tab-pane" id="toolbox"> 
  	<div class="panel panel-primary">
  		<div class="panel-heading">Programming</div>
		  <div class="panel-body">
		    Python, R, Scala, Java, Octave, C, C++
		</div>
  	</div>
	<div class="panel panel-success">
		<div class="panel-heading">IDE \ Text Editors</div>
		  <div class="panel-body">
		    R Studio, Tex Studio, Eclipse, Sublime Text, Spyder, Mou, Vim
		</div>
	</div>
	<div class="panel panel-info">
		<div class="panel-heading">Collaboration</div>
		  <div class="panel-body">
		    Git (Github, BitBucket), Share Latex, Dropbox
		</div>
	</div>
	<div class="panel panel-warning">
		<div class="panel-heading">Documentation</div>
		  <div class="panel-body">
		    $\LaTeX$, Markdown, R Markdown, HTML, IPython
		</div>
	</div>
	<div class="panel panel-danger">
		<div class="panel-heading">Data Science</div>
		  <div class="panel-body">
		    R, Scipy ecosystem, Hadoop, Spark, SQL, Plotly
		</div>
	</div>

	<div class="panel panel-info">
		<div class="panel-heading">OS and Others</div>
		  <div class="panel-body">
		    Ubuntu, OS X, Terminal, Jekyll, VirtualBox, Excel...
		</div>
	</div>
  </div>
</div>

<script>
 function activaTab(tab){
    $('.nav-tabs a[href="#' + tab + '"]').tab('show');
	};

	activaTab('profile');
</script>




