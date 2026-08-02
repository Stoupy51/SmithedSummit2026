# Running the panel — step by step

Everything needed to go from a freshly edited PDF to slides on the Welded Woodlands screen.
Library reference in [REEF.md](REEF.md), open decisions in [HUMAN_TODO.md](HUMAN_TODO.md).

---

## The short version

```bash
uv run stewbeet                    # build + deploy to the world and resourcepacks
```

```mcfunction
/reload
/function summit.stages:permissions/grant_host
/loot give @s loot summit.stages:remote/welded_woodlands
```

Hold the remote → **Sneak + Sprint + right-click** → *Load slideshow* → `stoupy_panel:panel` → **right-click** to advance.

---

## 1. Build

```bash
cd panel
uv run stewbeet
```

Faster iteration, using the local beet checkout:

```bash
uv run --with ../../beet stewbeet
```

The build already copies itself where it needs to go — no manual zip juggling:

| Output | Destination |
|---|---|
| `BoostYourProductivity_datapack.zip` | `D:/minecraft/latest/saves/smithed_summit_panels/datapacks/` |
| `BoostYourProductivity_resource_pack.zip` | `D:/minecraft/latest/resourcepacks/` |
| `Bookshelf Move.zip` | same datapacks folder, fetched automatically |

Watch for two lines in the output:

```
[INFO] Registered slideshow 'stoupy_panel:panel' holding 6 slides
```
That is your slide count. If it does not match your deck, the PDF did not re-export.

```
[INFO] Fitted slides from 1440x810 pt to 336x192 pt for Welded Woodlands -> 21x12 blocks
```
Reef sizes the in-game screen from the PDF page size, so the build rescales your export to the stage first. **Export at any page size you like** — 1920x1080 is fine. Only the aspect ratio matters, and only a little: the screen is 7:4, a 16:9 deck loses 1.5 pt (0.09 block) top and bottom. Past a 2% border the build says so.

Enable the resource pack once in Minecraft's options; after that a `/reload` picks up datapack changes, but **resource pack changes need `F3+T`** (or rejoining the world).

---

## 2. Set yourself up in game

```mcfunction
/reload
```

```mcfunction
/function summit.stages:permissions/grant_host
```

That single function gives you `reef.permissions.use_remote`, the `summit.stages.host` tag, the **Stage Remote**, and enables the stage controls. Without `reef.permissions.use_remote` the Reef remote does nothing at all — silently.

Then take the remote already linked to your screen:

```mcfunction
/loot give @s loot summit.stages:remote/welded_woodlands
```

You get a **Linked Remote | Welded Woodlands**. It is pre-bound by tag to `summit.stages.welded_woodlands.screen`, so there is no linking step.

Optional while developing — Reef then narrates what it is doing in chat:

```mcfunction
/tag @s add reef.permissions.see_debug
```

---

## 3. Load the slideshow

Hold the remote and **sneak + sprint + right-click** (Shift + Ctrl + right-click). The settings dialog opens.

1. *Load slideshow* → type `stoupy_panel:panel`
2. *Change page* → `0`

The slideshow id is always `<namespace>:panel`, so `stoupy_panel:panel`. It does not change when you add slides.

---

## 4. Drive the presentation

| Input | Action |
|---|---|
| **Right-click** | Next |
| **Sneak** + right-click | Previous |
| **Sneak + Sprint** + right-click | Settings dialog |

Two things worth internalising before you are in front of people:

- The remote is a **consumable** item, so "use" means **hold** right-click, not tap. You get a short use animation.
- **Sneak + Sprint is Shift + Ctrl**, and it is easy to hit Sneak alone by accident, which sends you *backwards*. Practise it.

"Next" advances the element group first when a slide has several, and only moves to the next slide once the last group is shown. With a PDF deck every slide is a single group, so one click is one slide.

---

## 5. The extras

**Laser pointer** (shipped by Summit, three colours):

```mcfunction
/loot give @s loot summit.laser_pointer:zz/green_laser_pointer
/loot give @s loot summit.laser_pointer:zz/red_laser_pointer
/loot give @s loot summit.laser_pointer:zz/smithed_laser_pointer
```

**Tomatoes** (for the AI section):

```mcfunction
/function stoupy_panel:tomato/give      # 8 tomatoes to everyone not spectating
/function stoupy_panel:tomato/clear     # splats what is flying AND empties every inventory
```

Tomatoes always fly, there is nothing to arm. `clear` is the kill switch — it takes them out of people's hands, so the barrage actually stops.

To fire either of these off a specific slide instead of typing them, add a `PAGE_OVERRIDES` entry in [src/reef/slideshow.py](src/reef/slideshow.py):

```python
PAGE_OVERRIDES: dict[int, PageOverride] = {
	12: PageOverride(on_enter=["function stoupy_panel:tomato/give"], on_unload=["function stoupy_panel:tomato/clear"]),
}
```

Slide indexes are 0-based.

---

## 6. When something breaks

| Symptom | Cause | Fix |
|---|---|---|
| Remote does nothing, no message | Missing permission | `/tag @s add reef.permissions.use_remote` |
| Screen is blank, slideshow gone | Screen was cleared | Remote → settings → *Load slideshow* → `stoupy_panel:panel`, then *Change page* |
| No screen at all | Screen entity removed | `/function summit.stages:resummon_screens` — **resummons every stage screen and drops their slideshows**, so reload yours afterwards |
| Wall is missing / screen hidden | Stage screen toggle is off | Stage Remote → Welded Woodlands → toggle the screen back on |
| Slides look enormous | Fitted copy is stale | Delete `.beet_cache/panel_slides/` and rebuild |
| Slides are the old version | Resource pack not reloaded | `F3+T`, or rejoin the world |
| Slide count is stale | PDF did not re-export | Check the `holding N slides` line in the build output |

Reef's own escape hatches, if the registry ever gets confused:

```mcfunction
/function reef:api/clear_registry
/function stoupy_panel:reef/register_namespace
```

The second one is what the datapack runs on load; running it by hand re-registers the slideshow without a `/reload`.

---

## 7. Every command in one place

```mcfunction
# Setup
/function summit.stages:permissions/grant_host
/loot give @s loot summit.stages:remote/welded_woodlands
/loot give @s loot summit.laser_pointer:zz/green_laser_pointer
/tag @s add reef.permissions.see_debug

# Panel
/function stoupy_panel:tomato/give
/function stoupy_panel:tomato/clear

# Recovery
/function summit.stages:resummon_screens
/function reef:api/clear_registry
/function stoupy_panel:reef/register_namespace
```

Slideshow id: **`stoupy_panel:panel`**
