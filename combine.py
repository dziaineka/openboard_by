import os
import xml.etree.ElementTree as ET


def extract_variants_without_pluses(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    variants_without_pluses = []

    for paradigm in root.findall(".//Paradigm"):
        for variant in paradigm.findall(".//Variant"):
            for form in variant.findall(".//Form"):
                word = form.text.replace("+", "")
                word = f"word={word},f=100,flags=,originalFreq=100"
                variants_without_pluses.append(word)

    return variants_without_pluses


def process_all_files_in_folder(folder_path, output_file_path):
    xml_files = [f for f in os.listdir(folder_path) if f.endswith(".xml")]

    all_variants = []

    for xml_file in xml_files:
        xml_file_path = os.path.join(folder_path, xml_file)
        variants = extract_variants_without_pluses(xml_file_path)
        all_variants.extend(variants)

    with open(output_file_path, "w") as output_file:
        for variant in all_variants:
            output_file.write(variant + "\n")


# Example usage:
folder_path = "./RELEASE-20230920"
output_file_path = "./by_wordlist.combined"
process_all_files_in_folder(folder_path, output_file_path)
