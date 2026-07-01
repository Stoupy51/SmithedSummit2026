""" The link subsystem for presentation walls.

text_display entities don't fire click events in-world, so any page that contains
a link() is backed by an interaction entity that opens a `multi_action` dialog; in
that dialog each link becomes a real, clickable button (dialogs honour clicks).

This module owns both ends: the link() text component used inside page content, and
the dialog + prompt builders the wall builder summons around the nav arrows. Social
-platform glyphs come from the custom `summit_icons` font shipped by the Summit event.
"""

# Imports
from typing import Any, cast

from stewbeet import TextComponent
from stouputils.typing import JsonDict

# Social-platform glyphs from the custom "summit_icons" font, keyed by URL host.
SOCIAL_ICONS: dict[str, str] = {
	"github.com": "github",
	"smithed.dev": "smithed",
	"modrinth.com": "modrinth",
	"curseforge.com": "curseforge",
	"discord.gg": "discord",
	"discord.com": "discord",
	"youtube.com": "youtube",
	"youtu.be": "youtube",
	"twitch.tv": "twitch",
	"twitter.com": "twitter",
	"x.com": "twitter",
	"bsky.app": "bluesky",
	"instagram.com": "instagram",
	"ko-fi.com": "kofi",
	"patreon.com": "patreon",
	"planetminecraft.com": "planetminecraft",
	"mapverse": "mapverse",
}

def social_icon(key: str) -> JsonDict:
	""" A single glyph from the custom 'summit_icons' font (e.g. key='github'). """
	return {"font": "summit_icons:icons", "translate": f"summit_icons.{key}"}

def icon_for_url(url: str) -> str | None:
	""" The summit_icons key matching a URL's host, or None if we have no glyph. """
	for fragment, key in SOCIAL_ICONS.items():
		if fragment in url:
			return key
	return None

def link(label: str, url: str, color: str = "#8BE9FD") -> TextComponent:
	""" A colored, underlined link, prefixed with its platform's social icon when
	we have one. text_display entities don't fire click events in-world, so the wall
	builder backs every page that contains a link with an interaction entity that
	opens a dialog; there the same label is a real, clickable button.

	Returns a nested list component starting with an empty parent so the icon's
	custom font doesn't leak onto the label (siblings inherit from the parent). """
	label_component: JsonDict = {
		"text": label, "color": color, "underlined": True,
		"click_event": {"action": "open_url", "url": url},
		"hover_event": {"action": "show_text", "value": f"Open {url}"},
	}
	key: str | None = icon_for_url(url)
	if key is None:
		return ["", label_component]
	return ["", social_icon(key), {"text": " "}, label_component]


# ── Click -> dialog (used by the wall builder) ───────────────────────────────
# A centered interaction between the nav arrows opens a dialog listing every link
# on the current page; each entry is a real button that opens the URL in a browser.

def collect_links(node: Any) -> list[tuple[str, str]]:
	""" Walk a text component (nested lists included) and return every (label, url)
	pair carried by an open_url click_event, in reading order. """
	found: list[tuple[str, str]] = []
	if isinstance(node, list):
		for child in node:  # type: ignore[reportUnknownVariableType]
			found += collect_links(child)
	elif isinstance(node, dict):
		component = cast(dict[str, Any], node)
		event = component.get("click_event")
		if isinstance(event, dict):
			event = cast(dict[str, Any], event)
			if event.get("action") == "open_url":
				url: str = str(event.get("url", ""))
				found.append((str(component.get("text", url)), url))
	return found

def link_button_label(label: str, url: str) -> TextComponent:
	""" Dialog button label: the platform icon (when known) followed by the text.
	Starts with an empty parent so the icon's custom font doesn't leak onto the
	label (in a component list, siblings inherit from the first element). """
	text: JsonDict = {"text": label, "color": "#8BE9FD"}
	key: str | None = icon_for_url(url)
	return ["", social_icon(key), {"text": " "}, text] if key else [text]

def link_dialog(title: str, subtitle: str, links: list[tuple[str, str]]) -> JsonDict:
	""" A multi_action dialog with one open_url button per link on the page. """
	return {
		"type": "minecraft:multi_action",
		"title": {"text": title, "bold": True, "color": "#FFD479"},
		"body": [{
			"type": "minecraft:plain_message", "width": 240,
			"contents": {"text": subtitle, "color": "gray"},
		}],
		"columns": 1,
		"actions": [{
			"label": link_button_label(label, url),
			"tooltip": {"text": url, "color": "gray"},
			"width": 240,
			"action": {"type": "open_url", "url": url},
		} for label, url in links],
		"exit_action": {"label": {"text": "Close", "color": "red"}},
		"can_close_with_escape": True,
	}

def link_hint(links: list[tuple[str, str]]) -> list[JsonDict]:
	""" The centered under-arrows prompt: platform icon + 'Open link' when the page
	has a link (with a '+N' when it has several), otherwise nothing. """
	if not links:
		return [{"text": ""}]
	key: str | None = icon_for_url(links[0][1])
	parts: list[JsonDict] = [social_icon(key), {"text": " "}] if key else []
	parts.append({"text": "Open link", "color": "#8BE9FD", "underlined": True})
	if len(links) > 1:
		parts.append({"text": f" (+{len(links) - 1})", "color": "gray"})
	return parts

