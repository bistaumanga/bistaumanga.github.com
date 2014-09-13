---
layout: page
title: CICLING 2014
permalink: /archive/cicling/
---

<div id="ciclingCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#ciclingCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#ciclingCarousel" data-slide-to="1"></li>
    <li data-target="#ciclingCarousel" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    <div class="item active">
      <img src="/images/me/cicling_1.jpg" alt="me and Dr. Basanta Joshi">
      <div class="carousel-caption">
        Dr. Basanta Joshi, Research Director @ LogpPoint and me during CICLING 2014
      </div>
    </div>
    <div class="item">
      <img src="/images/me/cicling_3.jpg" alt="cicling presentation">
      <div class="carousel-caption">
        me speaking @ CICLING 2014 on our clustering algorithm for log messages streams.
      </div>
    </div>
    <div class="item">
      <img src="/images/me/cicling_2.jpg" alt="cicling poster">
      <div class="carousel-caption">
        me with our poster for CICLING 2014.
      </div>
    </div>
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#ciclingCarousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="#ciclingCarousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>
</div>
<br>

Research Team from <a href="http://www.logpoint.com/en/" target="_blank">LogPoint</a> presented a conference paper at <a href="http://www.cicling.org/2014/" target="_blank">CICLING 2014 </a> on <strong> Clustering algorithm for streams of log messages</strong>. 

Read about the paper <a href="http://link.springer.com/chapter/10.1007%2F978-3-642-54903-8_38" target="_blank">here</a>.

Our algorithm works in two steps. First, it sketeches the log messages using <a href="http://en.wikipedia.org/wiki/Bloom_filter">Bloom filter</a>, then uses modified version of <a href="http://www.teco.edu/tea/unsup/overview.html#Sequential_Leader_Clustering_Algorithm" target="_blank"> Sequential Leader Clustering</a> to cluster messages based on sketched representation. The notion of similarity used was <a href="http://en.wikipedia.org/wiki/Jaccard_index" target="_blank"> Jaccard similarity</a> for bit-strings.