# Reef — Reference for the Smithed Summit 2026 Panel

Everything needed to build and present the "Boost Your Productivity" panel with Reef.
Researched 2026-08-02 from the wiki, the plugin source, the `reef_summit` demo pack, and the real `summit-dp-core-v3171` datapack.

---

## 1. Hard numbers for this panel

| Fact | Value |
|---|---|
| Stage (inferred from `336 x 192`) | **Welded Woodlands** |
| Slide page size | **336 x 192 pt** (aspect **7:4** = 1.75) |
| In-game screen size | **21 x 12 blocks** (336/16 x 192/16) |
| Screen entity | `239.9 81.0 1.0` rotated `90 0` |
| Screen wall region | `fill 240 64 1 241 80 21` → 21 blocks along +Z |
| Screen entity tags | `summit.stages.screen`, `summit.stages.welded_woodlands.screen` |
| Reef data pack version present on the day | **1.1.0** (environment `summit`) |
| Reef Beet plugin version | **1.0.0b7** (2026-07-29) |
| Minecraft | `26.2` — data pack format `[107,1]`, resource pack format `[88,0]` |
| Python | `>=3.14` |

**All four Summit stages**, from the official templates (`other_packs/reef_summit/src/assets/reef_summit/reef/pdf/`):

| Stage | Page size (pt) | Blocks |
|---|---|---|
| Patched Plateaus — main | 546 x 269 | 34.125 x 16.8125 |
| Patched Plateaus — side | 273 x 167 | 17.0625 x 10.4375 |
| Textured Tropics | 400 x 224 | 25 x 14 |
| **Welded Woodlands** | **336 x 192** | **21 x 12** |

> The `Trioplane/reef-pdf-template` repo ships the *Patched Plateaus main* template (546 x 269).
> If you use that repo as a starting point, **replace the PDF and the page size** with the Welded Woodlands one.

---

## 2. What Reef is

