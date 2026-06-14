import re
import sys

def main():
    file_path = r'c:\Users\nakul\OneDrive\Desktop\Antigravity IDE\index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Navigation Links
    content = content.replace('href="#partner"', 'href="#advertise"')
    content = content.replace('Partner Program', 'Advertise')
    content = content.replace('href="#gallery"', 'href="#brand-experience"')
    content = content.replace('Gallery', 'Brand Experience')
    
    # 2. Add New CSS rules for responsiveness and new sections
    new_css = """
/* Responsive Overhaul */
html { scroll-padding-top: 80px; }
@media (max-width: 1024px) {
  .hero-bg { transform: scale(1.1); }
  h1.font-display { font-size: 4rem; line-height: 1; }
  h2.font-display { font-size: 3.5rem; line-height: 1.1; }
  .grid.lg\\:grid-cols-2 { grid-template-columns: 1fr; }
  .ind-card { height: 200px; }
}
@media (max-width: 768px) {
  h1.font-display { font-size: 3rem; }
  h2.font-display { font-size: 2.5rem; }
  .f-card { padding: 1.5rem; }
  .grid.md\\:grid-cols-4 { grid-template-columns: 1fr; }
  .grid.md\\:grid-cols-3 { grid-template-columns: 1fr; }
  .grid.md\\:grid-cols-2 { grid-template-columns: 1fr; }
  .grid.sm\\:grid-cols-2 { grid-template-columns: 1fr; }
  .gal-grid { grid-template-columns: 1fr; grid-auto-rows: 250px; }
  .gal-item:nth-child(1), .gal-item:nth-child(4) { grid-column: span 1; grid-row: span 1; }
  .glass { padding: 1.5rem; }
  .glass-light { padding: 1.5rem; }
  .px-6 { padding-left: 1rem; padding-right: 1rem; }
  .py-28 { padding-top: 4rem; padding-bottom: 4rem; }
  .hero-container { flex-direction: column; text-align: center; }
  .hero-container .flex-wrap { justify-content: center; }
  .hero-stats { justify-content: center; }
  #mob-menu { width: 100%; top: 80px; left: 0; position: absolute; }
  .faq-ans { max-height: 0; }
  .faq-ans.open { max-height: 500px; }
  .ind-card { height: auto; padding: 2rem 1rem; }
  .ind-overlay { position: static; opacity: 1; background: transparent; padding: 0; margin-top: 1rem; text-align: center; }
  .ind-overlay p { display: block; }
}

/* Brand Experience & Advertise Sections CSS */
.journey-step { position: relative; z-index: 10; }
.journey-line { position: absolute; top: 50%; left: 50%; width: 100%; height: 2px; background: linear-gradient(90deg, #C9AA71, transparent); transform: translateY(-50%); z-index: 0; }
.journey-line.gold { background: #C9AA71; }
@media (max-width: 768px) {
  .journey-horizontal { flex-direction: column; align-items: center; gap: 2rem; }
  .journey-line { width: 2px; height: 100%; left: 50%; top: 50%; transform: translateX(-50%); background: linear-gradient(180deg, #C9AA71, transparent); }
}
.eco-icon { position: absolute; background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 0.5rem; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); cursor: pointer; transition: all 0.3s ease; }
.eco-icon:hover { transform: scale(1.1); background: #2929CC; }
.eco-tooltip { position: absolute; bottom: 120%; left: 50%; transform: translateX(-50%); background: #fff; color: #0E0E2C; padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; }
.eco-icon:hover .eco-tooltip { opacity: 1; }

.timeline-step { display: flex; align-items: flex-start; gap: 1.5rem; position: relative; padding-bottom: 2rem; }
.timeline-step::before { content: ''; position: absolute; left: 1rem; top: 2rem; bottom: 0; width: 2px; background: rgba(41,41,204,0.2); }
.timeline-step:last-child::before { display: none; }
.timeline-dot { width: 2rem; height: 2rem; border-radius: 50%; background: #2929CC; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; z-index: 10; }

.split-bottle { position: relative; height: 500px; display: flex; justify-content: center; align-items: center; }
.bottle-mask-client { position: absolute; top: 10%; bottom: 10%; left: 50%; width: 120px; transform: translateX(-50%); background: #f0f4ff; border-radius: 10px 10px 0 0; height: 60%; display: flex; align-items: center; justify-content: center; color: #2929CC; font-weight: bold; border: 2px solid #2929CC; border-bottom: none; }
.bottle-mask-sponsor { position: absolute; bottom: 10%; left: 50%; width: 120px; transform: translateX(-50%); background: #2929CC; border-radius: 0 0 10px 10px; height: 20%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold; border: 2px solid #2929CC; border-top: 1px dashed white; }
</style>"""
    
    content = content.replace('</style>', new_css)
    
    # 3. Generate New Brand Experience Section HTML
    brand_experience_html = """
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
          <div class="font-semibold text-sm">Customer Scan</div>
        </div>
        <div class="journey-step flex flex-col items-center gap-3 text-center">
          <div class="w-16 h-16 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-lg"><span class="material-icons-outlined text-gold text-2xl">star</span></div>
          <div class="font-semibold text-sm">Brand Recall</div>
        </div>
      </div>
    </div>

    <!-- Section 2: INDUSTRY EXPERIENCE CARDS -->
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-28 reveal">
      <div class="f-card text-center">
        <span class="material-icons-outlined text-royal text-4xl mb-4">celebration</span>
        <h4 class="font-heading font-bold text-xl mb-3">Luxury Weddings</h4>
        <p class="text-sm text-gray-500 font-light">Create personalized wedding bottles featuring monograms, event branding, and QR-linked wedding albums.</p>
      </div>
      <div class="f-card text-center">
        <span class="material-icons-outlined text-royal text-4xl mb-4">restaurant</span>
        <h4 class="font-heading font-bold text-xl mb-3">Restaurants &amp; Cafés</h4>
        <p class="text-sm text-gray-500 font-light">Transform bottles into interactive menus, loyalty tools, and social media touchpoints.</p>
      </div>
      <div class="f-card text-center">
        <span class="material-icons-outlined text-royal text-4xl mb-4">hotel</span>
        <h4 class="font-heading font-bold text-xl mb-3">Hotels &amp; Resorts</h4>
        <p class="text-sm text-gray-500 font-light">Elevate guest experiences through premium branded hydration in rooms and wellness centers.</p>
      </div>
      <div class="f-card text-center">
        <span class="material-icons-outlined text-royal text-4xl mb-4">business_center</span>
        <h4 class="font-heading font-bold text-xl mb-3">Corporate Events</h4>
        <p class="text-sm text-gray-500 font-light">Generate brand visibility, sponsorship exposure, and attendee engagement.</p>
      </div>
    </div>

    <!-- Section 3: INTERACTIVE BOTTLE ECOSYSTEM & Section 4: TIMELINE -->
    <div class="grid lg:grid-cols-2 gap-16 items-center mb-28">
      <div class="relative flex justify-center items-center h-[500px] reveal d1 bg-gray-50 rounded-2xl p-8 border border-gray-100">
        <img src="hero_bottle_new.png" alt="Ecosystem" class="h-full object-contain drop-shadow-2xl z-10" />
        
        <!-- Floating Icons -->
        <div class="eco-icon" style="top: 15%; left: 20%;"><span class="material-icons text-royal">language</span><div class="eco-tooltip">Direct to Website</div></div>
        <div class="eco-icon" style="top: 30%; right: 20%;"><span class="material-icons text-pink-500">camera_alt</span><div class="eco-tooltip">Instagram Follow</div></div>
        <div class="eco-icon" style="top: 50%; left: 15%;"><span class="material-icons text-orange-500">restaurant_menu</span><div class="eco-tooltip">Digital Menu</div></div>
        <div class="eco-icon" style="top: 65%; right: 15%;"><span class="material-icons text-green-500">shopping_bag</span><div class="eco-tooltip">Product Catalogue</div></div>
        <div class="eco-icon" style="bottom: 15%; left: 30%;"><span class="material-icons text-blue-500">event</span><div class="eco-tooltip">Event Info</div></div>
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
          <div class="bottle-mask-client">75% Client</div>
          <div class="bottle-mask-sponsor">25% Sponsor</div>
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
        <input type="range" min="10" max="30" value="25" class="w-64 accent-gold" id="sponsorSlider" />
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
"""

    # 4. Generate New Advertise on Bottles Section HTML
    advertise_html = """
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
        <div class="text-center w-32">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">confirmation_number</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Choose Event</h4>
        </div>
        <div class="text-center w-32">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">image</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Submit Assets</h4>
        </div>
        <div class="text-center w-32">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">brush</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Label Design</h4>
        </div>
        <div class="text-center w-32">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">local_shipping</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Distributed</h4>
        </div>
        <div class="text-center w-32">
          <div class="w-16 h-16 mx-auto rounded-full bg-navy border border-royal flex items-center justify-center mb-3"><span class="material-icons text-white">qr_code_scanner</span></div>
          <h4 class="text-white text-xs font-bold uppercase tracking-wider">Engagement</h4>
        </div>
        <div class="text-center w-32">
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


    <!-- Section 7: CASE STUDY & SECTION 8: BOLD STATEMENT -->
    <div class="grid lg:grid-cols-2 gap-12 items-center mb-20 reveal">
      <div class="glass p-10 rounded-2xl border-t border-l border-white/20">
        <div class="text-xs uppercase tracking-widest text-gold mb-2">Real-World Case Study</div>
        <h3 class="text-2xl font-bold text-white mb-6">Restaurant Promotion Campaign</h3>
        <ul class="space-y-4 text-white/70 text-sm">
          <li><strong>Event:</strong> College Sports Tournament</li>
          <li><strong>Sponsor:</strong> Local Restaurant</li>
          <li><strong>Campaign:</strong> 20% Discount Offer</li>
          <li><strong>Feature:</strong> QR Code linked to Menu & Offer Page</li>
          <li><strong class="text-green-400">Result:</strong> Students scanned the bottle, discovered the restaurant, and redeemed the offer during and after the event.</li>
        </ul>
      </div>
      <div class="text-center lg:text-left p-8">
        <h2 class="font-display text-4xl md:text-5xl text-white leading-tight">"Unlike banners people ignore and flyers they throw away,<br/><span class="text-royal-light">a bottle stays in their hand.</span>"</h2>
      </div>
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
"""

    # 5. Perform the replacements using regex
    # Replace Gallery
    content = re.sub(r'<!-- ── GALLERY ── -->.*?</section>', brand_experience_html, content, flags=re.DOTALL)
    
    # Replace Partner Program
    content = re.sub(r'<!-- ── PARTNER BRANDING PROGRAM ── -->.*?</section>', advertise_html, content, flags=re.DOTALL)

    # 6. Apply responsive hero classes
    # Change grid lg:grid-cols-2 in Hero to be more robust
    content = content.replace('<div class="grid lg:grid-cols-2 gap-16 items-center">', '<div class="grid lg:grid-cols-2 gap-16 items-center hero-container">')
    content = content.replace('<div class="flex flex-wrap gap-4 reveal d3">', '<div class="flex flex-wrap gap-4 reveal d3 justify-center lg:justify-start">')
    content = content.replace('<div class="flex gap-10 mt-16 pt-10 border-t border-white/10 reveal d4">', '<div class="flex flex-wrap gap-10 mt-16 pt-10 border-t border-white/10 reveal d4 hero-stats justify-center lg:justify-start">')
    
    # Update HTML tag to ensure padding for fixed nav doesn't cut off section tops
    content = content.replace('<html lang="en" class="scroll-smooth">', '<html lang="en" class="scroll-smooth" style="scroll-padding-top: 80px;">')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
