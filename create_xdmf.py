import os
import sys
import h5py
import lxml.etree as etree


def process_file(filename):
    f = h5py.File(filename, "r")
    groups = list(f.keys())

    # if not (
    #     "Config" in groups and \
    #     "Header" in groups # and \
    #     # "PartType0" in groups
    # ):
    #     print(f"[ERROR] looks like it is not Arepo output file: {filename}")
    #     return

    Domain = etree.Element("Domain")
    #if f["Config"].attrs["DOUBLEPRECISION"] == 1.0:
    #    precision = "8"
    #else:
    #    precision = "4"
    precision = "8"

    for group_name in groups:
        if not group_name.startswith("PartType"):
            continue

        group = f[group_name]
        Grid = etree.SubElement(Domain, "Grid", GridType="Uniform", Name=group_name)
        for name, data in group.items():
            # TODO do smth with hdf5 attributes (data.attrs)
            num_elements = data.shape[0]
            if len(data.shape) == 1:
                dims = f"{num_elements} 1"
                attribute_type = "Scalar"
            elif len(data.shape) == 2:
                dims = f"{num_elements} {data.shape[1]}"
                attribute_type = "Vector"
            else:
                print(f"[ERROR] invalid shape of dataset in file {filename}")
                continue

            path = os.path.basename(filename)
            if name == "Coordinates":
                Topology = etree.SubElement(Grid, "Topology", NumberOfElements=str(num_elements), TopologyType="PolyVertex", NodesPerElement="1")
                Geometry = etree.SubElement(Grid, "Geometry", GeometryType="XYZ")
                DataItem = etree.SubElement(Geometry, "DataItem", Dimensions=dims, Format="HDF", Precision=precision)
                DataItem.text = f"{path}:{group.name}/Coordinates"
            else:
                Attribute = etree.SubElement(Grid, "Attribute", Name=f"{group_name} {name}", AttributeType=attribute_type, Center="Node")
                DataItem = etree.SubElement(Attribute, "DataItem", Dimensions=dims, Format="HDF", Precision=precision)
                DataItem.text = f"{path}:{group.name}/{name}"

    raw_filename = os.path.splitext(filename)[0]
    with open(raw_filename+".xdmf", "w") as out_file:
        contents = '<?xml version="1.0"?>\n<!DOCTYPE Xdmf SYSTEM "Xdmf.dtd" []>\n<Xdmf Version="3.0" xmlns:xi="http://www.w3.org/2001/XInclude">\n'
        contents += etree.tostring(Domain, pretty_print=True).decode("utf-8")
        contents += "</Xdmf>"
        out_file.write(contents)
    print(f"[INFO] {filename} done")


def print_usage():
    usage = f"""
[USAGE]
python {os.path.basename(__file__)} [path]
.xdmf file(s) will be created in the same directory.
.xdmf files must be in the same directory with its .hdf5 file.
"""
    print(usage)

def handle_error(message):
    print("[ERROR] " + message)
    print_usage()
    exit(-1)


if __name__ == "__main__":
    if len (sys.argv) == 1:
        path = "."
    elif len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        handle_error("Invalid command line arguments")
    path = path.replace("~", os.path.expanduser("~"))
    if not os.path.exists(path):
        handle_error("Path does not exist")
    if os.path.isdir(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for file in files:
            if not file.endswith(".hdf5"):
                continue
            file = os.path.join(path, file)
            process_file(file)
    elif os.path.isfile(path):
        if not path.endswith(".hdf5"):
            hanlde_error("Not .hdf5 has provided")
        process_file(path);
    else:
        handle_error("wtf? path is not file and is not dir")