Reef is a slideshow / presentation library for **vanilla Minecraft: Java Edition**, by [@trplnr](https://github.com/trplnr) (co-author [@rx-dev](https://github.com/rx-dev)), built for Smithed Summit 2026.

Two separate pieces:

1. **The data pack + resource pack library** — runtime. Summons *screens*, plays *transitions*, spawns *elements*, provides the *remote*. Already bundled in the Summit datapack.
2. **The Beet plugin (`reef-beet-plugin`)** — build time. Turns declarative JSON (and PDFs) into the register functions, models, item model definitions and textures. Writing definitions by hand is possible but tedious; the wiki itself says use the plugin.

---

## 3. Geometry and the coordinate system

This is the part the docs do not explain, and it is the thing you will fight with. Derived from the plugin source and confirmed against `reef_summit`'s own decks and the real stage wall dimensions.

### 3.1 The element base model

`reef:item/element_base` is a **1 x 1 model-pixel quad** (`from [0,0,0]` `to [1,1,0]`), unshaded, `light_emission: 15` (fullbright — slides are not affected by world light), single north face with `tintindex: 0`.

Every graphic is that quad, scaled up by a `transformation` matrix in the item model definition:

```
[ W, 0, 0, 0.5 - W/16 ]
[ 0, H, 0, 0.5 - H/16 ]
[ 0, 0, 1, 0.5        ]
[ 0, 0, 0, 1          ]
```

where `W`/`H` are the element `size` in **model pixels** (= PDF points, 1:1).

### 3.2 The rule that matters

> **1 pt = 1 model pixel = 1/16 block.**
> **Element origin is the TOP-LEFT corner. +X goes right, −Y goes DOWN, +Z goes toward the audience.**

So an element placed at `"pos": [0, 0, 0]` occupies `x ∈ [0, W/16]` and `y ∈ [-H/16, 0]` in blocks.

### 3.3 Welded Woodlands cheat sheet (336 x 192 → 21 x 12 blocks)

| Anchor | `pos` |
|---|---|
| Top-left | `[0, 0, 0]` |
| Top-right | `[21, 0, 0]` |
| **Centre** | **`[10.5, -6, 0]`** |
| Bottom-left | `[0, -12, 0]` |
| Bottom-right | `[21, -12, 0]` |
| Title line (upper third) | `[10.5, -4, 0]` |
| Body start | `[10.5, -6, 0]`, then step `-1` per line at `scale [3,3,1]` |

Evidence this is right — `reef_summit`'s own 528x288 (33x18 block) deck puts its centred title at `[16.5, -9, 0]`, which is exactly `(33/2, -18/2)`.

### 3.4 Z-fighting

Backgrounds go **behind** at `"pos": [0, 0, -0.01]`; text and foreground sit at `z = 0`. Every single `reef_summit` page does this. Copy it.

### 3.5 DPI and texture resolution

`pixels = points x (dpi / 72)`.

| dpi | Texture for 336x192 | px per block | Note |
|---|---|---|---|
| 144 | 672 x 384 | 32 | **Use this.** 2x vanilla, clean integers, what every Summit template uses. |
| 216 | 1008 x 576 | 48 | 3x, sharper, heavier |
| 200 (plugin default) | 933.3 x 533.3 | — | **Non-integer — avoid.** Always pick a multiple of 72. |

---

## 4. The Beet plugin

### 4.1 Install

```toml
# pyproject.toml
requires-python = ">=3.14"
dependencies = ["beet>=0.116.0", "reef-beet-plugin>=1.0.0b7"]
```

Transitive deps: `beet`, `odfdo`, `pdf2image`. **`pdf2image` needs the Poppler binaries** (`pdftoppm`, `pdfinfo`) — they are *not* pip-installable on Windows. See [HUMAN_TODO.md](HUMAN_TODO.md).

### 4.2 beet.yml configuration

```yaml
require:
    - "reef"          # must be present for the .pdf / reef JSON handlers to register
    - "stewbeet"

meta:
    reef:
        tint: null              # optional constant tint applied to every generated element
        compress_functions: false   # true = all register code in one function per namespace
        cache_timeout_hours: 24
        pdf:
            dpi: 144            # keep a multiple of 72
            poppler_path: null  # absolute path to poppler's bin/ if not on PATH
        odp:
            cm_per_block: 1     # ODP/Google Slides support — CURRENTLY DISABLED in the plugin
```

All options and defaults, from `options.py`:

| Option | Default | Meaning |
|---|---|---|
| `tint` | `None` | Constant colour multiplied into every element. `None` = no `tints` field emitted. |
| `compress_functions` | `False` | `False` → one function per definition + a dispatcher. `True` → everything inlined into `<ns>:reef/register_namespace`. |
| `cache_timeout_hours` | `24` | PDF page-image cache lifetime. |
| `pdf.dpi` | `200` | Rasterisation DPI. |
| `pdf.poppler_path` | `None` | Poppler `bin/` directory. |
| `odp.cm_per_block` | `1` | ODP only. |

Changing any option **invalidates the PDF cache** automatically.

### 4.3 File layout the plugin watches

Source files are **consumed and dropped** — none of them appear in the built pack. They only generate other files.

**Data pack** (`src/data/<ns>/reef/...`):

| Path | Type | Generates |
|---|---|---|
| `reef/special/<name>.json` | PDF / item-model slideshow | pages + slideshow (or a Reef Mini registration) |
| `reef/slideshow/<name>.json` | page list | `<ns>:reef/register/slideshow/<name>` |
| `reef/page/<name>.json` | page | `<ns>:reef/register/page/<name>` |
| `reef/transition/<name>.json` | transition | `<ns>:reef/register/transition/<name>` |

**Resource pack** (`src/assets/<ns>/reef/...`):

| Path | Type | Generates |
|---|---|---|
| `reef/pdf/<name>.pdf` | the PDF itself | one texture + model per page, plus one `range_dispatch` item model at `<ns>:reef/mini/<name>` |
| `reef/element/<name>.json` | graphic / animated element | model(s) + item model definition at `<ns>:<name>` |

### 4.4 The generated entry point — DO NOT MISS THIS

The plugin creates **`<ns>:reef/register_namespace`** and **attaches it to nothing**. Nothing calls it for you.

> **You must call `function stoupy_panel:reef/register_namespace` from your load function**, or no slideshow will exist in-game.

Definitions are written to storage `<ns>:reef` under `register.page."<id>"` / `register.slideshow."<id>"` / etc., then handed to `reef:api/register/*`. Reef's own registry lives in `reef.zzzinternals:registry`.

---

## 5. Definition schemas

### 5.1 Slideshow — `reef/slideshow/<name>.json`

A flat list of page identifiers, in order. The same page may repeat (useful for a recurring wordmark or blank).

```json
[
    "stoupy_panel:intro",
    "stoupy_panel:who_am_i",
    "stoupy_panel:explore_code"
]
```

### 5.2 Page — `reef/page/<name>.json`

```typescript
type Page = {
    commands?: { on_load?: string[]; on_enter?: string[]; on_unload?: string[] };
    transition?: ResourceLocation;
    sequence: Element[][];   // REQUIRED, double-nested
}
```

`sequence` is a **list of element groups**. Group 0 shows when the page opens; each subsequent "next" reveals the next group *without changing page* — this is Reef's build/appear animation. Only when the last group is shown does "next" advance to the next page.

### 5.3 Elements

Shared optional fields on every element type:

| Field | Type | Note |
|---|---|---|
| `pos` | `[x, y, z]` | Top-left anchored, −Y is down |
| `translation` | `[x, y, z]` | Display-entity transform |
| `scale` | `[x, y, z]` | `[5,5,1]` title, `[3,3,1]` body in the demo deck |
| `left_rotation` | quaternion `[x,y,z,w]` or `{angle, axis}` | |
| `right_rotation` | same | |
| `components` | item component map | |
| `commands` | `{ on_enter?: string[]; on_exit?: string[] }` | |

Type-specific:

| `type` | Extra fields |
|---|---|
| `graphic` | `model` (ResourceLocation) |
| `animated_graphic` | `model`, `frames` (int) |
| `text` | `text` (TextComponent), `background?` (int ARGB), `alignment?` `"left"\|"center"\|"right"`, `line_width?` (int) |

Real example (`reef_summit`, 33x18 screen):

```json
{
    "transition": "reef_summit:smithed_slide_up",
    "sequence": [
        [
            { "type": "graphic", "model": "reef_summit:onboarding_demo/yellow_gradient", "pos": [0, 0, -0.01] },
            { "type": "text", "text": {"text": "Text Elements", "color": "black"}, "pos": [16.5, -6, 0], "scale": [5, 5, 1] }
        ],
        [
            { "type": "text", "text": {"text": "Normal boring text", "color": "black"}, "pos": [16.5, -12, 0], "line_width": 200, "scale": [3, 3, 1] }
        ],
        [
            { "type": "text", "text": {"text": "Ooooo I have a background", "color": "white"}, "background": -13348117, "pos": [16.5, -14, 0], "line_width": 200, "scale": [3, 3, 1] }
        ]
    ]
}
```

### 5.4 Transition — `reef/transition/<name>.json`

```json
{ "frames": 21, "switch_frame": 11, "model": "reef_summit:smithed_slide_up" }
```

| Field | Meaning |
|---|---|
| `frames` | Total length in ticks/frames |
| `switch_frame` | Frame at which the page actually swaps — set it to where the screen is fully covered |
| `model` | Item model of the animated overlay (usually a `reef:animated_element`) |

Reef pre-summons one transition-layer entity per screen, tagged `reef.element.transition`.

### 5.5 Element assets — `assets/<ns>/reef/element/<name>.json`

```json
{ "type": "reef:graphic",          "texture": "ns:item/reef/graphic/bg", "size": [336, 192] }
{ "type": "reef:animated_element", "texture": "ns:item/reef/anim/foo",   "size": [128, 64], "frames": 37 }
```

`size` is in points/model-pixels — same unit as PDF points. For `reef:animated_element`, frame `i` reads texture `<texture>/<i>` for `i` in `1..frames`; **frame 0 is forced to `minecraft:air`** (so frame indices are 1-based).

### 5.6 Special — `reef/special/<name>.json` (the PDF path)

```json
{
    "type": "reef:pdf",
    "pdf": "stoupy_panel:panel_slides",
    "page_count": 42,
    "transition": "stoupy_panel:my_transition",
    "overrides": {
        "0": { "commands": { "on_enter": ["tellraw @a 'first slide'"] } }
    }
}
```

| Field | Required | Meaning |
|---|---|---|
| `type` | yes | `"reef:pdf"` or `"reef:item_model"` |
| `pdf` | yes (pdf) | Points at `assets/<ns>/reef/pdf/<path>.pdf` |
| `item_model` | yes (item_model) | Points at `assets/<ns>/items/<path>` |
| `page_count` | yes | **Must match the real page count** — nothing validates this |
| `transition` | no | Applied to every generated page |
| `overrides` | no | `{"<page index>": Page}` — page indices are **0-based, string keys, digits only** |

**The `overrides` key flips the whole codegen path:**

- **Without `overrides`** → registers a *Reef Mini* (compact, one registration, model `<ns>:reef/mini/<path>`).
- **With `overrides`** → expands into `page_count` real Page files + a Slideshow, each page holding one `graphic` element with `custom_model_data.floats = [i]` selecting the PDF page.

Both are addressable by the same slideshow id `<ns>:<name>`.

---

## 6. In-game usage

### 6.1 Screens

A screen is an `item_display` tagged `reef.screen`. It is the anchor; it has no size of its own.

```mcfunction
execute positioned 239.9 81.0 1.0 rotated 90 0 run function reef:api/screen/summon {tags: ["my.screen"]}
```

- `summon` is a **macro function** — the `{tags: [...]}` argument is **mandatory**. Pass `{tags: []}` if you want none. (The wiki's getting-started example omits it and is wrong.)
- **Position and rotation are fixed at summon time.** To move it you must `reef:api/screen/remove` and re-summon.
- To rotate afterwards, edit the entity's `Rotation` tag — **never** its `transformation`.
- Multiple independent screens per world are supported.

### 6.2 Screen API

| Function | Context | Notes |
|---|---|---|
| `reef:api/screen/summon` | positioned + rotated | macro, needs `tags` |
| `reef:api/screen/set_page` | `as <screen>` | macro, needs `page` (0-based) |
| `reef:api/screen/next` | `as <screen>` | advances element group first, then page |
| `reef:api/screen/prev` | `as <screen>` | |
| `reef:api/screen/clear` | `as <screen>` | kills elements, keeps the screen + transition layer |
| `reef:api/screen/remove` | `as <screen>` | destroys everything |

All of these `return fail` if no slideshow is loaded or a transition is still playing.

### 6.3 Register API

| Function | Macro args |
|---|---|
| `reef:api/register/slideshow` | `identifier`, `storage_path` |
| `reef:api/register/page` | `identifier`, `storage_path` |
| `reef:api/register/transition` | `identifier`, `storage_path` |
| `reef:api/register/mini` | `identifier`, `storage_path` |
| `reef:api/clear_registry` | — |

`storage_path` is `"<storage id> <nbt path>"`, e.g. `'stoupy_panel:reef register.page."stoupy_panel:intro"'`.

### 6.4 The remote — **the controls you will actually use on stage**

Get one: `loot give @s loot reef:remote` (a re-skinned `poisonous_potato`, `consumable` with `consume_seconds: 9999999`, so "use" = **hold right-click**).

An **unlinked** remote right-clicked opens a link dialog (link by **screen ID** or by **screen tags**, comma-separated, no quotes).

A **linked** remote (detected via `input` predicates on the player):

| Input | Action |
|---|---|
| **Right-click** | **next** (next element group, else next page) |
| **Sneak + right-click** | **prev** |
| **Sneak + sprint + right-click** | **open the slideshow settings dialog** |

The settings dialog offers *load slideshow*, *change page*, *clear screen*, *remove screen*, *unlink remote*.

> Debounced by a `reef.item.linked_remote.clicked_this_tick` tag, so a held right-click does not spam. But it *is* a hold-to-use item — expect a use animation.

### 6.5 Permissions

| Tag | Grants |
|---|---|
| `reef.permissions.use_remote` | Remote functions + dialogs. **Required or the remote does nothing.** |
| `reef.permissions.see_debug` | Reef's chat logging, screen-summon particles/sound |

`/tag <player> add reef.permissions.use_remote`

### 6.6 Uninstall

`function reef:uninstall`, then remove the data pack. Does **not** remove already-loaded screens.

---

## 7. Summit-day specifics

The Summit datapack (`summit-dp-core-v3171-do-not-share.zip`) bundles **Reef 1.1.0**, slightly patched (screens also get a `summit.static` tag).

- `summit.stages:resummon_screens` deletes and re-summons all five stage screens.
- `summit.stages:permissions/grant_host` gives `reef.permissions.use_remote` + `summit.stages.host` + the Stage Remote and enables stage controls.
- **A laser pointer already exists** — `summit.laser_pointer`, a `carrot_on_a_stick` with a distance-scaled dot, in three colours. Do not build another one.
  `loot give @s loot summit.laser_pointer:zz/green_laser_pointer` (also `red_` and `smithed_`).
- Per-stage pre-linked remotes exist as loot tables, e.g. `summit.stages:remote/welded_woodlands` → a Linked Remote bound by tag to `summit.stages.welded_woodlands.screen`.
- `summit.stages:controls/welded_woodlands/hide_screen/enable` clears the screen and fills the wall with air.

**You will most likely be handed a pre-linked "Linked Remote | Welded Woodlands".** You do not need to summon a screen or link anything yourself — you need your slideshow *registered* so it can be loaded onto their screen.

---

## 8. Gotchas

1. **`register_namespace` is never called automatically.** Call it from your load function. (§4.4)
2. **`reef:api/screen/summon` requires `{tags: ...}`** — it is a macro function; calling it bare errors.
3. **Poppler is a hard native dependency** of `pdf2image`. Not on PATH here.
4. **`page_count` is not validated** against the PDF. Wrong value = missing or blank slides.
5. **`overrides` keys must be digit-only strings.** The `reef-pdf-template` ships a literal `"<page_number>"` placeholder key with `_1`/`_2`/`_3` notes — that **fails pydantic validation** (`^[0-9]*$`). Delete the placeholder block before building.
6. **`overrides[i].sequence` must contain exactly one element group.** `special.py` does `page["sequence"].append(*page_override["sequence"])` — `list.append` takes one argument, so zero or two-plus groups raise `TypeError`. Bug in 1.0.0b7; work around it by putting everything in one group.
7. **Use a DPI that is a multiple of 72**, otherwise page pixel dimensions are fractional.
8. **`odp` (ODP / Google Slides) is disabled** — `ctx.require(data.odp)` is commented out in `plugin.py` with `# CURRENTLY UNSTABLE!`. PDF is the only supported import path.
9. **If graphics render black or mis-tinted**, set `meta.reef.tint`. The base model face carries `tintindex: 0`, and no `tints` entry is emitted unless `tint` is set. `16777215` (`0xFFFFFF`) is the neutral value.
10. **Z-fight**: always push backgrounds to `z = -0.01`.
11. **Animated element frames are 1-based**; frame 0 is `minecraft:air`.
12. **Screens cannot be moved.** Pick the position once.
13. **Reef source files never reach the build output** — they all `raise Drop()`. If you see your `.json` in `build/`, the handler did not run (check `require: ["reef"]`).

---

## 9. How this project wires it up

The generic advice above is implemented in [src/reef/](src/reef/). Two files, no hand-written JSON:

| File | Role |
|---|---|
| [src/reef/stages.py](src/reef/stages.py) | `Stage` dataclass and the table of all four Summit stages. `TARGET_STAGE` picks ours. |
| [src/reef/slideshow.py](src/reef/slideshow.py) | Reads the PDF, validates its page size, registers it, generates the slideshow, hooks the load chain. |

What the build does on every run:

1. Reads `How to Boost your Productivity.pdf` from the project root with `pypdf`.
2. **Rescales it to `TARGET_STAGE`'s page size**, preserving aspect and centring, into `.beet_cache/panel_slides/`. Only redone when the export actually changed, since rasterizing is the slow part. Export at any page size.
3. Registers that fitted copy as `stoupy_panel:panel`, generating one texture, model and item-model entry per slide.
4. Emits `data/stoupy_panel/reef/special/panel.json` with the **page count read from the PDF**, so adding slides needs no code change.
5. Appends `function stoupy_panel:reef/register_namespace` to `confirm_load`.

Result in game: slideshow id **`stoupy_panel:panel`**.

Per-slide commands go in `PAGE_OVERRIDES` in [src/reef/slideshow.py](src/reef/slideshow.py), keyed by 0-based slide index:

```python
PAGE_OVERRIDES: dict[int, PageOverride] = {
	12: PageOverride(on_enter=["function stoupy_panel:tomato/give"], on_unload=["function stoupy_panel:tomato/clear"]),
}
```

While that dict is empty the deck compiles to a lighter Reef Mini; adding an entry switches it to full page definitions. Only `commands` are exposed, which sidesteps gotcha #6 entirely.

---

## 10. Sources

- Wiki — https://github.com/Trioplane/reef/wiki (`installation`, `getting_started`, `writing_definitions`, `api`, `permission_system`, `definition_schemas`; the element-model and Beet-plugin pages are still empty stubs)
- Source monorepo — https://github.com/Trioplane/reef (`main/src/data/reef/modules/api.bolt`, `packages/reef/src/reef/*`, `other_packs/reef_summit/*`)
- PyPI — https://pypi.org/project/reef-beet-plugin/ (1.0.0b7, MIT, `>=3.14`)
- Template — https://github.com/Trioplane/reef-pdf-template
- Modrinth — https://modrinth.com/datapack/reef-slideshow-library
- Local ground truth — `D:\minecraft\latest\saves\smithed_summit_panels\datapacks\summit-dp-core-v3171-do-not-share.zip`
