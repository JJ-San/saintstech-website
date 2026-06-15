/* saintstech.co.nz — interactions: scroll reveals, ROI calculator,
   inline tool-name rotator, sticky mobile CTA. Reduced-motion safe. */

(function(){
  'use strict';
  document.documentElement.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- scroll reveals (IntersectionObserver — works on iOS Safari) ---- */
  var reveals = [].slice.call(document.querySelectorAll('.reveal'));
  if (!('IntersectionObserver' in window) || reduce){
    reveals.forEach(function(el){ el.classList.add('is-in'); });
  } else {
    /* stagger siblings inside [data-stagger] groups */
    [].slice.call(document.querySelectorAll('[data-stagger]')).forEach(function(group){
      [].slice.call(group.children).forEach(function(child, i){
        child.style.transitionDelay = (i * 90) + 'ms';
      });
    });
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting){
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    reveals.forEach(function(el){ io.observe(el); });
  }

  /* ---- the honest calculator ---- */
  var WEEKS = 48, EFFICIENCY = 0.8, SUPPORT_YR = 2400, BUILD_LO = 7500, BUILD_HI = 15000;
  var hoursEl = document.getElementById('calc-hours');
  var rateEl  = document.getElementById('calc-rate');

  if (hoursEl && rateEl){
    var outHours = document.getElementById('out-hours');
    var outRate  = document.getElementById('out-rate');
    var resAnnual = document.getElementById('res-annual');
    var resSaving = document.getElementById('res-saving');
    var verdictEl = document.getElementById('res-verdict');
    var badgeEl   = document.getElementById('res-badge');
    var titleEl   = document.getElementById('res-title');
    var subEl     = document.getElementById('res-sub');
    var rafA = null, rafS = null;

    function fmt(n){ return '$' + Math.round(n).toLocaleString('en-NZ'); }

    function paint(input){
      var pct = (input.value - input.min) / (input.max - input.min) * 100;
      input.style.background = 'linear-gradient(90deg, var(--teal-bright) ' + pct + '%, rgba(255,255,255,.16) ' + pct + '%)';
    }

    function countTo(el, target, prevRaf){
      if (prevRaf) cancelAnimationFrame(prevRaf);
      var from = parseFloat(el.dataset.val || '0');
      if (reduce || Math.abs(target - from) < 1){
        el.dataset.val = target; el.textContent = fmt(target); return null;
      }
      var t0 = null, DUR = 380, raf;
      function tick(ts){
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / DUR, 1);
        p = 1 - Math.pow(1 - p, 3); /* ease-out */
        var val = from + (target - from) * p;
        el.textContent = fmt(val);
        if (p < 1){ raf = requestAnimationFrame(tick); }
        else { el.dataset.val = target; }
      }
      raf = requestAnimationFrame(tick);
      return raf;
    }

    function update(){
      var h = +hoursEl.value, r = +rateEl.value;
      outHours.textContent = h + (h === 1 ? ' hr' : ' hrs');
      outRate.textContent = '$' + r;
      paint(hoursEl); paint(rateEl);

      var annual = h * r * WEEKS;
      var saving = annual * EFFICIENCY - SUPPORT_YR;

      rafA = countTo(resAnnual, annual, rafA);
      rafS = countTo(resSaving, Math.max(0, saving), rafS);

      var state, badge, title, sub;
      if (saving < 1500){
        state = 'is-no'; badge = 'Honestly, no';
        title = 'Keep doing this one by hand.';
        sub = 'A build won\u2019t pay for itself at these numbers, and we\u2019d tell you the same in person. If it still annoys you, the <b>Enable</b> tier ($2,500–6,000) might cover it with training. The talk is free either way.';
      } else {
        var perMonth = saving / 12;
        var pLo = Math.max(1, Math.ceil(BUILD_LO / perMonth));
        var pHi = Math.max(pLo, Math.ceil(BUILD_HI / perMonth));
        if (pHi <= 14){
          state = ''; badge = 'Worth automating';
          title = 'This one should be a machine.';
          sub = 'A build at $7,500–$15,000 pays for itself in about <b>' + pLo + '\u2013' + pHi + ' months</b>, then keeps saving \u2248 <b>' + fmt(saving) + '/yr</b> after support costs.';
        } else if (pHi <= 26){
          state = 'is-maybe'; badge = 'Borderline';
          title = 'Worth a conversation.';
          sub = 'Payback lands around <b>' + pLo + '\u2013' + pHi + ' months</b>. Sometimes that\u2019s worth it for the hours back; sometimes training (<b>Enable</b>, $2,500–6,000) is the smarter buy. The free talk settles it.';
        } else {
          state = 'is-no'; badge = 'Honestly, no';
          title = 'Keep doing this one by hand.';
          sub = 'Payback would take over two years, so we\u2019d talk you out of a build. If it still annoys you, the <b>Enable</b> tier ($2,500–6,000) might cover it with training.';
        }
      }
      verdictEl.className = ('verdict ' + state).trim();
      badgeEl.textContent = badge;
      titleEl.textContent = title;
      subEl.innerHTML = sub;
    }

    hoursEl.addEventListener('input', update);
    rateEl.addEventListener('input', update);
    update();
  }

  /* ---- "we work with" rotator: size the slot to the widest entry, then crossfade ---- */
  var rot = document.getElementById('ww-rotator');
  if (rot && !reduce){
    var rotItems = [].slice.call(rot.querySelectorAll('.rot-item'));
    if (rotItems.length){
      var longest = rotItems[0];
      rotItems.forEach(function(el){
        if (el.textContent.trim().length > longest.textContent.trim().length) longest = el;
      });
      var sizer = document.createElement('span');
      sizer.className = 'rot-sizer';
      sizer.setAttribute('aria-hidden','true');
      sizer.innerHTML = longest.innerHTML;
      rot.insertBefore(sizer, rot.firstChild);
      rot.classList.add('is-live');
      var ri = 0;
      rotItems[0].classList.add('active');
      setInterval(function(){
        rotItems[ri].classList.remove('active');
        ri = (ri + 1) % rotItems.length;
        rotItems[ri].classList.add('active');
      }, 1900);
    }
  }

  /* ---- hide the mobile bar when the contact band is on screen ---- */
  var bar = document.getElementById('mobile-cta');
  var contact = document.getElementById('contact');
  if (bar && contact && 'IntersectionObserver' in window){
    var barIO = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        bar.classList.toggle('is-hidden', entry.isIntersecting);
      });
    }, { threshold: 0.15 });
    barIO.observe(contact);
  }
})();
