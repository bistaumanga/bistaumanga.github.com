---
layout: page
homepage: True
permalink: /
---

<ul class="nav nav-tabs" role="tablist" id="myTab">
  <li class="active"><a href="#profile" role="tab" data-toggle="tab">Profile</a></li>
  <li><a href="#publications" role="tab" data-toggle="tab">Publications</a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane active" id="profile"> 
  	{% include profile.html %}
  </div>

  <div class="tab-pane" id="publications"> 
	  {% include publications.html %}
  </div>

</div>

<script>
 function activaTab(tab){
    $('.nav-tabs a[href="#' + tab + '"]').tab('show');
	};

	activaTab('profile');
</script>