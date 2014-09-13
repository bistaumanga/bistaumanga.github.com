---
layout: page
homepage: True
permalink: /
---

<ul class="nav nav-tabs" role="tablist" id="myTab">
  <li class="active"><a href="#profile" role="tab" data-toggle="tab">Profile</a></li>
  <li><a href="#learning" role="tab" data-toggle="tab">Learning</a></li>
  <li><a href="#publications" role="tab" data-toggle="tab">Publications</a></li>
  <li><a href="#toolbox" role="tab" data-toggle="tab">Toolbox</a></li>
  <li><a href="#share" role="tab" data-toggle="tab">Share</a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane active" id="profile"> 
  	{% include profile.html %}
  </div>

  <div class="tab-pane" id="learning"> 
	  {% include learning.html %}
  </div>

  <div class="tab-pane" id="publications"> 
	  {% include publications.html %}
  </div>

  <div class="tab-pane" id="toolbox"> 
  	{% include toolbox.html %}
  </div>

  <div class="tab-pane" id="share"> 
  	{% include share.html %}
  </div>

</div>

<script>
 function activaTab(tab){
    $('.nav-tabs a[href="#' + tab + '"]').tab('show');
	};

	activaTab('profile');
</script>




