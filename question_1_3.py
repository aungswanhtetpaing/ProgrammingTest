import os
import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file_path):
    xml_file_path = csv_file_path.replace('.csv', '.xml')

    root = ET.Element('bounding_boxes')
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            bbox_element = ET.SubElement(root, 'bounding_box')
            ET.SubElement(bbox_element, 'x').text = str(float(row[0]))
            ET.SubElement(bbox_element, 'y').text = str(float(row[1]))
            ET.SubElement(bbox_element, 'width').text = str(float(row[2]))
            ET.SubElement(bbox_element, 'height').text = str(float(row[3]))
            ET.SubElement(bbox_element, 'tag').text = row[4]

    xml_tree = ET.ElementTree(root)
    xml_tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

def convert_csv_to_xml_in_folder(folder_path):
    abs_folder_path = os.path.abspath(folder_path)
    for root, _, files in os.walk(abs_folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                csv_file_path = os.path.join(root, filename)
                csv_to_xml(csv_file_path)
                
if __name__ == "__main__":
    folder_path = "gw_test/Question1/Dataset"
    convert_csv_to_xml_in_folder(folder_path)
