// Record the demo HTML as a GIF using Playwright
const { chromium } = require('playwright');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const W = 1200;
const H = 720;
const FPS = 12;
const DURATION_MS = 12000;  // 12 seconds total
const TOTAL_FRAMES = Math.floor(DURATION_MS / 1000 * FPS);

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: W, height: H },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();

  const htmlPath = path.join(__dirname, 'demo.html');
  await page.goto('file://' + htmlPath);
  await page.waitForLoadState('networkidle');

  // Take frames at regular intervals
  const tmpDir = '/tmp/demo_frames';
  if (!fs.existsSync(tmpDir)) fs.mkdirSync(tmpDir);

  const frameDelay = 1000 / FPS;
  const totalFrames = Math.floor(DURATION_MS / frameDelay);

  console.log(`Recording ${totalFrames} frames at ${FPS} fps...`);

  for (let i = 0; i < totalFrames; i++) {
    await page.waitForTimeout(frameDelay);
    const buf = await page.screenshot({ type: 'png', fullPage: false });
    fs.writeFileSync(`${tmpDir}/frame_${String(i).padStart(4, '0')}.png`, buf);
  }

  await browser.close();
  console.log('Frames captured.');

  // Encode to GIF with ffmpeg
  const out = path.join(__dirname, '..', 'docs', 'assets', 'demo.gif');
  console.log(`Encoding GIF to ${out}...`);

  execSync(`ffmpeg -y -framerate ${FPS} -i ${tmpDir}/frame_%04d.png -vf "fps=${FPS},scale=${W}:${H}:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ${out}`, { stdio: 'inherit' });

  // Cleanup
  for (const f of fs.readdirSync(tmpDir)) fs.unlinkSync(path.join(tmpDir, f));
  fs.rmdirSync(tmpDir);

  const size = fs.statSync(out).size / 1024;
  console.log(`Done. ${out} (${size.toFixed(0)} KB)`);
})();
