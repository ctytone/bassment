# Bassment

A trap and underground beat machine in the browser, played with a Novation Launchpad MK2 or the on-screen pads.

## Run it

Open `index.html` in Chrome or Edge (double-click works), click **Start audio and MIDI**, and play.
Plug the Launchpad in first to use it; the on-screen pads work without one.

## What's in it

- **Page 1, Drums:** kicks, snares, claps, closed hats, open hats and cymbals, percussion, underground hits and FX, one row each. The right-hand buttons pick a hi-hat roll speed; hold a drum pad to roll it in time with the tempo.
- **Page 2, 808s:** six 808s, tuned to play in key.
- **Page 3, Melody:** piano, bells, flute, organ, kalimba and harp, all real recordings.
- Everything on pages 2 and 3 is in a minor key you choose. Notes play while their pad is held.

On the Launchpad: the bottom two right-hand buttons change page; on the top row ▲ is the rainbow light show, ▼ stops all sound, ◀ ▶ change the key.

## Folders

| Path | What it is |
|---|---|
| `index.html` | The whole app |
| `sounds/raw/` | Every sample as a normal audio file (usable in any DAW) |
| `sounds/*.js` | The samples packed so the page works when opened straight from disk |
| `sounds/build-bundles.py` | Rebuilds those packs after adding or swapping samples |
| `sounds/CREDITS.md` | Where every sound came from (all CC0) |

## Planned

- Record performances and loop them
- Save and load loops
- Export to MP3 / WAV
