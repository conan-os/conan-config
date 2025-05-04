import os

CONAN_PROFILES = "/usr/conan_profile"


def deploy(graph, output_folder, **kwargs):
    for name, dep in graph.root.conanfile.dependencies.items():
        print(dep.package_folder)
        for item in os.listdir(os.path.join(dep.package_folder, "bin")):
            os.symlink(os.path.join(dep.package_folder, "bin", item),
                       os.path.join(CONAN_PROFILES, "bin", item))
