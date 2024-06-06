import sys
import os

def demo_sys():
    # print(sys.path)
    for path in sys.path:
        print(path)

    for index, arg in enumerate(sys.argv):
        print(f"Argument {index}: {arg}")

    print(sys.version)

# int main(int argc, char* argv)


def demo_os():
    current_dir = os.getcwd()
    print(current_dir)

    new_dir = os.path.join(current_dir, 'demo_dir')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\nDirectory 'demo_dir' created at {new_dir}")
    else:
        print(f"\nDirectory 'demo_dir' already present at {new_dir}")

    for item in os.listdir(current_dir):
        print("\t", item)

    new_file_path = os.path.join(new_dir, 'demo_file.txt')
    # fl = open(new_file_path, 'w')
    # fl.write("This is a demo file.")
    # fl.close()

    with open(new_file_path, 'w') as fl:
        fl.write("This is a demo file.")

    if os.path.exists(new_file_path):
        print(f"File has been created at {new_file_path}")

    os.remove(new_file_path)
    os.rmdir(new_dir)

# demo_sys()
demo_os()