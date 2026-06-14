$filePath = "c:\Users\nakul\OneDrive\Desktop\Antigravity IDE\index.html"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

$partnerStart = "<!-- ── PARTNER BRANDING PROGRAM ── -->"
$galleryStart = "<!-- ── GALLERY ── -->"
$testimonialsStart = "<!-- ── TESTIMONIALS ── -->"

$idxPartner = $content.IndexOf($partnerStart)
$idxGallery = $content.IndexOf($galleryStart)
$idxTestimonials = $content.IndexOf($testimonialsStart)

if ($idxPartner -ge 0 -and $idxGallery -gt $idxPartner -and $idxTestimonials -gt $idxGallery) {

$brandExperienceHtml = @"
<!-- ── BRAND EXPERIENCE ── -->
<section id="brand-experience" class="py-28 bg-white overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-20 reveal">
      <span class="s-label">THE CLAIRMAUNT EXPERIENCE</span>
      <h2 class="font-display text-5xl md:text-6xl font-bold text-gray-900 leading-tight mb-5">Every Bottle<br/><em class="text-grad not-italic">Tells A Story</em></h2>
      <p class="text-gray-500 font-light text-lg leading-relaxed">Transform ordinary hydration into unforgettable brand experiences through luxury customization, QR technology, and premium presentation.</p>
    </div>

    <!-- Section 1: BRAND JOURNEY VISUALIZATION -->
    <div class="mb-28 reveal d1">
      <h3 class="font-heading text-2xl font-bold text-center mb-12">The Brand Journey</h3>
      <div class="flex journey-horizontal justify-between items-center relative max-w-4xl mx-auto">
        <div class="hidden md:block absolute top-1/2 left-0 w-full h-[2px] bg-gray-200 -z-10 -translate-y-1/2"></div>
        
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-royal text-2xl">verified</span></div>
          <div class="font-semibold text-sm">Your Brand</div>
        </div>
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-royal text-2xl">palette</span></div>
          <div class="font-semibold text-sm">Custom Design</div>
        </div>
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-royal text-2xl">water_drop</span></div>
          <div class="font-semibold text-sm">Premium Bottle</div>
        </div>
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-royal text-2xl">qr_code_scanner</span></div>
          <div class="font-semibold text-sm">Customer Interaction</div>
        </div>
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-gold text-2xl">star</span></div>
          <div class="font-semibold text-sm">Brand Recall</div>
        </div>
      </div>
    </div>


    <!-- Section 3: INTERACTIVE BOTTLE ECOSYSTEM & Section 4: TIMELINE -->
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-28">
      <div class="relative flex justify-center items-center h-[500px] reveal d1 bg-gray-50 rounded-2xl p-8 border border-gray-100 overflow-hidden">
        <img src="hero_bottle_new.png" alt="Ecosystem" class="h-full object-contain drop-shadow-2xl z-10" />
        
        <!-- Floating Icons -->
        <div class="eco-icon" style="top: 15%; left: 20%;"><span class="material-icons text-royal">language</span><div class="eco-tooltip">Direct visitors to your website instantly.</div></div>
        <div class="eco-icon" style="top: 30%; right: 20%;"><span class="material-icons text-pink-500">camera_alt</span><div class="eco-tooltip">Increase followers through bottle QR scans.</div></div>
        <div class="eco-icon" style="top: 50%; left: 15%;"><span class="material-icons text-orange-500">restaurant_menu</span><div class="eco-tooltip">Provide digital restaurant menus.</div></div>
        <div class="eco-icon" style="top: 65%; right: 15%;"><span class="material-icons text-green-500">shopping_bag</span><div class="eco-tooltip">Product Catalogue</div></div>
        <div class="eco-icon" style="bottom: 15%; left: 30%;"><span class="material-icons text-blue-500">event</span><div class="eco-tooltip">Event Information</div></div>
        <div class="eco-icon" style="bottom: 30%; right: 25%;"><span class="material-icons text-red-500">play_circle</span><div class="eco-tooltip">Video Content</div></div>
        <div class="eco-icon" style="top: 10%; right: 40%;"><span class="material-icons text-purple-500">contacts</span><div class="eco-tooltip">Contact Information</div></div>
      </div>
      
      <div class="reveal d2">
        <h3 class="font-heading text-3xl font-bold text-gray-900 mb-8">Real Customer Journey</h3>
        <div class="space-y-0">
          <div class="timeline-step">
            <div class="timeline-dot">1</div>
            <div><h4 class="font-semibold text-lg">Receive</h4><p class="text-gray-500 text-sm">Customer receives the premium ClairMaunt bottle.</p></div>
          </div>
          <div class="timeline-step">
            <div class="timeline-dot">2</div>
            <div><h4 class="font-semibold text-lg">Notice</h4><p class="text-gray-500 text-sm">Customer notices the high-quality branding and design.</p></div>
          </div>
          <div class="timeline-step">
            <div class="timeline-dot">3</div>
            <div><h4 class="font-semibold text-lg">Scan</h4><p class="text-gray-500 text-sm">Customer scans the integrated QR code out of curiosity.</p></div>
          </div>
          <div class="timeline-step">
            <div class="timeline-dot">4</div>
            <div><h4 class="font-semibold text-lg">Visit</h4><p class="text-gray-500 text-sm">Customer visits the designated website or campaign page.</p></div>
          </div>
          <div class="timeline-step">
            <div class="timeline-dot">5</div>
            <div><h4 class="font-semibold text-lg">Engage</h4><p class="text-gray-500 text-sm">Customer engages with the brand digitally.</p></div>
          </div>
          <div class="timeline-step">
            <div class="timeline-dot">6</div>
            <div><h4 class="font-semibold text-lg">Remember</h4><p class="text-gray-500 text-sm">The physical and digital experience creates lasting brand recall.</p></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 5: SPONSOR BRANDING EXPERIENCE -->
    <div class="bg-navy rounded-3xl p-10 md:p-16 text-white mb-28 reveal">
      <div class="text-center mb-12">
        <h3 class="font-heading text-4xl font-bold mb-4">One Bottle. Two Opportunities.</h3>
        <p class="text-white/60 max-w-2xl mx-auto">Our unique split-branding design serves both the event host and the sponsor perfectly.</p>
      </div>
      <div class="grid md:grid-cols-3 gap-8 items-center">
        <div class="space-y-6 text-right md:text-left">
          <h4 class="text-xl font-bold text-gold">Event Organizer</h4>
          <ul class="space-y-3 text-sm text-white/70">
            <li class="flex justify-end md:justify-start items-center gap-2">Reduced beverage costs <span class="material-icons text-green-400 text-sm">check</span></li>
            <li class="flex justify-end md:justify-start items-center gap-2">Premium branding <span class="material-icons text-green-400 text-sm">check</span></li>
            <li class="flex justify-end md:justify-start items-center gap-2">Event visibility <span class="material-icons text-green-400 text-sm">check</span></li>
          </ul>
        </div>
        
        <div class="split-bottle">
          <img src="hero_bottle_new.png" class="h-full object-contain opacity-30 absolute" alt="Bottle Base" />
          <div class="bottle-mask-client" id="clientMask">75% Client Branding</div>
          <div class="bottle-mask-sponsor" id="sponsorMask">25% Sponsor Branding</div>
        </div>
        
        <div class="space-y-6">
          <h4 class="text-xl font-bold text-royal-light">Brand Sponsor</h4>
          <ul class="space-y-3 text-sm text-white/70">
            <li class="flex items-center gap-2"><span class="material-icons text-green-400 text-sm">check</span> Advertising exposure</li>
            <li class="flex items-center gap-2"><span class="material-icons text-green-400 text-sm">check</span> QR-enabled campaigns</li>
            <li class="flex items-center gap-2"><span class="material-icons text-green-400 text-sm">check</span> Audience engagement</li>
          </ul>
        </div>
      </div>
      <div class="mt-8 text-center">
        <input type="range" min="10" max="50" value="25" class="w-64 accent-gold" id="sponsorSlider" oninput="updateSponsorMask(this.value)" />
        <div class="text-xs text-white/50 mt-2">Adjust Sponsor Branding Area (%)</div>
      </div>
    </div>

    <!-- Section 6: IMPACT METRICS & CLOSING -->
    <div class="text-center reveal">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-16">
        <div class="p-6 bg-gray-50 rounded-2xl border border-gray-100"><div class="font-display text-4xl font-bold text-royal mb-2">100%</div><div class="text-xs uppercase tracking-widest text-gray-500">Brand Visibility</div></div>
        <div class="p-6 bg-gray-50 rounded-2xl border border-gray-100"><div class="font-display text-4xl font-bold text-royal mb-2">Smart</div><div class="text-xs uppercase tracking-widest text-gray-500">QR Enabled</div></div>
        <div class="p-6 bg-gray-50 rounded-2xl border border-gray-100"><div class="font-display text-4xl font-bold text-royal mb-2">Multiple</div><div class="text-xs uppercase tracking-widest text-gray-500">Touchpoints</div></div>
        <div class="p-6 bg-gray-50 rounded-2xl border border-gray-100"><div class="font-display text-4xl font-bold text-royal mb-2">Premium</div><div class="text-xs uppercase tracking-widest text-gray-500">Presentation</div></div>
      </div>
      
      <div class="max-w-3xl mx-auto py-12 border-t border-gray-200">
        <h2 class="font-display text-4xl italic text-gray-900 mb-8">"Every hand that holds a ClairMaunt bottle becomes a touchpoint for your brand."</h2>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="#quote" class="btn btn-blue">Start Your Brand Experience</a>
          <a href="#quote" class="btn btn-outline-b">Request A Custom Mockup</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── SCRIPT FOR BRAND EXPERIENCE ── -->
<script>
function updateSponsorMask(val) {
  const s = document.getElementById('sponsorMask');
  const c = document.getElementById('clientMask');
  if(s && c) {
    s.style.height = val + '%';
    s.innerText = val + '% Sponsor Branding';
    c.style.height = (80 - val) + '%';
    c.innerText = (100 - val) + '% Client Branding';
  }
}
</script>
`r`n
"@

$advertiseHtml = @"
<!-- ── ADVERTISE ON BOTTLES ── -->
<section id="advertise" class="py-28 relative overflow-hidden" style="background:#0E0E2C">
  <div class="absolute inset-0 opacity-5" style="background-image:radial-gradient(circle,#2929CC 1px,transparent 1px);background-size:40px 40px"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-20 reveal">
      <span class="s-label" style="color: #C9AA71;">CLAIRMAUNT MARKETING SOLUTIONS</span>
      <h2 class="font-display text-5xl md:text-6xl font-bold text-white leading-tight mb-6">Advertise On <em class="text-grad not-italic">Bottles</em></h2>
      <p class="text-white/60 font-light text-lg leading-relaxed">Put your brand directly into the hands of your audience through premium customized water bottles distributed at events, conferences, tournaments, exhibitions, and corporate gatherings.</p>
    </div>

    <!-- Section 1: HOW IT WORKS -->
    <div class="mb-28 reveal">
      <div class="flex flex-col md:flex-row justify-between items-center relative gap-6">
        <div class="hidden md:block absolute top-1/2 left-0 w-full h-[2px] bg-white/10 -z-10 -translate-y-1/2"></div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">confirmation_number</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Choose Event</h4>
        </div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">image</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Submit Assets</h4>
        </div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">brush</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Label Design</h4>
        </div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">local_shipping</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Distributed</h4>
        </div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">qr_code_scanner</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Engagement</h4>
        </div>
        <div class="text-center w-32 relative z-10">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">trending_up</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Visibility & Leads</h4>
        </div>
      </div>
    </div>

    <!-- Section 2: WHY ADVERTISE -->
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-28 reveal">
      <div class="glass p-8 hover:border-royal transition-colors">
        <h4 class="text-gold font-bold text-lg mb-3">Direct Visibility</h4>
        <p class="text-white/60 text-sm font-light">Your brand appears directly in the hands of event attendees.</p>
      </div>
      <div class="glass p-8 hover:border-royal transition-colors">
        <h4 class="text-gold font-bold text-lg mb-3">QR Code Marketing</h4>
        <p class="text-white/60 text-sm font-light">Drive traffic to websites, Instagram pages, WhatsApp, and landing pages.</p>
      </div>
      <div class="glass p-8 hover:border-royal transition-colors">
        <h4 class="text-gold font-bold text-lg mb-3">Premium Association</h4>
        <p class="text-white/60 text-sm font-light">Align your business with high-quality events and memorable experiences.</p>
      </div>
      <div class="glass p-8 hover:border-royal transition-colors">
        <h4 class="text-gold font-bold text-lg mb-3">Longer Attention</h4>
        <p class="text-white/60 text-sm font-light">Unlike flyers that are discarded, bottles remain with attendees throughout the event.</p>
      </div>
    </div>


    <!-- Section 8: BOLD STATEMENT -->
    <div class="text-center max-w-4xl mx-auto p-8 mb-20 md:mb-28 reveal">
      <h2 class="font-display text-4xl md:text-5xl lg:text-6xl text-white leading-tight">"Unlike banners people ignore and flyers they throw away,<br/><span class="text-royal-light">a bottle stays in their hand.</span>"</h2>
    </div>

    <!-- CTA -->
    <div class="text-center border-t border-white/10 pt-16 reveal">
      <h3 class="font-display text-4xl font-bold text-white mb-4">Ready To Advertise On Bottles?</h3>
      <p class="text-white/60 mb-8 max-w-2xl mx-auto">Reach your audience through a marketing medium they carry, hold, use, and interact with throughout the event.</p>
      <div class="flex flex-wrap justify-center gap-4">
        <a href="#quote" class="btn btn-blue">Become A Sponsor</a>
        <a href="#quote" class="btn btn-outline-w">Request Media Kit</a>
      </div>
    </div>

  </div>
</section>
`r`n
"@

  $newContent = $content.Substring(0, $idxPartner) + $advertiseHtml + $brandExperienceHtml + $content.Substring($idxTestimonials)
  [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
  Write-Output "Successfully replaced sections using Substring!"
} else {
  Write-Output "Could not find one of the markers:"
  Write-Output "Partner: $idxPartner, Gallery: $idxGallery, Testimonials: $idxTestimonials"
}
