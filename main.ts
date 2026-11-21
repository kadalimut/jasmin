// Sum up Saturday 21 November 2026 world news in one image.
// Node 22, standard library only, no network.
// The program copies the image beside it to the output folder.
// The image is drawn by tools/draw_image.py and stored as entry.png.
import { copyFileSync } from 'node:fs';
import { join } from 'node:path';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
