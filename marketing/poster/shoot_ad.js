const { chromium } = require('playwright'); const path=require('path');
(async () => {
  const b = await chromium.launch({args:['--font-render-hinting=none','--disable-lcd-text','--force-color-profile=srgb']});
  const p = await b.newPage({viewport:{width:1400,height:2230}, deviceScaleFactor:2});
  await p.goto('file://'+path.join(__dirname,'ad.out.html'),{waitUntil:'load'});
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
  const a = await p.evaluate(() => {
    const c=document.querySelector('.canvas'), sh=document.querySelector('.shell');
    const cb=c.getBoundingClientRect(); const bad=[];
    document.querySelectorAll('.shell *').forEach(el=>{
      const r=el.getBoundingClientRect(); if(!r.width&&!r.height) return;
      if(r.left<cb.left+8||r.right>cb.right-8||r.top<cb.top+4||r.bottom>cb.bottom-4)
        bad.push(`${el.className||el.tagName} L${r.left|0} R${r.right|0} T${r.top|0} B${r.bottom|0}`);
    });
    // detect text that overflows its own box (clipped/overlapping)
    const clip=[];
    document.querySelectorAll('.shell *').forEach(el=>{
      if(el.children.length===0 && el.scrollWidth>el.clientWidth+1 && el.clientWidth>0)
        clip.push(`${el.className||el.tagName}: ${el.scrollWidth}>${el.clientWidth} "${(el.textContent||'').slice(0,28)}"`);
    });
    return {overflowY: sh.scrollHeight-sh.clientHeight, canvasH:c.clientHeight,
            footBottom: document.querySelector('.foot2').getBoundingClientRect().bottom,
            contactTop: document.querySelector('.contact').getBoundingClientRect().top,
            bad: bad.slice(0,12), clip: clip.slice(0,12)};
  });
  console.log(JSON.stringify(a,null,1));
  await p.locator('.canvas').screenshot({path:path.join(__dirname,'khw-ad.png'), scale:'device'});
  await b.close();
})();
