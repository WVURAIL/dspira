#!/usr/bin/env python3
"""Export the three assembly Word guides as website includes and illustrations."""

import argparse
from hashlib import sha256
from html import escape
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
GUIDES = {
    "horn-and-can-assembly-2021": [
        "assembled-horn", "panel-dimensions", "panel-cutting-layout", "panel-seams",
        "copper-probe", "drilled-can", "attached-feedthrough", "horn-flashing",
        "can-flashing", "sealed-horn-interior",
    ],
    "cradle-assembly-2021": ["cradle-dimensions", "assembled-cradle"],
    "stand-assembly-2021": ["stand-notches", "stand-braces", "assembled-stand"],
}
# These references describe paper pages, whose positions change on the website.
WEB_TEXT = {
    "Use the layout on the next page.": "Use the cutting layout below.",
    "Use the dimensions on the preceding page, not the drawing scale.":
        "Use the panel dimensions above, not the drawing scale.",
    "from left to right": "in order",
    "as shown at left in Figure 6": "as shown in the first photograph in Figure 6",
    "Braced frame (left). Figure 3. Stand with the horn telescope attached (right).":
        "Braced frame (first photograph). Figure 3. Stand with the horn telescope attached (second photograph).",
}


def text_of(element):
    return "".join(node.text or "" for node in element.findall(".//w:t", NS)).strip()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def export_guide(root, name, image_names):
    source = root / "assets/lessons/horn-construction" / (name + ".docx")
    prefix = name.split("-assembly")[0]
    blocks, assets, image_index = [], {}, 0
    current_list = None
    heading_ids = set()

    def close_list():
        nonlocal current_list
        if current_list:
            blocks.append(f"</{current_list}>")
            current_list = None

    with ZipFile(source) as package:
        doc = ET.fromstring(package.read("word/document.xml"))
        relations = {
            node.attrib["Id"]: node.attrib["Target"]
            for node in ET.fromstring(package.read("word/_rels/document.xml.rels"))
        }

        def inline(element):
            parts = []
            for node in element:
                tag = node.tag.rsplit("}", 1)[-1]
                if tag == "r":
                    value = escape("".join(t.text or "" for t in node.findall(".//w:t", NS)))
                    if node.find("w:rPr/w:b", NS) is not None:
                        value = f"<strong>{value}</strong>" if value else ""
                    parts.append(value)
                elif tag == "hyperlink":
                    target = relations[node.attrib[f"{{{NS['r']}}}id"]]
                    if "cradle-assembly-2021.pdf" in target:
                        target = "#cradle"
                    if not target.startswith(("https://", "http://", "#")):
                        raise ValueError(f"Unsupported link in {name}: {target}")
                    parts.append(f'<a href="{escape(target, quote=True)}">{inline(node)}</a>')
            value = "".join(parts)
            for old, new in WEB_TEXT.items():
                value = value.replace(escape(old), escape(new))
            return value

        for element in doc.find("w:body", NS):
            if element.tag == f"{{{NS['w']}}}sectPr":
                continue
            if element.tag == f"{{{NS['w']}}}tbl":
                close_list()
                rows = element.findall("w:tr", NS)
                blocks.append("<table>\n<thead>")
                for index, row in enumerate(rows):
                    cells = row.findall("w:tc", NS)
                    blocks.append("<tr>" + "".join(
                        ("<th scope=\"col\">" if index == 0 else "<td>")
                        + "<br>".join(inline(p) for p in cell.findall("w:p", NS))
                        + ("</th>" if index == 0 else "</td>") for cell in cells
                    ) + "</tr>")
                    if index == 0:
                        blocks.append("</thead>\n<tbody>")
                blocks.append("</tbody>\n</table>")
                continue
            if element.tag != f"{{{NS['w']}}}p":
                raise ValueError(f"Unsupported document element: {element.tag}")
            style_node = element.find("w:pPr/w:pStyle", NS)
            style = style_node.attrib[f"{{{NS['w']}}}val"] if style_node is not None else ""
            if style in ("Title", "Subtitle"):
                continue
            value = inline(element).strip()
            drawings = element.findall(".//w:drawing", NS)
            if drawings:
                close_list()
                blocks.append('<div class="assembly-figures">')
                for drawing in drawings:
                    if drawing.find(".//a:srcRect", NS) is not None:
                        raise ValueError("Cropped images need an explicit web export")
                    props = drawing.find(".//wp:docPr", NS)
                    alt = re.sub(r"^Figure \d+\.\s*", "", props.attrib.get("descr", ""))
                    if not alt:
                        raise ValueError(f"Missing image description in {name}")
                    rid = drawing.find(".//a:blip", NS).attrib[f"{{{NS['r']}}}embed"]
                    member = "word/" + relations[rid]
                    filename = image_names[image_index] + Path(member).suffix.lower()
                    image_index += 1
                    image_path = Path("images/horn-construction/assembly") / filename
                    data = package.read(member)
                    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
                        raise ValueError(f"Add dimension handling for the new image format: {member}")
                    width, height = struct.unpack(">II", data[16:24])
                    assets[image_path] = data
                    blocks.append(
                        '<figure><img src="{{ \'' + '/' + image_path.as_posix()
                        + '\' | relative_url }}" alt="' + escape(alt, quote=True)
                        + f'" width="{width}" height="{height}"></figure>'
                    )
                blocks.append("</div>")
            if not value:
                continue
            if style.startswith("Heading"):
                close_list()
                level = int(style[-1]) + (2 if prefix in ("cradle", "stand") else 1)
                heading_id = prefix + "-" + slug(text_of(element))
                if heading_id in heading_ids:
                    raise ValueError(f"Duplicate heading: {heading_id}")
                heading_ids.add(heading_id)
                blocks.append(f'<h{level} id="{heading_id}">{value}</h{level}>')
            elif style == "Caption":
                close_list()
                blocks.append(f'<p class="assembly-caption">{value}</p>')
            else:
                numbered = re.match(r"^\d+\.\s+", value)
                list_type = "ol" if style == "ListNumber" or numbered else "ul" if style == "ListBullet" else None
                if current_list != list_type:
                    close_list()
                if list_type and not current_list:
                    blocks.append(f"<{list_type}>")
                    current_list = list_type
                if numbered:
                    value = value[numbered.end():]
                blocks.append(f"<li>{value}</li>" if list_type else f"<p>{value}</p>")
        close_list()
    if image_index != len(image_names):
        raise ValueError(f"Image list needs updating for {name}")
    source_hash = sha256(source.read_bytes()).hexdigest()
    header = f"<!-- Generated from {source.relative_to(root).as_posix()}; SHA256 {source_hash}. -->\n"
    assets[Path("_includes/assembly") / (name + ".html")] = (header + "\n".join(blocks) + "\n").encode()
    return assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed exports need updating")
    args = parser.parse_args()
    files = {}
    for name, image_names in GUIDES.items():
        files.update(export_guide(ROOT, name, image_names))
    outdated = []
    for relative, data in files.items():
        path = ROOT / relative
        if args.check:
            actual = path.read_bytes() if path.is_file() else b""
            if path.suffix == ".html":
                actual = actual.replace(b"\r\n", b"\n")
            if actual != data:
                outdated.append(str(relative))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    if outdated:
        raise SystemExit("Run python3 tools/export_assembly_guides.py:\n" + "\n".join(outdated))
    print(f"{'Checked' if args.check else 'Exported'} {len(GUIDES)} guides and {len(files) - len(GUIDES)} illustrations.")


if __name__ == "__main__":
    main()
