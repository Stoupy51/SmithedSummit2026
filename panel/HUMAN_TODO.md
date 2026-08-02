# Human TODO — things only Stoupy can do

Things that need a human: design decisions, visual assets, or talking to other people.
Technical background in [REEF.md](REEF.md). Panel content plan in [TODO.md](TODO.md).

---

## 🔴 Blocking — the one thing standing between you and working slides

### 1. Re-export the presentation at 336 x 192 pt

`How to Boost your Productivity.pdf` is currently **1440 x 810 pt** (16:9). Reef maps 1 point to 1/16 of a block, so that renders as a **90 x 50.6 block** screen — roughly four times the Welded Woodlands wall.

The build already tells you this on every run:

```
[WARNING] 'How to Boost your Productivity.pdf' is 1440x810 pt but Welded Woodlands expects
336x192 pt. Reef would render a 90x50.625 block screen instead of 21x12.
```

**Set a custom page size of `336 x 192 pt`** = `4.667 x 2.667 in` = `118.53 x 67.73 mm`, then re-export over the same filename. Nothing else needs touching — the build picks up the new size and slide count automatically.

> The aspect changes from 16:9 (1.778) to 7:4 (1.75). A 1.6% difference, invisible in practice, but your existing 6 slides will squash very slightly. Fix it now while the deck is small.
>
> To keep true 16:9 instead, use **336 x 189 pt** and change `page_height` in [src/reef/stages.py](src/reef/stages.py). You lose 3 pt (0.19 block) at the bottom of the wall, which nobody will notice.

### 2. Confirm the stage with the organisers

I inferred **Welded Woodlands** because it is the only Summit stage template that is exactly 336 x 192 pt. If they move you, change `TARGET_STAGE` in [src/reef/stages.py](src/reef/stages.py) — every other stage is already in the table.

| Stage | pt | blocks |
|---|---|---|
| Patched Plateaus — main | 546 x 269 | 34.1 x 16.8 |
| Patched Plateaus — side | 273 x 167 | 17.1 x 10.4 |
| Textured Tropics | 400 x 224 | 25 x 14 |
| **Welded Woodlands** | **336 x 192** | **21 x 12** |

Also worth asking:
- Will you be handed a **pre-linked remote**, or link one yourself?
- Do you get `reef.permissions.use_remote` automatically as a presenter?
- Can you get a **rehearsal slot** on the real stage screen?
- Deadline for handing over the datapack and resource pack?

---

## 🟢 Done — no action needed

| Was | Now |
|---|---|
| Install Poppler | Installed at `D:/advanced_desktop/poppler/poppler-26.02.0/`, wired into `beet.yml` as `meta.reef.pdf.poppler_path` |
| Bundle Bookshelf | Not needed — StewBeet spots `#bs.move:` and drops `Bookshelf Move.zip` into the world itself |
| Wire Reef into `beet.yml` | `reef` added to `require`, `meta.reef` configured at dpi 144 |
| Scaffold the Reef source | Replaced by [src/reef/](src/reef/), which reads the PDF directly — no renaming, no copying, no manual page count |
| Hook `register_namespace` | Called from `confirm_load`, verified in the build output |
| Build a laser pointer | Summit already ships one: `loot give @s loot summit.laser_pointer:zz/green_laser_pointer` |

---

## 🟡 Content and assets — the actual work

### 3. Make the slides

35 minutes, beginner-to-expert audience. Outline in [TODO.md](TODO.md).

Design constraints that come from Reef, not from taste:
- **7:4 aspect** (1.75), wider than 16:9. Do not design at 16:9 and letterbox.
- At dpi 144 the texture is **672 x 384 px** = 32 px per block. Small text will be mush. **Test your minimum font size in-game early.**
- Slides render **fullbright** — no world lighting, no shadows. High-contrast flat designs read best.
- The audience stands at variable distance and angle. Bigger than you think.

### 4. Screenshots and images to produce

From [TODO.md](TODO.md): the GitHub contribution graph, code samples from Myriad / Gamemode 4 / Bookshelf, the good-vs-bad structure comparison, StewBeet abstraction examples, the shopping-kart-vs-Steve visual, and the AI section examples.

### 5. Get permission / credit right

- Ask before putting other people's code on a screen in front of the whole Summit.
- The Discord message you link in the AI section quotes someone — consider anonymising it.

---

## 🔵 Still to build (say the word and I will)

### 6. The live AI vote
5-point hate/tolerate scale per Gen-AI type (image / text-code / sound), results shown live. A `dialog` plus scoreboards. Wire it to a slide with `PAGE_OVERRIDES` in [src/reef/slideshow.py](src/reef/slideshow.py).

### 7. Tomato polish
The mechanics work, but two things are yours to decide:
- **Appearance.** The tomato is a `recovery_compass` carrying a `profile` component, which does nothing on that base item — it currently renders as a plain recovery compass. Give it an `item_model` and a texture, or change `base_item`. The flying tomato copies whatever the thrower holds, so it follows automatically.
- **Distribution.** Right now `<ns>:tomato/give` hands 8 to everyone. Decide whether people find them, get them at the start, or only during the AI section.

---

## 🟠 Known issue (pre-existing, not blocking)

**Smithed Weld fails on Python 3.14:**

```
[ERROR] Smithed Weld merging failed: no validator found for
<class 'beet.toolchain.config.ListOption[str]'>
```

This only skips the `_with_libs.zip` bundles; the normal datapack and resource pack build and deploy fine. StewBeet suggests the fix:

```
uv pip install git+https://github.com/Stoupy51/smithed-python.git
```

---

## 🔵 Rehearsal and stage day

### 8. Test it in game now

```mcfunction
function summit.stages:permissions/grant_host
```

That gives you `reef.permissions.use_remote`, the stage remote and the stage controls. Then hold the Welded Woodlands remote and **sneak + sprint + right-click** to open the settings dialog → *Load slideshow* → `stoupy_panel:panel`.

Tomatoes:

```mcfunction
function stoupy_panel:tomato/give      # 8 tomatoes to everyone
function stoupy_panel:tomato/clear     # kill switch: splats what is flying and empties every inventory
```

Tomatoes always fly, so there is nothing to arm and nothing to forget. `clear` is the only thing you need if the room gets rowdy.

### 9. Practise the remote until it is muscle memory

| Input | Action |
|---|---|
| Right-click (hold) | **Next** |
| **Sneak** + right-click | **Previous** |
| **Sneak + Sprint** + right-click | Settings dialog |

It is a *consumable* item — "use" means **hold** right-click. Sneak+Sprint is Shift+Ctrl and it is awkward; practise it or you will reverse yourself mid-sentence.

### 10. Time the talk
35 minutes across 6 sections. Run it with a timer at least twice. The AI section is the one that will overrun.

### 11. Stage-day checklist
- [ ] PDF re-exported at 336 x 192 pt
- [ ] Datapack delivered to organisers by their deadline
- [ ] Resource pack delivered (the slides live in it — not optional)
- [ ] `Bookshelf Move.zip` delivered too, or confirm the server already has `bs.move` ≥ 4.1
- [ ] Confirm you have `reef.permissions.use_remote`
- [ ] Confirm `stoupy_panel:panel` loads on their screen
- [ ] Know the recovery path: settings dialog → *Load slideshow* → *Change page*
- [ ] Slides as a normal PDF on hand as a fallback
